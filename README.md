# Relational Factoid Ontology (RFO)

**Working reconstruction v0.1** | OWL/RDF (Turtle) | Source-grounded relational prosopography

**Author and research concept:** Hervin Fernández Aceves. **Technical implementation:** reconstructed in November 2026 with AI assistance, from the author's documented conceptual model and John Bradley's Factoid Prosopography Ontology (FPO).

> **Important provenance:** This repository is a **new reconstruction**, **not** a recovered copy of Fernández Aceves's lost TextMate ontology, and **not** a verified reconstruction of his 2022 Masaryk University implementation. No original file from the lost ontology is reproduced or claimed to have survived.

## Research question and formal model

In *The Uncharted Networks of a 'Chartered' Territory*, Fernández Aceves extended Bradley and Short's factoid formulation to distinguish **attributional** and **relational** factoids. The relational model can be paraphrased as:

> A source S, at locus L and time T, states a connection N between actants A1 and A2.

The result is a **sourced assertion of a relationship**, not an unqualified claim that the relationship is historically true. In particular, documentary assertions, actors' mentions, historians' interpretations and historical persons must remain distinct.

A primary reference for the author's formulation is [the presentation](https://www.academia.edu/24429003/The_Uncharted_Networks_of_a_Chartered_Territory_Diplomatic_Evidence_and_Relational_Sociology_for_the_Norman_Kingdom_of_Sicily). The later public lecture *An adapted ontology for a prosopography of medieval Sardinia: RDF schemes, OWL and an open linked database* was announced by [Masaryk University / DISSINET (23 March 2022)](https://www.dissinet.cz/news/events-calendar/616919u-online-lecture-an-adapted-ontology-for-a-prosopography-of-medieval-sardinia-rdf-schemes-owl-and-an-open-linked-database).

## Relationship to Bradley's FPO

- Base ontology: [John Bradley, FPO v1.0](https://github.com/johnBradley501/FPO), [source file](https://github.com/johnBradley501/FPO/blob/master/fpo.owl), whose own source includes a CC BY-NC 4.0 rights statement.
- **Extension, not fork:** this repository references FPO classes and properties in its own namespace and **does not include a copy of Bradley's ontology**. Load FPO alongside this extension when running inference across their complete axioms.
- `rf:RelationalFactoid` descends from `fpo:Factoid`, **not** `fpo:RelationshipFactoid`: the latter is a `StateOfAffairsFactoid` and cannot also represent a `Transaction` event without contradicting Bradley's event/state disjointness.
- `rf:hasActant1Reference` and `rf:hasActant2Reference` refine `fpo:hasReference`. Each actant is encountered through a source-specific `fpo:PersonReference`, with a `fpo:Role` and original source name.

## Repository contents

| File | Purpose |
| --- | --- |
| `relational-factoid-ontology.ttl` | OWL/RDFS vocabulary for relational and attributional factoids |
| `relational-factoid-shapes.ttl` | SHACL constraints for a binary, source-grounded record |
| `example-SYNTHETIC.ttl` | **Fictitious** test assertion (no historical evidential claims) |
| `query-relations.rq` | SPARQL query for source-aware relational factoids |
| `test_prototype.py` | Offline Turtle parsing, structural and SPARQL smoke test |
| `requirements.txt` | Python requirement for the smoke test |
| `LICENSE` | CC BY-NC 4.0 licensing notice and official legal-code link |

## Model boundaries and outstanding decisions

1. **T remains interpretatively unresolved in the original formula.** This prototype treats it provisionally as the date of the source assertion via FPO's `hasDateAssertionMade`, distinct from a `relationTime` for a relationship's asserted period. A dated charter does **not** automatically date every relationship mentioned in it.
2. **L is the textual locus**, not geographic location. FPO's `SourceCitation` and `hasPlaceInSource` provide the documentary anchor.
3. **Binary relations only** in v0.1. Witnesses, additional parties and genuinely n-ary legal transactions require a later design decision. Participant roles must not be flattened away.
4. **Not a complete relational database.** It is an RDF/OWL formalisation of relational factoids, not a SQL implementation of the earlier relational tables.
5. **No real Sardinian charter data are asserted.** The example uses invented actors and a non-existent charter. Its claims are software test fixtures only.
6. **SHACL is separate from OWL.** Closed-world record completeness is checked using SHACL (or the simple smoke-test assertions), rather than presumed from open-world OWL axioms.
7. **No inferred person-to-person network edges are asserted as historical truths.** Any later network projection must specify a derivation rule, scope, chronology and evidential weighting.

## Run the basic tests

```bash
python -m pip install -r requirements.txt
python test_prototype.py
```

This is **not** a substitute for running an OWL reasoner with Bradley's FPO loaded or a proper SHACL validator against the shapes. The current test checks Turtle syntax, selected logical structure and SPARQL query results.

## Namespace

The working project vocabulary uses:

```text
https://raw.githubusercontent.com/falcando/relational-factoid-ontology/main/relational-factoid-ontology.ttl#
```

This URI depends on the `main` branch and the repository remaining available. Before a formal stable release, evaluate a persistent namespace and archive a tagged version. Raw GitHub URLs do not by themselves guarantee persistent semantic-web publication or appropriate RDF content negotiation.

## Credit, licence and reproducibility

The conceptual relational extension is attributed to **Hervin Fernández Aceves**; Bradley's distinct original FPO is credited above. This implementation is reconstructed with AI assistance and should not be cited as an original 2022 source artefact.

**Licence:** This newly authored reconstruction is made available under [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/). See [LICENSE](LICENSE) for the declaration and the official legal code. Bradley's original FPO independently declares CC BY-NC 4.0; this repository references but does not reproduce his ontology. Attribution to Bradley is required for reusing his original material, and the relational extension is credited to Hervin Fernández Aceves.

The repository is a versioned research prototype, not a peer-reviewed or historically validated dataset.
