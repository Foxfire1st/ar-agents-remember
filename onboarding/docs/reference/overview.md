# docs/reference

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | docs/reference |
| doc_type | route-local-overview |
| lastUpdated | 2026-08-30T12:42+02:00 |
| lastVerifiedCommitHash | `f9f92ca793811b6cb738d7e302dfecdf8636e96e` |
| lastVerifiedCommitDate | 2026-08-30T14:26:46+02:00|

## Purpose

### 260731-EFA-L23 Route Delta

L23 documents guarded MCP citation repair, task-addressed asynchronous closeout/integration and
cancellation, and Dagger as the sole acceptance executor. Host/unit invocations are diagnostic;
Python, Vitest, and Playwright refuse direct execution without the Dagger run nonce and container
attestation.

### 260713-TES-L1 Rename — Settings And Harness Reference

`settings-json.md` now documents the `orchestration.agentNotifier` family (the deterministic
agent-notifier sweep knobs) with the compatibility-window alias: the legacy
`orchestration.supervisor` key is accepted loudly and both-keys is refused. `harnesses.md` prose
was refreshed to agent-notifier wording; no harness contract changed.

### 260713-TES-L4 — Inbox Landing, Supersession, And Reserved Ladder Reference

`mcp-tools.md` now documents the N16 inbox contract (terminal `landed` only on correlated
adapter acceptance at a turn boundary), `include_terminal` poll inspectability (N11), the
attribution-only `operator_inbox_consume`, and the explicit `operator_inbox_supersede` tool
(R11). `settings-json.md` marks `escalationBudget` reserved (N3): the timed escalation ladder is
demolished as policy — rows resolve by the 5-attempt ceiling, the 5-minute rebind grace, or
explicit supersession — and the knob no longer gates sweep behavior (removed with the L5
demolition leaf).

### 260713-TES-L5 — Ladder Demolished, Budget Re-Wired

`settings-json.md` now documents `escalationBudget` as the per-sweep load-shed cap on
owner-signal emissions (seat-liveness + dead-upstream), the twin of `redeliverBudget`; the
`orchestration.escalation` settings family is removed (fail-loud unknown key), and the
recovery/observability docs use the fact-relay terminal paths (landing, attempt ceiling
`unresolved`, rebind grace `expired`) instead of ladder states. The legacy `ladder-resolved`
literal remains parse-compat and is still written by the confirmed-gone reclamation fold.

Reference contract for harnesses, MCP tools, and settings. ACPUI makes role settings the initial
native-selection authority: Claude, Codex, and Pi discover token-free per-install/account catalogs,
validate effort under the selected model, launch through adapter-owned native channels, and retain
honest same-session mutation evidence. The harness manual now keeps Claude's three startup evidence
sources distinct: correlated initialize supplies command rows, `system/init` supplies live session
state, and a separate correlated `list_models` response supplies the dynamic catalog and model-local
effort metadata. Settings-defined non-native harness mappings remain an explicit compatibility
surface rather than the default path. The route also retains the three-state hosted dispatch,
readiness, catalog-concurrency, and serving-cutover contracts.

## Hot Path Summary

The current orchestration references describe free chat as the identity-free launcher that, for
ordinary role-shaped work, compiles the canonical architect brief and calls `dispatch_agent` once
on the sprint document. An explicit developer-declared task-seat takeover is the bounded exception:
it targets the named role at that role's canonical task altitude rather than silently turning
ordinary free chat into a non-architect seat. Plane-hosted architect/orchestrator/manager seats use
the same public tool with injected seat identity and exact direct-child scope. Caller kind is
process-derived, the request never supplies caller identity, and a plane refusal never falls back
to ambient. Runtime identity and custody remain private control-plane evidence behind the canonical
task-document-plus-role seat. Role-table `dispatch` and `tools` rows describe structural authority
and capability; they are not settings keys and cannot override that caller matrix.

For native launch and control questions, read `harnesses.md` for the dynamic catalog,
model-gated effort, duplicate-selector refusal, distinct Claude startup evidence sources, and the
Claude/Codex/Pi launch/set matrix; read `settings-json.md` for the complete `roles.<role>` /
`rolesPerLevel` model-and-effort authority. Exact harness versions and captured catalog rows are
live/fixture evidence, not production pins; in particular, Claude Code 2.1.210 live-confirmed Fable
switching supersedes the earlier launch-only assumption without creating a Fable-name policy.
Structured hosted dispatch, complete serving reload, and the bounded R9 compatibility exception
remain separate contracts.

For task, closeout, and recovery questions, `mcp-tools.md` is the public tool-surface reference and
`worktrees-c09.md` explains the operational sequence. Task documents and closeout doors are canonical
publication authorities; closeout queue state is a disposable projection; the enclosure-external
journal owns claimed operation/evidence/recovery state; and the stable locator plus external archive
own terminal cleanup proof. Queue invalidation never blocks task authoring or erases a claimed
operation.

The quality boundary remains separate. `skills.md` records synchronized skill-copy checks at both
pre-commit and pre-push. The hook tiers are not equivalent: pre-commit runs a fast staged-content
tier without the wrapper, pre-push runs the change-set-scoped targeted Dagger tier, and the full
Dagger graph runs once per master at the master integration gate. The closeout gate applies to any
repository whose checkout carries the wrapper, not only `agents-remember`.

## IAS Execution-Topology Reference Impact

`execution-topology-migration.md` now describes graph-less scheduling as exact source-pair
activation, not a requirement that every master integrate fully before another begins. Canonical
commanded-master order is only the stable equal-priority tie-break. Selecting another atomic master
logically pauses and preserves the former while the new selection stays `reconciling` until its
exact code/memory bases are current.

The reference also makes the ownership boundary explicit: task authoring never reads selector or
queue state; queue projection observes active/reconciling/paused/vacant facts but owns no lifecycle
transition; and malformed selector state fails closed only for affected runtime projection or
admission before an exact selecting operation archives and replaces it. No contract-presence or
tolerant-reader fallback is documented.

## 260718-CHATS-L5I Commit-Gate Reference Impact

The public reference route now exposes the same mandatory source-quality order
as the implementation and runtime guidance. `worktree_closeout_apply` runs the
strict project-owned wrapper before a source commit — in any repository whose
checkout carries that wrapper, since 260731-EFA-L1 removed the
`agents-remember`-only condition;
`worktrees-c09.md` places that gate before code, onboarding, memory, and ledger
commit steps; and the skills reference names both pre-commit and pre-push sync
checks. These are documentation projections of the existing gate authority, not
independent bypasses or alternative check sequences.

## 260731-EFA-L2 Reference Impact

Two things a reader of this route must now hold.

**The tool surface has a new authoritative source, and `mcp-tools.md` says so.** It no longer points
at `mcp/server.py`; the `@server.tool()` registrations moved to
`mcp/src/agents_remember/mcp/registration/`, one module per tool family, and `create_server` only
walks `TOOL_REGISTRARS` — an ordered tuple that also fixes the order the server advertises tools in.
Response shapes are still enforced by `models/` via `tool_registry.PUBLIC_TOOL_RESPONSE_MODELS`.
When a tool is added or its schema changes, the family module under `registration/` is what to read,
and its `@server.tool()` signature **is** the published schema — this route's job is to project that
truth, not to restate a parameter list that can drift from it.

**Three commit-gate facts these public documents predate.** As with the L1 note above, `docs/` is
pathRules-excluded, so the durable record lives on the root overview and here:

1. **There are no baselines, allowlists, grandfather lists or exemption files anywhere in the
   gate.** Several were built during L2 and then deleted; the no-deferral rule forbids the category,
   so a document that describes "the current offender list" would be describing something that does
   not exist and cannot be created.
2. **The binding coverage gate is per-diff at 100%** — every statement and every branch arc leaving
   a changed line must be exercised, reported as named uncovered lines rather than a percentage.
   There is no aggregate coverage pin.
3. **CRAP consumes branch coverage at threshold 20.0** and refuses a coverage report that lacks
   branch data rather than silently falling back to statement coverage.

`worktrees-c09.md`'s quality-before-commit *sequence* is unaffected — the gate still runs before any
closeout mutation, and still fails closed. What changed is what the gate can catch.

## 260731-EFA-L6 Reference Impact

`mcp-tools.md` now carries three additions this route must hold:

1. **The memory tools are leaf-scoped by `contract_path`.** `drift_check`, `memory_quality_check`,
   and `route_index_refresh` all take the same optional `contract_path` as the `worktree_*` verbs.
   Supplied, they act on that leaf's memory worktree and measure it against the leaf's code
   worktree; `route_index_refresh` **writes**, so running it unscoped from inside a leaf dirties
   the official memory repo. The response carries `onboardingRoot`, so the acted-on tree is always
   visible.
2. **Citation ranges are not repaired by hand.** `agents-remember memory-citations --repo <id>
   --contract <enclosure contract> [--fix]` regenerates every range that can be regenerated from
   its anchor after a package move and prints a work order for the rest. `--contract` is required,
   and only pure moves (symbol keeps its name, changes file) are repaired — a rename, deletion, or
   ambiguous match is refused rather than guessed.
3. **Task-document and lifecycle rows were added.** `worktree_cleanup` is explicitly non-terminal
   for task documents; `lifecycle_finalize_task` proves the landed edge and completes the exact
   contract-bound leaf (with parent-row reconciliation); the new Task documents section names
   `task_doc` and `task_reopen`.

## 260731-EFA-L17 Reference Impact

The public reference docs were corrected to the ladder: `mcp-tools.md` and
`use-external-memory.md` describe the leaf `--targeted` closeout contract, `worktrees-c09.md`
places the full wrapper at the master integration gate inside `worktree_integrate`, and
`settings-json.md` documents optional `orchestration.qualityGate.memoryCapBytes`
(absent/host-managed default, fail-loud family) — the schema source for an
explicit constrained-environment full-gate cap.

## 260805-ARG-L1 Reference Impact

`settings-json.md` now documents the third retirement setting,
`autoCloseCompletedSeats` (default `true`). The two existing edge gates still decide whether
completion cleanup runs; this setting chooses its result for exact-leaf worker/reviewer/curator
seats. Default mode requires the exact sender's durable `turn-report`, retires the process through
normal session-retire semantics, and preserves transcript/report evidence. `false` restores the
landed/archive path. Manager and orchestrator seats are excluded in either mode. The public quality
description also reflects cheap-first subprocess ordering and CI-fresh local proof reuse policy.

## 260731-EFA-L19 Reference Impact

The public reference now presents structural agent control directly: agents dispatch and address
children by canonical task document plus role, while launch/session, inbox-row, adapter, and gate
correlations remain private control-plane state. `harnesses.md`, `mcp-tools.md`, and
`settings-json.md` describe that division and the settings-derived role/altitude launch selection;
the retired exact-session agent tools are not retained as a compatibility surface.

`drift-c02.md` distinguishes the task-start temporary drift report from the curator's full
contract-scoped combined checklist at `<worktree-enclosure>/reports/curator-memory-quality.md`.
That enclosure-local operational artifact is atomically replaced, combines repairable onboarding
and quality work with explicitly closeout-owned evidence, and is removed with the enclosure.

## R39 Settings Reference Disposition

The settings reference now names Dagger as the only accepted executor, places optional memory caps
inside the container wrapper, and removes host systemd/RLIMIT semantics. It also records that leaf
closeout and master integration are the only acceptance owners.

## 260821-CLIVE Canonical Lifecycle Reference

The public reference route now assigns each mutable fact one owner. Task mutation publishes first,
then invalidates/rebuilds the affected disposable queue projections and reports bounded effects;
projection failure cannot roll back task truth. A manager publishes an immutable closeout-door
generation, and the lifecycle journal atomically claims that exact waiting generation. Commit,
memory, ledger, review, cancellation, supersession, and recovery evidence live in the journal—not in
queue rows.

Closeout validates every enabled nonblank commit-message/input field before any claim. Retry and
repair are task-addressed through advertised controls and exact retained evidence; normal recovery
does not synthesize a missing initial door or guess a successor. Terminal cleanup/abandon publishes
and reads back a bounded external archive, receipt, and stable locator before removing the enclosure;
successor publication proves the exact archived predecessor. Discard-before-start is an audited
task-document transaction and cannot be used once work has begun.

The tool inventory documents `closeout_door`, status/rebuild-only `closeout_queue`, lifecycle
operation control, direct landing, adopt, cleanup/abandon, legacy-incident repair, and
discard-unstarted. These are routed authorities, not compatibility duplicates or raw-Git escape
hatches.

## 260821-DAGQC Memory-Quality Request Contract

The current `mcp-tools.md` reference uses one `memory_quality_check.request` discriminated by
`sync | start | poll`. Only sync/start carry contract path and execution/detail scope; poll carries
repository plus run id. Full leaf sync/start may publish the combined checklist; fresh success uses
`reportPath`, while `publishedResultPath` is recovery-only. Capacity refusal has no run id, and poll
cannot smuggle start-only fields. These newer DAGQC facts are additive to the CLIVE lifecycle split.

## 260815-DAG-L15 Route Impact

`execution-topology-migration.md` gained section 4 — the served-build preflight operator contract (run authoring through the deployed serving server; refresh the rc7 venv, L15-R4). The changed file is excluded by pathRules, so this route's onboardable surface is unchanged.

## Update History

- 2026-08-30T12:42+02:00 — 260821-ARSPAWN-L3 review correction: distinguished ordinary
  architect bootstrap from an explicit named-role takeover and made the structural role-table
  rows' non-settings boundary explicit. Verification remains closeout-owned.

- 2026-08-30T11:47+02:00 — 260821-ARSPAWN-L3 reconciled the public reference route to one
  `dispatch_agent` vocabulary, one-call architect bootstrap, disjoint plane/ambient authority, and
  no fallback. Verification remains closeout-owned.

- 2026-08-26T05:20+02:00 — Reconciled the reference route with the source-pair selector, paused
  live-master preservation, reconciling-before-active admission, retained conflict
  continuation/cancellation, unlocked task authoring, disposable queue ownership, and
  no-fallback boundaries documented in `execution-topology-migration.md`.

- 2026-08-24T15:04+02:00 — Reframed the reference hot path around canonical task/door/journal/
  locator ownership, disposable queue rebuilds, exact retry/terminal/discard contracts, and preserved
  the concurrent DAGQC discriminated memory-quality request contract.

- 2026-08-20T21:30+02:00 — 260815-DAG-L15 route impact: execution-topology-migration.md gained the served-build preflight operator section (excluded file; onboardable surface unchanged). Verified at code commit de3a0fd9.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13 route impact: `execution-topology-migration.md` was
  retitled from the migration cutover to graph authoring — the atomic-sequential default covers
  graph-less sprints and `author_execution_graph` bootstraps the graph; the reference-route model
  is unchanged. Verification remains closeout-owned.
- 2026-08-18T12:00:00+00:00 — No route impact: L9 adds `execution-topology-migration.md` (operator migration/rollback reference); the reference-route model is unchanged.
- 2026-08-18T09:10+02:00 — No route impact: renamed the atomic 'barrier' concept to 'blocker' throughout; route purpose unchanged.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-14T11:29+02:00 — R39 curator: reconciled the documentation route with the final
  settings and altitude contract. Verification remains closeout-owned.

- 2026-08-14T06:25+02:00 — L23 final candidate review: corrected quality references to
  Dagger-only acceptance and fail-closed host test startup; removed the stale local-executor and
  host-managed-full descriptions. Verification remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator route review: L23 documents guarded MCP citation repair, task-addressed asynchronous closeout/integration and cancellation, and exact `local`/`dagger` quality-executor policy with fail-closed selection. Verification provenance remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: corrected the
  settings-reference route from a mandatory 2 GiB cap to host-managed memory
  with an optional explicit cap. Verification metadata remains pinned until
  closeout stamps L24.

- 2026-08-11T19:58+02:00 — 260731-EFA-L19 curator: reconciled the four changed reference files
  with structural agent control and the enclosure-local curator checklist; no exact-session public
  control or duplicate drift-report authority remains.

- 2026-08-10T07:30+02:00 — 260805-ARG-L1: `settings-json.md` now documents default-on completion
  close, the exact durable report blocker, owner exclusions, landed/archive opt-out, and the
  cheap-first quality/retry contract.

- 2026-08-10T04:39+02:00 — 260713-TES-L6: reviewed the reference route for sprint-bound command
  seats and migration-only unbound language. Verification metadata remains pinned until closeout.

- 2026-08-09T12:08+02:00 — 260713-TES-L5 route impact: recorded the escalation-family
  removal, the `escalationBudget` load-shed re-wiring, and the fact-relay terminal vocabulary
  in the reference docs; superseded the L4 "reserved/removed" row in place. Verification
  metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 route impact: recorded the `mcp-tools.md` inbox
  landing/supersession rows (N16/R11/N11) and the `settings-json.md` escalationBudget reserved
  wording (N3, ladder demolished as policy). Verification metadata pinned until closeout stamps
  the 260713-TES-L4 commit.
- 2026-08-08T21:20+02:00 — 260713-TES-L1 route impact: `settings-json.md` documents the
  `orchestration.agentNotifier` family with the compatibility-window alias, and `harnesses.md`
  prose was refreshed to agent-notifier wording; route shape unchanged. Verification metadata
  pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 route impact: recorded the corrected hook-tier and
  closeout wording in the public references plus the `qualityGate` settings family. Verification
  metadata stays pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-05T03:47+02:00 — 260731-EFA-L6 curator: recorded the reference-route impact of the
  contract-scoped memory tools (`contract_path` on `drift_check`, `memory_quality_check`,
  `route_index_refresh`, with write behavior and `onboardingRoot`), the required-`--contract`
  `memory-citations` repair rule (moves only), and the new task-document/lifecycle rows
  (`worktree_cleanup` non-terminal, `lifecycle_finalize_task`, `task_doc`, `task_reopen`).
  Verification metadata remains pinned.
- 2026-07-31T16:20+02:00 — 260731-EFA-L2 curator: `mcp-tools.md` now names
  `mcp/src/agents_remember/mcp/registration/` (one module per tool family, `TOOL_REGISTRARS` walked
  by `create_server`) as the authoritative tool surface instead of `mcp/server.py`. Flagged the
  three gate facts these pathRules-excluded reference documents predate: no baselines or exemption
  files exist anywhere in the gate, the binding coverage gate is a 100% per-diff floor, and CRAP
  consumes branch coverage at threshold 20.0. The closeout gate order is unchanged. Verification
  metadata remains pinned.
- 2026-07-31T04:28+02:00 — 260731-EFA-L1 curator: flagged the two commit-gate facts these public
  reference documents now predate — the fast/full hook tier split (pre-commit no longer runs the
  wrapper) and the removal of the repository-name condition from the closeout gate. The skill-copy
  check claim remains true in both tiers. The referenced `docs/` sources are pathRules-excluded, so
  the durable contract lives on the root overview. Verification metadata remains pinned.

- 2026-07-24T14:44Z — 260718-CHATS-L5I preview-gate remediation: refreshed the
  route body for the public MCP closeout description, strict
  quality-before-commit worktree order, and pre-commit/pre-push skill-sync
  checks. Verification metadata remains pinned until the code commit.

- 2026-07-16T07:27+02:00 — 260714-ACPUI-L5 curator: aligned the reference route with the final
  three-source Claude startup contract, live native advertise/launch/set evidence, dynamic Fable
  switching, and the rule that captured versions/catalog rows remain evidence rather than pins.
- 2026-07-15T23:31+02:00 — 260714-ACPUI-L2 closeout-preview delta: replaced the stale static
  registry/session-command launch summary with settings-owned complete selection, token-free
  per-install catalogs, model-local effort validation, native Claude/Codex/Pi launch channels, and
  honest startup evidence.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: refreshed the reference route body for the
  negotiated capability model, full reload ownership, and deferred R10 boundary.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: refreshed the reference route for structured harness
  capability negotiation, full serving reload ownership, and the deferred R10 boundary.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 closeout remediation: refreshed the reference route body for
  the final harness effort policy and explicit control-bridge boundary.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator: established governing route coverage for the final candidate.
