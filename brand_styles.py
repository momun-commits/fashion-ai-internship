STYLE_PRESETS = {
    "nike": {
        "style": "minimalist athletic sportswear",
        "prompt": "clean sportswear, performance fabric, modern athletic fashion"
    },
    "zara": {
        "style": "casual european",
        "prompt": "casual european street fashion, neutral colors, elegant everyday wear"
    },
    "gucci": {
        "style": "luxury designer",
        "prompt": "luxury designer fashion, premium fabric, embroidery, high-end editorial"
    },
    "hm": {
        "style": "affordable casual",
        "prompt": "simple casual fashion, modern everyday clothing, comfortable style"
    }
}


def apply_brand_style(request):
    brand = request.get("brand", "").lower()

    if brand in STYLE_PRESETS:
        request["style"] = STYLE_PRESETS[brand]["style"]
        request["brand_prompt"] = STYLE_PRESETS[brand]["prompt"]
    else:
        request["brand_prompt"] = ""

    return request