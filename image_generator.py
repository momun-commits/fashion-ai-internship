from dotenv import load_dotenv
load_dotenv()

from huggingface_hub import InferenceClient
from clip_scorer import get_clip_score, interpret_score
from prompt_builder import build_sd_prompt
import os

#Initializing the Hugging Face Inference Client with the API token
hf_token = os.getenv("HF_TOKEN")
client = InferenceClient(api_key=hf_token)

def generate_fashion_image(fashion_request: dict)->bytes:
    #Building the stable diffusion prompt using the fashion request
    prompts=build_sd_prompt(fashion_request)
    # Generating image
    image = client.text_to_image(
        prompt=prompts["positive"],
        negative_prompt=prompts["negative"],
        model="black-forest-labs/FLUX.1-schnell"
    )
    image_path = f"generated_{fashion_request['garment_type']}_{fashion_request['color']}.png"
    image.save(image_path)
    
    score = get_clip_score(image_path, prompts["positive"])
    quality = interpret_score(score)
    return {
        "image_path": image_path,
        "prompt": prompts["positive"],
        "clip_score": round(score, 2),
        "quality": quality
    }

#if __name__ == "__main__":
 #   test = {
  #      "color": "navy",
   #     "style": "minimalist",
    #    "garment_type": "jacket",
     #   "gender": "women",
      #  "season": "autumn"
    #}
    
    #image = generate_fashion_image(test)
    #image.save("test_generation.png")
    #print("--Image saved as test_generation.png--")

#if __name__ == "__main__":
 #   image = client.text_to_image(
  #      prompt="A minimalist navy jacket for women, autumn, fashion photography, 8k, sharp focus, professional editorial, clean white background, close up jacket shot, chest up, jacket only, no bottom garment, isolated garment, no pants",
   #     negative_prompt="blurry, low quality, bad lighting, background clutter, full body, pants, trousers, lower body, legs, bottom half, outfit, clothing below waist",
    #    model="black-forest-labs/FLUX.1-schnell")
    #image.save("test_b3.png")
    #print("✅ Saved test_b3.png")

#if __name__ == "__main__":
    #image = client.text_to_image(
     #   prompt="A minimalist navy jacket for women, autumn, flat lay product photography, overhead shot, clean white background, commercial fashion, jacket only",
      #  negative_prompt="blurry, low quality, bad lighting, background clutter, full body, pants, trousers, lower body, legs, bottom half, outfit, clothing below waist",
       # model="black-forest-labs/FLUX.1-schnell")
    #image.save("test_c.png")
    #print("✅ Saved test_c.png")

if __name__ == "__main__":
    test = {
        "color": "navy",
        "style": "minimalist",
        "garment_type": "jacket",
        "gender": "women",
        "season": "autumn"
    }
    result = generate_fashion_image(test)
    print(f"Image: {result['image_path']}")
    print(f"Prompt: {result['prompt']}")
    print(f"CLIP Score: {result['clip_score']}")
    print(f"Quality: {result['quality']}")

    print("HF_TOKEN found:", hf_token is not None)