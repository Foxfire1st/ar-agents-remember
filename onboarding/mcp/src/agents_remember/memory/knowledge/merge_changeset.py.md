# mcp/src/agents_remember/memory/knowledge/merge_changeset.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/merge_changeset.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:45+02:00 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Base-to-side deltas and the three facts that make one trustworthy**, plus the one place the engine names the row it could not apply. It owns SQLite's session/changeset machinery for the merge: producing a delta, materialising every operation in it before the cursor moves, applying it with an aborting conflict policy, and proving complete coverage by replay.

## Code Commentary

### Logic

`require_session_capability(operation)` reads the selected binding's own compile options rather than guessing from a version, because a wheel built without session support has the classes and not the capability; it returns `session_unavailable_refusal` with the concrete `REQUIRED_SESSION_CAPABILITY` requirement.

`build_delta(side_database, base_database, *, side)` runs the session on a connection whose main database is the **side** with the validated base attached as `BASE_SCHEMA_NAME`, attaches and diffs every canonical table before reading the changeset, then calls `_materialize` so every operation is copied out of the cursor while it is still valid. The side connection is opened read-only: a diff reads both databases and never writes either. **Direction is load-bearing and silent when wrong** — driving the session from the opposite side yields an empty changeset with no error, which is why the caller compares a delta's touched tables against the tables whose rows actually differ.

`apply_changeset(delta, target_path)` applies with `flags=0`, no filter and a conflict callback that returns `SQLITE_CHANGESET_ABORT` unconditionally. The callback copies the available facts — the conflict code, the table, the operation and `_conflicting_key(change)` — and the first blocking conflict rolls the whole application back rather than continuing with `OMIT` to collect a cosmetically complete list.

`replay_delta(delta, base_database, target_path, side_identity)` is the complete-coverage check: apply the delta to a fresh copy of the base and require the side's whole logical dataset. It is deliberately a replay rather than an inspection, because a changeset that omitted a table applies cleanly and reports success — only the resulting dataset can say whether every intended change was carried. The target path must not exist; the copy comes from the base's own bytes, because a base reaching this point is a validated closed snapshot with no journal dependency of its own.

### Conventions

- `MaterializedChange` carries `old` and `new` as positional tuples in declared column order, with three possible value states: a stored SQL value, `None` for a stored SQL `NULL`, and `NOT_SUPPLIED` for a column the changeset does not carry. The distinction between the last two is load-bearing and asserted, because APSW's `no_change` marker is not SQL `NULL`.
- `supplied` names the columns on the operation's *carrying* side — `new` for an insert or an update, `old` for a delete — which is what makes "this operation sets this column" checkable without re-reading the changeset.
- `AppliedChangeset.detail` carries the engine's own message when the application failed **without** invoking the conflict callback at all, so a caller always has a reason even when there was no conflict to report. `_unapplied_count` reports the count only when SQLite reported one, because `ABORT` raises without a count and some failures raise before any conflict is counted: "SQLite did not report one" is a different fact from zero.

### Invariants And Boundaries

- **It is a changeset, never a patchset.** A patchset carries only the new values, so applying it cannot detect that the target row moved; a changeset carries the original values too, which is what lets the application report a conflict instead of overwriting. The binding asks the session for `changeset()` and never for `patchset()`, and there is no `filter`/`filter_change` argument anywhere on this path.
- **The conflict key is copied, never reconstructed.** `_conflicting_key` reads the **old** values first, because a changeset supplies only the columns an operation changes and a key column is by definition unchanged by an `UPDATE`: the new side of an update carries the not-supplied marker where the key is, so a key read from there would name no row. An `INSERT` is the one operation with no old side, and it carries every column including the key. Copying is also the only option, because an APSW `TableChange` expires when the iterator advances.
- **No filtered application and no partial success.** The single returned conflict action is `ABORT`; a caller never receives a partially applied target.
- **Boundary.** This module produces and applies deltas and proves coverage. It does not choose a base, decide a conflict policy at the operation level, validate the merged candidate's postconditions, or publish.

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
| The delta: its changeset bytes, its digest and its emptiness. | `MaterializedChange`; `changeset_digest`; `is_empty` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:108-129; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:120-123; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:126-129 |
| One materialised operation and the three-valued semantics of its columns. | `MaterializedChange` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:73-104 |
| The capability check read from the binding's own compile options, the required capability, and the not-supplied marker that is not SQL `NULL`. | `require_session_capability`; `NOT_SUPPLIED` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:160-182; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:59-59 |
| The directional delta build with every canonical table attached before the changeset is read. | `build_delta` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:185-220 |
| The aborting application and the callback that copies the facts it was handed. | `apply_changeset` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:223-263 |
| The conflict key read from the operation's **old** values, with the `INSERT` exception. | `_conflicting_key` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:266-289 |
| The coverage replay that no return code can substitute for. | `replay_delta` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:292-331 |
| What one application attempt did, with the engine's own `detail` and the optional unapplied count. | `_unapplied_count`; `conflicted` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:133-157; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:393-404; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:154-157 |
| The optional unapplied count, distinct from zero. | `_unapplied_count` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:393-404 |
| The session-capability and coverage refusals this module produces. | `session_unavailable_refusal`; `changeset_incomplete_refusal` | mcp/src/agents_remember/memory/knowledge/merge_refusals.py:199-218; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:221-245 |
| The unit node that proves a subset delta is accepted by SQLite and refused by both completeness measures. | "test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate" | mcp/tests/test_knowledge_guarded_merge.py:248-250 |
| The boundary nodes that hold the conflict key to the engine's own operation. | "test_a_table_carrying_an_insert_and_a_conflicting_update_names_the_conflicting_row" | mcp/tests/test_knowledge_guarded_merge_boundaries.py:135-162 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate` in the row 72 of this card from mcp/tests/test_knowledge_guarded_merge.py:183-242 to mcp/tests/test_knowledge_guarded_merge.py:248-250, the extent of the construct the claim is about (the checker named line(s) [19, 248] as its live location)
- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): created this one-to-one card for the new changeset module. It records the three trust facts (a changeset rather than a patchset, operations materialised before the cursor advances, coverage proven by replay rather than by a return code), the silent direction hazard, and the corrected conflict-key contract this leaf's review round 2 produced: the key is copied inside the callback and read from the operation's **old** values, because an `UPDATE`'s new side carries the not-supplied marker where its key columns are, and reconstructing a key from the changeset names a different operation whenever a table carries more than one. It also records the three-valued column semantics (`NOT_SUPPLIED` is not SQL `NULL`) and that an unapplied count is optional rather than zero. Verification metadata remains empty until closeout stamps the code commit.
