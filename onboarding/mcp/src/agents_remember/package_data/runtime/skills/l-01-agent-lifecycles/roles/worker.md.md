# l-01-agent-lifecycles/roles/worker.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-08T23:59+02:00 |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce` |
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|

## Purpose

The self-contained worker lifecycle: one leaf, one session, one report. The brief is the worker's ENTIRE session start - it replaces the front half the spawner already ran. The worker builds code and writes the builder turn report; it owns no lifecycle machinery and no official onboarding memory pass. Closeout, integration, finalization, gates, task-doc bookkeeping, and the curator memory pass belong to separate owning/spawned seats. Terminal state: checks green + mandatory turn report with changed paths for the curator.

## Code Commentary

### Logic

260707-HFX2-L5 (doctrine inversion, active vigilance → passive process-and-ack): the mandatory
turn-report paragraph's "A missing report gets nudged." is reworded to name the actual mechanism —
"A missing report gets nudged by the supervisor sweep (HFX2-L2), never by a seat-local watcher — no
owning seat, and no worker, hand-rolls its own polling loop over this artifact; ending your turn
once the report is written is safe, not a risk you have to cover for." The Comms Protocol's "Stdin
push" line is reworded the same way (the L2 sweep's injector delivers on its own tick, in the
owning seat's name, never the owning seat or the worker watching/polling by hand), and a new "Idle
is safe" bullet plus an explicit **watcher ban** line (uniform-mechanism ruling 2026-07-07) are
added right after it. Pure doctrine reword — the worker's own build loop and artifact obligation are
unchanged; only the language describing what happens to a missing/late artifact inverts to name the
supervisor sweep as the one mechanism.

260707-HFX2-L6 adds the same developer-declared takeover guard to worker intake. If a developer
walks into or reuses a dashboard chat as the worker for a named leaf, the worker first runs the
shared Developer-Declared Task-Seat Takeover checklist from `../SKILL.md`, attaching the current
terminal catalog session to the leaf's qualified key and verifying the catalog/dashboard row before
reading the brief and leaf `task_doc`. This does not widen the worker's authority: worktree,
closeout, gate, lifecycle, and memory operations still belong to the owning seat.

Sync-propagated copy of the canonical `skills/l-01-agent-lifecycles/roles/worker.md`. The worker loop: intake (brief + leaf task_doc + predecessor report - never a transcript) -> orient (paired reads via read_ar_files, which serves the OFFICIAL baseline, plus native worktree reads as the edit precondition; evidence tally per brief) -> build code (leaf plan exactly; produce changed paths, code-diff summary, tests, and route/onboarding observations for the downstream curator; NEVER git commit) -> checks green (brief-prescribed focused + full wrapper; a red check outside leaf scope is an escalation) -> mandatory turn report (../templates/turn-report.md, written even when blocked) -> end. Tool surface stated positively: native file tools in the code worktree, memory reads for context/changelog hints, read-only AR retrieval, shell for checks, inbox when wired; no worktree_*/lifecycle_*/task_doc/gate_*/memory_*/route_index_refresh. Default behavior: fulfill the task, fill small blanks; plan deltas escalate one rung to the owning seat (spirit test belongs to the backend orchestrator or architect owner seat). Knob default harness is codex (the practiced worker economics); `roles/worker.claude-code.md` overlays Claude Code.

HFX-L6 adds role-seat immutability for dashboard-owned worker sessions and names architect as the
owning seat in solo/flat dispatch. L6R3 keeps the worker as the builder only: a worker never absorbs
curator/onboarding-writer work, and the official manager -> builder -> reviewer -> curator chain puts
onboarding writes in a fresh curator session. A worker still escalates only one rung to its owner
(manager, backend orchestrator, or architect in solo flat mode), never directly to the developer.

As of the L8 de-harnessing pass the file carries a Fan-Out capability-doctrine section (read/search sub-agents only, scoped to the leaf; durable notes + compact summaries; the main loop owns every durable act incl. the never-delegated turn report) — formerly the deleted roles/worker.claude-code.md overlay, generalized off the vendor.

As of cycle 4 the knob footer resolution reads role-file defaults < settings (dead variant rung removed).

As of cycle 5: the fan-out fallback clarifies workers do not spawn AR sessions (spawning is the seats' channel).

As of 260703-L12 the file carries a **Loop Position** section (between Fan-Out and Default Behavior): on a builder-verified or full-loop leaf this seat is the three-party loop's BUILDER — fix rounds resume the SAME session and round-2+ reports APPEND to the report file (loop history stays legible); the cap, the convergence call, and escalation are the OWNER's controls, not the worker's; disagreement with a handed reviewer finding is stated with evidence in the report — the owner rules, the worker never argues a verdict into the code.

### L16 Knob Additions

260703-L16: the Knobs table gains the three FREE-FORM rows (`launchArgs` — verbatim harness argv;
`sessionCommands` — lines pasted + submitted into the fresh session before the brief;
`promptKeywords` — prepended as the first line of the dispatch brief paste; all settings-only,
never validated, recorded in spawn provenance), and the knob footer now names the per-level
override (`orchestration.rolesPerLevel.<level>.<role>`; role-file defaults < settings < level
override) plus the `docs/reference/harnesses.md` spawn-knobs manual.

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-08T23:59+02:00 — 260707-HFX2-L5 (doctrine rewrite, active vigilance → passive
  process-and-ack): "A missing report gets nudged." reworded to name the HFX2-L2 supervisor sweep
  as the actual mechanism (never a seat-local watcher); Comms "Stdin push" line reworded the same
  way, plus a new "Idle is safe" bullet and watcher-ban line (uniform-mechanism ruling 2026-07-07).
  Doctrine-only change set (5 canonical `skills/` files synced to 9 downstream copies, 0 Python);
  sync-propagated bundle copy of the canonical `skills/l-01-agent-lifecycles/roles/worker.md`.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L5 commit.

- 2026-07-08T15:27+02:00 — 260707-HFX2-L6 (seat takeover doctrine): worker intake now starts a
  developer-declared takeover by running the shared task-seat checklist, attaching the current
  dashboard terminal catalog session to the qualified leaf key and verifying the dashboard row
  before reading the brief/task doc. The worker remains a build-only seat; the note does not grant
  worktree, closeout, gate, lifecycle, or memory authority. Verification metadata pinned until
  closeout stamps the 260707-HFX2-L6 commit.

- 2026-07-07T21:40+02:00 — 260707-HFX-L6R3 curator seat: reframed the worker
  as code builder only in the manager -> builder -> reviewer -> curator chain. The worker report now
  supplies changed paths, code-diff summary, tests, and observations for the curator memory pass;
  the curator, not the worker, writes onboarding. Sync-propagated bundle copy. Verification metadata
  pinned until closeout stamps the HFX-L6 commit.

- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: added
  role-seat immutability and updated worker dispatch/escalation language for architect-owned
  flat runs while preserving the one-leaf/one-report worker loop. Sync-propagated bundle copy.
  Verification metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): Knobs table gained the three
  free-form escape-hatch rows (launchArgs / sessionCommands / promptKeywords, settings-only, never
  validated) and the knob footer now includes the rolesPerLevel per-level override and the
  harnesses.md manual pointer. Sync-propagated bundle copy. Verification metadata pinned until
  closeout stamps the L16 commit.

- 2026-07-06T15:35+02:00 — 260703-L12 (three-party loops): a Loop Position section makes the worker the loop's BUILDER — fix rounds resume the same session, reports append, cap/convergence/escalation stay the owner's, and disagreement with a finding goes into the report as evidence. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): the fan-out fallback clarifies workers do not spawn AR sessions (spawning is the seats' channel).. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:20+02:00 - L8 seam-ruling remediation (cycle 4): knob footer variant rung removed. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:40+02:00 - L8 de-harnessing pass: harness overlay deleted; fan-out doctrine folded in; knob harness row is a preference settings overrides. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: worker.md rewritten as a POSITIVE, self-contained lifecycle: no session-job references, closeout/integrate/attach stripped (owning seat's machinery), brief-as-session-start, terminal state = checks green + turn report; body rewritten accordingly. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T12:31+02:00 - L3: worker comms now name the inbox message-kind
  metadata, mandatory turn-report artifact path, and manager nudge tool.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-02-agent-orchestration` worker job file (leaf 260703-L1) — one short-lived fresh worker per leaf onboarded from context packet + task_doc (never a transcript), the l-01 build spine in the leaf worktree, the manager-decided closeout gate, the mandatory turn-report artifact, and the same default-behavior rule as the manager (spirit test does not apply; a plan delta escalates to the manager). Verification metadata pinned until closeout stamps the L1 commit.
