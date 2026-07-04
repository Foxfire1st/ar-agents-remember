# l-02-agent-orchestration/templates/master-handover-packet.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/templates/master-handover-packet.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-04T12:31+02:00                     |
| lastVerifiedCommitHash | `6b940141fc319f1d2d18b2c94fd9e9a213d43141` |
| lastVerifiedCommitDate | 2026-07-04T12:52:03+02:00|

## Purpose

This template is the **manager → orchestrator** hand-off artifact posted at **master exit** in the `l-02-agent-orchestration` report-template library. It is what the orchestrator integrates a completed master into the super branch from: the integration branch ref, the change-set summary, the master-exit verdict reference, and the C-11 carry-over state.

## Code Commentary

### Logic

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical `skills/l-02-agent-orchestration/templates/master-handover-packet.md`. It carries a prose header naming the writer (`jobs/manager.md`) and the delivery path (inbox + stdin push), a numbered **Rules** block, and a fenced **Shape**: a metadata table (master / manager / integration branch / base / verdict / verdict outcome / written) followed by *Change-Set Summary*, *Requirements / Steps Completion*, *Carry-Over State* (for the orchestrator's master → super C-11), *Known Follow-Ups*, and *Reachability*.

### Conventions

The packet is delivered durably via the inbox plus a stdin push, using the
`master-handover` message kind so the orchestrator can distinguish it from nudges
or ordinary notes. It names the integration branch precisely (the orchestrator
bases its C-11 integration on it) and summarizes the change set at master
granularity, listing each leaf landed with a one-line outcome.

### Invariants And Boundaries

The packet is posted **only after** the master-exit adversarial verdict exists — the verdict reference is a required slot. The carry-over state must let the orchestrator's `c-11-memory-carryover-from-branch` integration run without re-deriving what landed (parked/carried memory rows, ledger coverage of every leaf commit, single-siding notes for overlapping strands).

### Todos

No TODO markers are present in this report template.

### Docs References

No external domain documentation applies to this repository-local report template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This bundle copy is the shape the manager job posts at master exit; it references the master-exit verdict artifact and feeds the orchestrator's C-11 integration.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Sync-propagated bundle copy of the canonical templates source. | n/a | [master-handover-packet.md](agents-remember/skills/l-02-agent-orchestration/templates/master-handover-packet.md) |
| The manager posts this packet to the orchestrator at master exit. | n/a | [manager.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/manager.md) |
| The required verdict slot references the master-exit adversarial verdict artifact. | n/a | [verdict.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/templates/verdict.md) |
| The frame lists the master-handover packet among the per-role artifact obligations. | n/a | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this report template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-04T12:31+02:00 - L3: documented the `master-handover` inbox
  message-kind convention for manager-to-orchestrator delivery. Verification
  metadata pinned until closeout stamps the L3 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-02-agent-orchestration` master-handover-packet report template (leaf 260703-L1) — the manager → orchestrator master-exit hand-off (integration branch, change-set summary, verdict ref, C-11 carry-over), posted only after the master-exit verdict exists. Verification metadata pinned until closeout stamps the L1 commit.
