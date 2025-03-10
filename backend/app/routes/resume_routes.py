from flask import Blueprint, request, jsonify
from app.services.resume_parser import parse_resume
from app.services.ai_analysis import analyze_resume
from bson import ObjectId
from app import mongo
import os
resume_bp = Blueprint("resume", __name__)

UPLOAD_FOLDER = "uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # ✅ Ensure 'uploads/' directory exists

@resume_bp.route("/upload", methods=["POST"])
def upload_resume():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)  # Save uploaded file

    text = parse_resume(file_path)

    if not text:
        return jsonify({"error": "Could not parse resume"}), 500

    resume_data = {
        "filename": file.filename,
        "text": text
    }

    # Insert into MongoDB and get the ID
    inserted_id = mongo.db.resumes.insert_one(resume_data).inserted_id

    # Convert ObjectId to string
    resume_data["_id"] = str(inserted_id)

    return jsonify({"message": "Resume uploaded successfully", "data": resume_data}), 200


@resume_bp.route("/test", methods=["GET"])
def test_resume_processing():
    """Test route to process a predefined resume."""
    
    # Fix test file path (ensure correct directory)
    test_resume_path = os.path.join(os.path.dirname(__file__), "test_files/test_resume.pdf")

    if not os.path.exists(test_resume_path):
        return jsonify({"error": "Test resume file not found", "path_checked": test_resume_path}), 404

    # Extract text from resume
    text = parse_resume(test_resume_path)
    
    if not text:
        return jsonify({"error": "Failed to extract text from test resume"}), 500

    # Analyze the extracted text using AI
    feedback = analyze_resume(text)

    return jsonify({
        "message": "Test resume processed successfully",
        "extracted_text": text[:500],  # Show only first 500 chars for readability
        "feedback": feedback
    }), 200