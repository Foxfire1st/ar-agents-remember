# mcp/src/agents_remember/models/lifecycles/enclosure.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/enclosure.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash |  `bb65a2073228c5e143b055a470f39c6c9e2f4d9d`|
| lastVerifiedCommitDate |  2026-09-14T19:36:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Lifecycle models overview](overview.md)

## Purpose

Defines immutable enclosure locator, manifest, terminal archive, receipt, and cleanup argument contracts.

## Code Commentary

### Logic

Strict models bind repository/task identity, generation, contract digest, predecessor, archive
entries, removed working-state identities (`TerminalEnclosureArchive.removedWorkingState`), and
cleanup request evidence; validators require exact manifest, path, and removed-working-state
uniqueness proofs.

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
| No external domain source is required to establish this repository-owned implementation. | `TerminalEnclosurePredecessor` | mcp/src/agents_remember/models/lifecycles/enclosure.py:1-367 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `TerminalEnclosurePredecessor` | mcp/src/agents_remember/models/lifecycles/enclosure.py:1-367 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `TerminalEnclosurePredecessor` | mcp/src/agents_remember/models/lifecycles/enclosure.py:1-367 |

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/models/lifecycles/enclosure.py` changed since the recorded verification
  commit. Re-read the card against the frozen on-disk source and re-checked its claims and cited
  ranges: nothing this card asserts is falsified by the change, so no wording changed. Verification
  metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source gained the
  `TerminalEnclosureRemovedWorkingState` model, the `removedWorkingState` archive field and its
  uniqueness validator (the module is now 367 lines). Corrected the three file-extent citations
  (1-327 → 1-367) and stated the new archive obligation in the Logic summary. Verification metadata
  remains closeout-owned.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
