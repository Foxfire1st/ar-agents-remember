# File Card — mcp/test_support/agents_remember_test_support/testing/evidence_provenance.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | mcp/test_support/agents_remember_test_support/testing/evidence_provenance.py |
| targetOnboardingFile | mcp/test_support/agents_remember_test_support/testing/evidence_provenance.py.md |
| generated | 2026-08-28T05:10+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | shared exact-candidate and machine provenance publisher |
| Risk | evidence can be compared or reused across different candidates or machines without detectable drift |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-005 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | mcp/test_support/agents_remember_test_support/testing/overview.md |
| ancestorOverviews | overview.md, mcp/overview.md |
| localArea | non-accepting Dagger evidence |

## Why This File Matters

[HIGH] Q5-Q8 need one shared candidate/machine identity instead of route-specific untyped dictionaries
that can drift or support false same-candidate claims.

## What The Worker Must Explain

- complete candidate snapshot
- explicit machine/runtime facts and environment digest
- Dagger admission
- provenance-only, non-accepting altitude

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | mcp/test_support/agents_remember_test_support/testing/evidence_provenance.py | yes | shared schema |
| Candidate owner | mcp/test_support/agents_remember_test_support/testing/candidate_snapshot.py | yes | exact Git identity |
| Route consumers | cadence_runner.py; retry_evidence_route.py; route_measurement.py | yes | schema use |
| Target sidecar | mcp/test_support/agents_remember_test_support/testing/evidence_provenance.py.md | yes | durable onboarding |

## Files The Worker May Read

- evidence_provenance.py
- candidate_snapshot.py
- cadence_runner.py
- retry_evidence_route.py
- route_measurement.py
- testing/overview.md

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

- Do not infer machine identity from the image tag alone.
- Do not let provenance mint acceptance.
- Do not omit staged-tree or working-path identity.

## Questions To Resolve

None.

## Done When

- Exact sidecar explains shared identity and limits.
- Route overview names the owner.
- Generated testing index contains the sidecar.
