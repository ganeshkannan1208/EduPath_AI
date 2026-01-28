import json

ranked_paths = json.load(open("outputs/ranked_paths.json", encoding="utf-8"))
out = []

for i, p in enumerate(ranked_paths):
    path_text = p["path"]
    eligibility = p.get("eligibility", 0.0)  # Use .get() to avoid KeyError
    explanation = (
        f"If a student follows the path {path_text}, "
        f"they can expect eligibility score {eligibility}, "
        f"salary score {p.get('salary', 0.0)}, and demand score {p.get('demand', 0.0)}."
    )

    if len(p["path"]) >= 3:
        rag_entry = {
            "path_id": f"PATH_{i+1}",
            "path_text": path_text,
            "structured_path": p["path"],
            "score": p["final_score"],
            "metadata": {
                "program": p["path"][0],
                "job": p["path"][1],
                "employer": p["path"][2],
                "region": p["path"][3],
                "salary_p75": p.get("components", {}).get("S3_salary", 0.0),
                "demand_2026": p.get("components", {}).get("S4_demand", 0.0),
                "eligibility": eligibility,
                "skill_gap": p.get("components", {}).get("S6_skill_gap", 0.0),
                "explanation": explanation
            }
        }
    else:
        # Handle the case when the list does not have enough elements
        print(f"Skipping path {i+1} due to insufficient information")
        continue

    out.append(rag_entry)

with open("outputs/rag_paths.jsonl", "w", encoding="utf-8") as f:
    for o in out:
        f.write(json.dumps(o) + "\n")

print("✅ RAG paths materialized → outputs/rag_paths.jsonl")