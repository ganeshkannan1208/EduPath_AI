import json
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]
GRAPH_DIR = BASE_DIR / "graph"

nodes = json.load(open(GRAPH_DIR / "edu_nodes.json", encoding="utf-8"))
edges = json.load(open(GRAPH_DIR / "edu_edges.json", encoding="utf-8"))

node_ids = {n["id"]: n["type"] for n in nodes}

errors = []

# V1 — Referential Integrity
for i, e in enumerate(edges):
    if e["source"] not in node_ids:
        errors.append(f"[V1] Edge {i}: source not found → {e['source']}")
    if e["target"] not in node_ids:
        errors.append(f"[V1] Edge {i}: target not found → {e['target']}")

# V2 — Type Compatibility Rules
VALID_RULES = {
    ("Program", "leads_to", "Specialization"),
    ("Program", "leads_to", "Program"),
    ("Program", "requires", "Exam"),
    ("Specialization", "leads_to", "Job"),
    ("Job", "can_be_reached_from", "Specialization"),
    ("Job", "belongs_to", "Industry"),
    ("Job", "demands", "Skill"),
    ("Skill", "qualifies_for", "Job"),
    ("Certification", "teaches", "Skill"),
    ("Certification", "qualifies_for", "Job"),
    ("Job", "hired_by", "Employer"),
    ("Employer", "located_in", "Region"),
    ("Job", "salary_in", "Region"),
    ("Job", "trending_in", "Region"),
}

for i, e in enumerate(edges):
    src_type = node_ids.get(e["source"])
    tgt_type = node_ids.get(e["target"])
    rule = (src_type, e["label"], tgt_type)
    if rule not in VALID_RULES:
        errors.append(f"[V2] Edge {i}: invalid rule {rule}")

# V3 — Path existence (Program → Job)
programs = [n["id"] for n in nodes if n["type"] == "Program"]
jobs = {n["id"] for n in nodes if n["type"] == "Job"}

reachable_jobs = set()
for e in edges:
    if e["label"] == "leads_to" and e["target"] in jobs:
        reachable_jobs.add(e["target"])

if not reachable_jobs:
    errors.append("[V3] No Program → Job paths detected")

# V4 — DIR3 sanity (no self-loops)
for i, e in enumerate(edges):
    if e["source"] == e["target"]:
        errors.append(f"[V4] Edge {i}: self-loop detected on {e['source']}")

# Result
if errors:
    print("❌ GRAPH VALIDATION FAILED\n")
    for err in errors:
        print(err)
    sys.exit(1)
else:
    print("✅ GRAPH VALIDATION PASSED — all checks OK")
