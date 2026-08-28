# File Card — mcp/tests/test_cadence_runner.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/tests/test_cadence_runner.py` |
| targetOnboardingFile | `onboarding/mcp/tests/test_cadence_runner.py.md` |
| generated | 2026-08-28T06:28+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | evidence-route contract |
| Risk | shadow acceptance or silent trigger reuse |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-005 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `onboarding/mcp/tests/overview.md` |
| ancestorOverviews | `onboarding/overview.md`, `onboarding/mcp/overview.md` |
| localArea | Python evidence tests |

## Why This File Matters

It prevents scheduled/provider/migration cadence evidence from bypassing Dagger admission or
quietly becoming a second quality gate.

## What The Worker Must Explain

- host refusal ordering;
- trigger-specific populations;
- serial scheduled stress;
- non-accepting authority and explicit shadow-route refusal.

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/tests/test_cadence_runner.py` | yes | forcing behavior |
| Governing overview | `onboarding/mcp/tests/overview.md` | yes | test-area model |
| Producer | `mcp/test_support/agents_remember_test_support/testing/cadence_runner.py` | yes | contract owner |

## Known Traps

- A passing mocked subprocess is not proof unless the command and emitted population are checked.

## Questions To Resolve

None.

## Done When

- The strict one-to-one sidecar records admission, trigger, and non-accepting boundaries.
