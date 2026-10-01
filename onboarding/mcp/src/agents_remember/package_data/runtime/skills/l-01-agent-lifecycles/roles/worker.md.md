# mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md

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

## Evidence

### Repo-Internal References

- The packaged worker declares its seat purpose, authority boundary, and no-commit contract. [1]
- The role is a self-contained capsule — everything this seat does is on this page — and it declares no inherited shared sources. [2]
- The build procedure the worker follows has one home outside the role file. [3]
- The targeted-check contract the worker owes its owner has one home outside the role file. [4]
- The role declares the readable order — Inputs, Process, Outputs — with no operator-knob block. [5]
- The canonical source owns this doctrine. [6]
- A non-sanctioned sibling-role reference fails the shipped corpus check, which is why this role file names none. [7]
- MCP package data is copied from canonical skills and checked for drift. [8]

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
