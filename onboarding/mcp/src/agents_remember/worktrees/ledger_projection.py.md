# mcp/src/agents_remember/worktrees/ledger_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/ledger_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Nearest governing overview](overview.md)

Working-candidate verification: source inspected at 2026-09-15T00:51 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Derives the consumer memory ledger from committed `Code-Commit` attribution and reports
informational differences from a disposable cache. It does not decide, create, or repair Git
transactions.

## Code Commentary

### Logic

`read_ledger_source(repository, commit, *, code_repository=None, repo_name=None)` calls
`derive_memory_ledger`. It never reads a `memory.md` blob or unions historical cached rows into the
result. When a code repository is supplied, missing code objects are excluded and reported;
`trailered_commits` counts attribution before that filtering. `_ledger_with_rows` recomputes both
the current header and oldest retained base pair. Empty attributed history remains an empty ledger.

`contract_ledger_projection` resolves the named source history and the actual selected memory tip.
A leaf uses its memory-worktree HEAD; a series uses the exact local memory work-branch tip.
`observed_ledger_state` reads the optional local cache only after resolving that Git state, and
`read_ledger_text` returns `None` for malformed cached text. Cache read failures are misses; an
unreadable repository, commit, or branch remains a distinct Git error.

`project_ledger` derives expected rows, order, base pair, and current header from the selected
memory Git history. Observed cache pairs cannot contribute mappings, even when both objects exist.
The removed `additions` input cannot inject a pair that no commit attributes. Source information is
reported relative to the selected history; it is not spliced into the expected rows as an
unconditional table tail.

`LedgerProjection` retains observed and computed rows/text, added/removed/reordered rows, headers,
source exclusions, and bounded operator diagnostics. Reasons distinguish missing code, unreachable
memory, absent attribution, and duplicate cached mappings. `cache_hit` and payload `cacheState`
distinguish a parseable observation from a miss; states are `cache-miss`, `diverged`, or
`already-correct`.

`is_fixed_point` and `is_interleaved_projection` are comparison data. `needs_write` compares cache
bytes with the canonical rendering; none of these properties grants Git authority.
`inspect_ledger_projection` reports unreadable history as `not-recomputed` with its reason.
Historical tables may still be explicit one-time migration input, but these runtime readers do not
use them as a substitute for committed attribution.

### Conventions

The frozen result family (`LedgerSource`, `LedgerWorld`, `LedgerRowRemoval`, `LedgerProjection`)
keeps omissions observable. Row payloads are capped at twenty with counts for elided detail.
The canonical ledger path constant remains owned by `kernel.memory_ledger`; this projection no
longer reexports it or accepts `read_ledger_source(relative=...)`.

### Invariants And Boundaries

- Only committed attribution determines expected mappings; source and branch code targets are checked when code authority is supplied.
- Cached headers, rows, order, and valid-looking pairs are observations, never input authority.
- Missing/malformed cache and absent attribution are valid data states, not Git refusals.
- Actual Git read failures remain explicit and cannot be repaired by editing cache bytes.
- The module reads and compares; it does not write onboarding, update refs, or create ledger commits.

### Todos

No new file-local follow-up is established by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

| Finding | Anchor | Source |
| --- | --- | --- |
| Source reads derive only Git attribution and recompute retained revision metadata. | `read_ledger_source`; `_ledger_with_rows` | mcp/src/agents_remember/worktrees/ledger_projection.py:222-249; mcp/src/agents_remember/worktrees/ledger_projection.py:252-264 |
| Contract projection resolves actual memory history independently of cache availability. | `contract_ledger_projection` | mcp/src/agents_remember/worktrees/ledger_projection.py:290-312 |
| Expected mappings and informational differences are built from the selected Git history. | "the selected Git history" | mcp/src/agents_remember/worktrees/ledger_projection.py:284-284 |
| The kernel walks committed attribution without reading a ledger file. | `derive_memory_ledger` | mcp/src/agents_remember/kernel/memory_cache.py:22-41 |
| Cache forgery/misses and invalid attributed targets have focused regression coverage. | `test_cache_misses_preserve_contract_and_named_ref_history` | mcp/tests/test_memory_ledger.py:338-360 |

## Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence is claimed. | — | — |

## Historical Context

The previous card recorded memory tip `f5edc613` as a 479-row cached table with one trailered commit,
and recorded 466 reachable rows plus 13 exclusions under the then-current union reader. It also
recorded the older `5e4899ea` observation as zero trailered commits among 958 reachable commits.
These are preserved observations from the earlier card, not measurements repeated in this pass or
claims about the working candidate. Their former table-union interpretation is superseded above.

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T06:48:46+02:00 — Preserved the following dated pre-takeover review notes from the parent working tree. They describe that earlier candidate; current behavior is documented above. Exact original files and patches are retained in the master cutover report.

- 2026-09-14T23:55+02:00 — 260913-LCA completed-master review follow-up (same uncommitted change set,
  `ar/260913_ledger-commit-attribution`, base `bb65a207`): **the projection now asks the code half of
  a row's truth of the SOURCE's own rows.** `read_ledger_source` decides the memory half and holds no
  code repository; `project_ledger` asks the code half through the new `_kept_true_source_rows`, which
  keeps a source row the code repository holds and excludes one it does not with reason
  `code-commit-missing`, reported through the existing `source_excluded_rows`/
  `source_excluded_reasons` channel and surfaced as `sourceRowsExcluded`/`sourceExcludedReasons`. The
  reviewed defect: `project_ledger` appended the source rows unchanged, so a source trailer naming a
  code commit the code repository does not hold survived the recompute with the correct code
  repository in `LedgerWorld` — the rebuild preserved the very row the landing refuses and re-derived
  it on every run, so the recompute could not repair the state it exists to repair. Recorded the
  deliberate behaviour change: `LedgerWorld.code_repository` widened to `Path | None = None`, so a
  world that names no code repository cannot answer the code question and keeps its rows unchanged
  (previously a `None` there died inside the `cat-file -e` object test with an `AttributeError`);
  `_untrue_reason` was narrowed to ask the code question only when a repository is named. Added the
  card row and the reference row for `_kept_true_source_rows` and the two new cases that pin it
  (`test_a_source_row_naming_a_code_commit_the_repository_lacks_is_excluded`,
  `test_a_source_with_no_code_repository_to_ask_keeps_its_rows`). Every citation in this card was
  re-derived against the grown module (781 → 840 lines): `_own_row_candidates` 644-661 → 694-711,
  `_untrue_reason` 681-686 → 731-745, `_newest_first` 689-707 → 748-766, `project_ledger` 579-641 →
  592-656, `LedgerProjection` 145-271 → 154-284, `is_fixed_point` 168-177 → 181-190,
  `is_interleaved_projection` 179-210 → 192-223, `needs_write` 222-231 → 235-244, `operator_payload`
  233-258 → 246-271, `observed_ledger_state` 547-576 → 560-589, `read_ledger_source` 302-350 →
  315-363, `_tail_rows` 353-383 → 366-396, `_distinct` 386-390 → 399-403, `_rows_the_source_records`
  393-420 → 406-433, `_source_ledger_with_rows` 423-441 → 436-454, `read_ledger_text` 467-480 →
  480-493, `code_commit_exists` 483-486 → 496-499, `inspect_ledger_projection` 489-511 → 502-524,
  `contract_ledger_projection` 514-544 → 527-557, `resolve_memory_source_commit` 274-299 → 287-312,
  `LedgerSource` 93-112 → 96-115, `LEDGER_RELATIVE_PATH`'s re-export block 44-63 → 47-66, and
  `_bounded_removal_reasons` 774-781 → 833-840. Verification metadata remains closeout-owned; no
  acceptance claim and no verification stamp advanced.

- 2026-09-15T00:51 UTC — Replaced source-table union, cached-pair admission, and additions with Git-only mappings; documented optional code-object filtering, cache misses, computed metadata, diagnostic states, and retired path arguments. Earlier table-union and ledger-commit descriptions are superseded. Working candidate verified by source inspection; real last-touch commit metadata retained, with no future commit hash or certification claim.


- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (provenance repair): the gate could not compare
  this claim with its verification provenance because one or more of its anchors resolved more than
  once at the verification commit, so no historical location was unique. Repaired the citation, not
  the claim: each anchor that named a construct by bare name now names its exact declaration text,
  which resolves once in the code tree, and any range that had drifted off its construct was re-read
  at the declaration. The claim wording is unchanged, and the construct each range covers is the one
  the claim is about. Verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 9 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). 1 claim(s) were declined as ambiguous or not the subject
  and were left for a reading curator. No claim wording changed; every rewritten range was read back
  at its current position. Verification metadata remains closeout-owned.
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
