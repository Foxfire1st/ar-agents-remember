# mcp/src/agents_remember/application/knowledge_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:20+02:00 |
| lastVerifiedCommitHash |  `b5a74aee6cdf671c9963f3aba4df6d44b856f697`|
| lastVerifiedCommitDate |  2026-09-18T09:42:44+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l12` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

The application seam for the evidence-specific selection: one explicit context, one seed, one complete
page. It decides no authority and holds no durable state.

## Code Commentary

### Logic

`read_evidence_scope` is the narrow API a caller uses. It is the seventh application seam beside the
knowledge, snapshot, merge, export, read, facet and detection surfaces, and like them it admits a context,
delegates selection to the memory layer and returns the typed result unchanged.

Three boundaries this module owns, each because getting it wrong is a different kind of wrong:

1. **The read is read-only, and that is how a refusal persists nothing.** The connection is opened through
   the shipped read-only opener, so the strongest statement available to this operation is a `SELECT`. "A
   refused evidence read left the file byte-identical" is therefore a property of the handle rather than a
   rollback this code has to remember.
2. **The declared snapshot is verified before anything is selected.** `_read_inside_snapshot` requires the
   file to be bound to the requested namespace, to implement the schema generation the context declares, and
   to hold the declared logical dataset — the same three comparisons the recorded-scope read and the facet
   read make, for the same reason: a context describing another dataset is refused by name rather than
   answered from whatever bytes the path happens to hold.
3. **The artifact resolution is a read-time fact and never a rewrite.** A caller may declare a local
   artifact root so a recorded repository-relative path can be resolved against real bytes; the resolution
   is reported as its own state and the stored record is served exactly as it was written, whatever the
   resolution says.

`_absence_refusal`, `_snapshot_identity_refusal`, `_unusable_snapshot` and `_refused` are the seam's own
refusal shapes, so every failure leaves through the shipped `KnowledgeRefusal` vocabulary rather than as an
exception.

This operation does not touch the recorded-scope selection or the facet selection in any way: it does not
call either, shares no policy name with either, and appears in neither's response.

### Conventions

One function per operation, with the private helpers below it and `_OPERATION` naming the operation in every
refusal the seam itself builds. The module's `__all__` is the seam's public surface.

### Invariants And Boundaries

- **No authority is decided here.** The context is admitted by the caller's own boundary; this module
  verifies identity and selects, and never authenticates.
- **A refused read writes nothing**, by construction of the handle rather than by a compensating action.
- **The seam is thin on purpose**: selection logic belongs to the memory layer and the declared contract to
  the models; this file only admits, delegates and refuses.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one operation this seam exposes. | `read_evidence_scope` | mcp/src/agents_remember/application/knowledge_evidence.py:72-121 |
| The three identity comparisons made before anything is selected, and the refusals that name them. | `_read_inside_snapshot`; `_snapshot_identity_refusal` | mcp/src/agents_remember/application/knowledge_evidence.py:126-160; mcp/src/agents_remember/application/knowledge_evidence.py:191-224 |
| The absent-selection refusal and the refusal builder the seam's own failures leave through. | `_absence_refusal`; `_refused` | mcp/src/agents_remember/application/knowledge_evidence.py:163-187; mcp/src/agents_remember/application/knowledge_evidence.py:244-255 |
| The read-only open that makes "a refused read persists nothing" a property of the handle. | `open_read_only_database` | mcp/src/agents_remember/memory/knowledge/connection.py:52-60 |
| The selection this seam delegates to. | `select_evidence_scope` | mcp/src/agents_remember/memory/knowledge/evidence_read.py:112-133 |
| The case that asserts the read refuses a database that is not the selected snapshot. | "def test_the_read_refuses_a_database_that_is_not_the_selected_snapshot(" | mcp/tests/test_knowledge_evidence_claims.py:838-867 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T06:20+02:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): created this one-to-one card for the evidence application seam. It records the read-only handle as the reason a refused read persists nothing, the three snapshot-identity comparisons, and the rule that artifact resolution is a read-time fact and never a rewrite. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
