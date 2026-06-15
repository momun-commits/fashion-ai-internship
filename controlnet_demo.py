from huggingface_hub import InferenceClient
import os

client = InferenceClient(api_key=os.getenv("HF_TOKEN"))

# UNCONTROLLED — vague prompt, no shape guidance
print("Generating uncontrolled...")
uncontrolled = client.text_to_image(
    prompt="a jacket, fashion photography",
    negative_prompt="blurry, low quality, mannequin, person",
    model="black-forest-labs/FLUX.1-schnell"
)
uncontrolled.save("uncontrolled.png")
print("✅ saved uncontrolled.png")

# CONTROLLED — detailed prompt simulating sketch guidance
print("Generating controlled...")
controlled = client.text_to_image(
    prompt="a minimalist white cropped jacket, flat lay product photography, clean white background, precise silhouette, structured shoulders",
    negative_prompt="blurry, low quality, mannequin, person",
    model="black-forest-labs/FLUX.1-schnell"
)
controlled.save("controlled.png")
print("✅ saved controlled.png")

# SKETCH-TO-DESIGN — prompt derived from actual edge map of jacket
print("Generating sketch-to-design...")
sketch_design = client.text_to_image(
    prompt="a minimalist navy wool jacket, flat lay product photography, clean white background, structured silhouette, hooded, professional fashion shoot, high quality",
    negative_prompt="blurry, low quality, mannequin, person, leaves, accessories",
    model="black-forest-labs/FLUX.1-schnell"
)
sketch_design.save("sketch_to_design.png")
print("✅ saved sketch_to_design.png")