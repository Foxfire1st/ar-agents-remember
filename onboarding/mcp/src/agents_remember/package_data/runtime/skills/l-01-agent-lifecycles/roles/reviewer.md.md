# l-01-agent-lifecycles/roles/reviewer.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

This is the packaged runtime artifact synchronized exactly from canonical
`skills/l-01-agent-lifecycles/roles/reviewer.md`: the portable **adversarial reviewer** lifecycle the
corpus houses at the requested review seams. The central doctrine the card must protect is unchanged:
**verdicts are evidence, not decisions**, a **blocking verdict must decompose into fix leaves**, and the
reviewer uses different rubrics at master-exit and super-exit because those seams review different
accumulated change sets.

The packaged role is now a **self-contained lifecycle in the corpus's readable order** — purpose and
authority → required inputs → normal workflow → permitted writes and actions → stop and escalation
cases → completion and handoff, then its machine-readable knob block. It declares its shared sources
with `**Inherits:**` rather than restating them (`core/authority.md`, `core/invariants.md`,
`core/loop.md`, `core/acceptance.md`, `operations/orientation.md`, `operations/review.md`). The exact
mode contract — what a `reviewMode=baseline` seals, what a successor may verify, how the verdict is
recorded and consumed — now lives once in `operations/review.md`; the loop doctrine, tiers, and
three-round convergence rule live once in `core/loop.md`; and per-ID adjudication with completion truth
lives once in `core/acceptance.md`.

Attitude is now stated as a seam binding: the reviewer binds the exact leaf, master, or sprint document
its seam adjudicates, and an atomic child leaf receives **no** separate route-review verdict — that
review is checked on the canonical master at master-to-parent integration. Review itself is **opt-in and
explicit**: it runs only when the developer or the approved task/role brief requests it, and closeout and
integration neither require nor launch it. Independence requires **another agent**; the reviewing seat is
never the author/implementer seat.

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

The synchronized caller matrix keeps reviewer target-only while making ownership seam-specific:
the manager dispatches leaf and master-exit reviewers, the architect dispatches the sprint plan
reviewer, and the orchestrator dispatches the sprint super-exit reviewer. Each generation carries
that plane-stamped structural parent. An identity-free launcher may target an altitude-valid
reviewer only for explicit takeover; an ambient sprint reviewer cannot invent architect versus
orchestrator parentage. Dispatch/tools rows remain structural documentation, not settings keys.

The synchronized reviewer independently validates the exact lightweight worker record and frozen
expanded-evidence digest/anchor while treating internal protocol events as supporting history, not
formal attempts to adjudicate.

The body defines one short-lived reviewer role across leaf code/full-loop review, master exit,
portfolio-plan review, and super exit. Its exact task document fixes the review altitude and its
generation parent fixes the reporting plane. The lens is refute-or-confirm over the seam diff, task
documents, and bound rubric, with a verdict artifact rather than a decision.

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
prose-only** — if it cannot be named as fix leaves it is not yet a block. Leaf-level review is an
independent reviewer seam owned and dispatched by the manager. The reviewer does not escalate; an
un-reviewable change set (missing diff/task docs) is itself a **blocking finding** in the verdict, routed
to the decider. Findings adopt the refute-or-confirm posture — one that cannot survive an attempt to
refute it is not a finding.

**The declared knowledge effects (260928-MIK-L11, MIK-R11 rule 2).** Process step 7, where each requirement
revision is adjudicated, now ends with one line: when the leaf's task document declares
`expectedKnowledgeEffects`, the reviewer checks that declaration against the leaf's requirement packet —
its declared subjects and effects match what the packet requires, with no effect missing and none invented
— and a mismatch is a finding. The architect ruled the line in (ruling Q3, 2026-09-29T21:56:18+02:00); it
sits in the role file rather than a criteria catalog because the catalogs admit a standing criterion only
with catching evidence. The package copy is synced from `skills/` with the eight harness copies
(`scripts/sync-skills.py`).

### Todos

No task-independent TODO is declared by this job file.


## CCR-R12@v5 Transaction Boundary

This role card follows the transaction-only lifecycle boundary: the role reports its own targeted or scoped evidence with failed and not-run states visible and leaves closeout/integration to the authorized code, memory-content, and ledger Git transaction. Full code quality, full tests, certification, and independent review are explicit operations only; curation is the exception — the curator always runs the complete memory-quality operation, and closeout and integration carry its completed result as a prerequisite rather than rerunning it. Requested reviews retain the sealed finding list and monotonic three-round limit.

### Docs References

No external domain documentation applies to this repository-local orchestration job file.

No relevant external documentation found.

## Evidence

### Repo-Internal References

The reviewer job file is its own source authority for the seat, lenses, seams, duties, and knobs.

- A leaf's declared knowledge effects are checked against its packet; a mismatch is a finding (MIK-R11). [1]
- The reviewer is short-lived and self-contained. [2]
- The reviewer receives the brief as its session start. [3]
- Dashboard-owned sessions keep this seat's role fixed for the session lifetime. [4]
- A pasted brief for another role is refused and reported through the inbox. [5]
- Review retrieval is refute-or-confirm, and findings must survive attempted refutation. [6]
- Review criteria are not made up on the spot. [7]
- A first review runs the standing catalogs its review type binds. [8]
- The exploratory mandate defaults to two lenses. [9]
- The completion lens accounts for every master requirement, leaf, substep, and accepted blank-fill. [10]
- Skipped or reshaped work has a decision-log trail. [11]
- No unfinished leaf work is hidden inside the handover packet. [12]
- The scoped-implementation lens checks the builder's targeted tests and the repository-prescribed lint, formatting, typing and structural checks. [13]
- The onboarding-vs-code lens diffs sidecars and route overviews against as-landed code and rejects history-only refreshes. [14]
- Route overviews are among the memory surfaces the onboarding-vs-code lens diffs against as-landed code. [15]
- The reviewer's evidence reports the affected-sidecar and route-overview checks; full suites and `drift_check` run only on an explicit developer request, and the complete `memory_quality_check` is the curator's own operation. [16]
- A master-exit block returns to the owning manager as fix leaves. [17]
- A super-exit block returns to the orchestrator as fix leaves. [18]
- Reviewer duties include writing the verdict artifact and returning a baseline block as decomposable fix leaves. [19]
- Reviewer communications use `message_parent` for missing context or structural routing problems without carrying the parent's runtime identity. [20]
- The verdict artifact and terminal/finalizer truth are the completion signal; the reviewer does not author a duplicate completion row. [21]
- The seat is not driven by a host input stream; it is woken with its pending signals. [22]
- The role's tools are the review surface. [23]
- The role declares the readable order — Inputs, Process, Outputs — with no inherited-sources line and no operator-knob block. [24]
- The exact baseline / fix-verification mode contract has one home outside the role file. [25]
- The role keeps the two seam rubrics and the three review lenses. [26]
- The reviewer names `roles/manager.md` only to return fix leaves to the seat it reports to, which is this role's one sanctioned sibling reference. It appears in the role's own description at `:3`. [27]

### Cross-Repo References

No sibling repository evidence is needed for this orchestration job file.

No meaningful cross-repo references found.

## 260915-CAPS-L1 Citation Rebase (read this before the preserved sections below)

The rewrite of `roles/reviewer.md` kept its rule set but changed every heading and sentence the older
citation rows pointed at, so **21 rows whose anchor strings no longer resolve were removed** rather than
repointed to a lookalike. Their claims are still true of the current file; read them through these
current anchors:

| Former claim | Current anchor |
| --- | --- |
| Short-lived, self-contained seat; brief is its session start; dashboard-owned sessions stay reviewer and refuse a pasted brief | `## 1 — Purpose And Authority` — `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:15-59` |
| Refute-or-confirm posture; criteria are not made up on the spot; the baseline runs its type's standing catalog with the exploratory mandate | `## 3 — Normal Workflow` — `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:100-139` |
| The three lenses (completion, code quality, onboarding-vs-code) and the two seam rubrics | `## 3 — Normal Workflow`; `### MASTER-EXIT …`; `### SUPER-EXIT …` — `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:100-139`, `:184-199`, `:200-215` |
| Fix leaves return to the owning manager (master-exit) or the orchestrator (super-exit) | `### MASTER-EXIT …`; `### SUPER-EXIT …` — `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:195-195`, `:210-210` |
| The verdict artifact is the completion signal and the seat authors no duplicate completion row | `## 6 — Completion And Handoff` — `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:216-233` |
| Communications use structural parent messaging, not a runtime address; stdin is not a work driver | `## Knobs, Tool Surface, And Dispatch Authority` — `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:234-251` |

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.

## 260815-DAG-L2 Candidate And Repair Scope

Organizational master-exit review covers the exact proposed final super candidate before its full
gate and landing; atomic review covers the isolated branch. Plan-review verdicts return to the
architect. Super-exit blocks decompose to owning/reopened or new scoped leaves and may not authorize
repair directly on super.

## 260815-DAG-L15 Review-Doctrine

The seat gains a "Review Independence and Evidence-Type Matching" section: the reviewer seat is
never the author seat — a self-review is returned to the decider as a verdict-laundering finding
(260815-DAG L7/L8/L9 route reviews were orchestrator self-reviews). Every requirement verdict must
cite evidence of the requirement's class: rendering → mounted-UI proof, scheduling →
operation-level proof, data model → artifact-level proof, doctrine → a code anchor (D-1). Evidence
of the wrong class is a finding, never a pass (L8-R3 was passed on projection-only evidence).

## M38 Reviewer Adjudication Projection

The installed reviewer role independently inspects every cited artifact and gives each stable ID
its own `accepted` or `rejected` rationale. Missing rationale, missing or wrong-class evidence,
invalid citations, or missing durable approval forces rejection, and any rejection prevents the
overall pass. Delta rounds retain accepted rows unless the repair directly regresses them. This
copy is synchronized doctrine, not an independent review policy.
Canonical-packet inspection includes the version-addressed path, exact ID/version, approved state,
and durable corpus ruling; task prose cannot substitute for that source.

## M41-M43 Reviewer Attempt Projection

The packaged reviewer appends a separate record against one exact worker attempt and candidate,
classifies rejection, and may prove regression without unilaterally reopening acceptance or
extending scope. Bounded invalidation remains an owning-seat record.

## 2026-08-27 Attempt Boundary Clarification

This packaged projection preserves the canonical phase boundary: validate before append; a
malformed never-handed-off row receives a non-attempt correction/void without consuming an ID;
a malformed handed-off attempt requires independent rejection before successor handoff.
