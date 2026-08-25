# mcp/src/agents_remember/testing/cohort_manifest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/cohort_manifest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Python test infrastructure overview](overview.md)

## Purpose

Loads and validates the exact content-sealed direct-diagnostic cohort manifest.

## Code Commentary

### Logic

It validates schema, file/config hashes, node selectors, import closure, population limits, unique ownership, and reachability without auto-refreshing the approved cohort.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Paths, nodes, imports, effects, and content hashes must match exactly; any unknown, changed, oversized, or unreachable member refuses direct execution.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `COHORT_MANIFEST_PATH` | mcp/src/agents_remember/testing/cohort_manifest.py:1-379 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `COHORT_MANIFEST_PATH` | mcp/src/agents_remember/testing/cohort_manifest.py:1-379 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `COHORT_MANIFEST_PATH` | mcp/src/agents_remember/testing/cohort_manifest.py:1-379 |

## Update History

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
