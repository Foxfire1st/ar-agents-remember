# dashboard/src/panels/detail-panel/changeSetBar.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/changeSetBar.tsx`        |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-09-18T18:10+02:00 |
| lastVerifiedCommitHash | `c5a74a85af20a8fb48cc44f59de7e926d589d3fc`                  |
| lastVerifiedCommitDate | 2026-09-18T18:30:35+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l22` uncommitted source; base `2dcacb27446ecbaba01b69ee32e2ac40a1713b09` |
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The change-set bar of the DetailPanel task-document reader, extracted from
`DetailPanel.tsx` by the 260731-EFA-L8 split. `ChangeSetButton` is the per-document
button, `DocChangeSetBar` the compact bar rendered above the reader content.

## Code Commentary

### Logic

The bar renders the change-set summary for the displayed document and exposes the
change-set viewer toggle; selection state stays in the panel's `useDetailPanelState`.

### Conventions

Small presentational components; no data-store imports.

**260915-KS-L22** adds a third entry beside the two existing ones rather than in their place.
`DocChangeSetBar` takes `selectorKind` (defaulting to `"invariant"`) and `selectorId`, and renders a
`ChangeSetButton` labelled **Intent review** when — and only when — both the enclosure liveness the
working action already requires and a `selectorId` are present. Its target is
`{ repo, master, leaf, review: { selectorKind, selectorId } }`: the reviewed subject's recorded
identity comes from the caller, never from the browser, because the browser does not choose the
candidate. The bar still fetches nothing itself; the button's counter effect reads only the leaf or
master request, so a review entry reports no counters.

### Invariants And Boundaries

The bar renders only the document currently displayed; it never fetches a change set
itself.

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
| The change-set bar entry points. | `ChangeSetButton`; `DocChangeSetBar` | dashboard/src/panels/detail-panel/changeSetBar.tsx:20-118 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  change-set bar extracted from `DetailPanel.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
2026-09-18T18:10+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **added the reviewer entry beside the change-set actions.** `DocChangeSetBar` gained
`selectorKind = "invariant"` / `selectorId` props and a third `ChangeSetButton` labelled *Intent
review*, rendered only when the enclosure is live and a `selectorId` is supplied — the same liveness
the working action is gated on, and never in the working or committed action's place. Its target
carries `review: { selectorKind, selectorId }`, the reviewed subject's recorded identity rather than
a filesystem path, because the browser does not choose the candidate. The new paragraph above states
that, and states the boundary the bar keeps: it still fetches nothing itself, and the new entry's
counter effect reads only the leaf or master request, so no counters are reported for a review. No
reference row was touched; ranges into this source belong to the citation-reprojection engine. The
metadata block above names this leaf's uncommitted candidate as what was read, and the two
verification stamps are left exactly as the last real verification set them. The body was changed
substantively and this entry is the history record, not a metadata-only refresh.
