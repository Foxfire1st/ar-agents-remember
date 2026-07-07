# c-12-closeout/SKILL.md

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-07-05T01:32+02:00 |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063` |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|

## Purpose

This skill documents `c-12-closeout` skill, the shared closeout contract for approved Agents
Remember edits in repositories that use external memory.

## Code Commentary

### Logic

`c-12-closeout` skill owns closeout sequencing for worktree-backed tasks. It
uses the worktree closeout preview/apply tools against the task contract,
requires a non-mutating preview before real commits, requires explicit commit
approval with an intent note, runs the package-local missing-onboarding gate,
commits code, refreshes affected onboarding metadata, entity fingerprints, route
overview metadata, and generated route indexes, runs the full memory quality
check, commits memory content only after the quality gate is clean, prepends the
`C2 | M2` mapping to `memory.md`, and commits the ledger update.

Closeout is worktree-only: every change affecting the code repo runs through a
`c-09-git-worktree-manager` dual worktree (code + memory), and the former
direct-closeout usage block was removed (issue #62). Worktree closeout is used
when `c-09-git-worktree-manager` skill created or attached a task contract;
`c-09-git-worktree-manager` skill then owns later integration, lifecycle
finalization, cleanup, and task-document completion. Closeout does not mark the
task `Completed`; `lifecycle_finalize_task` does that after landing and
carryover are complete.

### Conventions

Closeout approval is separate from implementation approval. Agents must not
treat a previous "looks good", implementation approval, or their own judgment
as commit approval. The matching preview tool is the approval prompt surface:
it reports the proposed code, memory, and ledger commit messages before the
apply tool mutates Git. The relay follows the `l-01-agent-lifecycles`
skill hand-off protocol in the corrected order — run the preview/dry-run first,
call `lifecycle_turn_end_notification` as the **last tool call**, then report the
preview facts and proposed messages as the **final prose** ending with the
approval question. `worktree_closeout_apply`
is never invoked in the same turn as the relay; the next turn auto-resumes to run
it (the parked dashboard `lifecycle_gate` path instead raises the durable gate
after the report and is then cleared with `lifecycle_resume`), because harnesses
can hide approval-prompted reports.

The missing-onboarding check is scoped to current additions so newly added
eligible source files cannot escape the gradual onboarding adoption boundary. A
parallel content gate covers changed (already-onboarded) files: a changed source
whose existing sidecar body was not updated this task fails closeout, so
verification metadata is never advanced over stale onboarding content.

The closeout worklist covers the working tree plus the contract-recorded
committed range (issue #83): paths changed between the last verified commit and
the work branch HEAD, scoped by the recorded base so synced-in parallel work
and previously closed-out slices never re-gate. Already-onboarded artifacts
gate on every transported change regardless of author; committed-range paths
without onboarding are reported as `unonboarded` (count plus capped sample) and
never block, and the skill instructs relaying that list at the commit-approval
gate so important transported files are onboarded deliberately.
Entity fingerprints are refreshed after the code commit because
`git-blob-set-v1` resolves `HEAD:<path>` Git blobs. Route overview metadata and
generated route indexes are refreshed before `memory_quality_check` so the
quality gate sees the same memory tree that will be committed.

Task 25 consolidates the **Server-Side Gate Enforcement** section onto
`lifecycle_gate`: when the lifecycle is dashboard-connected, the agent runs the
preview/dry-run first, reports the preview facts in chat, then raises one
`closeout-approval` lifecycle gate carrying the durable junction kind,
developer-facing ask, and preview packet. That call also blocks the active
lifecycle and waits for the developer decision or matching inbox response.
`worktree_closeout_apply` refuses
unless that gate is `approved` **by the developer** — an agent self-approval
(`decidedBy="model"`) never satisfies it. The section remains explicit that
opening a gate is opt-in (a pure-chat session with no cockpit must not open one,
or it self-blocks on its own `open` gate) and that gateless lifecycles keep the
chat `intent_note` commit gate unchanged; the preview/apply `closeout_gate`
block is relayed at the commit-approval gate.

After the developer's resolution reaches the agent it **always clears** with
`lifecycle_resume()` before `worktree_closeout_apply` — the clear remains
agent-owned because a chat "approved" does not propagate itself.
The section also states plainly that **`closeout-approval` is the commit gate**:
closeout is the single commit-of-record for code, memory, and ledger, so every
commit (even a singular one) routes through this one gate and there is no separate
`commit-approval` kind. The push junction in External-Memory Order is likewise the
`push-approval` gate kind through `lifecycle_gate`, followed by `lifecycle_resume`
before any push once the developer response is handled.

Task 28 reframes the closeout commit hand-off (and the push hand-off) from the
block-and-wait `lifecycle_gate` to **notify-and-continue**, in the order **dry-run
→ notify (last tool call) → report (last prose) → stop**: after the preview/dry-run
the agent calls
`lifecycle_turn_end_notification(summary={…the preview facts + the commit ask…})`
as the **last tool call of the turn**, then delivers the preview facts, quality
results, and proposed commit messages as its **final prose** (ending on the commit
ask) and **STOPs / ends the turn**. That tool sets the new `awaiting-developer`
lifecycle state, surfaces a dashboard attention item, and returns immediately —
no wait, no operator inbox, and because it does not render a prompt over the prose
the report stays the last thing the developer reads; the developer approves and the **first AR tool call
of the next turn** auto-resumes (`running`) and auto-dismisses the item, after
which the agent runs `worktree_closeout_apply` (then any push) with no explicit
`lifecycle_resume`. The server-enforced block-and-wait
`closeout-approval` / `push-approval` `lifecycle_gate` and the operator inbox are
parked as the fallback for a deliberate durable, developer-attributed,
mutation-blocking record (on that parked path the report still precedes the gate
raise, since the durable gate renders a prompt over the prose); the Task 25 Server-Side Gate Enforcement /
`lifecycle_resume` descriptions above are superseded historical context. This
packaged file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the
canonical `skills/c-12-closeout/SKILL.md`.

### Invariants And Boundaries

`c-12-closeout` skill must not commit without explicit approval after a preview, must not create
a memory content commit whose affected onboarding metadata still points at
pre-closeout code, must not commit memory before route overview metadata,
generated route indexes, and `memory_quality_check` are clean for the new code
commit, must not advance verification metadata for a changed source file whose
sidecar content was not updated in the task, and must not push automatically. It does not create worktrees, integrate
worktrees, finalize lifecycles, clean up worktrees, or initialize memory roots.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `c-12-closeout` skill defines worktree closeout tool usage and centralizes the closeout sequence. | L11-L31; L70-L96 | [`c-12-closeout` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md) |
| `c-12-closeout` skill keeps commit approval separate from implementation approval and requires preview before apply. | L31-L47 | [`c-12-closeout` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md) |
| Server-Side Gate Enforcement: run preview/dry-run first, report in chat, raise one `lifecycle_gate(kind="closeout-approval", ask=..., packet=...)`, then `lifecycle_resume` before apply once the developer response is handled; the developer-attributed gate is the security boundary and `closeout-approval` IS the commit gate. | L43-L87 | [`c-12-closeout` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md) |
| `c-12-closeout` skill uses the missing-onboarding gate before code commit and routes missing sidecars to `c-05-create-or-update-onboarding-files` skill. | L50-L59 | [`c-12-closeout` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md) |
| `c-09-git-worktree-manager` skill routes worktree closeout to `c-12-closeout` skill and retains worktree lifecycle, integration, and cleanup ownership. | L8-L14; L63-L74 | [`c-09-git-worktree-manager` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |
| Closeout delegates task completion to `lifecycle_finalize_task` after closeout, integration, PR merge/pull, and carryover. | L180-L184 | [`c-12-closeout` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Series-Contract Notes

Closeout instructions now target the leaf enclosure `series-contract.md`; the root series contract is integration-branch state and is not the path used for leaf code/memory closeout.

## Update History

- 2026-07-05T01:32+02:00 - L9 lifecycle convergence: the relay reference now names the l-01-agent-lifecycles orchestrator hand-off protocol. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-27T22:00+02:00 — Order fix (notify-then-report): corrected the Task 28
  notify-and-continue hand-off ORDER for the closeout commit and push hand-offs to
  **dry-run → notify (`lifecycle_turn_end_notification`, the last tool call) →
  report (the last prose) → stop**. The earlier notify-and-continue pass (entry
  below) had described report-before-notify; the corrected order ends the turn on
  the prose report (the notification returns immediately and does not render a
  prompt over the prose, so the report stays last). Parked block-and-wait
  `closeout-approval` / `push-approval` `lifecycle_gate` fallback unchanged (report
  still precedes the durable gate raise there). Sync-propagated
  (`scripts/sync-skills.py`) bundle copy of the canonical
  `skills/c-12-closeout/SKILL.md`. Verification metadata pinned.
- 2026-06-27T22:00+02:00 — Task 28 (notify-and-continue reframe): the closeout
  commit hand-off (and the push hand-off) now notify-and-continue through the new
  `lifecycle_turn_end_notification` tool — preview/dry-run, chat report, then
  `lifecycle_turn_end_notification(summary=…)` + STOP, which sets the new
  `awaiting-developer` state, surfaces a dashboard attention item, and returns
  immediately; the developer approves and the next turn's first AR tool call
  auto-resumes (`running`) and auto-dismisses the item before
  `worktree_closeout_apply` (no `lifecycle_resume`). Block-and-wait
  `closeout-approval` / `push-approval` `lifecycle_gate` and the operator inbox
  parked as the fallback. Sync-propagated (`scripts/sync-skills.py`) bundle copy
  of the canonical `skills/c-12-closeout/SKILL.md`; the Task 25 Server-Side Gate
  Enforcement block above is superseded historical context. Verification metadata
  pinned until closeout stamps the task-28 code commit.
- 2026-06-26T18:58+02:00 — No content impact: reviewed the source commit's
  generated skill-copy sync; the existing body already documents closeout as
  preview/dry-run first, chat report second, then `lifecycle_gate`, with apply
  only after developer resolution plus `lifecycle_resume`.
- 2026-06-26T17:21+02:00 — Task 25 regression fix: current closeout guidance now
  follows preview/dry-run first, chat report second, and `lifecycle_gate` third;
  apply remains after developer resolution plus `lifecycle_resume`.
- 2026-06-26T17:12+02:00 — Regression fix: current closeout and push gate
  guidance now describes `lifecycle_gate` as the single call that creates the
  durable gate, blocks the lifecycle, and waits for the developer decision or
  matching inbox response.
- 2026-06-26T14:27+02:00 — Task 25: updated current closeout and push gate guidance to use `lifecycle_gate` as the single lifecycle-gate junction call that creates the durable gate, blocks the lifecycle with the ask, and waits for the developer response. Older split-call history entries below are superseded historical context. Verification metadata pinned until closeout stamps the task-25 code commit.
- 2026-06-25T13:20+02:00 — Task 23/24: closeout gate instructions now rely on one normal five-minute `gate_response_wait` call instead of caller-managed timeout loops.
- 2026-06-25T07:17+02:00 — Task 19: closeout gate enforcement docs now use `gate_response_wait` and require consuming returned operator-inbox entries after reading them, so dashboard Chat responses do not disappear while dashboard approvals/rejections remain developer-attributed gate decisions. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: packaged closeout guidance now names leaf enclosure `series-contract.md` paths and says the closeout worklist is anchored by the leaf contract-recorded range. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00 — Dashboard task 14: clarified that closeout is commit-only; `lifecycle_finalize_task` later proves the landed edge, runs or verifies cleanup, and marks the current task plus immediate parent row complete. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-23T07:39+02:00 — Slice 09: extended the Server-Side Gate Enforcement onboarding to the full **raise → wait → clear** choreography — the raise now opens the ambient `lifecycle_block(kind="decision")` **and** the durable `gate_create(kind="closeout-approval")`, and the agent **always clears** with `lifecycle_resume` (the new step) before `worktree_closeout_apply`, since a chat "approved" does not propagate itself. Stated that **`closeout-approval` IS the commit gate** (the single commit-of-record for code/memory/ledger; no separate `commit-approval`), and that the push junction uses the `push-approval` gate kind. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: documented the new Server-Side Gate Enforcement section — opt-in `gate_create`/`gate_wait` choreography for dashboard-connected lifecycles, the developer-approved-gate-binds / never-self-approve rule, and the gateless-unchanged fallback. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-12T19:47+02:00 — Approval Gate adopted the `l-01-agent-lifecycles` skill gate protocol: the relay is its own turn ending with a prose approval question, and the apply tool is never invoked in the same turn as the relay.
- 2026-06-12T19:06+02:00 — Issue #83: the skill documents the committed-range worklist (last verified commit → HEAD, base-scoped), the gate-regardless-of-author rule for existing artifacts, the non-blocking `unonboarded` report, and the commit-gate relay of its count + sample.
- 2026-06-11T06:47+02:00 — Issue #62 worktree-only closeout: the skill no longer offers `direct_closeout_preview`/`apply` or the "small approved edits" direct-closeout guidance; the MCP Tools block lists only the worktree closeout pair and the intro states the worktree-only rule.
- 2026-05-29T07:36+02:00: Updated after `c-12-closeout` skill added a changed-file content gate — a changed source whose existing sidecar body was not updated this task fails closeout — plus the matching failure condition and boundary against metadata-only verification refreshes.
- 2026-05-28T15:24+02:00: Updated after `c-12-closeout` skill explicitly required route overview metadata, generated route index refresh, and clean `memory_quality_check` before memory commits. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-26T16:25+02:00: Created after closeout guidance was promoted from `c-09-git-worktree-manager` skill into a shared direct/worktree closeout skill.
