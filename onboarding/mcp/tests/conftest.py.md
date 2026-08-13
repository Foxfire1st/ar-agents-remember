# mcp/tests/conftest.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/conftest.py`                    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-12T08:41+02:00 |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

`conftest.py` provides session-wide pytest bootstrap that pins imports to the candidate checkout,
declares the explicit hermetic `test` execution mode,
scrubs ambient Git repository selection before fixtures run, and supplies fallback commit identity
for throwaway repositories. Its autouse cit:([`reject_owned_global_state_leaks`], mcp/tests/conftest.py:118-129) fixture snapshots the explicit owned-global register,
restores every registered value after each test, and fails the leaking test with the complete list of
changed globals.

The session-autouse `_isolate_xdist_worker_cache` fixture gives every xdist worker its own
`XDG_CACHE_HOME` below that worker's pytest base temp directory and restores the inherited value on
teardown. The non-xdist `master` process keeps its existing environment. This isolates application
caches that are process-global by design without changing production cache resolution.

## Code Commentary

### Logic

The xdist autouse fixture uses `mock.patch.dict` around each worker's private `XDG_CACHE_HOME`, so
the environment is restored by the context manager without a duplicated manual save/restore
branch. The fixture remains active under serial invocation as well as xdist workers.

At collection time the bootstrap removes previously imported `agents_remember` modules and places
the current worktree's `mcp/src` first on `sys.path`. Immediately after that pin, it calls
`declare_test_process()` before importing application services. This is the explicit bypass for
temporary fixture configs and stores: tests do not masquerade as MCP/dashboard daemons, and
production does not infer test mode from `pytest`, argv, or an environment flag. It imports
`GIT_REPOSITORY_SELECTOR_ENV` from production `kernel.git_command` and removes every selector from
the process environment before a fixture can spawn Git. It then uses `setdefault` for test-only
author/committer identity so an explicit caller identity remains authoritative.

**cit:([`reject_owned_global_state_leaks`; `OWNED_MUTABLE_STATES`; "from _global_state import restore_owned_mutable_state"], mcp/tests/_global_state.py:33-39; mcp/tests/conftest.py:81-81; mcp/tests/conftest.py:118-129) — the autouse guard and its explicit ownership register.**
The register is deliberately not a repository scan: a row is added only after a mutable module
global has been proved capable of carrying state between tests. The current row owns
`kernel.primitives.checkout_coordination._declared`, whose session baseline is `mode=test`. Before
each test the fixture snapshots all registered state; afterward it
restores every value, collects every changed owner, and then fails the test that leaked it. Restore
happens before failure so one defect cannot contaminate later tests.

`preserve_owned_mutable_state()` is the scoped escape hatch for a test that intentionally calls a
production entry point whose contract mutates registered process state. It snapshots and restores
the same register around that bounded call. It suppresses cross-test leakage, not the global-state
gate: a test that leaves a registered value changed without that explicit scope still fails.

### Conventions

The production selector tuple is the sole inventory. Tests must import it rather than maintaining a
parallel list that could omit a newly supported selector.

Owned-global hygiene is suite-wide and lives in the autouse guard, while the enumeration and scoped
preservation helper live in `_global_state.py`. Do not add a broad reflective scan: ownership is an
explicit, reviewable contract, and diagnostics must name the exact global that changed.

### Invariants And Boundaries

- Selector cleanup runs at module import before fixture construction or test collection can execute
  repository commands.
- Fixture Git calls use explicit temporary `cwd`; ambient selectors may not redirect them into a
  real repository.
- Checkout-source pinning ensures verification exercises the candidate, not a sibling editable
  installation.
- Explicit test-mode declaration occurs after checkout pinning and before application imports, so
  linked-worktree tests retain their existing temporary-root contracts without gaining production
  authority.
- Fallback identity applies only to temporary fixture commits and never overwrites an exported
  identity.
- The guard restores every registered value before it reports a leak, keeping failure attribution
  on the offending test without poisoning later tests.
- `OWNED_MUTABLE_STATES` is an ownership register, not a claim that every mutable global has been
  discovered. Add a row only with evidence of cross-test persistence and an exact restore operation.
- Intentional entry-point mutation must use `preserve_owned_mutable_state()` around the smallest
  scope that owns it; the autouse guard remains the backstop.
- Coverage of ownership-guard branches must not be re-derived from ambient role state. Any future
  guard on `is_compaction_owner` or `check_declared_writer` needs its own test that declares both
  roles and asserts the contrast; with this fixture in place, nothing else will reach the skip arm.

### Todos

No task-independent follow-up is recorded for the current guard.

## Docs References

No Domain Documentation source is configured for this repository; the bootstrap mirrors production
Git isolation directly.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Production owns the eight-selector inventory and the scrubbed Git environment built from it. | `GIT_REPOSITORY_SELECTOR_ENV`; `git_environment` | mcp/src/agents_remember/kernel/git_command.py:34-43; mcp/src/agents_remember/kernel/git_command.py:85-91 |
| Route-index tests independently contaminate each selector and require identical output. | "test_ambient_git_repository_selectors_cannot_redirect_the_census"; "test_regular_checkout_and_linked_worktree_produce_identical_indexes" | mcp/tests/test_route_index.py:592-620; mcp/tests/test_route_index.py:822-850 |
| Worktree fixture tests. |"test_closeout_blocks_missing_onboarding_for_changed_source"; "test_closeout_plan_uses_memory_worktree_settings"|mcp/tests/test_worktree_support_tests_1.py:1036-1036; mcp/tests/test_worktree_support_tests_2.py:122-122|
| The explicit ownership register, snapshot/restore operations, and scoped preservation helper used by the autouse guard. | `OWNED_MUTABLE_STATES`; `snapshot_owned_mutable_state`; `restore_owned_mutable_state`; `preserve_owned_mutable_state` | mcp/tests/_global_state.py:33-39; mcp/tests/_global_state.py:42-43; mcp/tests/_global_state.py:46-54; mcp/tests/_global_state.py:57-64 |
| Every xdist worker receives a private XDG cache below its pytest base temp directory; the master process is unchanged. | `_isolate_xdist_worker_cache` | mcp/tests/conftest.py:47-64 |
| The current autouse guard restores all registered state and fails the leaking test with the complete changed-owner list. | `reject_owned_global_state_leaks` | mcp/tests/conftest.py:118-129 |
| The currently registered process-global execution declaration, explicit test entry, and accessor. | "_declared: dict[str, ExecutionMode] = {}"; "def declare_test_process() -> None:"; `return _declared.get("mode")` | mcp/src/agents_remember/kernel/primitives/checkout_coordination.py:27-66 |

## Cross-Repo References

No sibling repository defines the pytest bootstrap contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T08:41+02:00 — 260731-EFA-L20 replaced manual `XDG_CACHE_HOME` save/restore branches with `mock.patch.dict`; isolation semantics remain the same while unreachable test-only coverage branches are gone.
- 2026-08-12T00:08+02:00 — Recorded worker-private XDG cache isolation for pytest-xdist and
  re-resolved citations shifted by the new session fixture. Verification metadata remains pinned
  until closeout.

- 2026-08-10T19:57:55+02:00 — Closeout citation review: retained the execution-declaration claim
  after re-reading the candidate and replaced the reopened broad identifiers with exact unique
  declaration/signature anchors. Verification metadata remains pinned until closeout.

- 2026-08-10T18:31+02:00 — 260731-EFA-L21: pytest now declares explicit hermetic test mode after
  pinning candidate source; owned-global documentation follows the kernel execution declaration.
  Verification metadata remains pinned until approved closeout.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T11:39:21+02:00 — 260731-EFA-L6 S18-B09 curator: reconciled the frozen-source ledger and repaired scoped citations; unsupported source claims were narrowed or removed, and the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: superseded the removed single-purpose
  `restore_declared_process_role` fixture with the current explicit owned-global register,
  restore-before-fail autouse guard, and scoped `preserve_owned_mutable_state` escape hatch. New
  ranges are explicit provisional curator input.

- 2026-08-03T11:05+02:00 — 260731-EFA-L6 W3-B07 curator: repaired 13 live findings (2 missing anchors, 2 malformed sources, 7 prose citations, and 2 live-only duplicate sources); 3 Tier-3 citations naming the removed `restore_declared_process_role` fixture remain unresolved.

- 2026-08-01T16:20+02:00 — 260731-EFA-L5 curator: the older single-purpose fixture narrative is superseded by
  the current explicit owned-global register and restore-before-fail autouse guard. The current rows
  bind the surviving register and guard symbols; the removed `restore_declared_process_role` fixture is
  not cited.
<!-- S18-B09 removed the superseded historical paragraph that attributed current behavior to the deleted fixture. -->
- 2026-07-31T21:45+02:00 — 260731-EFA-L2 curator: re-derived the `test_route_index.py` citation
  after the leaf's whole-tree `ruff format` moved it, verified by reading both ends back. The leaf
  also deleted a stray `# Reopen drill marker` comment left in
  this conftest by earlier drill scaffolding; it was referenced nowhere and carried no behaviour,
  so no claim in this sidecar changes. Every other citation here was re-checked and is correct.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: replaced the duplicated Git selector list with the
  production `GIT_REPOSITORY_SELECTOR_ENV` inventory and corrected the nearest governing overview.
- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: added the worktree-local source/import pin so pytest
  cannot silently exercise a sibling editable install. Verification remains pinned until closeout.
- 2026-07-03T02:58+02:00 — No content impact: the reopen drill's second cycle extended the marker
  comment; the reopened leaf ran under its original id with a fresh lifecycle.
- 2026-07-03T02:40+02:00 — No content impact: the reopen drill appended a marker comment; the drill
  exercised task-reopen mechanics, not fixture behavior.
- 2026-05-30T23:59+02:00 — Created after inherited `GIT_DIR` redirected temporary fixture commands;
  the import-time guard strips repository selectors and supplies fallback identity.
