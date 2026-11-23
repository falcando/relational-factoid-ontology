# Relational Factoid Prosopography Ontology (RFPO)

**RFPO · Working formalisation v0.1** | RDF/OWL | Source-grounded relational prosopography

**Author and relational model:** Hervin Fernández Aceves. The **Relational Factoid Prosopography Ontology (RFPO)** formalises his published model of relational factoids in historical prosopography through RDF/OWL, extending John Bradley's Factoid Prosopography Ontology (FPO).

## Research question and formal model

In *The Uncharted Networks of a 'Chartered' Territory*, Fernández Aceves extended Bradley and Short's factoid formulation to distinguish **attributional** and **relational** factoids. The relational model can be paraphrased as:

> A source S, at locus L and time T, states a connection N between actants A1 and A2.

The result is a **sourced assertion of a relationship**, not an unqualified claim that the relationship is historically true. In particular, documentary assertions, actors' mentions, historians' interpretations and historical persons must remain distinct.

A primary reference for the author's formulation is [the presentation](https://www.academia.edu/24429003/The_Uncharted_Networks_of_a_Chartered_Territory_Diplomatic_Evidence_and_Relational_Sociology_for_the_Norman_Kingdom_of_Sicily). The later public lecture *An adapted ontology for a prosopography of medieval Sardinia: RDF schemes, OWL and an open linked database* was announced by [Masaryk University / DISSINET (23 March 2022)](https://www.dissinet.cz/news/events-calendar/616919u-online-lecture-an-adapted-ontology-for-a-prosopography-of-medieval-sardinia-rdf-schemes-owl-and-an-open-linked-database).

## Relationship to Bradley's FPO

- Base ontology: [John Bradley, FPO v1.0](https://github.com/johnBradley501/FPO), [source file](https://github.com/johnBradley501/FPO/blob/master/fpo.owl), whose own source includes a CC BY-NC 4.0 rights statement.
- **Extension, not fork:** this repository references FPO classes and properties in its own namespace and **does not include a copy of Bradley's ontology**. Load FPO alongside this extension when running inference across their complete axioms.
- `rfpo:RelationalFactoid` descends from `fpo:Factoid`, **not** `fpo:RelationshipFactoid`: the latter is a `StateOfAffairsFactoid` and cannot also represent a `Transaction` event without contradicting Bradley's event/state disjointness.
- `rfpo:hasActant1Reference` and `rfpo:hasActant2Reference` refine `fpo:hasReference`. Each actant is encountered through a source-specific `fpo:PersonReference`, with a `fpo:Role` and original source name.

## Repository contents

| File | Purpose |
| --- | --- |
| `relational-factoid-ontology.rdf` | The relational factoid ontology in RDF/XML, including OWL definitions |
| `relational-factoid-ontology.ttl` | The same RDF/OWL ontology in Turtle syntax |
| `relational-factoid-shapes.ttl` | SHACL constraints for a binary, source-grounded record |
| `example-SYNTHETIC.ttl` | **Fictitious** test assertion (no historical evidential claims) |
| `query-relations.rq` | SPARQL query for source-aware relational factoids |
| `test_prototype.py` | Offline Turtle parsing, structural and SPARQL smoke test |
| `requirements.txt` | Python requirement for the smoke test |
| `LICENSE` | Full text of the CC BY-NC 4.0 International licence |

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

## Namespace and identifier stability

The RFPO's public name and its short Turtle prefix (`rfpo:`) do not change the identities of classes and properties. The existing namespace is retained to avoid breaking published RDF references:

The working project vocabulary uses:

```text
https://raw.githubusercontent.com/falcando/relational-factoid-ontology/main/relational-factoid-ontology.ttl#
```

The historical repository and file path in this namespace are technical identifiers, not the current academic name of the ontology. Renaming these URLs without a persistent redirect would create incompatible RDF identities. This URI depends on the `main` branch and the repository remaining available. Before a formal stable release, evaluate a persistent namespace and archive a tagged version. Raw GitHub URLs do not by themselves guarantee persistent semantic-web publication or appropriate RDF content negotiation.

## Credit, licence and reproducibility

The relational factoid model was developed by **Hervin Fernández Aceves** and described in his publicly available academic work. **RFPO** is the name adopted for its RDF/OWL formalisation. This repository formalises that model in RDF/OWL, building on the distinct FPO developed by John Bradley. The files here are not copies of the original TextMate document prepared for the 2022 lecture.

**Licence:** This RDF/OWL formalisation is made available under [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/). See [LICENSE](LICENSE) for the declaration and the official legal code. Bradley's original FPO independently declares CC BY-NC 4.0; this repository references but does not reproduce his ontology. Attribution to Bradley is required for reusing his original material, and the relational extension is credited to Hervin Fernández Aceves.

The repository is a versioned research prototype, not a peer-reviewed or historically validated dataset.

## RDF, OWL and Turtle: what is the difference?

The distinction starts with RDF, or the *Resource Description Framework*. RDF represents information in a graph through explicit statements, each made of a subject, a predicate and an object. As explained in [*What can we learn from the Semantic Web to 'revamp' our Historical Research?*](https://www.epoch-magazine.com/post/what-can-we-learn-from-the-semantic-web-to-revamp-our-historical-research), these statements are called *semantic triples*. They allow us to connect data entities directly, rather than retrieve their connections only through the structure of a relational database.

Yet stating a connection is not quite the same as defining its meaning. Consider a medieval charter that records a kinship relationship between two persons. RDF can represent that documentary statement, but an ontology is needed to define what the relationship means, which classes of entities it connects, and how it relates to other concepts. RDF Schema (RDFS) provides basic classes, properties and hierarchies; the *Web Ontology Language* (OWL) extends these possibilities with a more formal vocabulary for describing a domain of knowledge. In this project, the ontology defines how a relational factoid is represented, without turning the source's assertion into an unquestioned historical fact.

So, where does Turtle fit in? **Turtle** (*Terse RDF Triple Language*) and **RDF/XML** are simply two syntaxes for writing RDF. The former is usually more compact and readable; the latter expresses the same statements using XML. Both can represent OWL ontologies. The extensions `.ttl` and `.rdf` describe these serialisations, whereas `.owl` is a conventional file extension, not a different semantic language. Indeed, Bradley's original `fpo.owl` file is written in Turtle.

This repository therefore provides **two equivalent serialisations of one ontology**, rather than three different ontologies:

- [`relational-factoid-ontology.rdf`](relational-factoid-ontology.rdf) is the RDF/XML document, including the classes and properties defined using OWL.
- [`relational-factoid-ontology.ttl`](relational-factoid-ontology.ttl) expresses the same 60 RDF triples in Turtle syntax, making the ontology more convenient to read and edit.

The [synthetic example](example-SYNTHETIC.ttl) is a separate RDF graph illustrating how assertions can be recorded with this vocabulary; it is not a corpus of actual Sardinian charters. The [SHACL shapes](relational-factoid-shapes.ttl) serve a different purpose: validating the structure of records. Bradley's FPO is referenced, not reproduced here, and its axioms must be loaded separately when reasoning across both ontologies.
