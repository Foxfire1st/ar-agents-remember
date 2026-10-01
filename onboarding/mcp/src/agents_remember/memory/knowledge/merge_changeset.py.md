# mcp/src/agents_remember/memory/knowledge/merge_changeset.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Base-to-side deltas and the three facts that make one trustworthy**, plus the one place the engine names the row it could not apply. It owns SQLite's session/changeset machinery for the merge: producing a delta, materialising every operation in it before the cursor moves, applying it with a conflict policy that aborts on everything the caller did not decide, and proving complete coverage by replay.

**One authored decision is the single exception to that policy, and it is bounded to the conflict in hand.** `apply_changeset(..., reconciliations=())` applies the caller's `AuthoredReconciliation` entries only where the decision names exactly the conflict SQLite just reported, records it in `AppliedChangeset.resolved`, and lets the application continue to the *next* conflict — which is refused exactly as before. This is where `OMIT` and `REPLACE` became reachable at all, and only through a decision the caller authored: "the caller reconciled this row explicitly" and "the merge picked a winner" are different facts, and only the first is expressible here.

## Code Commentary

### Logic

`require_session_capability(operation)` reads the selected binding's own compile options rather than guessing from a version, because a wheel built without session support has the classes and not the capability; it returns `session_unavailable_refusal` with the concrete `REQUIRED_SESSION_CAPABILITY` requirement.

`build_delta(side_database, base_database, *, side)` runs the session on a connection whose main database is the **side** with the validated base attached as `BASE_SCHEMA_NAME`, attaches and diffs every canonical table before reading the changeset, then calls `_materialize` so every operation is copied out of the cursor while it is still valid. The side connection is opened read-only: a diff reads both databases and never writes either. **Direction is load-bearing and silent when wrong** — driving the session from the opposite side yields an empty changeset with no error, which is why the caller compares a delta's touched tables against the tables whose rows actually differ.

`apply_changeset(delta, target_path, *, within_transaction=None, reconciliations=())` applies with `flags=0`, no filter and a conflict callback that returns `SQLITE_CHANGESET_ABORT` **unless** `_authored_decision` matches the conflict in hand. The callback copies the available facts — the conflict code, the table, the operation and `_conflicting_key(change)` — and the first blocking conflict rolls the whole application back rather than continuing with `OMIT` to collect a cosmetically complete list. When the caller's decision matches, the callback returns `_OMIT` for `keep-left` (the left's stored value stands) or `_REPLACE` for `keep-right` (the arriving change is applied over it), records a `ResolvedConflict` in `AppliedChangeset.resolved`, and the application continues. The decisions
arrive as a **sequence** rather than as one, because one retained conflict is rarely the last one: a decision that
settles the first reveals the second, and the attempt that answers the second has to carry the first, or the merge
re-refuses the row the first decision already answered and the two alternate forever. Each decision still answers
only the row it named.

`_authored_decision` is the whole matching rule, and which shape can match is a property of the conflict rather than of the caller's intent: a conflict the engine attributed to a row is answered only by a decision naming that exact table and rendered key, and a conflict the engine reported without a change is answered only by the row-less decision. Nothing else matches, so a decision always applies to the conflict the caller read and never to a neighbouring one.

**The row-less decision cannot be settled by `OMIT` alone, so it is retracted explicitly.** Measured on this schema, returning `OMIT` for the foreign-key conflict committed the application with the violating row still there. `_retract_referential_rows` therefore identifies the row afterwards, by the violation SQLite left behind (`PRAGMA foreign_key_check`), and deletes it — but only a row the *arriving* delta **inserted**, matched by `_delta_inserted_keys` and re-read through `_row_record_id` exactly the way the delta renders a key. An insertion is the one operation whose retraction removes exactly what arrived and nothing else: retracting an arriving `UPDATE` would mean restoring the value it overwrote, which this layer cannot do because the stored value is the left's, and deleting the row instead would remove content the left authored. A violation no arriving insertion accounts for returns `None`, and the caller refuses the whole application with the conflict it started from. The `_MAX_RETRACTION_PASSES` bound exists so a reference cycle refuses instead of looping. The application runs inside an explicit `BEGIN`/`COMMIT` this function owns, and `within_transaction` is the caller's own rule over the rows the application just wrote: it runs on the same connection, after the application and **before the commit**, so a rule that refuses turns the whole application into one rolled-back step and the target keeps exactly what it held. Both that rule and the conflict path undo through `_roll_back_if_open`, which asks the connection whether a transaction is still open instead of assuming one — a failed application may already have ended its own transaction, and `ROLLBACK` against a connection with none is an error rather than a no-op.

`replay_delta(delta, base_database, target_path, side_identity)` is the complete-coverage check: apply the delta to a fresh copy of the base and require the side's whole logical dataset. It is deliberately a replay rather than an inspection, because a changeset that omitted a table applies cleanly and reports success — only the resulting dataset can say whether every intended change was carried. The target path must not exist; the copy comes from the base's own bytes, because a base reaching this point is a validated closed snapshot with no journal dependency of its own.

### Conventions

- `MaterializedChange` carries `old` and `new` as positional tuples in declared column order, with three possible value states: a stored SQL value, `None` for a stored SQL `NULL`, and `NOT_SUPPLIED` for a column the changeset does not carry. The distinction between the last two is load-bearing and asserted, because APSW's `no_change` marker is not SQL `NULL`.
- `supplied` names the columns on the operation's *carrying* side — `new` for an insert or an update, `old` for a delete — which is what makes "this operation sets this column" checkable without re-reading the changeset.
- `AppliedChangeset` has **three** outcomes and they are not the same fact: a conflict the engine reported (whose row identity is copied out of the change), the engine's own `detail` when the application failed without invoking the callback at all, and a `refusal` from a caller-supplied check that ran inside the application's own transaction — the operation applied, the caller's rule refused it, and the application was rolled back. `resolved` is orthogonal to all three: it names every conflict an authored decision settled instead of aborting, so the merge's own postcondition check can tell "the engine dropped this operation" from "the caller decided this row". `ResolvedConflict.record_id` is rendered the way the refusal renders it — primary key values joined with `/` — so the record the caller decided and the record the postcondition looks for are one string rather than two spellings of one row, and its `reason` is empty for a row-attributed conflict and names what was removed for a retraction. A refusal is deliberately not modelled as a conflict: nothing conflicted, everything the engine was given was applied, and what the caller proved afterwards is that the whole application must not stand. `_unapplied_count` reports the count only when SQLite reported one, because `ABORT` raises without a count and some failures raise before any conflict is counted: "SQLite did not report one" is a different fact from zero.

### Invariants And Boundaries

- **It is a changeset, never a patchset.** A patchset carries only the new values, so applying it cannot detect that the target row moved; a changeset carries the original values too, which is what lets the application report a conflict instead of overwriting. The binding asks the session for `changeset()` and never for `patchset()`, and there is no `filter`/`filter_change` argument anywhere on this path.
- **The conflict key is copied, never reconstructed.** `_conflicting_key` reads the **old** values first, because a changeset supplies only the columns an operation changes and a key column is by definition unchanged by an `UPDATE`: the new side of an update carries the not-supplied marker where the key is, so a key read from there would name no row. An `INSERT` is the one operation with no old side, and it carries every column including the key. Copying is also the only option, because an APSW `TableChange` expires when the iterator advances.
- **No filtered application and no partial success.** The returned conflict action is `ABORT` for every conflict the caller did not decide; a caller never receives a partially applied target, and an application refused by a caller-supplied rule is rolled back for the same reason — the target holds what it held before either way.
- **`OMIT` and `REPLACE` are unreachable without an authored decision naming exactly that row.** The package still never drops a conflicting operation on its own judgement and never replaces one side's value as an automatic resolution; the only thing that reaches either action is `_authored_decision` matching the conflict in hand.
- **A retraction is bounded to an arriving INSERT.** `_retract_referential_rows` deletes only a row the arriving delta inserted and only while SQLite reports it as breaking a declared reference; an arriving `UPDATE` or `DELETE` is not a candidate, because the reconciled answer there would be to restore content the left authored — which is the orientation this change deliberately leaves refused.
- **The key rule is one rule, stated twice for two sides of the same engine callback.** `_conflicting_key` reads the old side first inside the conflict callback, and `MaterializedChange.primary_key()` now reads it the same way for the postcondition check (`self.old if self.old is not None else self.new`): a `DELETE` has only an old side, an `UPDATE` has both and only the old side holds the key, and an `INSERT`, the one operation with no old side, carries every column including the key. The same not-supplied marker that made a new-side read name no row in the callback made the change-applied postcondition read `KEY_NOT_SUPPLIED` for every right-side `UPDATE`, which is what it refused.
- **Boundary.** This module produces and applies deltas and proves coverage. It does not choose a base, decide a conflict policy at the operation level, validate the merged candidate's postconditions, or publish.

### Todos

None recorded for this slice.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The delta: its changeset bytes, its digest and its emptiness. [1]
- One materialised operation and the three-valued semantics of its columns. [2]
- The capability check read from the binding's own compile options, the required capability, and the not-supplied marker that is not SQL `NULL`. [3]
- The directional delta build with every canonical table attached before the changeset is read. [4]
- **The application whose conflict policy aborts on everything the caller did not decide, and the one authored decision that is the exception.** [5]
- **The whole matching rule: which shape of decision can answer which shape of conflict.** [6]
- **The retraction of a row-less referential conflict, bounded to rows the arriving delta inserted.** [7]
- **One conflict an authored decision settled, with the row identity the engine supplied and the reason a retraction removed it.** [8]
- The conflict key read from the operation's **old** values, with the `INSERT` exception. [9]
- The coverage replay that no return code can substitute for. [10]
- What one application attempt did, with the engine's own `detail`, the authored decisions it settled, and the optional unapplied count. [11]
- The session-capability and coverage refusals this module produces. [12]
- The unit node that proves a subset delta is accepted by SQLite and refused by both completeness measures. [13]
- The boundary nodes that hold the conflict key to the engine's own operation. [14]
- **The integration cases that drive one authored decision through this application, including the row-less retraction, the orientation where that retraction is unavailable, and the schema refusal that admits no decision at all.** [15]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
