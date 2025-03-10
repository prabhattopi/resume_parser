import spacy
import re

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Keywords to help extract job titles & skills dynamically
JOB_TITLE_KEYWORDS = ["developer", "engineer", "manager", "analyst", "consultant", "architect", "specialist"]
SKILL_CATEGORIES = ["programming language", "database", "cloud", "framework", "library", "technology"]

def extract_skills(text):
    """Dynamically extracts skills, tools, and programming languages from resume."""
    doc = nlp(text)
    extracted_skills = set()

    # Use NLP entities to extract skills
    for ent in doc.ents:
        if ent.label_ in ["ORG", "PRODUCT", "WORK_OF_ART", "FACILITY"]:  # Common labels for tech/tools
            extracted_skills.add(ent.text)

    # Regex-based skill extraction for common patterns
    tech_patterns = r"\b(JavaScript|Python|Java|C\+\+|C#|Go|Swift|Kotlin|Django|Flask|MongoDB|AWS|Docker|Kubernetes|React|Vue|Angular|Node.js|Express.js|PostgreSQL|MySQL|Redis)\b"
    matches = re.findall(tech_patterns, text, re.IGNORECASE)
    extracted_skills.update(matches)

    return list(extracted_skills)

def extract_experience(text):
    """Dynamically extracts experience-related information."""
    doc = nlp(text)
    experience = []

    for sent in doc.sents:
        for word in JOB_TITLE_KEYWORDS:
            if word in sent.text.lower():
                experience.append(sent.text.strip())

    return experience if experience else ["No clear job experience found."]

def analyze_resume(text):
    """
    Analyze the resume text to extract dynamic experience, skills, and generate tailored feedback.
    """
    skills = extract_skills(text)
    experience = extract_experience(text)

    feedback = {
        "strengths": skills,
        "experience": experience,
        "suggestions": []
    }

    # Tailored Recommendations Based on Missing Sections
    if not skills:
        feedback["suggestions"].append("Consider listing technical skills relevant to your role.")
    if not experience or experience == ["No clear job experience found."]:
        feedback["suggestions"].append("Add detailed work experience with job titles and responsibilities.")
    if "projects" not in text.lower():
        feedback["suggestions"].append("Consider adding personal or open-source projects to showcase expertise.")
    if "linkedin" not in text.lower():
        feedback["suggestions"].append("Include a LinkedIn profile link for better online presence.")

    return feedback
