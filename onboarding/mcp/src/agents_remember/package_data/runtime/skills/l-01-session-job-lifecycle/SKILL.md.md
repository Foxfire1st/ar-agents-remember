# l-01-session-job-lifecycle/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-27T22:00+02:00                      |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|

## Purpose

This file is the complete entry contract for `l-01-session-job-lifecycle` skill, the session job lifecycle the coordinator routes every session into. It now carries the full shared spine inline (request -> trust checkpoint -> reframe/research -> decide -> build -> close), the build-mode decision that is the only task-format call, research-only exits after investigation, the two remaining companion files (`job-variants.md` and `deep-research-report-template.md`), and the invariants that keep memory, developer agreement, evidence gathering, onboarding, and tests in lockstep with code. The previous `lifecycle.md` companion was consolidated into this file so agents cannot stop after `SKILL.md` and skip the phase doctrine.

## Code Commentary

### Logic

The skill frames `l-01-session-job-lifecycle` skill as a canvas rather than a task format. It now states the front half as a developer/model collaboration loop: the developer states the request, the model resolves context through `context_packet(... include_providers=true, include_drift=true)`, the model handles drift and provider readiness before trusting memory, the model gathers `c-04-retrieval-strategy-router` evidence for a `tasks/AGENTS.md` reframe, and the developer agrees or revises that reframe before deeper research. It then carries the build-mode decision (research-only exit, chat build, or durable `w-02-light-task-workflow` skill task), the relationship to the core skills it sequences (`c-04-retrieval-strategy-router` skill, `c-05-create-or-update-onboarding-files` skill, `c-08-ar-coordination-context-resolver` skill, `c-09-git-worktree-manager` skill, `c-11-memory-carryover-from-branch` skill), and the invariants that protect the collaboration and build gates.

The former `lifecycle.md` phase detail is now inline. `request` receives the developer's raw request and identifies the target repository; the trust checkpoint reveals whether the request is inside Agents Remember managed-repo scope and requires lifecycle re-entry if later work crosses that boundary. `trust checkpoint` runs `context_packet(repo_id="<repo-id>", include_providers=true, include_drift=true, include_freshness=true)`, reports repo/memory/provider/drift facts — including any `indexing` busy targets from the providers summary, which the agent relays to the developer as healthy-but-mid-scan (results may be partial until the scan completes), plus branch freshness (GitHub #54: behind/diverged code or memory checkouts mean the local official line is stale and should be fast-forwarded before trusting analysis; `ledgerMapsCodeHead=false` means the memory checkout does not match the code state) — asks about clean-source onboarding drift, treats dirty-source drift as active work-in-progress, and recovers degraded providers before relying on them. `reframe and research` gathers `c-04-retrieval-strategy-router` evidence for a `tasks/AGENTS.md` reframe, gets developer agreement or revision, then performs proof-bearing deeper research. `decide` is the single build-mode branch: research-only exit, or a worktree build that first presents the worktree intent packet and waits for developer approval before `worktree_start`. `build` implements in the worktree with live per-section onboarding and green checks before each commit, watching `worktree_status`'s freshness block and syncing a moved official line in early via `worktree_sync` (GitHub #54: before memories are written, the sync is a pure fast-forward and integration stays ff-only). `close` previews the `c-09-git-worktree-manager` skill closeout (worktree-only — the close step no longer offers a `direct_closeout_preview` alternative, issue #62), stops at the commit gate, runs the external-memory invariant, integrates the worktree branch into the approved source/integration branch before PR-gated landing, maps the ledger to the landed commit, then uses `lifecycle_finalize_task` to prove one parent-child branch edge, reclaim the worktree/provider stack, and mark the leaf task plus immediate parent row `Completed` when task-doc paths are supplied. PR-gated edges are structurally identical after the model finishes the PR merge and pulls the target branch locally; squash equivalence is not a default proof.

The per-job lenses live in `job-variants.md`; the reusable deep research report and evidence-ledger shape lives in `deep-research-report-template.md`.

The skill also carries the **parked** block-and-wait gate protocol (the active
hand-off is the notify-and-continue order below — dry-run → notify → report-last);
on that parked path a raised `lifecycle_gate` runs the
applicable dry-run action first, delivers the complete gate report as plain chat
output second, then raises `lifecycle_gate` third before the turn ends, because the
durable gate renders a prompt over the prose. The
report action ends with the approval question in prose and must not contain a
structured question widget, a mutating apply call, or a permission-triggering
operation, because harnesses render approval prompts over or instead of
same-turn prose and the developer never sees a report attached to its own
approval prompt. The `lifecycle_gate` raise creates the durable gate, blocks the
lifecycle with the ask, and waits for the developer decision or matching inbox
response before returning; after the response is handled, the agent clears the
block with `lifecycle_resume`.

Slice 2c adds a **Lifecycle Signals** section mapping lifecycle signals to the
phases: `lifecycle_start` at the trust checkpoint, `lifecycle_phase` per phase,
`lifecycle_gate` followed by `lifecycle_resume` at gates, `worktree_start`
promoting fleeting→persistent, `worktree_attach` resuming, `switch_lifecycle`
with `on_unsaved` for the save gate, and `lifecycle_end` at close — with the
rules that the model never handles ids, `paused` is system-owned, and a
lifecycle-less call is dropped.

Slice 07 (S5 sync) re-synced this generated `l-01` mirror to carry the
`read_ar_files` **research-phase read** doctrine: a "read tool for this phase"
rule states that until the build-mode decision (Phase 3), managed-repo source is
read through the `read_ar_files` MCP tool, not the harness's native read — one
observable, lifecycle-attributed call returns paired source+onboarding plus the
repository/route overviews — with native read reserved as the edit precondition in
Phase 4; the deeper-research evidence ledger lists the running `read_ar_files`
call count alongside onboarding docs, semantic queries, and code-graph queries.
(The authored skill source owns the wording; this is the synced runtime mirror.)

Slice 6b adds a server-side gate-enforcement pointer to the `close` commit gate
(§5): when the lifecycle is dashboard-connected, the commit gate is **also**
enforced server-side via a durable developer-attributed `closeout-approval` gate
that `worktree_closeout_apply` binds on — an agent self-approval never satisfies
it. Task 25 replaces the earlier split public choreography with **one** public
gate junction after the dry-run and report actions: the agent calls
`lifecycle_gate(kind=<junction>, ask=..., packet=...)`. That call creates the
durable gate, blocks the lifecycle with the same ask, and waits for the
developer decision or matching inbox response.
Durable gate `kind` names the
dashboard junction (`plan-approval`, `worktree-intent`, `closeout-approval`,
`push-approval`, `integration-approval`, `cleanup-approval`, or `agent-question`);
`ask.kind` names the answer shape (`decision`, `question`, or `conflict`) with
its prompt/options. The skill no longer teaches a separate create/block/wait
sequence or a report-then-wait-for-reply turn before the gate raise.
`closeout-approval` **is** the commit gate —
closeout is the single commit-of-record for code, memory, and ledger, so there
is no separate `commit-approval`. The choreography is opt-in and additive (most
valuable under a dashboard); a gateless chat session keeps the dry-run/report
discipline while skipping the durable dashboard gate.

Task 28 reframes the whole developer hand-off protocol from the block-and-wait
`lifecycle_gate` to **notify-and-continue**, the new default for every junction
(reframe agreement, plan gate, worktree intent, commit/closeout, push,
integration, cleanup/finalization, and regular turn-end). The hand-off is **three
actions, never one**, in the order **dry-run → notify → report-last**: a dry-run
action, then a notify-and-stop action that calls the new
`lifecycle_turn_end_notification(summary=…)` tool as the **last tool call of the
turn**, then a plain-chat report action delivered as the **final prose** whose last
line is the developer-facing decision — then the turn ends. That tool
sets the new `awaiting-developer` lifecycle state, surfaces a dashboard attention
item, and returns immediately — no wait, no operator inbox, and because it does not
render a prompt over the prose the report stays the last thing the developer reads; the developer responds
on the dashboard or the leaf's attached chat and the **first AR tool call of the
next turn** auto-resumes the lifecycle (`running`) and auto-dismisses the item, so
the agent sends no explicit `lifecycle_resume`. `next_step.py` repoints every gate
moment to `lifecycle_turn_end_notification`; the named junction `kind` is kept only
as the **parked** durable-gate label. The block-and-wait `lifecycle_gate` (+
`lifecycle_resume`), the operator inbox, and the dashboard GateResponder still
exist but are no longer the active path — reach for them only for a deliberate
durable, developer-attributed, mutation-blocking approval record (on that parked
path the report still precedes the gate raise, since the durable gate renders a
prompt over the prose). The Task 25 /
Gate Choreography / `lifecycle_resume` descriptions above are superseded historical
context. This packaged file is a sync-propagated (`scripts/sync-skills.py`) bundle
copy of the canonical `skills/l-01-session-job-lifecycle/SKILL.md`.

### Conventions

The frontmatter `name` is lowercase (`l-01-session-job-lifecycle`) so the flat-layout installer accepts it (`[a-z0-9][a-z0-9-]*`), and the skill directory uses the same lowercase ID. The skill remains multi-file like the `w-02-light-task-workflow` skill, but its phase behavior lives in `SKILL.md` rather than in a separate lifecycle companion. It supersedes the retired chat workflow without naming it by a dead identifier.

### Invariants And Boundaries

Every session enters `l-01-session-job-lifecycle` skill; the job type is a lens, never a gate. The model must run the MCP context packet with providers and drift before trusting onboarding or provider-backed context. Clean-source drift creates a developer choice point for `c-05-create-or-update-onboarding-files`; dirty-source drift is reported as active work-in-progress. Degraded providers are recovered through MCP provider/runtime operations and rechecked. Persistent provider issues are reported to the developer before provider-backed evidence is used. The developer is the state authority for reframe agreement: the model does not proceed to deeper research while the developer disagrees. Research reports use the deep research template and still list onboarding docs, semantic queries, code graph queries, source files, and truth gaps. `build => worktree`; `durable task => worktree + task.md`; `chat build => worktree, no artifact`; `research-only => no worktree`. Before `worktree_start`, the model must present a worktree intent packet and the developer must approve or revise it. No implementation before the `frame` plan gate; implementation approval is not commit approval. Onboarding is refreshed live per completed plan-section; tools.md checks run green before each incremental commit. The agent never pushes a protected branch on its own authority. `l-01-session-job-lifecycle` skill must cover everything the retired chat workflow did plus the job lens, developer-agreed reframe, proof-bearing research, and research-only exit, with no default-path regression.

### Todos

No current todo is recorded for this lifecycle skill.

### Docs References

No external domain documentation applies to this repository-local lifecycle skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

`l-01-session-job-lifecycle` skill is the lifecycle the coordinator `AGENTS.md` routes into; it sequences the C-0x core skills and hands off to `w-02-light-task-workflow` skill for durable task builds.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The coordinator and root `AGENTS.md` route every session into `l-01-session-job-lifecycle` skill and reduce task-format choice to `l-01-session-job-lifecycle` skill's build-mode step. | n/a | [coordinator AGENTS.md](agents-remember/mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md) |
| The lifecycle phase spine now lives inline in `SKILL.md`; companion files are limited to the job lenses and deeper-research report template. | L17-L20; L49-L216 | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/SKILL.md) |
| The build-mode invariant requires a developer-approved worktree intent packet before `worktree_start`. | L147-L168 | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/SKILL.md) |
| The active hand-off protocol runs dry-run first, `lifecycle_turn_end_notification` (the last tool call) second, and the report prose last before the turn ends; the parked `lifecycle_gate` fallback keeps report-before-raise. | L28-L58 | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/SKILL.md) |
| The gate protocol and lifecycle-gate table route each approval junction through one `lifecycle_gate(kind=<junction>, ask=..., packet=...)` call that creates the gate, blocks, waits, and is followed by `lifecycle_resume` once the developer response is handled. | L53-L88 | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this lifecycle skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Series-Contract Notes

The lifecycle doctrine now treats the observable worktree unit as a leaf task, while a master series is the integration branch owner that coordinates multiple leaf enclosures.

## Update History

- 2026-06-27T22:00+02:00 — Order fix (notify-then-report): corrected the Task 28
  notify-and-continue hand-off ORDER across every junction to **dry-run → notify
  (`lifecycle_turn_end_notification`, the last tool call) → report (the last prose)
  → stop**. The earlier notify-and-continue pass (entry below) had described
  report-before-notify; the corrected order ends the turn on the prose report,
  because the notification returns immediately and does not render a prompt over
  the prose, so the report the developer reads is genuinely last. The Hand-off
  Protocol header/3-step block, the Lifecycle Signals gate row, and each phase gate
  (plan, worktree intent, commit/closeout, push, finalize) now read
  notify-then-report. Parked block-and-wait `lifecycle_gate` fallback unchanged
  (report still precedes the durable gate raise there). Sync-propagated
  (`scripts/sync-skills.py`) bundle copy of the canonical
  `skills/l-01-session-job-lifecycle/SKILL.md`. Verification metadata pinned.
- 2026-06-27T22:00+02:00 — Task 28 (notify-and-continue reframe): the whole
  developer hand-off protocol moves from block-and-wait `lifecycle_gate` to
  **notify-and-continue** — every junction (reframe, plan, worktree intent,
  commit/closeout, push, integration, cleanup, turn-end) now runs dry-run → chat
  report → `lifecycle_turn_end_notification(summary=…)` + STOP. The new tool sets
  the new `awaiting-developer` lifecycle state, surfaces a dashboard attention
  item, and returns immediately (no wait, no inbox); the next turn's first AR tool
  call auto-resumes (`running`) and auto-dismisses the item, with no explicit
  `lifecycle_resume`. `next_step.py` repoints every gate moment to the
  notification; the durable-gate `kind` is kept only as the parked label.
  Block-and-wait `lifecycle_gate` / operator inbox / GateResponder parked as the
  fallback. Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
  `skills/l-01-session-job-lifecycle/SKILL.md`; the Task 25 / Gate Choreography
  body above is superseded historical context. Verification metadata pinned until
  closeout stamps the task-28 code commit.
- 2026-06-26T18:58+02:00 — No content impact: reviewed the source commit's
  generated skill-copy sync; the existing body already captures the
  developer-authored gate order and the blocking `lifecycle_gate` behavior.
- 2026-06-26T17:21+02:00 — Task 25 regression fix: current body and references
  now mirror the developer-authored gate order: dry-run action, chat report,
  then `lifecycle_gate`; the raise blocks and waits instead of merely
  initializing wait state or deferring the gate until a later reply. Older
  split-call and report/action history entries below are superseded historical
  context.
- 2026-06-26T17:12+02:00 — Regression fix: synced lifecycle skill mirror now
  records `lifecycle_gate` as the action-turn call that creates the durable gate,
  blocks the lifecycle, and waits for the developer decision or matching inbox
  response before returning.
- 2026-06-26T14:16+02:00 — Task 25: generated lifecycle skill mirror now documents the developer-authored `lifecycle_gate` path as the single public gate junction and removes the previous split create/block/wait choreography from the sidecar body.
- 2026-06-25T13:20+02:00 — Task 23/24: Gate Choreography now teaches one normal five-minute `gate_response_wait` call, with the tool owning polling cadence.
- 2026-06-25T07:17+02:00 — Task 19: Gate Choreography now waits with `gate_response_wait`, consuming returned operator-inbox entries after reading them, so dashboard Chat responses are noticed while durable dashboard approvals/rejections still resolve through developer-attributed gate state. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: packaged lifecycle doctrine now describes worktree granularity as leaf-task based, with master series owning integration branches and leaf enclosures owning worktrees. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00 — Dashboard task 14: refreshed the close phase for `lifecycle_finalize_task`. After closeout, integration, PR merge/pull, and ledger/carryover alignment, the finalizer proves one landed parent-child edge, reclaims worktrees/providers, and marks the current task plus immediate parent row complete; squash equivalence is excluded from the normal path. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-23T07:39+02:00 — Slice 09: documented the new **Gate Choreography — Raise The Signal, Wait, Then Clear** section that the synced `l-01` mirror now teaches: at every approval junction the agent raises `lifecycle_block(kind,prompt,options)` (ambient) **and** `gate_create(kind=<junction>, packet=…)` (durable), `gate_wait`s, the developer resolves (dashboard or chat, never the agent's own model-attributed `gate_decide`), and the agent **always** clears with `lifecycle_resume`. Captured the junction→`kind` table (`plan-approval`, `worktree-intent`, `closeout-approval` = the commit gate, `push-approval`, `integration-approval`, `cleanup-approval`, `agent-question` catch-all) and the updated Lifecycle Signals gate row. Generated-mirror note; the authored skill source owns the wording. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T00:53+02:00 — Slice 07 (S5 sync): this generated `l-01` skill mirror was re-synced to carry the `read_ar_files` **research-phase read** doctrine — a "read tool for this phase" rule (read managed-repo source via `read_ar_files` until the build-mode decision; native read = the Phase 4 edit precondition) and the running `read_ar_files` call count in the deeper-research evidence ledger. Generated-mirror note only; the authored skill source owns the wording. Verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: §5 Close commit gate gained a server-side gate-enforcement pointer (a durable developer-attributed `closeout-approval` gate that `worktree_closeout_apply` binds on; agent self-approval never satisfies it; `c-12-closeout` owns the opt-in choreography; gateless lifecycles unchanged). Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-13T18:45+02:00 — Slice 2c: added the **Lifecycle Signals** section teaching the six `lifecycle_*` signals mapped to the phases (start at trust checkpoint, phase per phase, block/resume at gates, worktree_start promotes, worktree_attach resumes, switch_lifecycle save gate, end at close) plus the never-handle-ids / system-owned-paused / drop-lifecycle-less rules. Verification metadata pinned until closeout stamps the 2c code commit.
- 2026-06-12T19:47+02:00 — Added the Gate Protocol section: every lifecycle gate is two turns (report turn delivering the full gate report ending with a prose approval question, then the action turn invoking the gated tool after the developer replies); the report turn must not raise question widgets, mutating tool calls, or permission prompts, which harnesses render over same-turn prose.
- 2026-06-11T06:47+02:00 — Issue #62 worktree-only closeout: the close step offers only `worktree_closeout_preview`; the conditional `direct_closeout_preview` escape hatch ("only if the repo's git-workflow.md permits a direct-checkout build") was removed.
- 2026-06-10T10:26+02:00 — GitHub #54: trust checkpoint adds `include_freshness=true` (branch freshness + `ledgerMapsCodeHead` reporting), and the build phase gains the watch-and-sync-early doctrine (`worktree_status` freshness → `worktree_sync` before memories are written).
- 2026-06-10T06:20+02:00 — Body-quality pass: merged the `indexing` busy-target relay into the trust-checkpoint prose in Logic (documentation only).
- 2026-06-09T22:10+02:00 — Trust checkpoint step 5 now tells agents to report the providers summary's `indexing` busy targets to the developer: those providers are healthy but mid-scan, and their results may be partial until the scan completes (paired with the 2.5.0 `ProviderSummary.indexing` field).
- 2026-06-09T15:26+02:00: Consolidated the detailed lifecycle spine from the deleted `lifecycle.md` companion into `SKILL.md`, leaving only `job-variants.md` and `deep-research-report-template.md` as companion files. Updated references and preserved the phase behavior in this sidecar so agents get the complete lifecycle contract from the skill entry file. Verification metadata remains pinned until closeout refreshes it to the code commit.
- 2026-06-04T15:45+02:00: Updated the entry-contract onboarding for the new worktree intent gate: before `worktree_start`, the model must present repo/build mode, branch policy, source and work branches, memory mode, landing path, and risks for developer approval.
- 2026-06-04T14:50+02:00: Updated the entry-contract onboarding for the new deep research report template companion file and the invariant that deeper research reports use that template while preserving the lifecycle's proof categories. Verification metadata remains pinned until closeout refreshes it to the code commit.
- 2026-06-03T03:05+02:00: Updated the entry-contract onboarding for the recast front half: request, context packet with providers and drift, drift/provider choice points, developer-agreed reframe, proof-bearing deeper research, and research-only exits. Verification metadata remains pinned until closeout refreshes it to the code commit.
- 2026-06-02T03:30+02:00: Created file-level onboarding for the new L-01 session job lifecycle skill, the canvas the coordinator routes into; it supersedes the retired chat workflow (W-03) by migrating and modernizing its doctrine and adds the job lens plus the no-worktree answer exit.
