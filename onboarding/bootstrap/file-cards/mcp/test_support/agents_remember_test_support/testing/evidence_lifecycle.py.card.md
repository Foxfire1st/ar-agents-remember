# File Card — mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py` |
| targetOnboardingFile | `mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py.md` |
| generated | 2026-08-25T02:13+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | durable evidence lifecycle authority |
| Risk | stale or self-authored evidence entering acceptance |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-003 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `mcp/test_support/agents_remember_test_support/testing/overview.md` |
| ancestorOverviews | `overview.md`, `mcp/overview.md` |

## Why This File Matters

[HIGH] This file makes evidence authority, fidelity, cadence, lifetime, expiry, replacement, and consumers executable instead of relying on fixture folklore.

## What The Worker Must Explain

- closed metadata enums and inventory loading
- governed artifact census and replacement-node AST validation
- expiry, permanence, versioning, and migration constraints
- full-delta error accumulation

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py` | yes | concrete current behavior |
| Governing overview | `mcp/test_support/agents_remember_test_support/testing/overview.md` | yes | route authority |
| Target sidecar | `mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py.md` | yes | durable one-to-one onboarding |

## Files The Worker May Read

- `mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py`
- `mcp/test_support/agents_remember_test_support/testing/overview.md`
- `mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py.md`
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

- Do not retain expired proof through prose or compatibility fields.
- Do not let an internal generator claim external-recorded authority.

## Questions To Resolve

None.

## Done When

- The exact sidecar exists and explains current ownership and non-ownership.
- The governing overview routes readers to the new owner.
- Deleted predecessor authority is not preserved through a fallback or stale sidecar.
- Generated route indexes include the sidecar after the final content pass.
