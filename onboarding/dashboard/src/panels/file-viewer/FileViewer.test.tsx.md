# dashboard/src/panels/file-viewer/FileViewer.test.tsx

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

## Evidence

### Repo-Internal References

- The component under test. [1]
- `CockpitShell` registers the "File Viewer" mode and keeps it mounted via `display`. [2]
- The empty-state backdrop prompt copy ("Select a code file") asserted here. [3]
- `applySnapshot` loads the projection under test. [4]
- The `engine-fleet` GALLERY fixture. [5]

## Current L5I Maintenance

The focused viewer suite now proves that a hidden mounted viewer makes no files API request, first
selection makes exactly one catalog read, and later hide/show cycles retain the settled catalog.
