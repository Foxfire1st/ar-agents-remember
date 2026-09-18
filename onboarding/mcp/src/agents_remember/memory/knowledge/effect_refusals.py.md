# mcp/src/agents_remember/memory/knowledge/effect_refusals.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/effect_refusals.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T10:20+02:00 |
| lastVerifiedCommitHash |  `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| lastVerifiedCommitDate |  2026-09-18T13:43:14+02:00 |
| reviewedWorkingCandidate | `ar/260915-ks-l13` uncommitted staged source; base `b5a74aee6cdf671c9963f3aba4df6d44b856f697` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The authored-effect record group's own refusal factories: two facts only this group can state, each
emitting a **shipped** code rather than widening the refusal vocabulary. Four factories — a label, a
cardinality, a succession cycle and a duplicate claim — built where the fact is decided rather than at
each raise site.

## Code Commentary

### Logic

Refusals live beside the record group that owns them, for the same reason the row codecs and the
schema modules do: a refusal is a statement about *this* contract, and the shared
`memory/knowledge/refusals.py` is where a code, its facts and its next action are *spelled* rather than
where every contract's failures accumulate. This leaf added **no line** to the shared module.

Four failures, and each is a different fact:

- **A label outside the closed nine-member set** (`effect_label_refusal`, `invalid_payload`). The
  refusal carries the **observed label and the nine admitted values** as facts, because the remedy is
  the author spelling one of the nine exactly and the message has to say which nine. There is no
  synonym, no compound label, no free-text label and no locally added tenth member, and no nearest
  match is substituted.
- **A declaration the one cardinality rule does not admit** (`effect_cardinality_refusal`,
  `invalid_payload`). The `observed` fact is the **declared label plus the observed input and output
  counts**, and — where the two sides name the same revision — that reference too, so a caller can
  branch on the fact without reading the sentence. The predicate that decides is
  `models.knowledge.effect.cardinality_violation`, which is imported rather than restated, so the
  construction validator and this storage-boundary refusal cannot disagree about what is admitted.
  `cardinality_rule_text` supplies the `expected` half from the same module, again so the rule has one
  definition.
- **A succession that reaches itself** (`succession_cycle_refusal`, `lineage_cycle`). The self-naming
  case and the longer cycle are one refusal from one rule, so a successor that names itself is **not**
  reported as a missing reference. The fact names the change sets that form the cycle.
- **A second claim declaring exactly what a stored one already declares**
  (`duplicate_effect_claim_refusal`, `duplicate_identity`). Only an identical declaration reaches
  this: the same label *and* the same input and output reference sets, for the same change set. Two
  **differently labelled** claims for one comparison are deliberately **not** this refusal — that is
  the authored disagreement the design requires to stay visible, so both rows are kept. The refusal
  names the stored claim it duplicates rather than reporting a conflict to be resolved.

**The refusals this module deliberately does not restate.** A reference that resolves to nothing is
`invalid_reference` through `memory/knowledge/endpoints.py`; a dataset whose recorded generation
predates the succession table is `unsupported_schema` through
`facets.generation_mismatch_refusal`'s own factory; a reused record identity is `stale_precondition`
through the batch's own insertion check; a stored accepted-origin record is `promotion_not_supported`,
raised in `effects.py` through the shared `refusal(...)` helper. Each already has a home, and a second
factory here would be the second definition the shipped doctrine forbids.

**Why `EFFECT_OPERATION` is the narrow literal rather than the wide vocabulary.** Every refusal this
group raises belongs to the candidate batch's act — the requirement places these records on that one
write path and the group has no standalone operation beside it — so the constant is spelled
`Literal["change_candidate"]`. It is assignable both to `KnowledgeRefusal.operation` and to the shared
endpoint check's own narrower set, so neither call site needs a cast.

### Conventions

The factories build through the shared `refusal(...)` helper with `RefusalFacts`, so they carry the same
shape as every other refusal in the package. The module's only import from the shared spelling module is
that helper and its facts type, plus the shipped `KnowledgeOperation` / `KnowledgeRefusal` models — so
the shared module can be split later without this one changing.

`ADMITTED_LABEL_LISTING` renders the nine labels once, joined by `" | "`, and both the refusal's
`expected` fact and the label check's own `next_action` read it. A second rendering would be a second
place the vocabulary could be spelled differently.

### Invariants And Boundaries

- **Every code here is shipped.** `invalid_payload`, `lineage_cycle` and `duplicate_identity` were all
  already members of `KnowledgeRefusalCode`; this leaf widened no vocabulary, and the nine-member
  effect vocabulary is a payload vocabulary rather than a refusal one.
- **One rule, two enforcement points.** `cardinality_violation` is imported, never re-implemented, so a
  change to the rule cannot leave the construction validator and the storage refusal disagreeing.
- **A refused claim writes nothing.** Every factory here is raised before a row exists and the batch
  rolls the whole transaction back, so an inadmissible declaration leaves no envelope row, no revision
  and no succession edge behind.
- **A duplicate is not a conflict.** The refusal reports what is duplicated; nothing here merges,
  replaces or deletes a stored claim, and the remedy it names is to author a claim that says something
  the stored ones do not.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The label refusal: the observed label and the nine admitted values as facts, with no synonym and no nearest match. | `effect_label_refusal` | mcp/src/agents_remember/memory/knowledge/effect_refusals.py:48-68 |
| The cardinality refusal, whose `observed` fact is the declared label and the two counts, and whose `expected` comes from the rule's own text. | `effect_cardinality_refusal` | mcp/src/agents_remember/memory/knowledge/effect_refusals.py:71-103 |
| The succession-cycle refusal: the self-naming case and the longer cycle are one refusal from one rule. | `succession_cycle_refusal` | mcp/src/agents_remember/memory/knowledge/effect_refusals.py:106-132 |
| The duplicate-claim refusal, which only an *identical* declaration reaches; a differently labelled claim for one comparison is kept. | `duplicate_effect_claim_refusal` | mcp/src/agents_remember/memory/knowledge/effect_refusals.py:135-161 |
| The operation every refusal in this group belongs to, spelled narrowly so neither the refusal model nor the endpoint check needs a cast. | `EFFECT_OPERATION` | mcp/src/agents_remember/memory/knowledge/effect_refusals.py:41-41 |
| The one rendering of the nine admitted values, read by both the refusal's `expected` fact and its `next_action`. | `ADMITTED_LABEL_LISTING` | mcp/src/agents_remember/memory/knowledge/effect_refusals.py:45-45 |
| The one cardinality rule, imported rather than restated so the two enforcement points cannot disagree. | `cardinality_violation`; `cardinality_rule_text` | mcp/src/agents_remember/models/knowledge/effect.py:102-133; mcp/src/agents_remember/models/knowledge/effect.py:136-148 |
| The nine-member effect vocabulary the label refusal reads its admitted set from. | `ADMITTED_EFFECT_LABELS`; `EffectLabel` | mcp/src/agents_remember/models/knowledge/effect.py:63-73; mcp/src/agents_remember/models/knowledge/effect.py:75-85 |
| The shared spelling helper and facts type these factories build through — this module's only import from the shared refusals module. | `refusal`; `RefusalFacts` | mcp/src/agents_remember/memory/knowledge/refusals.py:57-79; mcp/src/agents_remember/memory/knowledge/refusals.py:48-56 |
| The shipped code vocabulary these three codes stay inside; no new member was added by this leaf. | "KnowledgeRefusalCode = Literal[" | mcp/src/agents_remember/models/knowledge/result.py:151-222 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A refusal is a statement about one
namespace's own store, and the facts it carries are identities inside that store.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T10:20+02:00 — 260915-KS-L13 curator (uncommitted change set on `ar/260915-ks-l13`, base `b5a74aee`): created this one-to-one card for the authored-effect record group's own refusal factories. It records the four distinct facts, the shipped codes they reuse, the import-not-restate rule that keeps the cardinality predicate single-defined, and the deliberate absence of the shipped refusals that already have a home. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
