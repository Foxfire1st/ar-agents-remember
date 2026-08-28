# File Card — mcp/test_support/agents_remember_test_support/testing/evidence_lanes.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/test_support/agents_remember_test_support/testing/evidence_lanes.py` |
| targetOnboardingFile | `mcp/test_support/agents_remember_test_support/testing/evidence_lanes.py.md` |
| generated | 2026-08-25T02:13+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | evidence category and cadence router |
| Risk | wrong test population or accidental acceptance altitude |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-003 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `mcp/test_support/agents_remember_test_support/testing/overview.md` |
| ancestorOverviews | `overview.md`, `mcp/overview.md` |

## Why This File Matters

[HIGH] This registry is the one executable mapping from evidence categories to markers, fidelity, lifetime, and affected/release/provider/stress/migration triggers.

## What The Worker Must Explain

- eight exhaustive categories and marker uniqueness
- affected versus full-release selection
- provider-gate catalog routing
- category assignment without authority promotion

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/test_support/agents_remember_test_support/testing/evidence_lanes.py` | yes | concrete current behavior |
| Governing overview | `mcp/test_support/agents_remember_test_support/testing/overview.md` | yes | route authority |
| Target sidecar | `mcp/test_support/agents_remember_test_support/testing/evidence_lanes.py.md` | yes | durable one-to-one onboarding |

## Files The Worker May Read

- `mcp/test_support/agents_remember_test_support/testing/evidence_lanes.py`
- `mcp/test_support/agents_remember_test_support/testing/overview.md`
- `mcp/test_support/agents_remember_test_support/testing/evidence_lanes.py.md`
- directly imported/consuming source needed to prove a boundary

## Files The Worker Must Not Read Without Escalation

- unrelated repository routes
- adjacent repositories
- broad historical task archives

## Required Onboarding Sections

- metadata and governing overview
- Purpose
- Code Commentary
- Invariants And Boundaries
- Docs References
- Repo-Internal References
- Cross-Repo References
- Update History

## Known Traps

- Do not let diagnostic evidence enter cadence expressions.
- Do not silently resolve conflicting category markers.

## Questions To Resolve

None.

## Done When

- The exact sidecar exists and explains current ownership and non-ownership.
- The governing overview routes readers to the new owner.
- Deleted predecessor authority is not preserved through a fallback or stale sidecar.
- Generated route indexes include the sidecar after the final content pass.
