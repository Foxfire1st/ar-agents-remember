# mcp/tests/test_harness_control_ipc.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Private harness IPC identity, lifecycle and receipt-loss contracts.

## Code Commentary

### Logic

Actual private sockets expose status and queued withdrawal with restrictive directory/socket permissions. Lost outer receipt reconciles retained truth with one adapter submit; a public duplicate also preserves the original payload and one write. Exact endpoint identity and malformed-request refusals remain enforced.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

IPC ambiguity does not authorize resend or a control fallback. Native adapter behavior is doubled while the local socket and public routing paths are real.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Private lifecycle status and withdraw round trip. [1]
- Outer socket lost receipt reconciles retained known truth. [2]
- Public duplicate returns retained result with one adapter call. [3]
- Private endpoint exact identity and submission. [4]
- Malformed ipc request is rejected without control fallback. [5]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
