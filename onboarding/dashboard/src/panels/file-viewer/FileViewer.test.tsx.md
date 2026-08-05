# dashboard/src/panels/file-viewer/FileViewer.test.tsx

| Field | Value |
| ---------------------- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/file-viewer/FileViewer.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

The vitest + Testing-Library test for the File Viewer center tab. It pins three behaviors: mode-bar
tab registration (full-bleed), the empty-state backdrop prompt before any file is selected, and the
keep-mounted-on-switch behavior that lets the viewer's state survive a view change.

## Code Commentary

### Logic

`beforeEach` stubs global `fetch` (the viewer fetches the repo catalog on mount) so jsdom never hits
the network; `afterEach` runs `cleanup` and unstubs. Test 1 applies the `engine-fleet` GALLERY
snapshot, renders `CockpitShell`, clicks the "File Viewer" radio, then asserts the `file-viewer` testid
is present, the shell body carries `data-fullbleed="true"`, and `.rail--left` is gone (full-bleed, like
Engine Room / Topology). Test 2 renders `FileViewer` directly and asserts the empty-state backdrop
prompt — it checks `container.textContent` contains "Select a code file" (the siege-tank backdrop fills
the pane; there are no per-side placeholders to query). Test 3 (keep-mounted) checks the viewer node exists
from the default Operations view but its parent is `display:none`; switching to File Viewer reveals the
SAME node (`display:flex`, never remounted); leaving hides it again (still the same node) — proving
state is preserved.

### Invariants And Boundaries

The test must stay hermetic — `fetch` is always stubbed, so no real `/api/files/*` calls fire. The
keep-mounted assertions encode the Cockpit contract: the File Viewer is toggled via CSS `display`,
never unmounted, so the DOM node's identity must persist across switches. Assertions key off stable
hooks (`data-testid` `file-viewer`, the "File Viewer" radio role, the `data-fullbleed` attribute) plus the
empty-state prompt copy ("Select a code file") matched against `container.textContent`, so renaming those
is a breaking change.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The component under test. | `FileViewer` | dashboard/src/panels/file-viewer/FileViewer.tsx:278-278 |
| `CockpitShell` registers the "File Viewer" mode and keeps it mounted via `display`. | `CockpitShell`; "File Viewer" | dashboard/src/cockpit/Cockpit.tsx:74-74; dashboard/src/cockpit/Cockpit.tsx:385-666 |
| The empty-state backdrop prompt copy ("Select a code file") asserted here. | "Select a code file" | dashboard/src/panels/file-viewer/DualPane.tsx:99-112 |
| `applySnapshot` loads the projection under test. | `applySnapshot` | dashboard/src/data/store.ts:43-43 |
| The `engine-fleet` GALLERY fixture. | `GALLERY`; "engine-fleet" | dashboard/src/dev/fixtures.ts:146-490; dashboard/src/dev/fixtures.ts:484-490; dashboard/src/panels/engine-room/fixtures.ts:724-724 |

## Current L5I Maintenance

The focused viewer suite now proves that a hidden mounted viewer makes no files API request, first
selection makes exactly one catalog read, and later hide/show cycles retain the settled catalog.

## Update History

- 2026-08-04T18:00+02:00 — 260731-EFA-L6 S18-B14 curator: repaired 3 citation rows with exact anchors (`FileViewer`/`CockpitShell`/"File Viewer"/`GALLERY`/"engine-fleet") and ledger-verified ranges, added the applySnapshot implementation range beside its interface signature, and bound the engine-fleet entry to its GALLERY spread-map and scenario definition. Scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-07-24T13:17:17Z — Curator: recorded first-visible catalog-read regressions; verification
  fields remain pre-commit.

- 2026-06-30T00:00:00+02:00 — operations-integration L5: the pre-selection assertion now checks `container.textContent` contains "Select a code file" (the siege-tank empty-state backdrop fills the pane, so there are no per-side `pane-placeholder` nodes to query) instead of scanning `pane-placeholder` elements.
- 2026-06-29T09:06+02:00 — Created for operations-integration L2 (File Viewer): the vitest/RTL test
  covering File Viewer mode-bar registration (full-bleed), the pre-selection placeholder, and the
  keep-mounted-on-switch state preservation. Verification metadata pinned to the task base until
  closeout stamps the L2 code commit.
