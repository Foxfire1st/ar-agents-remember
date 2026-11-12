# mcp/tests/test_task_reopen_series_extension.py

## Governing Overview

[mcp/tests overview](overview.md)

Source-inspection boundary: this module already has committed history. The L9 working-candidate
account below is historical, not the identity or acceptance status of the present L46 candidate.
Current route claims describe source assertions only; verification metadata remains closeout-owned.

## Purpose

The durable proof that a **completed atomic master is a door, not a dead end**. The sibling
`mcp/tests/test_task_reopen.py` pins the reopen itself — a terminal series is reset under CAS, its
retired integration ref is re-cut, and its successor enclosure generation cites the archived one.
That is the entry. This module pins what the entry is *for*, because the reopen was added to this
plane precisely because a finished master had no route back to a new leaf and no route back to
integration once that leaf existed: reopen, author a new leaf with its owning-master row, start it,
work it, close it out, integrate it, finalize its row, close the master out again and land it —
nine steps, in order, once, on one real temporary world, through the same entry points the
registered tools call.

It is also the leaf's response to the developer's ratchet ruling (*"the ratchets are a cancer"*):
six refusals that forbade this route were removed, and each removal is bound here to a case that
fails if the refusal comes back — set against the guards that were kept and are named below, so
"refuse less" and "refuse harder" are both falsifiable.

## Code Commentary

### Current Contract

The integration lane contains test_task_reopen_series_extension.py at the current declaration location, line 615. Integration membership and the nine-step route are unchanged; a stale historical row number is not a semantic reopen change or an executed result.

### Logic

> **Retained historical source account — superseded by the current contract:**
> Three `unittest.TestCase` classes and three module-level readers, **18 cases**, no `pytest` marks.
> The lane placement is load-bearing and is `integration`, not unit-regression (`T98`): the world is a
> real Git repository with a real coordination root, so the module is registered in the `integration`
> array of `mcp/tests/test-evidence-lanes.toml` at current row 464. Registry placement is a
> source fact, not a collected or executed case result.

- **The route** (`SeriesExtensionRouteTests`). The single case
  `test_a_reopened_master_runs_a_new_leaf_through_closeout_and_lands_again` runs nine private steps
  in order, each of which asserts where it stands, and appends to `ROUTE_COMPLETIONS` only on the
  last line so a skipped or half-run route cannot report success. Every step goes through a
  registered entry point — `reopen_task`, the `task_doc` application function,
  `worktree_start_tool`, the closeout and integrate tools, `lifecycle_finalize_task_tool`.
  `_work_the_leaf` first calls the public conversion command and asserts return 0, then authors
  fixture Markdown and an open canonical history row for `onboarding:extension.txt` with
  `disposition: no_impact`, empty `items`, and a `sources` entry naming `extension.txt` with the
  actual blob from `CodeSnapshot.capture(self._leaf.code_worktree)` after its edit and before
  committing code. This is test scaffolding,
  not a new execution or semantic acceptance receipt. Two of the steps exist
  because the open question they answer had never been measured: `_start_the_leaf_off_the_reopened_master`
  carries the new row's `file` cell through the real start, and `_close_the_master_out_again_and_land_it`
  re-runs closeout and integration on a master that was already `Completed` once.
- **The guards** (`SeriesReopenGuardTests`), below.
- **The population check** (`RouteExecutionTests`). `test_z_the_route_case_actually_executed` asserts
  the route case reached its last line: `unittest` reports a *skipped* test as a success, so without
  this a `skipTest` injected into the route would turn the leaf's whole end-to-end claim green while
  executing nothing. The boundary is stated in `ROUTE_COMPLETIONS`' own docstring rather than
  implied: a deliberate skip decorator and a deleted append both red this case, while skipping the
  route case *and* this one leaves nothing red, because the population check is itself an ordinary
  case. The residual is a hole in the counting, not in the guard (`T99`, `S7`).
- **The module-level readers** are deliberately three small functions rather than copied numbers:
  `_declared_case_rails` reads the two case ceilings out of the repository-root `pyproject.toml`
  (where they are the single declaration, since `mcp/tests/conftest.py` states no `default=`), and
  `_declared_screen_boundaries` reads the budget screen's own pair out of the interface the screen
  runs with; `_coordination_files` builds the write surface a refusal is a claim about.

### The six removals, each bound to the case that fails if it returns

1. **The leaf-only kind gate** — reopening refused every contract whose `kind` was not a leaf
   enclosure, before any other check. The whole module is the case: every case here reopens a
   contract whose `kind` is `series`, so restoring the gate reds the module wholesale rather than one
   case, and the route case names the consequence.
2. **The unreachable-landing refusal, replaced by reconstruction** —
   `test_a_retired_branch_whose_landing_left_the_source_line_is_reconstructed` rewrites the source
   line so the series' recorded landing is no longer an ancestor of the tip, and requires the reopen
   to rebuild the retired branch **at the recorded landing** (not at the rewritten tip), report
   `action: "reconstructed"`, echo the recorded landing, and leave the master at `cleanup: pending`.
   The refusal it replaces stranded a master whose only fault was that its source line moved; the
   ordinary `worktree_sync` projection is the remedy for the branch being behind its source.
3. **The `R3` document precondition, demoted to a report fact** —
   `test_a_missing_master_document_does_not_block_the_reopen` deletes `task.json` and requires the
   reopen to succeed, to name the missing path in `documentNote`, and to leave the branch in place.
   What the precondition actually gated was the reopen's own status demotion, and the reopen's object
   — the contract, the refs, the successor generation — is exactly what a seat needs in hand to
   repair the document afterwards. The other side is kept: a task root holding a **non-master**
   document is still refused.
4. **The archived-generation file-existence gap** — the archived-contract guard used to answer "no
   existing contract" at its first line whenever the contract *path* was absent, so a hand-deleted
   `series-contract.md` beside a `terminal-archived` locator reached the fresh-bootstrap path, which
   created the integration branch and wrote the bootstrap journal before the plane refused the
   publication, untyped. `test_a_hand_deleted_contract_beside_an_archived_generation_is_refused`
   authors the leaf first (the refusal is only reachable once the leaf document resolves), deletes
   the contract, and then requires the **typed** `atomic-series-contract-reopen-required` refusal with
   `nextTool: task_reopen`; that no replacement contract was minted; that **no integration branch
   exists**; and — through `_coordination_files` — that the whole coordination root is the same file
   set afterwards, which detects newly created journal and lock files the old path left
   behind. This is the case whose absence was `T123`; its acceptance test is the mutation that
   removes the plane query, not a green run.
5. **The `source-lineage-unavailable` symptom** —
   `test_a_cleaned_up_master_reads_as_unprovable_until_it_is_reopened` asserts the operator-visible
   projection itself: `worktree_status` reports `unavailable` before the reopen and `current` after
   it. Cleanup retires the master's work branch, so the lineage edges could not be proven and every
   task-bound seat failed closed on a terminal master; what restores the proof is the ref the reopen
   re-establishes.
6. **`operation-location-terminal-archived`** — the archived generation is collected, and only a
   *successor* publication may re-address the lane. The route's last step re-runs closeout and
   integration on the reopened master, which is the exercise; the sibling's successor/predecessor
   assertions pin the publication's shape, and the archived-contract case above pins the refusal that
   names the route back to it.

### The guards kept, and named

| Guard | Case |
| --- | --- |
| A **live** series is never reset under a running seat (the terminal-cleanup precondition) | `test_a_live_series_is_still_refused_so_a_running_seat_is_never_reset_under` |
| An existing ref is **never moved** — the direction that keeps reconstruction from being a licence | `test_an_existing_branch_at_an_unrelated_tip_is_refused_not_moved` |
| …and the same proof must not refuse a sound reopen, or "refuse harder" would pass | `test_a_reachable_landing_on_an_existing_branch_still_reopens` |
| A contract recording **no landing at all** refuses rather than re-cutting from nothing | `test_a_contract_that_records_no_landing_at_all_refuses` |
| A landing the contract **no longer records** refuses the re-cut | `test_a_landing_the_contract_no_longer_records_refuses_the_re_cut` |
| A task root holding a **non-master** document is a different task and is refused | `test_a_task_root_holding_a_leaf_document_is_still_refused` |
| The reachability proof runs **per side** — the memory line is a separate landing | `test_the_memory_side_is_proven_too_and_not_only_the_code_side` |
| The documented **fallback** from the closeout cell to the integration cell, both sides | `test_the_integration_cell_is_the_documented_code_landing_fallback` and `test_the_integration_cell_is_the_documented_memory_landing_fallback` |

**Two coverage boundaries are stated as boundaries, not as coverage.** The **source-branch existence**
check is a pre-existing guard whose bytes this leaf did not change, and no case in this module pins
it: removing it leaves the suite green (`K2`, `S7`). And the reachability proof's scope is the two
arms above; a branch hand-re-established at a **rewritten** tip that happens to equal the source tip
is adopted as `present` without consulting the proof, which is the case the unrelated-tip refusal is
paired with to keep the pair honest.

### `S2`: the reader, original L7 landing orders, and the current budget boundary

`_declared_screen_boundaries` reads the pair the budget screen actually runs with
(`test_selected_case_budgets` hands the hook its own rails) by walking the `parametrize` marks
pytest resolved on the screen's own members. Literal ints, module constants and computed
expressions therefore resolve alike. The original L7 account contrasts a 2300/400 declaration
with a 1000/250 screen before that raise, and a matching 3000/600 pair after it; reading the
interface rather than literal-only source syntax addressed the named-constant reader defect.
That dated account is not a general guarantee for every later raise or landing order.

With the current ruled constants 10,000/2,000, the agreement method compares the declaration tuple
lexicographically with that ruled tuple. At or above it, the screen must equal the declaration.
Below it, the screen must equal the fixed 1000/250 legacy pair and differ from the declaration.
A synchronized 4000/1000 or 3000/600 pair thus enters the legacy branch and fails; the method does
not accept every intermediate matched pair. The separate ruling method unconditionally requires exactly 10,000/2,000 and fails a below-ruling declaration; the obsolete pending-owner skip is removed. It does not qualify the agreement method. These are current assertion boundaries, not
proof of arbitrary mixed-state publication or a whole-suite compatibility claim. [17] [18] [19]

### Conventions

- The world is disposable, real and bound: `_World` builds one terminal atomic series from the shared
  task-reopen fixtures, binds every entry point to that world's own runtime configuration, and is
  driven inside `tempfile.TemporaryDirectory()`. Guard cases take the standalone shape because their
  refusals are decided before any integration surface is computed; the route takes the sprint shape,
  which is what makes the master landable at all.
- A refusal is asserted as a **refusal plus its consequence**: the typed `state`, the named
  `nextTool`, the blocker text, then the bytes that must not have moved. `_unchanged` compares the
  contract and master document; `_coordination_files` widens that to the whole coordination root
  whenever the claim is about bytes the old path wrote *outside* those two files.
- Rewritten-line worlds are built with real `git` plumbing and the assertions are made on refs and
  ancestry rather than on messages; the helper documents why `checkout -B` (not `branch -f`) is the
  form that moves the worktree with the ref, because a hand repair would have run the former.
- Every step of the route is one method so a break names its own phase, and the failing assertion is
  reported where it failed rather than at the end of one long case.

### Invariants And Boundaries

- This is a test module and a durable acceptance check, not a production reopen or admission API. It
  composes the product's own entry points; it re-implements none of them.
- The route is the claim: a case that does not run is not a case that passed, and the population
  check is what makes that true for this module. Deleting the check, or skipping it together with the
  route, is outside what any in-repo case can prevent and is recorded as such rather than presented
  as proof.
- The two budget figures inside the module — the ruled 10,000/2,000 constants and the pre-raise 1000/250
  pair — are **this module's declared inputs and the ruling's values**, never a second copy of the
  repository's ceilings: the ceilings themselves are read from `pyproject.toml` at run time. Do not
  restate either pair here; read them there.
- A case added here must protect a distinct operation or a distinct refusal. The guards above
  deliberately do not overlap: each names one failing state, and the two "direction" pairs exist so
  that neither removing a guard nor hardening one can pass unnoticed.

### Historical L9 follow-up account (not current blocker status)

Verification metadata remains closeout-owned; this card records source inspection of the working
candidate only. Two obligations this card does **not** discharge, recorded with their identity rather
than absorbed: (a) the three governing route overviews the product's census obliges for this leaf's
changed sources — `onboarding/mcp/src/agents_remember/worktrees/overview.md`,
`onboarding/mcp/src/agents_remember/worktrees/modules/overview.md`, `onboarding/mcp/tests/overview.md`
— carry unchanged bodies (`memory-refresh-attestation-failed`); (b) `mcp/tests/evidence-lifecycle.toml`
has no consumer row naming this module for the four `consumer_scope = "exact"` artifacts it imports,
so the consumer-completeness oracle reports it missing from `mcp/tests/task_reopen_test_support.py`,
`mcp/tests/lifecycle_enclosure_test_support.py`, `mcp/tests/curator_coherence_test_support.py` and
`mcp/tests/fixtures/repository_profiles/node/package-lock.json`.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, and no external specification
governs these assertions; the leaf's own contract and the developer's ratchet ruling are the
authority, and both are repository-local records rather than published standards.

No external domain claim is required.

### Repo-Internal References


Each row names one construct and cites the exact span that construct occupies in the reviewed
candidate, so the row is falsifiable by the source alone.


### Cross-Repo References

Every repository this module touches is a temporary fixture created inside the case; no real
adjacent repository, external service or network boundary is involved.

No cross-repository claim is made.

### Current Source-Inspection References













- The nine-step route — reopen, author the new row with its `file` cell, start, work, close out, integrate, finalize, close the master out, land it — runs in order and records completion on its last line. [1]



- The documented fallback from the closeout cell to the integration cell carries the code landing. [10]


- The same fallback carries the memory landing. [11]


- A missing master document no longer blocks: the reopen proceeds and reports the missing path. [12]


- The other side of that demotion is kept: a task root whose document is not a master is refused. [13]


- With both landing cells empty on both sides there is nothing to reconstruct or re-cut from, and the reopen refuses. [14]


- An existing ref at a tip that is neither the source tip nor the recorded landing is refused, not moved — the arm the reconstruction must not swallow. [15]


- The reachable direction: a work branch on the source tip whose line still holds the landing is adopted, so "refuse harder" cannot pass. [16]


- The current agreement method asserts screen equals declaration at or above the ruled tuple; below it asserts the fixed 1000/250 screen and inequality. Its original L7 landing-order account is historical, not generic later-raise compatibility.  Anchor: `SeriesExtensionRouteTests.test_the_budget_screen_and_the_declaration_agree_in_either_landing_order` [17]




- The current ruling screen unconditionally requires exactly 10000 unit and 2000 integration selected cases; it no longer skips a below-ruling declaration. [18]




- The screen's proved pair is read from the `parametrize` marks the screen runs with, so literals and named constants resolve alike. [19]


- A retired branch whose landing left the source line is rebuilt **at the recorded landing**, reports `reconstructed`, and leaves the master reopenable. [2]


- The case ceilings are read from the repository-root declaration rather than copied, so this check cannot rot into a third copy of the number. [20]


- A skipped route cannot report success: the sentinel and its boundary, stated rather than implied. [21]


- The population assertion no skip can satisfy, sorting last by construction. [22]


- The guard cases' invariant that a refused reopen writes nothing to the contract or the master document. [23]


- The disposable world every case is built on, and the two hand-repair shapes the reachability proof has to survive. [24]


- The developer's symptom is pinned with its remedy: the operator-visible source lineage reads `unavailable` before the reopen and `current` after it. [3]


- A contract that no longer records its landing refuses the re-cut, writes nothing, and creates no branch. [4]


- A start over an archived terminal contract refuses with the typed status and `nextTool: task_reopen`, mints nothing, and the named route then really works. [5]


- The archived-generation start asserts the typed refusal, no replacement contract or integration branch, and equality of the coordination-root file-name set. [6]


- The refusal snapshot compares relative file-path sets under the coordination root, excluding Git internals; it does not compare existing file bytes. [7]


- A live series is still refused, so the reopen never resets a series out from under a running seat. [8]


- The reachability proof runs on the memory side too, and the two sides' actions are asserted independently so a one-sided mutation cannot satisfy it. [9]







- The integration lane in `mcp/tests/test-evidence-lanes.toml` lists `mcp/tests/test_task_reopen_series_extension.py`, and its nine-step route case still runs the whole route in order. [26]




- The ruled constants and current declaration are 10000 unit and 2000 integration; the independent agreement method retains its fixed 1000/250 lower-rail fixture branch. [25]
