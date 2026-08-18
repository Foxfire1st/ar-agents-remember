# test_tool_response_conformance.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                 |
| path                   | `mcp/tests/test_tool_response_conformance.py`      |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-08-15T14:05+02:00 |
| lastVerifiedCommitHash | `cdcdc566fc6bee44b371a9d15c2048ceb1a49b8b`|
| lastVerifiedCommitDate | 2026-08-18T03:31:59+02:00|
| governingOverview      | `overview.md`                                      |

## Purpose

`test_tool_response_conformance.py` moves the production response-contract
guarantee into the test suite: every response-modeled MCP payload builder produces
a payload that conforms to its registered Pydantic response model (L11: the worktree
flow ends by reopening the landed demo-task leaf so `task_reopen` has a live
representative payload), so application entry point
drift is caught at dev time instead of in a live tool call.

## Code Commentary

### Logic

Production already validates each tool payload through
`tools._tool_payload()` against `models.tool_registry.TOOL_RESPONSE_MODELS`
(strict models use `extra="forbid"`). These tests reproduce that guarantee by
obtaining a *representative* payload for every modeled builder from the real
`*_payload` builder, then asserting conformance.

`setUpClass` builds eight temporary fixtures (each in its own temp dir) and
collects one representative payload per tool into `cls.payloads`:

- `_base_fixture` / `_simple_payloads`: a code repo, memory layer, and
  `.codex/mcp` settings drive the directly runnable tools (core, context,
  runtime, memory, skills, provider status/diagnostics/watchers, GrepAI/CGC
  dry-run, baseline, benchmarks, HFX-L4 representative task docs for canonical leaf-ref validation,
  the L9 terminal leaf reassignment builder's missing-session
  payload, (HFX2-L10) the `spawn_agent_session` builder's `spend-override-unsupported` refusal
  payload — a legacy caller-supplied harness id short-circuits before any tmux spawn, so the
  fixture never touches a real terminal host — and (260707-HFX-L8) representative
  `session_retire`/`session_rename` refusal
  payloads: `tools.session_retire_payload(config, actor_session_id="missing-actor",
  session_id="missing-session")` and `tools.session_rename_payload(config,
  session_id="missing-session", label="New Label")`, both short-circuiting before touching a real
  tmux host because neither session id has a catalog row).
- `_worktree_payloads`: a real worktree lifecycle in explicit disabled-memory mode
  with task-doc leaf fixtures for the worktree-start leaves
  produces `worktree_start`, `worktree_status`, `worktree_attach`,
  `worktree_sync` (dry-run, GitHub #54 sub-task D), `worktree_closeout_preview`,
  `worktree_closeout_apply`, an explicit checkout of the parent integration branch before
  `worktree_integrate`, `worktree_cleanup`, and
  `lifecycle_finalize_task` (dry-run) against a real contract.
- `_carryover_payloads`: a landed-branch fixture drives `memory_carryover_plan`
  and `memory_carryover_apply` (a docstring names the
  `c-11-memory-carryover-from-branch` skill).
- `_lifecycle_payloads`: installs an ambient lifecycle over a temp `EventStore`
  and drives the lifecycle signal payloads (task 28 adds a representative
  `lifecycle_turn_end_notification` payload — the NOTIFY-AND-CONTINUE turn end that
  leaves the lifecycle `awaiting-developer`); `lifecycle_block` remains here as
  lower-level compatibility coverage, not as an advertised public MCP tool.
  **Since 260731-EFA-L4 it first calls `_stale_supervisor(observer_root)`** — see below.
- `_task_doc_payloads`: a base fixture authoring one representative `task_doc`
  document (a `create` of a `master`, since `light` is no longer authorable), so the
  JSON-primary task tool has a payload (slice 3c).
- `_gate_payloads`: a base fixture driving `lifecycle_gate` with an injected
  developer decision for deterministic conformance, then create/decide/wait/response-wait/list
  compatibility payloads, so both the public unified gate response and retained
  lower-level gate response models have representative payloads.
- `_operator_inbox_payloads`: a base fixture posting, polling, consuming, and — since
  260713-TES-L4 — superseding one external-chat inbox entry, so the four `operator_inbox_*`
  tools have representative payloads (task 10 + L4's R11 supersession).

The former `_direct_closeout_payloads` fixture was removed with the
`direct_closeout_*` tools (issue #62 worktree-only closeout).

**260731-EFA-L4 — the fixtures now write a stale agent-notifier heartbeat.** `_stale_agent_notifier(root)`
cit:([`_stale_agent_notifier`], mcp/tests/test_tool_response_conformance.py:578-587) does `AgentNotifierHeartbeatStore(observer_root).tick(now=datetime.now(UTC) -
timedelta(hours=6))`, and both lifecycle-bearing collectors call it before installing their ambient
(`_lifecycle_payloads` L356-L388, `_gate_payloads` L415-L483). This is not decoration. The two
envelope-wide keys the choke point adds — `nextStep` and `agentNotifierBanner` — are set in
`mcp.tools.base._attach_lifecycle_tail`, and `_agent_notifier_banner` is *opportunistic*: a workspace
whose supervisor has **never** ticked is deliberately silent, so `agentNotifierBanner` never fired.
This suite therefore sat exactly at the mutation point and validated the one shape the choke point
cannot break. A **ticked-then-quiet** row is the state in which the choke point adds the key, so it
is the state the contract has to be checked in.

cit:([`test_the_choke_point_injections_are_actually_exercised`], mcp/tests/test_tool_response_conformance.py:828-845) makes that self-verifying: it
asserts `lifecycle_start` is among the payloads carrying `nextStep`, and that both
`lifecycle_start` and `lifecycle_gate` carry `agentNotifierBanner`. A fixture that quietly stops
producing them is now a failure here rather than a silent hole under every conformance assertion
below it. Both keys are declared envelope fields since this leaf (`models.base`), which is what
makes them validate rather than fail `model_validate` as an undeclared extra.

`tearDownClass` removes the temp dirs with `shutil.rmtree(..., ignore_errors=True)`
because git worktrees leave read-only pack files that otherwise break cleanup on
Windows.

`test_every_modeled_tool_has_a_representative_payload` asserts the payload set
exactly covers the registry. `test_representative_payloads_conform_to_registered_models`
asserts, per tool, that the payload validates and that round-tripping
(`model_validate(...).model_dump(mode="json", exclude_none=True)`) fabricates no
keys. `test_strict_response_models_forbid_extra_fields` asserts the
strict/flexible split matches the response-model taxonomy.
`test_completion_cleanup_fields_are_declared_on_both_edge_models` pins the four ARG-L1
close/deferred/failed/landed fields on both integration and finalization models, catching a strict
finalizer wire rejection even when a representative dry-run payload has empty cleanup.

### Conventions

Fixtures reuse helpers from `test_worktree_support` (`init_repo`, `commit_file`,
`git`, `initialized_memory_repo`, `write_file_onboarding`) and settings from
`test_config`. `_allowed_keys()` collects a model's field names plus any
aliases/serialization aliases.

The round-trip check is taxonomy-aware: strict models (not built on
`FlexibleResponseModel`) may emit only declared fields, while intentionally
flexible models (`extra="allow"`, e.g. provider-native command plans that carry an
undeclared `command` key by design) may also pass through keys present on the
input payload — so the assertion is "round trip invents no keys that are neither
declared nor part of the input."

### Invariants And Boundaries

- Prefer the real application entry point/`*_payload` builder for representative payloads; fall
  back to hand-built fixtures only where invoking the application entry point is impractical
  (currently none are needed — every modeled tool runs for real, including the
  task-28 `lifecycle_turn_end_notification`).
- Strict response models must keep `extra="forbid"`; flexible models keep
  `extra="allow"`. The structural rule is `FlexibleResponseModel` membership.
- This is a dev-time conformance net; the runtime contract still lives in
  `_tool_payload()`.
- The fixtures must keep capturing payloads in a state where the choke-point injections **fire**.
  A never-ticked supervisor is silent by design, so without `_stale_supervisor` the suite covers
  only the envelope shape that has no `agentNotifierBanner` on it —
  `test_the_choke_point_injections_are_actually_exercised` is what keeps that from regressing
  unnoticed.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The registry maps each public tool to its response model. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tool_registry.py:116-179 |
| `_tool_payload()` is the production validation path mirrored here. | `_tool_payload`; "def complete_tool_response(" | mcp/src/agents_remember/application/tool_response.py:53-53; mcp/src/agents_remember/mcp/tools/base.py:72-74 |
| The strict/flexible response-model taxonomy lives in the model base. | `StrictResponseModel`, `FlexibleResponseModel` | mcp/src/agents_remember/models/base.py:10-13; mcp/src/agents_remember/models/base.py:16-19 |
| Worktree/carryover fixtures reuse worktree test helpers. | `init_repo`, `write_file_onboarding`, `initialized_memory_repo` | mcp/tests/test_worktree_support.py:78-98; mcp/tests/test_worktree_support.py:169-190; mcp/tests/test_worktree_support.py:323-351 |
| Schema-level registry coverage is asserted separately. | `test_every_public_tool_has_a_response_model` | mcp/tests/test_models.py:17-18 |
| Inbox representative payloads call the real post, poll, consume, and supersede builders. | `_operator_inbox_payloads` | mcp/tests/test_tool_response_conformance.py:740-767 |
| Lifecycle finalizer representative payload exercises the new terminal worktree tool. | `lifecycle_finalize_task_payload` | mcp/src/agents_remember/mcp/tools/lifecycle_finalize.py:15-32 |
| Terminal representative payloads exercise the strict `AttachTerminalSessionToTaskResponse` (unknown-session) and `SpawnAgentSessionResponse` (retired caller-harness input) models. | `_simple_payloads`; `AttachTerminalSessionToTaskResponse`; `SpawnAgentSessionResponse`; "definitely-not-a-real-harness" | mcp/src/agents_remember/models/terminal.py:35-48; mcp/src/agents_remember/models/terminal.py:91-134; mcp/tests/test_tool_response_conformance.py:246-381 |
| The choke point that sets both envelope-wide keys before the single dump — `_attach_lifecycle_tail` assigns `nextStep` and `agentNotifierBanner` (plus the legacy `supervisorBanner` alias), and `_agent_notifier_banner` is exception-safe and silent on a never-ticked agent-notifier, which is why the fixtures have to tick one into the past. | `_agent_notifier_banner`, `_attach_lifecycle_tail`, `complete_tool_response` | mcp/src/agents_remember/application/tool_response.py:22-31; mcp/src/agents_remember/application/tool_response.py:34-48; mcp/src/agents_remember/application/tool_response.py:49-61 |
| `nextStep` and `agentNotifierBanner` (plus the legacy `supervisorBanner` alias) as declared envelope fields, which is what lets a banner-carrying payload validate at all. | "class ResponseModel(" | mcp/src/agents_remember/models/base.py:41-60 |
| The heartbeat store the fixtures tick and the staleness banner they make fire. | `AgentNotifierHeartbeatStore` | mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:63-109 |
| The sibling suite that pins the same two keys against the token count and the response model on the tool side. | `test_tool_payload_attaches_next_step_and_lifecycle_start_emits_rundown`, `test_advertised_token_count_covers_the_attached_next_step` | mcp/tests/test_next_step.py:298-303; mcp/tests/test_next_step.py:305-317 |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

## 260815-DAG-L3 Queue Response Conformance

The representative payload set now constructs canonical organizational master/sprint graph facts,
resolves an ambient orchestrator seat, calls the real `closeout_queue` status payload, and validates
it against `CloseoutQueueResponse` with the rest of the public success surface.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## Update History

- 2026-08-17T14:00+02:00 — No content impact: L5 repair; added a demo code change and a `load_contract` import to the conformance fixture so the demo leaf prepends a fresh ledger mapping. The documented tool-response conformance surface is unchanged.

- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: every representative leaf fixture now
  has its canonical commanding sprint and integration branch; only `executionGraph` remains
  conditional so intentionally unmanaged lifecycle payloads do not enter queue governance.
- 2026-08-15T13:08+02:00 — No content impact: removed the unused configurable repository
  parameter from the private leaf-fixture helper; every caller already used the canonical
  `agents-remember` repository and all generated payloads are unchanged.
- 2026-08-15T11:43+02:00 — No content impact: accepted Ruff's one-line list-comprehension
  formatting; the generated node fixtures and conformance assertions are unchanged.
- 2026-08-15T11:07+02:00 — L3 Dagger repair: representative sprint graphs now create one
  canonical node for every `orchestrates` entry before exercising the strict queue response.
- 2026-08-15T09:53+02:00 — No content impact: L3's Pyright repair constructs the closeout-queue
  sprint reference explicitly; the response-conformance payload and assertions are unchanged.
- 2026-08-15T09:10+02:00 — L3 content update: added a real closeout-queue status payload to strict
  response conformance; verification remains closeout-owned.
- 2026-08-14T06:40+02:00 — L23 final candidate review: response conformance retains bounded
  task-addressed operation status and excludes private operation, lease, worker, and resume ids.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: No content impact: the L9 citation/body repair was re-read against the current staged response-conformance source; the existing sidecar remains accurate. Verification metadata remains pinned until closeout.
- 2026-08-10T10:40+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-10T05:45+02:00 — 260805-ARG-L1: added an explicit cross-model declaration proof for
  all four completion-seat cleanup fields. Verification remains pinned until closeout stamps
  ARG-L1.

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded `operator_inbox_supersede` joining
  the inbox representative payloads (R11 explicit supersession response conformance).
  Verification metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-03T03:59:59+02:00 — Curated 25 citation findings (12 table rows, 1 prose citation, 12 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:00+02:00 — 260731-EFA-L4 curator: the fixtures now write a **stale agent-notifier
  heartbeat**, and that is a real change to what this suite covers, so the card gained a paragraph
  for it. cit:([`_stale_agent_notifier`], mcp/tests/test_tool_response_conformance.py:578-587) ticks
  `AgentNotifierHeartbeatStore(...).tick(now=datetime.now(UTC) - timedelta(hours=6))`, and both
  lifecycle-bearing collectors call it before installing their ambient (`_lifecycle_payloads`
  L356-L388, `_gate_payloads` L415-L483). Verified the reason against
  `mcp/tools/base.py`: `_attach_lifecycle_tail` sets `nextStep` and `supervisorBanner`, and
  `_supervisor_banner` is silent on a workspace whose supervisor has never ticked — so before this
  leaf the suite sat exactly at the mutation point and never reached it, validating the one
  envelope shape the choke point cannot break. Recorded the new
  cit:([`test_the_choke_point_injections_are_actually_exercised`], mcp/tests/test_tool_response_conformance.py:828-845) and the invariant it exists
  to hold, plus four Repo-Internal rows for the choke point, the two now-declared envelope fields,
  the heartbeat store, and the sibling `test_next_step.py` coverage. The Repo-Internal table is a
  deliberate 2-column `| Finding | Source Path |`; the new rows were written with 2 cells so the
  table stays well formed (a 3-cell row under a 2-column header silently shifts its link into a
  column that does not exist). The eight fixtures, the payload set, and the three conformance
  assertions are otherwise unchanged. Verification metadata pinned until closeout stamps the L4
  commit.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: No content impact: the diff is entirely the
  PLR0913 parameter-object conversion of the representative-payload call sites
  (`GrepaiSearchQuery`, `GrepaiTraceQuery`, `ProviderQueryScope`, `TaskRef`, `TaskIdentity`,
  `TaskBases`, `StartExecution`, `CloseoutCommitMessages`, `CloseoutApproval`,
  `CarryoverSelection`, `TaskDocTarget`/`TaskDocEdit`,
  `GateRaise`/`GateWait`/`GateRequest`/`GateAnchor`/`GateVerdict`,
  `InboxAddress`/`InboxMessage`/`InboxPoster`, `NudgeTarget`/`NudgeSubject`,
  `RetiredSpawnInputs`, `AmbientTiming`), plus the two module constants
  `DRY_RUN_SCOPE`/`DISABLED_MEMORY_BASES` and a `_carryover_selection` builder factored out of
  the two carryover calls. None of those keywords were named by this card, and every literal it
  does quote still matches the source byte for byte: `tools.session_retire_payload(config,
  actor_session_id="missing-actor", session_id="missing-session")` and
  `tools.session_rename_payload(config, session_id="missing-session", label="New Label")` are
  untouched, `worktree_sync` and `lifecycle_finalize_task` still pass `dry_run=True`, and the
  `c-11-memory-carryover-from-branch` docstring is still there. I counted the fixtures:
  `setUpClass` still builds eight temp dirs and still calls the same eight collectors, no
  `*_payload` entry was added or removed from `cls.payloads`, and the three conformance test
  functions and their strict/flexible taxonomy assertions are unchanged, so the coverage and
  round-trip claims hold as written.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-09T12:04+02:00 — 260707-HFX2-L10 (spawn settings authority): the representative
  `spawn_agent_session` payload changed from `harness-unknown` to the new
  `spend-override-unsupported` refusal, because legacy caller-supplied harness/model/effort values
  now fail before harness lookup. The conformance purpose is unchanged: strict response shape is
  still validated through the real payload builder. Verification metadata pinned until closeout
  stamps the 260707-HFX2-L10 commit.

- 2026-07-08T02:43+02:00 — 260707-HFX-L8 (seat lifecycle: retirement + live identity +
  turn-state): `_simple_payloads` gained two new representative payloads —
  `session_retire`/`session_rename` — so the conformance sweep (which walks
  `TOOL_RESPONSE_MODELS` and validates every registered tool has at least one representative
  payload round-tripping through its Pydantic model) covers the two new seat-lifecycle tools.
  Verification metadata pinned until closeout stamps the HFX-L8 commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: representative fixtures now write task docs for terminal
  leaf assignment and worktree-start payloads, and worktree-start conformance explicitly requests disabled
  memory, so strict response conformance runs through canonical leaf-ref validation without creating
  external-memory parent branches. Verification metadata pinned until closeout stamps the 260707-HFX-L4
  commit.
- 2026-07-04T12:31+02:00 - L3: added a representative
  `orchestration_nudge_manager` payload and kept the expanded inbox responses in
  the modeled conformance path. Verification metadata pinned until closeout
  stamps the L3 commit.
- 2026-07-04T11:10+02:00 — L2: `_simple_payloads` now includes a representative `spawn_agent_session`
  payload (a `harness-unknown` refusal, which short-circuits before any tmux spawn), so the new strict
  `SpawnAgentSessionResponse` model is covered by `test_every_modeled_tool_has_a_representative_payload`
  / `test_representative_payloads_conform_to_registered_models`. Verification metadata pinned until
  closeout stamps the L2 commit.
- 2026-07-03T00:30+02:00 — L11: the worktree-flow fixture reopens the fully landed demo-task leaf, giving task_reopen a real representative payload against TaskReopenResponse.
- 2026-07-02T17:04+02:00 — L9: `_simple_payloads` now includes a representative
  `attach_terminal_session_to_leaf` payload (`unknown-session` fixture), so the new strict response model
  is covered by the conformance suite. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-29T21:24+02:00 — Post-landing cleanup (master/leaf-only authoring): the representative
  `_task_doc_payloads` fixture now authors a `master` instead of a `light` document, because
  `task_doc` create/replace refuse `light`. Conformance coverage is otherwise unchanged.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE turn end): `_lifecycle_payloads` now also drives a representative `lifecycle_turn_end_notification` payload, so the new public tool's registered response model is covered by `test_every_modeled_tool_has_a_representative_payload` / `test_representative_payloads_conform_to_registered_models`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T18:43+02:00 — Regression fixture update: `_gate_payloads`
  now resolves the representative `lifecycle_gate_payload` through an injected
  developer-attributed decision instead of the internal zero-timeout path.
- 2026-06-26T17:05+02:00 — Regression fixture update: `_gate_payloads`
  preserves deterministic conformance coverage after the public junction became blocking.
- 2026-06-26T14:16+02:00 — Task 25: conformance now targets `TOOL_RESPONSE_MODELS`, adds a representative `lifecycle_gate` payload, and keeps split gate/block/wait payloads as compatibility coverage rather than public-tool coverage.
- 2026-06-25T07:17+02:00 — Task 19: `_gate_payloads` now includes a representative `gate_response_wait` payload so the new public helper is covered by response conformance. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-23T22:50+02:00 — Dashboard task 14: added a representative `lifecycle_finalize_task` payload to the worktree fixture, so all 51 public tools still validate through their registered response models. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: added `_operator_inbox_payloads` and a seventh fixture so the three `operator_inbox_*` tools have representative payloads; the suite now covers 50 public tools. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-18T01:05+02:00: Task 6 slice 6a — added the `_gate_payloads` fixture (a sixth fixture) so the four `gate_*` tools have representative payloads; the suite now covers 47 public tools. Verification metadata pinned until closeout stamps the 6a code commit.
- 2026-06-13T22:34: Slice 3c commit 1 — added the `_task_doc_payloads` fixture (a fifth fixture) so the `task_doc` tool has a representative payload; the suite now covers 43 public tools. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T16:41+02:00: Slice 2b — added the `_lifecycle_payloads` fixture (a fourth fixture) so the six `lifecycle_*` tools have representative payloads; the suite now covers 42 public tools. Verification metadata pinned until closeout stamps the 2b code commit.
- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-06-11T06:47+02:00 — Removed the `_direct_closeout_payloads` fixture and its temp dir (issue #62 worktree-only closeout); the suite now covers the 36 public tools across three fixtures.
- 2026-06-10T09:56+02:00: Added the `worktree_sync` dry-run representative payload to the worktree fixture (GitHub #54 sub-task D).
- 2026-06-06T12:28+02:00: Corrected the `_tool_payload()` reference after the former `mcp/tools.py` module became the `mcp/tools/` package; source behavior unchanged.
- 2026-06-02T16:24+02:00: A docstring now references the `c-11-memory-carryover-from-branch` skill in full (was "C-11"). Reference-style normalization; behavior unchanged.
- 2026-06-01T20:45+02:00 — Extended conformance coverage to the new `worktree_abandon` payload/response model.
- 2026-05-29T08:53+02:00: Created onboarding for the dev-time tool-response conformance tests covering all public tools.
