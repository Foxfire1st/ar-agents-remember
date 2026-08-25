# File Card — mcp/src/agents_remember/testing/causal_failures.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/src/agents_remember/testing/causal_failures.py` |
| targetOnboardingFile | `mcp/src/agents_remember/testing/causal_failures.py.md` |
| generated | 2026-08-25T02:13+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | pytest causal failure reporter |
| Risk | suppression hiding independent regressions |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-003 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `mcp/src/agents_remember/testing/overview.md` |
| ancestorOverviews | `overview.md`, `mcp/overview.md` |

## Why This File Matters

[HIGH] This plugin converts owner-preflight evidence into exact blocked consumers and preserves independent/process-sensitive failure reproduction data.

## What The Worker Must Explain

- graph-proven blocked-node collection behavior
- failure classes and retry semantics
- xdist worker versus controller publication
- JSON and Markdown reproduction evidence

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/src/agents_remember/testing/causal_failures.py` | yes | concrete current behavior |
| Governing overview | `mcp/src/agents_remember/testing/overview.md` | yes | route authority |
| Target sidecar | `mcp/src/agents_remember/testing/causal_failures.py.md` | yes | durable one-to-one onboarding |

## Files The Worker May Read

- `mcp/src/agents_remember/testing/causal_failures.py`
- `mcp/src/agents_remember/testing/overview.md`
- `mcp/src/agents_remember/testing/causal_failures.py.md`
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

- Incomplete ownership authorizes no blanket skip.
- A causal report is diagnostic evidence, never acceptance.

## Questions To Resolve

None.

## Done When

- The exact sidecar exists and explains current ownership and non-ownership.
- The governing overview routes readers to the new owner.
- Deleted predecessor authority is not preserved through a fallback or stale sidecar.
- Generated route indexes include the sidecar after the final content pass.
