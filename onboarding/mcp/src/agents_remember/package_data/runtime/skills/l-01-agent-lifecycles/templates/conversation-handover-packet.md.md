# l-01-agent-lifecycles/templates/conversation-handover-packet.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/conversation-handover-packet.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T18:20+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|

## Purpose

This template is the **one schema, three uses** hand-off packet of the `l-01-agent-lifecycles` report-template library: **role takeover** (profile-fit — the frame spawns the correct profile and hands over), **worker respawn** (a fresh worker continues a leaf), and any **master-complete handover**. The receiver always onboards from the packet, **never from a prior conversation**.

## Code Commentary

### Logic

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical `skills/l-01-agent-lifecycles/templates/conversation-handover-packet.md`. It carries a prose header stating the single-schema/three-use design (the COMMS model), a numbered **Rules** block, and a fenced **Shape**: a metadata table (use / seat-role / from / to / leaf-master / written) followed by *Why This Handover* (a line per use), *The Request (as agreed)*, *Decisions Already Made*, *Constraints & Invariants*, *Links (onboard from these, not the transcript)*, *Open Questions For The Successor*, and *Current State*.

### Conventions

The `use` slot selects among role-takeover, worker-respawn, and master-handover, and the *Why This Handover* section carries one line per use. Links (task_doc, integration branch, prior turn reports, durable notes) are named so the successor onboards from artifacts rather than a transcript.

### Invariants And Boundaries

The receiver must be able to act from **this packet alone** — the transcript is assumed gone. For a **takeover spawn**, the packet states the profile mismatch that triggered it so the successor knows why it exists and does not repeat the wrong-profile work. The same one schema serves master handover, role takeover, and worker respawn alike.

### Todos

No TODO markers are present in this report template.

### Docs References

No external domain documentation applies to this repository-local report template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This bundle copy is the shape the frame hands a successor at a takeover spawn or respawn; the worker and manager jobs both hand over through it.

| Finding | Anchor | Source |
| --- | --- | --- |
| Sync-propagated bundle copy of the canonical templates source. | `# Conversation-Handover-Packet Template` | skills/l-01-agent-lifecycles/templates/conversation-handover-packet.md:1-54 |
| The frame's job-selection contact point hands this packet to a takeover-spawned successor so it onboards from state, not the transcript. | `## The Minimal Frame (the only machinery every session shares)` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:140-174 |
| The worker respawn use continues a leaf handed over by the worker job. | `# Lifecycle — Worker` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md:1-154 |
| The master-handover use is the manager's completed-master seat hand-off. | `# Lifecycle — Manager` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md:1-242 |

As of cycle 4 the takeover use names its owner (the orchestrator's profile check in roles/orchestrator.md) instead of the retired 'frame' vocabulary.

As of cycle 5: the takeover pointer names the real section.

## Cross-Repo References

No sibling repository evidence is needed for this report template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 4 repo-internal citation rows and preserved verification metadata.

- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): the takeover pointer names the real section.. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:20+02:00 - L8 seam-ruling remediation (cycle 4): takeover owner named; frame vocabulary removed. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: re-homed under l-01-agent-lifecycles/templates/ (content unchanged). Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` conversation-handover-packet report template (leaf 260703-L1) — one schema with three uses (role takeover, worker respawn, master-complete handover) where the receiver always onboards from the packet, not the transcript. Verification metadata pinned until closeout stamps the L1 commit.
