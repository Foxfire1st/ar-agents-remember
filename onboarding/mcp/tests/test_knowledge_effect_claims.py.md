# mcp/tests/test_knowledge_effect_claims.py

## Governing Overview

[tests route overview](../overview.md)

## Purpose

`InvariantEffectClaim`: the authored effect, its closed vocabulary and its one code. **33 cases**, in the
order the requirement states its clauses, all in the `unit-regression` lane.

## Code Commentary

### Logic

Every case protects one clause group: which payload shape the kind admits, the closed nine-label
vocabulary, the one cardinality rule and its one refusal code, which references resolve, the author and the
lifecycle as stored envelope data, the batch union and the kind registry, and the derived read beside the
mechanical comparison's documented semantic silence.

Two properties are load-bearing enough that the module's own probe tuples exist to make them checkable:

- **There is no truth verdict field and no derived label.** `VERDICT_FIELD_NAMES` probes for a field that
  would make a stored claim a verdict rather than a claim, and each probe is asserted refused as the
  shipped `invalid_payload` — asserted, so the case cannot pass by there being nothing to probe.
  `IDENTITY_FIELD_NAMES` probes for a content address, a logical digest, a fingerprint or a generated
  summary. And an authored effect that the comparison contradicts is stored **exactly as authored**: an
  author records `weaken` on a revision whose statement grew, the record is served with that label and
  `unresolved_references == ()`, and nothing reports the growth or flags the disagreement. A store that
  quietly disagreed with its author is the failure the whole requirement exists to prevent.
- **The comparison keeps its semantic silence.** No field of `KnowledgeDiffItem`,
  `KnowledgeDiffSourceChange` or `KnowledgeDiffResult` carries an effect, a preservation, a severity or a
  verdict word, and the shipped field-name vocabulary carries none either, so the record group adds a
  record *beside* the comparison and never a field on it.

**The vocabulary is closed and pinned, not unioned.** The nine labels are asserted as the literal tuple in
the document's own order, and the literal type the payload validates against *is* that tuple, so a synonym,
a compound label, a free-text label and a locally added tenth member all fail. `DIVISION_EFFECT_LABELS` is
asserted as exactly the frozenset of `split` and `merge` — the set the module's own
`NON_DIVISION_LABELS` is derived from by subtraction rather than restated, so the seven-label tuple cannot
drift from the vocabulary. Near-miss spellings are measured against a real dataset and refused as
`invalid_payload` with the observed label named and nothing written; the same synonym is refused at
construction, so a widening that only the write path enforced would fail here.

**The cardinality rule is one reading, and it is not just a count.** One predicate is asserted over the
four readings Example 6 names, and the cases prove the rule also rejects a claim naming one revision on
*both* sides under an otherwise-admitted combination. Every non-division label admits any counts as long as
the two sides differ, including no references at all. A contradiction is refused as `invalid_payload` and
never as `invalid_reference`, which is the exact instability the blocking finding `CR13-2` was about.

**The lifecycle is the shipped vocabulary and the author is the admission.** Every stored row is served as
`proposed` and no code path sets `accepted`; a payload carrying its own `actor_ref` is refused, while the
command that *can* declare accepted origin data is refused as `promotion_not_supported` — that is what
makes the opposite property checkable. The stored revision and its record row are sealed: the envelope
triggers refuse an update of the payload and a delete of the revision, and the record row cannot be rebound
to another kind.

**The write path is one path.** The batch union carries exactly the four authored-effect commands and their
four kinds; each effect kind resolves to exactly one frozen model in the envelope registry and the effect
kind set does not overlap the requirement kinds; the record group's own operation vocabulary declares the
read and no write operation. Duplicates are keyed on the identical *declaration*, not on the label: an
identical second claim is `duplicate_identity`, while two claims with the same label and different
references, and two differently labelled claims for one comparison, are both stored — an authored
disagreement is not a conflict and is not resolved.

**The read is derived and the generation is refused as a fact.** Two reads over unchanged rows reproduce
the scope byte-for-byte and `READ_OPERATION == "read_effect_scope"`; against a genuine generation-4 dataset
the read refuses as `unsupported_schema` with both numbers, the observed one read from the dataset and the
required one read from the record group's own constant rather than a literal, and nothing is migrated,
repaired or written through.

**What the cases deliberately do NOT assert.** No case asserts that a claim is correct, verified,
consistent with the comparison, or accepted; none asserts a resolved assessment reference; and the
`record_revision.content_digest` column is deliberately **not** counted as a forbidden column — the
exception is the requirement's own, because the sealed revision's content digest belongs to the shipped
envelope and what the packet forbids is these records carrying an identity *of their own*, which the
payload cases assert directly.

### Conventions

Cases are hermetic: temporary directories, in-process APSW databases built through
`mcp/tests/candidate_batch_test_support.py`, a genuine earlier-generation dataset through
`mcp/tests/generation_test_support.py`, and the shared knowledge fixture. The lane row is
`mcp/tests/test-evidence-lanes.toml:164`, and the module is inside the unit population registered in
`mcp/tests/evidence-lifecycle.toml`. The cases drive direct assertions and subtests rather than
parametrization, with every assertion naming the probe, label or kind it is about.

### Invariants And Boundaries

- **No case was removed to make room.** The module is new; it adds 33 cases to the unit population and
  changes no shipped case.
- **The forbidden field sets are asserted as an absence at both planes**: the payload model refuses an
  undeclared field through its ordinary `extra="forbid"` rule — there is no named denylist to relax — and
  no column of any registered generation carries one of the names. A case that asserted only the validator
  half would leave the schema free to hold the value later.
- **A refusal is asserted with its facts**, not merely with a code: the out-of-vocabulary refusal names the
  observed label beside all nine admitted values, the cardinality refusal carries the label and the
  observed counts, and each is paired with `wrote_nothing()`.
- **The change-set half of this record group lives in its sibling module**, `test_knowledge_change_sets.py`,
  and the division of labour is stated in both docstrings.
- **Nothing in this module writes outside a temporary root**, and the record group resolves no requirement
  reference: a stored requirement revision is written by the requirement module's own operation and read
  back unchanged, with this record group's change-set list still empty.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The module docstring stating what these cases protect, the failures each case catches, and why the forbidden field sets are asserted as an absence at both planes. [1]
- The seven labels that claim neither division nor union, derived by subtraction from the admitted set so the tuple cannot drift. [2]
- The probe names that would make a stored claim a verdict rather than a claim. [3]
- The probe names that would make this record group its own identity authority, or its own narrative. [4]
- The case that asserts the effect set is closed, spelled once, in the document's own order, and that the literal type is the declared tuple. [5]
- The case that asserts an out-of-vocabulary label is refused as invalid payload naming the observed label beside all nine admitted values, with nothing written. [6]
- The case that asserts near-miss spellings are refused rather than corrected, each asserted and each named in its failure. [7]
- The case that asserts the shape check holds at construction as well as at the storage boundary. [8]
- The case that asserts one cardinality reading predicts exactly the four cases Example 6 names. [9]
- The case that asserts a split with one output and a merge with one input are refused under the same code, naming label and counts. [10]
- The case that asserts one revision on both sides is refused even though its counts are inside the admitted combination. [11]
- The case that asserts a cardinality contradiction is never reported as an invalid reference. [12]
- The case that asserts every non-division label admits any counts when the two sides differ, and that "any counts" includes none. [13]
- The case that asserts a claim naming no revision on either side is admissible and stored. [14]
- The case that asserts the author is the shipped envelope stamped from the admission, and that a payload cannot supply one. [15]
- The case that asserts a rationale that says nothing is refused at both planes. [16]
- The case that asserts an unresolvable input or output is refused as an invalid reference naming the identity, with nothing written. [17]
- The case that asserts a claim naming a change set that is not stored is a dangling reference rather than a claim outside every change set. [18]
- The case that asserts the batch applies commands in order, so a citation arriving before its change set is refused by name with its remedy. [19]
- The case that asserts the batch union carries exactly the four authored-effect commands and no member accepting a computed label or free-form text. [20]
- The case that asserts every effect kind resolves to exactly one frozen model and that the effect kind set does not overlap the requirement kinds. [21]
- The case that asserts no field can hold a truth verdict about the label, probing the payload through the envelope registry and naming the admitted probe in its failure. [22]
- The case that asserts no field can hold an identity of this record group's own, or a generated summary or narrative. [23]
- The case that asserts no registered generation carries a verdict, severity or summary column on any table of this record group, and that the appended table carries no identity column either. [24]
- The case that asserts an incorrect authored effect is stored exactly as authored, with nothing reporting the disagreement. [25]
- The case that asserts every stored row is served as proposed and no path sets accepted. [26]
- The case that asserts a command declaring accepted origin data is refused as promotion not supported. [27]
- The case that asserts a stored claim revision cannot be rewritten or deleted and its record row cannot be rebound. [28]
- The case that asserts an unresolved assessment reference is a stored state reported verbatim with its holder, never a refusal. [29]
- The case that asserts an identical second claim is refused as duplicate identity with the dataset unchanged. [30]
- The case that asserts two differently labelled claims for one comparison are both stored and neither is promoted. [31]
- The case that asserts the duplicate rule is keyed on the declaration, not on the label alone. [32]
- The case that asserts the read serves a derived scope that reproduces byte-for-byte and that the read is the record group's one operation. [33]
- The case that asserts a generation-4 dataset is refused as unsupported schema with both numbers as facts and nothing migrated. [34]
- The case that asserts no field of the mechanical comparison can hold an authored meaning. [35]
- The case that asserts the record group's own operation vocabulary declares the read and no write path beside the batch. [36]
- The case that asserts a stored requirement revision is written by the requirement module's own operation and left untouched, with this record group's change-set list empty. [37]
- The lane row placing this module in the unit population. [38]
- The registration listing this module among the exact consumers of the shared candidate-batch case harness. [39]
- The registration listing this module among the exact consumers of the shared candidate-batch case harness. [40]
- The registration listing this module among the exact consumers of the shared earlier-generation case support. [41]
- The registration listing this module among the exact consumers of the shared earlier-generation case support. [42]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The cases exercise one in-process knowledge store
under a temporary root and construct no process, publication or Git object.

No meaningful cross-repo references found.
