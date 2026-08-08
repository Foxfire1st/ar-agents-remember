# l-01-agent-lifecycles/roles/reviewer.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T17:40+02:00 |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af` |
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|

## Purpose

This is the portable **adversarial reviewer** job file the `l-01-agent-lifecycles` frame houses at the
review seams. Like every job file it carries **both axes in one file** — the **role** (review the
accumulated change set at a seam) and the **lens** (refute-or-confirm across three review lenses) — plus
an opening move, duties, artifact obligations, a comms protocol, and a harness-agnostic knob block. The
central doctrine the card must protect: **verdicts are evidence, not decisions**, a **blocking verdict
must decompose into fix leaves**, and the reviewer uses different rubrics at master-exit and
super-exit because those seams review different accumulated change sets.

## Code Commentary

### Coding-Guidelines Lens (260731-EFA-L16)

The second review lens (code quality) now spans guideline adherence beside the `system/tools.md`
suite: the change set's added lines are read against the memory layer's
`system/coding-guidelines.md` — budgets, responsibility/anti-pattern rules, source-comment scope,
DTO rules, D1/D2/D3 — because the wrapper proves none of it. This is the chain's only
**independent** read for adherence: the worker self-writes against the guidelines (its Orient
step), and the manager's c-12 closeout relays named findings, but the reviewer verdict is where
adherence stops being self-attestation.

### Logic

The body defines a short-lived reviewer seat at the master-exit and super-exit seams, plus the
reusable reviewer seat for full-loop and portfolio-plan reviews. Master-exit hands the accumulated
master branch to the orchestrator; super-exit hands the accumulated super branch to the architect for
developer review; leaf-level review remains the manager's duty. The lens is refute-or-confirm over
the seam diff, task documents, and bound rubric, with a verdict artifact rather than a decision.

The three lenses are completion versus task docs, code quality and regressions, and
onboarding-versus-code. Criteria come from the standing catalog for the review type plus the
exploratory mandate. The seam rubrics cover the relevant accumulated change set, evidence, and
decomposable fix leaves. The role also defines six duties, artifact obligations, inbox communications,
and harness-agnostic knobs; its durable reports and verdict are written under the series report
directory.

### Conventions

Role, lens, criteria, duties, artifacts, communications, and knobs live in one self-contained job file.
The reviewer receives the seam context through the inbox, posts the verdict reference to the decider,
and does not use stdin as a work driver.

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

No task-independent TODO is declared by this job file.

### Docs References

No external domain documentation applies to this repository-local orchestration job file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The reviewer job file is its own source authority for the seat, lenses, seams, duties, and knobs.

| Finding | Anchor | Source |
| --- | --- | --- |
| The reviewer is short-lived and self-contained. | "Short-lived and self-contained" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:3-3 |
| The reviewer receives the brief as its session start. | "Your **brief is your session start**" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:4-4 |
| Dashboard-owned sessions keep this seat reviewer. | "stays reviewer" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:41-41 |
| A pasted brief for another role is refused and reported through the inbox. | "role is refused and reported" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:42-42 |
| Review retrieval is refute-or-confirm, and findings must survive attempted refutation. | "findings must survive an attempt to refute them" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:51-51 |
| Review criteria are not made up on the spot. | "Criteria are never made up on the spot." | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:58-58 |
| Every review runs its type's standing catalog. | "Every review runs its type's STANDING catalog" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:58-58 |
| The exploratory mandate defaults to two lenses. | "plus an **exploratory mandate**"; "default 2" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:59-60 |
| The completion lens accounts for every master requirement, leaf, substep, and accepted blank-fill. | "every master requirement, leaf, substep"; "accounted for" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:104-105 |
| Skipped or reshaped work has a decision-log trail. | "skipped or reshaped work has a decision-log trail" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:105-105 |
| No unfinished leaf work is hidden inside the handover packet. | "no unfinished leaf work is hidden"; "inside the handover packet" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:105-106 |
| The code-quality lens checks lint, typecheck, tests, and complexity. | "lint · typecheck · tests · complexity" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:84-84 |
| The onboarding-vs-code lens checks same-pass sidecars. | "changed source files have same-pass sidecar updates" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:110-110 |
| Route overviews are current for the master side of the change. | "route overviews are current" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:111-111 |
| Onboarding evidence records drift and memory-quality checks and names any memory or carry-over gap. | "any memory/carry-over gap is named" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:112-112 |
| A master-exit block returns to the owning manager as fix leaves. | "returns to the owning **manager**" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:113-113 |
| A super-exit block returns to the orchestrator as fix leaves. | "returns to the **orchestrator**" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:136-136 |
| Reviewer duties include writing a verdict artifact and decomposing blocking verdicts into fix leaves. | "Write the verdict artifact"; "Decompose a blocking verdict into fix leaves" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:148-148; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:155-155 |
| Reviewer communications use the inbox to receive context. | "Inbox" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:172-172 |
| Reviewer communications post the verdict reference to the seam's decider. | "verdict reference" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:173-173 |
| Stdin is not a driver for the reviewer. | "Stdin push" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:174-174 |
| The role's tools are the review surface. | "review surface" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:189-189 |

## Cross-Repo References

No sibling repository evidence is needed for this orchestration job file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.

## Update History
- 2026-08-05T21:55+02:00 — 260731-EFA-L16 curator: recorded the guideline-adherence read added to the second review lens — the chain's only independent adherence verification, ending self-attestation as the sole mechanism (developer ruling after three leaves shipped guideline violations through green rails). Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-04T10:18:21+02:00 — 260731-EFA-L6 S18-B07 split-row reconciliation: bound exploratory, completion, and handover predicates across every source line they require; same-reviewer delta pending.

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
