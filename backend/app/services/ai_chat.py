from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch
import os
from typing import Optional

# ✅ **Model Configuration**
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN", "your_token_here")

# ✅ **Device Selection & Offloading Prevention**
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ✅ **Proper Quantization Configuration**
bnb_config = None  # Default
if torch.cuda.is_available():
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,  # ✅ Enables efficient 4-bit inference
        bnb_4bit_use_double_quant=True,  # ✅ Optimizes quantization
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16
    )

# ✅ **Ensure Efficient Model Loading**
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=HUGGINGFACE_TOKEN)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        quantization_config=bnb_config if DEVICE.type == "cuda" else None,
        device_map="auto",  # ✅ Automatically maps model to available device
        torch_dtype=torch.float16 if DEVICE.type == "cuda" else torch.float32
    )
    print(f"✅ Model successfully loaded on {DEVICE}")

except Exception as e:
    raise RuntimeError(f"❌ Model loading failed: {str(e)}")


def generate_chat_response(
    user_input: str,
    resume_text: Optional[str] = None,
    max_new_tokens: int = 200
) -> str:
    """
    Generates career advice using TinyLlama-1.1B (4-bit optimized).

    Args:
        user_input: User's career-related question.
        resume_text: Resume summary to provide context (optional).
        max_new_tokens: The max number of tokens for the response.

    Returns:
        A structured career advice response.
    """
    try:
        # ✅ **Resume Truncation for Efficient Token Usage**
        safe_resume_text = resume_text[:800] if resume_text else "No resume provided."

        # ✅ **Optimized Prompt Format for Better Responses**
        prompt = f"""<|system|>
You are a professional AI career advisor with expertise in industry trends, career planning, and job transitions.

Resume Summary: {safe_resume_text}
Question: {user_input}</s>
<|user|>
{user_input}</s>
<|assistant|>
"""

        # ✅ **Safe Tokenization with Length Control**
        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            max_length=1024,
            truncation=True
        ).to(DEVICE)

        # ✅ **Optimized Generation Parameters**
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=0.7,
            top_k=50,
            top_p=0.92,
            repetition_penalty=1.15,
            do_sample=True
        )

        # ✅ **Extract AI's Response & Clean Output**
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        assistant_start = response.find("<|assistant|>")
        if assistant_start != -1:
            response = response[assistant_start + len("<|assistant|>"):].strip()

        return response if response else "Could you provide more details? I'm here to assist!"

    except Exception as e:
        return f"❌ Error generating response: {str(e)}"



