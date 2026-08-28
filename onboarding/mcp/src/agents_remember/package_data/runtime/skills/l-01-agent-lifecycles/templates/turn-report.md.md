# l-01-agent-lifecycles/templates/turn-report.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/turn-report.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-28T11:51+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |

## Purpose

This template is the **mandatory worker hand-off artifact** of the `l-01-agent-lifecycles` report-template library. A worker fills it at **every** hand-off so a leaf's work survives session death and a respawned successor onboards from **state, not the transcript**. It is the leaf's single artifact of record; a missing turn report is nudged by the HFX2-L2 agent-notifier sweep, never by a manager watching for it (uniform-mechanism ruling 2026-07-07).

## Code Commentary

### Logic

The synchronized report separates internal protocol-event rows from formal review-handoff attempt
records and gives each lightweight attempt a content-addressed expanded-evidence anchor.

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical `skills/l-01-agent-lifecycles/templates/turn-report.md`. It has three parts: a prose header naming the artifact and its writer (`roles/worker.md`), a numbered **Rules** block, and a fenced **Shape** the worker copies verbatim — a metadata table (leaf / master / worker / worktree / status / checks / written) followed by the sections *What Was Done*, *Issues Hit*, *Solved On The Spot*, *What Is Left*, *Onboarding Refreshed*, *Escalations*, and the closing **Respawn State** block that onboards a successor from state alone.

### Conventions

The report is written in the **main loop** from the worker's own work plus any sub-agent summaries — never delegated to a sub-agent. It states facts (what changed, what broke, what is proven green, what remains) rather than a narrative, and lives durably in the series notes (`notes/reports/<leaf>-worker-report.md`), referenced from the leaf `task_doc` and posted through the inbox with `messageKind: turn-report`.

### Invariants And Boundaries

The report is mandatory at every hand-off, and a missing one is nudged — by the HFX2-L2 supervisor
sweep mechanically, never a manager hand-rolling its own watch over the artifact (uniform-mechanism
ruling 2026-07-07, 260707-HFX2-L5). The **Respawn State** section must let a fresh successor continue **without reading any transcript**. A plan delta beyond blank-filling does not belong in *Solved On The Spot* — it is escalated to the manager and recorded under *Escalations*.

### Todos

No TODO markers are present in this report template.

### Docs References

No external domain documentation applies to this repository-local report template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This bundle copy is the shape the worker job writes at every hand-off; the frame catalogs it as a per-role artifact obligation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Sync-propagated bundle copy of the canonical templates source. | `# Turn-Report Template` | skills/l-01-agent-lifecycles/templates/turn-report.md:1-57 |
| The worker writes the turn report in the main loop at every hand-off; it is the leaf's single artifact of record. | `# Lifecycle — Worker` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md:1-154 |
| The frame lists the mandatory worker turn report among the per-role artifact obligations. | `# l-01-agent-lifecycles — The Agent Lifecycles` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:6-416 |

## Cross-Repo References

No sibling repository evidence is needed for this report template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## M38 Turn-Report Projection

The synchronized report shape repeats a complete acceptance envelope for every stable requirement
ID and now contains a dedicated Checks section with exact commands and outcomes, closing the former
brief/report mismatch. It separately records durable-evidence promotion and curator observations;
neither substitutes for requirement evidence.
Packet inspection now records the version-addressed path, approved state, matching ID/version, and
durable corpus ruling before delivery evidence can be review-passable.

## M40/M43 Turn-Report Projection

The installed report is the append-only worker side of the leaf journal. Each record binds exact
requirement/manifestation, attempt/predecessor, candidate, envelope, checks, append time, and
classified findings; prior records are immutable.

## 2026-08-27 Attempt Boundary Clarification

This packaged projection preserves the canonical phase boundary: validate before append; a
malformed never-handed-off row receives a non-attempt correction/void without consuming an ID;
a malformed handed-off attempt requires independent rejection before successor handoff.

## Update History

- 2026-08-28T11:51+02:00 — No content impact: synchronized the final independence and single-
  authority wording; projection ownership and byte-identity rules remain unchanged.

- 2026-08-28T11:32+02:00 — No content impact: synchronized projection payload changed with the
  canonical one-primary requirement doctrine; projection ownership and byte-identity rules remain
  unchanged.

- 2026-08-27T22:15+02:00 — Synchronized the pre-handoff correction versus post-handoff rejection
  contract from canonical lifecycle/task doctrine.

- 2026-08-27T21:53+02:00 — Synchronized M40@v2/M44@v2 report structure.

- 2026-08-27T18:06+02:00 — M40/M43: synchronized the complete worker attempt record shape.

- 2026-08-27T14:04+02:00 — Added approved version-addressed packet and durable corpus-ruling proof
  to the installed turn-report envelope.
- 2026-08-27T13:32+02:00 — M39@v1: each acceptance block now names the stable ID + version and
  records the matching canonical packet inspection before delivery/verification evidence.
  Verification remains closeout-owned.

- 2026-08-27T12:43+02:00 — M38: recorded the per-ID envelope and explicit Checks section in the
  installed report shape. Verification metadata stays pinned until governed closeout stamps the
  PDLS commit.


- 2026-08-11T19:58+02:00 — Recorded `turn-report.md` as a synchronized runtime artifact of the current canonical lifecycle doctrine; it introduces no independent role contract.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 6 citation findings for the canonical turn-report template, worker role, and lifecycle skill references.

- 2026-07-08T23:59+02:00 — 260707-HFX2-L5 (doctrine rewrite, active vigilance → passive
  process-and-ack): "A missing turn report is nudged by the manager" reworded to name the HFX2-L2
  supervisor sweep as the actual mechanism, never a manager watching for it (uniform-mechanism
  ruling 2026-07-07); Invariants And Boundaries updated to match. Doctrine-only change set (5
  canonical `skills/` files synced to 9 downstream copies, 0 Python); sync-propagated bundle copy of
  the canonical `skills/l-01-agent-lifecycles/templates/turn-report.md`. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L5 commit.

- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: re-homed under l-01-agent-lifecycles/templates/; role-file reference now roles/worker.md. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T12:31+02:00 - L3: pinned the default
  `notes/reports/<leaf>-worker-report.md` artifact path and `turn-report` inbox
  message-kind convention. Verification metadata pinned until closeout stamps
  the L3 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` turn-report report template (leaf 260703-L1) — the mandatory worker hand-off artifact whose Respawn State onboards a successor from state, not the transcript. Verification metadata pinned until closeout stamps the L1 commit.
