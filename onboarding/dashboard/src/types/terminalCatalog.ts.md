# dashboard/src/types/terminalCatalog.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/types/terminalCatalog.ts`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-25T22:27+02:00 |
| lastVerifiedCommitHash |  `c51373425be3e3f488590ad2f444810df89b4ffb`|
| lastVerifiedCommitDate |  2026-08-26T19:22:10+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Mirrors the terminal-catalog wire row consumed by the dashboard. The current binding fields are
`taskDocumentRef` plus `seatRole`; replacement declares the same structural document independently
of runtime session identity.

## Code Commentary

### Logic

`TerminalCatalogRow` carries runtime transport/status, structural binding, replacement declaration,
spawn provenance, control evidence, and terminal outcome. `dispatchBriefEntryId` is an optional
private control-plane receipt proving which durable pinned brief completed the current generation's
spawn transaction. `TaskDocumentRef` is declared locally as the canonical `{repository, path}`
shape used by this catalog wire; it is not imported from the generated projection module. The full
catalog interface now has 66 fields and is checked bidirectionally against the server response
model.

### Conventions

`seatRole` is current binding and `spawnRole` is provenance. Optionality mirrors catalog rows
during creation/migration; current server writers use the structural fields.

### Invariants And Boundaries

- `leafKey` and `replacementForLeaf` are not current wire fields.
- Task document plus role is the stable seat; `id` is the occupant.
- Replacement provenance does not create a second seat identity.
- `dispatchBriefEntryId` is reconciliation/diagnostic evidence, never a destination or public seat
  identity.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The wire row separates runtime identity, structural binding, replacement, and dispatch receipt evidence. | `TerminalCatalogRow` | dashboard/src/types/terminalCatalog.ts:31-115 |
| The canonical task-document pair is declared locally for this catalog wire. | `TaskDocumentRef` | dashboard/src/types/terminalCatalog.ts:19-22 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History
- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2 final curation: corrected the false generated-import
  claim, refreshed the current interface ranges, and recorded the bidirectional 66-field parity
  boundary. Verification remains closeout-owned.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: added the optional private
  `dispatchBriefEntryId` projection without changing structural seat identity. Verification remains
  closeout-owned.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current data-contract card for `terminalCatalog.ts` with task-document identity, qualified seat state, and terminal projections represented by this source.
- 2026-08-10T04:39+02:00 — 260713-TES-L6: recorded the additive sprint-provenance wire fields and
  their legacy-absence semantics. Verification metadata remains pinned until closeout stamps the
  code commit.

- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 5 repository-reference citations (5/5 anchored and sourced; scoped citation check clean).

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
