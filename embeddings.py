from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

_model = None


def get_model():
    global _model

    if _model is None:
        print("Loading embedding model...")
        _model = SentenceTransformer("all-MiniLM-L6-v2")

    return _model


def get_embedding(text: str):
    model = get_model()
    embedding = model.encode(text)
    return embedding.tolist()


if __name__ == "__main__":

    text1 = "Nike navy athletic sports jacket"
    text2 = "Gucci luxury navy embroidered jacket"
    text3 = "Pink floral summer dress"

    vec1 = get_embedding(text1)
    vec2 = get_embedding(text2)
    vec3 = get_embedding(text3)

    print("Embedding length:", len(vec1))

    sim12 = cosine_similarity([vec1], [vec2])[0][0]
    sim13 = cosine_similarity([vec1], [vec3])[0][0]

    print("Jacket vs Jacket:", round(sim12,3))
    print("Jacket vs Dress :", round(sim13,3))