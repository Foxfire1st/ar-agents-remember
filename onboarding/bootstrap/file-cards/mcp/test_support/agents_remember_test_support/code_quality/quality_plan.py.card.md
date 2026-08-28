# File Card — mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py |
| targetOnboardingFile | mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py.md |
| generated | 2026-08-28T04:48+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | typed quality-plan and progress owner |
| Risk | command-plan drift could silently change the certifying population or enforcement order |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-005 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | mcp/test_support/agents_remember_test_support/code_quality/overview.md |
| ancestorOverviews | overview.md, mcp/overview.md |
| localArea | Dagger-only Python quality planning |

## Why This File Matters

[HIGH] The extracted module is the single typed plan consumed by the Dagger quality facade; a
second plan builder would recreate the duplicated-policy failure this split prevents.

## What The Worker Must Explain

- immutable CheckConfig and Step contracts
- atomic bounded progress state
- delegated scope ownership
- exact rail order and report-only distinction
- Dagger-gated pytest command construction
- facade compatibility without a second entrypoint

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py | yes | concrete plan contract |
| Governing overview | mcp/test_support/agents_remember_test_support/code_quality/overview.md | yes | route authority |
| Execution facade | mcp/test_support/agents_remember_test_support/code_quality/check.py | yes | proves the ownership split |
| Target sidecar | mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py.md | yes | durable one-to-one onboarding |

## Files The Worker May Read

- mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py
- mcp/test_support/agents_remember_test_support/code_quality/check.py
- mcp/test_support/agents_remember_test_support/code_quality/scope.py
- mcp/test_support/agents_remember_test_support/code_quality/overview.md
- the focused tests that consume check.quality_steps

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

- Do not document quality_plan.py as a runnable acceptance gate.
- Do not duplicate scope policy or execution result logic here.
- Do not remove the check.py re-export contract without an approved caller migration.

## Questions To Resolve

None.

## Done When

- The exact sidecar explains plan ownership and non-ownership.
- check.py onboarding explains the stable facade.
- The generated route index contains the new sidecar.
