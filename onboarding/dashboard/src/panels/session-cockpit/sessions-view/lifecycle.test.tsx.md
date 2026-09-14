# dashboard/src/panels/session-cockpit/sessions-view/lifecycle.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/sessions-view/lifecycle.test.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d`                  |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

The lifecycle/session suite split from `SessionsView.test.tsx` by the
260731-EFA-L8 test split. Pins the S5 legacy-duty parity, smart-default focus +
handoff + session cycling (L2 R9/F17), authoritative landed cleanup through rail
and palette callers (F5-S5-2), and the planned-retirement window rule (a retired seat
closes its own rail window while a bare `terminated` row and a landed session keep theirs).

## Code Commentary

### Logic

Seeds legacy/ready sessions via `test-utils.tsx` and asserts duty parity, focus
handoff, cycling, the cleanup callers' authority, and — in the fourth suite — that
retirement provenance (`retiredAt`/`retiredBySession`/`retiredReason`/`retiredEdge`)
closes a rail window that a bare `terminated` mark leaves open.

### Invariants And Boundaries

Assertions preserved from the monolithic suite.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The lifecycle file contains the legacy-duty, smart-default/handoff, authoritative landed-cleanup, and planned-retirement-window suites. | "describe(\"S5 legacy duty parity\", () => {"; "describe(\"smart-default focus + handoff + session cycling (L2: R9, F17)\", () => {"; "describe(\"authoritative landed cleanup through rail and palette callers (F5-S5-2)\", () => {"; "describe(\"planned retirement closes its own window (unplanned termination keeps it)\", () => {" | dashboard/src/panels/session-cockpit/sessions-view/lifecycle.test.tsx:64-423; dashboard/src/panels/session-cockpit/sessions-view/lifecycle.test.tsx:425-508 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the suite-coverage row's
  first range stopped inside the third suite. Corrected the three earlier suites to `:64-423`, with
  the planned-retirement suite at `:425-508`. Noting that this staleness is pre-existing.
  Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `dashboard/src/panels/session-cockpit/sessions-view/lifecycle.test.tsx` changed since the recorded
  verification commit. Re-read the card against the frozen on-disk source and re-checked its claims
  and cited ranges: nothing this card asserts is falsified by the change, so no wording changed.
  Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source gained a
  fourth suite, "planned retirement closes its own window (unplanned termination keeps it)" at
  `:425-508`, since the recorded verification commit. Added its anchor to the coverage row with its
  range and stated the retirement-provenance rule in Purpose and Logic. Note the drift predates this
  task line: the change landed with an earlier route change, not with this master. Verification
  metadata remains closeout-owned.
- 2026-08-11T15:20+02:00 — Replaced the ambiguous `describe` anchor with the three exact suite
  declarations and stated the file-level coverage they evidence.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  lifecycle suite split from `SessionsView.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
