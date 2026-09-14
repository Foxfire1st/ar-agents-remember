# mcp/src/agents_remember/worktrees/ledger_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/ledger_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T17:20+02:00 |
| lastVerifiedCommitHash | `270704b86116728a64ada83ee258a0e7726206b4` |
| lastVerifiedCommitDate | 2026-09-14T18:18:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees route overview](overview.md)

## Purpose

Projects the external-memory `memory.md` ledger from its **source** plus the branch's own true
mappings, so closeout recomputes the table instead of read-and-re-stamping whatever the file
currently says. The ledger is derived state: the developer ruling on the 260713 super line
records that every closeout following a `worktree_sync` merges two ledgers by hand, and that the
mechanics of that merge produced three real errors in one day — a superseded row kept, rows
ordered so the validator rejects them, and a header disagreeing with its own first row. None of
the three needed judgement, so the projection owns the deterministic form `validate_ledger` and
the integration-side check already enforced: the complete source ledger as the trailing rows in
source order, the branch's own true mappings ahead of that tail newest-first, and a header naming
the projection's first row.

Since 260913-LCA-L2 the **source** half of that is itself derived from the memory commits' own
`Code-Commit:` trailers, read back through `kernel/memory_attribution.py::attributed_commits`.

**Since 260913-LCA-L11 the source read is the union of two records, and the blob is read in every
case.** `read_ledger_source` asks the source's own table what rows it recorded
(`_rows_the_source_records`, an unvalidated read of `commit:memory.md`) and merges the trailers'
rows into that list, keeping the table's order and counting each mapping once. The earlier form
returned the trailers **alone** as soon as the history carried a single one, which made the blob a
"fallback" that a partially backfilled line never reached — see the defect below. A row whose memory
commit the exact source commit does not carry is excluded at the read rather than carried into the
projection to be dropped there, and every exclusion travels back to the caller with its reason.
The tracked ledger commit is **not** retired by either change: `memory.md` is still written,
committed and proved by the closeout family.

Since 260913-LCA-L3 the module no longer declares the ledger's path. `LEDGER_RELATIVE_PATH` is
imported from `kernel/memory_ledger.py` and re-exported through that import, so this module's own
default (`read_ledger_source`, `_rows_the_source_records`, `observed_ledger_state`) and every caller
that names it from here are unchanged, while the kernel's tracker of the same table no longer has to
reach into `worktrees/` for a filename.

Nothing here reads or writes onboarding prose. The projection owns the mapping table and its
header alone.

## Code Commentary

### Logic

A mapping the branch claims is *true* only when the code repository really holds its code commit
and its memory commit is reachable from the memory state the ledger is written for.
`_own_row_candidates` cit:([`_own_row_candidates`], mcp/src/agents_remember/worktrees/ledger_projection.py:644-661) keeps the source rows and the branch's own
candidates, `_untrue_reason` cit:([`_untrue_reason`], mcp/src/agents_remember/worktrees/ledger_projection.py:681-686) names `code-commit-missing` or
`memory-commit-unreachable` for each dropped row, and `_newest_first` cit:([`_newest_first`], mcp/src/agents_remember/worktrees/ledger_projection.py:689-707) orders the branch's
own true rows ahead of the source tail. Untrue rows are dropped (that is how a superseded row
leaves the table), duplicated source rows are collapsed, and a table whose tail is not the source
is reordered. Only an input that cannot be read at all refuses, and each refusal names its remedy.

`project_ledger` cit:([`project_ledger`], mcp/src/agents_remember/worktrees/ledger_projection.py:579-641) assembles the result;
`LedgerProjection` cit:([`LedgerProjection`], mcp/src/agents_remember/worktrees/ledger_projection.py:146-271) carries the source, the observed rows and bytes, the projected
table, and the difference between them. Three questions are answered separately, because they are
different claims:

- `is_fixed_point` cit:([`is_fixed_point`], mcp/src/agents_remember/worktrees/ledger_projection.py:169-179) — is the observed table already *its own* projection, rows and
  header, semantically rather than byte-exact?
- `is_interleaved_projection` cit:([`is_interleaved_projection`], mcp/src/agents_remember/worktrees/ledger_projection.py:180-212) — is it that projection with the branch's own rows
  placed elsewhere? A master's ledger does not arrive the way a leaf's does: a leaf's closeout
  *writes* the table, while a master's line accumulates one closeout per leaf and can absorb its
  own source through a merge, so a union merge can interleave the two sides' rows instead of
  stacking them. The weaker question keeps the content promise — no row added, dropped, replaced,
  duplicated or untrue, source rows still in source order — and leaves only placement to the
  merge. Order is not otherwise free, because a reader resolves a code commit to the FIRST row
  naming it, so the accepted table must resolve every code commit the way the projection does.
- `needs_write` cit:([`needs_write`], mcp/src/agents_remember/worktrees/ledger_projection.py:223-231) — are the bytes on disk not the canonical rendering? The closeout
  writer is the one caller that must decide whether to touch the file at all, and a table already
  correct stays byte-identical and produces no ledger commit.

`operator_payload` cit:([`operator_payload`], mcp/src/agents_remember/worktrees/ledger_projection.py:233-258) renders what recomputation changed in row terms —
`rowsAdded`, `rowsRemoved`, `rowsReordered`, `removedReasons`, the header before/after and the
row counts — bounding the row lists at `_PAYLOAD_ROW_LIMIT` so a pathological ledger cannot
inflate a tool response.

`observed_ledger_state` cit:([`observed_ledger_state`], mcp/src/agents_remember/worktrees/ledger_projection.py:547-576) is the one place that decides **which bytes are observed and which
memory state the rows must be true against**, and it answers for both contract shapes. A leaf
writes its ledger inside its own memory worktree, so the file on disk is the observed table and
`head_commit(memory_worktree)` is the reachable state. A series owns no memory worktree at all,
so it reads the blob at the exact memory work-branch tip (`memory_work_branch` via
`require_git(["show", f"{tip}:{LEDGER_RELATIVE_PATH}"])`) and uses that same tip as the reachable
state: the tip is the artifact its closeout records and its integration lands. Reading the live
file for a series is not an option — there is none — and reading a stale one would be worse,
because the evidence would describe a table the contract no longer names.

**The source ledger is the source's own recorded table with the attributed rows merged into it.**
`read_ledger_source` cit:([`read_ledger_source`], mcp/src/agents_remember/worktrees/ledger_projection.py:302-350) asks
`kernel/memory_attribution.attributed_commits` for the commits reachable from the exact commit it
was given, turns them into rows with `ledger_rows_from_attribution`, and independently reads the
rows **that commit's own table records** through
`_rows_the_source_records` cit:([`_rows_the_source_records`], mcp/src/agents_remember/worktrees/ledger_projection.py:393-420) — deliberately with the
unvalidated parse, because a header disagreeing with its own first row is one of the shapes the
projection repairs. `_tail_rows` cit:([`_tail_rows`], mcp/src/agents_remember/worktrees/ledger_projection.py:353-383) then returns the union in the
table's order (`_distinct` cit:([`_distinct`], mcp/src/agents_remember/worktrees/ledger_projection.py:386-390) keeps the first occurrence, so a
mapping the table already records is not counted twice), **keeping only rows the exact source
commit carries** and returning every other row as a `LedgerRowRemoval` with reason
`memory-commit-unreachable`. `_source_ledger_with_rows` cit:([`_source_ledger_with_rows`], mcp/src/agents_remember/worktrees/ledger_projection.py:423-441) supplies
**rows only**; the metadata fields are left empty because no trailer records them, and
`project_ledger` recomputes the header from row one while keeping the observed table's own
`repoName` and base fields, which is the one promise `validate_ledger` makes about a header. Two
inputs still refuse: a history the attribution module cannot walk (its error is converted into a
`LedgerProjectionRefusal` carrying `_SOURCE_REMEDY`), and a blob that exists and cannot be parsed.
A commit that carries no ledger blob at all contributes no rows, which is the bootstrap state the
ledger-creation paths start from.

**The reader's second defect, recorded because it is the expensive shape of a missing
attribution (260913-LCA-L11).** The earlier reader returned the trailers *alone* as soon as the
history carried one — `if attributed:` immediately returning `LedgerSource(commit, _source_ledger_with_rows(attributed))`
— so the blob was reachable only for a history that carried *no* trailer at all. The developer's
ruling named the removal of the integration-side file rule, not this; the worker found it while
reproducing the ruling, and it is the more dangerous half: a missed entry looks exactly like "no
attribution exists". **Measured by the worker on the master's source: `f5edc613` records 479 rows
of which exactly ONE commit carries a trailer, so the old reader returned a ONE-ROW source and
every pre-rule row vanished from the tail.** The curator re-verified both halves independently
against the official memory repository (`git show f5edc613:memory.md` parsed as the ledger parser
does → 479 data rows; `git log --format=%(trailers:key=Code-Commit,valueonly) f5edc613` → exactly
one commit with a non-empty value, `02ed1fbc` trailing `4214d7a1`), and re-derived the read's own
split with `git merge-base --is-ancestor` row by row → **466 kept + 13 excluded**, the same figures
the worker reported. The blob read is the COMMON case now and not a fallback *mode*: the trailers
are merged into it, so a partially backfilled history reads as the union its own table records.

Two consequences are load-bearing. The projection's trailing rows are now the *mapping the history
carries* rather than the bytes a previous round wrote down, so a hand edit to the table cannot move
them. And the exclusion is reported rather than performed in silence: `LedgerSource` carries
`excluded_rows` and `trailered_commits`, and `operator_payload` surfaces `sourceRowsExcluded`,
`sourceExcludedRows`, `sourceExcludedReasons` and `sourceTraileredCommits`, so a caller can tell a
partially backfilled line from a line the trailer rule never reached — which is exactly what the
rows alone cannot say. The two historical measurements this card used to carry (0 of 958 reachable
memory commits trailered at tip `5e4899ea`, so the blob read was the live path) were taken before
the backfill reached the line and remain true *of that commit*; at `f5edc613` the line is partially
backfilled (1 trailered commit of 965 reachable) and the union read is what returns its 466 rows.

`contract_ledger_projection` cit:([`contract_ledger_projection`], mcp/src/agents_remember/worktrees/ledger_projection.py:514-544) builds the one projection for a live external-memory
contract: the source rows come from `read_ledger_source` at
`resolve_memory_source_commit` cit:([`resolve_memory_source_commit`], mcp/src/agents_remember/worktrees/ledger_projection.py:274-299), the observed table and reachable state from
`observed_ledger_state`, and row truth from `code_commit_exists` cit:([`code_commit_exists`], mcp/src/agents_remember/worktrees/ledger_projection.py:483-486) — which now
delegates to the attribution module's single `cat-file -e` definition instead of repeating it —
plus `is_ancestor`. A memory source that resolves but carries no ledger yet (the bootstrap state)
contributes no rows instead of refusing. `read_ledger_text` cit:([`read_ledger_text`], mcp/src/agents_remember/worktrees/ledger_projection.py:467-480) deliberately uses the
**unvalidated** parse, because a header disagreeing with its own first row is one of the shapes
the repair exists to fix; structural damage still refuses. `inspect_ledger_projection` cit:([`inspect_ledger_projection`], mcp/src/agents_remember/worktrees/ledger_projection.py:489-511)
reports diverged/already-correct evidence for the re-run and recovery paths without writing, and
**never raises**, because it is evidence about a completed step rather than a new gate on it.

### Conventions

A `@dataclass(frozen=True)` result family — `LedgerSource`, `LedgerWorld`, `LedgerRowRemoval`,
`LedgerProjection` — over plain functions, with `LEDGER_RELATIVE_PATH` imported from
`kernel/memory_ledger.py` and re-exported by that import alone
cit:([`LEDGER_RELATIVE_PATH`], mcp/src/agents_remember/worktrees/ledger_projection.py:44-63). The declaration lives in the
kernel because the path is a property of the ledger **format** rather than of this projection, so a
kernel-level reader of the same table needs no feature-package import; every caller that already
names `worktrees.ledger_projection.LEDGER_RELATIVE_PATH` — `series_closeout.py`, the closeout legs
and the tests — keeps working unchanged, and no second declaration may appear here. Every refusal
is a `LedgerProjectionRefusal` carrying a named remedy: `_REPAIR_REMEDY` for a malformed observed
table (re-run `worktree_closeout_apply`, which recomputes it) and `_SOURCE_REMEDY` for a missing
or unreadable source. Refusal codes are the validator's vocabulary (`code-commit-missing`,
`memory-commit-unreachable`), so the projection and `validate_ledger` speak one language. Since
260913-LCA-L11 `LedgerSource` also carries the read's own accounting — `excluded_rows` (the rows the
source's table records that the exact source commit cannot prove) and `trailered_commits` (how many
commits on the line carry the attribution) — so a read's omissions are data rather than an absence.

### Invariants And Boundaries

- **The projection is derived, not authoritative.** Closeout computes `memory.md` from its source
  plus this branch's own true rows; a malformed or partially merged table needs no hand edit.
- **The source is the contract's memory source commit, resolved once.** The projection and the
  integration-side check measure one world; a source that resolves but has no ledger is empty,
  never an error.
- **The source ledger is the union of the source's own recorded table and its attributed history,
  not the blob alone.** `read_ledger_source` reads the table the source commit carried in every
  case and merges the reachable commits' `Code-Commit:` trailers into it, keeping the table's order.
  A row whose memory commit the exact source commit does not carry is **excluded at the read** with
  a recorded reason and an operator-visible count, never dropped in silence — a row that vanishes
  without a word is the "looks like no attribution exists" failure. There is no fallback *mode*: the
  blob is the record a pre-trailer commit left, read whether or not the history carries trailers.
- **The tracked ledger commit is not retired here.** `memory.md` is still written, committed and
  proved by the closeout family and the ledger leg still exists across closeout, direct landing,
  queue recovery, series closeout, integration and sync. This module changed where the *source* is
  read from, nothing else.
- **Row truth is proved against the repository, not the table.** A claimed code commit must exist
  and its memory content must be reachable from the state the ledger is written for.
- **A series reads its ledger from its memory work-branch tip.** There is no series memory
  worktree, so the observed table and the reachable state are both the exact tip; this module
  must not require a memory worktree for a series contract — that leaf-only assumption raised on
  every external-memory series closeout.
- **Two acceptance questions stay separate.** `is_fixed_point` is still live: `series_closeout`'s
  reconciled-pair recording and the read-only `inspect_ledger_projection` both read it.
  `is_interleaved_projection` is the weaker checkpoint-route question — a union merge's row
  placement tolerated, a changed row set or a different current mapping not — but since
  260913-LCA-L11 the landing no longer evaluates the projection at all, so **no production caller
  reads `is_interleaved_projection`**; only `mcp/tests/test_checkpoint_landing_end_to_end.py` does.
  It is retained rather than deleted as an unreferenced producer, and a future reader should not
  infer a live gate from its presence. (The developer's ruling removed the file-preservation rule
  and the series prefix producer, not this predicate.)
- **`inspect_ledger_projection` reports, it does not gate.** It converts a refusal into a
  `not-recomputed` state with the reason, so a recovery payload always says something about the
  ledger.

### Todos

None.

## Docs References

No configured domain-documentation or cross-repository source applies to this file; every claim
here is about this repository's own ledger projection and is proved by the retained source.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The projection's deterministic form: source tail in source order, own true rows ahead of it newest-first, header naming the first row. | `project_ledger`; `read_ledger_source`; `resolve_memory_source_commit` | mcp/src/agents_remember/worktrees/ledger_projection.py:579-641; mcp/src/agents_remember/worktrees/ledger_projection.py:302-350; mcp/src/agents_remember/worktrees/ledger_projection.py:274-299 |
| The source read is the union of the source's own recorded table and its trailered commits, with the unprovable rows excluded and counted rather than dropped. | `read_ledger_source`; `_tail_rows`; `_rows_the_source_records`; `_distinct`; `_source_ledger_with_rows` | mcp/src/agents_remember/worktrees/ledger_projection.py:302-350; mcp/src/agents_remember/worktrees/ledger_projection.py:353-383; mcp/src/agents_remember/worktrees/ledger_projection.py:393-420; mcp/src/agents_remember/worktrees/ledger_projection.py:386-390; mcp/src/agents_remember/worktrees/ledger_projection.py:423-441 |
| The attribution reader itself: the full-ancestry traverse, the one-row-per-trailer map, and the code-commit truth test. | `attributed_commits`; `ledger_rows_from_attribution`; `MemoryAttributionError` | mcp/src/agents_remember/kernel/memory_attribution.py:148-179; mcp/src/agents_remember/kernel/memory_attribution.py:213-232; mcp/src/agents_remember/kernel/memory_attribution.py:100-101 |
| The projection result and its three separate acceptance questions, only one of which still has a production caller. | `LedgerProjection`; `is_fixed_point`; `is_interleaved_projection`; `needs_write` | mcp/src/agents_remember/worktrees/ledger_projection.py:146-271; mcp/src/agents_remember/worktrees/ledger_projection.py:169-179; mcp/src/agents_remember/worktrees/ledger_projection.py:180-212; mcp/src/agents_remember/worktrees/ledger_projection.py:223-231 |
| Which bytes are observed and which memory state the rows must be true against, for a leaf and for a series. | `observed_ledger_state` | mcp/src/agents_remember/worktrees/ledger_projection.py:547-576 |
| The one live-contract projection: world facts in, difference out, with the unvalidated observed parse. | `contract_ledger_projection`; `read_ledger_text`; `code_commit_exists` | mcp/src/agents_remember/worktrees/ledger_projection.py:514-544; mcp/src/agents_remember/worktrees/ledger_projection.py:467-480; mcp/src/agents_remember/worktrees/ledger_projection.py:483-486 |
| The single `cat-file -e` object test this module's `code_commit_exists` now delegates to. | `code_commit_exists` | mcp/src/agents_remember/kernel/memory_attribution.py:207-210 |
| Read-only divergence evidence for the re-run and recovery paths, which reports instead of raising. | `inspect_ledger_projection` | mcp/src/agents_remember/worktrees/ledger_projection.py:489-511 |
| Row-level truth and the bounded operator report, now including the read's own exclusions. | `_own_row_candidates`; `_untrue_reason`; `_newest_first`; `operator_payload`; `_bounded_removal_reasons` | mcp/src/agents_remember/worktrees/ledger_projection.py:644-661; mcp/src/agents_remember/worktrees/ledger_projection.py:681-686; mcp/src/agents_remember/worktrees/ledger_projection.py:689-707; mcp/src/agents_remember/worktrees/ledger_projection.py:233-258; mcp/src/agents_remember/worktrees/ledger_projection.py:774-781 |
| The leaf ledger-commit leg passes this closeout's own new row as an addition and writes only when the bytes must change. | "repair = contract_ledger_projection(contract, additions)" | mcp/src/agents_remember/worktrees/modules/closeout_external.py:202-243 |
| The series route's surviving projection gate: only the **reconciled-pair recording** of the final closeout still requires `is_fixed_point`, and it refuses a dropped, reordered or replaced source row there. This is a different route from the landing check 260913-LCA-L11 removed, and it is deliberately untouched. | `_require_series_ledger_projection` | mcp/src/agents_remember/worktrees/series_closeout.py:841-858 |
| No production caller reads `is_interleaved_projection` any more: the landing stopped evaluating the projection at 260913-LCA-L11, so only the checkpoint end-to-end suite reads it. | `is_interleaved_projection` | mcp/src/agents_remember/worktrees/ledger_projection.py:180-212; mcp/tests/test_checkpoint_landing_end_to_end.py:533-534 |
| The closeout payload reports the ledger's divergence through the read-only inspection. | `inspect_ledger_projection` | mcp/src/agents_remember/worktrees/modules/closeout.py:613-616 |

## Cross-Repo References

The external-memory repository this module reads is another repository governed by the same
closeout contract. The code and memory repositories are both addressed through the worktree
contract; no sibling repository or external system is reached by any other route.

| Finding | Anchor | Source |
| --- | --- | --- |
| The memory repository and ledger path are the contract's, never an ambient checkout. | `contract_ledger_projection`; `observed_ledger_state` | mcp/src/agents_remember/worktrees/ledger_projection.py:514-544; mcp/src/agents_remember/worktrees/ledger_projection.py:547-576 |

## Update History

- 2026-09-14T17:20+02:00 — 260913-LCA-L3 (uncommitted change set on `ar/260913-lca-l3-ar`, base
  `7317108b`): this module stopped declaring the ledger's path. `LEDGER_RELATIVE_PATH` now arrives
  from `kernel/memory_ledger.py` on the existing import block and is re-exported by that import
  alone, because the path is a property of the ledger format rather than of the projection; the
  kernel's own reader of the tracked table (`kernel/memory_backfill.ledger_rows_at`) takes it as its
  default without importing `worktrees`. `Purpose` and `Conventions` were corrected from "the single
  declaration of the ledger's path" to the re-export shape, and the invariant that no second
  declaration may appear was recorded on the kernel ledger card. Every citation in this card was
  re-derived against the grown module (the change adds three lines at the import block, so every
  later range moved): `project_ledger` 576-640 → 579-641, `LedgerProjection` 143-270 → 146-271,
  `is_fixed_point` 166-176 → 169-179, `is_interleaved_projection` 177-219 → 180-212, `needs_write`
  220-229 → 223-231, `operator_payload` 230-256 → 233-258, `read_ledger_source` 299-349 → 302-350,
  `_tail_rows` 350-382 → 353-383, `_distinct` 383-389 → 386-390, `_rows_the_source_records`
  390-419 → 393-420, `_source_ledger_with_rows` 420-440 → 423-441, `read_ledger_text` 464-479 →
  467-480, `code_commit_exists` 480-485 → 483-486, `inspect_ledger_projection` 486-510 → 489-511,
  `contract_ledger_projection` 511-543 → 514-544, `observed_ledger_state` 544-575 → 547-576,
  `resolve_memory_source_commit` 271-298 → 274-299, `_own_row_candidates` 641-660 → 644-661,
  `_untrue_reason` 678-685 → 681-686, `_newest_first` 686-706 → 689-707, `_bounded_removal_reasons`
  771-778 → 774-781, and `_require_series_ledger_projection` 841-857 → 841-858. Verification metadata
  remains closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-09-14T11:58+02:00 — 260913-LCA-L11 curator (uncommitted change set on `ar/260913-lca-l11-ar`,
  base `4214d7a1`): corrected the reader's account. `read_ledger_source` no longer has a *fallback*:
  the source's own recorded table is read on every path (`_rows_the_source_records`, unvalidated
  because a disagreeing header is one of the shapes the projection repairs) and the reachable
  commits' `Code-Commit:` trailers are merged into it in the table's order (`_tail_rows`,
  `_distinct`), keeping only rows the exact source commit carries and returning the rest as
  `LedgerRowRemoval`s with reason `memory-commit-unreachable`. Recorded the reader's **second,
  independent defect** — the earlier form returned the trailers ALONE as soon as the history
  carried one, so a partially backfilled line read as a nearly empty source — with the worker's
  measurement, this curator's independent re-verification of it, and the direction of the fix.
  Recorded the new accounting fields (`LedgerSource.excluded_rows`/`trailered_commits` and the
  `sourceRowsExcluded`/`sourceExcludedRows`/`sourceExcludedReasons`/`sourceTraileredCommits` operator
  payload), the removed `_source_ledger_from_blob`, and that `is_interleaved_projection` now has
  **no production caller** because the landing stopped evaluating the projection. Repointed every
  citation in this card to its current range (the module grew from 625 to 778 lines and the kernel
  attribution module's own ranges had drifted since the L2 pass), corrected the series row that
  still described the deleted reconciled-prefix census, and kept `_require_series_ledger_projection`
  recorded as a **surviving** gate on the closeout route that this leaf deliberately did not touch.
  Verification metadata remains closeout-owned; no acceptance claim and no verification stamp
  advanced.

- 2026-09-13T23:07+02:00 — 260913-LCA-L2 curator (uncommitted change set on `ar/260913-lca-l2-ar`):
  corrected the claim that the source ledger is read from the tracked `memory.md` blob.
  `read_ledger_source` now projects the complete source ledger from the memory commits' own
  `Code-Commit:` trailers via `kernel/memory_attribution.py`, and reads **that commit's own** blob
  only when the whole walk attributes nothing (the pre-trailer history), a reading rule scoped to
  the commit being read rather than a caller-selected mode. Recorded the new helpers
  (`_source_ledger_with_rows`, `_source_ledger_from_blob`), the delegation of `code_commit_exists`
  to the attribution module's single `cat-file -e` definition, the measured real-repository state
  (0 of 958 reachable memory commits carry the trailer at tip `5e4899ea`, so the 476 rows the
  projection returns there come through the fallback), and the boundary the changed claim moved:
  the tracked ledger commit is **not** retired by this change. Repointed every citation in this
  card to its current range in the grown module. Verification metadata remains closeout-owned; no
  acceptance claim and no verification stamp advanced.

- 2026-09-13T17:35+02:00 — 260831-LOCR-L36 curator: created the one-to-one sidecar for this
  module. Documents the deterministic projection and its developer-ruling origin, the three
  separate acceptance questions (`is_fixed_point`, `is_interleaved_projection`, `needs_write`),
  the bounded operator report, and the new `observed_ledger_state` boundary: a leaf is observed
  from its memory worktree file and HEAD, while a series — which owns no memory worktree — is
  observed from the blob at its exact memory work-branch tip, with that same tip as the state its
  rows are proved reachable from. Records that the previous leaf-only
  `assert contract.memory_worktree is not None` is gone from `contract_ledger_projection`, and
  that `inspect_ledger_projection` reports rather than raises. Verification metadata mirrors the
  sibling cards' leaf base commit and remains closeout-owned; no acceptance claim.
