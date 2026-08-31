# selection.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `scripts/e2e_harness/selection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T22:20:19+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `scripts/e2e_harness/overview.md` |

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Defines and evaluates the exact changed-path dependency surface that makes the expensive ambient
role-chat E2E applicable in targeted acceptance.

## Code Commentary

### Logic

`changed_paths` joins the committed diff with untracked candidate paths. `selected_paths` returns the
sorted intersection with explicit spawn, serving, Codex configuration, public-tool contract,
harness, and quality-graph prefixes. The self-updating starter config, full MCP registration route,
public-surface validator, and response-model registry are named inputs rather than implicit
dependencies.

### Conventions

Applicability is path-explicit and reviewable. A new load-bearing dependency must be added here rather
than hidden in a caller-side special case.

### Invariants And Boundaries

- Deleted and untracked paths participate in selection.
- Targeted skip requires an empty exact intersection.
- This module selects the E2E scenario only; the canonical Python test-consumer graph remains owned by
  `dependency_ownership.py`.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| Targeted applicability is an explicit repository-owned dependency contract. | `DEPENDENCY_PREFIXES` | scripts/e2e_harness/selection.py:8-74 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Base diff and untracked files are both included before prefix selection. | `changed_paths` | scripts/e2e_harness/selection.py:32-74 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| Selection contains no external repository authority. | `DEPENDENCY_PREFIXES` | scripts/e2e_harness/selection.py:8-74 |

## Update History

- 2026-08-30T22:20:19+02:00 — 260821-ARSPAWN-L5 converted source references to the
  canonical anchored citation format. Verification metadata remains closeout-owned.

- 2026-08-30T21:59:40+02:00 — 260821-ARSPAWN-L5: made untracked inputs executable
  selection truth and added exact Codex-config, registration, public-surface, and response-registry
  dependencies. Verification metadata remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 created onboarding for exact targeted E2E applicability. Verification metadata remains closeout-owned.
