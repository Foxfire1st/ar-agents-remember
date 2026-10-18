# mcp/tests/test_drift_dismissal_occurrences.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pin occurrence-scoped actionable-drift dismissal and conservative native source-census reclamation.

## Code Commentary

Converted drift fingerprints cover complete actionable findings rather than sample, count or clock alone. Clicks capture the published fingerprint; old acknowledgement rows adopt a first fingerprint once without resurfacing. Failed/partial source censuses mutate no dismissal bytes while valid changed findings may still publish. Healthy findings and proved-deleted branches end only their occurrences; a missing snapshot alone does not prove branch disappearance. ASGI click/restart tests preserve acknowledgements until changed findings. Historical stale-session JSON is deliberately invalid cleanup input, not a current attention kind. Large native-ref/dismissal fixtures assert bounded retained rows, not a new execution or scalability certification.

## Evidence

- Fingerprint ignores order and nonactionable rows but changes with a finding despite equal counts. [1]
- Click retains the shown fingerprint; time-only refreshes stay dismissed and changed findings return. [2]
- Legacy acknowledgement adopts once and later changed findings recur. [3]
- Partial, malformed, unreadable and invalid-count inputs leave acknowledgement bytes intact. [4]
- Incomplete overall census may publish good changed findings without mutating stored dismissals. [5]
- Healthy drift and proved branch deletion reclaim only their own occurrences. [6]
- Real in-process ASGI dismiss/state routes survive restart and reveal a new finding. [7]
- Invalid retired-session rows are compacted and only surviving native branch subjects remain; unchanged reread does not rewrite. [8]
