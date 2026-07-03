# dashboard/src/panels/file-viewer/FileViewer.test.tsx

| Field | Value |
| ---------------------- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/file-viewer/FileViewer.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-06-29T09:06+02:00 |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a` |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test. | L151-L252 | [FileViewer.tsx](FileViewer.tsx) |
| `CockpitShell` registers the "File Viewer" mode and keeps it mounted via `display`. | L36, L171-L172, L239-L246 | [../../cockpit/Cockpit.tsx](../../cockpit/Cockpit.tsx) |
| The empty-state backdrop prompt copy ("Select a code file") asserted here. | L99-L112 | [DualPane.tsx](DualPane.tsx) |
| `applySnapshot` loads the projection under test. | L129-L144 | [../../data/store.ts](../../data/store.ts) |
| The `engine-fleet` GALLERY fixture. | L152 | [../../dev/fixtures.ts](../../dev/fixtures.ts) |

## Update History

- 2026-06-30T00:00:00+02:00 — operations-integration L5: the pre-selection assertion now checks `container.textContent` contains "Select a code file" (the siege-tank empty-state backdrop fills the pane, so there are no per-side `pane-placeholder` nodes to query) instead of scanning `pane-placeholder` elements.
- 2026-06-29T09:06+02:00 — Created for operations-integration L2 (File Viewer): the vitest/RTL test
  covering File Viewer mode-bar registration (full-bleed), the pre-selection placeholder, and the
  keep-mounted-on-switch state preservation. Verification metadata pinned to the task base until
  closeout stamps the L2 code commit.
