# dashboard/src/panels/session-cockpit/sessionRailParts.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/sessionRailParts.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated | 2026-08-11T23:40+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`                  |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Contains the row, master block, attention, and rail-body renderers for the structural Chats tree.

## Code Commentary

### Logic

`RailMasterBlock` renders master and leaf containment, while `RailBody` walks sprint sections and
their current occupants. `RailRow` treats the occupant id as an action/focus target but renders task
and role identity supplied by the model.

### Conventions

Structure is passed in; this module does not infer parentage from spawn ids or labels.

### Invariants And Boundaries

- One structural row remains stable when its occupant changes.
- Row actions target the currently rendered occupant only.
- Empty and attention states do not manufacture a fallback seat.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Individual rows separate structural label from occupant actions. | `RailRow` | dashboard/src/panels/session-cockpit/sessionRailParts.tsx:330-429 |
| Master blocks render the supplied task containment. | `RailMasterBlock` | dashboard/src/panels/session-cockpit/sessionRailParts.tsx:567-606 |
| The rail body renders sprint/master/leaf sections. | `RailBody` | dashboard/src/panels/session-cockpit/sessionRailParts.tsx:751-961 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T23:40+02:00 — No content impact: `RailTop` now delegates its summary and completed-bulk
  controls to focused helpers; the supplied sprint/master/leaf structure, completed-seat actions,
  and current-occupant row contract are unchanged. Verification metadata remains pinned until
  governed closeout.

- 2026-08-11T19:58+02:00 — Aligned the current dashboard card for `sessionRailParts.tsx` with its task-document, seat-state, and lifecycle interaction boundaries.
- 2026-08-10T04:39+02:00 — 260713-TES-L6: recorded the sprint-group and legacy-section presentation
  contract. Verification metadata remains pinned until closeout stamps the code commit.

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the rail
  parts module extracted from `SessionRail.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
