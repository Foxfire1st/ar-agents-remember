# mcp/src/agents_remember/application/knowledge_writer/case_proof.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**A proof that names a test case by its lines, resolved at the code candidate (MIK-R194 rules 1-3).**
The module parses the candidate bytes, asks whether any `path::name` really reaches the case through
the code snapshot's own resolver, and answers the locator the proof stores plus the titles its
evidence pairs with. `authoring.py` keeps only the call, so the check and its reasons live here rather
than inside the editor.

## Code Commentary

### Logic

- **`CaseProof`** is the whole answer: the locator (`None` when nothing is written), the titles the
  evidence pairs with, and the refusal text when the lines prove nothing.
- **`range_proof(code, test)`** reads `start` and `end` from the reference's locator document, decodes
  the file's bytes at C, and calls the grammar module's case check with `_reaches` as the name
  question. A refusal comes back in the grammar's own words; otherwise the answer carries the locator
  and the pairing titles. An unreadable or undecodable blob and a grammar that cannot be loaded are
  refusals, so a caller never has to catch for them.
- **`_reaches`** asks the snapshot whether a `path::title` reaches this case. Resolving is not the
  question: a name can resolve to an ordinary declaration in the same file, or to another case, and
  the range is still the only proof of this one. The name reaches the case only when its own anchor
  holds the very bytes this case's extent holds, so a title that resolves elsewhere answers with a
  reason and the range stays open.
- **Pairing is separate from name eligibility.** A literal case inside a computed `describe` suite is
  reached by no name and still pairs its evidence by its own title, while a case whose own title is
  computed pairs with nothing. The titles come from the case-extent module, not from this one.
- **`proven_tests(proofs, write)`** maps each cited test to its outcome: a `path::name` proof lands
  under its own reference, and a range proof lands only under the titles it pairs with. The first
  outcome recorded for a title stands, so a case proved twice is one result rather than the last
  writer's.

### Conventions

- Nothing here reads the working tree: bytes and resolution come from the snapshot the caller passes,
  and the module imports neither the row layer nor `test_cases`.

## Invariants And Boundaries

- A refusal writes nothing: the caller turns it into one named problem of the entry and no sidecar
  entry is made.
- The snapshot's own resolver decides the name question, and the same snapshot's bytes are what is
  parsed. A title that resolves to another construct never suppresses the range.
- A range proof never reports itself as reaching a name: it is cited by evidence, so it enters the
  outcomes only through the titles its case pairs with.
- The first outcome for a title is kept, so a second proof of the same case cannot overwrite the
  first's report.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- A range proof answers the locator, the pairing titles, or the reason the lines are no case. [1]
- The case check is the grammar module's, run over the candidate bytes with the snapshot's name question. [2]
- An unreadable blob or an unavailable grammar is a refusal rather than an exception. [3]
- A title reaches the case only when the snapshot resolves that name to the same content the case's extent holds. [4]
- A named proof lands under its own reference and a range proof under the titles it pairs with. [5]
- The first outcome recorded for a title stands, so a case proved twice is one result. [6]
