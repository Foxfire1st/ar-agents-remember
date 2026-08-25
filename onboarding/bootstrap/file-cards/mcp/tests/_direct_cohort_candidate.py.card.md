# File Card — mcp/tests/_direct_cohort_candidate.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/tests/_direct_cohort_candidate.py` |
| targetOnboardingFile | `mcp/tests/_direct_cohort_candidate.py.md` |
| generated | 2026-08-25T02:13+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | sealed direct diagnostic candidate support |
| Risk | diagnostic cohort executing complex or stateful helpers |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-003 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `mcp/tests/overview.md` |
| ancestorOverviews | `overview.md`, `mcp/overview.md` |

## Why This File Matters

[HIGH] These deliberately inert functions are the only direct-cohort execution population and keep timing/eligibility proof independent from the production suite.

## What The Worker Must Explain

- seven exact top-level nodes
- no fixtures, parametrization, imports with effects, or state mutation
- content hash and symbol closure binding
- cataloged shared-support status

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/tests/_direct_cohort_candidate.py` | yes | concrete current behavior |
| Governing overview | `mcp/tests/overview.md` | yes | route authority |
| Target sidecar | `mcp/tests/_direct_cohort_candidate.py.md` | yes | durable one-to-one onboarding |

## Files The Worker May Read

- `mcp/tests/_direct_cohort_candidate.py`
- `mcp/tests/overview.md`
- `mcp/tests/_direct_cohort_candidate.py.md`
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

- Do not add behavior merely to increase cohort size.
- Any byte change requires deliberate manifest re-audit.

## Questions To Resolve

None.

## Done When

- The exact sidecar exists and explains current ownership and non-ownership.
- The governing overview routes readers to the new owner.
- Deleted predecessor authority is not preserved through a fallback or stale sidecar.
- Generated route indexes include the sidecar after the final content pass.
