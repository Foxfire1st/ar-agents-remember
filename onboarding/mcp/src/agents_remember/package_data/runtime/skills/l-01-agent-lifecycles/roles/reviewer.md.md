# l-01-agent-lifecycles/roles/reviewer.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T17:40+02:00 |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77` |
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|

## Purpose

This is the portable **adversarial reviewer** job file the `l-01-agent-lifecycles` frame houses at the
review seams. Like every job file it carries **both axes in one file** — the **role** (review the
accumulated change set at a seam) and the **lens** (refute-or-confirm across three review lenses) — plus
an opening move, duties, artifact obligations, a comms protocol, and a harness-agnostic knob block. The
central doctrine the card must protect: **verdicts are evidence, not decisions**, a **blocking verdict
must decompose into fix leaves**, and the reviewer uses different rubrics at master-exit and
super-exit because those seams review different accumulated change sets.

## Code Commentary

### Logic

L13 review follow-up (L13R-1): the knob table's `harness` example is the registry id `claude` (was the non-id `claude-code`); spawn refuses non-registry values, so examples must model valid input.

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/roles/adversarial-reviewer.md`; it is model-interpreted markdown, never
an executor. The body defines: the seat (**short-lived, spawned at exactly TWO seams** — developer
decision 2026-07-03: **master-exit** before a manager hands its master integration branch to the
orchestrator, and **super-exit** before the orchestrator hands the super integration branch to the
developer; it reviews an **accumulated change set, not a single leaf**); the lens (opening move = scope
the review to the seam's diff · task docs · rubric; retrieval lean = refute-or-confirm, argue *against*
the change set; decide default = a verdict artifact with an explicit pass/block recommendation — never a
decision, never prose-only); the **three review lenses** (1. completion vs task docs; 2. code quality per
`system/tools.md` + regressions **vs the past** via route indexes/cgc/grepai; 3. onboarding-vs-code = the
paired `read_ar_files` + `memory_quality_check` + `drift_check` check); and the seam-specific rubrics.
The **master-exit** rubric reviews the accumulated master integration branch before manager →
orchestrator handover: master/leaf task docs, worker reports, decision logs, the draft handover packet,
resolved tools evidence, changed sidecars, route overviews, and memory/carry-over state. The
**super-exit** rubric reviews wholesale super-branch behavior before orchestrator → developer handover:
the full portfolio docs, master handovers, prior master-exit verdicts, orchestrator decision logs,
branch-wide quality evidence, route/memory coherence, and final ledger/carry-over state. Both rubrics
require refute-or-confirm findings and make any BLOCK invalid unless it names concrete fix leaves. The
file also defines five duties, artifact obligations, the comms protocol, and the knob block. It **fans
out sub-agents that write durable reports** (`templates/impact-analysis.md`,
`templates/onboarding-coherency.md`) backing the verdict (`templates/verdict.md`) under the series
`notes/reports/` directory.

HFX-L6 keeps verdicts as evidence, not decisions, and makes the super-exit handoff
architect/developer mediated: the backend orchestrator hands the reviewable environment and verdict
to the architect before developer review. Reviewer seats also carry role-seat immutability in
dashboard-owned sessions.

### Conventions

Role + lens in one file (D10); a portable knob block (D7, high-reasoning / high-effort — the last line of
defense) resolving job base < variant < `settings.json orchestration.roles.adversarial-reviewer`. Comms
ride the inbox (receive the seam's change-set context, post the verdict reference to the seam's decider);
stdin push is not a driver here — the reviewer is short-lived and reports through its verdict.

### Invariants And Boundaries

**VERDICTS ARE EVIDENCE, NOT DECISIONS.** The reviewer never decides a gate; its verdict attaches to the
handover gate as **judge evidence** and the gate's decider (manager / orchestrator / developer per the L4
policy) decides. A **BLOCKING verdict MUST DECOMPOSE INTO FIX LEAVES** — concrete, leaf-shaped findings
the owning manager (master-exit) or orchestrator (super-exit) can dispatch; a block is **never
prose-only** — if it cannot be named as fix leaves it is not yet a block. **Leaf-level review is the
manager's own duty — NOT an adversarial seam.** The reviewer does not escalate up the ladder; an
un-reviewable change set (missing diff/task docs) is itself a **blocking finding** in the verdict, routed
to the decider. Findings adopt the refute-or-confirm posture — one that cannot survive an attempt to
refute it is not a finding.

### Todos

No `roles/adversarial-reviewer.<harness>.md` overlay ships yet; author one when a harness needs
reviewer-specific knobs. Gate-policy enforcement (the seam-verdict requirement) is documented here but is
**leaf L4**. No other TODO is recorded for this job file.

### Docs References

No external domain documentation applies to this repository-local orchestration job file.

| Finding | Citations | Source Path |
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

The reviewer is spawned at the manager's master-exit seam and the orchestrator's super-exit seam.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | n/a | [adversarial-reviewer.md](agents-remember/skills/l-01-agent-lifecycles/roles/adversarial-reviewer.md) |
| The frame that houses this seat and owns the two adversarial review seams, the gate-delegation doctrine, and the report-template library. | n/a | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md) |
| The manager that spawns the reviewer at master-exit and dispatches its decomposed fix leaves. | n/a | [manager.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md) |
| The orchestrator that spawns the reviewer at super-exit and decides that seam's handover gate. | n/a | [orchestrator.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md) |

As of the L8 de-harnessing pass the overlay-authoring sentence is gone and the knob harness row is a preference settings overrides: no per-harness reviewer files.

As of cycle 4 the file is `roles/reviewer.md` (renamed from adversarial-reviewer.md to match the server role vocabulary and the spawn value `AR_SPAWN_ROLE=reviewer`), and its header states the ruled deciders: the ORCHESTRATOR decides master-exit via the delegable `master-handover-approval` gate kind, the DEVELOPER decides super-exit; `requireReviewerVerdictAtSeams` binds delegated seam decisions to attached verdict evidence.

As of cycle 5: settings key is orchestration.roles.reviewer; the super-exit scope packet says 'against its base (main)' instead of spear jargon; the knob tools row gains the inbox.

As of 260703-L12 the file **binds the criteria catalogs** (a new Criteria Catalogs section before the three lenses): criteria are never made up on the spot — every review runs its type's STANDING catalog from `criteria/` plus an exploratory mandate (default 2 novel lenses), with a binding table (master-exit → code-seam · onboarding-memory · report-verification, + doctrine when doctrine files ride; super-exit → all four wholesale; leaf full-loop → per the change set; plan review → plan-review · report-verification) and the promotion-ratchet duty (surviving novel finding-classes are proposed as catalog amendments IN THE VERDICT, promoted on the loop owner's acceptance). The seat definition extends beyond the two seams — since round 2 (L12R-5) the OPENING sentence itself is count-honest ("spawned at exactly two adversarial seams — and as any three-party loop's reviewer seat"): **the same role file is every three-party loop's reviewer** (developer ruling L12-Q2 — reuse, not a lighter loop-checker), including the portfolio plan review; **delta-verify reuse** is stated as this seat's duty (resumed via follow-up to verify a passing round's landed residuals, appending a delta section to its own verdict; only full rounds count against the loop's 3-round cap). The refute-or-confirm posture is unchanged.

## Cross-Repo References

No sibling repository evidence is needed for this orchestration job file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.


## Update History

- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: removed a leaked diff marker. A body section (heading plus paragraph) had been pasted into this Update History list on 260712-TRH-L4 carrying the diff's `+`. Because `+##` has no space after the plus, markdown rendered it as literal text, so the heading was not a heading and the surrounding bullet list was broken. The same section already existed correctly earlier in the file; where the pasted copy said more, its wording was promoted into that section before the paste was deleted. No claim changed. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: added
  role-seat immutability and adjusted super-exit wording so the backend orchestrator hands
  verdict/demo evidence to the architect for developer review; the reviewer remains evidence,
  never the decider. Sync-propagated bundle copy. Verification metadata pinned until closeout
  stamps the HFX-L6 commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): Knobs table gained the three
  free-form escape-hatch rows (launchArgs / sessionCommands / promptKeywords, settings-only, never
  validated) and the knob footer now includes the rolesPerLevel per-level override and the
  harnesses.md manual pointer. Sync-propagated bundle copy. Verification metadata pinned until
  closeout stamps the L16 commit.

- 2026-07-06T23:45+02:00 — L13 adversarial-review follow-up (L13R-1): knob-table harness example fixed to the registry id `claude`. Verification metadata pinned until closeout stamps the L13 commit.

- 2026-07-06T17:35+02:00 — 260703-L12 round 2 (L12R-5): the What-This-Seat-Is opening sentence made count-honest — two adversarial seams AND the loop-reviewer seat named up front instead of ten lines later. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T15:35+02:00 — 260703-L12 (three-party loops): the criteria catalogs are bound (binding table per review type + promotion-ratchet duty in the verdict); the seat extends to every three-party loop's reviewer (L12-Q2 reuse ruling) incl. the plan review; delta-verify reuse stated (same-instance resume closes rounds; only full rounds count against the cap); refute-or-confirm unchanged. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): settings key is orchestration.roles.reviewer. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:20+02:00 - L8 seam-ruling remediation (cycle 4): renamed to reviewer.md (server vocabulary + spawn value); deciders ruled (orchestrator@master-exit, developer@super-exit); L4-policy shorthand replaced with the as-built citation. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:40+02:00 - L8 de-harnessing pass: overlay-authoring sentence removed (no per-harness files). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: re-homed to roles/ under the unified skill; self-contained header (brief = session start); template references now ../templates/. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T13:16+02:00: 260703-L6 sharpened this reviewer job with separate MASTER-EXIT and
  SUPER-EXIT rubrics, explicit refute-or-confirm evidence-file posture, `notes/reports/` verdict
  placement, and the rule that blocking verdicts decompose into fix leaves for the owning
  manager/orchestrator. Verification metadata pinned until closeout stamps the L6 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` adversarial reviewer job file (leaf 260703-L1) — short-lived at exactly two seams (master-exit, super-exit), the three review lenses, sub-agent durable reports, and the critical doctrine that verdicts are evidence not decisions and a blocking verdict must decompose into fix leaves (leaf-level review being the manager's duty, not a seam). Verification metadata pinned until closeout stamps the L1 commit.
