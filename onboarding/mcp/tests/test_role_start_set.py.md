# Leaf-set start proofs

[Tests route overview](overview.md)

## Contract

Operation-level fake-host tests prove the Manager-owned three-seat path: Worker opens, Reviewer and Curator exist without turns, optional Reviewer work opens only Reviewer, and the first addressed message opens one held seat with its handover. A repeated set retains all three agent identities, and partial creation is completed under the same set UUID without a fourth agent or a spontaneous held opening.

The suite also refuses an Architect set and a wrong-master Manager set without launch effects, while an ordinary Architect single Worker start remains admitted. These are executable fixture assertions, not evidence of the required paid sandbox/real-host journey.

Set start publishes all three role facts. When an older held receipt lacks its role index, the first addressed message restores the Reviewer registration before agent-create starts its turn; the other held seat stays closed.

## Evidence

- Held opener restores missing role facts before native agent-create and leaves the other held. [4]


- One Manager call creates three agents with exactly the Worker opened. [1]
- A partial creation completes with the same set identities and held seats intact. [2]
- A set does not enlarge the existing role may-start matrix. [3]
