# File Card — mcp/tests/_quality_evidence_fixture.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/tests/_quality_evidence_fixture.py` |
| targetOnboardingFile | `mcp/tests/_quality_evidence_fixture.py.md` |
| generated | 2026-08-25T08:27+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | canonical published-quality test fixture |
| Risk | dictionary-only mocks bypassing the evidence lifecycle actually consumed |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-004 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `mcp/tests/overview.md` |
| ancestorOverviews | `overview.md`, `mcp/overview.md`, `mcp/tests/overview.md` |
| localArea | quality evidence consumer fixtures |

## Why This File Matters

[HIGH] Lifecycle consumer tests need the immutable report generation a passing gate promises, not
only a mocked green return mapping.

## What The Worker Must Explain

- candidate-tree binding
- clean-executor report publication
- public gate summary
- test-only scope and private-access isolation

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/tests/_quality_evidence_fixture.py` | yes | exact published-evidence fixture behavior |
| Governing overview | `mcp/tests/overview.md` | yes | test-support ownership boundary |
| Target sidecar | `mcp/tests/_quality_evidence_fixture.py.md` | yes | durable one-to-one onboarding |

## Files The Worker May Read

- `mcp/tests/_quality_evidence_fixture.py`
- `mcp/tests/overview.md`
- `mcp/tests/_quality_evidence_fixture.py.md`
- direct lifecycle consumer tests that call the helper
- production quality publication owners imported by the helper

## Files The Worker Must Not Read Without Escalation

- unrelated test suites
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

## Reference Expectations

| Section | Expected? | Evidence Source |
| --- | --- | --- |
| Docs References | no | fixture contract is repository-internal |
| Repo-Internal References | yes | fixture, direct consumers, and production publication owner |
| Cross-Repo References | no | no adjacent-repository boundary is owned |

## Known Traps

- Do not promote fixture output to real acceptance evidence.
- Do not duplicate private publication calls across consumer tests.

## Questions To Resolve

None.

## Done When

- Exact sidecar explains why publication is required.
- Tests overview routes the helper.
- Generated route indexes include the sidecar.
