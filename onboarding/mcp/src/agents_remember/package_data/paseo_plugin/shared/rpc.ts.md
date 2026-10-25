# mcp/src/agents_remember/package_data/paseo_plugin/shared/rpc.ts

## Governing Overview

[Route overview](../../../../../overview.md)

## Purpose

The shared definitions type ar.embed-list and the explicit ar.host-activity-snapshot server/client transports.

## Code Commentary

ar.embed-list takes empty input and returns string dashboardOrigin/frameBaseUrl pairs; provisioning and client origin checks remain separate. ar.host-activity-snapshot takes empty input and returns a bootId string after the server-owned reconciliation. It is an explicit startup/plugin-boot read, not a host poll or task-stage producer.


**L184 — INV-VDWN33.** The shared contract is what both sides are written against, so the number's type is stated here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Invariants And Boundaries

Schema shape is not origin authorization, independent frame permission or a secret channel.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.


- Embed-list and explicit host-snapshot transports have separate typed empty-input responses. [1]
