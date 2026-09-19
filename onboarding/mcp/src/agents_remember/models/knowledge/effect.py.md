# mcp/src/agents_remember/models/knowledge/effect.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/effect.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T10:28+02:00 |
| lastVerifiedCommitHash |  `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| lastVerifiedCommitDate |  2026-09-18T13:43:14+02:00 |
| reviewedWorkingCandidate | `ar/260915-ks-l13` uncommitted staged source; base `b5a74aee6cdf671c9963f3aba4df6d44b856f697` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

The authored-effect record group's frozen payload vocabulary: what a change was *intended* to do, and
who said so. Three member kinds — an invariant effect claim, a preservation claim and an unresolved
question — and nothing about where they are stored. Like the requirement-revision and authored-facet
groups before it, this group adds **no** envelope, no identity mechanism and no second revision
aggregate: the shapes below are what the envelope's registry resolves for those kinds.

## Code Commentary

### Logic

**The effect vocabulary is closed, and it is spelled once.** `ADMITTED_EFFECT_LABELS` names the nine
labels in the source document's own order — `restore`, `clarify`, `introduce`, `strengthen`, `weaken`,
`replace`, `split`, `merge`, `retire` — and `EffectLabel` is the literal type built from exactly that
tuple, with a case asserting the two agree. So a synonym, a compound label, a free-text label and a
tenth member are **all the same refusal**: the payload does not validate. Code never derives a label
from anything — a comparison that observes a condition set growing does not make the effect
`strengthen`, and no field here could receive such a derivation.

**Inputs and outputs are exact revision references, never prose.** `RevisionReference` is a
`UUID_PATTERN`-constrained string, and the two sets are what the one cardinality rule reads. Nothing in
this vocabulary parses a reference, splits it on a separator, or infers an identity from it.
`EffectReference` is the separate bounded-but-opaque type used where the referenced thing's future
shape is not this leaf's to fix.

**One cardinality rule, one refusal.** `cardinality_violation` is the single definition of what a
declared label may claim about counts, and it returns the *fact* as text (or `None` when admissible)
rather than raising: the construction validator raises it as a `ValueError`, and the storage boundary
builds its typed `invalid_payload` refusal from the same text. Three clauses, in order — no revision may
appear as both an input and an output of the same claim (an effect that names one revision on both
sides claims no change); `split` is admitted only with two or more outputs; `merge` only with two or
more inputs — and every other label admits any counts. `DIVISION_EFFECT_LABELS` names the two labels the
rule reads a count for, so the rule reads as the sentence the requirement states.
`cardinality_rule_text` renders what one declared label *does* admit, as a refusal's `expected` fact,
because a refusal that said only "the counts are wrong" would send the author nowhere.

**A preservation claim is a separate record, and it is not an effect.** `PreservationSubject` carries a
declared `kind` from a closed four-member set — `invariant`, `invariant_revision`, `source_anchor`,
`semantic_change_set` — plus one exact reference identity. There is deliberately **no** subject kind for
an effect claim, no `preserve` member in `ADMITTED_EFFECT_LABELS`, and no preservation flag on an effect
claim, so "this revision preserves that claim's meaning" is not a shape this record can take.

**A question is first-class, and there is no field recording that it was answered.**
`UnresolvedQuestionPayload` has a statement and nothing else, so a change set does not default a
question to answered and does not drop one in order to look finished: the only way a question stops
being open is for a later change set to be authored.

**Membership is declared by the member.** Each member carries the `change_set_id` of the one change set
it belongs to, so "a member is never silently shared between two change sets" is a property of the
member's own immutable declaration rather than a rule two records have to agree about.

### Conventions

Every payload model derives from the shipped `KnowledgeModel`, so `extra="forbid"` is what refuses a
payload arriving with a field the vocabulary does not declare. Two declarations must agree and are
cross-checked rather than restated: `MEMBER_KINDS` (the three kind strings) and `MEMBER_PAYLOAD_MODELS`
(the three `(kind, schema)` → model pairs), whose key sets cannot drift because the envelope's registry
unpacks the mapping instead of restating the pairs. `EFFECT_COMMAND_KINDS` lists the four candidate
commands that write this group as one closed set, and the change-set command is a member even though
its payload model lives beside the views it serves — a dispatch table built from half the set would be
a second declaration that could drift. `EFFECT_WRITABLE_TABLES` declares the group's canonical tables
beside the commands that address them, for the same reason `EVIDENCE_WRITABLE_TABLES` does.

Blank-after-trim is refused, not only length zero: a rationale, a preservation statement and a question
statement each have their own validator that trims, because a claim whose rationale says nothing is a
label without a claim.

### Invariants And Boundaries

- **There is no field that is a truth verdict.** No boolean, score, confidence, verdict or `verified`
  field exists on a claim, and `extra="forbid"` is what refuses a payload arriving with one. Storage
  authority is not semantic endorsement: a stored claim is a claim whose **declared shape** was
  accepted.
- **The author is not a payload field.** A claim's authorship *is* the revision's `provenance` on
  `record_revision`, stamped from the admission, so a payload field naming an actor, an authorization,
  an operation or a recorded time would be a second, competing statement of one fact.
- **Assessment references may remain unresolved, and that is representable.** `assessment_refs` are
  bounded *named* references rather than exact identities, precisely because the assessment record
  belongs to another leaf: one that resolves to nothing is reported as an unresolved reference — never
  a refused write, never a filled-in substitute, and never a claim that an assessment happened.
- **The two reference types are different contracts.** `RevisionReference` is an exact stored revision
  identity and is resolved; `EffectReference` is opaque stored text and is never parsed. A card that
  treated one as the other would describe a second requirement authority this group must not create.
- **`EFFECT_WRITABLE_TABLES` is exactly the two envelope tables, and that is the group's shape rather
  than an omission.** Each of the four commands writes one `knowledge_record` row and its one sealed
  `record_revision`; the succession edge a change set declares is written only as part of the aggregate
  that owns it. This group therefore contributes **no** table to `MutableRecordTable`, and the facet
  case asserts the derived effect-only remainder is empty so the absence is a checked fact.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The nine admitted labels, in one declaration, and the literal type built from exactly that tuple. | `ADMITTED_EFFECT_LABELS`; `EffectLabel` | mcp/src/agents_remember/models/knowledge/effect.py:63-73; mcp/src/agents_remember/models/knowledge/effect.py:75-85 |
| The two labels the cardinality rule reads a count for, named rather than compared inline. | `DIVISION_EFFECT_LABELS` | mcp/src/agents_remember/models/knowledge/effect.py:90-90 |
| The two reference contracts: an exact stored revision identity, and bounded-but-opaque stored text. | `RevisionReference`; `EffectReference` | mcp/src/agents_remember/models/knowledge/effect.py:99-99; mcp/src/agents_remember/models/knowledge/effect.py:94-94 |
| The one cardinality rule — shared-reference, `split`, `merge` — and the renderer of what a declared label does admit. | `cardinality_violation`; `cardinality_rule_text` | mcp/src/agents_remember/models/knowledge/effect.py:102-133; mcp/src/agents_remember/models/knowledge/effect.py:136-148 |
| The effect claim's frozen shape: closed label, two exact reference sets, a non-blank rationale, and unresolved-by-design assessment references. | `InvariantEffectClaimPayload` | mcp/src/agents_remember/models/knowledge/effect.py:151-203 |
| The closed four-member subject kind a preservation claim may name — with no effect-claim member. | `PreservationSubjectKind`; `PreservationSubject` | mcp/src/agents_remember/models/knowledge/effect.py:198-203; mcp/src/agents_remember/models/knowledge/effect.py:206-217 |
| The preservation claim and the open question, each with its own non-blank statement validator and no verdict field. | `PreservationClaimPayload`; `UnresolvedQuestionPayload` | mcp/src/agents_remember/models/knowledge/effect.py:220-242; mcp/src/agents_remember/models/knowledge/effect.py:245-262 |
| The three kind strings and the three frozen shapes, declared once each so the registry unpacks rather than restates them. | `MEMBER_KINDS`; `MEMBER_PAYLOAD_MODELS` | mcp/src/agents_remember/models/knowledge/effect.py:275-279; mcp/src/agents_remember/models/knowledge/effect.py:281-285 |
| The four candidate commands that write this group, as one closed set the dispatch, the preconditions and the duplicate check all read. | `EFFECT_COMMAND_KINDS` | mcp/src/agents_remember/models/knowledge/effect.py:292-297 |
| The group's canonical tables, declared beside the commands that address them — exactly the two envelope tables, so the mutable union gains nothing. | `EFFECT_WRITABLE_TABLES` | mcp/src/agents_remember/models/knowledge/effect.py:312-315 |
| The `extra="forbid"` base every payload derives from, which is what refuses a verdict field or a second authorship statement. | `model_config` | mcp/src/agents_remember/models/knowledge/base.py:34-37 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A payload shape is a property of one
namespace's stored records, and every reference it carries is a store-local identity or opaque text.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T10:28+02:00 — 260915-KS-L13 curator (uncommitted change set on `ar/260915-ks-l13`, base `b5a74aee`): created this one-to-one card for the authored-effect payload vocabulary. It records the closed nine-label vocabulary and its one declaration, the single cardinality rule and why it is shared with the storage boundary rather than restated, the two distinct reference contracts (exact versus opaque), the deliberate absences (no truth verdict, no authorship field, no preservation flag, no answered-question field), and the two-table writable set that follows from the group being envelope-only. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
