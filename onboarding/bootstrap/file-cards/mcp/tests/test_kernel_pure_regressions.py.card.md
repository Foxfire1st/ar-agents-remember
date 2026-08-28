# File Card — mcp/tests/test_kernel_pure_regressions.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | mcp/tests/test_kernel_pure_regressions.py |
| targetOnboardingFile | mcp/tests/test_kernel_pure_regressions.py.md |
| generated | 2026-08-28T05:10+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | retained pure-regression and representative-measurement cohort |
| Risk | Candidate A removal could accidentally delete unique assertions or preserve a shadow runner |
| Suggested action | replace retired cohort onboarding |
| Suggested wave | onboarding-wave-005 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | mcp/tests/overview.md |
| ancestorOverviews | overview.md, mcp/overview.md |
| localArea | explicit unit-regression evidence |

## Why This File Matters

[HIGH] It is the preservation boundary for Candidate A retirement: unique assertions remain, while
the command, classifier, manifest, and host execution authority do not.

## What The Worker Must Explain

- seven preserved product assertions
- ordinary pytest and explicit-lane status
- representative pure-cohort ownership
- absence of host execution or acceptance authority

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | mcp/tests/test_kernel_pure_regressions.py | yes | current assertions |
| Lane manifest | mcp/tests/test-evidence-lanes.toml | yes | explicit category |
| Measurement owner | mcp/test_support/agents_remember_test_support/testing/route_measurement.py | yes | exact consumer |
| Target sidecar | mcp/tests/test_kernel_pure_regressions.py.md | yes | durable one-to-one onboarding |

## Files The Worker May Read

- mcp/tests/test_kernel_pure_regressions.py
- mcp/tests/test-evidence-lanes.toml
- mcp/test_support/agents_remember_test_support/testing/route_measurement.py
- mcp/tests/overview.md

## Files The Worker Must Not Read Without Escalation

- unrelated product routes
- adjacent repositories
- broad task archives

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

- Do not describe this as a host diagnostic route.
- Do not recreate the retired sealed-cohort or static-closure machinery.
- Do not treat non-accepting route measurement as quality acceptance.

## Questions To Resolve

None.

## Done When

- The renamed source has exactly one current sidecar.
- Retired source sidecars and cards are absent.
- The test overview and generated route index name the current owner.
