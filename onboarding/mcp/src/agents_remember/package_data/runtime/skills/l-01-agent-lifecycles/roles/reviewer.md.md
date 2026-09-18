# l-01-agent-lifecycles/roles/reviewer.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675`|
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview | `../../../../../../../overview.md` |

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

### Todos

No task-independent TODO is declared by this job file.


## CCR-R12@v5 Transaction Boundary

This role card follows the transaction-only lifecycle boundary: the role reports its own targeted or scoped evidence with failed and not-run states visible and leaves closeout/integration to the authorized code, memory-content, and ledger Git transaction. Full code quality, full tests, certification, and independent review are explicit operations only; curation is the exception — the curator always runs the complete memory-quality operation, and closeout and integration carry its completed result as a prerequisite rather than rerunning it. Requested reviews retain the sealed finding list and monotonic three-round limit.

### Docs References

No external domain documentation applies to this repository-local orchestration job file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The reviewer job file is its own source authority for the seat, lenses, seams, duties, and knobs.

| Finding | Anchor | Source |
| --- | --- | --- |
| The role declares the readable order — Inputs, Process, Outputs — with no inherited-sources line and no operator-knob block. | `## Inputs`; `## Process`; `## Outputs` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:12-12; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:48-48; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:83-83 |
| The exact baseline / fix-verification mode contract has one home outside the role file. | `# Operation — Review`; `## Required inputs` | skills/l-01-agent-lifecycles/operations/review.md:1-1; skills/l-01-agent-lifecycles/operations/review.md:22-34 |
| The role keeps the two seam rubrics and the three review lenses. | "all three lenses (completion against task docs · scoped implementation evidence · onboarding against code)"; "Master-exit (before manager → orchestrator handover)."; "Super-exit (before orchestrator → architect handover)." | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:56-57; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:101-101; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:113-113 |
| The reviewer names `roles/manager.md` only to return fix leaves to the seat it reports to, which is this role's one sanctioned sibling reference. It appears in the role's own description at `:3`. | `SANCTIONED_SIBLING_REFERENCES`; `description:` | mcp/tests/test_role_instruction_corpus.py:114-116; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:3-3 |

## Cross-Repo References

No sibling repository evidence is needed for this orchestration job file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

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

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T05:26:45+00:00: Generated citation repair: `SANCTIONED_SIBLING_REFERENCES` repointed to mcp/tests/test_role_instruction_corpus.py:114-116. No content impact: mechanical anchor-range projection bound to citation source snapshot 70078cc4ca208e40e9a66742bdc38893ecfb1757ca7d77a526e6ba2159339959; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: **complete curation inverts the doctrine this card recorded.** CAPS-R18@v1 removes the optional/narrow-curation sentences from the shipped instruction corpus and states the rule normatively — the full `memory_quality_check` operation runs as part of every leaf's curation at its contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every curator-actionable finding is repaired or escalated as blocked with its exact returned code, and closeout and integration **carry** the completed curation as a prerequisite while invoking nothing. Replaced the CCR-R12@v5 transaction-boundary boilerplate sentence, which still presented full memory quality as an explicit request, and updated the role's own curation sentences to the complete-handoff rule. Hand-repaired one citation finding this leaf's own source edit drifted (D14): the `SANCTIONED_SIBLING_REFERENCES` range to the test module's current :110.
- 2026-09-16T20:45+02:00 — owning-seat merge resolution (source-line convergence): the
  `governingOverview` field and its link were restored to `../../../../../../../overview.md`.
  The 2026-09-16T08:01 metadata repair above dropped one path level — this card sits one directory
  below the skill's `SKILL.md` card, so the target it names (the MCP package overview,
  `onboarding/mcp/overview.md`) needs seven levels up, not five. The five-level value resolved to
  `onboarding/mcp/src/agents_remember/overview.md`, which does not exist, so the card pointed at a
  missing file while its own text claimed the MCP package overview. No content claim changed; only
  the path. Verification metadata is unchanged and stays closeout-owned.
- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: **body updated for the corpus consolidation.**
  The canonical reviewer role was rewritten (251 lines) into the corpus's readable order and declares
  its inherited sources with `**Inherits:**`. Updated Purpose into the packaged-synchronized framing:
  readable order, inherited sources, where the mode contract and loop doctrine now live, the seam
  bindings (leaf/master/sprint; atomic children defer to the canonical master), and the explicit opt-in
  nature of review. Repo-Internal References: **22 rows whose anchor strings no longer resolve in the
  rewritten source were removed** (the file kept its rule set but none of those literal anchor strings),
  and three current rows plus a `SANCTIONED_SIBLING_REFERENCES` row were added. The preserved
  task-delta sections below still describe rules in force at their new homes in `operations/review.md`
  and `core/acceptance.md`. **Metadata repair:** `governingOverview` was absent from this card (the c-05 content model requires the field and its `## Governing Overview` section); added as `../../../../../overview.md`, the `onboarding/mcp/overview.md` route-local overview that governs this generated tree. Verification metadata remains closeout-owned — the source is uncommitted, so no stamp was advanced and no commit hash invented.

- 2026-09-10T09:50+02:00 — CCR-R12@v5 transaction-only curation against code commit `4bbe2c37b0fa70b07af4ddbc247aeee1f58343b0`: re-read the three lens rows against the rewritten criteria text; the code-quality and onboarding-vs-code anchors now name the sentences the lenses actually carry. Verification metadata remains closeout-owned.

- 2026-09-10T07:41:10+00:00: Generated citation repair: "stays reviewer" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:51-51. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "role is refused and reported" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:52-52. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "findings must survive an attempt to refute them" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:102-102. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "Criteria are never made up on the spot." repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:109-109. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "plus an **exploratory mandate**"; "default 2" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:110-110; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:111-111. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "every master requirement"; "accounted for" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:263-263; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:264-264. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "skipped or reshaped work has a decision-log trail" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:264-264. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "no unfinished leaf work is hidden"; "inside the handover packet" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:264-264; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:265-265. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "route overviews are current" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:271-271. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "returns to the owning **manager**" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:274-274. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "Structural parent message" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:365-365. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "The verdict artifact plus terminal/finalizer truth is the completion" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:366-366. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "Stdin push" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:368-368. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "review surface" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:384-384. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "stays reviewer" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:50-50. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "role is refused and reported" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:51-51. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "findings must survive an attempt to refute them" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:101-101. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "Criteria are never made up on the spot." repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:108-108. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "plus an **exploratory mandate**"; "default 2" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:109-109; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:110-110. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "every master requirement"; "accounted for" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:264-264; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:265-265. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "skipped or reshaped work has a decision-log trail" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:265-265. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "no unfinished leaf work is hidden"; "inside the handover packet" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:265-265; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:266-266. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "lint · typecheck · tests · complexity" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:227-227. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "changed source files have same-pass sidecar updates" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:272-272. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "route overviews are current" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:273-273. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "any memory/carry-over gap is named" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:274-274. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "returns to the owning **manager**" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:275-275. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "returns to the **orchestrator**" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:299-299. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "Structural parent message" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:364-364. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "The verdict artifact plus terminal/finalizer truth is the completion" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:365-365. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "Stdin push" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:367-367. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "review surface" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:383-383. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: reconciled the packaged
  reviewer card to leaf/master/plan/super contexts, plane-stamped parent ownership, and independent
  leaf review. Verification remains closeout-owned.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 synchronized manager-only reviewer dispatch,
  explicit ambient takeover, and fixed structural-row ownership. Verification remains
  closeout-owned.

- 2026-08-28T14:18+02:00 — Reconciled reviewer-doctrine citations with the committed PDLS
  candidate after the acceptance-envelope wording settled; the contract is unchanged.

- 2026-08-28T11:32+02:00 — No content impact: synchronized projection payload changed with the
  canonical one-primary requirement doctrine; projection ownership and byte-identity rules remain
  unchanged.

- 2026-08-27T22:15+02:00 — Synchronized the pre-handoff correction versus post-handoff rejection
  contract from canonical lifecycle/task doctrine.

- 2026-08-27T21:53+02:00 — Synchronized M40@v2/M44@v2 reviewer evidence boundaries.

- 2026-08-27T18:06+02:00 — M41-M43: synchronized exact-attempt adjudication, failure classes, and
  regression-proof/owner-invalidation separation.

- 2026-08-27T14:04+02:00 — Tightened installed reviewer adjudication around the approved
  version-addressed packet and its packet-local durable corpus ruling.
- 2026-08-27T13:32+02:00 — M39@v1: reviewers inspect the matching canonical packet and reject
  missing, mismatched, or superseded requirement versions; affected leaves must be rebriefed before
  new acceptance. Verification remains closeout-owned.

- 2026-08-27T12:43+02:00 — M38: recorded independent per-ID adjudication and forcing rejection
  rules. Verification metadata stays pinned until governed closeout stamps the PDLS commit.


- 2026-08-20T21:30+02:00 — 260815-DAG-L15: the seat gains the Review Independence and
  Evidence-Type Matching section — never the author seat, and requirement verdicts must cite their
  evidence class (mounted-UI / operation-level / artifact-level / code anchor). Verified at code
  commit de3a0fd9.
- 2026-08-15T04:32+02:00 — 260815-DAG-L2: synchronized nature-aware review scope, architect plan
  ownership, and leaf-only repair routing. Verification remains closeout-owned.
- 2026-08-14T06:32+02:00 — L23 synchronized runtime doctrine: independent reviewers bind verdicts
  to the exact candidate and major ownership route, with same-reviewer delta verification after
  repair. Verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Recorded `reviewer.md` as a synchronized runtime artifact of the current canonical lifecycle doctrine; it introduces no independent role contract.
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
