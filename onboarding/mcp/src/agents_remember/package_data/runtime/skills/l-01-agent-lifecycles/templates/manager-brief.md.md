# l-01-agent-lifecycles/templates/manager-brief.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/manager-brief.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-13T14:32+02:00 |
| lastVerifiedCommitHash | `a89a6fc88d9330eb2749c87b3dcc3f6c4e46c4bd`                                  |
| lastVerifiedCommitDate | 2026-08-14T12:44:51+02:00|

## Purpose

Packaged runtime copy of the complete manager dispatch brief. The canonical
`skills/l-01-agent-lifecycles/templates/manager-brief.md` owns the packet; the sync process installs
this exact artifact.

## Code Commentary

### Logic

The orchestrator calls `dispatch_agent` with the canonical master document, role `manager`, and this
complete brief. The manager dispatches worker/reviewer/curator children on canonical leaf or review
documents, never handles their occupant ids, and closes a leaf only after builder code, reviewer
verdict, and curator coherence exist. Master handover raises the structural gate from ambient master
identity; the orchestrator later decides the one matching open gate by master document and kind.

### Conventions

Fill every placeholder, retain the current-super branch anchor, include existing/ruled/current
memory intent inputs for the curator, and synchronize only from the canonical template.

### Invariants And Boundaries

- The brief addresses `(master document, manager)`, not a qualified leaf key or runtime id.
- Child retirement uses `retire_child` by leaf document and role.
- Gate authority and initial brief delivery remain control-plane-owned.
- This packaged artifact must remain byte-identical to the canonical template.

### Todos

None recorded.

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

### 260731-EFA-L17 — Quality Altitude Ladder

The manager brief now assigns Agents Remember acceptance to the pinned Dagger graph. Leaf and
focused gates select targeted mode; `worktree_integrate` selects full mode once at master
altitude. Both use the task-derived explicit diff base. Host pytest and direct wrapper commands
are refused, never acceptance or an automatic fallback. `memory_quality_check` remains a
per-leaf closeout gate, and omitted required proof refuses the gate.

## L23 Final Candidate Disposition

The manager brief makes route partitioning, exact candidate identity, same-reviewer delta checks,
and the final pre-curator lineage proof explicit deliverables rather than conversational memory.

## R39 Generic Manager Brief Contract

The manager brief requires repository memory to supply executor, environment, arguments, resource
policy, retry rules, and evidence. It preserves one leaf-closeout acceptance and one
master-integration full acceptance, with no leaf-integration rerun or fallback.

## Update History

- 2026-08-14T11:25+02:00 — R39 curator: made the quality section repository-generic without
  weakening cadence. Verification remains closeout-owned.
- 2026-08-14T06:34+02:00 — L23 synchronized runtime template: manager briefs make route
  partitioning, exact candidate review, and pre-curator lineage proof explicit handoff evidence.

- 2026-08-13T14:32+02:00 — L23 final curator pass: synchronized the brief's Dagger-only
  acceptance, targeted/full altitude, explicit diff-base, and diagnostic-only host boundary.
  Verification remains closeout-owned.
- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: synchronized the
  manager brief's host-managed master-gate default and optional constrained-CI
  cap. Verification metadata remains pinned until closeout stamps L24.

- 2026-08-11T19:58+02:00 — Reconciled `manager-brief.md` as the exact synchronized runtime artifact of its current canonical document/role contract; removed obsolete leaf-key and runtime-id ownership implications.
- 2026-08-10T05:45+02:00 — 260805-ARG-L1: synced the manager brief's completion cleanup contract
  to exact report ordering, all three leaf-altitude roles, owner exclusion, and the landed opt-out.
  Verification metadata remains pinned until closeout stamps ARG-L1.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the manager-brief
  template's quality altitude ladder bullet (leaf `--targeted`; full wrapper once
  per master, memory-capped; `memory_quality_check` per leaf). Verification
  metadata stays pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-07-10T15:48+02:00 — 260707-HFX2-L17 generated-runtime doctrine delta: manager, worker, and
  curator dispatch defaults now describe the environment-role-plus-qualified-leaf pair claim, and
  cleanup now names the manager's worker/reviewer/curator retirement boundary. Verification
  metadata remains pinned until closeout stamps the L17 commit.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 reviewer N7: recorded the stale post-boot-echo
  instruction as doctrine debt; no source behavior changed.

- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 curator correction: the manager brief template sidecar
  now describes `worktree_integrate` as auto-landing successful worker/reviewer seats into the
  landed archive (`autoLandOnIntegration`); `session_retire` remains only for exceptional
  stuck/abandoned seats under the manager's authority. Verification metadata pinned until closeout
  stamps the HFX2-L11 commit.

- 2026-07-08T02:55+02:00 — 260707-HFX-L8 (seat lifecycle: retirement, issue #12): the "Dispatch
  defaults" section gains a "Cleanup" line — `worktree_integrate` auto-retires a landed leaf's
  worker/reviewer seats (config-gated, default ON); `session_retire` is available for a
  stuck/abandoned seat of the manager's OWN master only, server policy refuses any other target.
  Sync-propagated bundle copy. Verification metadata pinned until closeout stamps the HFX-L8
  commit.

- 2026-07-08T02:10+02:00 — 260707-HFX-L11 curator activation (R1/R4): Dispatch defaults section
  updated to match the new curator-brief template — curator spawns now point at
  `../templates/curator-brief.md` and name the fed inputs (landed change set over the leaf
  contract's base-to-head range, task doc, notes/) and the mgmt-L4 routing rule; the leaf closeout
  chain line adds "never before the curator pass exists." Doctrine-only change set (7 canonical
  `skills/` files: 6 edits + 1 new template, each synced to 9 mirrors, 0 Python); sync-propagated
  (`scripts/sync-skills.py`) bundle copy of the canonical
  `skills/l-01-agent-lifecycles/templates/manager-brief.md`. Verification metadata pinned — no
  commit yet on `ar/260707-hfx-l11-curator-activation` (working-tree change, synced onto the landed
  HFX-L7 base).

- 2026-07-08T01:00+02:00 — 260707-HFX-L7 (provider degradation protocol): dispatch defaults gain a
  one-line "Provider degradation:" bullet (no provider starts/watchers/retry until all-clear; no
  manager kill authority; stops and fixes route through the orchestrator/system-specialist),
  mirroring `roles/manager.md`'s fuller "Provider Degradation Alert" subsection in compact
  brief-compiler form. Sync-propagated bundle copy. Verification metadata pinned until closeout
  stamps the HFX-L7 commit.
- 2026-07-07T21:40+02:00 — 260707-HFX-L6R3 curator seat: dispatch defaults now
  name the manager -> builder -> reviewer -> curator leaf closeout chain, the exact closeout
  inputs (builder code + reviewer verdict + curator memory pass), and the fresh per-leaf curator
  spawn. Sync-propagated bundle copy. Verification metadata pinned until closeout stamps the
  HFX-L6 commit.

- 2026-07-05T19:55+02:00 - L8 builder cycle 7: exit block pins the enclosure to the EXACT contract task name + states the enclosure-less raise refusal (AR4-1c). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 - L8 builder cycle 6: enclosure on the raise, all-human conditional, planner-master slot (AR3-1/AR3-2/AR3-6b). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): the exit block states the wait=false raise and the gateId-in-packet hand-off.. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:30+02:00 - Created file-level onboarding for the new manager-brief template (L8
  seam-ruling remediation, cycle 4 — closes AR-12's dispatch-determinism gap). Verification
  metadata pinned until closeout stamps the L8 commit.
