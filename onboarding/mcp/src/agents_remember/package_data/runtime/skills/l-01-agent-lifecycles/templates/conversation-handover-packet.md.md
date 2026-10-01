# l-01-agent-lifecycles/templates/conversation-handover-packet.md

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

## Evidence

### Repo-Internal References

This bundle copy is the shape the frame hands a successor at a takeover spawn or respawn; the worker and manager jobs both hand over through it.

- Sync-propagated bundle copy of the canonical templates source. [1]
- The frame's job-selection contact point hands this packet to a takeover-spawned successor so it onboards from state, not the transcript. [2]
- The worker respawn use continues a leaf handed over by the worker job. [3]
- The master-handover use is the manager's completed-master seat hand-off. [4]

As of cycle 4 the takeover use names its owner (the orchestrator's profile check in roles/orchestrator.md) instead of the retired 'frame' vocabulary.

As of cycle 5: the takeover pointer names the real section.

### Cross-Repo References

No sibling repository evidence is needed for this report template.

No meaningful cross-repo references found.
