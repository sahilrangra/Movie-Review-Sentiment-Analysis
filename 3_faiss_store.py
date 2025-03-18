import faiss
import numpy as np

# Load embeddings
embeddings = np.load("movie_embeddings_100.npy")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index
faiss.write_index(index, "movie_index_100.faiss")

print("✅ FAISS index saved as movie_index_100.faiss")
