import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_collection(name="functions")

def retrieve_function(user_query):
    """Retrieve the best-matching function for a given user query."""
    query_embedding = model.encode(user_query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )
    
    if results["ids"]:
        function_name = results["ids"][0][0]
        return function_name
    return None

# Test the retriever
if __name__ == "__main__":
    user_query = "Launch Google Chrome"
    function_name = retrieve_function(user_query)
    print(f"🔍 Matched function: {function_name}")
