from dotenv import load_dotenv
import os

from huggingface_hub import InferenceClient
from clip_scorer import get_clip_score, interpret_score
from prompt_builder import build_sd_prompt

# Load environment variables
load_dotenv(dotenv_path=".env", override=True)

hf_token = os.getenv("HF_TOKEN")

print("HF_TOKEN loaded:", hf_token is not None)
print("Token prefix:", hf_token[:10] if hf_token else None)

if hf_token is None:
    raise ValueError("HF_TOKEN not found in .env file")

# Initialize Hugging Face Client
client = InferenceClient(api_key=hf_token)


def generate_fashion_image(fashion_request: dict):
    """
    Generate a fashion image with optional brand-specific styling.
    """

    brand = fashion_request.get("brand", "").lower()

    # -------- Week 4: Brand Style Switching --------
    if brand == "nike":
        fashion_request["style"] = "minimalist athletic sportswear"
        fashion_request["brand_prompt"] = (
            "clean sportswear, performance fabric, modern athletic fashion"
        )

    elif brand == "gucci":
        fashion_request["style"] = "luxury designer"
        fashion_request["brand_prompt"] = (
            "premium fabric, embroidery, luxury editorial"
        )

    elif brand == "zara":
        fashion_request["style"] = "casual european"
        fashion_request["brand_prompt"] = (
            "neutral colors, modern european fashion"
        )

    elif brand == "hm":
        fashion_request["style"] = "affordable casual"
        fashion_request["brand_prompt"] = (
            "comfortable everyday clothing"
        )

    else:
        fashion_request["brand_prompt"] = ""

    # Build prompt
    prompts = build_sd_prompt(fashion_request)

    # Generate image
    image = client.text_to_image(
        prompt=prompts["positive"],
        negative_prompt=prompts["negative"],
        model="black-forest-labs/FLUX.1-schnell"
    )

    # Save image
    image_path = (
        f"generated_{fashion_request['garment_type']}_"
        f"{fashion_request['color']}.png"
    )

    image.save(image_path)

    # Evaluate with CLIP
    score = get_clip_score(image_path, prompts["positive"])
    quality = interpret_score(score)

    return {
        "image_path": image_path,
        "prompt": prompts["positive"],
        "clip_score": round(score, 2),
        "quality": quality
    }


if __name__ == "__main__":

    test = {
        "brand": "gucci",
        "color": "navy",
        "style": "minimalist",
        "garment_type": "jacket",
        "gender": "women",
        "season": "autumn"
    }

    result = generate_fashion_image(test)

    print("\n========== RESULT ==========")
    print("Image:", result["image_path"])
    print("Prompt:", result["prompt"])
    print("CLIP Score:", result["clip_score"])
    print("Quality:", result["quality"])
    print("============================")