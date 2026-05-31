def process_fashion_item(item: dict)->dict:
    #1.Handle missing fields with defaults
    if item["color"] is None:
        item["color"]="unknown"
    if item["season"] is None:
        item["season"]="unknown"
    if item["gender"] is None:
        item["gender"] = "unspecified"
    
    #2.Normalize text fields to lowercase
    item["category"] = item["category"].lower()
    item["attributes"] = [x.lower() for x in item["attributes"]]
    item["season"] = item["season"].lower()
    item["gender"] = item["gender"].lower()
    item["description"] = item["description"].lower()
    item["color"] = item["color"].lower()
    #3.Remove duplicate attributes
    item["attributes"] = list(set(item["attributes"]))
    #4.Return cleaned item
    return item


def process_fashion_dataset(item: list)->list:
    return [process_fashion_item(x) for x in item]

dataset = [
    {
        "image": "jacket_001.jpg",
        "category": "Outerwear",
        "attributes": ["Slim Fit", "slim fit"],
        "gender": None,
        "season": None,
        "color": "Navy",
        "description": "A Navy Blazer"
    },
    {
        "image": "dress_001.jpg",
        "category": "DRESS",
        "attributes": ["Floral", "MAXI", "floral"],
        "gender": "Women",
        "season": "Summer",
        "color": "Pink",
        "description": "A Floral Summer Dress"
    }
]

cleaned_dataset = process_fashion_dataset(dataset)
for item in cleaned_dataset:
    print(item)
    print("---")

def item_to_text(item: dict)->str:
    attributes_text=", ".join(item["attributes"])
    return f"{item['category']} {item['color']} {item['description']} {attributes_text} {item['gender']} {item['season']}"
test_item = {
    "category": "jacket",
    "attributes": ["slim fit", "notch lapel"],
    "color": "navy",
    "description": "a navy blazer",
    "gender": "women",
    "season": "summer"
}

print(item_to_text(test_item))