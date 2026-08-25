# File Card — mcp/src/agents_remember/testing/cohort_manifest.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/src/agents_remember/testing/cohort_manifest.py` |
| targetOnboardingFile | `mcp/src/agents_remember/testing/cohort_manifest.py.md` |
| generated | 2026-08-25T02:13+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | direct-cohort policy owner |
| Risk | content-sealed admission schema |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-003 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `mcp/src/agents_remember/testing/overview.md` |
| ancestorOverviews | `overview.md`, `mcp/overview.md` |

## Why This File Matters

[HIGH] This file is the sole strict schema and reachability owner for the tiny direct diagnostic cohort. Drift here can either execute unreviewed host tests or make the supported diagnostic route unusable.

## What The Worker Must Explain

- schema/policy v2 and hard population bounds
- exact paths, hashes, symbols, imports, effects, configuration, and node closures
- reachability of every audited file
- no auto-refresh, compatibility reader, or inferred population

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/src/agents_remember/testing/cohort_manifest.py` | yes | concrete current behavior |
| Governing overview | `mcp/src/agents_remember/testing/overview.md` | yes | route authority |
| Target sidecar | `mcp/src/agents_remember/testing/cohort_manifest.py.md` | yes | durable one-to-one onboarding |

## Files The Worker May Read

- `mcp/src/agents_remember/testing/cohort_manifest.py`
- `mcp/src/agents_remember/testing/overview.md`
- `mcp/src/agents_remember/testing/cohort_manifest.py.md`
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

- Do not turn seven nodes into a generic whole-repository analyzer.
- Do not treat manifest author statements as runtime evidence without candidate-byte verification.

## Questions To Resolve

None.

## Done When

- The exact sidecar exists and explains current ownership and non-ownership.
- The governing overview routes readers to the new owner.
- Deleted predecessor authority is not preserved through a fallback or stale sidecar.
- Generated route indexes include the sidecar after the final content pass.
