import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR / "scripts"))

from query_vector_index import query

PROMPT_FILE = BASE_DIR / "prompts" / "career_explainer.txt"

# -------------------------------
# LLM CALL (UTF-8 SAFE)
# -------------------------------
def call_ollama(prompt, model="gemma:2b"):
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode("utf-8", errors="ignore").strip()

# -------------------------------
# INTENT EXTRACTION
# -------------------------------
def extract_intent(question):
    q = question.lower()

    INTENT_KEYWORDS = {
        "doctor": ["doctor", "medical", "mbbs"],
        "lawyer": ["lawyer", "law", "llb"],
        "data_scientist": ["data scientist", "data"],
        "engineer": ["engineer", "engineering"],
        "pilot": ["pilot", "aviation"],
    }

    for intent, keywords in INTENT_KEYWORDS.items():
        if any(k in q for k in keywords):
            return intent

    return None

# -------------------------------
# STRICT PATH FILTERING
# -------------------------------
def filter_paths_by_intent(intent, paths):
    if intent is None:
        return []

    INTENT_MATCH = {
        "doctor": ["JOB_MEDICAL_DOCTOR", "PROGRAM_MBBS"],
        "lawyer": ["JOB_LAWYER", "PROGRAM_LLB"],
        "data_scientist": ["JOB_DATA_SCIENTIST"],
        "engineer": ["ENGINEER"],
    }

    required_tokens = INTENT_MATCH.get(intent, [])
    filtered = []
    seen = set()

    for p in paths:
        parts = p["path_text"]

        joined = " ".join(parts)

        if any(token in joined for token in required_tokens):
            key = tuple(parts)
            if key not in seen:
                seen.add(key)
                filtered.append(p)

    return filtered

# -------------------------------
# GROUNDED ANSWER (NO LLM FACTS)
# -------------------------------
def build_grounded_answer(paths):
    if not paths:
        return (
            "Based on available data, there is no confirmed career path "
            "for this goal in the current system."
        )

    lines = ["Based on available data, the confirmed paths are:\n"]

    for p in paths:
        program, job, employer, region = p["path_text"][:4]
        lines.append(
            f"- Studying {program} can lead to {job} roles at "
            f"{employer} in {region}."
        )

    lines.append("\nNo additional details are available in the current data.")
    return "\n".join(lines)

# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    question = input("Ask a question: ")

    intent = extract_intent(question)

    retrieved_paths = query(question, k=5)
    relevant_paths = filter_paths_by_intent(intent, retrieved_paths)

    answer = build_grounded_answer(relevant_paths)

    print("\nLLM Answer:\n")
    print(answer)
