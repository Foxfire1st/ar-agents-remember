# mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T14:25+02:00 |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d` |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

This file is the packaged runtime artifact synchronized exactly from canonical
`skills/l-01-agent-lifecycles/roles/manager.md`. It supplies installed runtimes with the same
one-real-master manager lifecycle and owns no separate intent.

## Logic

The packaged source therefore carries the canonical manager's structural leaf dispatch,
builder/reviewer/curator closeout chain, delegated gate authority, leaf/master quality altitudes,
subordinate cleanup, and durable master-handover contract unchanged. The sync process copies the
complete canonical tree; package-local edits are drift, not customization.

The synchronized quality altitude keeps leaf checks change-set scoped and runs
the full wrapper once at master integration with host-managed RAM/swap. Only a
constrained environment explicitly opts into `memoryCapBytes`.

## Conventions

- Change manager doctrine only in canonical `skills/`.
- Propagate and verify with `scripts/sync-skills.py`.
- Keep package-path provenance distinct while keeping content byte-identical.
- Do not append package-only task deltas or compatibility instructions.

## Invariants And Boundaries

- Installation cannot widen manager authority beyond one canonical master.
- Runtime packaging cannot expose child occupant ids to the manager model.
- Builder, reviewer, curator, closeout, and handover separation matches canonical doctrine exactly.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The packaged manager is one master-scoped owner of the leaf closeout chain. | "## What This Seat Is" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md:10-30 |
| Its hosted child dispatch uses structural task document and role. | "## Hosted Role Dispatch" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md:41-47 |
| The canonical source owns this doctrine. | "# Lifecycle — Manager" | skills/l-01-agent-lifecycles/roles/manager.md:1-47 |
| MCP package data is copied from canonical skills and checked for drift. | "mcp package data"; `sync_target`; `check_targets` | scripts/sync-skills.py:43-47; scripts/sync-skills.py:136-157; scripts/sync-skills.py:179-203 |

## L23 Manager And Leaf Admission

The packaged manager role starts only after the control plane proves its master
contains super for code/external memory. Every subordinate dispatch re-proves
the full chain before creating a child; refusal mutates no seat and carries the
ordered contract-addressed sync needed before retrying the same leaf.

## Update History
- 2026-08-12T20:10+02:00 — L23 curator: documented manager/leaf lineage admission without agent-held ids; verification remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: synchronized the
  canonical manager quality-altitude rule: full master gates use host-managed
  RAM/swap by default and only constrained CI opts into a hard cap.

- 2026-08-11T14:25+02:00 — Replaced duplicated history/task fragments with the exact synchronized
  manager-artifact contract and current source evidence.
- 2026-08-10T07:30+02:00 — Synchronized report-gated subordinate cleanup doctrine.
- 2026-08-09T13:59+02:00 — Synchronized fact-relay supervision wording.
- 2026-07-12T14:20+02:00 — Established packaged manager lifecycle coverage.
