# mcp/tests/test_atomic_series_chain_pair_order.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_atomic_series_chain_pair_order.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T17:09+02:00 |
| lastVerifiedCommitHash | `756c47b37fa16324a836a44336655413d10fffaa` |
| lastVerifiedCommitDate | 2026-09-20T03:26:53+02:00|
| reviewedWorkingCandidate | candidate `ar/260915-ks-l35-ar`, uncommitted; base `7abacd8e432730cfca177ff0136711f13ea5f34d` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Contract-scoped forcing tests for the atomic-series landing validator
`worktrees/series_closeout.py`. The property they pin is the **ordering predicate over the landing
pair**: a leaf whose code leg is `not-applicable` lands a memory commit and records the code position
it stood on, so two leaves can share one code commit and still be two distinct landings, "each memory
commit makes the pair unique." The chain therefore orders on the pair — code ancestry where the code
position moved, memory ancestry where it did not — "and refuses only a pair that is equal on both
sides, which really is one landing recorded twice."

The module docstring records the live regression it closes: "Before this case existed the ordering
predicate returned 'unordered' in *both* directions as soon as two leaves shared a code commit, so no
total order could be built and the master closeout refused `atomic-series-leaf-chain-invalid`: a
complete atomic master containing a memory-only leaf could not be landed by any governed route." It
also states that the fix arrived with a second, surviving refusal (register row `D-45`), pinned by the
second class here: "the spine's admissible positions were read from the series contract alone, so a
base advanced by a *leaf-level* sync was invisible and a step to it was refused even though the leaf's
own contract records that position as synced." The addition was paid for inside the module — the
identical-pair case now asserts both fixture pairs — "so the module's case count is unchanged by the
addition."

## Code Commentary

### Logic

**The fixtures build real Git state instead of fabricating commit ids.** `_git` shells out with
`check=True`; `_init_repo` creates a repository on a named branch with a fixed committer identity;
`_commit` writes a file, stages everything and returns `rev-parse HEAD`; and `_branch` uses
`git branch -f` with the docstring "point a ref the checked-out branch does not own, so the series tip
can be placed exactly." `_Side` is the frozen record of one side of a leaf's pair — "the base it
started from and the commit it landed" — so a case can build a contract whose recorded base and
landed commit differ per side. Both classes are `unittest.TestCase` with a `TemporaryDirectory` in
`setUp` and `cleanup()` in `tearDown`; nothing outside the temporary root is touched.

**The first class forces the pair-order property over the production predicate.** 
`AtomicSeriesChainPairOrderTests` — "one code commit, two memory commits: two landings, ordered by
memory ancestry" — builds its contracts through `_contract`, which fills a `WorktreeContract` with
the shared `code_source_branch` `line`, distinct work branches per leaf, and
`integrated_code_commit`/`integrated_memory_content_commit` taken from the caller's pair. Its four
cases are: `test_a_shared_code_commit_with_ordered_memory_is_a_chain_step` (two leaves on one code
commit and two memory commits — the predicate is true one way and false the other);
`test_code_ancestry_still_orders_when_the_code_position_moved` (the code-only rule still orders when
the code position advances, "still" being the point); `test_an_identical_pair_is_still_one_landing_recorded_twice`
(equality on both sides stays unordered in both directions, "nothing is relaxed here", and the case
loops over both the second and the first memory commit because "the property is over the pair, not
over either commit's value"); and `test_disabled_memory_keeps_the_code_only_rule` ("with memory
disabled there is no pair to order, so a shared code commit stays unordered"). Every assertion is on
the shipped `_leaf_landing_precedes` imported from `agents_remember.worktrees.series_closeout`.

**The second class forces the admissible-position rule that survived the pair fix.** 
`AtomicSeriesLeafSyncPositionTests` — "a leaf-level sync position is admissible; a position no
contract recorded is not" — explains why one case carries both directions: "a sync is journaled on the
contract it ran for. When a leaf's own base was advanced ... the entry is on the *leaf's* contract,
and the series contract holds only its own syncs. Reading the series contract alone therefore refused
a step to a base the leaf's own contract records as synced, and named a commit that is that leaf's
recorded base *and* its landing." Its `_series` helper builds the canonical series contract (its own
contract path, `kind="series"`, `code_work_branch`/`memory_work_branch` `series`), and `_leaf` builds
a landed leaf whose `code_source_branch`/`memory_source_branch` are the series work branches, with
`integration_status="completed"`, both integrated commits set, and an optional `sync_log` tuple of
`{"codeBaseTo": ..., "memoryBaseTo": ...}` entries. The single case
`test_a_leaf_level_sync_position_is_admitted_and_a_silent_one_is_refused` first orders two leaf
contracts — one plain landing and one whose own sync log records the base it moved to — places the
series branch tips with `_branch`, and asserts
`[leaf.leaf_id for leaf in _require_exact_atomic_landing_chain(series, {...})] == ["L1", "L2"]`; it
then adds a third leaf whose code position no contract's sync log ever recorded, moves the series
tips to it, and asserts the call raises `CloseoutQueueError` with
`status == "atomic-series-leaf-chain-invalid"` and the foreign commit named in the message.

**The production module under test is `mcp/src/agents_remember/worktrees/series_closeout.py`.** The
test imports exactly two private functions from it — `_leaf_landing_precedes` and
`_require_exact_atomic_landing_chain` — plus `CloseoutQueueError`, `leaf_enclosure_path`,
`WorktreeContract` and `MemoryMode`. The predicate it pins is the one the chain walk uses:
`_ordered_atomic_landing_chain` repeatedly asks, for each remaining leaf, whether
`_leaf_landing_precedes(series, leaf, other)` holds against every other remainder, and refuses
`atomic-series-leaf-chain-invalid` unless exactly one leaf is the minimum ("atomic series leaves do not
form one exact code-and-memory landing chain"). The predicate itself checks
`same_code`/`same_memory` first and returns `False` when the pair is equal on both sides (or when
memory is not external), then requires code ancestry when the code position moved, and — only for an
external memory mode — either an equal memory commit or memory ancestry. The second case's refusal
comes from the spine check: `_require_landing_spine_side` proves each landing is an ancestor of the
series ref and then `_require_admitted_step` runs `git rev-list --no-merges --full-history <later>
--not <earlier> <positions...>`; any commit it reports is "history beyond the exact leaf landing chain
and the reconciled source line." The `positions` argument is produced by `_landing_source_positions`,
whose docstring is the fix this test forces: "A sync is journaled on the contract it ran for, and
that is not always the series contract ... Reading the series contract alone therefore hid a
leaf-level sync from this check and refused a step to a base the leaf's own contract records as
synced, so both are read here." The union stays bounded — "every contract named here is one of the
ordered leaves this closeout already proved landed, so a position no contract ever synced with stays
inadmissible" — which is precisely the third leaf the second case adds.

**The same case now pins a third direction: the reconciled line a step merged with is that step's own
history.** After the ordering and silent-position directions, the case builds a step whose *endpoint* is
a `--no-ff` merge of the previous landing with a recorded position, places the series branches on it, and
asserts `_require_exact_atomic_landing_chain` still orders `["L1", "L2"]` — with the step's own non-merge
count asserted as `rev-list --no-merges --count` = `"4"`, so the direction cannot pass vacuously on an
empty step. This is the 260915-KS master's real history at its L5 → L6 step: the recorded base
`8dfc11b8` *is* the merge of the previous landing `7db50f8f` with the synced super-line position
`8dd62345`, every commit the step adds is reachable from `8dd62345`, and the pre-repair validator admitted
the position while refusing the whole line it introduced (register row `D-60`) — the master's own closeout
refused `atomic-series-leaf-chain-invalid` naming 22 commits. The third direction is a **statement inside
the existing case body**, not a new `test_*` method, because both lanes sit at exactly their configured
budget — unit **2300 / 2300** and integration **400 / 400** — where one added collected case makes
`pytest_collection_finish` raise `UsageError` and that lane executes **zero** tests. The counter-case is
untouched and still refuses: a recorded position that reaches *past* a step cannot vacate a foreign commit
inside it.

### Conventions

Cases assert observable outcomes of the production functions, not internal helpers: the first class
asserts the boolean predicate in both directions, and the second asserts the returned order and the
`CloseoutQueueError.status` plus the refusal message. Every contract is built by a local helper rather
than a shared factory, so each class states its own premise (`_contract` for the pair class, `_series`
plus `_leaf` for the position class). Git state is real but disposable: repositories live under a
`TemporaryDirectory`, commits are created with a fixed `chain@example.invalid` identity, and refs the
checked-out branch does not own are placed with `git branch -f`. Cases are named as the property they
pin rather than as the function they call (`..._is_a_chain_step`, `..._is_still_one_landing_recorded_twice`,
`..._keeps_the_code_only_rule`), and the docstrings carry the reasoning the assertions cannot. The file
carries no assertion about time, no network access, and no dependence on the repository's own Git
state.

### Invariants And Boundaries

- **The order is over the pair, never over the code commit alone.** A shared code commit with ordered
  memory ancestry is a chain step; equality on both sides is one landing recorded twice and stays
  unordered in both directions.
- **Memory-disabled enclosures keep the code-only rule.** With `memory_mode="disabled"` there is no
  pair to compare, so a shared code commit is unordered.
- **A leaf-level sync position is admissible only because the chain's own contracts recorded it.** The
  admissible set is the union of the series contract's and the ordered leaves' own `sync_log` entries
  plus the recorded base; a position no contract ever synced with is refused as history beyond the
  chain.
- **A recorded position inside a step admits that position's own line, and only that.** When a step's
  endpoint is the merge of the previous landing with a synced position, every commit the step adds is
  that position's history, so each commit such a position reaches is admitted. The admission is bounded
  to positions lying strictly inside the step: a position that merely descends from the step is outside
  it and admits nothing, which is what the counter-case still measures.
- **The refusal is typed and names the offender.** The failure is `CloseoutQueueError` with
  `atomic-series-leaf-chain-invalid`, and the message carries the foreign commit, so a caller reads
  which step failed rather than only that the chain is invalid.
- **The chain must have exactly one minimum.** `_ordered_atomic_landing_chain` refuses when the
  candidate set is not exactly one element, which is the failure mode the pair fix removed.
- **The tests own no production behavior.** They import two private production predicates and the
  contract type; they add no fixture hook, monkeypatch or alternate code path to the module under
  test.
- **Nothing is asserted about real task state.** The fixtures use synthetic task ids
  (`260915_TEST`), a temporary coordination root, and `leaf_enclosure_path` only to derive a path, so
  the suite never reads or writes a live enclosure.

### Todos

No task-independent follow-up is recorded in the source. The docstring's two register rows (`D52` for
the pair-order regression, `D-45` for the admissible-position refusal) are historical provenance
rather than open work: both behaviours are now pinned by the two classes here.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The rows below separate the test file's own fixtures and cases from the production predicates they
force, so a reader can see which half of each claim is asserted here and which half is asserted by the
module under test.

| Finding | Anchor | Source |
| --- | --- | --- |
| The property the module pins: the chain orders on the landing pair rather than the code commit alone, so two leaves on one code commit remain two landings. | "The atomic landing chain orders a memory-only leaf by the pair, not by the code commit alone." | mcp/tests/test_atomic_series_chain_pair_order.py:1-7 |
| The regression the case closes: both directions returned unordered once two leaves shared a code commit, so a complete atomic master containing a memory-only leaf could not be landed. | "two leaves shared a code commit"; "atomic-series-leaf-chain-invalid" | mcp/tests/test_atomic_series_chain_pair_order.py:9-11; mcp/tests/test_atomic_series_chain_pair_order.py:11-13 |
| The second, surviving refusal (register row D-45): a base advanced by a leaf-level sync was invisible to a spine that read the series contract alone. | "the spine's admissible positions were read from the series contract alone" | mcp/tests/test_atomic_series_chain_pair_order.py:15-20 |
| The production predicates under test and the import that names them. | "from agents_remember.worktrees.series_closeout import ("; `_leaf_landing_precedes` | mcp/tests/test_atomic_series_chain_pair_order.py:37-40; mcp/src/agents_remember/worktrees/series_closeout.py:284-317 |
| The Git fixture helpers: a checked-out repository on a named branch, a commit that returns its own id, and a ref placement the checked-out branch does not own. | `_commit`; `_branch`; `_Side` | mcp/tests/test_atomic_series_chain_pair_order.py:62-66; mcp/tests/test_atomic_series_chain_pair_order.py:69-72; mcp/tests/test_atomic_series_chain_pair_order.py:76-80 |
| The pair-order class and the contract builder that fixes each leaf's recorded pair independently of its work branch. | `AtomicSeriesChainPairOrderTests`; `_contract` | mcp/tests/test_atomic_series_chain_pair_order.py:83-99; mcp/tests/test_atomic_series_chain_pair_order.py:101-134 |
| The four pair-order cases: a shared code commit with ordered memory is a step, code ancestry still orders, an identical pair is one landing recorded twice in both fixture pairs, and disabled memory keeps the code-only rule. | `test_a_shared_code_commit_with_ordered_memory_is_a_chain_step`; `test_code_ancestry_still_orders_when_the_code_position_moved`; `test_an_identical_pair_is_still_one_landing_recorded_twice`; `test_disabled_memory_keeps_the_code_only_rule` | mcp/tests/test_atomic_series_chain_pair_order.py:136-144; mcp/tests/test_atomic_series_chain_pair_order.py:146-152; mcp/tests/test_atomic_series_chain_pair_order.py:154-168; mcp/tests/test_atomic_series_chain_pair_order.py:170-193 |
| The leaf-sync class and its two builders: the canonical series contract, and a landed leaf that may carry its own sync log. | `AtomicSeriesLeafSyncPositionTests`; `_series`; `_leaf` | mcp/tests/test_atomic_series_chain_pair_order.py:196-209; mcp/tests/test_atomic_series_chain_pair_order.py:231-254; mcp/tests/test_atomic_series_chain_pair_order.py:256-296 |
| The single case that pins all three directions: the recorded leaf-level sync position is admitted and ordered, a position no contract's sync recorded is refused with the foreign commit named, and a step whose endpoint merges the previous landing with a recorded position is admitted as that position's own line. | `test_a_leaf_level_sync_position_is_admitted_and_a_silent_one_is_refused` | mcp/tests/test_atomic_series_chain_pair_order.py:298-377 |
| The production chain walk the order comes out of: the chain is proved landed, then ordered by asking the pair predicate against every other remaining leaf and refusing unless exactly one minimum exists. | `_require_exact_atomic_landing_chain`; `_ordered_atomic_landing_chain` | mcp/src/agents_remember/worktrees/series_closeout.py:226-248; mcp/src/agents_remember/worktrees/series_closeout.py:251-281 |
| The spine proof behind the second refusal: each landing must be an ancestor of the ref, and each step may add only official positions the chain's own contracts synced with — or a line one of those positions, lying inside that step, reaches. | `_require_landing_spine_side`; `_require_admitted_step`; `_positions_inside_the_step`; `_reached_by_an_official_position`; `_landing_source_positions` | mcp/src/agents_remember/worktrees/series_closeout.py:405-446; mcp/src/agents_remember/worktrees/series_closeout.py:483-543; mcp/src/agents_remember/worktrees/series_closeout.py:546-566; mcp/src/agents_remember/worktrees/series_closeout.py:569-576; mcp/src/agents_remember/worktrees/series_closeout.py:579-602 |
| The origin rule the chain still enforces: with no sync the oldest leaf starts at the recorded base, and with a sync its base must lie on one line with the position the first sync advanced from. | `_require_chain_origin` | mcp/src/agents_remember/worktrees/series_closeout.py:320-351 |
| The contract fields the fixtures set: the mid-task sync log, the integration status, and the leaf identity the chain is keyed by. | `sync_log`; `integration_status`; `leaf_id` | mcp/src/agents_remember/worktrees/worktree_contract.py:280-280; mcp/src/agents_remember/worktrees/worktree_contract.py:263-263; mcp/src/agents_remember/worktrees/worktree_contract.py:269-269 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The suite drives real `git` against
temporary repositories it creates itself, and every contract it builds names one synthetic
coordination root; no sibling repository, remote, or external service participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-20T03:19+02:00 — 260915-KS-L35 curator (uncommitted change set on `ar/260915-ks-l35-ar`, code base `7abacd8e`): **the leaf-sync case gained a third direction, and it is the reason this leaf exists.** `test_a_leaf_level_sync_position_is_admitted_and_a_silent_one_is_refused` now also builds a step whose endpoint is a `--no-ff` merge of the previous landing with a recorded position and asserts the chain admits it, counting the step's own non-merge commits (`"4"`) so the direction cannot pass on an empty step. That is the 260915-KS master's real L5 → L6 history — recorded base `8dfc11b8` is the merge of the previous landing `7db50f8f` with the synced super-line position `8dd62345`, and the pre-repair `_require_admitted_step` admitted the position while refusing all 22 commits of the line it introduced (register row `D-60`). The direction is statements inside the existing case body, not a new collected case, because both lanes sit at exactly their budget — **2300 / 2300** unit and **400 / 400** integration — and one added collected case makes `pytest_collection_finish` raise `UsageError`, after which that lane executes zero tests; the Invariants section now states that budget arithmetic as this module's decision rule. The case's own reference row was re-pointed to its current extent (`:298-377`, it grew by the new direction) and the spine row now carries the two helpers the repair added, `_positions_inside_the_step` and `_reached_by_an_official_position`. The `_position_that_descends_from_a_step_does_not_vacate_it` counter-case and its helper are untouched and still refuse. No verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-19T17:09+02:00 — 260915-KS-L28 curator: created this one-to-one card for the atomic-series
  chain pair-order suite. It records the property the module pins (the landing order is over the pair,
  not the code commit alone), the two refusals it forces — the pair-order regression that made a
  complete atomic master containing a memory-only leaf unlandable (register row D52), and the
  leaf-level sync position the spine used to miss (register row D-45) — the Git-backed fixture
  helpers, all five cases in both classes, and the production predicates in
  `worktrees/series_closeout.py` they exercise (`_leaf_landing_precedes`,
  `_require_exact_atomic_landing_chain`, `_ordered_atomic_landing_chain`,
  `_require_landing_spine_side`, `_require_admitted_step`, `_landing_source_positions`). Verified
  against the committed source at `e79985045437d7e6409b873c7da3c51aa7cd9685`.
