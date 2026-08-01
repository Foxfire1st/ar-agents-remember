# mcp/tests/conftest.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/conftest.py`                    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T16:20+02:00                     |
| lastVerifiedCommitHash | `a714114ef94eedb8042fb4caa38d9469f4767dd6` |
| lastVerifiedCommitDate | 2026-08-01T18:06:36+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

`conftest.py` provides session-wide pytest bootstrap that pins imports to the candidate checkout,
scrubs ambient Git repository selection before fixtures run, and supplies fallback commit identity
for throwaway repositories. Since 260731-EFA-L5 it also carries the tree's one autouse fixture,
`restore_declared_process_role` (L57-L85), which restores the durable store's process-role
declaration around every test.

## Code Commentary

### Logic

At collection time the bootstrap removes previously imported `agents_remember` modules and places
the current worktree's `mcp/src` first on `sys.path`. It imports
`GIT_REPOSITORY_SELECTOR_ENV` from production `kernel.git_command` and removes every selector from
the process environment before a fixture can spawn Git. It then uses `setdefault` for test-only
author/committer identity so an explicit caller identity remains authoritative.

**`restore_declared_process_role` (L57-L85) — the autouse fixture, and the leak it closes.**
`durable_store._declared` is a process-global dict with no reset, because in a real process it is
written once at the entry point and never again. The test suite is the one interpreter that hosts
both roles and reaches those entry points directly: `cli/dashboard.py::run` declares `"dashboard"`
before anything else it does, and `test_serving.py` calls `run()` — seven times, four of them in
`CliRunTests` and three in `CliSimTests` — so from the first of those calls onward every later test
in the same interpreter claimed to be the dashboard.

The value is not cosmetic. It is what `StoreOwnership.is_compaction_owner` and
`check_declared_writer` answer from, so a leaked role silently flips whether a process counts as a
log's compaction owner and whether a write to a dashboard-only store is refused. The fixture
snapshots `_declared`, yields, then clears and re-applies the snapshot.

**It RESTORES rather than clears, and the distinction is load-bearing.** A test that legitimately
declares its own role must still observe that declaration for the rest of its body, and an
enclosing fixture that declared one must get it back; only the escape into the *next* test is
closed. Being autouse is what makes it reach `unittest.TestCase` tests, which is the great majority
of this suite and the reason it cannot be a per-file helper.

**Adding this fixture turned the branch-coverage gate red at 345/347, and what the two uncovered
branches turned out to be is the most important thing this leaf learned about its own evidence.**
The uncovered branch was `mcp/tools/gates.py::_reclaim_gate_log`'s
`if not GATE_OWNERSHIP.is_compaction_owner(): return` (L485-L486) — the guard for this leaf's own
reclaim-ownership mechanism, the single thing that keeps gate compaction, having just been moved
off the dashboard's projection tick, from simply running in the dashboard again. **It had no
test.** Its skip arm had only ever been reached because the leaked `"dashboard"` role happened to
arrive from a suite that sorts earlier alphabetically. In other words: **a 100% branch-coverage
floor was being satisfied by cross-test state leakage rather than by a test**, and the leaf's R1
evidence was an artefact of filename order. Closing the leak is what exposed it. Both gaps are now
covered by real tests — `test_durable_store_contract.py::ProcessRoleIsolationTests` (L795-L832) for
the fixture itself and `GateReclaimOwnershipTests` (L835-L898) for the guard.

### Conventions

The production selector tuple is the sole inventory. Tests must import it rather than maintaining a
parallel list that could omit a newly supported selector.

**Process-role hygiene is a session-wide concern and lives here, not in the files that need it.**
Any suite may declare a role (`test_durable_store_contract.py`, `test_provider_store_durability.py`
and `test_controlplane_store_durability.py` all do), and the entry points that declare one as a
side effect are ordinary production code being exercised (`cli/dashboard.py::run`, and `_dev_app`
for the `--reload` worker). No single test file can own the cleanup, so the one autouse fixture in
this tree does.

**`ProcessRoleIsolationTests` is a mutually-checking pair on purpose.** Each of its two tests
asserts the process is undeclared *before* declaring a role of its own, so whichever runs second
fails when the fixture leaks — in either order, and both orders are exercised explicitly. A
one-directional "declare here, assert clean there" pair would prove the fixture only for the order
it was written in, which is the same class of defect as a test that cannot fail.

### Invariants And Boundaries

- Selector cleanup runs at module import before fixture construction or test collection can execute
  repository commands.
- Fixture Git calls use explicit temporary `cwd`; ambient selectors may not redirect them into a
  real repository.
- Checkout-source pinning ensures verification exercises the candidate, not a sibling editable
  installation.
- Fallback identity applies only to temporary fixture commits and never overwrites an exported
  identity.
- The role fixture restores, never clears. Changing it to clear on setup would break every test
  that declares a role and then expects its own declaration to hold for the rest of its body.
- It reaches into `durable_store._declared` directly — a private module global — because that is
  the only handle on the whole declaration, and `declare_process_role` has no inverse by design.
  A rename there breaks this fixture at import, which is the loud failure mode rather than the
  quiet one.
- Coverage of ownership-guard branches must not be re-derived from ambient role state. Any future
  guard on `is_compaction_owner` or `check_declared_writer` needs its own test that declares both
  roles and asserts the contrast; with this fixture in place, nothing else will reach the skip arm.

### Todos

**The fixture's docstring attributes all seven `run()` calls to `test_serving.py::CliRunTests`.**
Four of them are there; the other three are in `CliSimTests`. The claim the docstring is making —
that the leak originates in `test_serving.py` reaching `cli/dashboard.py::run` — is correct, and
the count is right for the file; only the class attribution is too narrow. Reported, not repaired:
this card does not modify the code worktree.

## Docs References

No Domain Documentation source is configured for this repository; the bootstrap mirrors production
Git isolation directly.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Production owns the eight-selector inventory and the scrubbed Git environment built from it. | `GIT_REPOSITORY_SELECTOR_ENV` L24-L33; `git_environment` L58-L64 | [git_command.py](agents-remember/mcp/src/agents_remember/kernel/git_command.py) |
| Route-index tests independently contaminate each selector and require identical output. | L592-L640 | [test_route_index.py](agents-remember/mcp/tests/test_route_index.py) |
| Worktree fixtures create and commit temporary code/memory repositories. | fixture setup | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| The process-global declaration this fixture snapshots and restores, the writer that has no inverse, the accessor the isolation tests assert through, and the two predicates a leaked role silently flips. | `_declared`; `declare_process_role`; `declared_process_role`; `StoreOwnership.is_compaction_owner`; `StoreOwnership.check_declared_writer` | [controlplane/durable_store.py](agents-remember/mcp/src/agents_remember/controlplane/durable_store.py) |
| The production entry points that declare the role, and which the suite reaches directly: the CLI `run` path and the `--reload` worker's app factory (a spawn child re-imports and never runs `run`). | `run` L161-L167; `_dev_app` L52-L72 | [cli/dashboard.py](agents-remember/mcp/src/agents_remember/cli/dashboard.py) |
| The suite that calls `run()` and so was the source of the leak in practice. | `CliRunTests` L1599-L1693 | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |
| The ownership guard that had no test, and whose skip arm was reached only because a role leaked from an alphabetically earlier suite. | `_reclaim_gate_log` L455-L488 | [mcp/tools/gates.py](agents-remember/mcp/src/agents_remember/mcp/tools/gates.py) |
| The two suites that now cover both gaps with real tests: the fixture's own mutually-checking isolation pair, and the guard driven under both declared roles on one log. | `ProcessRoleIsolationTests` L795-L832; `GateReclaimOwnershipTests` L835-L898 | [test_durable_store_contract.py](agents-remember/mcp/tests/test_durable_store_contract.py) |

## Cross-Repo References

No sibling repository defines the pytest bootstrap contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-01T16:20+02:00 — 260731-EFA-L5 curator: recorded the tree's one autouse fixture,
  `restore_declared_process_role` (L57-L85), which restores `durable_store._declared` around every
  test. The leak it closes is a real one with a named origin: `cli/dashboard.py::run` declares the
  process role into a module-level dict that has no reset (correct for a real process, written once
  at its entry point), and `test_serving.py` calls `run()` — seven times, four in `CliRunTests` and
  three in `CliSimTests` — so the role escaped into every later test in the same interpreter. It
  RESTORES rather than clears, so a test that legitimately declares its own role still observes it
  for the rest of its body and an enclosing fixture gets its declaration back; only the escape into
  the next test is closed. Autouse is what makes it reach `unittest.TestCase` tests, which is most
  of this suite. **The finding worth carrying forward is not the hygiene.** Adding the fixture
  turned the branch-coverage gate **red at 345/347**, and the uncovered branch was
  `mcp/tools/gates.py::_reclaim_gate_log`'s `if not GATE_OWNERSHIP.is_compaction_owner(): return`
  (L485-L486) — the guard for this leaf's own reclaim-ownership mechanism, the only thing keeping
  gate compaction from running in the dashboard again after being moved off its projection tick.
  **It had no test.** Its skip arm had been reached solely because the leaked `"dashboard"` role
  arrived from a suite that sorts earlier alphabetically. **A 100% branch-coverage floor was being
  satisfied by cross-test state leakage rather than by a test**, and this leaf's R1 evidence was an
  artefact of filename order until closing the leak exposed it. Both gaps are now covered:
  `test_durable_store_contract.py::ProcessRoleIsolationTests` (L795-L832), a deliberately
  mutually-checking pair run in both orders so neither direction can be the only one proven, and
  `GateReclaimOwnershipTests` (L835-L898), which drives the same call under both declared roles on
  one log so the contrast is the assertion. Also repaired the `git_command.py` citation, which
  claimed the "scrubbed Git environment" over a range (L9-L42) that stopped before
  `git_environment` ever appeared; it is now cited by symbol as
  `GIT_REPOSITORY_SELECTOR_ENV` L24-L33 and `git_environment` L58-L64, both ends read back. Rows
  into `controlplane/durable_store.py` are cited **by symbol name with no line range**: that module
  grew ~100 lines mid-leaf and every earlier range into it was invalidated. **Filed one Todo:** the
  fixture's docstring attributes all seven `run()` calls to `CliRunTests`; four are there and three
  are in `CliSimTests`. Reported, not repaired. Verification metadata untouched.
- 2026-07-31T21:45+02:00 — 260731-EFA-L2 curator: re-derived the `test_route_index.py` citation
  after the leaf's whole-tree `ruff format` moved it (L595-L644 → L592-L640), verified by reading
  both ends back. The leaf also deleted a stray `# Reopen drill marker (L13): …` comment left in
  this conftest by earlier drill scaffolding; it was referenced nowhere and carried no behaviour,
  so no claim in this sidecar changes. Every other citation here was re-checked and is correct.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: replaced the duplicated Git selector list with the
  production `GIT_REPOSITORY_SELECTOR_ENV` inventory and corrected the nearest governing overview.
- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: added the worktree-local source/import pin so pytest
  cannot silently exercise a sibling editable install. Verification remains pinned until closeout.
- 2026-07-03T02:58+02:00 — No content impact: L13 reopen drill second cycle extended the marker
  comment; the reopened leaf ran under its original id with a fresh lifecycle.
- 2026-07-03T02:40+02:00 — No content impact: L13 reopen drill appended a marker comment; the drill
  exercised task-reopen mechanics, not fixture behavior.
- 2026-05-30T23:59+02:00 — Created after inherited `GIT_DIR` redirected temporary fixture commands;
  the import-time guard strips repository selectors and supplies fallback identity.
