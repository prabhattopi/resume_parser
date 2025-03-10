from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# ✅ Check if CUDA is available
device = "cuda" if torch.cuda.is_available() else "cpu"

# ✅ Use a lightweight model (distilgpt2)
MODEL_NAME = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16 if device == "cuda" else torch.float32).to(device)

def generate_chat_response(user_input, resume_text=""):
    """
    Generates AI-based responses using distilgpt2 (small & fast).
    Uses resume text for better context-aware responses.
    """
    prompt = f"""
    You are an AI Career Coach providing expert career guidance. 
    
    Resume Summary:
    {resume_text[:400]}... (truncated for processing)

    User's Question:
    {user_input}

    Provide a detailed, structured, and actionable career recommendation.
    """

    inputs = tokenizer(prompt, return_tensors="pt").to(device)  # ✅ Automatically selects CPU or GPU

    output = model.generate(
        **inputs,
        max_new_tokens=80,
        do_sample=True,
        temperature=0.8,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.1,
        eos_token_id=tokenizer.eos_token_id
    )

    response_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # ✅ Extract Only AI's Response
    ai_response = response_text.split("User's Question:")[-1].strip()

    return ai_response
