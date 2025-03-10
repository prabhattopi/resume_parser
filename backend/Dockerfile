# ✅ Use Python 3.10 as the base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Install spaCy and download language model
RUN pip install spacy
RUN python -m spacy download en_core_web_sm

# ✅ Install AI dependencies
RUN pip install torch transformers accelerate

# ✅ Pre-load Mistral-7B model (avoids runtime delays)
RUN python -c "from transformers import AutoModelForCausalLM, AutoTokenizer; \
    AutoTokenizer.from_pretrained('mistralai/Mistral-7B-Instruct'); \
    AutoModelForCausalLM.from_pretrained('mistralai/Mistral-7B-Instruct', torch_dtype='auto')"

# Expose Flask API port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=main.py
ENV FLASK_ENV=production

# ✅ Use Gunicorn for production deployment
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
