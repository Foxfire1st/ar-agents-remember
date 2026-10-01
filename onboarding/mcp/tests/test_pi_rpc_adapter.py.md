# mcp/tests/test_pi_rpc_adapter.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Pi RPC framing/model contracts and shared fake transport.

## Code Commentary

### Logic

The fake transport and launch/operation builders support adapter consumers. Three retained protocol cases preserve Unicode line separators under LF framing, accept CRLF, refuse malformed or overlong frames and retain provider-qualified model identity with model-gated thinking options.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Historical adapter launch, setter and reconnect scenarios no longer run in this file. Protocol fixtures are not an installed Pi conformance run or a static fallback model catalog.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Lf only decoder preserves unicode separators and accepts crlf. [1]
- Malformed and overlong frames refuse loudly. [2]
- Available models preserve provider identity and model gated thinking. [3]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
