import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/resume_db")
    UPLOAD_FOLDER = "uploads/"
    ALLOWED_EXTENSIONS = {"pdf", "docx"}
