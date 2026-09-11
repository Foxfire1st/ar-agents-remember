# mcp/src/agents_remember/models/lifecycles/enclosure.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/enclosure.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Lifecycle models overview](overview.md)

## Purpose

Defines immutable enclosure locator, manifest, terminal archive, receipt, and cleanup argument contracts.

## Code Commentary

### Logic

Strict models bind repository/task identity, generation, contract digest, predecessor, archive entries, and cleanup request evidence; validators require exact manifest and path proofs.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- The locator-manifest-journal address chain is exact; terminal cleanup requires replayable archive proof; duplicate or mismatched paths/digests refuse.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `TerminalEnclosurePredecessor` | mcp/src/agents_remember/models/lifecycles/enclosure.py:1-327 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `TerminalEnclosurePredecessor` | mcp/src/agents_remember/models/lifecycles/enclosure.py:1-327 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `TerminalEnclosurePredecessor` | mcp/src/agents_remember/models/lifecycles/enclosure.py:1-327 |

## Update History

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
