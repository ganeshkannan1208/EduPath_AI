import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
INDEX_DIR = BASE_DIR / "vector_store"

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index(str(INDEX_DIR / "paths.index"))
embeddings = np.load(INDEX_DIR / "paths_embeddings.npy")
metadata = json.load(open(INDEX_DIR / "paths_metadata.json", encoding="utf-8"))

def query(text, k=3):
    q_emb = model.encode([text], convert_to_numpy=True)
    D, I = index.search(q_emb, k)

    results = []
    for idx in I[0]:
        results.append(metadata[idx])
    return results

if __name__ == "__main__":
    q = input("Enter your question: ")
    results = query(q)

    print("\nTop Matches:\n")
    for r in results:
        print(f"- {r['path_text']} | score={r['score']}")
