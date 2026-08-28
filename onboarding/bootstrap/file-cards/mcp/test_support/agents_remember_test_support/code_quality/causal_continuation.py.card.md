# File Card — mcp/test_support/agents_remember_test_support/code_quality/causal_continuation.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | mcp/test_support/agents_remember_test_support/code_quality/causal_continuation.py |
| targetOnboardingFile | mcp/test_support/agents_remember_test_support/code_quality/causal_continuation.py.md |
| generated | 2026-08-28T04:48+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | causal-preflight safe-continuation policy |
| Risk | invalid evidence could suppress independent or affected tests |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-005 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | mcp/test_support/agents_remember_test_support/code_quality/overview.md |
| ancestorOverviews | overview.md, mcp/overview.md |
| localArea | Dagger causal-quality continuation |

## Why This File Matters

[HIGH] This is the fail-safe boundary that prevents a broken causal report from becoming authority
to skip tests.

## What The Worker Must Explain

- process/report consistency pairs
- unavailable-evidence safe mode
- separation from dependency derivation
- preservation of the failing preflight result

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | mcp/test_support/agents_remember_test_support/code_quality/causal_continuation.py | yes | current policy |
| Governing overview | mcp/test_support/agents_remember_test_support/code_quality/overview.md | yes | route authority |
| Execution facade | mcp/test_support/agents_remember_test_support/code_quality/check.py | yes | consuming behavior |
| Target sidecar | mcp/test_support/agents_remember_test_support/code_quality/causal_continuation.py.md | yes | durable one-to-one onboarding |

## Files The Worker May Read

- causal_continuation.py
- check.py
- testing/causal_failures.py
- focused causal-preflight tests
- the governing overview

## Files The Worker Must Not Read Without Escalation

- unrelated test routes
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

- Do not treat unreadable evidence as a causal failure.
- Do not let a zero process exit override a failed report.
- Do not turn safe mode into a passing quality result.

## Questions To Resolve

None.

## Done When

- Exact sidecar exists.
- The quality overview routes the safe-mode owner.
- Generated route indexes contain the new sidecar.
