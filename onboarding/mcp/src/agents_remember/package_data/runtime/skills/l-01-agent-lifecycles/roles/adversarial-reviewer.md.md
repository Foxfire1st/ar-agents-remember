# l-01-agent-lifecycles/roles/adversarial-reviewer.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/adversarial-reviewer.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T01:30+02:00 |
| lastVerifiedCommitHash | `277f27a33b35aed8235cbb3c1ae2b5633cc88b22` |
| lastVerifiedCommitDate | 2026-07-05T01:30:08+02:00|

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

## Repo-Internal References

The reviewer is spawned at the manager's master-exit seam and the orchestrator's super-exit seam.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | n/a | [adversarial-reviewer.md](agents-remember/skills/l-01-agent-lifecycles/roles/adversarial-reviewer.md) |
| The frame that houses this seat and owns the two adversarial review seams, the gate-delegation doctrine, and the report-template library. | n/a | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md) |
| The manager that spawns the reviewer at master-exit and dispatches its decomposed fix leaves. | n/a | [manager.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md) |
| The orchestrator that spawns the reviewer at super-exit and decides that seam's handover gate. | n/a | [orchestrator.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md) |

## Cross-Repo References

No sibling repository evidence is needed for this orchestration job file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: re-homed to roles/ under the unified skill; self-contained header (brief = session start); template references now ../templates/. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T13:16+02:00: 260703-L6 sharpened this reviewer job with separate MASTER-EXIT and
  SUPER-EXIT rubrics, explicit refute-or-confirm evidence-file posture, `notes/reports/` verdict
  placement, and the rule that blocking verdicts decompose into fix leaves for the owning
  manager/orchestrator. Verification metadata pinned until closeout stamps the L6 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` adversarial reviewer job file (leaf 260703-L1) — short-lived at exactly two seams (master-exit, super-exit), the three review lenses, sub-agent durable reports, and the critical doctrine that verdicts are evidence not decisions and a blocking verdict must decompose into fix leaves (leaf-level review being the manager's duty, not a seam). Verification metadata pinned until closeout stamps the L1 commit.
