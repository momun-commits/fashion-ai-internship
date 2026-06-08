from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

# Lazy loading - model loads only when first used
_model = None
_processor = None

def _load_model():
    global _model, _processor
    if _model is None:
        _model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        _processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def get_clip_score(image_path: str, prompt: str) -> float:
    _load_model()
    
    image = Image.open(image_path)
    
    inputs = _processor(
        text=[prompt],
        images=image,
        return_tensors="pt",
        padding=True
    )
    
    outputs = _model(**inputs)
    score = outputs.logits_per_image[0][0].item()
    
    return score

def interpret_score(score: float) -> str:
    if score >= 35:
        return "Excellent"
    elif score >= 30:
        return "Good"
    elif score >= 25:
        return "Average"
    else:
        return "Poor"