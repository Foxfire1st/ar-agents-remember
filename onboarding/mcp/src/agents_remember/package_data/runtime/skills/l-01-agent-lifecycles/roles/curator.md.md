# mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T14:40+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

This file is the packaged runtime artifact synchronized exactly from canonical
`skills/l-01-agent-lifecycles/roles/curator.md`. It carries the same curator lifecycle into installed
runtimes and owns no independent doctrine.

## Logic

Because synchronization replaces the complete canonical skill tree, the packaged curator has the
same leaf-scoped onboarding-only seat, three-way intent reconciliation, current/evidence/history
separation, and the single enclosure-checklist intake/repair loop as the canonical source. The
full scoped call combines missing-onboarding, quality, stale indexes, source-change candidates, and
noteworthy evidence; the curator reruns it until the zeroable count clears. Changes must be made
canonically and propagated; editing this artifact independently creates drift.

## Conventions

- Treat canonical `skills/` as the sole doctrine owner.
- Keep this artifact byte-identical through `scripts/sync-skills.py`.
- Describe packaged behavior only as synchronized canonical behavior.
- Verification provenance remains specific to this packaged source path.

## Invariants And Boundaries

- Package installation must not alter curator authority or workflow.
- This artifact cannot introduce a compatibility lifecycle or task-specific override.
- Curator still writes onboarding only and communicates through structural parent messaging/report.
- The synchronized curator cannot report completion with an enforced curator-actionable finding.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The packaged curator contains the same current seat definition and three-way responsibility. | "## What This Seat Is" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:7-47 |
| The synchronized check loop requires complete curator-actionable repair before report. | "### 4 — Iterate The Checklist, Then Report" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:136-191 |
| The canonical source is the doctrine owner. | "# Lifecycle — Curator" | skills/l-01-agent-lifecycles/roles/curator.md:1-47 |
| MCP package data is an explicit synchronization target. | "mcp package data" | scripts/sync-skills.py:43-47 |
| Synchronization replaces each target from the canonical tree and then checks equality. | `sync_target`; `check_targets` | scripts/sync-skills.py:136-157; scripts/sync-skills.py:179-203 |

## Update History

- 2026-08-11T16:54+02:00 — Synchronized the single enclosure-checklist intake/repair loop and its
  zeroable curator gate without creating copy-specific doctrine.
- 2026-08-11T14:40+02:00 — Synchronized the curator-owned missing-onboarding/full-quality
  completion condition without creating copy-specific doctrine.
- 2026-08-11T14:25+02:00 — Replaced accumulated copy-specific/task-delta prose with the exact
  synchronized-artifact contract and current packaged-source evidence.
- 2026-08-09T13:59+02:00 — Synchronized fact-relay supervision wording from canonical doctrine.
- 2026-08-08T22:10+02:00 — Synchronized the agent-notifier naming wave.
- 2026-07-12T18:11+02:00 — Established packaged curator lifecycle coverage.
