# dashboard/src/panels/session-cockpit/ModelEffortControl.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/ModelEffortControl.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-02T01:42+02:00|
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Header-mounted live model/effort readout, exact-session picker, staged apply flow, and acceptance
chip surface.

## Code Commentary

### Logic

Opening the controlled popover fetches only the live session snapshot. The trigger reads effective
selection and source; model options are visible snapshot rows, and effort options are re-gated to
the staged model's session-settable row. Model-only and effort-only apply one set; an explicitly
staged pair enters the serialized model-then-effort flow. Fetch errors render verbatim with retry,
while the adjacent chip row exposes pending and completed evidence.

### Conventions

Staged values are requests, not markers, and reset on open/session changes. A staged model's
default effort is only a visual pre-highlight until the user explicitly selects it.

### Invariants And Boundaries

The control renders only for live harness sessions. It never reads the pre-session catalog,
inherits an old row's effort options, or treats a missing echoed effort as an empty menu.

### Todos

- Reviewer sev-4 observation 6: before the first exact-session readback, the trigger fallback is
  visually indistinguishable from an echo-verified effective value even though its accessible
  description names the source.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Trigger, exact-session menus, staging, serialized apply, error, and chip UI. | `ModelEffortControl` | dashboard/src/panels/session-cockpit/ModelEffortControl.tsx:635-704 |
| Sourcing, corrected menu, apply, and chip regression matrix. | "model + effort staged runs the SERIALIZED pair flow" | dashboard/src/panels/session-cockpit/ModelEffortControl.test.tsx:270-304 |
| Live-session client and actions. | `sendSet` | dashboard/src/data/setClient.ts:157-244 |
| Menu and effective-marker derivation. | `effectiveSelection` | dashboard/src/data/sessionCapabilities.ts:219-248 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Current L5I Maintenance

The trigger shows only a real running model/effort pair: freshest echoed evidence first, then the
launch-resolved value. Missing effort now removes its segment instead of emitting an unsupported
sentinel; the live menu remains the authority for choosing a value.

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T20:53:56+02:00 — W2-B04 curator: repaired 8 citation findings; scoped check passed.

- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-24T13:17:17Z — Curator: corrected missing-effort presentation to omission rather than a
  fabricated sentinel; verification fields remain pre-commit.

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R1–R3/R5/R6 through fix round 3 and
  final reviewer PASS. Sev-4 observation 6 remains recorded. Verification metadata is pinned to
  the contract base until code commit.
