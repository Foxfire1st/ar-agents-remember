# File Card — mcp/src/agents_remember/code_quality/causal_preflight.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/src/agents_remember/code_quality/causal_preflight.py` |
| targetOnboardingFile | `mcp/src/agents_remember/code_quality/causal_preflight.py.md` |
| generated | 2026-08-25T02:13+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | owner-level prerequisite validator |
| Risk | high-fanout root failure becoming hundreds of symptoms |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-003 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `mcp/overview.md` |
| ancestorOverviews | `overview.md`, `mcp/overview.md` |

## Why This File Matters

[HIGH] This file validates a reproduced high-fanout contract once at its actual owner and emits exact proven consumers without moving the owner logic into test infrastructure.

## What The Worker Must Explain

- typed preflight specs and stable cause IDs
- canonical lifecycle terminalization preflight
- candidate/environment/attempt binding
- proven-edge-only blocked groups

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/src/agents_remember/code_quality/causal_preflight.py` | yes | concrete current behavior |
| Governing overview | `mcp/overview.md` | yes | route authority |
| Target sidecar | `mcp/src/agents_remember/code_quality/causal_preflight.py.md` | yes | durable one-to-one onboarding |

## Files The Worker May Read

- `mcp/src/agents_remember/code_quality/causal_preflight.py`
- `mcp/overview.md`
- `mcp/src/agents_remember/code_quality/causal_preflight.py.md`
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

- Do not add speculative preflights without reproduced cascade evidence.
- A failed preflight still fails the quality result.

## Questions To Resolve

None.

## Done When

- The exact sidecar exists and explains current ownership and non-ownership.
- The governing overview routes readers to the new owner.
- Deleted predecessor authority is not preserved through a fallback or stale sidecar.
- Generated route indexes include the sidecar after the final content pass.
