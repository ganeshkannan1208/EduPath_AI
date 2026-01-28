import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RAG_FILE = BASE_DIR / "outputs" / "rag_paths.jsonl"
INDEX_DIR = BASE_DIR / "vector_store"
INDEX_DIR.mkdir(exist_ok=True)

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

texts = []
metadata = []

with open(RAG_FILE, "r", encoding="utf-8") as f:
    for line in f:
        obj = json.loads(line)
        texts.append(" ".join(obj["path_text"]) + " " + obj["metadata"]["explanation"])
        metadata.append(obj)

print(f"Loaded {len(texts)} RAG paths")

# Generate embeddings
embeddings = model.encode(texts, convert_to_numpy=True, show_progress_bar=True)

# Build FAISS index
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(embeddings)

# Save
faiss.write_index(index, str(INDEX_DIR / "paths.index"))
np.save(INDEX_DIR / "paths_embeddings.npy", embeddings)

with open(INDEX_DIR / "paths_metadata.json", "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)

print("✅ Vector index built and saved")
