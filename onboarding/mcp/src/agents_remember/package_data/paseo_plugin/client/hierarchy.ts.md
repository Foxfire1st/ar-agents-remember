# mcp/src/agents_remember/package_data/paseo_plugin/client/hierarchy.ts

## Governing Overview

[Route overview](../../../../../overview.md)

## Purpose

The helper owns one public SDK catalog lifetime and agent/workspace-specific Parent composer pills.

## Code Commentary

Initial and continuation requests use `PAGE_SIZE=200` and unique nonempty cursors. The subscribed agent read and every continuation request both include archived and background agents. Subscriptions publish allowed canonical/native-parent labels and the native project/workspace/agent fields. Replacement snapshots clear older queued deltas only for their directory; generation checks suppress older loads. Parent pills track native relation/workspace and disappear for root/missing/archived rows, and they are offered only while the agent is in the live selected-candidate set published by `selection.ts` (MIK-R75 rule 9a): the module subscribes to `onSelectedChats`, so an unknown source removes the pill at every width and a known wide selection restores it without a second DOM read or a retained earlier selection.

## Invariants And Boundaries

Errors remain explicit; native membership is transported without inventing AR grouping. The pill gate uses the same live value the bridge checks; at the host's narrow layout no pill is drawn and the host's list is the navigation. Teardown releases listeners/subscriptions/pills.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- Directory continuation uses the shared page size, follows every page and refuses invalid cursors. [1]
- The hierarchy registers Parent controls for the live selected agent and projects native catalog facts. [2]
- Subscribed and continuation agent requests explicitly include archived and background agents. [3]
- The initial and continuation filters retain background role agents from both paths. [4]
- Deferred lookups respect tab and relation changes, missing targets and archived agents. [5]
- Overlapping snapshots leave unrelated and newer updates intact and release owned resources at teardown. [6]
