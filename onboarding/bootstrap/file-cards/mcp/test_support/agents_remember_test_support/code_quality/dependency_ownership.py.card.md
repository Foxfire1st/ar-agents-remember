# File Card — mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py` |
| targetOnboardingFile | `mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py.md` |
| generated | 2026-08-25T02:13+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | canonical test-consumer graph |
| Risk | three quality layers disagreeing about affected tests |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-003 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `mcp/overview.md` |
| ancestorOverviews | `overview.md`, `mcp/overview.md` |

## Why This File Matters

[HIGH] Targeted selection, retry proof, and causal preflight all consume this one graph. Duplicating its logic recreates the implementation drift PDLS is meant to remove.

## What The Worker Must Explain

- module/import graph and declared lifecycle consumers
- complete typed selection reasons
- global inputs and safe-full fallback
- reverse-import and product coverage-root helpers

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py` | yes | concrete current behavior |
| Governing overview | `mcp/overview.md` | yes | route authority |
| Target sidecar | `mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py.md` | yes | durable one-to-one onboarding |

## Files The Worker May Read

- `mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py`
- `mcp/overview.md`
- `mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py.md`
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

- Do not optimize away real broad fan-out.
- Heuristics may select tests but cannot authorize causal suppression.

## Questions To Resolve

None.

## Done When

- The exact sidecar exists and explains current ownership and non-ownership.
- The governing overview routes readers to the new owner.
- Deleted predecessor authority is not preserved through a fallback or stale sidecar.
- Generated route indexes include the sidecar after the final content pass.
