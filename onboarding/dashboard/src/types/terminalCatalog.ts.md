# dashboard/src/types/terminalCatalog.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/types/terminalCatalog.ts`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T02:30+02:00                           |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The TypeScript mirror of the **FULL terminal-catalog row** (260715-FEUI-L2 R4):
`mcp/src/agents_remember/serving/terminal_catalog.py` `TerminalCatalogEntry.to_json()`, served
verbatim by `GET /api/terminal/sessions` (`serving/app.py` `_catalog_payload`). The Python entry
is the source of truth — kept in lockstep BY HAND, camelCase to match the wire form,
written-only-when-set fields optional (`?:`) — the same posture as `types/projection.ts`. It
replaces the former partial `TerminalSessionInfo` in `data/terminal.ts`, which now re-exports
`TerminalCatalogRow as TerminalSessionInfo` so existing consumers keep their import site.

## Code Commentary

### Logic

- **Vocabulary unions** (L7-L15): `TerminalOpenKind`, `TerminalSessionStatus`
  (`running|exited|landed|terminated`), `HarnessControlState`, `HarnessActivityState`,
  `HarnessAcceptanceState`, `SeatTurnState` (`working|turn-ended|awaiting-input|stale` —
  classified on the 10 s sweep cadence; ABSENT means unclassified, never a fabricated state),
  `TerminalLivenessEvidence` (`tmux-command-failed|pane-gone`).
- **`ControlRawDiagnostics`** (L19-L22): `controlRaw` is the retained verbatim adapter state; the
  two keys the cockpit reads (`bridgeError`, `paneDiagnostic`) are NAMED but typed opaque
  (`unknown`) — the backend retains vendor payloads the UI must not re-shape.
- **`TerminalCatalogRow`** (L24-L90) — the full row: identity/transport (id, label, kind, cwd,
  tmuxName, `command?` — always serialized by the server, optional here because no cockpit
  surface consumes it, existing fixtures omit it), timestamps + status, leaf identity
  (`leafKey`, `seatRole` — always serialized, the server migrates legacy rows;
  `replacementForLeaf`), spawn provenance (`spawnedBySession/Lifecycle`, `spawnRole`,
  `launchArgs`/`promptKeywords`/`sessionCommands`, `spawnLevel` + `spawnLevelSource`),
  **requested** model/effort (`resolvedModel`/`resolvedEffort` — settings-resolved argv pins,
  NEVER proof of the effective pair; evidence tiers live in `sessionCockpitStore`, L4), control
  metadata (`controlState/Endpoint/Protocol/Activity/Acceptance/VendorSessionId/
  PendingInteraction/LastEventSequence/Raw`), liveness evidence, retirement provenance
  (`retiredAt/BySession/Reason/Edge`), landing provenance (`landedAt/Reason/Edge`), the frozen
  `spawnedLabel`, and `turnState` + `turnStateChangedAt`.

### Invariants And Boundaries

- Reviewer-verified key-by-key against `to_json()`: every declared field is actually serialized —
  nothing invented. Any server field addition lands HERE first, then in consumers.
- `resolvedModel`/`resolvedEffort` are REQUESTED provenance; presenting them as effective anywhere
  is an honesty violation (R7 renders them "(requested)" until the tier proves better).
- The one hand-maintained wire mirror for the catalog; `data/terminal.ts` must keep re-exporting
  rather than re-declaring.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The unions, opaque diagnostics keys, and the full row shape. | L7-L90 | [terminalCatalog.ts](terminalCatalog.ts) |
| The Python source of truth (`TerminalCatalogEntry.to_json()`). | L219-L287 | [terminal_catalog.py](../../../mcp/src/agents_remember/serving/terminal_catalog.py) |
| The re-export seam preserving existing import sites. | L267-L281 | [../data/terminal.ts](../data/terminal.ts) |
| The `OpenSession` mapping that carries these fields into the client registry. | L406-L455 | [../data/sessions.ts](../data/sessions.ts) |
| The sibling hand-mirrored wire type this follows the posture of. | — | [projection.ts](projection.ts) |
| The full-wire-shape fixtures built on this type. | L10-L172 | [../test/fixtures/catalogRows.ts](../test/fixtures/catalogRows.ts) |

## Update History

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 R4 (full wire types): the complete
  `TerminalCatalogEntry.to_json()` mirror — status/control/turn-state vocabularies, named-but-
  opaque `controlRaw` diagnostics keys, spawn/level/requested-pair provenance, liveness evidence,
  and retirement/landing provenance — replacing the partial shape formerly declared in
  `data/terminal.ts` (now a re-export). Verification metadata pinned to the leaf base until
  closeout stamps the L2 code commit.
