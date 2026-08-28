# File Card — mcp/tests/test_causal_quality_preflight.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/tests/test_causal_quality_preflight.py` |
| targetOnboardingFile | `onboarding/mcp/tests/test_causal_quality_preflight.py.md` |
| generated | 2026-08-28T06:28+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | quality continuation contract |
| Risk | broken causal evidence suppresses real tests |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-005 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `onboarding/mcp/tests/overview.md` |
| ancestorOverviews | `onboarding/overview.md`, `onboarding/mcp/overview.md` |
| localArea | Python evidence tests |

## Why This File Matters

It forces valid causal suppression to coexist with independent pytest continuation and forces
invalid evidence into broader unsuppressed safe mode.

## What The Worker Must Explain

- valid-report continuation;
- missing/invalid-report safe mode;
- overall failure preservation;
- absence of silent pytest omission.

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/tests/test_causal_quality_preflight.py` | yes | wrapper forcing behavior |
| Governing overview | `onboarding/mcp/tests/overview.md` | yes | test-area model |
| Plan owner | `mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py` | yes | continuation policy |

## Known Traps

- A broken preflight is not permission to skip pytest.

## Questions To Resolve

None.

## Done When

- The sidecar distinguishes valid exact suppression from unsuppressed safe mode.
