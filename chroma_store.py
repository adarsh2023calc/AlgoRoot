import chromadb
import json
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="functions")

# Load function metadata
with open("functions_metadata.json", "r") as f:
    functions = json.load(f)

# Store function descriptions in ChromaDB
for function_name, description in functions.items():
    embedding = model.encode(description).tolist()
    collection.add(
        ids=[function_name], 
        embeddings=[embedding], 
        metadatas=[{"description": description}]
    )

print("✅ Function embeddings stored successfully in ChromaDB.")
