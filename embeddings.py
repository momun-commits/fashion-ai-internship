from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

_model = None

def get_model():
    global _model

    if _model is None:
        print("Loading embedding model...")
        _model = SentenceTransformer("all-MiniLM-L6-v2")

    return _model


def get_embedding(text: str) -> list:
    model = get_model()
    embedding = model.encode(text)
    return embedding.tolist()


if __name__ == "__main__":
    test_text = "jacket navy blazer slim fit notch lapel women summer"

    vector = get_embedding(test_text)

    print(f"Vector length: {len(vector)}")
    print(f"First 5 values: {vector[:5]}")

    text1 = "jacket navy blazer slim fit women summer"
    text2 = "jacket dark navy coat slim fit women winter"
    text3 = "floral pink dress maxi bohemian summer"

    vec1 = get_embedding(text1)
    vec2 = get_embedding(text2)
    vec3 = get_embedding(text3)

    sim_12 = cosine_similarity([vec1], [vec2])[0][0]
    sim_13 = cosine_similarity([vec1], [vec3])[0][0]

    print(f"Jacket vs Jacket similarity: {sim_12:.3f}")
    print(f"Jacket vs Dress similarity: {sim_13:.3f}")