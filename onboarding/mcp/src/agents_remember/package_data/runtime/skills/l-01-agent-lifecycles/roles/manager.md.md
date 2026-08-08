# l-01-agent-lifecycles/roles/manager.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-08T02:00+02:00 |
| lastVerifiedCommitHash | `1b7f6f07c5ccc64627299b5d22463ef9c267e187` |
| lastVerifiedCommitDate | 2026-08-08T02:42:36+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

This is the portable **manager** job file the `l-01-agent-lifecycles` frame houses at the master
tier. Like every job file it carries **both axes in one file** — the **role** (drive exactly one master
series) and the **lens** (leaf loop: dispatch · review · curator memory pass · delegated gates ·
master-exit handover) — plus an opening move, duties, artifact obligations, a comms protocol, and a
harness-agnostic knob block. The central doctrine the card must protect: **the spirit test does NOT
apply to the manager** — the default agent behavior stands, with no creative-liberty prompting in either
direction.

## Code Commentary

### Spawn Doctrine (260731-EFA-L16)

The immutability clause's fan-out permission is removed (developer ruling): the manager, as an
orchestration seat, uses no native sub-agents — analysis and report checks are its own work or a
dispatched reviewer/curator seat's, and role seats are created only via `spawn_agent_session`,
never as native sub-agents. Previously the clause allowed "sub-agents drill vertically for bounded
analysis or report checks", a shadow channel beside the seat machinery the manager exists to
operate. Native fan-out survives only on the hands-on seats (worker, reviewer, curator,
architect-solo).

### Logic

260707-HFX2-L5 (doctrine inversion, active vigilance → passive process-and-ack): the leaf-dispatch
loop's "Monitor the worker" bullet is gone. In its place, "Process and ack the worker's signals —
passive contract": a turn-report artifact is expected at every hand-off, but the manager does not
watch for it — the HFX2-L2 supervisor sweep evaluates each expected artifact
(`evaluate_turn_report_findings`/`missing_artifact()`) on its own mechanical tick and, on
inactivity, injects the nudge and walks the HFX2-L4 escalation ladder (renudge → skip-level →
architect custody/architect attention, then respawn). The manager's own job inverts to being woken with its pending
signals and processing/acking every item before ending its turn. A new **watcher ban** line
(uniform-mechanism ruling 2026-07-07) states this in the file directly: no seat-local watcher of
any kind, the L2 sweep is the one mechanism, no per-seat variance. The Comms Protocol's "Stdin
push" line is reworded the same way — nudges are delivered by the L2 supervisor's injector on its
own tick, never the manager's own initiative; a non-hosted seat gets the inbox equivalent. This is
purely a doctrine reword — the mechanical detection/escalation machinery itself (the sweep, the
ladder) already landed in HFX2-L2/L4; this leaf only inverts the seat's OWN duty language to match
what those leaves already built.

260707-HFX2-L6 adds the developer-declared takeover pre-step to the manager opening move. A manager
entered by the developer through an existing dashboard chat first runs the shared
Developer-Declared Task-Seat Takeover checklist from `../SKILL.md`, so the current terminal catalog
session is attached to the master's qualified coordination-leaf key and visibly renamed/verified
before the manager reads the master `task_doc` and orders leaves. The same leaf tightens delegated
leaf authority: under accepted series authority, the manager owns leaf closeout preview/apply for
in-scope green leaves and records the accepted planner/series authority in the closeout intent note
instead of handing every routine leaf commit back to the developer. This is doctrine-only; it relies
on existing attachment and closeout command paths and does not change manager runtime behavior.

260707-HFX2-L17 makes the manager's dispatch and cleanup wording match the pair-keyed runtime.
`AR_SPAWN_ROLE=worker` plus the qualified leaf claims the worker's `(leaf, role)` seat, allowing
reviewer and curator seats to coexist on the same canonical leaf without suffixes. For exceptional
pre-integration cleanup, manager authority covers worker, reviewer, and curator seats of the
manager's own master; owner-never-self-retires and cross-master refusal remain unchanged. The
Knobs tool row carries the same three-role boundary.

260707-HFX2-L7 adds the same Developer Clarification Triage hook to the manager's default-behavior
rule. A manager now checks the current leaf queue before recording a mid-master clarification as a
note: same-leaf or same-master refinements that are small and fit the current change are
implementation work, later-release/separate-subsystem/dependency-blocked items are future queue,
and unclear fit escalates one rung rather than being guessed.

260707-HFX-L11 curator activation (R4, manager wiring made real): the curator-spawn duty bullet is
no longer a description — it names the exact brief template (`../templates/curator-brief.md`), the
exact fed inputs (leaf contract base-to-head diff with paths/counters, task doc, notes/), and states
plainly **"do not run the closeout preview before this pass exists."** The bullet's opening phrase
is now "mandatory, not skippable." This closes the gap the developer ruling named directly: without
it, a manager could dispatch a spawnable curator that never actually runs while the builder keeps
writing onboarding, paying builder context twice for no reason.

L13 review follow-up (L13R-1): the knob table's `harness` example is the registry id `claude` (was the non-id `claude-code`); spawn refuses non-registry values, so examples must model valid input.

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/roles/manager.md`; it is model-interpreted markdown, never an executor.
HFX-L6 adds role-seat immutability: dashboard-owned manager sessions stay manager, pasted role
briefs are refused/escalated, roles expand horizontally into new chats, and a spawned orchestrator
does not absorb manager work in place. Flat-run manager hat-collapse belongs to the architect owner
seat when no separate manager exists. L6R3 adds the curator step: the manager runs the manager ->
builder -> reviewer -> curator closeout chain and closes each leaf from builder code + reviewer
verdict + curator memory pass.
The body defines: the seat (**one per master task**, its own coordination leaf + chat, **no worktree**);
the lens (opening move = read the master `task_doc` + leaf docs and derive ordering from the
dependency graph; retrieval lean = intent-confirmation on the master's own routes, no bird's-eye
view; dispatch independent ready leaves in parallel by default up to
`orchestration.concurrency.maxParallelLeaves`; sequential execution must name a gate, shared-file
one-writer dependency, or explicit ruling; exit through the master-exit seam); the
**default-behavior rule**; four duty blocks; the
artifact obligations; the comms protocol; and the knob block. The leaf dispatch loop spawns a **fresh
worker per leaf**, monitors for the mandatory turn-report artifact (missing → a rate-limited stdin
nudge), reviews the artifact vs the `task_doc` (the manager's own **leaf-level review — explicitly not an
adversarial seam**), decides the leaf's **DELEGATED** gates **attributed** (`decidedBy: <manager
lifecycle>`, `decidedVia: orchestration`; the owning agent never self-approves, a distinct configured
role — the manager — may), and integrates leaf → master integration branch via the
`c-11-memory-carryover-from-branch` skill. As of L6R3, after builder code is ready and the reviewer
verdict exists, the manager spawns a fresh curator (`roles/curator.md`, `AR_SPAWN_ROLE=curator`) for
the onboarding-only memory pass and treats that report as the third leaf closeout input.
**260707-HFX-L7 (provider degradation protocol)** inserts a new "Provider Degradation Alert"
subsection right after the seat definition/opening-move paragraph, before the leaf dispatch loop:
on a `degradation-alert` inbox row, the manager immediately stops **starting** any more providers
until an all-clear/healthy event arrives — no `worktree_start` with provider setup, no
`provider_watchers start`, no watcher restart, no `retry_provider_setup` — while continuing any
providerless/native-read work that remains valid and reporting provider-dependent blockers up to
the orchestrator. The subsection is explicit that this is an ADDITION to, not a relaxation of, the
manager's existing no-kill-authority boundary (see Invariants And Boundaries below): the manager
must not docker-kill, must not stop containers, and must not call any provider teardown path
either before or during a degradation alert — investigation, remediation orders, and provider
stops belong exclusively to the orchestrator via the new system-specialist protocol
(`roles/orchestrator.md`). This composes cleanly with the manager's pre-existing "no bird's-eye
view" limit (Invariants And Boundaries): the manager reacts locally (stop starting) and escalates
rather than reasoning about portfolio-wide provider health itself. At master exit
it spawns the **adversarial reviewer**
(master-exit seam); a blocking verdict **decomposes into fix leaves** the manager dispatches, and
verdicts are **evidence, not decisions** (the manager decides the handover gate with the verdict as judge
evidence). It then posts the **master-handover packet** (`templates/master-handover-packet.md`) up to the
orchestrator.

### Conventions

Role + lens in one file (D10); a portable knob block (D7) resolving job base <
`roles/manager.<harness>.md` variant < `settings.json orchestration.roles.manager`. Coordination seat =
an ordinary `subTask` leaf with no enclosure and a role marker; comms ride the inbox (durable, dashboard-
visible) plus stdin push (nudges/messages into hosted worker sessions, poll as fallback). Gate delegation
is documented here but **enforced in leaf L4**; until then hand-offs follow the
`l-01-session-job-lifecycle` skill.

### Invariants And Boundaries

**The spirit test does NOT apply to this seat — it is orchestrator-only.** The manager gets **no
creative-liberty prompting in either direction**: the **default agent behavior stands** (fulfill the
task, fill small unambiguous blanks a competent implementer would fill, and no more). A **plan delta
beyond blank-filling ESCALATES to the orchestrator** — never a reshape, and **never straight to the
developer**. The manager has **no bird's-eye view** (one master, not the portfolio); the breadth /
blast-radius reasoning belongs to the orchestrator. **260707-HFX-L7:** the manager has **NO
provider kill authority, full stop** — this holds both in ordinary operation and during a
provider-degradation alert; a degradation alert only ADDS a stop-starting duty on top of an
already-absolute boundary, it does not create a new exception either direction. The **owning agent never self-approves**; the manager
decides its leaves' delegated gates as the distinct configured role. Escalation resolves within the
master's own view first, then rises up the ladder to the orchestrator. The manager does not write the
curator's onboarding pass; it spawns the curator and consumes the resulting memory-pass report.

### Todos

No `roles/manager.<harness>.md` overlay ships yet; author one when a harness needs manager-specific knobs.
No other TODO is recorded for this job file.

### Docs References

No external domain documentation applies to this repository-local orchestration job file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

### L16 Knob Additions

260703-L16: the Knobs table gains the three FREE-FORM rows (`launchArgs` — verbatim harness argv;
`sessionCommands` — lines pasted + submitted into the fresh session before the brief;
`promptKeywords` — prepended as the first line of the dispatch brief paste; all settings-only,
never validated, recorded in spawn provenance), and the knob footer now names the per-level
override (`orchestration.rolesPerLevel.<level>.<role>`; role-file defaults < settings < level
override) plus the `docs/reference/harnesses.md` spawn-knobs manual.

## Repo-Internal References

The manager spawns workers, spawns the master-exit reviewer, and hands its master up to the orchestrator.

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | `# Lifecycle — Manager` | skills/l-01-agent-lifecycles/roles/manager.md:1-242 |
| The frame that houses this seat and owns the escalation ladder, gate-delegation doctrine, and the two adversarial seams. | `# l-01-agent-lifecycles — The Agent Lifecycles` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:6-416 |
| The worker seat the manager spawns fresh per leaf and whose turn report it reviews. | `# Lifecycle — Worker` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md:1-154 |
| The adversarial reviewer spawned at the master-exit seam, whose blocking verdict decomposes into fix leaves the manager dispatches. | `# Lifecycle — Adversarial Reviewer` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:1-187 |
| The orchestrator seat the manager escalates to and hands the completed master over to. | `# Lifecycle — Orchestrator` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:1-463; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:283-290 |

As of the 260703-L8 reopened pass the file carries two additions: a flat-run note (in a flat series the ORCHESTRATOR wears this hat — same duties, same artifacts, one chair) and the reopen-and-reshape rule in the leaf-review bullet (a leaf whose deliverable came out wrong is reopened under its own id via task_reopen and its doc reshaped — never duplicated into a redo sibling; new leaves are for genuinely new changes).

As of the L8 de-harnessing pass the overlay-authoring sentence is gone and the knob harness row is a preference settings overrides: no per-harness manager files.

As of cycle 4 the master-exit procedure is operable as-built: the manager RAISES the `master-handover-approval` gate (delegable, never human-pinned) with the verdict attached as evidenceRefs, and the ORCHESTRATOR decides it — identity mechanics stated (raiser = the manager's ambient lifecycle; the deciding orchestrator's ambient identity becomes decidedBy; owner-never-self-approves holds; no ids handled). The leaf loop now names the human-pinned kinds (integration-approval, push-approval, cleanup-approval) and marks the integrate step's durable-gate behavior; reviewer spawns state AR_SPAWN_ROLE=reviewer; finalize wording is honest (statuses via the tool, steps by hand); the knob footer resolution is role-file defaults < settings.

As of cycle 5: the seam channel is exact: raise with lifecycle_gate(..., wait=false) → carry the returned gateId in the handover packet; identity truth restated (gate ids are model-visible, lifecycle ids stay server-side); the integrate-step sentence now defines the series' standing approval (the developer's portfolio-gate approval recorded in the planner master) and the seat's own hand-off idiom (gates + inbox, never the developer-facing notification). Cycle 6 completes the raise's address: §3's call now carries `enclosure="<master task name>"` — the master identity integration enforcement matches the gate by — and adds the all-human conditional (under an all-human policy the raise blocks and the developer decides; do not pass wait=false). Cycle 7 pins the address as a contract, not a convention: §3 now states the match is exact-string — the EXACT master task name as the contracts carry it (`worktree_start`'s `task_name`) — and that a wait=false raise without an enclosure is refused.

As of 260703-L12 the leaf dispatch loop opens with **loop-tier scoring at dispatch** (blast radius · novelty · size → direct | builder-verified | full loop; round 2 (L12R-4) pins the direct tier so it cannot read manager-implements: NO loop machinery — the leaf's worker implements as usual, this seat still dispatches per leaf and never grows a build surface; the strategist's blast-radius register is the scoring input when an orchestration task exists; the mark — tier + scope manager|orchestrator — lands on the leaf doc with a decision-log entry; **a master whose leaves all score direct is a workflow-free manager**), and a full-loop leaf runs under this level's loop controls: hard cap 3 FULL rounds (delta-verifies by the same reviewer close rounds and do not count; fix rounds resume the same builder), and a non-shrinking round escalates to the orchestrator immediately with the full round history. The Comms escalation bullet adds the **quo-vadis test** — a high-blast-radius truth is flagged as quo-vadis when raised so the orchestrator relays it to the architect immediately; presentation-grade choices are decided and logged, never escalated.

### 260707-HFX2-L11 Seat Cleanup Addition

Issue #12's authority split still governs explicit retirement, but normal successful completion no
longer terminates chats. A landed leaf's worker/reviewer chats are marked `status:"landed"` by
`worktree_integrate` (config-gated `retirement.autoLandOnIntegration`, default ON) and move into the
dashboard's collapsed landed archive for later inspection; tmux stays alive until an explicit archive
cleanup. For a stuck/abandoned leaf seat before integration (a dead-end retry, a duplicate spawn), the
manager retires it by hand: `session_retire(actor_session_id=<own session>, session_id=<the seat>,
reason=...)`. Server-side policy (`serving/retire_policy.py`) enforces the authority split: the
manager lives OUTSIDE the master stack it manages, so it may retire ONLY the
worker/reviewer/curator seats of its OWN master — it can never unseat itself by construction
(owner-never-self-retires), and a target of any other role or a different master is refused loudly,
naming the exact policy clause.
Transcripts are never deleted; retiring only terminates the tmux session and marks the catalog row
terminated with retirement provenance. The Knobs table's `tools` row includes `session_retire`
(scoped to the manager's own master's worker/reviewer/curator seats) for those exceptional by-hand
cases.

## Cross-Repo References

No sibling repository evidence is needed for this orchestration job file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.


### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

### 260731-EFA-L17 — Quality Altitude Ladder

The manager role file's integration section now carries a **Quality altitude ladder**
bullet (source lines 163-168): leaf closeout and leaf integration run the
change-set-scoped contract (`agents_remember.code_quality.check --targeted`); the full
wrapper runs exactly once per master inside `worktree_integrate` at master altitude,
memory-capped (`orchestration.qualityGate.memoryCapBytes`); `memory_quality_check` is NOT
part of that move — it stays a per-leaf closeout gate, and a leaf closeout that skips its
required checks is refused, not passed.

## Update History

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the manager's quality
  altitude ladder bullet (leaf `--targeted`; full wrapper once per master,
  memory-capped; `memory_quality_check` per leaf). Verification metadata stays
  pinned until closeout stamps the 260731-EFA-L17 commit.
- 2026-08-05T22:10+02:00 — 260731-EFA-L16 curator: recorded the removal of the manager's native fan-out permission (developer ruling: orchestration seats use no shadow channel; analysis and report checks are the seat's own work or a dispatched reviewer/curator seat's) and the role-seat-only-via-`spawn_agent_session` binding. Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-04T18:20+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 10 citation findings and two wording
  drifts. Re-anchored the five role/frame rows to their `#`-heading anchors with exact spans (canonical
  manager.md 1-242 byte-identical to this copy; SKILL.md 6-416; worker 1-80; reviewer 1-151;
  orchestrator 1-8/283-290). Aligned the spirit-test line to the source's "orchestrator-only" and the
  quo-vadis relay to the architect (was "developer"). Scoped recheck clean.
- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: removed a leaked diff marker. A body section (heading plus paragraph) had been pasted into this Update History list on 260712-TRH-L4 carrying the diff's `+`. Because `+##` has no space after the plus, markdown rendered it as literal text, so the heading was not a heading and the surrounding bullet list was broken. The same section already existed correctly earlier in the file; where the pasted copy said more, its wording was promoted into that section before the paste was deleted. No claim changed. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-10T15:48+02:00 — 260707-HFX2-L17 generated-runtime doctrine delta: worker dispatch now
  records the environment-role-plus-qualified-leaf pair claim, and manager cleanup authority now
  consistently includes worker/reviewer/curator seats of the manager's own master in both prose and
  the tools row. Verification metadata remains pinned until closeout stamps the L17 commit.

- 2026-07-10T02:39+02:00 — HFX3/L14 combined curation: manager leaf scheduling now follows the
  dependency graph and dispatches independent ready leaves in parallel within
  `maxParallelLeaves`; serial work must name its gate, one-writer dependency, or ruling. Corrected
  the ladder terminal to architect custody and added the governing-overview backlink. Verification
  metadata remains pinned until closeout stamps the eventual two-parent code commit.

- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 curator correction: the package-data manager role
  sidecar now states that `worktree_integrate` auto-lands successful worker/reviewer chats into the
  landed archive (`autoLandOnIntegration`) rather than auto-retiring them; manual `session_retire`
  remains only for stuck/abandoned seats inside the manager's authority. Verification metadata
  pinned until closeout stamps the HFX2-L11 commit.

- 2026-07-08T23:59+02:00 — 260707-HFX2-L5 (doctrine rewrite, active vigilance → passive
  process-and-ack): "Monitor the worker" replaced with the passive contract — the HFX2-L2 sweep
  detects missing/stale turn reports mechanically, the HFX2-L4 ladder handles inactivity, and the
  manager's duty inverts to processing/acking supervisor-injected signals; new watcher-ban line
  (uniform-mechanism ruling 2026-07-07); Comms "Stdin push" line reworded to name the L2 injector as
  the delivery mechanism. Doctrine-only change set (5 canonical `skills/` files synced to 9
  downstream copies, 0 Python); sync-propagated bundle copy of the canonical
  `skills/l-01-agent-lifecycles/roles/manager.md`. Verification metadata pinned until closeout
  stamps the 260707-HFX2-L5 commit.

- 2026-07-08T15:45+02:00 — 260707-HFX2-L7 doctrine refinement: the manager's default-behavior rule
  now runs Developer Clarification Triage against the current leaf queue before note-only handling.
  Same-leaf/same-master refinements that are small and fit the active change are implementation
  work; future/dependency-blocked items are queued; unclear fit escalates one rung.

- 2026-07-08T15:27+02:00 — 260707-HFX2-L6 (seat takeover + delegated leaf closeout):
  manager opening move now points developer-declared takeovers to the shared task-seat checklist
  before reading the master `task_doc`: attach the current dashboard terminal catalog session to the
  qualified leaf key, rename it to the expected seat label, and verify the catalog/dashboard row.
  The delegated leaf-gates paragraph now states that, under accepted series authority, the manager
  owns leaf closeout preview/apply for in-scope green leaves and records the accepted planner/series
  authority in the closeout intent note. Verification metadata pinned until closeout stamps the
  260707-HFX2-L6 commit.

- 2026-07-08T02:55+02:00 — 260707-HFX-L8 (seat lifecycle: retirement + live identity + turn-state,
  issue #12): leaf-dispatch-loop section gains a "Seat cleanup" bullet — `worktree_integrate`
  auto-retires a landed leaf's worker/reviewer seats (config-gated, default ON); manual
  `session_retire` for a stuck/abandoned seat is scoped server-side to only the manager's own
  master's worker/reviewer seats (owner-never-self-retires unconditional). Knobs `tools` row
  updated. Sync-propagated bundle copy from the canonical `skills/l-01-agent-lifecycles/roles/
  manager.md`. Verification metadata pinned until closeout stamps the HFX-L8 commit.

- 2026-07-08T02:10+02:00 — 260707-HFX-L11 curator activation (R4): the curator-spawn duty bullet
  reworded from descriptive to enforced — "Curator memory pass — mandatory, not skippable," naming
  `../templates/curator-brief.md`, the exact fed inputs (leaf contract base-to-head diff w/
  paths/counters, task doc, notes/), and the hard gate "do not run the closeout preview before this
  pass exists." Doctrine-only change set (7 canonical `skills/` files: 6 edits + 1 new template,
  each synced to 9 mirrors, 0 Python); sync-propagated (`scripts/sync-skills.py`) bundle copy of the
  canonical `skills/l-01-agent-lifecycles/roles/manager.md`. Verification metadata pinned — no
  commit yet on `ar/260707-hfx-l11-curator-activation` (working-tree change, synced onto the landed
  HFX-L7 base).

- 2026-07-08T01:00+02:00 — 260707-HFX-L7 (provider degradation protocol): documented the new
  "Provider Degradation Alert" subsection landed right after the seat/opening-move paragraph — on
  a `degradation-alert` inbox row the manager stops starting providers (no worktree provider
  setup, no watcher start/restart, no `retry_provider_setup`) until an all-clear, continues valid
  providerless work, and escalates provider blockers to the orchestrator; reinforced in Invariants
  And Boundaries that this is additive to the manager's pre-existing absolute no-kill-authority
  boundary, not a new carve-out. Sync-propagated bundle copy. Verification metadata pinned until
  closeout stamps the HFX-L7 commit.
- 2026-07-07T21:40+02:00 — 260707-HFX-L6R3 curator seat: documented the manager
  -> builder -> reviewer -> curator leaf closeout chain; manager spawns a fresh curator after
  builder code and reviewer verdict are available, and leaf closeout inputs are builder code +
  reviewer verdict + curator memory pass. Sync-propagated bundle copy. Verification metadata
  pinned until closeout stamps the HFX-L6 commit.

- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: added
  role-seat immutability; updated flat-run hat-collapse to the architect owner seat; and adjusted
  escalation wording so manager deltas rise to the backend orchestrator and then architect relay
  when needed. Sync-propagated bundle copy. Verification metadata pinned until closeout stamps
  the HFX-L6 commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): Knobs table gained the three
  free-form escape-hatch rows (launchArgs / sessionCommands / promptKeywords, settings-only, never
  validated) and the knob footer now includes the rolesPerLevel per-level override and the
  harnesses.md manual pointer. Sync-propagated bundle copy. Verification metadata pinned until
  closeout stamps the L16 commit.

- 2026-07-06T23:45+02:00 — L13 adversarial-review follow-up (L13R-1): knob-table harness example fixed to the registry id `claude`. Verification metadata pinned until closeout stamps the L13 commit.

- 2026-07-06T17:35+02:00 — 260703-L12 round 2 (L12R-4): the direct-tier gloss reworded per the ruling — the leaf's worker implements without loop machinery; the manager still dispatches per leaf and never grows a build surface (the worker-per-leaf framing stays unconditional). Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T15:35+02:00 — 260703-L12 (three-party loops): the leaf dispatch loop gains loop-tier scoring at dispatch (direct / builder-verified / full loop; strategist blast-radius register as input; all-direct = workflow-free manager) and the full-loop controls (3-full-round cap, delta-verify/builder-resume, convergence escalation with round history); the escalation bullet carries the written quo-vadis test. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-05T19:55+02:00 - L8 builder cycle 7: §3 pins the enclosure as the EXACT contract task name (exact-string match) and states the enclosure-less raise refusal (AR4-1c). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 - L8 builder cycle 6: §3 raise now carries enclosure=<master task name> (the integration guard's address) + the do-not-pass-wait=false-under-all-human conditional (AR3-1/AR3-2). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): the seam channel is exact: raise with lifecycle_gate(..., wait=false) → carry the returned gateId in the handover packet. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:20+02:00 - L8 seam-ruling remediation (cycle 4): master-exit seam made operable (raise-with-verdict -> orchestrator decides); human-pinned kinds enumerated at the integrate step; reviewer spawn value stated. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:40+02:00 - L8 de-harnessing pass: overlay-authoring sentence removed (no per-harness files). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:15+02:00 - L8 orchestrator routes rework: flat-run note added (in a flat series the orchestrator wears this hat) and the leaf-review bullet gained the reopen-and-reshape rule (task_reopen a wrong deliverable, never a redo sibling). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: the manager now owns the leaf lifecycle END-TO-END (worker closeout stripped; worktree_start -> closeout/gates -> integrate -> finalize incl. task-doc steps); master-exit reviewer spawn procedure inlined; gate policy described as-built; briefs compiled from templates/worker-brief.md with AR_SPAWN_ROLE + the qualified leaf key. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` manager job file (leaf 260703-L1) — one manager per master, the leaf dispatch loop with delegated attributed gates and C-11 integration, the master-exit adversarial seam and handover packet, and the critical rule that the spirit test does NOT apply here (default behavior stands; a plan delta escalates to the orchestrator, never the developer). Verification metadata pinned until closeout stamps the L1 commit.
