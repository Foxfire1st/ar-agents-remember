# File Card — mcp/tests/task_reopen_test_support.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/tests/task_reopen_test_support.py` |
| targetOnboardingFile | `mcp/tests/task_reopen_test_support.py.md` |
| generated | 2026-08-25T08:27+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | canonical task-reopen fixture world |
| Risk | duplicated fixtures silently weakening lineage or terminal-predecessor proof |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-004 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `mcp/tests/overview.md` |
| ancestorOverviews | `overview.md`, `mcp/overview.md`, `mcp/tests/overview.md` |
| localArea | task-reopen test construction |

## Why This File Matters

[HIGH] It centralizes the real branch, enclosure, runtime, and task-document world shared by the
task-reopen forcing family.

## What The Worker Must Explain

- terminal predecessor publication
- real branch lineage
- contract-scoped runtime and external-memory setup
- controlled leaf/master document variants

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/tests/task_reopen_test_support.py` | yes | canonical fixture construction behavior |
| Governing overview | `mcp/tests/overview.md` | yes | test-support ownership boundary |
| Target sidecar | `mcp/tests/task_reopen_test_support.py.md` | yes | durable one-to-one onboarding |

## Files The Worker May Read

- `mcp/tests/task_reopen_test_support.py`
- `mcp/tests/overview.md`
- `mcp/tests/task_reopen_test_support.py.md`
- direct test consumers needed to prove the shared fixture contract
- production task-reopen entrypoints referenced by the helper

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
| Docs References | no | helper contract is repository-internal |
| Repo-Internal References | yes | helper, its direct test consumers, and production reopen contract |
| Cross-Repo References | no | external-memory fixtures remain same-repository test evidence |

## Known Traps

- Do not treat the helper as production reopen authority.
- Do not replace exact lineage with default-branch assumptions.

## Questions To Resolve

None.

## Done When

- Exact sidecar explains fixture authority and non-authority.
- Tests overview routes the helper.
- Generated route indexes include the sidecar.
