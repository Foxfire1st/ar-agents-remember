# File Card — mcp/test_support/agents_remember_test_support/testing/cadence_runner.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/test_support/agents_remember_test_support/testing/cadence_runner.py` |
| targetOnboardingFile | `mcp/test_support/agents_remember_test_support/testing/cadence_runner.py.md` |
| generated | 2026-08-25T02:13+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | non-accepting Dagger cadence executor |
| Risk | scheduled evidence becoming a second gate |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-003 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `mcp/test_support/agents_remember_test_support/testing/overview.md` |
| ancestorOverviews | `overview.md`, `mcp/overview.md` |

## Why This File Matters

[HIGH] This command runs stress, provider-bump, and migration evidence in the pinned environment while explicitly refusing acceptance authority.

## What The Worker Must Explain

- Dagger admission and lifecycle validation
- closed supported trigger set
- serial pytest and structured artifacts
- not-applicable migration population

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/test_support/agents_remember_test_support/testing/cadence_runner.py` | yes | concrete current behavior |
| Governing overview | `mcp/test_support/agents_remember_test_support/testing/overview.md` | yes | route authority |
| Target sidecar | `mcp/test_support/agents_remember_test_support/testing/cadence_runner.py.md` | yes | durable one-to-one onboarding |

## Files The Worker May Read

- `mcp/test_support/agents_remember_test_support/testing/cadence_runner.py`
- `mcp/test_support/agents_remember_test_support/testing/overview.md`
- `mcp/test_support/agents_remember_test_support/testing/cadence_runner.py.md`
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

- Do not add release or direct-diagnostic triggers.
- Every result must remain acceptanceEligible=false and certifying=false.

## Questions To Resolve

None.

## Done When

- The exact sidecar exists and explains current ownership and non-ownership.
- The governing overview routes readers to the new owner.
- Deleted predecessor authority is not preserved through a fallback or stale sidecar.
- Generated route indexes include the sidecar after the final content pass.
