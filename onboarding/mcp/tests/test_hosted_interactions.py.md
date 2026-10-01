# test_hosted_interactions.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Durable hosted interactions and bounded delivery retry.

## Code Commentary

### Logic

Pending adapter questions become exact durable gates. A successful response applies the gate. Pre-write failure retains the decision for bounded retry then reopens after exhaustion; post-write uncertainty reopens with failure evidence and does not answer again. Ambiguous null-request-ID vendor correlation leaves inbox rows accepted rather than falsely completed.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Not-sent and unknown delivery have different retry rights. Developer decision attribution is preserved in failure evidence when an interaction is handed back.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Pending interaction round trips through durable gate. [1]
- Failed respond reopens the gate instead of silently swallowing. [2]
- Pre write failure keeps the decision and retries until the budget runs out. [3]
- Post write failure hands the decision back without re answering. [4]
- Null request id completion rejects ambiguous vendor correlation. [5]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
