# Week 5 Report – Intelligent Fashion Recommendation (RAG)

## Objective

Develop a semantic fashion recommendation system capable of retrieving similar fashion products using vector embeddings and ChromaDB.

## Work Completed

### 1. Fashion Knowledge Base

Created a fashion knowledge database containing fashion descriptions and metadata including:

* Brand
* Category
* Color
* Season

### 2. Embedding Generation

Implemented semantic text embeddings using the Sentence Transformers model:

all-MiniLM-L6-v2

This converts fashion descriptions into numerical vectors.

### 3. Vector Database

Used ChromaDB to store

* Embeddings
* Documents
* Metadata

allowing efficient semantic retrieval.

### 4. Similarity Search

Implemented nearest-neighbor search using vector similarity.

Example Query

Luxury navy jacket

Example Recommendation

* Gucci luxury embroidered navy jacket
* Nike athletic navy jacket

### 5. Recommendation Engine

Built a recommendation pipeline that:

* Accepts user query
* Generates embedding
* Searches ChromaDB
* Returns the most similar fashion items

## Technologies Used

* Python
* Sentence Transformers
* ChromaDB
* Vector Embeddings
* Semantic Search

## Outcome

Successfully implemented an intelligent fashion recommendation pipeline using Retrieval Augmented Generation (RAG) concepts.
