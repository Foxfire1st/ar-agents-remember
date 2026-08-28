# File Card — mcp/test_support/agents_remember_test_support/testing/evidence_governance.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | mcp/test_support/agents_remember_test_support/testing/evidence_governance.py |
| targetOnboardingFile | mcp/test_support/agents_remember_test_support/testing/evidence_governance.py.md |
| generated | 2026-08-28T05:10+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | complete durable-evidence discovery policy |
| Risk | an undiscovered suffix or self-referential catalog can make lifecycle coverage incomplete or impossible |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-005 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | mcp/test_support/agents_remember_test_support/testing/overview.md |
| ancestorOverviews | overview.md, mcp/overview.md |
| localArea | durable evidence lifecycle |

## Why This File Matters

[HIGH] This predicate defines what the lifecycle catalog must cover; fixed-suffix drift or accidental
self-cataloging would silently omit evidence or create an unsatisfiable recursive contract.

## What The Worker Must Explain

- known durable and unknown threshold-driven discovery
- shared-support and task/date proof discovery
- positive threshold refusal
- lifecycle catalog as policy input, not its own artifact

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | mcp/test_support/agents_remember_test_support/testing/evidence_governance.py | yes | discovery authority |
| Lifecycle consumer | mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py | yes | complete-catalog validation |
| Focused test | mcp/tests/test_evidence_lifecycle.py | yes | threshold and self-catalog forcing |
| Target sidecar | mcp/test_support/agents_remember_test_support/testing/evidence_governance.py.md | yes | durable onboarding |

## Files The Worker May Read

- evidence_governance.py
- evidence_lifecycle.py
- test_evidence_lifecycle.py
- testing/overview.md

## Files The Worker Must Not Read Without Escalation

- unrelated runtime routes
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

- Do not add a permissive unknown-suffix fallback.
- Do not catalog the lifecycle catalog inside itself.
- Do not classify ordinary Python implementation files as fixtures.

## Questions To Resolve

None.

## Done When

- Exact sidecar explains discovery and non-ownership.
- Threshold and self-catalog boundaries have forcing citations.
- Generated testing index contains the owner.
