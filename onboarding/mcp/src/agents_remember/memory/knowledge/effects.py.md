# mcp/src/agents_remember/memory/knowledge/effects.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/effects.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T10:37+02:00 |
| lastVerifiedCommitHash |  `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| lastVerifiedCommitDate |  2026-09-18T13:43:14+02:00 |
| reviewedWorkingCandidate | `ar/260915-ks-l13` uncommitted staged source; base `b5a74aee6cdf671c9963f3aba4df6d44b856f697` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The authored-effect record group's write path, its preconditions and its read — the *rules* the group
obeys, each one a rule the requirement states as a refusal or as a state. The records themselves are
envelope records written through the candidate batch's one write path, so what this module adds is the
shape check, the reference resolution, the one succession edge and the derived read.

## Code Commentary

### Logic

**The shape check, applied where the requirement puts it.** The construction half is the payload
models' own validators; the storage half is `require_admitted_declaration`, which reads only the three
declared values — the label and the two reference sets — so it stays a **shape check** and inspects no
content, no diff and no text. The label must be one of the nine admitted members and the declared counts
must satisfy `cardinality_violation`; the refusal is built from *that* function rather than from a second
copy of the predicate, so the two enforcement points cannot disagree about what is admitted. Anything
else about a payload — a missing field, an undeclared field, a value of the wrong type — is deliberately
left to the envelope seam, which is the one place a payload's admissibility is decided;
`_declared_references` therefore returns the empty set for a non-sequence rather than reporting a
cardinality problem, because that would name the wrong fact.

**Resolution order: validate, then resolve, then check duplicates — and only then write.**
`_admissible_payload` runs `validate_record_payload` first (the envelope seam decides admissibility —
that is its whole contract), then `require_payload_references` on the **validated** payload, so a
reference is only ever resolved once the shape carrying it is known to be the shape the kind declares,
and then `require_no_stored_duplicate`. Every refusal is *raised*, not returned, so the transaction that
carries the record and its revision is aborted whole: a refused command leaves no envelope row, no
revision and no succession edge behind, and an earlier command's rows in the same batch are rolled back
with it.

**Four references are resolved, and two families deliberately are not.**
`require_payload_references` resolves an effect claim's inputs and outputs (exact stored revisions), a
member's change set and a change set's predecessors (stored `semantic_change_set` records), and a change
set's candidate realization claims (stored `realization_claim` rows) — all through
`memory/knowledge/endpoints.py`, which is the one place a relation write says which endpoint kinds
exist, because a second resolution path beside it is what the shipped doctrine forbids.
**Assessment references and requirement-revision references are deliberately not resolved**: they are
stored verbatim and reported as unresolved, so a code path that resolved one here would be the second
requirement authority this record group must not create.

**One succession edge, written with its successor.** There is no standalone predecessor-append
operation: `_write_succession_edges` inserts each declared edge inside the successor's own creation
batch, exactly as the shipped store rule states. The self-naming case is refused before any edge is
written, through `succession_cycle_refusal`; the longer cycle is found after the inserts, by the shared
acyclic walk over generation 8's table (`require_acyclic_successions` → `lineage.cycle_vertices`, the
same strongly-connected-component scan the two predecessor graphs and the decision supersession edge
use), so no second cycle rule grows beside the first.

**A duplicate is a duplicate, and a disagreement is not.** `require_no_stored_duplicate` compares only
the declared label and the two declared reference sets, and only among the stored claims of the one
change set the new claim names — so two **differently labelled** claims for one comparison are two
records and are both stored, because that is the authored disagreement the design requires to stay
visible.

**The read is derived and refusal-carrying.** `read_effect_scope` checks the generation first and
returns a typed `EffectReadResult` in the `refused` state rather than raising, because a read that is
refused has to persist nothing; when it serves, the scope is built by `effect_views.effect_scope` from
the rows this module's readers hand it. `build_effect_scope` is kept as the thin entry point so this
module stays the write path plus its two entry points.

**One ordering rule is this record group's own**, and it is stated where it is enforced: a command that
*cites* an identity the same batch also creates must appear **after** the command that creates it. That
is the shipped `ChangeBatch` contract — commands are applied in the order given — and a citation that
arrives first is refused as `invalid_reference` naming the identity and the remedy, rather than left to
a foreign key to report as an unnamed constraint failure.

### Conventions

The command's `(kind, record_schema)` pair is read from `_COMMAND_DECLARATION` rather than from the
payload, so a caller cannot store a pair the envelope's registry would refuse and a refusal can name
both without having decoded anything. `_authority_home` reads the bound namespace's own home — a
record's `authority_home` is a fact about the namespace it was written into, not a field a caller
authors. `_written` builds a receipt entry with `model_construct` because the store computed every
field; `_stored_revision_digest` reads the just-written revision's seal back from the row that carries
it rather than recomputing it.

### Invariants And Boundaries

- **Every row this record group writes is `proposed`.** `require_proposed_origin` is a shared step
  rather than a batch-only check, because the same refusal is owed wherever the command is submitted;
  there is no promotion operation anywhere in this group, and acceptance belongs to the process that
  owns it. The code is the shipped `promotion_not_supported`.
- **Nothing is derived.** No code path here computes, infers, suggests, ranks, defaults or repairs an
  effect label from a comparison, a text difference, a condition count or a source change, and no code
  path converts an unchanged file, row or revision into a preservation claim. Those acts are absent from
  the vocabulary rather than refused by it: the command union has no member that could carry one, and
  the payload models have no field one could land in.
- **The generation gate compares against the dataset, not the build.** `require_effect_generation` reads
  the open store's own generation, so a dataset whose recorded generation predates the succession table
  is refused with the observed and required versions as facts; nothing is migrated, widened or written
  through.
- **A named governing route must exist; an ungoverned record is the explicit `None` state.**
  `require_governing_route` refuses a named route that is not authored in this repository as a dangling
  reference, and never refuses `None`.
- **Two enforcement points, one rule.** The cardinality predicate and the admitted-label set are
  imported from `models/knowledge/effect.py`; neither is restated here.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one entry point that applies a command inside the caller's open transaction, and raises rather than returns so the whole batch rolls back. | `apply_effect_command` | mcp/src/agents_remember/memory/knowledge/effects.py:129-154 |
| The measured order — validate at the envelope seam, then resolve on the validated payload, then check duplicates — before any row exists. | `_admissible_payload` | mcp/src/agents_remember/memory/knowledge/effects.py:157-182 |
| The envelope row and its one sealed revision, written together. | `_write_record` | mcp/src/agents_remember/memory/knowledge/effects.py:185-206 |
| The one succession edge, inserted inside the successor's own batch and cycle-checked in the same transaction. | `_write_succession_edges` | mcp/src/agents_remember/memory/knowledge/effects.py:209-226 |
| The shape check: the nine admitted labels and the shared cardinality rule, reading no content, no diff and no text. | `require_admitted_declaration` | mcp/src/agents_remember/memory/knowledge/effects.py:254-286 |
| The refusal of accepted origin data, with no promotion operation anywhere in the group. | `require_proposed_origin` | mcp/src/agents_remember/memory/knowledge/effects.py:312-336 |
| The generation gate, compared against the dataset's own recorded generation rather than the build's support. | `require_effect_generation`; `require_effect_generation_or_raise` | mcp/src/agents_remember/memory/knowledge/effects.py:339-360; mcp/src/agents_remember/memory/knowledge/effects.py:363-368 |
| The four resolved reference families and the two deliberately unresolved ones. | `require_payload_references` | mcp/src/agents_remember/memory/knowledge/effects.py:371-410 |
| The duplicate scan, bounded to the one change set and comparing only label and the two reference sets. | `require_no_stored_duplicate` | mcp/src/agents_remember/memory/knowledge/effects.py:432-466 |
| The shared acyclic walk over generation 8's table, so no second cycle rule grows beside the first. | `require_acyclic_successions` | mcp/src/agents_remember/memory/knowledge/effects.py:484-507 |
| The derived read that refuses by state rather than by exception, and the thin builder entry point under it. | `read_effect_scope`; `build_effect_scope` | mcp/src/agents_remember/memory/knowledge/effects.py:510-531; mcp/src/agents_remember/memory/knowledge/effects.py:534-541 |
| The named-route check: a dangling named route is refused, the explicit ungoverned state is not. | `require_governing_route` | mcp/src/agents_remember/memory/knowledge/effects.py:544-557 |
| The command-to-kind table read instead of the payload, so a caller cannot store a pair the registry would refuse. | `_COMMAND_DECLARATION` | mcp/src/agents_remember/memory/knowledge/effects.py:121-126 |
| The operation and the generation this module's refusals and writes belong to. | `READ_OPERATION`; `REQUIRED_EFFECT_GENERATION` | mcp/src/agents_remember/memory/knowledge/effects.py:115-115; mcp/src/agents_remember/memory/knowledge/effects.py:116-116 |
| The one place a relation write says which endpoint kinds exist, which this module reuses rather than paralleling. | `require_realization_claim_endpoint`; `require_effect_revision_endpoint`; `require_change_set_endpoint` | mcp/src/agents_remember/memory/knowledge/endpoints.py:172-195; mcp/src/agents_remember/memory/knowledge/endpoints.py:274-305; mcp/src/agents_remember/memory/knowledge/endpoints.py:308-332 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The write path resolves identities inside one
namespace's own store, and the generation it requires is that dataset's own.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T10:37+02:00 — 260915-KS-L13 curator (uncommitted change set on `ar/260915-ks-l13`, base `b5a74aee`): created this one-to-one card for the authored-effect record group's write path, preconditions and read. It records the measured validate-then-resolve-then-deduplicate order, the four resolved reference families against the two deliberately unresolved ones, the one succession edge written with its successor and cycle-checked in the same transaction, the group's own citation-ordering rule, the derived read that refuses by state, and the deliberate absences (no derived label, no derived preservation claim, no promotion). This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
