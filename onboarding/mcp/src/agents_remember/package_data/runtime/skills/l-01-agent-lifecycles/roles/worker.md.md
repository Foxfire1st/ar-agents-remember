# mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634`|
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

This file is the packaged runtime artifact synchronized exactly from canonical
`skills/l-01-agent-lifecycles/roles/worker.md`. It gives installed runtimes the same one-real-leaf
builder lifecycle and owns no independent worker doctrine.

The packaged role is now a **self-contained lifecycle in the corpus's readable order** — purpose and
authority → required inputs → normal workflow → permitted writes and actions → stop and escalation
cases → completion and handoff, then its machine-readable knob block. It declares its shared sources
with `**Inherits:**` instead of restating them (`core/authority.md`, `core/invariants.md`,
`core/lifecycle-frame.md`, `core/acceptance.md`, `operations/orientation.md`,
`operations/implementation.md`, `operations/recovery.md`). The build procedure it used to carry inline
now lives once in `operations/implementation.md`, and the targeted-check contract it owes its owner
lives once in `operations/closeout.md` § The targeted-check contract.

## Code Commentary

### Logic

The synchronized worker is the builder with a **no-commit contract** at leaf altitude: it implements
exactly the leaf plan inside the leaf's code worktree, runs its targeted checks, and writes the turn
report — and it does not commit, land, close out, integrate, decide gates, or write onboarding.

Its acceptance duty is now stated as one envelope per owned primary stable ID + version: `satisfied`,
`blocked`, or `approved-change`, with delivery rationale and citations (code uses file path + symbol;
non-code work uses the deliverable path + section/anchor), verification rationale that names the
failure the evidence would catch, and the exact command and result. Attempt identity is a separate
axis: the worker appends an immutable candidate-bound attempt record to the leaf's requirement attempt
journal before review handoff, and internal test/evidence reruns are logged as experimental protocol
events rather than minting attempts. A malformed row that was never handed off is voided without
consuming an ID; a malformed handed-off row is rejected by the independent reviewer. All of this is
authored once in `core/acceptance.md`, which the role now inherits rather than restating.

A worker that never touches a mutating AR tool never instantiates a lifecycle; where it does mutate,
it runs its own. Escalation is one rung up, and a red targeted check is reported rather than worked
around.

### Conventions

- Change worker doctrine only in canonical `skills/`.
- Propagate and verify through `scripts/sync-skills.py`.
- Keep this file byte-identical while retaining its own path-specific verification metadata.
- Do not append task-local deltas to the packaged artifact card. The corpus's single-source rule is
  the reason: this role states its own seat's side of a shared rule and never restates the whole of
  it.

### Invariants And Boundaries

- Installation cannot grant workers gates, closeout, integration, task-state, or memory authority.
- Worker identity remains canonical leaf document plus role.
- The worker never commits: it leaves the worktree dirty for the owning seat's transaction.
- Durable turn report and terminal/finalizer truth remain the completion evidence — and terminal
  truth attests only that the turn ended, so the owner's validation is what accepts the handoff.
- **This role file names no sibling role file.** The corpus forbids learning one's own obligations
  from another seat's prose; the shipped check fails on any non-sanctioned reference.


## CCR-R12@v5 Transaction Boundary

This role card follows the transaction-only lifecycle boundary: the role reports its own targeted or scoped evidence with failed and not-run states visible and leaves closeout/integration to the authorized code, memory-content, and ledger Git transaction. Full code quality, full tests, certification, and independent review are explicit operations only; curation is the exception — the curator always runs the complete memory-quality operation, and closeout and integration carry its completed result as a prerequisite rather than rerunning it. Requested reviews retain the sealed finding list and monotonic three-round limit.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The packaged worker declares its seat purpose, authority boundary, and no-commit contract. | `## 1 — Purpose And Authority` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md:16-50 |
| The role opens by naming the shared sources it composes with rather than restating them. | "**Inherits:**" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md:12-12 |
| The build procedure the worker follows has one home outside the role file. | `# Operation — Implementation`; `## Handoff / exit` | skills/l-01-agent-lifecycles/operations/implementation.md:1-1; skills/l-01-agent-lifecycles/operations/implementation.md:69-80 |
| The targeted-check contract the worker owes its owner has one home outside the role file. | `## The targeted-check contract (what closeout consumes as evidence)` | skills/l-01-agent-lifecycles/operations/closeout.md:22-42 |
| The role declares the readable order and the knob block after the handoff section. | `## 6 — Completion And Handoff`; `## Knobs, Tool Surface, And Dispatch Authority` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md:146-193 |
| The canonical source owns this doctrine. | `# Lifecycle — Worker` | skills/l-01-agent-lifecycles/roles/worker.md:1-14 |
| A non-sanctioned sibling-role reference fails the shipped corpus check, which is why this role file names none. | `SANCTIONED_SIBLING_REFERENCES` | mcp/tests/test_role_instruction_corpus.py:110-110 |
| MCP package data is copied from canonical skills and checked for drift. | `TARGETS`; `sync_target`; `check_targets` | scripts/sync-skills.py:43-47; scripts/sync-skills.py:136-157; scripts/sync-skills.py:179-203 |

## R39 Generic Worker Checks

Workers copy repository-specific acceptance requirements from the resolved workflow, coding
guidelines, and tools memory; they may not choose a familiar runner. Leaf closeout owns change-set
acceptance, leaf integration does not rerun it, and full acceptance belongs to master integration.

## 260815-DAG-L2 Leaf Quality Altitude

Worker dispatch carries organizational or atomic execution nature and the corresponding source
edge. Each leaf reports its targeted checks before handoff; closeout and integration consume that
evidence as part of the authorized Git transaction without launching a full suite automatically.

## M38 Worker Acceptance Projection

The installed worker role carries the canonical one-block-per-stable-ID envelope: delivery and
verification rationales, independently inspectable citations, exact result evidence, and the extra
developer-ruling fields for blocked or approved-change status. It also makes Checks an explicit
report section and uses deliverable paths plus stable anchors for non-code work. This copy owns no
independent worker behavior.
Intake refuses any packet that is not version-addressed, approved, ID/version-matched, and carrying
its durable corpus-ruling citation.

## M40/M43 Worker Attempt Projection

The packaged worker appends an immutable exact-candidate attempt with predecessor findings,
acceptance envelope, checks, and a closed failure class before handoff. Repairs append successors;
they do not edit history or rewrite requirement semantics.

## 2026-08-27 Attempt Boundary Clarification

This packaged projection preserves the canonical phase boundary: validate before append; a
malformed never-handed-off row receives a non-attempt correction/void without consuming an ID;
a malformed handed-off attempt requires independent rejection before successor handoff.

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `## 6 — Completion And Handoff`; `## Knobs, Tool Surface, And Dispatch Authority` repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md:146-175; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md:176-193. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: **complete curation inverts the doctrine this card recorded.** CAPS-R18@v1 removes the optional/narrow-curation sentences from the shipped instruction corpus and states the rule normatively — the full `memory_quality_check` operation runs as part of every leaf's curation at its contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every curator-actionable finding is repaired or escalated as blocked with its exact returned code, and closeout and integration **carry** the completed curation as a prerequisite while invoking nothing. Replaced the CCR-R12@v5 transaction-boundary boilerplate sentence, which still presented full memory quality as an explicit request, and updated the role's own curation sentences to the complete-handoff rule. Hand-repaired two citation findings this leaf's own source edit drifted (D14): the `## Knobs, Tool Surface, And Dispatch Authority` range to :176-193 and the `SANCTIONED_SIBLING_REFERENCES` range to the test module's current :110.
- 2026-09-16T20:45+02:00 — owning-seat merge resolution (source-line convergence): the
  `governingOverview` field and its link were restored to `../../../../../../../overview.md`.
  The 2026-09-16T08:01 metadata repair above dropped one path level — this card sits one directory
  below the skill's `SKILL.md` card, so the target it names (the MCP package overview,
  `onboarding/mcp/overview.md`) needs seven levels up, not five. The five-level value resolved to
  `onboarding/mcp/src/agents_remember/overview.md`, which does not exist, so the card pointed at a
  missing file while its own text claimed the MCP package overview. No content claim changed; only
  the path. Verification metadata is unchanged and stays closeout-owned.
- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: **body updated for the corpus consolidation.** The
  canonical worker role was rewritten (187 lines) into the corpus's readable order and now declares
  its inherited sources with `**Inherits:**`. Updated Purpose (readable order plus inherited sources,
  and where the build procedure and targeted-check contract now live), Logic (leaf altitude, the
  no-commit boundary, the per-ID acceptance envelope with its citation classes, attempt-vs-protocol-event
  separation, the two malformed-row outcomes, and lifecycle non-instantiation), Invariants (the
  never-commits rule and the no-sibling-role-reference rule the shipped check enforces), and
  Repo-Internal References (the two citations whose anchors no longer exist — `## What This Seat Is`
  and `### 3 — Build` — replaced by current anchors, plus rows for `operations/implementation.md`,
  `operations/closeout.md`, and `SANCTIONED_SIBLING_REFERENCES`). The preserved task-delta sections
  below still describe rules in force; their live homes are `core/acceptance.md` (acceptance, attempts,
  completion truth) and `operations/closeout.md` (the targeted-check contract). **Metadata repair:**
  `governingOverview` pointed at `../../../../../../../overview.md` (the repository root overview) while
  its link text said "MCP package overview"; corrected to `../../../../../overview.md`. Verification
  metadata remains closeout-owned — the source is uncommitted, so no stamp was advanced and no commit
  hash was invented.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "### 3 — Build" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md:73-73. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 synchronized manager-only worker dispatch,
  explicit ambient takeover, and fixed structural-row ownership. Verification remains
  closeout-owned.

- 2026-08-28T11:51+02:00 — No content impact: synchronized the final independence and single-
  authority wording; projection ownership and byte-identity rules remain unchanged.

- 2026-08-28T11:32+02:00 — No content impact: synchronized projection payload changed with the
  canonical one-primary requirement doctrine; projection ownership and byte-identity rules remain
  unchanged.

- 2026-08-27T22:15+02:00 — Synchronized the pre-handoff correction versus post-handoff rejection
  contract from canonical lifecycle/task doctrine.

- 2026-08-27T21:53+02:00 — Synchronized M40@v2 worker attempt/event boundaries.

- 2026-08-27T18:06+02:00 — M40/M43: synchronized immutable worker attempt and failure-routing
  doctrine from the canonical role.

- 2026-08-27T14:04+02:00 — Tightened installed worker intake around approved version-addressed
  packets and packet-local durable corpus rulings.
- 2026-08-27T13:32+02:00 — M39@v1: worker intake and handoff bind every block to the exact stable
  ID + version and canonical packet, refusing missing or mismatched revisions instead of repairing
  requirement identity locally. Verification remains closeout-owned.

- 2026-08-27T12:43+02:00 — M38: recorded the synchronized worker envelope and explicit Checks
  contract. Verification metadata stays pinned until governed closeout stamps the PDLS commit.


- 2026-08-15T04:32+02:00 — 260815-DAG-L2: synchronized execution-nature input and the exact
  leaf-targeted/master-full quality boundary. Verification remains closeout-owned.

- 2026-08-14T11:25+02:00 — R39 curator: replaced repository-specific worker commands with the
  resolved contract and fixed cadence. Verification remains closeout-owned.

- 2026-08-13T14:32+02:00 — L23 final curator pass: synchronized Dagger-only leaf acceptance,
  required explicit diff base, master-owned full mode, and diagnostic-only host execution.
  Verification remains closeout-owned.
- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: synchronized the
  canonical worker boundary: leaf checks remain targeted and master full gates
  use host-managed RAM/swap by default.

- 2026-08-11T14:25+02:00 — Replaced accumulated copy-specific/task-delta prose with the exact
  synchronized worker-artifact contract and current source evidence.
- 2026-08-09T13:59+02:00 — Synchronized fact-relay and idle-safety doctrine.
- 2026-08-08T02:00+02:00 — Synchronized leaf/master quality altitude boundaries.
- 2026-07-05T01:30+02:00 — Established the self-contained packaged worker lifecycle.
