# mcp/src/agents_remember/memory/knowledge/merge_refusals.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/merge_refusals.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:45+02:00 |
| lastVerifiedCommitHash | `4904e08f0668ed6d11a2c44d0118716bb82f735c`|
| lastVerifiedCommitDate | 2026-09-17T22:32:32+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The refusal vocabulary of the guarded common-base merge: one factory per observable failure point.** They live in one module so the codes, the offending record and the advertised next action stay together instead of being spelled out at each call site. The shared `refusal` factory and the exception types stay in `refusals.py`; this module only names the failures a merge can observe.

Ten factories, and two of them are **structural** refusals in the strong sense: a schema disagreement and a missing canonical table are refused **before a session exists**, because SQLite's changeset application can skip a table it cannot match and still report success. The rest refuse an application or a validation that ran against the result, and every one of them leaves the caller's inputs untouched.

## Code Commentary

### Logic

- `schema_mismatch_refusal` → `schema_mismatch`. An input whose structure is not the supported generation. A version string is not the check: two databases can both say `user_version = 1` and disagree about a column type, a foreign key or a trigger. The refused input is not migrated, repaired or re-created.
- `missing_required_table_refusal` → `missing_required_table`. An input that lacks a canonical table the merge would have to carry changes for. It gets its own code because the failure it prevents is the silent one: a changeset whose table does not exist on the target is either an error or — worse — no operation at all.
- `conflicting_values_refusal` → `conflicting_values`. Both sides changed the same field of the same row differently. The whole application is rolled back and neither side is preferred: latest-writer-wins is not a policy this operation implements.
- `duplicate_identity_refusal` → `duplicate_identity`. Both sides independently inserted the same identity — **even when the two payloads are equal**. Two independent insertions of one identity are two authored acts that happen to collide; treating them as one because the bytes match would be this operation deciding that two authors meant the same thing.
- `delete_reference_conflict_refusal` → `delete_reference_conflict`. One side removed a row the other side's new row still references, in **both** orientations, because SQLite reports the same foreign-key fact whichever side performed the removal. The row-level identity is deliberately absent: for a foreign-key conflict the engine hands the callback no change at all, so naming a row would be this operation's guess rather than the engine's report.
- `duplicate_relationship_refusal` → `duplicate_relationship`. The union duplicates a unique declared relationship under new identities.
- `immutable_revision_changed_refusal` → `immutable_revision_changed`. An input that altered an immutable revision in place behind its identity. It fires even when the file passes its own `integrity_check`: the row is well formed and its content is not what the base sealed. The compared value is the stored payload digest, so re-stating the same payload in different JSON key order is not a change.
- `session_unavailable_refusal` → `session_unavailable`. The selected binding/build cannot produce or apply a changeset at all. It is a capability failure with a concrete installation requirement, not a fallback opportunity: there is one supported binding, and a build without session support refuses rather than switching to a second mechanism.
- `changeset_incomplete_refusal` → `changeset_incomplete`. A delta that did not prove complete coverage of its base-to-side change — the class of failure SQLite reports as success.
- `changeset_postcondition_failed_refusal` → `changeset_postcondition_failed`. A merge whose applied result does not carry an intended change. The check is over the *result*, not over the return code.

### Conventions

- Each factory is named `<code>_refusal` and takes the operation plus the exact facts that produced the refusal, so the caller reads a factory name rather than assembling a code string.
- Facts are passed through `RefusalFacts` with the fields the failure actually has: `record_id` where the engine or the comparison named a row, `table` where the table is known, and nothing invented to fill a gap the engine left.
- `KEY_NOT_SUPPLIED`'s sibling in `merge.py` exists for the same reason as `delete_reference_conflict_refusal`'s absent row: an unreadable key is reported as naming no row rather than as some nearby row.

### Invariants And Boundaries

- **A refusal is a returned value, never an exception.** The caller branches on `code`.
- **No refusal modifies an input.** Every factory here is constructed after the fact; none of them repairs, deletes or rewrites anything.
- **No refusal carries a verdict.** Nothing here says a merge is compatible, acceptable or harmless; the codes name structural facts only.
- **A foreign-key refusal names no row and reports no count.** The pinned binding raises `ConstraintError` with no count in its arguments, so a number there would be the operation's own inference rather than the engine's report.
- **Boundary.** This module declares and builds merge refusals. It does not detect the failures, decide policy, map SQLite errors (`map_sqlite_error` in `refusals.py` does that) or publish.

### Todos

None recorded for this slice.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two structural refusals that run before a session exists. | `schema_mismatch_refusal`; `missing_required_table_refusal` | mcp/src/agents_remember/memory/knowledge/merge_refusals.py:21-45; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:48-67 |
| The conflict refusals that roll the whole application back rather than preferring a side. | `conflicting_values_refusal`; `duplicate_identity_refusal`; `delete_reference_conflict_refusal`; `duplicate_relationship_refusal` | mcp/src/agents_remember/memory/knowledge/merge_refusals.py:70-94; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:97-121; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:124-151; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:154-173 |
| The input-integrity refusal that fires even when the file passes its own `integrity_check`. | `immutable_revision_changed_refusal` | mcp/src/agents_remember/memory/knowledge/merge_refusals.py:176-196 |
| The capability refusal with a concrete installation requirement rather than a fallback. | `session_unavailable_refusal` | mcp/src/agents_remember/memory/knowledge/merge_refusals.py:199-218 |
| The two result-side refusals: incomplete coverage, and a result missing an intended change. | `changeset_incomplete_refusal`; `changeset_postcondition_failed_refusal` | mcp/src/agents_remember/memory/knowledge/merge_refusals.py:221-245; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:248-270 |
| The shared factory and the SQLite-error mapper this module deliberately leaves where they are. | `refusal`; `map_sqlite_error` | mcp/src/agents_remember/memory/knowledge/refusals.py:57-77; mcp/src/agents_remember/memory/knowledge/refusals.py:828-871 |
| The codes these factories produce, one per observable failure point. | `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:66-111 |
| The taxonomy in the operation that maps an application failure onto one of these factories. | `_TAXONOMY` | mcp/src/agents_remember/memory/knowledge/merge.py:650-655 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T20:39:57+00:00: Generated citation repair: `_TAXONOMY` repointed to mcp/src/agents_remember/memory/knowledge/merge.py:650-655. No content impact: mechanical anchor-range projection bound to citation source snapshot b181d6d0b4e4cacc1833ff166c579061a1762313f644c682eec8ffc186d8d42f; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): created this one-to-one card for the new refusal module. It records all ten factories with the code each produces and the fact each deliberately does **not** state — most importantly that a same-ID independent insert refuses even when both payloads are byte-identical (two authored acts that collide are not one act), that the delete-versus-reference refusal is orientation-independent and names no row because the engine hands the callback no change, and that a foreign-key refusal carries no violation count because the pinned binding reports none. It also records that a refusal is a returned value rather than an exception, that no refusal modifies an input, and that no refusal carries a verdict. Verification metadata remains empty until closeout stamps the code commit.
