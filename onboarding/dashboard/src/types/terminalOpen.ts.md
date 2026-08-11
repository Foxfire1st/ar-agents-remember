# dashboard/src/types/terminalOpen.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/types/terminalOpen.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-11T09:45+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`       |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Defines the strict terminal-open response union. Successful and seat-conflict responses expose the
structural task-document-and-role binding while the runtime session remains the opened occupant.

## Code Commentary

### Logic

The success body returns the accepted structural binding. `TerminalOpenSeatTakenBody` reports a
document-and-role conflict, and launch-conflict retains the live occupant's launch/binding facts.
Selection and kind refusals remain distinct.

### Conventions

The Python response models are authoritative; the TypeScript mirror is hand-maintained and covered by
contract fixtures.

### Invariants And Boundaries

- No leaf-key conflict body remains.
- Conflict identity is task document plus role.
- Requested model/effort provenance remains distinct from effective runtime evidence.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Success returns the accepted structural binding. | `TerminalOpenSuccessBody` | dashboard/src/types/terminalOpen.ts:10-26 |
| Seat conflicts use task-document and role identity. | `TerminalOpenSeatTakenBody` | dashboard/src/types/terminalOpen.ts:43-49 |
| Launch conflict remains a distinct live-occupant result. | `TerminalOpenConflictBody` | dashboard/src/types/terminalOpen.ts:51-63 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current data-contract card for `terminalOpen.ts` with task-document identity, qualified seat state, and terminal projections represented by this source.
- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 7 citation claims; scoped result 0 findings.

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R5 (open-route wire mirror): the 200
  success body (requested pair as provenance), 400 `launch-selection-invalid` (partial
  pair/non-native — the only synchronous refusal) and `bad-kind`, 409 `leaf-taken` (names the
  owner) and `launch-selection-conflict` (live retained pair, provenance never rewritten) —
  field-for-field against `app.py` per the L3 review. Verification metadata pinned to the leaf
  base until closeout stamps the L3 code commit.
