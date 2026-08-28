# File Card — mcp/tests/test_causal_failure_localization.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/tests/test_causal_failure_localization.py` |
| targetOnboardingFile | `onboarding/mcp/tests/test_causal_failure_localization.py.md` |
| generated | 2026-08-28T06:28+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | causal-localization forcing evidence |
| Risk | whole-file suppression or invented dependency closure |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-005 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `onboarding/mcp/tests/overview.md` |
| ancestorOverviews | `onboarding/overview.md`, `onboarding/mcp/overview.md` |
| localArea | Python evidence tests |

## Why This File Matters

It proves one failed owner blocks only source-derived exact dependent nodes and preserves
independent execution plus reproducible failure evidence.

## What The Worker Must Explain

- source-derived dependency authority;
- exact-node suppression;
- machine/human artifact parity;
- retained worker, seed, timing, family, and retry inputs.

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/tests/test_causal_failure_localization.py` | yes | forcing behavior |
| Governing overview | `onboarding/mcp/tests/overview.md` | yes | test-area model |
| Dependency owner | `mcp/test_support/agents_remember_test_support/testing/causal_dependency.py` | yes | source derivation |

## Known Traps

- A same-file node is not automatically dependent.

## Questions To Resolve

None.

## Done When

- The sidecar records exact-node, independent-continuation, and failure-evidence boundaries.
