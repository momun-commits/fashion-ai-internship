print("VECTOR STORE STARTED")
import chromadb
from embeddings import get_embedding

# Create ChromaDB client and collection
client = chromadb.PersistentClient(path="./fashion_db")
try:
    client.delete_collection("fashion_items")
except:
    pass

collection = client.get_or_create_collection("fashion_items")


def seed_data():
    print("Starting seed_data...")
    """
    Add sample fashion items to the collection.
    Call this only once when needed.
    """

    items = [
    {
        "id": "item_001",
        "text": "Nike navy athletic sports jacket for women",
        "metadata": {
            "brand": "Nike",
            "category": "Jacket",
            "color": "Navy",
            "season": "Autumn"
        }
    },

    {
        "id": "item_002",
        "text": "Gucci luxury embroidered navy jacket for women",
        "metadata": {
            "brand": "Gucci",
            "category": "Jacket",
            "color": "Navy",
            "season": "Autumn"
        }
    },

    {
        "id": "item_003",
        "text": "Zara casual beige oversized blazer",
        "metadata": {
            "brand": "Zara",
            "category": "Blazer",
            "color": "Beige",
            "season": "Spring"
        }
    },

    {
        "id": "item_004",
        "text": "H&M everyday black hoodie",
        "metadata": {
            "brand": "H&M",
            "category": "Hoodie",
            "color": "Black",
            "season": "Winter"
        }
    },

    {
        "id": "item_005",
        "text": "Nike black running hoodie",
        "metadata": {
            "brand": "Nike",
            "category": "Hoodie",
            "color": "Black",
            "season": "Winter"
        }
    }
]
    print("Checking collection...")
    existing = collection.count()

    if existing > 0:
        print("Collection already contains data.")
        return

    for item in items:
        print("Embedding:", item["id"])
        vector = get_embedding(item["text"])

        collection.add(
            ids=[item["id"]],
            documents=[item["text"]],
            embeddings=[vector],
            metadatas=[item["metadata"]]
        )

    print("Sample data added successfully.")


def search_similar(query: str, n_results: int = 2):
    query_vector = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_vector],
        n_results=n_results,
        include=["documents", "metadatas", "distances"]
)

    return results

print("__name__ =", __name__)

if __name__ == "__main__":
    seed_data()

    results = search_similar("luxury navy jacket")

    print("\nRecommended Fashion Items\n")

    for i in range(len(results["documents"][0])):

        print("=" * 50)
        print(f"Recommendation {i + 1}")

        print("Description :")
        print(results["documents"][0][i])

        print()

        print("Metadata :")
        print(results["metadatas"][0][i])

        print()

        print("Similarity :",
              round(1 - results["distances"][0][i], 3))