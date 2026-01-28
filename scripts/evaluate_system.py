import json
from pathlib import Path
from ask_llm import extract_intent, filter_paths_by_intent, build_grounded_answer
from query_vector_index import query

BASE_DIR = Path(__file__).resolve().parents[1]
TEST_FILE = BASE_DIR / "evaluation" / "test_questions.json"

tests = json.load(open(TEST_FILE, encoding="utf-8"))

results = {
    "total": 0,
    "answerable": 0,
    "correct_retrieval": 0,
    "correct_refusal": 0
}

for t in tests:
    results["total"] += 1
    intent = extract_intent(t["question"])
    retrieved = query(t["question"], k=5)
    filtered = filter_paths_by_intent(intent, retrieved)

    if t["answerable"]:
        results["answerable"] += 1
        if any(
            any(ep in " ".join(p["path_text"]) for ep in t["expected_paths"])
            for p in filtered
        ):
            results["correct_retrieval"] += 1
    else:
        if not filtered:
            results["correct_refusal"] += 1

print("\n📊 Evaluation Results")
print("-------------------")
print(f"Total Questions: {results['total']}")
print(f"Answerable Questions: {results['answerable']}")
print(f"Correct Retrievals: {results['correct_retrieval']}")
print(f"Correct Refusals: {results['correct_refusal']}")
