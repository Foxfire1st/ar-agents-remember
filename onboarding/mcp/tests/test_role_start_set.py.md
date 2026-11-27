# Leaf-set start proofs

[Tests route overview](overview.md)

## Contract

Operation-level fake-host tests prove the Manager-owned three-seat path: Worker opens on the host, Reviewer and Curator are reserved on disk as deferred held seats (`hostAgentExists: false`, zero host calls until first message), optional Reviewer work opens only Reviewer, and the first addressed message creates and opens one held seat with its handover. A repeated set retains all three agent identities, and partial creation is completed under the same set UUID without a fourth agent or a spontaneous held opening.

The suite also refuses an Architect set and a wrong-master Manager set without launch effects, while an ordinary Architect single Worker start remains admitted. These are executable fixture assertions, not evidence of the required paid sandbox/real-host journey.

Set start publishes role facts for opened seats and reserves deferred held receipts. When a deferred held seat receives its first addressed message, the opener publishes role facts before native `agent-create` creates and opens it; the other held seat stays reserved without a host agent.

## Evidence

- Held opener restores missing role facts before native `agent-create` and leaves the other seat reserved. [4]
- One Manager call opens Worker on the host and reserves Reviewer and Curator as deferred held seats. [1]
- A partial creation completes with the same set identities and deferred held seats intact. [2]

- A set does not enlarge the existing role may-start matrix. [3]
