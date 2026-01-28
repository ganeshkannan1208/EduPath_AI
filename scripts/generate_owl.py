import json
from pathlib import Path
from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal

BASE_DIR = Path(__file__).resolve().parents[1]
GRAPH_DIR = BASE_DIR / "graph"
EXPORT_DIR = GRAPH_DIR / "exports"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

nodes = json.load(open(GRAPH_DIR / "edu_nodes.json", encoding="utf-8"))
edges = json.load(open(GRAPH_DIR / "edu_edges.json", encoding="utf-8"))

g = Graph()

EDU = Namespace("http://edupath.ai/ontology#")
ESCO = Namespace("http://data.europa.eu/esco/model#")

g.bind("edu", EDU)
g.bind("owl", OWL)
g.bind("rdfs", RDFS)
g.bind("esco", ESCO)

# --- Classes ---
types = set(n["type"] for n in nodes)
for t in types:
    g.add((EDU[t], RDF.type, OWL.Class))

# --- Individuals ---
for n in nodes:
    uri = EDU[n["id"]]
    g.add((uri, RDF.type, EDU[n["type"]]))
    g.add((uri, RDFS.label, Literal(n["label"])))

# --- Properties ---
for e in edges:
    prop = EDU[e["label"]]
    g.add((prop, RDF.type, OWL.ObjectProperty))
    g.add((EDU[e["source"]], prop, EDU[e["target"]]))

owl_file = EXPORT_DIR / "edu_ontology.owl"
g.serialize(destination=str(owl_file), format="xml")

print(f"✅ OWL ontology generated at: {owl_file}")
