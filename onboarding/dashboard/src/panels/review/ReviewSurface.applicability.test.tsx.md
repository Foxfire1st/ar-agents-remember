# dashboard/src/panels/review/ReviewSurface.applicability.test.tsx

## Governing Overview

[panels route overview](../overview.md)

## Purpose

The former mounted assessment/applicability fixture is removed from freeze07, not renamed into a current mounted control. Its last actual c861abfe BASE source retained a synthetic selected/sibling assessment case; its fetch response was an HTTP-shaped cast, not a native response/run witness. The earlier four-case label/count/history compatibility account was already historical. None is current regression coverage after this file deletion.

## Code Commentary

### Logic

Current ReviewRecordPanes renders raw record facts, lane/read-only state and judgment identifiers; the removed applicability/context/count/evidence-pane helpers are not present there. The surviving server-side sibling check exercises selected leaf judgment rows, not the old assessment applicability labels. These are distinct current boundaries, not substitute proof that the deleted mounted case still executes.

### Invariants And Boundaries

No current execution, retained case, equivalent replacement, CODE/MEMORY acceptance or proof promotion is inferred from this historical card. No realization/proof attachments are removed: the inspected sidecar has none.

### Todos

No implementation request is invented to restore the retired channel.

## Evidence

### Docs References

No configured Domain Documentation source was available; current boundaries below are repository source, not the old fixture or its header.

### Repo-Internal References

- Current details/facts rendering and judgment identifiers are a different owner than the retired assessment labels. [16]

- The controlled current sibling test filters leaf judgment rows and excludes the sibling row; it does not revive the removed applicability surface. [17]

### Cross-Repo References

The surviving cited owners are in this repository; no external-system boundary is claimed.

## Historical Account

Superseded text is retained below. Historical citation labels are inert, not current anchors.

<details>
<summary>Removed test account, preserved for history</summary>

> # dashboard/src/panels/review/ReviewSurface.applicability.test.tsx
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> The mounted-surface cases for `ICR-R26@v1`'s record labels: the **real** `ReviewSurface` over the
> **real** review client, with `fetch` stubbed and the catalogue hook explicitly mocked. Every request is built by the shipped client and
> every response travels the way the browser's does — status, body, the shared decode, the component tree
> — and no assertion reads a prop the test itself passed.
>
> One surviving direct-record isolation case mounts the selected invariant over a synthetic labelled payload with the real `ReviewSurface` and client, replacing fetch and the catalogue hook. It asserts exactly one central direct assessment with its own finding, disposition, rationale and stale binding, and no sibling finding anywhere. The earlier context/count/history/pre-label cases are retired under the recorded ruling, not restored.
>
> The surface's retained direct assessments: the selected subject's own assessment treatment renders in pane 3 without borrowing a sibling's judgment. One synthetic labelled fixture exercises this through the real surface and client with only fetch and the catalogue replaced; dataset context, count, history and pre-selection probes are retired, not rebuilt.
> ## Code Commentary
>
> ### Logic
>
> The comparison-focused cases isolate the shared catalogue hook so its additional request cannot consume a comparison fixture. The ordinary-entry catalogue/comparison interaction is covered separately by ReviewSurface.navigation.test.tsx. Assertions follow the compact labels, central display controls and changed-region default without weakening the existing record, paging or refusal contracts.
>
> `directLabel` names the selected invariant and retained revision. `payload()` builds its direct and sibling assessments and the selected revision; `reviewed` wraps that synthetic payload and `response` supplies an HTTP-shaped fetch reply. There is no current boolean labelled/unlabelled payload pair or historical-label fixture.
>
> **Historical pre-R86 card account — superseded, not current assertion evidence.**
>
> > **The four cases, one property each:**
> >
> > 1. `"mounts each record's own treatment and the true subject of labelled context"` (`:238-265`) — three
> >    assessment rows mount, the direct one prints `applicability: direct (invariant <SUBJECT>)`, the
> >    label also travels on the evidence pane's copy of the same record (so one selection cannot be
> >    displayed with two treatments in two panes), the context row states the sibling's **true subject**
> >    and the recorded relationship that reached it (`realization 0cca9e84 at src/batch.py`), and the
> >    sibling's finding text is **absent** from the document — the contamination this requirement prevents.
> > 2. `"states the six-way counts beside the collections it filtered"` (`:267-281`) — the
> >    `review-applicability` block prints `supplied assessments: 4` with `direct 1`, `historical 1`,
> >    `context 1` and `not displayed 1`, so the filtering is visible as arithmetic on the page.
> > 3. `"labels a previous generation's record as historical rather than as the current result"`
> >    (`:283-297`) — a `[data-applicability="historical"]` node exists, names the selected subject and
> >    carries the old candidate tree id it examined.
> > 4. `"still renders a payload published before the labels existed"` (`:299-310`) — the unlabelled body
> >    renders its two assessment rows and mounts **no** context block and **no** counts block, so a client
> >    released before this vocabulary still works against a server that sends it.
>
> ### Conventions
>
> Cleanup restores stubbed globals. The retained case queries `review-center-assessment`, `data-binding` and its direct applicability treatment in the central member view, then checks that the sibling finding is absent from the whole document.
>
> ### Invariants And Boundaries
>
> - The current case establishes direct-record isolation in the centre only; it does not establish the earlier two-pane treatment, six-way rendered partition, historical-label or pre-label compatibility subjects.
> - This is synthetic-payload jsdom evidence, not a fresh backend or browser qualification.
>
> ### Todos
>
> None recorded.
>
> The fixture labels one direct assessment for the selected invariant with a retained revision selection, plus a sibling assessment about another subject. Mounting the invariant subject shows exactly one centre assessment with its own finding, disposition, rationale and stale binding beside a direct applicability treatment, while the sibling finding appears nowhere. The catalogue mock isolates this to the comparison path.
> ## Evidence
>
> ### Docs References
>
> No domain documentation source is configured for this repository (`system/sources.md` carries no
> `Domain Documentation` entries). The statements below are grounded in repository source only.
>
> No configured domain documentation could be checked.
>
> ### Repo-Internal References
>
> **Historical pre-R86 card account — superseded, not current assertion evidence.**
>
> > - **The two label fixtures the cases mount, each naming its own subject and references.** (historical reference 1)
> > - **The two real wire bodies: one with the labels, context rows and counts, one without any of them.** (historical reference 2)
> > - **The envelope and the real `Response` the client decodes.** (historical reference 3)
> > - **The one mount helper, and the cleanup that keeps no global across a case.** (historical reference 4)
> > - **The F09 client case: the treatment and the true subject are mounted, and the sibling's finding is nowhere in the document.** (historical reference 5)
> > - **The counts case: the six-way partition is rendered beside the collections it filtered.** (historical reference 6)
> > - **The historical case: a previous generation is labelled and never reads as the current result.** (historical reference 7)
> > - **The additive-compatibility case: a body published before the labels existed still renders.** (historical reference 8)
> > - **The client vocabulary these cases mount, and the fields the surface gained.** (historical reference 9)
> > - **The rendered labels themselves: the per-record note, the context list and the counts block.** (historical reference 10)
> > - **The two call sites that mount them, on the knowledge pane and on the evidence pane.** (historical reference 11)
> > - **The server-side case this client mirrors: a sibling's record is context and never the selected subject's.** (historical reference 12)
>
> ### Cross-Repo References
>
> No cross-repository behavior is implemented in this module. It mounts the dashboard's own surface over
> its own origin.
>
> No meaningful cross-repo references found.
> - Direct and sibling labelled assessments of the fixture (historical reference 13)
> - Synthetic comparison payload with retained revision selection (historical reference 14)
> - Admitted review wrapper for served answers (historical reference 15)

</details>
