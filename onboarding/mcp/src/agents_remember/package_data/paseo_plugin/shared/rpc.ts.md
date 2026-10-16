# mcp/src/agents_remember/package_data/paseo_plugin/shared/rpc.ts

## Governing Overview

[Route overview](../../../../../overview.md)

## Purpose

The shared definitions type ar.embed-list and the explicit ar.host-activity-snapshot server/client transports.

## Code Commentary

ar.embed-list takes empty input and returns string dashboardOrigin/frameBaseUrl pairs; provisioning and client origin checks remain separate. ar.host-activity-snapshot takes empty input and returns a bootId string after the server-owned reconciliation. It is an explicit startup/plugin-boot read, not a host poll or task-stage producer.

## Invariants And Boundaries

Schema shape is not origin authorization, independent frame permission or a secret channel.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- Embed-list and explicit host-snapshot transports have separate typed empty-input responses. [1]
