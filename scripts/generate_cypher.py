import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
GRAPH_DIR = BASE_DIR / "graph"
EXPORT_DIR = GRAPH_DIR / "exports"

EXPORT_DIR.mkdir(parents=True, exist_ok=True)

nodes = json.load(open(GRAPH_DIR / "edu_nodes.json", encoding="utf-8"))
edges = json.load(open(GRAPH_DIR / "edu_edges.json", encoding="utf-8"))

out = []

# --- Constraints ---
out.append("CREATE CONSTRAINT IF NOT EXISTS FOR (n:Node) REQUIRE n.id IS UNIQUE;\n")

# --- Nodes ---
for n in nodes:
    labels = f":{n['type']} :Node"
    props = f"id:'{n['id']}', label:'{n['label']}'"
    out.append(f"MERGE ({labels} {{{props}}});")

# --- Edges ---
for e in edges:
    rel = e["label"].upper()
    out.append(
        f"""
MATCH (a {{id:'{e['source']}'}}),(b {{id:'{e['target']}'}})
MERGE (a)-[:{rel}]->(b);
""".strip()
    )

cypher_file = EXPORT_DIR / "edu_graph.cypher"
cypher_file.write_text("\n".join(out), encoding="utf-8")

print(f"✅ Neo4j Cypher generated at: {cypher_file}")
