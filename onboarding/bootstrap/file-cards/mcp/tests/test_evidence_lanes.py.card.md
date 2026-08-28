# File Card — mcp/tests/test_evidence_lanes.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/tests/test_evidence_lanes.py` |
| targetOnboardingFile | `onboarding/mcp/tests/test_evidence_lanes.py.md` |
| generated | 2026-08-28T06:28+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | explicit evidence-classification contract |
| Risk | silent unit fallback or conflicting lane authority |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-005 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `onboarding/mcp/tests/overview.md` |
| ancestorOverviews | `onboarding/overview.md`, `onboarding/mcp/overview.md` |
| localArea | Python evidence tests |

## Why This File Matters

It makes every node's evidence class explicit and fail-loud, including provider and diagnostic
boundaries.

## What The Worker Must Explain

- exhaustive unique registry;
- trigger expressions;
- checked-in manifest authority;
- missing/conflicting classification refusals.

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/tests/test_evidence_lanes.py` | yes | forcing behavior |
| Governing overview | `onboarding/mcp/tests/overview.md` | yes | test-area model |
| Manifest | `mcp/tests/test-evidence-lanes.toml` | yes | classification authority |

## Known Traps

- A runtime opt-in marker does not replace checked-in category ownership.

## Questions To Resolve

None.

## Done When

- The sidecar records exhaustive explicit classification and refusal behavior.
