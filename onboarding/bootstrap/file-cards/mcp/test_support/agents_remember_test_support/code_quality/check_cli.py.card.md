# File Card — mcp/test_support/agents_remember_test_support/code_quality/check_cli.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/test_support/agents_remember_test_support/code_quality/check_cli.py` |
| targetOnboardingFile | `mcp/test_support/agents_remember_test_support/code_quality/check_cli.py.md` |
| generated | 2026-08-25T08:27+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | quality-wrapper CLI policy owner |
| Risk | parser drift creates an undocumented narrowing or apparent second gate |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-004 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `mcp/overview.md` |
| ancestorOverviews | `overview.md`, `mcp/overview.md` |
| localArea | Python quality wrapper policy |

## Why This File Matters

[HIGH] The extracted parser is the public argument vocabulary for the Python quality wrapper, but
must not acquire execution or acceptance authority.

## What The Worker Must Explain

- derived full/targeted policy arguments
- evidence-output path family
- no caller-selected path scope
- parser versus execution authority

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/test_support/agents_remember_test_support/code_quality/check_cli.py` | yes | concrete parser vocabulary and defaults |
| Governing overview | `mcp/overview.md` | yes | MCP quality-boundary authority |
| Target sidecar | `mcp/test_support/agents_remember_test_support/code_quality/check_cli.py.md` | yes | durable one-to-one onboarding |

## Files The Worker May Read

- `mcp/test_support/agents_remember_test_support/code_quality/check_cli.py`
- `mcp/test_support/agents_remember_test_support/code_quality/check.py`
- `mcp/overview.md`
- `mcp/test_support/agents_remember_test_support/code_quality/check_cli.py.md`
- directly importing entrypoints needed to prove parser ownership

## Files The Worker Must Not Read Without Escalation

- unrelated quality implementation routes
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
| Docs References | no | no domain documentation is needed for the local parser split |
| Repo-Internal References | yes | parser owner and consuming quality entrypoint |
| Cross-Repo References | no | no adjacent-repository boundary is owned |

## Known Traps

- Do not document the parser as a standalone quality runner.
- Do not imply direct host execution becomes certifying.

## Questions To Resolve

None.

## Done When

- Exact sidecar exists with current source citations.
- MCP overview routes parser ownership without duplicating the gate.
- Generated route indexes include the sidecar.
