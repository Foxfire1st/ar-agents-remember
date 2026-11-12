# dashboard/src/data/directExecutionGrant.ts

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Posts the developer grant control request for one canonical leaf.

## Contract

postDirectExecutionGrant sends repository, path and give/revoke to POST /api/direct-execution-grant. It preserves success summary or refusal detail and returns a typed unreachable or malformed-payload outcome instead of inventing server state. This adapter reads payload.ok; it is not the product authority or a task-document writer.

## Evidence

- Posts the developer grant control request for one canonical leaf [1]
