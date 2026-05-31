import chromadb
from embeddings import get_embedding

#creating a ChromaDB client
client=chromadb.Client()

#creating a collection named "fashion_items"
collection=client.create_collection(name="fashion_items")

# Sample fashion items
items = [
    {
        "id": "item_001",
        "text": "jacket navy blazer slim fit notch lapel women summer",
        "metadata": {"category": "jacket", "color": "navy", "season": "summer"}
    },
    {
        "id": "item_002", 
        "text": "dress pink floral maxi bohemian women summer",
        "metadata": {"category": "dress", "color": "pink", "season": "summer"}
    },
    {
        "id": "item_003",
        "text": "jacket black leather oversized unisex winter",
        "metadata": {"category": "jacket", "color": "black", "season": "winter"}
    }
]

# Store each item
for item in items:
    vector = get_embedding(item["text"])
    collection.add(
        ids=[item["id"]],
        embeddings=[vector],
        metadatas=[item["metadata"]]
    )

print("✅ 3 fashion items stored in ChromaDB")

def search_similar(query: str,n_results: int=2):
    query_vector=get_embedding(query)

    results=collection.query(
        query_embeddings=[query_vector],
        n_results=n_results
    )
    return results
if __name__ == "__main__":
    results = search_similar("navy jacket slim fit")
    
    print("Search Results:")
    for i, metadata in enumerate(results["metadatas"][0]):
        print(f"Result {i+1}: {metadata}")
        print(f"Distance: {results['distances'][0][i]:.3f}")
        print("---")