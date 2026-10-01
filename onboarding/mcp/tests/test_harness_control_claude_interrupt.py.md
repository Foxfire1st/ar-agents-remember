# mcp/tests/test_harness_control_claude_interrupt.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Claude native interrupt acknowledgement and terminal-outcome correlation.

## Code Commentary

### Logic

Accepted interrupt settles a matching interrupted turn as cancelled and replays its first acknowledgement without another native write. Guard failures write nothing. A racing rate-limit error stays failed and natural completion stays completed. Lost acknowledgement remains unknown until late correlated evidence resolves it.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Interrupt acknowledgement is not terminal success. The fixture uses structured stream-json frames, not a terminal paste or inferred text match.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Accepted interrupt settles interrupted not failed. [1]
- Interrupt replays first acknowledgement without a second write. [2]
- Interrupt guards reject before any native write. [3]
- Accepted interrupt racing a rate limit error stays failed. [4]
- Natural completion after an accepted interrupt stays completed. [5]
- Lost acknowledgement is unknown and a late success still correlates. [6]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
