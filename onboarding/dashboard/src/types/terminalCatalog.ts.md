# dashboard/src/types/terminalCatalog.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/types/terminalCatalog.ts`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-26T15:40+0200                            |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f`       |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The TypeScript mirror of the **FULL terminal-catalog row**:
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
- **`TerminalCatalogRow`** (L24-L93) — the full row: identity/transport (id, label, kind, cwd,
  tmuxName, `command?` — always serialized by the server, optional here because no cockpit
  surface consumes it, existing fixtures omit it), timestamps + status, leaf identity
  (`leafKey`, `seatRole` — always serialized, the server migrates legacy rows;
  `replacementForLeaf`), spawn provenance (`spawnedBySession/Lifecycle`, `spawnRole`,
  `launchArgs`/`promptKeywords`/`sessionCommands`, `spawnLevel` + `spawnLevelSource`),
  **requested** model/effort (`resolvedModel`/`resolvedEffort` — settings-resolved argv pins,
  NEVER proof of the effective pair; evidence tiers live in `sessionCockpitStore`, L4), control
  metadata (`controlState/Endpoint/Protocol/Activity/Acceptance/VendorSessionId/
  PendingInteraction/LastEventSequence/Raw`) plus the **additive plural
  `controlPendingInteractions`** (L69-L71 — multiplexed harness sub-agent pendings,
  review R6; the singular slot above stays the parent-thread entry), liveness
  evidence, retirement provenance (`retiredAt/BySession/Reason/Edge`), landing provenance
  (`landedAt/Reason/Edge`), the frozen `spawnedLabel`, and `turnState` + `turnStateChangedAt`.

### Invariants And Boundaries

- Reviewer-verified key-by-key against `to_json()`: every declared field is actually serialized —
  nothing invented. Any server field addition lands HERE first, then in consumers.
- `resolvedModel`/`resolvedEffort` are REQUESTED provenance; presenting them as effective anywhere
  is an honesty violation (R7 renders them "(requested)" until the tier proves better).
- The plural `controlPendingInteractions` is strictly ADDITIVE: the singular slot remains the
  parent-thread entry, and multiplexing bridges carry the parent in BOTH slots — consumers must de-duplicate
  by interactionId (see `data/interactionAnswer.ts` `pendingInteractionPayloads`) rather than
  assume the sets are disjoint.
- The one hand-maintained wire mirror for the catalog; `data/terminal.ts` must keep re-exporting
  rather than re-declaring.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The unions, opaque diagnostics keys, and the full row shape (incl. the additive plural pending slot). | L7-L93 | [terminalCatalog.ts](terminalCatalog.ts) |
| The Python source of truth (`TerminalCatalogEntry.to_json()`; both pending slots serialized). | L118-L121; L225-L293 | [terminal_catalog.py](../../../mcp/src/agents_remember/serving/terminal_catalog.py) |
| The re-export seam preserving existing import sites. | L318-L327 | [../data/terminal.ts](../data/terminal.ts) |
| The `OpenSession` mapping that carries these fields into the client registry. | L73-L74; L488-L525 | [../data/sessions.ts](../data/sessions.ts) |
| The sibling hand-mirrored wire type this follows the posture of. | — | [projection.ts](projection.ts) |
| The full-wire-shape fixtures built on this type (FLEET + appended packs, incl. the `L7_*` multiplexed seat). | L10-L172; L174-L446 | [../test/fixtures/catalogRows.ts](../test/fixtures/catalogRows.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## Update History

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: documented the additive plural
  `controlPendingInteractions` field (L69-L71 — multiplexed harness sub-agent pendings; the
  singular slot stays the parent-thread entry, bridges carry the parent in both slots) and added
  the both-slots/dedupe invariant. Refreshed stale citations (`to_json` now L225-L293, the
  terminal.ts re-export L318-L327, the OpenSession mapping L73-L74; L488-L525). The L7 code is
  uncommitted in the code worktree; closeout re-stamps verification.

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 R4 (full wire types): the complete
  `TerminalCatalogEntry.to_json()` mirror — status/control/turn-state vocabularies, named-but-
  opaque `controlRaw` diagnostics keys, spawn/level/requested-pair provenance, liveness evidence,
  and retirement/landing provenance — replacing the partial shape formerly declared in
  `data/terminal.ts` (now a re-export). Verification metadata pinned to the leaf base until
  closeout stamps the L2 code commit.
