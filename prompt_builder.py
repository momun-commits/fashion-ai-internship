def build_sd_prompt(fashion_request: dict) -> dict:

    color = fashion_request["color"]
    style = fashion_request["style"]
    garment = fashion_request["garment_type"]

    positive = f"A {style} {color} {garment}"

    if fashion_request.get("gender"):
        positive += f" for {fashion_request['gender']}"

    if fashion_request.get("season"):
        positive += f", {fashion_request['season']}"

    # ---------- WEEK 4 ADDITION ----------
    if fashion_request.get("brand_prompt"):
        positive += ", " + fashion_request["brand_prompt"]
    # -------------------------------------

    positive += ", flat lay product photography, overhead shot, clean white background, commercial fashion, garment only, highly detailed, high quality"

    negative = "blurry, low quality, bad lighting, background clutter, low resolution"

    return {
        "positive": positive,
        "negative": negative
    }

if __name__ == "__main__":
    test = {
        "color": "navy",
        "style": "minimalist",
        "garment_type": "jacket",
        "gender": "women",
        "season": "autumn"
    }
    
    result = build_sd_prompt(test)
    print("Positive:", result["positive"])
    print("Negative:", result["negative"])

    