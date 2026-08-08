# mcp/src/agents_remember/worktrees/modules/guidance.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/guidance.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00     |
| lastVerifiedCommitHash | `1b7f6f07c5ccc64627299b5d22463ef9c267e187` |
| lastVerifiedCommitDate | 2026-08-08T02:42:36+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Builds lifecycle status payloads and typed next-operation guidance for worktree
tools. Since 260731-EFA-L4 it is also **where the phase and next-move vocabularies are
declared** — `models.worktree` imports them from here rather than keeping a second copy.

## Code Commentary

### 260731-EFA-L4: this module owns the guidance vocabulary

Five `Literal` aliases and four `TypedDict`s now sit above the state machine that produces them.

| Alias | Members |
| --- | --- |
| `WorktreePhase` | `worktree-started`, `closeout-pending`, `integration-pending`, `integration-blocked`, `carryover-pending`, `cleanup-pending`, `cleanup-completed`, `abandoned` |
| `NextOperation` | `continue_work`, `closeout`, `request_integration_decision`, `developer_decision`, `request_carryover_decision`, `request_cleanup_decision`, `done` |
| `NextTool` | `worktree_status`, `worktree_closeout_apply`, `worktree_integrate`, `memory_carryover_apply`, `worktree_cleanup` |
| `RecoveryOperation` | `request_commit_approval`, `choose_memory_recovery`, `choose_provider_setup_recovery`, `choose_stale_base_recovery`, `choose_memory_sync_recovery` |
| `RecoveryTool` | `worktree_start`, `worktree_sync`, `worktree_closeout_apply` |

**Why here.** This module is the state machine that emits every one of these values, and
`models.worktree.WorktreeSummary` imports `WorktreePhase` / `NextOperation` / `NextTool` for the
response boundary instead of restating them. The second hand-written copy is what drifted:
`carryover-pending`, `abandoned`, `request_carryover_decision` and `memory_carryover_apply` were all
emitted below and all rejected by the packet's model.

**Why `recovery_guidance` is a separate function.** `next_guidance(operation: NextOperation, *,
tool: NextTool | None = None, args=None, required_args=None) -> NextGuidance` is now narrowed to the
phase machine's vocabulary. The *other* users of the same next-move key shape — the closeout
preview's commit-approval gate and the four blocked-start / blocked-sync recovery payloads — get
`recovery_guidance(operation: RecoveryOperation, *, tool: RecoveryTool, args, required_args=None)
-> dict[str, object]` instead. It emits exactly the same keys in the same order, so **nothing on the
wire changed**; the split is in the type. Every one of those callers hands its result to a
`FlexibleToolResponse` and none reaches `WorktreeSummary`, whose only producer is
`lifecycle_guidance` via `application.worktree_status` — so widening `next_guidance` to fit them would have
silently widened `WorktreeSummary.nextOperation`, putting "requires developer approval" and "blocked
on a stale base" back into the set the context packet's `nextOperation` claims to be. `tool` and
`args` are *required* on `recovery_guidance` (they are optional on `next_guidance`) because a block
that cannot say how to recover is not worth emitting.

The four payload types:

- **`NextGuidance`** — `nextOperation` required; `nextTool` / `nextArgs` / `nextRequiredArgs`
  `NotRequired`. `nextTool` is deliberately *absent*, not blank, when the operation needs no call
  (`done`); the wire model declares it optional for exactly that reason and the packet projection
  reads it with `.get`.
- **`LifecycleGuidance`** — everything `lifecycle_guidance` returns: `phase`, `summary`, the
  next-move keys, plus `NotRequired` `carryoverDoneAt` (only the `cleanup-pending` phase carries it).
- **`WorktreeStatusFacts`** — the local, contract-derived half, snake_case because it is the
  tool-response shape. Carries `NotRequired` `unknown_contract_cells`, `providers`, `freshness`,
  `landing`.
- **`WorktreeStatusPayload(WorktreeStatusFacts, LifecycleGuidance)`** — a full `worktree_status`
  payload: the facts plus the guidance.

`lifecycle_guidance` is now typed `-> LifecycleGuidance`, and the three phase helpers return
`LifecycleGuidance | None` / `LifecycleGuidance` (not `dict | None` / `dict`).
`status_payload` and `projected_status_payload` return `WorktreeStatusPayload`.

**`unknown_contract_cells`.** `_status_payload_with_landing` adds
`facts["unknown_contract_cells"] = list(contract.unknown_cells)` when the contract carried a cell
outside its vocabulary that `worktree_contract._vocabulary_cell` substituted for. It is the one
place a degraded read becomes visible to whoever called a worktree tool, and it says so explicitly:
the phase reported beside it was computed from the substituted values. Absent is the normal shape,
so the key is an exception report, not a flag.

Finally, the payload is assembled as `return {**facts, **guidance}` rather than
`payload.update(guidance)`, so the checker sees one payload of a declared type. The guidance keys
still come last and the emitted key order is unchanged.

The module converts a `WorktreeContract` into stable MCP-facing lifecycle phases
keyed off its **lifecycle position** (disposal/integration/closeout/approval
fields) — integration pending, carryover pending, cleanup pending, done, and so
on — and renders contract dataclasses into JSON-compatible dictionaries.

**Slice 09 (visibility fix): `lifecycle_guidance` no longer infers a commit-approval
gate from `git status`.** The old code carried a dirty-tree branch (worktree dirty
→ phase `commit-approval-pending`) that fabricated a gate the working tree has no
authority to assert; it has been removed (with its unused `contract_has_worktree_changes`
import — `worktree_dirty` stays, and so does `run_git`, though since 260731-EFA-L3 it is
imported from `kernel.git_command` rather than `modules.git`). A dirty worktree now falls through to its
honest lifecycle-position phase (e.g. `closeout_status == "completed"` →
`integration-pending`). `commit-approval-pending` is owned by the closeout preview
(the real gate moment, set in `closeout.py`) and — once the slice-6 gate plane is
adopted — by a raised `closeout-approval` gate surfaced via `GateNode`; it is never
read off the tree. (`closeout-approval` IS the commit gate: closeout is the single
commit-of-record for code + memory + ledger, so there is no separate
`commit-approval`.)

**Three phase groups (260731-EFA-L2).** `lifecycle_guidance` is now a three-line `or` chain over
one helper per group, and **the order is the contract** — read back to front: a reclaimed worktree
is done, an integrated one is waiting on carryover/cleanup, and everything else is still working
toward closeout.

- `_reclaimed_phase(contract) -> LifecycleGuidance | None` — the terminal phases, where the
  worktrees are gone: `cleanup-completed` and `abandoned`.
- `_post_integration_phase(contract) -> LifecycleGuidance | None` — integration has been attempted:
  `integration-blocked`, or it landed and `carryover-pending` / `cleanup-pending` follow.
- `_pre_integration_phase(contract) -> LifecycleGuidance` — still working: `integration-pending`,
  closeout-approved, closeout-pending, `worktree-started`. This one always returns a phase, which
  is why it terminates the chain.

The first two return `None` to mean "not my group", so an earlier group always wins — the same
precedence the old top-to-bottom if-chain had. `lifecycle_guidance` checks the disposal states
**first**: `cleanup == "completed"`
returns the `cleanup-completed` phase, and (slice 05l P1) `cleanup == "abandoned"`
returns a dedicated `abandoned` phase (`"Worktree abandoned — provider stack reclaimed;
no further action."`, `nextOperation: "done"`). Before this branch an abandoned worktree
fell through to the `worktree-started` default, so the dashboard rendered a torn-down /
deleted worktree as fully active; the explicit phase lets the observer surface it (the
reducer's `_GUIDANCE_PHASE` maps it through) and the teardown render (05k).

`carryover_done(contract) -> (done, carryoverDoneAt)` (slice 05m) is the new public
honesty signal for "has the parked memory been carried into official memory?". The
existing `memory_carryover_apply` is contract-decoupled and leaves no contract stamp, so
the truthful source is the OFFICIAL ledger itself: a successful carry prepends a row to
the official `memory.md` (`contract.memory_repo_path / "memory.md"`) mapping the landed
code commit → the carried memory commit. `carryover_done` reads it with `load_ledger`
and looks up the landed commit (`integrated_code_commit`, else `code_commit`) via
`find_mapping`; the carried memory commit's `%cI` (`run_git ... show -s --format=%cI`) is
the returned milestone time. It is **external-only**: `internal`/`disabled` memory has
nothing to carry, so it returns `(True, "")` — the carryover route + cleanup guard are
no-ops there. A `LedgerError`, an absent ledger, or a missing row returns `(False, "")`.

Slice 05m also splits the `integration_status == "completed"` branch on `carryover_done`,
making carryover a distinct lifecycle phase **between integration and cleanup**:

- **not carried** → phase `carryover-pending` (`"Integration completed; carry the parked
  memory home before cleanup."`). The next operation routes the EXISTING
  `memory_carryover_apply` (its own plan→apply gate stays intact) with args derived from
  the contract — `repo_id`, `source_memory` (the memory worktree posix path),
  `official_code_ref` (`integrated_code_commit` or `code_commit`) — and
  `required_args=["intent_note"]`. Carryover must run while the worktree (its parked
  memory branch) still exists; cleanup later hard-guards on this same signal.
- **carried** → phase `cleanup-pending`, with the guidance dict now carrying
  `carryoverDoneAt` (the milestone time from `carryover_done`, surfaced onto
  `EngineProcessNode.carryoverDoneAt` for the dashboard; 5k renders the seam).

New imports back this: `LedgerError`/`find_mapping`/`load_ledger` from
`kernel.memory_ledger`, and `run_git` — since 260731-EFA-L3 from
`agents_remember.kernel.git_command`, the package's single git runner, not from
`modules.git` (which no longer defines one). The one call site is unchanged in shape —
`run_git(contract.memory_repo_path, ["show", "-s", "--format=%cI", row.memory_commit])` — but
it now runs with the `GIT_DIR`-family selectors stripped from the environment and under
`run_git`'s default local bound `GIT_LOCAL_TIMEOUT_SECONDS = 300` (it passes no `timeout=`).
`carryover_done`'s `try` covers only `load_ledger`/`find_mapping` (`except LedgerError`) and the
`run_git` call sits outside it, so a git call that outran the bound would raise
`subprocess.TimeoutExpired` out of `carryover_done` and its `_post_integration_phase` caller;
a `show -s` of a known commit is a constant-time read, so tripping 300s means git is blocked,
not busy.

`status_payload` includes a `providers` block from
`provider_async.provider_setup_status(contract)` when present: the
`worktree_status` poll surface for background provider setup — running with
currentPhase/heartbeat/seedFallback, stale on a dead heartbeat, terminal
ok / ready-with-failed-phases / failed with `retryArgs` (GitHub #53).

`status_payload` also includes a `freshness` block from `base_freshness`
(issue #54): a deliberately fetch-free comparison of the contract's recorded
base commits against the current LOCAL source branch tips
(`baseBehindSource` counts per side). Local source branches move mid-task when
a parallel cycle lands (PR merge ff's code main, carryover advances memory
main); when behind, the block carries a `syncHint` recommending
`worktree_sync` with a dry-run preview. No network in this path — it must stay
safe for the provider-setup polling loop; the fetching freshness checks live in
`context_packet` (`include_freshness`), the start preflight, and
`worktree_sync` itself.

`status_payload` also includes a `landing` block (slice 5h) from
`landing.landing_refs(contract)` once the worktree reaches the landing window
(closeout-completed onward): the successful-landing arc's remote/PR refs
(`origin/<feat>`, `origin/mem-main`, the PR), observed best-effort — `git ls-remote`
for branch tips and a best-effort `gh` for PR state, each timeout-bounded with
`stdin=DEVNULL` (the #49 stdio-pipe guard). Honest `factState` (`observed` when a
probe ran, else `planned`/`missing` — never faked); additive and absent before the
landing window, so the build-phase poll stays network-free like `freshness`.

`status_payload` also emits `lifecycle_id` (slice 2c) — the contract's
observable-lifecycle enclosure anchor, surfaced snake_case (like its sibling
keys) so `worktree_attach` can resume it; `""` for contracts written before 2c.

### 260712-TRH-L7 projected versus interactive landing

`status_payload` remains the interactive, fresh-observation surface. `projected_status_payload` accepts a pre-observed landing snapshot for recurring projection, so guidance preserves landing semantics without synchronously invoking remote commands.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Context packet worktree status consumes the facade-exported status payload. | `worktree_status_packet` | mcp/src/agents_remember/application/worktree_status.py:21-56 |
| `status_payload` composes the best-effort landing arc (remote/PR probe) via this module. | `status_payload` | mcp/src/agents_remember/worktrees/modules/guidance.py:461-463 |
| `carryover_done` reads the official ledger via `load_ledger`/`find_mapping`. | "row = find_mapping(load_ledger(ledger_path), landed)" | mcp/src/agents_remember/worktrees/modules/guidance.py:221-221 |
| Cleanup hard-guards on `carryover_done` before deleting the parked memory branch. | `carryover_done` | mcp/src/agents_remember/worktrees/modules/cleanup.py:432-437 |
| The `carryover-pending`/`cleanup-pending` routing + `carryover_done` are pinned here. | "def test_routes_carryover_pending_when_not_carried(self, cd: MagicMock) -> None:"; "def test_routes_cleanup_pending_with_done_at_when_carried(self, cd: MagicMock) -> None:" | mcp/tests/test_cleanup_carryover.py:173-173; mcp/tests/test_cleanup_carryover.py:180-180 |
| `WorktreeSummary` imports `WorktreePhase` / `NextOperation` / `NextTool` from this module rather than restating them. | "    NextOperation,"; "    NextTool,"; "    WorktreePhase," | mcp/src/agents_remember/models/worktree.py:16-18 |
| The six persisted contract vocabularies imported for `WorktreeStatusFacts`. | `WorkflowKind`, `MemoryMode`, `HumanReviewStatus`, `CloseoutStatus`, `IntegrationStatus`, `CleanupStatus` | mcp/src/agents_remember/worktrees/worktree_contract.py:63-68 |
| `unknown_cells` is the source of `unknown_contract_cells`. | `unknown_cells` | mcp/src/agents_remember/worktrees/worktree_contract.py:287-287 |
| Three of the five `recovery_guidance` callers: the blocked memory, provider-setup and stale-base starts. | "choose_memory_recovery"; "choose_provider_setup_recovery"; "choose_stale_base_recovery" | mcp/src/agents_remember/worktrees/modules/start.py:121-121; mcp/src/agents_remember/worktrees/modules/start.py:177-177; mcp/src/agents_remember/worktrees/modules/start.py:356-356 |
| The fourth: the closeout preview's `request_commit_approval` gate. | `request_commit_approval` | mcp/src/agents_remember/worktrees/modules/closeout.py:384-384 |
| The fifth: `_memory_sync_block`'s `choose_memory_sync_recovery`. | "def _memory_sync_block("; "choose_memory_sync_recovery" | mcp/src/agents_remember/worktrees/modules/sync.py:149-149; mcp/src/agents_remember/worktrees/modules/sync.py:165-165 |
| The two named exhaustiveness tests are defined in this module. |"def test_every_contract_literal_validates_at_its_wire_field(self) -> None:"; "def test_a_live_contract_projects_onto_the_wire_model(self) -> None:"|mcp/tests/test_wire_vocabulary_exhaustiveness.py:635-635; mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:413-413|

## Invariants And Boundaries

- **One declaration per vocabulary.** `WorktreePhase`, `NextOperation` and `NextTool` are declared
  here and imported by `models.worktree`; do not restate a member at the response boundary. A
  second copy is what the packet's 260731-EFA-L4 failures were made of.
- **A phase payload uses `next_guidance`; a block or gate uses `recovery_guidance`.** Do not widen
  `NextOperation`/`NextTool` to admit a recovery caller — that vocabulary is what
  `WorktreeSummary.nextOperation` publishes, and a `worktree_status` response can never contain
  `choose_stale_base_recovery`.
- A next-move key with nothing to say is omitted, never defaulted. `next_guidance` writes `nextTool`
  / `nextArgs` / `nextRequiredArgs` only when there is a value, and the packet projection preserves
  the absence.
- `unknown_contract_cells` is additive and normally absent; its presence means the phase beside it
  was computed from substituted values.

## Series-Contract Notes

Guidance/status payloads now expose contract `kind`, `leaf_id`, `enclosure_path`, and optional `parent_contract_path`, making the leaf/root split visible to dashboard and tool callers.

## Update History

- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer semantic correction: corrected the worktree-status and carryover
  source owners, removed the false skill-tool claim, and split persisted vocabularies from unknown cells.

- 2026-08-02T17:00+02:00 — 260731-EFA-L6 curator W1-B03: repaired 10 citation rows with exact anchors and current source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:30+02:00 — 260731-EFA-L4 curator: the card described the phase machine but not the
  vocabulary it now declares, and the three L2 helper signatures it quoted (`-> dict | None` /
  `-> dict`) had become false — they are `-> LifecycleGuidance | None` / `-> LifecycleGuidance`.
  Corrected those and added the section for what this leaf put above the state machine: the
  `WorktreePhase` / `NextOperation` / `NextTool` / `RecoveryOperation` / `RecoveryTool` `Literal`s
  (members transcribed from the source, not from the summary) and the `NextGuidance` /
  `LifecycleGuidance` / `WorktreeStatusFacts` / `WorktreeStatusPayload` `TypedDict`s, backed by the
  new `from typing import Any, Literal, NotRequired, TypedDict` and the six vocabulary imports from
  `worktree_contract`. Recorded the new `recovery_guidance` function and, checked against all five
  of its call sites, why it is separate rather than a widened `next_guidance`: identical keys on the
  wire, but its callers render as `FlexibleToolResponse` and never reach `WorktreeSummary`, whose
  `nextOperation` would otherwise have had to admit them. Also recorded `next_guidance`'s narrowed
  signature, the new `unknown_contract_cells` key in `_status_payload_with_landing`, the
  `{**facts, **guidance}` merge that replaced `payload.update(guidance)` (key order unchanged), and
  the `-> WorktreeStatusPayload` return on both `status_payload` and `projected_status_payload`.
  Added an Invariants section and six reference rows. Verification metadata pinned until closeout
  stamps the L4 commit.
- 2026-07-31T20:56+02:00 — 260731-EFA-L3 curator: the Code Commentary said `run_git` comes from
  `modules.git`; that import is gone (`from agents_remember.kernel.git_command import run_git`,
  `modules.git` now supplies only `worktree_dirty`) and `modules.git` no longer defines a runner at
  all, so the sentence was false. Corrected it and the slice-09 parenthetical, and recorded what the
  one call site — `carryover_done`'s `run_git(memory_repo_path, ["show", "-s", "--format=%cI",
  row.memory_commit])` — inherits from the shared runner: the `GIT_DIR`-family scrub and the 300s
  `GIT_LOCAL_TIMEOUT_SECONDS` default, uncaught because the `except LedgerError` does not cover it.
  Historical entries left as written. Verification metadata pinned until closeout stamps the L3
  commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0911`/`PLR0912` armed with no
  exemptions): `lifecycle_guidance` became a three-way `or` chain over `_reclaimed_phase`,
  `_post_integration_phase` and `_pre_integration_phase`. The first two return `None` for "not my
  group", preserving the old top-to-bottom precedence; the third always returns a phase. Every
  emitted phase, summary and `next_guidance` block is unchanged. Verification metadata pinned until
  closeout stamps the L2 commit.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: separated interactive status landing probes from projected status, which accepts only the latest immutable observation and its freshness truth.

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: status and next-action payloads now include `kind`, `leaf_id`, `enclosure_path`, and `parent_contract_path`, while retaining `contract_path` for callers that have not yet renamed the field. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T07:25+02:00 — slice 09 (gate-signal adoption, S1 visibility fix): removed the dirty-tree → `commit-approval-pending` branch from `lifecycle_guidance` — a dirty worktree no longer fabricates a commit-approval gate and instead falls through to its honest lifecycle-position phase (closeout-completed → `integration-pending`, etc.). `commit-approval-pending` is owned by the closeout preview (`closeout.py`) and, once the gate plane is adopted, by a raised `closeout-approval` `GateNode` — never `git status`. Dropped the now-unused `contract_has_worktree_changes` import (`worktree_dirty`/`run_git` stay). Corrected the stale Code Commentary opening that still claimed the module reads worktree dirtiness into phases. Verification metadata pinned until closeout stamps the slice-09 code commit.
- 2026-06-21T06:40+02:00 — slice 05m (carryover-before-cleanup): added the public `carryover_done(contract) -> (done, carryoverDoneAt)` — it reads the OFFICIAL ledger (`memory_repo_path/memory.md` via `load_ledger`/`find_mapping`) to detect whether the landed code commit (`integrated_code_commit`, else `code_commit`) was carried home and returns the carry commit's `%cI`; external-only (internal/disabled → `(True, "")`). `lifecycle_guidance` now splits the `integration_status == "completed"` branch on it: not carried → phase `carryover-pending` (next: the existing `memory_carryover_apply`, args derived from the contract, `required_args=["intent_note"]`); carried → `cleanup-pending` with the new `carryoverDoneAt` in the guidance dict. New imports: `LedgerError`/`find_mapping`/`load_ledger` from `kernel.memory_ledger` and `run_git` from `modules.git`. Verification metadata pinned until closeout stamps the 05m code commit.
- 2026-06-21T04:10+02:00 — slice 05l P1 (backend teardown visibility, Gap A): `lifecycle_guidance` gained a `cleanup == "abandoned"` branch (right after the `cleanup == "completed"` branch) returning a dedicated `abandoned` phase (`nextOperation: "done"`). Previously an abandoned worktree fell through to the `worktree-started` default, so the dashboard rendered a deleted worktree as fully active; the explicit phase lets the observer project it for the teardown render (05k). Verification metadata pinned until closeout stamps the 05l-P1 code commit.
- 2026-06-18T08:51+02:00 — slice 5h H1: `status_payload` emits a best-effort `landing` block from `landing.landing_refs(contract)` (the successful-landing arc's remote/PR refs, gated to closeout-completed onward; git ls-remote + best-effort gh, honest factState, stdin=DEVNULL). Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-13T18:45+02:00 — Slice 2c: `status_payload` emits `lifecycle_id` (the contract's observable-lifecycle enclosure anchor) so `worktree_attach` can resume it. Verification metadata pinned until closeout stamps the 2c code commit.
- 2026-06-10T09:56+02:00 — Issue #54 sub-task D: added `base_freshness` (fetch-free recorded-base vs local source tip counts with a `worktree_sync` `syncHint`) and wired it into `status_payload` as `freshness`.
- 2026-06-10T07:30+02:00 — `status_payload` includes a `providers` block from `provider_async.provider_setup_status(contract)` when present: the worktree_status poll surface for background provider setup (running with currentPhase/heartbeat/seedFallback, stale on dead heartbeat, terminal ok/ready-with-failed-phases/failed with retryArgs) (GitHub #53).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
