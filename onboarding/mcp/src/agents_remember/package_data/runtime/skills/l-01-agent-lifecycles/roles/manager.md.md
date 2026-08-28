# mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T14:18+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

This file is the packaged runtime artifact synchronized exactly from canonical
`skills/l-01-agent-lifecycles/roles/manager.md`. It supplies installed runtimes with the same
one-real-master manager lifecycle and owns no separate intent.

## Logic

The synchronized manager does not advance attempt IDs at dispatch or during internal reruns,
validates the content-addressed handoff record, and rebuilds a non-gating summary that excludes
protocol events.

The packaged source therefore carries the canonical manager's structural leaf dispatch,
builder/reviewer/curator closeout chain, delegated gate authority, leaf/master quality altitudes,
subordinate cleanup, and durable master-handover contract unchanged. The sync process copies the
complete canonical tree; package-local edits are drift, not customization.

Curator dispatch carries the same exact approved revision packets and per-revision reviewer rows
used by builder/reviewer handoff. A rejected or worker-blocked revision is a curation blocker, not
authority for current onboarding.

The synchronized quality altitude uses the pinned Dagger graph for Agents Remember acceptance:
targeted for leaf/focused work and full exactly once at master integration. Both require the
task-derived explicit diff base; host pytest/wrapper runs are refused, never acceptance or a
fallback. A constrained lifecycle environment alone explicitly opts into `memoryCapBytes`.

## Conventions

- Change manager doctrine only in canonical `skills/`.
- Propagate and verify with `scripts/sync-skills.py`.
- Keep package-path provenance distinct while keeping content byte-identical.
- Do not append package-only task deltas or compatibility instructions.

## Invariants And Boundaries

- Installation cannot widen manager authority beyond one canonical master.
- Runtime packaging cannot expose child occupant ids to the manager model.
- Builder, reviewer, curator, closeout, and handover separation matches canonical doctrine exactly.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The packaged manager is one master-scoped owner of the leaf closeout chain. | "## What This Seat Is" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md:11-30 |
| Its hosted child dispatch uses structural task document and role. | "## Hosted Role Dispatch" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md:41-47 |
| Curator dispatch carries exact approved packets and per-revision reviewer adjudication. | "Curator coherence pass — mandatory, not skippable." | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md:206-206 |
| The canonical source owns this doctrine. | "# Lifecycle — Manager" | skills/l-01-agent-lifecycles/roles/manager.md:1-47 |
| MCP package data is copied from canonical skills and checked for drift. | "mcp package data"; `sync_target`; `check_targets` | scripts/sync-skills.py:43-47; scripts/sync-skills.py:136-157; scripts/sync-skills.py:179-203 |

## L23 Manager And Leaf Admission

The packaged manager role starts only after the control plane proves its master
contains super for code/external memory. Every subordinate dispatch re-proves
the full chain before creating a child; refusal mutates no seat and carries the
ordered contract-addressed sync needed before retrying the same leaf.

## L23 Pre-Curator Lineage Boundary

Immediately before curator dispatch, the packaged manager calls `worktree_status` for the canonical
leaf and requires every task-derived code and external-memory lineage edge to be `current`. It
synchronizes and reconciles stale ancestry before onboarding, carries the resulting projection in
the curator brief, and relies on dispatch to repeat the proof before hosted-process creation. Later
closeout/integration rechecks remain mandatory because they close a different, post-quality race.

## L23 Final Candidate Disposition

The manager partitions independent review by material ownership route, returns repairs to the same
reviewer, and proves complete code plus external-memory lineage immediately before compiling the
curator brief. A stale candidate is synchronized before curation rather than documented.

## R39 Generic Quality Altitude

The manager resolves each repository executor and evidence contract from its memory layer. Leaf
closeout accepts once, leaf integration reuses the certified commit, and master integration
accepts full once. Missing or failed required policy refuses; there is no inferred local fallback.

## 260815-DAG-L2 Nature-Aware Completion

Managers report master-local closeout facts and never rank the sprint. Organizational leaves use
the direct super edge; atomic leaves use the isolated master edge and expose no intermediate state.
The organizational master-exit reviewer receives the exact proposed final super candidate—prior
landed contributions plus the proposed final leaf—before the one full check and ref movement.

## 260821-CLIVE Manager Door And Task Duties

The manager now publishes complete canonical closeout-door truth after builder, current route
review, curator reconciliation, lineage, and task/source/memory/ledger provenance. The waiting door
is source truth; portfolio comparison and first-ready release remain orchestrator duties, while the
queue is only their current projection. Managers continue every intrinsically valid task edit and
relay incomplete `projectionEffects`; evidence-changing edits are re-proven through the door owner,
never delayed or patched into a row. After claim, status and operation controls address the stable
root journal, so queue absence or invalidation cannot strand the leaf.

## M38 Exact-Set Dispatch Projection

The installed manager role compiles the leaf-owned and inherited stable requirement IDs, requires
the complete worker envelope for that set, and sends the identical set to independent review.
Missing/duplicate IDs or an overall pass with a rejected row fail closed. The evidence-promotion
hold point remains a separate brief and verdict concern. This projection owns no manager-local
variant.
Each row must point to an approved version-addressed packet carrying its durable corpus ruling;
missing, unapproved, or mismatched revisions are undispatchable.

## M40-M45 Manager Attempt Projection

The packaged manager validates immutable worker/reviewer attempt identity, records bounded
invalidation after independent regression proof, and maintains only a rebuildable non-gating
summary over authoritative leaf journals.

## 2026-08-27 Attempt Boundary Clarification

This packaged projection preserves the canonical phase boundary: validate before append; a
malformed never-handed-off row receives a non-attempt correction/void without consuming an ID;
a malformed handed-off attempt requires independent rejection before successor handoff.

## Update History

- 2026-08-28T14:18+02:00 — Reconciled the manager-doctrine source ranges against the committed
  PDLS candidate after final requirement-ownership edits; the documented behavior is unchanged.

- 2026-08-28T11:32+02:00 — No content impact: synchronized projection payload changed with the
  canonical one-primary requirement doctrine; projection ownership and byte-identity rules remain
  unchanged.

- 2026-08-27T22:15+02:00 — Synchronized the pre-handoff correction versus post-handoff rejection
  contract from canonical lifecycle/task doctrine.

- 2026-08-27T21:53+02:00 — Synchronized M40@v2/M44@v2 manager attempt/summary boundaries.

- 2026-08-27T18:06+02:00 — M40-M45: synchronized exact-attempt dispatch, owner invalidation, and
  non-gating master-summary obligations.

- 2026-08-27T16:27+02:00 — Synchronized exact requirement packets and reviewer adjudication into
  manager-to-curator dispatch. Verification remains closeout-owned.

- 2026-08-27T14:04+02:00 — Tightened the installed manager projection around approved
  version-addressed packets and their durable corpus rulings.
- 2026-08-27T13:32+02:00 — M39@v1: manager dispatch now verifies the exact stable ID + version and
  matching canonical packet for every worker/reviewer row; missing or stale revisions are
  undispatchable. Verification remains closeout-owned.

- 2026-08-27T12:43+02:00 — M38: recorded exact-set manager dispatch and same-set review.
  Verification metadata stays pinned until governed closeout stamps the PDLS commit.


- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: merged manager-owned door publication, task-authoring primacy, and journal-only post-claim recovery. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: synchronized manager-local readiness, nature-aware
  lineage, and exact pre-landing organizational review scope. Verification remains closeout-owned.

- 2026-08-14T11:25+02:00 — R39 curator: removed repository-specific commands from the generic
  manager role and retained fixed cadence. Verification remains closeout-owned.
- 2026-08-14T06:32+02:00 — L23 synchronized runtime doctrine: managers partition route review,
  require current task-derived lineage, and pass only stable candidate evidence into curator
  dispatch. Verification remains closeout-owned.
- 2026-08-13T14:32+02:00 — L23 final curator pass: synchronized Dagger-only acceptance,
  targeted/full altitude, required explicit diff base, and diagnostic-only host execution.
  Verification remains closeout-owned.
- 2026-08-13T09:05+02:00 — L23 curator: recorded the mandatory pre-curator lineage check, projection
  handoff, and fail-before-host dispatch recheck; final provenance remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented manager/leaf lineage admission without agent-held ids; verification remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: synchronized the then-current
  master-gate resource rule. L23 later moved execution exclusively into Dagger.

- 2026-08-11T14:25+02:00 — Replaced duplicated history/task fragments with the exact synchronized
  manager-artifact contract and current source evidence.
- 2026-08-10T07:30+02:00 — Synchronized report-gated subordinate cleanup doctrine.
- 2026-08-09T13:59+02:00 — Synchronized fact-relay supervision wording.
- 2026-07-12T14:20+02:00 — Established packaged manager lifecycle coverage.
