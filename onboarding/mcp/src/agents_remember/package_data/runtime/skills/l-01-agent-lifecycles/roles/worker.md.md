# l-01-agent-lifecycles/roles/worker.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T15:35+02:00 |
| lastVerifiedCommitHash | `bcaa78070f77c76f1c4db0af93786bb193b92523` |
| lastVerifiedCommitDate | 2026-07-06T07:51:05+02:00|

## Purpose

The self-contained worker lifecycle: one leaf, one session, one report. The brief is the worker's ENTIRE session start - it replaces the front half the spawner already ran. The worker builds; it owns no lifecycle machinery: closeout, integration, finalization, gates, and task-doc bookkeeping belong to the owning seat. Terminal state: checks green + mandatory turn report.

## Code Commentary

### Logic

Sync-propagated copy of the canonical `skills/l-01-agent-lifecycles/roles/worker.md`. The worker loop: intake (brief + leaf task_doc + predecessor report - never a transcript) -> orient (paired reads via read_ar_files, which serves the OFFICIAL baseline, plus native worktree reads as the edit precondition; evidence tally per brief) -> build (leaf plan exactly; same-pass c-05 onboarding incl. the literal '- <ISO> - No route impact: <reason>' attestation form; generated indexes via local build_route_indexes; NEVER git commit) -> checks green (brief-prescribed focused + full wrapper; a red check outside leaf scope is an escalation) -> mandatory turn report (../templates/turn-report.md, written even when blocked) -> end. Tool surface stated positively: native file tools in the two worktrees, read-only AR retrieval, shell for checks, inbox when wired; no worktree_*/lifecycle_*/task_doc/gate_*/memory_*/route_index_refresh. Default behavior: fulfill the task, fill small blanks; plan deltas escalate one rung to the owning seat (spirit test is orchestrator-only). Knob default harness is codex (the practiced worker economics); `roles/worker.claude-code.md` overlays Claude Code.

As of the L8 de-harnessing pass the file carries a Fan-Out capability-doctrine section (read/search sub-agents only, scoped to the leaf; durable notes + compact summaries; the main loop owns every durable act incl. the never-delegated turn report) — formerly the deleted roles/worker.claude-code.md overlay, generalized off the vendor.

As of cycle 4 the knob footer resolution reads role-file defaults < settings (dead variant rung removed).

As of cycle 5: the fan-out fallback clarifies workers do not spawn AR sessions (spawning is the seats' channel).

As of 260703-L12 the file carries a **Loop Position** section (between Fan-Out and Default Behavior): on a builder-verified or full-loop leaf this seat is the three-party loop's BUILDER — fix rounds resume the SAME session and round-2+ reports APPEND to the report file (loop history stays legible); the cap, the convergence call, and escalation are the OWNER's controls, not the worker's; disagreement with a handed reviewer finding is stated with evidence in the report — the owner rules, the worker never argues a verdict into the code.

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-06T15:35+02:00 — 260703-L12 (three-party loops): a Loop Position section makes the worker the loop's BUILDER — fix rounds resume the same session, reports append, cap/convergence/escalation stay the owner's, and disagreement with a finding goes into the report as evidence. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): the fan-out fallback clarifies workers do not spawn AR sessions (spawning is the seats' channel).. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:20+02:00 - L8 seam-ruling remediation (cycle 4): knob footer variant rung removed. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:40+02:00 - L8 de-harnessing pass: harness overlay deleted; fan-out doctrine folded in; knob harness row is a preference settings overrides. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: worker.md rewritten as a POSITIVE, self-contained lifecycle: no session-job references, closeout/integrate/attach stripped (owning seat's machinery), brief-as-session-start, terminal state = checks green + turn report; body rewritten accordingly. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T12:31+02:00 - L3: worker comms now name the inbox message-kind
  metadata, mandatory turn-report artifact path, and manager nudge tool.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-02-agent-orchestration` worker job file (leaf 260703-L1) — one short-lived fresh worker per leaf onboarded from context packet + task_doc (never a transcript), the l-01 build spine in the leaf worktree, the manager-decided closeout gate, the mandatory turn-report artifact, and the same default-behavior rule as the manager (spirit test does not apply; a plan delta escalates to the manager). Verification metadata pinned until closeout stamps the L1 commit.
