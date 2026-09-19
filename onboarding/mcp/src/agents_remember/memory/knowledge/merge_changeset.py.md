# mcp/src/agents_remember/memory/knowledge/merge_changeset.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/merge_changeset.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:45+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Base-to-side deltas and the three facts that make one trustworthy**, plus the one place the engine names the row it could not apply. It owns SQLite's session/changeset machinery for the merge: producing a delta, materialising every operation in it before the cursor moves, applying it with an aborting conflict policy, and proving complete coverage by replay.

## Code Commentary

### Logic

`require_session_capability(operation)` reads the selected binding's own compile options rather than guessing from a version, because a wheel built without session support has the classes and not the capability; it returns `session_unavailable_refusal` with the concrete `REQUIRED_SESSION_CAPABILITY` requirement.

`build_delta(side_database, base_database, *, side)` runs the session on a connection whose main database is the **side** with the validated base attached as `BASE_SCHEMA_NAME`, attaches and diffs every canonical table before reading the changeset, then calls `_materialize` so every operation is copied out of the cursor while it is still valid. The side connection is opened read-only: a diff reads both databases and never writes either. **Direction is load-bearing and silent when wrong** — driving the session from the opposite side yields an empty changeset with no error, which is why the caller compares a delta's touched tables against the tables whose rows actually differ.

`apply_changeset(delta, target_path, *, within_transaction=None)` applies with `flags=0`, no filter and a conflict callback that returns `SQLITE_CHANGESET_ABORT` unconditionally. The callback copies the available facts — the conflict code, the table, the operation and `_conflicting_key(change)` — and the first blocking conflict rolls the whole application back rather than continuing with `OMIT` to collect a cosmetically complete list. The application runs inside an explicit `BEGIN`/`COMMIT` this function owns, and `within_transaction` is the caller's own rule over the rows the application just wrote: it runs on the same connection, after the application and **before the commit**, so a rule that refuses turns the whole application into one rolled-back step and the target keeps exactly what it held. Both that rule and the conflict path undo through `_roll_back_if_open`, which asks the connection whether a transaction is still open instead of assuming one — a failed application may already have ended its own transaction, and `ROLLBACK` against a connection with none is an error rather than a no-op.

`replay_delta(delta, base_database, target_path, side_identity)` is the complete-coverage check: apply the delta to a fresh copy of the base and require the side's whole logical dataset. It is deliberately a replay rather than an inspection, because a changeset that omitted a table applies cleanly and reports success — only the resulting dataset can say whether every intended change was carried. The target path must not exist; the copy comes from the base's own bytes, because a base reaching this point is a validated closed snapshot with no journal dependency of its own.

### Conventions

- `MaterializedChange` carries `old` and `new` as positional tuples in declared column order, with three possible value states: a stored SQL value, `None` for a stored SQL `NULL`, and `NOT_SUPPLIED` for a column the changeset does not carry. The distinction between the last two is load-bearing and asserted, because APSW's `no_change` marker is not SQL `NULL`.
- `supplied` names the columns on the operation's *carrying* side — `new` for an insert or an update, `old` for a delete — which is what makes "this operation sets this column" checkable without re-reading the changeset.
- `AppliedChangeset` has **three** outcomes and they are not the same fact: a conflict the engine reported (whose row identity is copied out of the change), the engine's own `detail` when the application failed without invoking the callback at all, and a `refusal` from a caller-supplied check that ran inside the application's own transaction — the operation applied, the caller's rule refused it, and the application was rolled back. A refusal is deliberately not modelled as a conflict: nothing conflicted, everything the engine was given was applied, and what the caller proved afterwards is that the whole application must not stand. `_unapplied_count` reports the count only when SQLite reported one, because `ABORT` raises without a count and some failures raise before any conflict is counted: "SQLite did not report one" is a different fact from zero.

### Invariants And Boundaries

- **It is a changeset, never a patchset.** A patchset carries only the new values, so applying it cannot detect that the target row moved; a changeset carries the original values too, which is what lets the application report a conflict instead of overwriting. The binding asks the session for `changeset()` and never for `patchset()`, and there is no `filter`/`filter_change` argument anywhere on this path.
- **The conflict key is copied, never reconstructed.** `_conflicting_key` reads the **old** values first, because a changeset supplies only the columns an operation changes and a key column is by definition unchanged by an `UPDATE`: the new side of an update carries the not-supplied marker where the key is, so a key read from there would name no row. An `INSERT` is the one operation with no old side, and it carries every column including the key. Copying is also the only option, because an APSW `TableChange` expires when the iterator advances.
- **No filtered application and no partial success.** The single returned conflict action is `ABORT`; a caller never receives a partially applied target, and an application refused by a caller-supplied rule is rolled back for the same reason — the target holds what it held before either way.
- **The key rule is one rule, stated twice for two sides of the same engine callback.** `_conflicting_key` reads the old side first inside the conflict callback, and `MaterializedChange.primary_key()` now reads it the same way for the postcondition check (`self.old if self.old is not None else self.new`): a `DELETE` has only an old side, an `UPDATE` has both and only the old side holds the key, and an `INSERT`, the one operation with no old side, carries every column including the key. The same not-supplied marker that made a new-side read name no row in the callback made the change-applied postcondition read `KEY_NOT_SUPPLIED` for every right-side `UPDATE`, which is what it refused.
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
| The delta: its changeset bytes, its digest and its emptiness. | `MaterializedChange`; `changeset_digest`; `is_empty` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:74-122; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:125-135; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:137-142; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:143-147 |
| One materialised operation and the three-valued semantics of its columns. | `MaterializedChange` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:73-104 |
| The capability check read from the binding's own compile options, the required capability, and the not-supplied marker that is not SQL `NULL`. | `require_session_capability`; `NOT_SUPPLIED` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:185-207; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:61-61 |
| The directional delta build with every canonical table attached before the changeset is read. | `build_delta` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:185-220 |
| The aborting application and the callback that copies the facts it was handed. | `apply_changeset` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:223-263 |
| The conflict key read from the operation's **old** values, with the `INSERT` exception. | `_conflicting_key` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:336-359 |
| The coverage replay that no return code can substitute for. | `replay_delta` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:362-401 |
| What one application attempt did, with the engine's own `detail` and the optional unapplied count. | `_unapplied_count`; `conflicted` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:150-183; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:469-480; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:179-183 |
| The optional unapplied count, distinct from zero. | `_unapplied_count` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:469-480 |
| The session-capability and coverage refusals this module produces. | `session_unavailable_refusal`; `changeset_incomplete_refusal` | mcp/src/agents_remember/memory/knowledge/merge_refusals.py:199-218; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:221-245 |
| The unit node that proves a subset delta is accepted by SQLite and refused by both completeness measures. | "def test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate(" | mcp/tests/test_knowledge_guarded_merge.py:307-376 |
| The boundary nodes that hold the conflict key to the engine's own operation. | "test_a_table_carrying_an_insert_and_a_conflicting_update_names_the_conflicting_row" | mcp/tests/test_knowledge_guarded_merge_boundaries.py:135-162 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T18:04:10+00:00: 260915-KS-L23 residue clearance (seat A, follow-up): the delta row that names `MaterializedChange`, `changeset_digest` and `is_empty` gained the declaration citation `mcp/src/agents_remember/memory/knowledge/merge_changeset.py:74-122` for `MaterializedChange` (the class the row names), beside the three ranges the earlier entry in this pass repointed -- `:125-135` the `Delta` head that holds the changeset bytes, `:137-142` `changeset_digest`, `:143-147` `is_empty`. The reopen item compares the changed construct's declaration line, and the class is declared at 74-122; a citation was **added**, not replaced, so nothing this claim cited was dropped and its wording is unchanged. Verification stamp not advanced: the code is uncommitted and closeout owns the stamp.
- 2026-09-18T17:54:55+00:00: 260915-KS-L23 residue clearance (seat A): `NOT_SUPPLIED` repointed from `merge_changeset.py:60-60` to `merge_changeset.py:61-61` — the new range holds `NOT_SUPPLIED = "<not-supplied>"` itself, not the docstring line above it; `require_session_capability` repointed from `:160-182` to `:185-207` — the new range holds the capability check read from the binding's own compile options, through its `session_unavailable_refusal` return; `changeset_digest` repointed from `:120-123` to `:137-142` — the new range holds the `Delta.changeset_digest` property that hashes the changeset bytes; `is_empty` repointed from `:130-134` to `:143-147` — the new range holds the `Delta.is_empty` property; the delta row's first range repointed from `:108-129` to `:125-135` — that range now holds the `Delta` declaration its own finding names; `conflicted` repointed from `:158-162` to `:179-183` — the new range holds the `AppliedChangeset.conflicted` property rather than the docstring above it; `_unapplied_count` repointed from `:413-424` to `:469-480` — the new range holds the count helper that reports the count only when SQLite reported one. Claim re-read against each construct, wording unchanged. Verification stamp not advanced: the code is uncommitted and closeout owns the stamp.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_conflicting_key` repointed to mcp/src/agents_remember/memory/knowledge/merge_changeset.py:336-359. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `replay_delta` repointed to mcp/src/agents_remember/memory/knowledge/merge_changeset.py:362-401. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_unapplied_count` repointed to mcp/src/agents_remember/memory/knowledge/merge_changeset.py:469-480. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:26+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): recorded the two changes this module's contract gained, both of which the card's account was missing. **The postcondition key now reads the carrying side.** `MaterializedChange.primary_key()` (`merge_changeset.py:96-112`) reads `self.old if self.old is not None else self.new` instead of the new side first, because SQLite reports an `UPDATE`'s new entries with the not-supplied marker exactly where the key is — so every right-side `UPDATE` produced a `changeset_postcondition_failed` naming `<not-supplied>`; the rule is now stated once for the postcondition check as `_conflicting_key` already stated it for the conflict callback, and the Invariants section carries it. **The application is one transaction with the caller's own rule.** `apply_changeset(delta, target_path, *, within_transaction=…)` (`:257-320`) wraps the application in an explicit `BEGIN`/`COMMIT`, runs the caller's rule on the same connection after the application and before the commit, and rolls the whole application back when it refuses; `AppliedChangeset` (`:151-177`) gained the `refusal` field as its **third** outcome (applied-but-refused, rolled back) beside the engine conflict and the engine `detail`, and `_roll_back_if_open` (`:322-334`) asks the connection whether a transaction is open rather than assuming one. The Logic and Conventions sections now state the signature, the third outcome and the ordering guarantee. No row was added, and no existing row, citation or range was rewritten: the ranges in the table above that name `apply_changeset` and `_conflicting_key` were left exactly as they stand because the citation-range repair pass owns them (they have drifted, and that is reported rather than patched here). No verification stamp advanced (the source is uncommitted and closeout owns the stamp).
- 2026-09-17T20:39:57+00:00: Generated citation repair: `_unapplied_count` repointed to mcp/src/agents_remember/memory/knowledge/merge_changeset.py:413-424. No content impact: mechanical anchor-range projection bound to citation source snapshot b181d6d0b4e4cacc1833ff166c579061a1762313f644c682eec8ffc186d8d42f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): citation ranges re-derived against the working tree after this leaf enlarged the modules this card cites (`schema.py` gained the relocated `PRIMARY_KEYS`/`JSON_COLUMNS`, and the knowledge modules and their test modules grew), so ranges that were exact at the base commit no longer held the constructs their rows name. Every re-derived range was verified to contain the construct its own row names; no row, citation or claim was deleted or weakened, and the claim wording was retained where it still holds. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate` in the row 72 of this card from mcp/tests/test_knowledge_guarded_merge.py:183-242 to mcp/tests/test_knowledge_guarded_merge.py:248-250, the extent of the construct the claim is about (the checker named line(s) [19, 248] as its live location)
- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): created this one-to-one card for the new changeset module. It records the three trust facts (a changeset rather than a patchset, operations materialised before the cursor advances, coverage proven by replay rather than by a return code), the silent direction hazard, and the corrected conflict-key contract this leaf's review round 2 produced: the key is copied inside the callback and read from the operation's **old** values, because an `UPDATE`'s new side carries the not-supplied marker where its key columns are, and reconstructing a key from the changeset names a different operation whenever a table carries more than one. It also records the three-valued column semantics (`NOT_SUPPLIED` is not SQL `NULL`) and that an unapplied count is optional rather than zero. Verification metadata remains empty until closeout stamps the code commit.
