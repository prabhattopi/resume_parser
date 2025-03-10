# 🚀 AI-Powered Resume Review & Career Coach

This project is an **AI-powered resume review and career guidance platform** built using **Flask (Python backend) and React (frontend)**. The system allows users to upload their resumes, get AI-driven insights, and receive career recommendations via a chat-based interface.

---

## 📌 Features

✅ **Resume Upload** – Users can upload PDFs for AI analysis.
✅ **AI-Powered Resume Analysis** – Extracts skills, experience, and education from the resume.
✅ **Career Coaching Chatbot** – AI-driven responses for career advice.
✅ **REST API** – Flask-based backend with MongoDB integration.
✅ **Secure & Scalable** – Supports authentication and modular API design.
✅ **Docker Support** – Easily deploy using Docker and Render.

---

## 🛠️ Tech Stack

### **Backend (Flask & AI)**
- **Flask** – Python web framework
- **MongoDB** – NoSQL database for storing resumes
- **Transformers (Hugging Face)** – AI model for resume analysis & chat
- **facebook/opt-1.3b** – AI model for career coaching
- **PyTorch** – AI inference & model loading
- **Gunicorn** – Production-ready WSGI server

### **Frontend (React & TypeScript)**
- **React** – User interface
- **TypeScript** – Type-safe development
- **TailwindCSS** – Styling
- **Axios** – API communication

### **Deployment & DevOps**
- **Docker** – Containerized deployment
- **Render** – Free-tier hosting support
- **Hugging Face Token** – Secure model authentication

---

## 🚀 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
# Clone the project
git clone https://github.com/prabhattopi/resume_parser.git
cd resume-review-ai
```

### **2️⃣ Backend Setup (Flask & MongoDB)**
#### **Install Dependencies**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

#### **Set Up Environment Variables**
Create a `.env` file inside `backend/` and add:
```
FLASK_ENV=production
FLASK_APP=main.py
MONGO_URI=mongodb+srv://your_mongo_uri
HUGGINGFACE_TOKEN=your_huggingface_token
```

#### **Run Flask API**
```bash
python main.py
```

### **3️⃣ Frontend Setup (React & TypeScript)**
#### **Install Dependencies**
```bash
cd frontend
npm install
```

#### **Run Development Server**
```bash
npm run dev
```

---

## 🐳 **Run with Docker**
```bash
# Build and run the backend in Docker
docker build -t resume-review-backend ./backend
docker run -p 5000:5000 resume-review-backend

# Build and run the frontend in Docker
docker build -t resume-review-frontend ./frontend
docker run -p 3000:3000 resume-review-frontend
```

---

## 📡 **API Endpoints**

### **Resume Upload & Analysis**
#### ➤ **Upload Resume**
```http
POST /api/resume/upload
```
**Payload:** (multipart form-data)
```json
{ "file": "resume.pdf" }
```
**Response:**
```json
{
  "resume_id": "65ff6c8b92e4a8c9f7d4e80b",
  "extracted_text": "Resume content here...",
  "feedback": "Improve your LinkedIn profile."
}
```

#### ➤ **Get Resume Feedback**
```http
GET /api/analysis/feedback/{resume_id}
```

### **Career Coaching Chatbot**
#### ➤ **Ask Career Advice**
```http
POST /api/analysis/chat
```
**Payload:**
```json
{
  "message": "What should I do for my next career phase?",
  "resume_id": "65ff6c8b92e4a8c9f7d4e80b"
}
```
**Response:**
```json
{
  "reply": "Consider advancing your skills in backend development with AWS and contributing to open-source projects."
}
```

---

## 🛠 **Project Structure**
```
resume-review-ai/
│── backend/                # Flask API
│   │── app/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── models/
│   │── config.py
│   │── requirements.txt
│   │── main.py
│
│── frontend/               # React + TypeScript
│   │── src/
│   │   ├── components/
│   │   ├── pages/
│   │── package.json
│
│── docker-compose.yml      # Docker configuration
│── README.md               # Documentation
```

---

## 📌 **Deployment on Render**
### **1️⃣ Backend Deployment**
1. Push to GitHub
2. Go to **Render → New Web Service**
3. Select **Python 3.10** runtime
4. Set environment variables:
```
FLASK_ENV=production
MONGO_URI=mongodb+srv://your_mongo_uri
HUGGINGFACE_TOKEN=your_huggingface_token
```
5. **Start Command:**
```bash
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

### **2️⃣ Frontend Deployment**
1. Go to **Render → New Static Site**
2. Set **Build Command:**
```bash
npm run build
```
3. Set **Publish Directory:**
```
dist/
```

---

## 👨‍💻 **Contributing**
PRs are welcome! Feel free to submit issues and feature requests.

---

## 📜 **License**
MIT License

---

## 🎯 **Next Steps**
🔹 **Improve AI model performance** with more resume-specific fine-tuning.  
🔹 **Add authentication** for better security.  
🔹 **Enhance UI/UX** with real-time AI suggestions.  

🚀 **Enjoy using AI for career growth!** 🎯

