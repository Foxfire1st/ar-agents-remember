# l-01-agent-lifecycles/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-09T13:59+02:00 |
| lastVerifiedCommitHash | `100b40d6be4a7d03eedbb1164ce54e2e8a314038` |
| lastVerifiedCommitDate | 2026-08-14T08:23:37+02:00|
| governingOverview      | `../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../overview.md)

## Purpose

Packaged runtime copy of the unified lifecycle router and shared frame. The canonical source at
`skills/l-01-agent-lifecycles/SKILL.md` owns doctrine; `scripts/sync-skills.py` replaces and checks
this artifact byte-for-byte for installed runtimes.

## Code Commentary

### Logic

The router selects exactly one role from plane-injected `AR_SPAWN_ROLE`, a fresh role brief, or the
unbound free-chat launcher. Managed seats bind to canonical sprint, master, or leaf task documents
plus role. `dispatch_agent` is the one structural child transaction: the control plane authorizes
the relationship, creates the child, proves readiness, persists the initial brief, and returns only
structural delivery state. Models never handle occupant, lifecycle, readiness, inbox-address, or
attachment identifiers.

### Conventions

Edit the canonical skill and run the sync process; never hand-author independent packaged doctrine.
Role files remain self-contained and the shared frame stays limited to routing, lifecycle signals,
and cross-role invariants.

### Invariants And Boundaries

- This artifact must remain byte-identical to the canonical lifecycle SKILL.
- Task-document-plus-role is seat identity; runtime occupant identity stays plane-private.
- A queued structural dispatch is durable and follows the notifier retry path without duplicate
  briefs or respawn.
- Installed runtimes receive the same doctrine as the canonical tree, not a compatibility variant.

### Todos

None recorded.

## Docs References

No external domain documentation is configured for this repository-local lifecycle doctrine.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The packaged source carries the launcher, approval-gated strategist, architect-custody, and parallel-by-default invariants. | `# l-01-agent-lifecycles — The Agent Lifecycles`; `## Which Lifecycle Am I? (the router — exactly three conditions, in order)`; `## The Role Registry` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:6-416 |
| Canonical skills are propagated into package data and harness mirrors by the sync script. | `CANONICAL_SKILLS`; `sync_targets` | scripts/sync-skills.py:15-15; scripts/sync-skills.py:195-203 |

## Cross-Repo References

No sibling repository evidence is needed for this doctrine file.

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

## 260713-TES-L5 Current Delta — Fact-Relay Supervision Doctrine (synced copy)

This synced runtime copy now teaches the fact-relay supervision model: the agent-notifier
sweep evaluates seat-state facts on its mechanical tick and relays them to owners
(turn-ended/completed state-signals, compound-idle, non-reaction residue); the timed
escalation ladder (renudge → skip-level → architect custody, then respawn) is retired, and no
role watches or nudges on its own initiative.

## L23 Dispatch Admission

Packaged lifecycle dispatch now resolves task-derived source lineage before
process creation. Managers require current super-to-master ancestry;
worker/reviewer/curator seats require the full code/external-memory chain. A
lineage refusal creates no child and is recovered by the ordered contract path,
never by asking an agent for branch or occupant ids.

## L23 Final Candidate Disposition

The packaged lifecycle roof now treats current task-derived lineage, exact-candidate independent
route review, and Dagger-only acceptance as shared lifecycle signals. Roles observe task-addressed
durable operations; they never carry private job or commit identifiers between turns.

## Update History
- 2026-08-14T06:32+02:00 — L23 synchronized runtime doctrine: the lifecycle roof carries
  Dagger-only acceptance, manager lineage preflight, and candidate-bound independent route review
  before curation or lifecycle exit. Verification remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented lineage admission in the packaged dispatch sequence; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `SKILL.md` as the exact synchronized runtime artifact of its current canonical document/role contract; removed obsolete leaf-key and runtime-id ownership implications.
- 2026-08-10T04:39+02:00 — 260713-TES-L6: recorded sprint-qualified command-seat dispatch and the
  all-subordinate liveness contract in the packaged lifecycle skill. Verification metadata remains
  pinned until closeout stamps the code commit.

- 2026-08-09T13:59+02:00 — 260713-TES-L5 curator completion round 2: refreshed this synced
  runtime copy for the judgment-demolition doctrine (fact-relay supervision; ladder retired);
  verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

"- 2026-08-02T16:46+02:00 — 260731-EFA-L6 curator W1-B03: repaired 2 citation rows with exact anchors and source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: removed a leaked diff marker. A body section (heading plus paragraph) had been pasted into this Update History list on 260712-TRH-L4 carrying the diff's `+`. Because `+##` has no space after the plus, markdown rendered it as literal text, so the heading was not a heading and the surrounding bullet list was broken. The same section already existed correctly earlier in the file; where the pasted copy said more, its wording was promoted into that section before the paste was deleted. No claim changed. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-15T23:16+02:00 — 260714-ACPUI-L2 curator: documented the synchronized dynamic
  model-gated launch doctrine, complete role examples, native per-harness launch channels,
  provenance-only spawn env, and the no-normalized-paste boundary; final-audited the nearest MCP
  governing overview backlink. Verification metadata remains pinned until closeout stamps the L2
  code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-10T15:48+02:00 — 260707-HFX2-L17 generated-runtime doctrine delta: documented
  task-seat identity as `(qualified leaf key, seat role)`, made developer-declared takeover pass
  and verify the claimed role with the qualified leaf, and recorded same-pair-only live collision.
  Sync-propagated bundle copy; verification metadata remains pinned until closeout stamps the L17
  commit.

- 2026-07-10T02:39+02:00 — HFX3/L14 combined curation: reconciled the free-chat launcher,
  settings-owned architect spawn, propose-first strategist approval, sanctioned-skip Job O path,
  architect terminal custody, and dependency-graph parallel-by-default invariant. Added the
  governing overview and required reference/boundary sections. Verification metadata remains
  pinned until closeout stamps the eventual two-parent code commit.

- 2026-07-09T12:04+02:00 — 260707-HFX2-L10 (spawn settings authority): the lifecycle skill spine now
  states that ordinary spawned seats use settings as the spend surface, with role/level declared on
  `spawn_agent_session`; legacy caller spend fields and maintained harness-native spend/env keys
  refuse with `spend-override-unsupported`. Sync-propagated bundle copy of the canonical skill.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L10 commit.

- 2026-07-08T23:59+02:00 — 260707-HFX2-L5 (doctrine rewrite, active vigilance → passive
  process-and-ack): Shared Invariants section gains the new "Notify-and-stop is safe by design"
  paragraph — ending a turn once the artifact is written is never a liveness gap because the
  HFX2-L2 sweep + HFX2-L4 escalation ladder supervise silence; states the watcher ban
  (uniform-mechanism ruling 2026-07-07) and the passive-duty inversion every role file now carries.
  Doctrine-only change set (5 canonical `skills/` files, propagated by `scripts/sync-skills.py` to 9
  downstream package copies, 0 Python); sync-propagated bundle copy of the canonical
  `skills/l-01-agent-lifecycles/SKILL.md`. Verification metadata pinned until closeout stamps the
  260707-HFX2-L5 commit.

- 2026-07-08T15:45+02:00 — 260707-HFX2-L7 doctrine refinement: Developer Clarification Triage now
  explicitly reads the active queue before choosing note-only handling; a small clarification that
  plainly fits the same task/current diff is a strong immediate-implementation signal, true future
  queue is recorded durably, and unclear fit asks the developer directly. Sync-propagated bundle
  copy of the canonical `skills/l-01-agent-lifecycles/SKILL.md`.

- 2026-07-08T15:27+02:00 — 260707-HFX2-L6 (task-seat takeover + delegated authority
  doctrine): added Developer-Declared Task-Seat Takeover, Developer Clarification Triage, and
  Delegated Series Authority sections to the lifecycle router. A developer-declared role takeover
  anchors on the named task leaf and verifies dashboard terminal attachment before lifecycle work.
  Close/current/small developer clarifications that fit the active leaf are implemented now rather
  than filed as future notes. Accepted orchestrated series authority lets owning seats close out,
  integrate, finalize, and clean up subordinate edges without repeated developer formality, while
  final super/PR-carryover, raised human-pinned gates, scope changes, red checks outside scope, and
  quo-vadis decisions remain developer stops. Doctrine-only change set propagated by
  `scripts/sync-skills.py`; no runtime attachment path changed. Verification metadata pinned until
  closeout stamps the 260707-HFX2-L6 commit.

- 2026-07-08T02:10+02:00 — 260707-HFX-L11 curator activation: Companion Files template registry
  gains `curator-brief` (new file, R1/R4) with its header-consistent description. Doctrine-only
  change set (7 canonical `skills/` files across 6 edits + 1 new template, synced to 9 mirrors, 0
  Python touched); sync-propagated bundle copy of the canonical `skills/l-01-agent-lifecycles/SKILL.md`.
  Verification metadata pinned — no commit yet on `ar/260707-hfx-l11-curator-activation`
  (working-tree change, synced onto the landed HFX-L7 base).

- 2026-07-08T01:00+02:00 — 260707-HFX-L7 (provider degradation protocol): the role registry table
  gains the `system-specialist` row (backend provider-degradation investigator; spawn value
  `system-specialist`; points at the new `roles/system-specialist.md`); frontmatter `description`
  and the Companion Files sentence both now say nine role lifecycles (was eight); the escalation
  ladder bullet gains a standalone `system-specialist -> orchestrator` clause beside the existing
  worker->manager->orchestrator->architect->developer chain; the settings-block worked example
  gains a `system-specialist` roles entry (`claude`/`fable`/`high`). Sync-propagated bundle copy of
  the canonical `skills/l-01-agent-lifecycles/SKILL.md`. Verification metadata pinned until
  closeout stamps the HFX-L7 commit.
- 2026-07-07T21:40+02:00 — 260707-HFX-L6R3 curator seat: added curator to the
  l-01 registry/settings example as the fresh per-leaf onboarding writer, and recorded the
  manager -> builder -> reviewer -> curator closeout chain. Sync-propagated bundle copy.
  Verification metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: added the
  architect role to the registry and router; condition 3 now routes developer-facing sessions
  to `roles/architect.md`; condition 2 is fresh-session role briefs only; the orchestrator is
  a spawned backend seat; escalation is worker -> manager -> orchestrator -> architect ->
  developer; dashboard-owned role-seat immutability and the minimal one-at-a-time decision-item
  relay over the existing operator inbox are doctrine. Sync-propagated bundle copy. Verification
  metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): the settings.json Orchestration
  Block example gains the `strategist` free-form row (`effort: ultracode` + `promptKeywords`), the
  `reviewer` economics row, and the `rolesPerLevel` block; the roles comment names the three-layer
  knob model (validated harness/model/effort · free-form launchArgs/promptKeywords/sessionCommands);
  the as-built paragraph becomes L13+L16 — the knob chain now APPLIES at the harness boundary
  (per-harness argv mapping via the effective registry, dispatch-time effort refusal, the session
  vehicle for `ultracode`, the `level` dispatch input with provenance, `orchestration.harnesses`
  openness) with `docs/reference/harnesses.md` as the manual. Sync-propagated bundle copy of the
  canonical skill. Verification metadata pinned until closeout stamps the L16 commit.

- 2026-07-06T22:56+02:00 — 260703-L13 (settings unification): the settings.json
  Orchestration Block section re-homes the knobs to the global agentic settings file with
  repo-local override (fixing the authority-file contradiction), the example uses registry
  harness ids and gains `orchestration.spawn`, and the as-built paragraph documents the
  kernel loader (per-use reads, fail-loud family), the boot-snapshot gateDelegation with
  legacy fallback, and the spawn resolution chain. Sync-propagated bundle copy of the
  canonical `skills/l-01-agent-lifecycles/SKILL.md`. Verification metadata pinned until
  closeout stamps the L13 commit.

- 2026-07-06T17:35+02:00 — 260703-L12 round 2 (L12R-4 ripple): the loop home's direct-tier gloss now names the level's ordinary build channel (hands-on at session scale; the leaf's worker under a manager) instead of the ambiguous "owner implements". Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T15:35+02:00 — 260703-L12 (three-party loops): the strategist joins the role registry (spawn-first, mandatory pre-run, spawn value `strategist`); a new The Three-Party Loop section becomes the loop doctrine's single home (tiers · 3-full-round cap · delta-verify/builder-resume · convergence rule · quo-vadis · criteria catalogs · per-level agent sets); Companion Files list 10 templates + the `criteria/` catalogs; the settings paragraph documents `orchestration.loops`. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-05T19:55+02:00 - L8 builder cycle 7: Companion Files template registry gains the manager-brief row — all 9 on-disk templates listed (AR4-5). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): the takeover pointer names the real section (Profile check (takeover), The Event Loop). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:20+02:00 - L8 seam-ruling remediation (cycle 4): router edge cases written; six signals enumerated; variant rung removed; at-seams flag documented as wired. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:40+02:00 - L8 de-harnessing pass: per-harness variant layer removed from the resolution order; registry overlay mentions dropped. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:15+02:00 - L8 orchestrator routes rework: registry row marks the designer as a hat the orchestrator pulls (separate chair optional); router condition 1 notes AR_SPAWN_ROLE=designer as the same hat in another chair; router condition 3 states solo = the three jobs with hats collapsed, task doc first. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: SKILL.md is now the unified-skill spine (router + minimal frame + shared invariants); body rewritten accordingly; supersedes the two retired skill spines. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T13:16+02:00 — 260703-L6 documented the adversarial seam procedures end to end: manager
  spawn at master-exit, orchestrator spawn at super-exit, `notes/reports/` verdict placement,
  `reviewer-verdict` gate evidence refs, policy-required verdict evidence, and block-to-fix-leaf routing
  back to the owning manager/orchestrator. Verification metadata pinned until closeout stamps the L6
  commit.
- 2026-07-04T13:03+02:00 — 260703-L5 expanded the frame's super integration branch topology from a
  summary into doctrine: super branches from main, masters branch from super, leaves branch from their
  master, C-11 is universal at every edge, dependent managers dispatch only after dependencies
  integrate into super, independent masters reconcile a moved super base, master-to-super integration
  runs in an orchestrator worktree, conflict resolution is either up-front foundation-master extraction
  or post-hoc super-worktree dedup with memory single-siding, leaf moves carry decision-log entries,
  and the final super-to-main PR includes main-memory carry-over plus push. Also recorded the
  260630-derived master finalize/archive and parallel-master reconcile items as sequenced follow-ups,
  not implemented behavior. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-07-04T11:00+02:00 — Created file-level onboarding for the new `l-02-agent-orchestration` skill
  (leaf 260703-L1), the developer-invoked, never-self-spawning frame that houses the five
  orchestration-family jobs via the four thin contact points (context → job selection → housed job
  execution → wrap-up). Captured the frame doctrine, the job registry, the coordination-leaf
  convention, the escalation ladder + orchestrator-only spirit test, the two adversarial seams, the
  gate-delegation doctrine (enforcement deferred to L4), the knob block + per-harness variant
  resolution, the settings.json orchestration schema block (schema doc only; parsing deferred to L4),
  the super integration branch topology summary (full topology owned by L5), the comms protocol
  (substrate implemented in L3), and the credits; noted `spawn_agent_session` is the L2 tool (not yet
  implemented). Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
  `skills/l-02-agent-orchestration/SKILL.md`. Verification metadata pinned until closeout stamps the L1
  commit.
