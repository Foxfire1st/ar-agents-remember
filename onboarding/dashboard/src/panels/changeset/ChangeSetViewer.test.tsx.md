# dashboard/src/panels/changeset/ChangeSetViewer.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/changeset/ChangeSetViewer.test.tsx`   |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-09-22T11:00:00+02:00                                      |
| lastVerifiedCommitHash | `2e11db883f77bb1bf2827ae537b5d1d564e020b3`                  |
| lastVerifiedCommitDate | 2026-09-24T22:33:57+02:00|
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
  (the fixture has no `activeWorktreeGroups`, so only the series button shows). cit:(["renders a series change-set button for an enclosure-backed lifecycle and opens the target"], dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:316-327)
- **Cockpit takeover** — `<CockpitShell/>` shows no `changeset-viewer` initially and keeps the
  `rail--left` + `data-fullbleed="false"`. cit:(["does not show the takeover initially and keeps the Operations rails"], dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:331-338)
- **Generation binding** — the master list publishes its exact endpoints; the viewer shows the
  bound generation caption and carries its pins into each file expansion, so an opened entry
  stays bound after the branch advances. cit:(["binds master file expansions to the generation the net listing published"], dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:280-313)

### Invariants And Boundaries

Pure unit test: `fetch` is stubbed, globals are unstubbed after each case. It pins the screen's row /
counters / empty-state (the "Select a changed file" prompt, now matched on `container.textContent`
since the siege-tank `EmptyStateBackdrop` provides it) behaviour, the DetailPanel → target contract, and
the Cockpit takeover's not-shown-initially state — not the live CodeMirror diff (kept out of jsdom by
design).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| URL-aware `fetch` stub for the change-set endpoints. | `fetch` | dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:24-42 |
| Screen rows + counters + empty-state prompt (matched on `container.textContent`); master-mode clickable row opens a diff; the master request asks for its per-leaf breakdown and the four R33 cases measure what the answer is used for. | "renders the changed-file rows + counters for a task scope"; "opens a per-file NET diff from a clickable row in master mode"; "lists the master net's leaves, each with its own code and memory counters (R33.2)"; "names a measured-empty change-set instead of leaving the pane to the pick-a-file backdrop (R33.3)" | dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:107-120; dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:262-280; dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:363-387; dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:454-473 |
| DetailPanel button calls `onOpenChangeSet` with the series target. | `onOpenChangeSet` | dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:479-479 |
| Cockpit shows no takeover initially and keeps the rails. | "does not show the takeover initially and keeps the Operations rails" | dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:491-498 |
| Generation caption shown and pins carried into expansions. | "binds master file expansions to the generation the net listing published" | dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:280-313 |
| Subject under test: the screen. | `ChangeSetViewer` | dashboard/src/panels/changeset/ChangeSetViewer.tsx:645-725 |

## Update History
- 2026-09-24T23:30:00+02:00 — 260921-ICR-L33 curator (candidate `ar/260921-icr-l33-ar`, uncommitted; code base `86639933d61528387ce106dbd4d7a334bd468671` plus the working-tree delta; adversarial round 2 `verify-l33.md` = `pass`): **body update — one assertion turned around and four cases added (339 → 476 lines).** The false sentence ("the master `includeLeaves=false` request") was corrected in place: the request now carries `includeLeaves: true` and the pre-existing assertion was flipped rather than dropped, so the shape is still pinned on the side the product takes. The four R33 cases are recorded above with their line ranges, and the row into this file was re-derived against the candidate. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-22T11:00:00+02:00 — 260921-ICR-L13 curator (candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **one new generation case (305 → 339 lines).** The Logic and table record `binds master file expansions to the generation the net listing published` (`:280-313`); the two cases below the insertion moved with it and their rows are re-derived (`:282-293` → `:316-327`, `:297-304` → `:331-338`, `onOpenChangeSet` `:285` → `:319`), as is the subject row (`ChangeSetViewer` `:416-478` → `:476-541`). The rows above the insertion stand. Verification metadata is **not** advanced: the candidate is uncommitted and closeout owns the stamp.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 11 citation finding(s); scoped recheck clean.

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
