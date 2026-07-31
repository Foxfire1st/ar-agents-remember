# dashboard/src/panels/changeset/ChangeSetViewer.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/changeset/ChangeSetViewer.test.tsx`   |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-07-12T12:55+02:00                                      |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77`                  |
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|
| governingOverview      | `overview.md`                                               |

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
master `includeLeaves=false` request, and a fake-timer working refresh that
proves no next cycle begins while the prior list/file requests remain pending.

`stubChangeset()` installs a `vi.fn` `fetch` that returns `MASTER_CHANGESET` for `/api/changeset/master`,
`TASK_CHANGESET` for `/api/changeset/task`, and `{}` otherwise. Cases:

- **task scope** — renders `<ChangeSetViewer repo scope onBack/>`, awaits `changeset-counters`, and
  asserts the changed code + onboarding rows render, the counters contain `+3`, and the no-file empty
  state prompts "Select a changed file" — now asserted via `container.textContent` (the prompt comes
  from the siege-tank `EmptyStateBackdrop`, not a bare `pane-placeholder`). (L44-L60)
- **back link** — clicking `changeset-back` calls `onBack` once. (L122-L130)
- **master mode** — `<ChangeSetViewer repo master onBack/>` now renders **clickable** rows; before a
  pick it shows the same empty-state prompt (asserted via `container.textContent`), and clicking a row
  opens a diff (`ChangeSetPane` is mocked so CodeMirror stays out of jsdom). (L262-L278)
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
  (the fixture has no `activeWorktreeGroups`, so only the series button shows). (L282-L293)
- **Cockpit takeover** — `<CockpitShell/>` shows no `changeset-viewer` initially and keeps the
  `rail--left` + `data-fullbleed="false"`. (L99-L108)

### Invariants And Boundaries

Pure unit test: `fetch` is stubbed, globals are unstubbed after each case. It pins the screen's row /
counters / empty-state (the "Select a changed file" prompt, now matched on `container.textContent`
since the siege-tank `EmptyStateBackdrop` provides it) behaviour, the DetailPanel → target contract, and
the Cockpit takeover's not-shown-initially state — not the live CodeMirror diff (kept out of jsdom by
design).

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| URL-aware `fetch` stub for the change-set endpoints. | L24-L42 | [ChangeSetViewer.test.tsx](ChangeSetViewer.test.tsx) |
| Screen rows + counters + empty-state prompt (matched on `container.textContent`); master-mode clickable row opens a diff. | L44-L81 | [ChangeSetViewer.test.tsx](ChangeSetViewer.test.tsx) |
| DetailPanel button calls `onOpenChangeSet` with the series target. | L84-L97 | [ChangeSetViewer.test.tsx](ChangeSetViewer.test.tsx) |
| Cockpit shows no takeover initially and keeps the rails. | L99-L108 | [ChangeSetViewer.test.tsx](ChangeSetViewer.test.tsx) |
| Subject under test: the screen. | L144-L293 | [ChangeSetViewer.tsx](ChangeSetViewer.tsx) |

## Update History

- 2026-07-31T17:48+02:00 — 260731-EFA-L2 curator: re-derived 3 stale self-citations after the
  loading/error and non-overlapping-refresh cases were inserted ahead of them. The back-link case
  moved L62-L70 → L122-L130, the master-mode clickable-row case L72-L81 → L262-L278, and the
  DetailPanel entry case L84-L97 → L282-L293. No described behaviour changed.

- 2026-07-12T12:55+02:00 — 260712-TRH-L2: added loading/error, master query-shape, and non-overlapping working-refresh regressions while retaining task, master, leaf, and DetailPanel entry coverage. Verification metadata pinned until closeout stamps the L2 code commit.

- 2026-06-30T00:00:00+02:00 — L5 (diff-viewer polish): the empty-state assertions in the **task-scope** and
  **master-mode** cases now match `container.textContent` for "Select a changed file" instead of
  querying the `pane-placeholder` testid — the prompt is now provided by the siege-tank
  `EmptyStateBackdrop` rather than a bare placeholder. Verification metadata pinned until closeout
  stamps the L5 commit.
- 2026-06-29T23:00+02:00 — L4a: added **leaf-mode** cases — a committed leaf loads via the `task` route,
  labels the header `committed · <leaf>`, and is per-file inspectable; a working leaf shows the
  `working · <leaf> · uncommitted` label — plus a **working auto-poll** case (fake timers: working
  re-fetches both the list and the open diff after the interval, committed does neither). Verification
  metadata pinned until closeout stamps the L4a commit.
- 2026-06-29T17:00+02:00 — L4 follow-up: the **master-mode** case now renders clickable rows and asserts a
  click opens a diff (`ChangeSetPane` mocked), replacing the old accumulated-placeholder assertion.
  Verification metadata pinned until closeout stamps the L4 follow-up commit.
- 2026-06-29T16:40+02:00 — Created for operations-integration L4 (Change-Set Viewer): vitest/jsdom test
  stubbing the change-set `fetch` and pinning the screen rows/counters/placeholders, the master
  accumulated placeholder, the DetailPanel button → target, and the Cockpit takeover initial state
  (CodeMirror kept out of jsdom). Verification metadata pinned to the task base until closeout stamps the
  L4 code commit.
