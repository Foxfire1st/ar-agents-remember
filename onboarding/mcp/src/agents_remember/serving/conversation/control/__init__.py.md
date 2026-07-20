# mcp/src/agents_remember/serving/conversation/control/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

Marks the package that owns the implemented structured exact-session control surface (interrupt,
source-aware queue/withdrawal recovery, typed attachments, read-only policy, and evidence-bound
telemetry) landed by 260718-CHATS-L3.

## Code Commentary

### Logic

Contains only the package docstring; the sibling `api.py` owns the seventeen registered control
routes and each capability lives in its own focused module.

### Conventions

Keep the marker behavior-free; no control work executes at import time. The landed submission
authority remains the mutation owner — the control modules compose it, never a second queue.

### Invariants And Boundaries

- The package marker must not execute control work at import time.
- This package is not a third conversation read port or a second operation queue.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The sibling API module owns the registered control routes; the package overview governs the slice.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The sibling `api.py` owns the seventeen registered exact-session control routes. | L57-L570 | [control/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/api.py) |
| The governing route-local overview for the implemented control slice. | L1-L40 | [control/overview.md](agents-remember/mcp/src/agents_remember/serving/conversation/control/overview.md) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: updated the package-marker description from the
  reserved shell to the implemented control surface and repointed the governing overview to the new
  `control/overview.md` pillar. Verification stays pinned at the L3E base until L3 closeout stamps the
  candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the package-marker sidecar.
  Verification is blank until closeout commits and stamps the new source.
