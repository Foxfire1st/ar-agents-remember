# File Card — mcp/tests/_evidence_catalog_fixture.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/tests/_evidence_catalog_fixture.py` |
| targetOnboardingFile | `mcp/tests/_evidence_catalog_fixture.py.md` |
| generated | 2026-08-25T02:13+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | lifecycle catalog test builder |
| Risk | many tests reimplementing catalog shape |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-003 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `mcp/tests/overview.md` |
| ancestorOverviews | `overview.md`, `mcp/overview.md` |

## Why This File Matters

[HIGH] This is the one synthetic builder for focused lifecycle-policy tests; it centralizes complete valid rows so forcing tests vary only the rule under test.

## What The Worker Must Explain

- minimal complete catalog construction
- artifact and replacement fixtures
- temporary root confinement
- catalog support rather than product authority

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/tests/_evidence_catalog_fixture.py` | yes | concrete current behavior |
| Governing overview | `mcp/tests/overview.md` | yes | route authority |
| Target sidecar | `mcp/tests/_evidence_catalog_fixture.py.md` | yes | durable one-to-one onboarding |

## Files The Worker May Read

- `mcp/tests/_evidence_catalog_fixture.py`
- `mcp/tests/overview.md`
- `mcp/tests/_evidence_catalog_fixture.py.md`
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

- Do not let the builder become a production catalog reader.
- A generated test catalog cannot prove external evidence fidelity.

## Questions To Resolve

None.

## Done When

- The exact sidecar exists and explains current ownership and non-ownership.
- The governing overview routes readers to the new owner.
- Deleted predecessor authority is not preserved through a fallback or stale sidecar.
- Generated route indexes include the sidecar after the final content pass.
