"""Small offline structural and SPARQL smoke test. Not a SHACL/OWL reasoner."""
from pathlib import Path
from rdflib import Graph, Namespace, RDF, RDFS, OWL

ROOT = Path(__file__).parent
FPO = Namespace('https://github.com/johnBradley501/FPO/raw/master/fpo.owl#')
RF = Namespace('https://raw.githubusercontent.com/falcando/relational-factoid-ontology/main/relational-factoid-ontology.ttl#')
DEMO = Namespace('https://raw.githubusercontent.com/falcando/relational-factoid-ontology/main/example-SYNTHETIC.ttl#')

def load(name):
    g = Graph()
    g.parse(ROOT / name, format='turtle')
    return g

ontology = load('relational-factoid-ontology.ttl')
data = load('example-SYNTHETIC.ttl')
shapes = load('relational-factoid-shapes.ttl')
assert (RF.RelationalFactoid, RDFS.subClassOf, FPO.Factoid) in ontology
assert (RF.hasActant1Reference, RDFS.subPropertyOf, FPO.hasReference) in ontology
assert (RF.hasActant2Reference, RDFS.subPropertyOf, FPO.hasReference) in ontology
assert len(shapes) > 0

for factoid in data.subjects(RDF.type, RF.BinaryRelationalFactoid):
    def unique(subject, prop):
        values = list(data.objects(subject, prop))
        assert len(values) == 1, f'{subject}: expected one {prop}, got {values}'
        return values[0]
    r1 = unique(factoid, RF.hasActant1Reference)
    r2 = unique(factoid, RF.hasActant2Reference)
    assert r1 != r2
    unique(factoid, RF.assertsConnectionType)
    citation = unique(factoid, FPO.sourcedFrom)
    unique(citation, FPO.fromSource)
    unique(citation, FPO.hasPlaceInSource)
    for ref in (r1, r2):
        assert (ref, RDF.type, FPO.PersonReference) in data
        unique(ref, FPO.referencesPerson)
        unique(ref, FPO.hasRole)

combined = ontology + data
query = (ROOT / 'query-relations.rq').read_text(encoding='utf-8')
rows = list(combined.query(query))
assert len(rows) == 1, f'Expected one test assertion, got {len(rows)}'
print(f'PASS: ontology={len(ontology)} triples, data={len(data)} triples, '
      f'shapes={len(shapes)} triples, SPARQL rows={len(rows)}')
for row in rows:
    print('SPARQL:', str(row.factoid), str(row.relation), str(row.locus))
