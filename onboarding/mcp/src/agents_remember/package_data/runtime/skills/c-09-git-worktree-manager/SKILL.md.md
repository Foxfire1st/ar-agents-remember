# c-09-git-worktree-manager/SKILL.md

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-07-06T17:35+02:00                     |
| lastVerifiedCommitHash | `e400ed0ce98752d1b65d00de97c9b84c7ea20814` |
| lastVerifiedCommitDate | 2026-07-10T20:04:45+02:00|

## Purpose

This skill documents `c-09-git-worktree-manager` skill, the Git worktree lifecycle manager for Agents
Remember tasks. `c-09-git-worktree-manager` skill now owns worktree start, attach/status, external-memory
compatibility before worktree start, integration, lifecycle finalization, and cleanup. Since L11 it also documents reopening: `task_reopen` resets a fully landed leaf back
to planning under its exact leaf id, and a normal `worktree_start` then recreates the
worktrees. HFX2-L6 changes the approval wording to applicable authority: standalone/new/final work
still stops for developer approval, while subordinate accepted-series work can record standing
series authority and continue through worktree start, integration, and finalize/cleanup after clean
previews. Closeout
sequencing belongs to `c-12-closeout` skill; `c-09-git-worktree-manager` skill only supplies the worktree-specific
`contract.md` path and the integration/finalization follow-up rules. Slice 2c adds a
Lifecycle Resume And Promotion section: `worktree_start` promotes the current
fleeting lifecycle to persistent (the contract `lifecycle:` anchor),
`worktree_attach` resumes it, and attaching over an unsaved fleeting lifecycle
hits the save gate (`on_unsaved=save`|`discard`).

## Code Commentary

### Logic

Since L10 the skill's intake no longer offers a chat build: it wraps the light-task or external workflow only, and single-session work rides a THIN w-02 doc (the l-01 'chat is never a build route' invariant swept into the intro and intake step 4). The skill defines the worktree MCP entrypoints for start, attach, status,
mid-task sync, worktree closeout tool handoff, integration, and cleanup. Since
the GitHub #54 series it documents the stale-base preflight (start blocks when
a source branch is behind/diverged from its upstream, with
`stale_base_choice="fast-forward"`/`"proceed-stale"` recoveries), the
auto-created external-memory source branch (official-tip base, code branch
name as template, reported as `memorySourceBranch`), the fetch-free
`worktree_status` freshness block with its `syncHint`, and the new **Mid-Task
Sync** section: `worktree_sync` pulls a moved official line into the live
worktree atomically (new code tip must be ledger-mapped at the official memory
tip; sync early — before memories are written — for the pure fast-forward
path; `memory_sync_choice` recoveries when local memory commits diverge). It states that `c-09-git-worktree-manager` skill
begins after the normal intake and onboarding gate, uses context resolved by the `c-08-ar-coordination-context-resolver` skill
through the MCP worktree tools, refuses external-memory worktree start while
the source memory repo has uncommitted content or ledger changes, and reports
recoverable lifecycle state through typed next-operation hints. 260707-HFX2-L6 broadens the
approval wording from all-human per-junction approval to **applicable authority**: standalone or
new work still uses the developer Worktree Intent Gate, but subordinate leaves/edges inside an
accepted orchestrated series record accepted-series authority and continue without a new developer
stop. The same authority distinction now governs integration and lifecycle finalization/cleanup:
accepted-series leaf→master and master→super edges may proceed after clean dry-runs under standing
series authority, while final super→main cleanup, standalone work, and deliberately raised
human-pinned gates still stop for the developer. It now also
requires agents to identify the branch that `worktree_integrate` would move
before `worktree_start`; when that branch is protected, PR-gated, or otherwise
not directly landable, agents must first create or check out a pushable
integration branch and use that branch as the worktree `source_branch`. Before
calling `worktree_start`, agents must present a Worktree Intent Gate for
developer approval; the packet names the repo, build mode, branch policy,
source branch, work branch/worktree name, memory mode, landing path, and risks.

The worktree closeout section is deliberately a routing section, not a parallel
closeout doctrine. It sends the approval gate, missing-onboarding check, code
commit, onboarding/entity refresh, memory quality gate, memory content commit,
ledger update, and ledger commit to `c-12-closeout` skill. For worktree-backed tasks, `c-09-git-worktree-manager` skill
contributes the task `contract.md` used by `worktree_closeout_preview` and
`worktree_closeout_apply`; after closeout, `c-09-git-worktree-manager` skill resumes ownership for
integration and cleanup. Since L8 cycle 6 the Integration section also names the
seam consumer: on an orchestrated master's exit (master → super), an undecided
or policy-invalid `master-handover-approval` gate addressed to the master (by
`enclosure` = master task name) makes `worktree_integrate` return
`handover-gate-blocked` instead of landing — decide the gate per the
`l-01-agent-lifecycles` seam doctrine, then rerun. Since cycle 7 the same
section also names the spelling-check warning: when no gate addresses the
integrating master but open `master-handover-approval` gates exist elsewhere,
integrate proceeds and its result carries a `handover_gate_warning` naming
them — a check on the raised gate's `enclosure` spelling.
Before previewing integration, agents must also check out the recorded code and
memory `source_branch` in the source repositories because `worktree_integrate`
requires those active checkouts even for `dry_run=true`.

Task 25 consolidates the worktree-manager junctions onto `lifecycle_gate` with
the lifecycle-wide dry-run -> report -> raise order. At the **Worktree Intent
Gate** the skill runs the applicable dry-run/preflight first, reports the intent
packet in chat, then raises one durable lifecycle gate carrying the
`worktree-intent` junction kind, developer-facing ask, and intent packet; the
single call also blocks the lifecycle and waits for the developer decision or
matching inbox response. Integration runs
`worktree_integrate(..., dry_run=true)` before reporting the preview in chat and
then uses `lifecycle_gate(kind="integration-approval", ask=..., packet=...)`.
Cleanup/finalization runs `lifecycle_finalize_task(..., dry_run=true)` before
reporting the cleanup plan in chat and then uses
`lifecycle_gate(kind="cleanup-approval", ask=..., packet=...)`. After a
developer response reaches the agent it clears the ambient block with
`lifecycle_resume` before running the gated mutation.

The developer resolves every one of these — an agent's own model-attributed
`gate_decide` never counts as approval, and a chat "approved" does not propagate
itself, so the agent always owns the `lifecycle_resume` clear.

Task 28 reframes these three worktree hand-offs (worktree-intent,
integration-approval, cleanup-approval) from the block-and-wait `lifecycle_gate`
to **notify-and-continue**, in the order **dry-run → notify (last tool call) →
report (last prose) → stop**: the agent runs the applicable dry-run/preflight,
then calls `lifecycle_turn_end_notification(summary={…the intent / integration /
cleanup packet + the developer ask…})` as the **last tool call of the turn**, then
delivers that packet as its **final prose** and **STOPs / ends the turn**. That tool
sets the new `awaiting-developer` lifecycle state, surfaces a dashboard attention
item, and returns immediately — no wait, no operator inbox, and because it does not
render a prompt over the prose the report stays the last thing the developer reads;
the developer
responds and the **first AR tool call of the next turn** auto-resumes
(`running`) and auto-dismisses the item, so the agent issues no explicit
`lifecycle_resume`. The block-and-wait `lifecycle_gate` (+ `lifecycle_resume`)
and the operator inbox are parked as the fallback for a deliberate durable,
developer-attributed, mutation-blocking approval record (on that parked path the
report still precedes the gate raise, since the durable gate renders a prompt over
the prose); the Task 25 /
`gate_decide` / `lifecycle_resume` descriptions above are superseded historical
context. This packaged file is a sync-propagated (`scripts/sync-skills.py`)
bundle copy of the canonical `skills/c-09-git-worktree-manager/SKILL.md`.

Dashboard task 14 adds `lifecycle_finalize_task` as the terminal worktree
lifecycle tool. The skill now instructs agents to preview it, relay the landed
commit proof, cleanup plan, and task-document updates, raise the
`cleanup-approval` gate, then run the real finalizer after developer approval.
The tool proves exactly one parent-child branch edge by checking that the landed
commit is reachable from the recorded local source branch, runs or verifies
cleanup, and updates the leaf task plus immediate parent row to `Completed` when
task-doc paths are supplied. PR-gated edges are structurally identical after the
PR merge has been pulled locally. Squash-merge equivalence is intentionally out
of the default path because it erases commit lineage and can invalidate memory
lookup history.

### Conventions

`c-09-git-worktree-manager` skill is a wrapper, not a replacement workflow. Task identity should be settled
before worktree creation: `w-02-light-task-workflow` skill creates `<task-root>/<task-slug>/task.md`, then
`c-09-git-worktree-manager` skill places `contract.md` beside it. External memory incompatibility is
interactive and offers reconciliation, disabled memory, or custom handling; its
common trigger is starting off a freshly-merged gated branch whose PR merge
commit the ledger has not mapped, which `c-11-memory-carryover-from-branch` skill carryover (run after the merge) now
maps automatically so `reconciliation` is not needed. Dirty source memory blocks
start until memory content and ledger updates are committed or the developer
chooses another path.

Integration remains human-gated, with the 260703-L12 round-2 orchestrated-run
carve-out stated in the section itself: dependency-ordered leaf→master and
master→super integrations ride the series' standing approval (the developer's
portfolio-gate approval recorded in the planner master), concentrating the
developer hand-off at the super PR/carry-over gate; a raised durable
`integration-approval` gate still awaits the developer. `ff-only` lands closed
task branches when source branches did not move; `replay` handles parallel non-overlapping work by
replaying code and memory content, then regenerating the final memory ledger
row. The recorded `source_branch` is the integration target, not just a base
branch: `worktree_integrate` will move it and will not open a PR or discover
protected-branch policy on its own. For PR-gated repositories, the approved
intent packet must make clear that the protected target is not the recorded
`source_branch`; the source branch is the pushable branch that will later be
pushed for PR. Integration preview also expects the recorded code and memory
source branches to be the active checkouts in the source repositories, so agents
should switch clean source checkouts before calling `worktree_integrate` with
`dry_run=true`. Lifecycle finalization remains human-gated and removes
worktrees plus merged local task branches only after integration, carryover, and
landed-commit proof.

### Invariants And Boundaries

`c-09-git-worktree-manager` skill must not use divergent memory as trusted context, must not bypass `c-12-closeout` skill's
explicit closeout approval gate, and must not create closeout commits outside
`c-12-closeout` skill's code-memory-ledger sequence. Worktree status reports lifecycle phase,
dirty flags, summary, and typed next hints instead of shell commands.
Integration must not move source branches until code and memory commits are
fast-forwardable or replay has produced mediated commits. The skill must not
call `worktree_start` until the developer has approved the Worktree Intent Gate.
For protected, PR-gated, or otherwise not-directly-landable target branches, the
selected `source_branch` must be a developer-approved pushable integration
branch created from that target, not the protected target itself. Lifecycle
finalization requires completed closeout, completed integration, completed
memory carryover, landed-commit ancestry on the recorded source branch, and
explicit cleanup/finalization approval.

### Todos

No current implementation todo is recorded for the skill contract.

### Docs References

No external documentation is needed for this repository-local skill.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `c-09-git-worktree-manager` skill owns worktree lifecycle and routes closeout to `c-12-closeout` skill. | L8-L13; L103-L115; L140-L152 | [`c-09-git-worktree-manager` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |
| `c-12-closeout` skill owns the shared closeout approval and code-memory-ledger sequence for direct and worktree closeout. | L8-L29; L33-L82 | [`c-12-closeout` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md) |
| The source-branch contract says protected, PR-gated, or otherwise not-directly-landable targets need a pushable integration branch before `worktree_start`, because integration lands into the recorded `source_branch`. | L49-L59; L72-L87; L121-L128 | [`c-09-git-worktree-manager` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |
| The Worktree Intent Gate must be explicitly approved before `worktree_start` and must name branch policy, source/work branches, memory mode, landing path, and risks. | L80-L94 | [`c-09-git-worktree-manager` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |
| The Worktree Intent Gate runs the applicable dry-run/preflight first, reports in chat, then uses one `lifecycle_gate(kind="worktree-intent", ask=..., packet=...)` call; `worktree_start` runs only after a developer-resolved decision is cleared with `lifecycle_resume`. | L99-L114 | [`c-09-git-worktree-manager` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |
| Integration and cleanup/finalization run their dry-runs first, report previews in chat, then use `lifecycle_gate(kind="integration-approval", ...)` / `lifecycle_gate(kind="cleanup-approval", ...)` before `worktree_integrate` / `lifecycle_finalize_task`, with `lifecycle_resume` after the developer response is handled. | L193-L199; L220-L225 | [`c-09-git-worktree-manager` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |
| Integration preview requires the recorded code and memory `source_branch` to be checked out in the source repositories, even for `dry_run=true`. | L117-L125 | [`c-09-git-worktree-manager` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |
| Integration remains owned by the `c-09-git-worktree-manager` skill and covers fast-forward and replay strategies after closeout. | L117-L134 | [`c-09-git-worktree-manager` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |
| Lifecycle finalization remains owned by the `c-09-git-worktree-manager` skill and requires completed integration, carryover, landed-commit proof, and cleanup/finalization approval. | L213-L242 | [`c-09-git-worktree-manager` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Series-Contract Notes

The packaged worktree-manager skill defines the new operating model: master tasks own an integration branch via root `series-contract.md`, and each active leaf owns a distinct enclosure contract/worktree under `enclosures/<leaf-id>/`.

## Update History

- 2026-07-08T15:27+02:00 — 260707-HFX2-L6 (delegated worktree lifecycle
  authority): frontmatter and worktree-intent/integration/finalization sections now distinguish
  standalone/new/final developer-gated work from subordinate accepted-series work. For accepted
  orchestrated series edges, agents record the planner/series authority and continue after clean
  dry-runs instead of stopping for every worktree start, closeout-adjacent edge, integration, or
  cleanup/finalize command. Final super→main cleanup, standalone work, and raised human-pinned
  gates remain developer stops. Sync-propagated bundle copy of the canonical
  `skills/c-09-git-worktree-manager/SKILL.md`; no Python worktree behavior changed. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L6 commit.

- 2026-07-06T17:35+02:00 — 260703-L12 round 2 (L12R-6): the Integration section gains the orchestrated-run standing-approval carve-out sentence (ruled 2026-07-06, resolves L8-Q9's practiced path) — the developer hand-off concentrates at the super PR/carry-over gate; a raised durable integration-approval gate still awaits the developer. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T12:30+02:00 — L10 owner ruling (builder escalation #1): the chat-build option is swept from the intro and intake decision — chat never builds; single-session work takes a thin w-02 doc. Verification metadata pinned until closeout stamps the L10 commit.

- 2026-07-05T19:55+02:00 — L8 builder cycle 7: Integration section adds one sentence — integrate reports unmatched open handover gates as the `handover_gate_warning` enclosure spelling check (AR4-1c). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:25+02:00 — L8 cycle 6 (owner follow-up to builder escalation #1 / AR3-1): the Integration section now names the `handover-gate-blocked` state — the delegated `master-handover-approval` seam enforced at master → super integrate, addressed by `enclosure` = master task name. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-03T00:30+02:00 — L11 documents the task_reopen flow (reopen a completed leaf in place; never mint a suffixed leaf id).
- 2026-06-27T22:00+02:00 — Order fix (notify-then-report): corrected the Task 28
  notify-and-continue hand-off ORDER for all three worktree hand-offs (worktree
  intent, integration, cleanup/finalization) to **dry-run → notify
  (`lifecycle_turn_end_notification`, the last tool call) → report (the last prose)
  → stop**. The earlier notify-and-continue pass (entry below) had described
  report-before-notify; the corrected order ends the turn on the prose report
  (the notification returns immediately and does not render a prompt over the
  prose). Parked block-and-wait `lifecycle_gate` fallback unchanged (report still
  precedes the durable gate raise there). Sync-propagated (`scripts/sync-skills.py`)
  bundle copy of the canonical `skills/c-09-git-worktree-manager/SKILL.md`.
  Verification metadata pinned.
- 2026-06-27T22:00+02:00 — Task 28 (notify-and-continue reframe): the three
  worktree hand-offs (worktree intent, integration, cleanup/finalization) now
  notify-and-continue through the new `lifecycle_turn_end_notification` tool —
  dry-run, chat report, then `lifecycle_turn_end_notification(summary=…)` + STOP,
  which sets the new `awaiting-developer` state, surfaces a dashboard attention
  item, and returns immediately; the next turn's first AR tool call auto-resumes
  (`running`) and auto-dismisses the item (no `lifecycle_resume`). Block-and-wait
  `lifecycle_gate` / operator inbox parked as the fallback. Sync-propagated
  (`scripts/sync-skills.py`) bundle copy of the canonical
  `skills/c-09-git-worktree-manager/SKILL.md`; the older block-and-wait
  `lifecycle_gate` body above is superseded historical context. Verification
  metadata pinned until closeout stamps the task-28 code commit.
- 2026-06-26T18:58+02:00 — No content impact: reviewed the source commit's
  generated skill-copy sync; the existing body already describes the current
  dry-run -> chat report -> `lifecycle_gate` order for worktree intent,
  integration, and cleanup/finalization.
- 2026-06-26T17:21+02:00 — Task 25 regression fix: current worktree intent,
  integration, and cleanup/finalization guidance now follows dry-run/preflight
  first, chat report second, and `lifecycle_gate` third; older report/action
  descriptions below are superseded historical context.
- 2026-06-26T17:12+02:00 — Regression fix: current worktree intent,
  integration, and cleanup/finalization guidance now describes `lifecycle_gate`
  as the single call that creates the durable gate, blocks the lifecycle, and
  waits for the developer decision or matching inbox response.
- 2026-06-26T14:27+02:00 — Task 25: updated current worktree intent, integration, and cleanup/finalization guidance to use `lifecycle_gate` as the single lifecycle-gate junction call that creates the durable gate, blocks the lifecycle with the ask, and waits for the developer response. Older split-call history entries below are superseded historical context. Verification metadata pinned until closeout stamps the task-25 code commit.
- 2026-06-25T13:20+02:00 — Task 23/24: worktree gate examples now rely on one normal five-minute `gate_response_wait` call instead of caller-managed timeout loops.
- 2026-06-25T07:17+02:00 — Task 19: worktree intent, integration, and cleanup/finalization gate examples now use `gate_response_wait` and tell agents to consume returned inbox entries after reading them. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: packaged worktree-manager doctrine now states the single-schema commitment: master tasks own root integration `series-contract.md`, leaf worktrees own `enclosures/<leaf-id>/series-contract.md`, and `contract.md` is retired. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00 — Dashboard task 14: documented `lifecycle_finalize_task` as the terminal tool replacing standalone cleanup as the normal final step. It proves one landed parent-child edge, runs or verifies cleanup, updates the leaf and immediate parent row to `Completed`, treats PR-gated edges as normal local ancestry after merge/pull, and excludes squash equivalence from the default path. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-23T07:39+02:00 — Slice 09: documented the mirror's adoption of the `l-01-session-job-lifecycle` skill's Gate Choreography at the three junctions this skill owns — the **Worktree Intent Gate** now raises `lifecycle_block(kind="decision")` + `gate_create(kind="worktree-intent")`, `gate_wait`s, and clears with `lifecycle_resume` before `worktree_start`; **integration** raises `gate_create(kind="integration-approval")` and **cleanup** raises `gate_create(kind="cleanup-approval")`, each raise → wait → developer-resolve → clear (an agent's own `gate_decide` never counts). Raised on top of the two-turn chat protocol, not instead of it. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-13T18:45+02:00 — Slice 2c: documented the Lifecycle Resume And Promotion section (start=promote the current fleeting lifecycle to persistent + contract `lifecycle:` anchor; attach=resume; save gate on leaving an unsaved fleeting via `on_unsaved`). Verification metadata pinned until closeout stamps the 2c code commit.
- 2026-06-10T10:26+02:00 — GitHub #54: documented the stale-base preflight + `stale_base_choice` recoveries, the auto-created memory source branch, the `worktree_status` freshness block, `worktree_sync` in the MCP tools list, and the new Mid-Task Sync section (sync-early-before-memories doctrine).
- 2026-06-04T16:03+02:00: Added the integration-preview reminder that agents must check out the recorded code and memory `source_branch` in the source repositories before calling `worktree_integrate`, including `dry_run=true`.
- 2026-06-04T15:45+02:00: Added the Worktree Intent Gate: agents must present branch policy, pushable source branch, work branch/worktree name, memory mode, landing path, and risks for developer approval before `worktree_start`; PR-gated flows must show that the recorded `source_branch` is the pushable integration branch, not the protected target.
- 2026-06-03T04:06+02:00: Clarified the source-branch contract for protected or PR-gated targets: before `worktree_start`, choose a pushable integration branch as `source_branch`, because `worktree_integrate` lands into the recorded source branch and does not open PRs or infer branch protection.
- 2026-06-02T04:25+02:00: Dropped the retired heavy-task workflow from the wrapped-workflow list and the intake decision step (now chat, `w-02-light-task-workflow` skill light task, or master + light sub-task series). `l-01-session-job-lifecycle` skill series, Sub-task B/S6, mcp 1.1.0.
- 2026-06-02T04:00+02:00: Added a Start/Attach/Status note that the external-memory "no compatible state" prompt's common trigger is a freshly-merged gated branch whose PR merge commit is unmapped, and that `c-11-memory-carryover-from-branch` skill carryover now maps it automatically after the merge (so `reconciliation` is usually unnecessary). `l-01-session-job-lifecycle` skill series, Sub-task C, mcp 1.1.0.
- 2026-05-29T20:25+02:00: Reviewed for the act-by-default `dry_run` flip — the `c-09-git-worktree-manager` skill worktree examples now omit `dry_run=false` and carry a preview-first note (`dry_run=true` then the real run).
- 2026-05-26T16:25+02:00: Updated after closeout guidance moved to `c-12-closeout` skill and `c-09-git-worktree-manager` skill became worktree lifecycle plus integration/cleanup only.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-24T05:03+02:00: Updated after `c-09-git-worktree-manager` skill worktree status guidance switched from next safe commands to typed `nextOperation`/`nextTool`/`nextArgs` hints.
- 2026-05-24T04:34+02:00: Updated after closeout guidance routed post-code-commit drift through `c-02-memory-quality-control` skill memory quality control.
- 2026-05-24T03:24+02:00: Updated after `c-09-git-worktree-manager` skill closeout adopted the pre-code-commit `check_missing_onboarding` pass for newly added files.
- 2026-05-24T02:47+02:00: Updated closeout guidance to run drift after the code commit, refresh memory, run `memory_quality_check`, then commit memory and ledger.
- 2026-05-16T18:17+02:00: Documented that external-memory closeout refreshes affected repo entity catalog fingerprints after the code commit and before the memory-content commit.
- 2026-05-12T10:59: Updated the direct-closeout contract after ledger branch metadata stopped being a compatibility condition.
- 2026-05-11T19:42: Refreshed verification metadata to `aa85d3862bf21fed791e3170e6957f9288c319e8` and corrected `c-09-git-worktree-manager` skill source citation ranges after confirming the coordination rename behavior remains current.
- 2026-05-11T18:34: Updated after `c-09-git-worktree-manager` skill command examples adopted `--code-repository-name` and `--code-repository-root`.
- 2026-05-10T03:01: Updated after the `c-09-git-worktree-manager` skill contract added direct checkout closeout for approved micro edits.
- 2026-05-10T01:55: Updated after the closeout contract documented code-commit-first onboarding metadata refresh before memory commit.
- 2026-05-10T01:19: Updated after `c-09-git-worktree-manager` skill split implementation approval from explicit commit approval and added closeout preview guidance.
- 2026-05-10T00:56: Updated to capture the clean external-memory baseline gate before `c-09-git-worktree-manager` skill worktree start.
- 2026-05-10T00:47: Updated for pre-worktree intake, wrapper task placement, lifecycle status, and cleanup command behavior.
- 2026-05-10T00:36: Refreshed verification metadata after approval-gated integration landed on main.
- 2026-05-09T23:55: Updated after documenting the `c-09-git-worktree-manager` skill integration phase and replay/conflict rules.
- 2026-05-09T22:57: Refreshed verification metadata and replaced task-artifact citations with current skill/spec evidence.
- 2026-05-09T22:10: Updated closeout boundary to include source-branch movement checks.
- 2026-05-09T21:59: Created onboarding for the new `c-09-git-worktree-manager` skill.
