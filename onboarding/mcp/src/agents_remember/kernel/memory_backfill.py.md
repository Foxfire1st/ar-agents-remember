# mcp/src/agents_remember/kernel/memory_backfill.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/memory_backfill.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T03:43 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[Nearest governing overview](../../../overview.md)

Committed-source review: inspected at 2026-09-15T03:43 UTC against `7cbda30d9a9a4c2944382fbef46ac58b85329935`.
Normal closeout owns final verification-metadata stamping for this committed source.

## Purpose

Plans and explicitly applies one-time memory-history attribution migration from a selected
historical ledger table. This migration reader is separate from runtime cache derivation.

## Code Commentary

### Logic

`MemoryBackfillRequest` names the memory repository, code repository, tip, historical table path,
rescue ref, and exact refs permitted to move. Planning resolves a branch-name tip to an exact commit
before reading its table, resolves abbreviated memory cells through Git, checks reachability and
code-object existence, and selects the trailers the history can carry.

Selection first seeks distinct code coverage through matching, then fills remaining eligible memory
commits with their own oldest claims. One effective trailer cannot represent two conflicting code
claims for the same memory commit, so skip reasons distinguish missing/unreachable data from
selection declines. Lost claims name the omitted code, contested memory commit, and winner.
`MemoryBackfillPlan` reports eligible rows, rewrites, named code commits, skips, and losses
separately; a plan with lost code claims is not empty, and its digest includes that distinction.

Apply optionally checks the preview digest and returns before rescue checks for an empty plan.
For work to perform, it validates rescue authority, writes and reads back rescue refs, rebuilds
commit objects with their trees, identities, timestamps, and remapped parents, then moves only the
named targets. The identity map includes unchanged commits, making reuse explicit.

`_walk` uses native `git rev-list --reverse --topo-order --all`. The topological ordering,
reversed for replay, visits every parent before its child even with tied or skewed commit dates.
`_rewrite_history` can therefore resolve remapped parent identities before rebuilding descendants;
date order alone is not the parent-ordering contract.

`_move_targets` resolves full ref names and emits one `update <ref> <new> <old>` command per changed
target to a single `update-ref --stdin` call. Commands are separated by one newline and the stream
ends with one newline; no blank command is inserted between targets. That fixes multi-ref apply
while preserving old-object checks and rescue reachability.

`ledger_rows_at` and `carry_ledger_cells` operate on explicit historical migration artifacts.
The carry resolves memory cells before remapping, retains code cells/code base, and updates memory
references and current headers. Carrying such a table is not required to make the runtime reader
find attribution: runtime reads now use the rewritten commit trailers alone.

### Conventions

Planning is a read-only description; applying it is a separate requested rewrite over named refs.
The kernel guarded Git runner carries the explicit input stream and commit identities. The migration
retains its historical-table `relative` input; runtime `read_ledger_source` no longer has one.

### Invariants And Boundaries

- Runtime cache absence never invokes this migration automatically.
- Missing mappings, declines, and losses remain observable rather than collapsed into a success count.
- Rescue refs precede target publication; only named refs may move.
- Multi-ref command framing contains no empty update command.
- Native reversed topological traversal resolves parent identities before rebuilding their children.
- This documentation pass makes no claim that shared history was rewritten or that a migration was approved to run.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Typed request and plan reporting distinguish work, losses, and an empty plan. | n/a | [mcp/src/agents_remember/kernel/memory_backfill.py](mcp/src/agents_remember/kernel/memory_backfill.py) |
| Selection preserves available memory attributions and reports unrepresentable claims. | `SKIP_MEMORY_COMMIT_CLAIMED` | mcp/src/agents_remember/kernel/memory_backfill.py:84-84 |
| Apply orders digest/rescue/rewrite/publication and frames every target update correctly. | n/a | [mcp/src/agents_remember/kernel/memory_backfill.py](mcp/src/agents_remember/kernel/memory_backfill.py) |
| Historical table reads/carry remain explicit migration helpers. | n/a | [mcp/src/agents_remember/kernel/memory_backfill.py](mcp/src/agents_remember/kernel/memory_backfill.py) |
| The apply regression now moves two named refs and verifies the rescue tip. | `test_the_rescue_ref_may_not_be_one_of_the_refs_the_run_moves` | mcp/tests/test_memory_backfill.py:624-634 |
| Native topological traversal visits parents before their children during replay. | n/a | [mcp/src/agents_remember/kernel/memory_backfill.py](mcp/src/agents_remember/kernel/memory_backfill.py) |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History

- 2026-09-15T06:48:46+02:00 — Preserved the following dated pre-takeover review notes from the parent working tree. They describe that earlier candidate; current behavior is documented above. Exact original files and patches are retained in the master cutover report.

- 2026-09-14T23:55+02:00 — 260913-LCA completed-master review follow-up (same uncommitted change set,
  `ar/260913_ledger-commit-attribution`, base `bb65a207`): **the multi-branch migration is fixed.**
  `_move_targets` appended an empty string after each update instruction and joined the list with
  newlines, so a run with two or more changed refs sent a blank line to `git update-ref --stdin`,
  which reads a blank line as an EMPTY COMMAND and aborts the whole transaction with
  `fatal: empty command in input`; the single-ref case survived only because the one trailing newline
  its last line needed doubled as the stream's terminator. The stream is now built by the new
  `_update_ref_stream` — one instruction per line plus exactly one terminating newline — so any number
  of refs moves atomically together, and the transaction is still fed by that one function rather
  than by a joined list. Recorded the fix and the review that found it, and stated plainly that the
  tool is fixed and host-verified with the review's own probes passing and the focused suites green,
  has still **not** been applied to any real repository, and has **no** Dagger certificate. Every
  citation in this card was re-derived against the grown module (1024 → 1037 lines): `_move_targets`
  837-879 → 837-880, `_full_ref_name` 882-898 → 895-911, `ledger_rows_at` 901-924 → 914-937,
  `carry_ledger_cells` 927-972 → 940-985, `_commit_fields` 992-1001 → 1005-1014, `_full_name`
  1004-1012 → 1017-1025, `_code_commit_is_held` 1023-1024 → 1036-1037, and the test-module anchors
  `MemoryBackfillApplyTests` 399-629 → 399-676 and `MemoryBackfillCliTests` 754-902 → 801-949.
  Verification metadata remains closeout-owned; no acceptance claim and no verification stamp
  advanced.

- 2026-09-15T03:43 UTC — Documented committed C2 native --topo-order parent-before-child replay and retained the actual multi-ref framing contract; reviewed the committed source rather than a pending working candidate. Verification hash/date stamping remains with normal closeout.


- 2026-09-15T01:02 UTC — Documented the multi-ref newline framing fix and retained named-ref/rescue/digest behavior; clarified that historical table reading/carry is explicit migration input, not a runtime fallback or condition for derived mappings. Working candidate verified by source inspection; commit metadata records real committed history only.


- 2026-09-14T18:20+02:00 — 260913-LCA-L3 curator (same uncommitted change set,
  `ar/260913-lca-l3-ar`, base `7317108b`): **an externally reviewed defect pair was fixed and this
  card now describes the fixed tool.** The selection is no longer "keep the last row per code commit,
  last assignment wins": `_select_pairings` computes a maximum matching (Kuhn, code commits offered
  most-constrained-first with the older claim winning a tie, read off the table rather than off object
  names) and then a **fill** giving every memory commit the matching did not reach its own oldest row
  — load-bearing, because a matching is symmetric and the format is not, so a matching alone left
  dozens of named memory commits unattributed. Measured at `7aa4cd97`: 418 of 428 code commits named
  (confirmed maximal with Hopcroft-Karp), 455 of 455 named memory commits trailered, 52 of the
  review's 60 omitted pairings recovered, 10 code commits reported through `lost_claims`. Recorded the
  structural bound (472 pairings, 455 single-trailer memory commits, at most 418 matchable code
  commits; 5 of the remaining 8 losses provably uncarryable and 3 the same tie resolved by the table's
  order) and that a 55-of-60 variant selecting by hash order was deliberately refused. The skip
  vocabulary is now five literals in two families — holes versus declines, the latter exported as
  `SKIP_REASONS_THE_RULE_CHOSE` — with `LostClaim(code_commit, memory_commit, winner)` naming each
  loss; `assigned_attributions` now means the eligible set before the rule; the old
  `attributions_one_commit_cannot_carry` property is gone; and `is_empty` includes `lost_code_commits`
  so a plan that lost a mapping can never report empty. The second finding: every name is resolved to
  an exact commit before any ref is written (`_resolve_commit`, `_full_ref_name`) and the empty-plan
  check now precedes the rescue-ref guard, so a retry is a no-op instead of a refusal about refs its
  own predecessor created. States plainly that the tool is fixed and proven on fixtures plus a
  read-only plan measurement and **has not been applied to any real repository**; the earlier
  pre-fix confined attempt stays recorded as the reason the rewrite is deferred to this master's
  integration into IAS. The superseded pre-fix figures (67/44 skips, four-literal vocabulary,
  0/7 already trailered) are kept in the measurement section as re-measurement history. Every citation
  in this card was re-derived against the grown module (686 → 1024 lines). Verification metadata
  remains closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-09-14T17:20+02:00 — 260913-LCA-L3 curator (uncommitted change set on `ar/260913-lca-l3-ar`,
  base `7317108b`): created the one-to-one sidecar for this new kernel module. Records the three
  contract properties and why each is forced (classified by the row rather than the subject; one
  trailer chosen by the oldest-row-per-code-commit rule because the reader takes the last and the
  table is newest-first; idempotence both at the plan and at the object id, the latter verified
  977/977), the closed four-literal skip vocabulary, the total old→new identity map and the
  `carry_ledger_cells` table carry that has to accompany it, the rescue-ref-before-first-object and
  one-`update-ref --stdin` ordering, and the `%ai`/`%ci`-not-`%aI` identity replay. Records the
  measured census at the shared line `7317108b` (474 rows, 419 distinct code commits, 0 trailered, 67
  skips — 44 row-is-not-the-oldest and 23 memory-commit-not-reachable — and 13 exclusions, of which
  11 are reachable-at-the-tip orphans and 2 name no object at all) and at this master's tip
  `7aa4cd97` (472 rows, 428 distinct code commits, 7 trailered, 44 skips, 0 exclusions), and marks
  the scoping document's earlier 104/513/10 census as not reproducible. States the reversal plainly:
  the confined apply was verified and then reverted by developer ruling because rewriting the shared
  ancestors removed the master's common ancestor with its super and the lineage gate refused
  downstream, so the shared line still carries 0 trailers and the backfill is an explicit step at
  this master's integration into IAS. Verification metadata names the leaf's base commit and remains
  closeout-owned; no acceptance claim and no verification stamp advanced.
