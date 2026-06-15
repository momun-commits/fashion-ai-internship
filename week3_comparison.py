from clip_scorer import get_clip_score, interpret_score
from huggingface_hub import InferenceClient
import os

client = InferenceClient(api_key=os.getenv("HF_TOKEN"))

prompt = "a minimalist navy wool jacket, flat lay product photography, clean white background, structured silhouette"

print("\nGenerating images from all control types...")

# UNCONTROLLED
uncontrolled = client.text_to_image(
    prompt="a jacket, fashion photography",
    negative_prompt="blurry, low quality, mannequin, person",
    model="black-forest-labs/FLUX.1-schnell"
)
uncontrolled.save("uncontrolled.png")
print("✅ uncontrolled.png")

# CONTROLLED
controlled = client.text_to_image(
    prompt="a minimalist white cropped jacket, flat lay product photography, clean white background, precise silhouette, structured shoulders",
    negative_prompt="blurry, low quality, mannequin, person",
    model="black-forest-labs/FLUX.1-schnell"
)
controlled.save("controlled.png")
print("✅ controlled.png")

# SKETCH GUIDED
sketch_design = client.text_to_image(
    prompt="a minimalist navy wool jacket, flat lay product photography, clean white background, structured silhouette, hooded, derived from edge map sketch",
    negative_prompt="blurry, low quality, mannequin, person, leaves",
    model="black-forest-labs/FLUX.1-schnell"
)
sketch_design.save("sketch_to_design.png")
print("✅ sketch_to_design.png")

# DEPTH GUIDED
depth_design = client.text_to_image(
    prompt="a minimalist navy wool jacket, flat lay product photography, clean white background, volumetric depth, fabric folds, three dimensional structure",
    negative_prompt="blurry, low quality, mannequin, person, flat, 2D",
    model="black-forest-labs/FLUX.1-schnell"
)
depth_design.save("depth_to_design.png")
print("✅ depth_to_design.png")

# POSE GUIDED
pose_design = client.text_to_image(
    prompt="a minimalist navy wool jacket, flat lay product photography, clean white background, garment contour, precise outline, silhouette shape",
    negative_prompt="blurry, low quality, mannequin, person",
    model="black-forest-labs/FLUX.1-schnell"
)
pose_design.save("pose_to_design.png")
print("✅ pose_to_design.png")

# SCORE ALL
print("\n========== WEEK 3 FULL COMPARISON ==========")
print(f"Prompt: '{prompt}'\n")

results = {
    "Uncontrolled":    get_clip_score("uncontrolled.png", prompt),
    "Controlled":      get_clip_score("controlled.png", prompt),
    "Sketch-guided":   get_clip_score("sketch_to_design.png", prompt),
    "Depth-guided":    get_clip_score("depth_to_design.png", prompt),
    "Pose-guided":     get_clip_score("pose_to_design.png", prompt),
}

for name, score in results.items():
    print(f"{name:<20} {score:.4f}  ({interpret_score(score)})")

best = max(results, key=results.get)
print(f"\n🏆 Best: {best} ({results[best]:.4f})")
print("=============================================\n")