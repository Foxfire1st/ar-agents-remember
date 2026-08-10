# skills/l-01-agent-lifecycles

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | skills/l-01-agent-lifecycles |
| doc_type | route-local-overview |
| lastUpdated | 2026-08-10T07:30+02:00 |
| lastVerifiedCommitHash | `b537abe20cf2498ef38e86e29ca586b5eec38466`|
| lastVerifiedCommitDate | 2026-08-10T08:37:35+02:00|

## Purpose

### 260713-TES-L1 Rename — Doctrine Wording

The canonical `skills/l-01-agent-lifecycles` tree and its nine synced copies now teach the
agent-notifier name (sweep/heartbeat/retry-path wording in SKILL.md, criteria, role files, and
templates); the lifecycle router, role registry, and doctrine content are unchanged.

Canonical lifecycle doctrine for hosted role dispatch. Spawn-only creation, an explicit readiness
gate, and one exact-session durable dispatch brief remain the three assignment states. ACPUI-L2
adds the settings-owned launch prerequisite: a configured role/level resolves one complete
harness/model/effort selection, then the own adapter validates that selection against its dynamic
model-local catalog and applies native launch configuration. Generated mirrors are outputs, not
doctrine owners.

## Hot Path Summary

The lifecycle router now treats free chat as the launcher and the architect as a separately bound
sprint command seat. Its shared liveness doctrine defines wake expectations across every direct
manager subordinate, so reviewer, curator, and future role seats cannot silently end the leaf when
the owner is also idle.

Hosted dispatch is role-first and exact-session throughout. Settings choose a complete native
model/effort pair; discovery and model-gated validation happen before the configured vendor session
starts; readiness precedes exactly one durable brief. Model/effort provenance is not configuration,
and normalized selection is never pasted through the composer. Canonical `skills/` content remains
the owner synchronized into package and harness mirrors.

### 260714-ACPUI-L2 Settings-Owned Native Launch

The lifecycle settings example now uses complete installed-catalog selections for every configured
role. The launch contract remains harness-native: Claude uses `--model`/`--effort`, Codex uses
thread model plus `model_reasoning_effort`, and Pi uses exact provider-qualified `--model` plus
`--thinking`. Missing, stale, unsupported, or conflicting selections fail through hosted control
state rather than falling back to a vendor default or becoming a model/effort session command.

### 260713-PHA-L5 Route Contract Review

The route remains governed by the shared hosted protocol bridge: exact adapter snapshots provide
readiness and liveness, correlated receipts sit beneath durable inbox rows, interactions use durable
gates, legacy/custom sessions are explicit unsupported states, and pane/log signals are diagnostic
only. Dashboard and packaged projections remain additive and synchronized.

### 260731-EFA-L6 Route Contract Review

Three changes landed on this route. `roles/curator.md` (and its brief template) now make the
curator's self-check explicit: `route_index_refresh`, `memory_quality_check`, and `drift_check`
are scoped to the leaf by passing the enclosure `contract_path`; without it they resolve the
official memory repo, and `route_index_refresh` writes there, leaving a repo the curator does not
own dirty. `criteria/report-verification.md` promotes RV-5 (canonical invocation target
provenance) from candidate to standing, with two catches including this leaf's S31 round-1
contract-name finding. `criteria/code-seam.md` now names the `application` entry point instead of
the controller in its production-wiring walk, matching the `controllers/` → `application/` move.

### 260731-EFA-L16 Route Impact — spawn doctrine and the guideline-adherence chain

Two developer-ruled doctrine waves landed. The spawn doctrine: role seats are created only via
`spawn_agent_session`, never as native sub-agents — now stated in the architect/orchestrator/
manager immutability clauses; the orchestrator's Sub-Agent Fan-Out section became "No Native
Sub-Agents — role seats only" (analyses run in-loop or dispatch as system-specialist/strategist
seats); native fan-out survives only on the hands-on seats (worker, reviewer, curator, and the
architect when building solo). The guideline-adherence chain: the worker's Orient step and brief
template now require reading the resolved `system/coding-guidelines.md` before the first edit,
the reviewer's second lens independently verifies adherence, and `c-12-closeout` Preconditions
plus Boundaries rule 10 relay named findings at the commit-approval gate — closing the hole
where green wrapper rails were the only signal (three leaves had shipped task identifiers in
source comments). The architect's Opening Move also gained a standing, repo-generic
`system/tools.md` inventory read.

## 260731-EFA-L17 Route Impact — The Quality Altitude Ladder

The lifecycle doctrine now states the ladder: `c-12-closeout` runs the leaf change-set-scoped
contract (`--targeted`) at leaf closeout and keeps `memory_quality_check` as a per-leaf closeout
gate; the full wrapper belongs to the master integration gate (inside `worktree_integrate`,
memory-capped); the worker/manager/orchestrator role files and their brief templates carry the
same ladder so no seat runs or expects a per-leaf full wrapper. Canonical `skills/` remains the
owner; the packaged `package_data/runtime/skills/` mirrors are sync-propagated copies.

## 260805-ARG-L1 Route Impact — Completion Cleanup And Retry Doctrine

Manager/orchestrator doctrine now treats the exact durable subordinate report and transcript as
the record: successful completion retries cleanup for worker/reviewer/curator seats, while
manager/orchestrator owners remain live until explicit handoff retirement. The landed/archive
path remains the setting-controlled opt-out. The closeout and orchestrator quality paragraphs also
state the wrapper-owned retry contract: cheap deterministic rails precede pytest, exact and
selected-test-only reuse are content-addressed and automatic, ambiguous deltas run fresh, a
conservative delta refusal falls back to one full selection, and CI always runs fresh.

### 260713-TES-L5 Route Impact — Judgment Demolition Doctrine

The lifecycle doctrine now teaches the fact-relay supervision model: the agent-notifier sweep
relays seat-state facts (turn-ended/completed state-signals, compound-idle, non-reaction
residue) and owners interpret; the timed escalation ladder (renudge → skip-level → architect
custody, then respawn) is retired from SKILL.md and the architect/manager/orchestrator/worker
role files. Dead-owner rows surface to the scoped architect mailbox; `operator_inbox_consume`
is an optional attribution marker. The `code-seam` criterion's coalescing invariant says
"date, tries, attempt" (no rung); the escalation-storm history remains catching evidence.

## Update History

- 2026-08-10T07:30+02:00 — 260805-ARG-L1: manager/orchestrator lifecycle doctrine now treats
  reports as the durable handoff and completed subordinate processes as reclaimable; owner roles
  remain live until explicit handoff retirement. The route also records the wrapper-owned
  cheap-first and content-addressed retry contract.

- 2026-08-10T04:39+02:00 — 260713-TES-L6: refreshed lifecycle routing and liveness hot paths for
  sprint command seats and all subordinate roles. Verification metadata remains pinned until
  closeout.

- 2026-08-09T12:08+02:00 — 260713-TES-L5 route impact: recorded the judgment-demolition
  doctrine (fact-relay supervision, ladder retired, mailbox custody, attribution-only
  consume, code-seam wording) across the canonical lifecycle tree and its synced mirrors.
  Verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-08T21:20+02:00 — 260713-TES-L1 route impact: the canonical `skills/l-01-agent-lifecycles`
  tree and its nine synced copies were refreshed from supervisor to agent-notifier wording
  (role files, templates, criteria, SKILL.md); route shape unchanged. Verification metadata
  pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 route impact: recorded the quality altitude ladder in
  the lifecycle doctrine (targeted leaf checks, once-per-master full gate, per-leaf memory
  quality). Verification metadata stays pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-05T22:30+02:00 — 260731-EFA-L16 route impact: recorded the spawn doctrine (role seats only via `spawn_agent_session`; no native sub-agents on orchestration seats; architect-solo exception) and the guideline-adherence chain (worker Orient/brief read, reviewer lens, c-12 Preconditions + Boundaries rule 10), plus the architect's generic `system/tools.md` inventory read. Verification metadata pinned until closeout stamps the code commit.
- 2026-08-05T03:47+02:00 — 260731-EFA-L6 route impact: recorded the curator self-check doctrine
  (`contract_path`-scoped `route_index_refresh`/`memory_quality_check`/`drift_check`), RV-5's
  promotion to a standing criterion, and the controller → application-entry-point language in
  `criteria/code-seam.md`. Verification metadata pinned until closeout stamps the code commit.
- 2026-07-15T23:31+02:00 — 260714-ACPUI-L2 closeout-preview delta: documented complete
  settings-owned role selections, dynamic model-local validation, native Claude/Codex/Pi initial
  configuration, provenance-only spawn env, and the no-composer/no-default-substitution boundary.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator: established governing route coverage for the final candidate.
