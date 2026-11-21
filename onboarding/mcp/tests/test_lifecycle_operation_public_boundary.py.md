# mcp/tests/test_lifecycle_operation_public_boundary.py

## Governing Overview

[MCP Tests](overview.md)

## Purpose

These cases protect the control payload adapter’s response for historical closeout and integration journals and the corresponding inspection-only projections.

## Code Commentary

The fixture checks the digest of each old-writer record, copies its bytes into the expected journal location and reads it through the current store. The test invokes the control payload adapter directly under tool-call context and reads its saved result. For retry, recover and resume, the response names the matching synchronous tool and current contract path. Closeout guidance includes a fresh intent placeholder. An absent retired record names its replacement without a generation. A missing direct-landing record returns the missing-operation refusal, and a stale generation returns the generation-changed refusal with both identities.

## Relationships

The retired and direct records share inspection projections. The cases check that retired projections offer no advice or controls and that a completed direct landing retains its recommendation. The old-writer fixture entries in the lifecycle catalog record their exact consumer scope.

## Evidence


- The direct payload adapter call under tool-call context reports both synchronous replacement names and keeps the retained journal bytes. [1]


- The adapter gives absent retired records a replacement without a generation, refuses a missing direct-landing record and reports the requested and actual identities for a stale generation. [2]
