from flask import Blueprint, request, jsonify
from app.services.ai_analysis import analyze_resume
from bson import ObjectId  # ✅ Import ObjectId to handle MongoDB IDs
from app.services.ai_chat import generate_chat_response
from app import mongo

analysis_bp = Blueprint("analysis", __name__)

@analysis_bp.route("/feedback/<resume_id>", methods=["GET"])
def get_resume_feedback(resume_id):
    """Fetch resume feedback using MongoDB ID."""
    
    # Try to convert `resume_id` to `ObjectId`, otherwise fallback to string search
    object_id = None
    if ObjectId.is_valid(resume_id):  # ✅ Check if the ID is a valid MongoDB ObjectId
        object_id = ObjectId(resume_id)

    # Try searching by ObjectId first, then fallback to string ID search
    resume = mongo.db.resumes.find_one({"_id": object_id}) or mongo.db.resumes.find_one({"_id": resume_id})

    if not resume:
        return jsonify({"error": "Resume not found"}), 404

    feedback = analyze_resume(resume["text"])

    return jsonify({"resume_id": str(resume["_id"]), "feedback": feedback}), 200



@analysis_bp.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip()
    resume_id = request.json.get("resume_id", "")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    # ✅ Retrieve resume text if resume_id is provided
    resume_text = ""
    if resume_id:
        try:
            object_id = ObjectId(resume_id) if ObjectId.is_valid(resume_id) else resume_id
            resume = mongo.db.resumes.find_one({"_id": object_id})
            if resume:
                resume_text = resume.get("text", "")
        except Exception as e:
            return jsonify({"error": "Invalid resume ID format"}), 400

    try:
        reply = generate_chat_response(user_input, resume_text)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": f"AI response error: {str(e)}"}), 500
