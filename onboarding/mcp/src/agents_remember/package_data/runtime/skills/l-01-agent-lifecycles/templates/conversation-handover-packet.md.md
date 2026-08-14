# l-01-agent-lifecycles/templates/conversation-handover-packet.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/conversation-handover-packet.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T18:20+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|

## Purpose

Packaged runtime copy of the conversation-handover packet. The canonical template owns its shape;
`scripts/sync-skills.py` publishes this exact artifact for installed runtimes.

## Code Commentary

### Logic

The packet transfers durable conversation context between structural seats. It identifies `from`
and `to` by canonical task-document path plus role, records the canonical sprint/master/leaf
document, and leaves harness/model/effort to settings. Runtime occupant, lifecycle, and agent ids do
not belong in the packet.

### Conventions

Fill the canonical packet completely, carry durable artifact references, and synchronize changes
from the canonical template rather than editing this packaged copy independently.

### Invariants And Boundaries

- A handover remains valid across occupant replacement because seats are document-and-role bound.
- The packet never becomes a transport-address or profile-selection surface.
- This packaged artifact must remain byte-identical to the canonical template.

### Todos

None recorded.

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

- 2026-08-11T19:58+02:00 — Reconciled `conversation-handover-packet.md` as the exact synchronized runtime artifact of its current canonical document/role contract; removed obsolete leaf-key and runtime-id ownership implications.
- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 4 repo-internal citation rows and preserved verification metadata.

- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): the takeover pointer names the real section.. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:20+02:00 - L8 seam-ruling remediation (cycle 4): takeover owner named; frame vocabulary removed. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: re-homed under l-01-agent-lifecycles/templates/ (content unchanged). Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` conversation-handover-packet report template (leaf 260703-L1) — one schema with three uses (role takeover, worker respawn, master-complete handover) where the receiver always onboards from the packet, not the transcript. Verification metadata pinned until closeout stamps the L1 commit.
