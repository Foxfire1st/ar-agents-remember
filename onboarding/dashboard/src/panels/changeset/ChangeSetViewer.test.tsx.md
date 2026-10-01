# dashboard/src/panels/changeset/ChangeSetViewer.test.tsx

## Governing Overview

[changeset/ overview](overview.md)

## Purpose

Vitest/jsdom test for the Change-Set Viewer screen + its Cockpit/DetailPanel wiring. It stubs the global
`fetch` with a URL-aware change-set fixture (CodeMirror is kept out of jsdom — the live `MergeView` render
is covered by build + typecheck, matching the L2 `FileViewer.test.tsx` approach), and asserts the screen,
master-mode row inspection, the DetailPanel button → target, and the Cockpit takeover's initial state.

## Code Commentary

### Logic

The viewer tests cover loading-before-data, explicit request errors, the
master request's per-leaf breakdown, and a fake-timer working refresh that
proves no next cycle begins while the prior list/file requests remain pending.

**260921-ICR-L33 turned the master assertion around and added four cases.** The master list request now
carries `includeLeaves: true` (R33.2), so the pre-existing assertion that pinned `includeLeaves=false`
was corrected rather than deleted — it still pins the request shape, on the side the product now takes.
The new cases measure what the answer is used FOR: `lists the master net's leaves, each with its own
code and memory counters (R33.2)` (`:363-387`) reads each row's `changeset-leaf-counters`;
`opens a landed leaf's committed change-set — and a working leaf's working delta — from the net
(R33.3)` (`:388-420`) drives both row kinds and asserts the targets the click produced;
`names the refusal when a landed leaf's committed range cannot be shown (R33.3)` (`:421-453`) stubs the
route's real 404 body and asserts the token the route's own code maps to (`not-found`), the status line
and the reason verbatim; and `names a measured-empty change-set instead of leaving the pane to the
pick-a-file backdrop (R33.3)` (`:454-473`) asserts the named measurement. Nine of the leaf's ten new
cases across the three suites fail against the base production bytes; the tenth is a boundary guard.

`stubChangeset()` installs a `vi.fn` `fetch` that returns `MASTER_CHANGESET` for `/api/changeset/master`,
`TASK_CHANGESET` for `/api/changeset/task`, and `{}` otherwise. Cases:

- **task scope** — renders `<ChangeSetViewer repo scope onBack/>`, awaits `changeset-counters`, and
  asserts the changed code + onboarding rows render, the counters contain `+3`, and the no-file empty
  state prompts "Select a changed file" — now asserted via `container.textContent` (the prompt comes
  from the siege-tank `EmptyStateBackdrop`, not a bare `pane-placeholder`). cit:(["renders the changed-file rows + counters for a task scope"], dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:107-120)
- **back link** — clicking `changeset-back` calls `onBack` once. cit:(["calls onBack when the back link is clicked"], dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:122-130)
- **master mode** — `<ChangeSetViewer repo master onBack/>` now renders **clickable** rows; before a
  pick it shows the same empty-state prompt (asserted via `container.textContent`), and clicking a row
  opens a diff (`ChangeSetPane` is mocked so CodeMirror stays out of jsdom). cit:(["opens a per-file NET diff from a clickable row in master mode"], dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:262-278)
- **leaf mode** (L4a) — `<ChangeSetViewer repo master leaf mode="committed"/>` loads via the `task` route
  (the stub returns `TASK_CHANGESET`), labels the header `committed · <leaf>`, and is per-file inspectable
  (a row click opens the diff pane); a `mode="working"` case asserts the `working · <leaf> · uncommitted`
  label.
- **working auto-poll** (L4a) — with `vi.useFakeTimers`, a `mode="working"` viewer (after opening a file)
  re-fetches BOTH `/api/changeset/task` (the list) and `/api/changeset/file-diff` (the open diff) after the
  interval advances (≥2 calls each = load/open + a poll), while a `mode="committed"` viewer stays at exactly
  1 each (the interval is gated off).
- **DetailPanel entry** — over the `full` gallery projection, a lifecycle selection renders an
  `open-changeset` button whose click calls `onOpenChangeSet` with the series target `{ repo, master }`
  (the fixture has no `activeWorktreeGroups`, so only the series button shows). cit:(["renders a series change-set button for an enclosure-backed lifecycle and opens the target"], dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:476-487)
- **Cockpit takeover** — `<CockpitShell/>` shows no `changeset-viewer` initially and keeps the
  `rail--left` + `data-fullbleed="false"`. cit:(["does not show the takeover initially and keeps the Operations rails"], dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:491-498)
- **Generation binding** — the master list publishes its exact endpoints; the viewer shows the
  bound generation caption and carries its pins into each file expansion, so an opened entry
  stays bound after the branch advances. cit:(["binds master file expansions to the generation the net listing published"], dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:280-313)

### Invariants And Boundaries

Pure unit test: `fetch` is stubbed, globals are unstubbed after each case. It pins the screen's row /
counters / empty-state (the "Select a changed file" prompt, now matched on `container.textContent`
since the siege-tank `EmptyStateBackdrop` provides it) behaviour, the DetailPanel → target contract, and
the Cockpit takeover's not-shown-initially state — not the live CodeMirror diff (kept out of jsdom by
design).

## Evidence

### Repo-Internal References

- URL-aware `fetch` stub for the change-set endpoints. [1]
- Screen rows + counters + empty-state prompt (matched on `container.textContent`); master-mode clickable row opens a diff; the master request asks for its per-leaf breakdown and the four R33 cases measure what the answer is used for. [2]
- DetailPanel button calls `onOpenChangeSet` with the series target. [3]
- Cockpit shows no takeover initially and keeps the rails. [4]
- Generation caption shown and pins carried into expansions. [5]
- Subject under test: the screen. [6]
