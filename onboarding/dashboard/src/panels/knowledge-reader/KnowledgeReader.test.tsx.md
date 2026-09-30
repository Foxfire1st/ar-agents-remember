# dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:41:49+02:00 |
| lastVerifiedCommitHash | `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`|
| lastVerifiedCommitDate | 2026-09-30T12:51:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**MIK-R29 on real data: the Knowledge reader's views over the real served answers of `/api/knowledge/reader`
for a converted scratch copy of the real repositories.** 14 component tests. `KnowledgeReader` is the real
component; only `fetch` is stubbed, and it answers from `knowledgeReader.captured.json` (the bodies' provenance is
its `_provenance` key). The memory was converted by L24's `knowledge-convert`; the decisions, incident, family
routes, history rows, proof and census on top of it are SCRATCH-AUTHORED, because converted memory holds none yet.

## Code Commentary

### Logic

- **The stub.** `bodyFor` maps each request (view plus path or ID) to a captured body; `overrides` replace a body
  for one case (a failed source, a trimmed page, a `next` subtree page); `heldTree` holds tree listings of one
  commit until the case releases them.
- **The cases:**
  1. a file (`integrate.py`): six `[n]` markers, reference 2 lists 3 targets, entries with states, the family via
     its route with locations elsewhere, the decision in full, the linked records;
  2. a directory (the packet's conforming example, `worktrees/`): the overview, `FAM-QWVGDSYX` via its route,
     `DEC-R29AAA` superseded and `DEC-R29DEC` active, the bounded children, and "list all" into the subtree (F2);
  3. the root summary as the landing, and "more" following the continuation, where a double click sends one
     request (F2, the R2 note);
  4. a test file: proofs by invariant with their facet;
  5. an invariant: states, links, and a timeline from all three sources, newest first, with a meaning diff and a
     moved entry event;
  6. a family, a decision (alternatives in order, `reconsider_when`) and an incident (cause,
     `cause_uncertainty`, recovery, corrective actions, typed links);
  7. the census, the without-proof list and code opened at its symbol;
  8. navigation by URL: explorer counts, links change the hash, the hash round-trips;
  9. a partial index, unavailable prose, unverifiable states and an unconverted tree, each named;
  10. `[n]` markers linked in text only, never in code spans or fences (F4);
  11. the located code lines (193 to 213) and a timeline source that could not be read (F6);
  12. a superseded decision headed with its derived status (F9);
  13. side reads that failed named, a clean published view pinned, and stale explorer answers dropped (F11, N2,
      F13);
  14. record links that could not be read named instead of "no outgoing link" (F17).

### Conventions

- Real captured bodies, not hand-written ones, except where a case overrides one field and says so.

### Invariants And Boundaries

- The captured bodies must stay the served bodies of the backend: the reviewer diffed the fixture's key sets
  against the backend's output for all captured views and found them identical.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement: real served answers, SCRATCH-AUTHORED curation, only `fetch` stubbed. | "MIK-R29 on real data" | dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx:1-6 |
| The captured bodies and the request-to-body map. | `captured`; `bodyFor` | dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx:16-21; dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx:33-65 |
| The file, directory, root-summary and test-file cases. | "opens a file with its prose, resolved references, entries, families and linked records"; "opens a directory with its overview, routed families elsewhere and the route decisions"; "lands on the bounded root summary and follows a subtree page to the next"; "shows a test file its proofs by invariant with their facets" | dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx:118-233 |
| The invariant, family, decision and incident, and census cases. | "opens an invariant truth view with its states, links and a three-source timeline"; "opens a family, a decision and an incident with every field and their links"; "shows the census, the without-proof list and code opened at its symbol" | dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx:235-338 |
| Navigation, and failures named. | "navigates by URL: explorer and links change the shareable hash, and the hash round-trips"; "names a partial index, unavailable prose, unverifiable states and an unconverted tree" | dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx:340-398 |
| The review-fix cases: code spans, located lines and a failed source, the derived header, side failures and stale answers, unreadable links. | "links [n] markers in prose text only, never inside code spans or fences"; "marks the located code lines, and names a timeline source that could not be read"; "heads a superseded decision with its derived status"; "names side reads that failed, pins a clean published view, and drops stale explorer answers"; "names record links that could not be read instead of claiming there are none" | dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx:400-503 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T12:41:49+02:00 — 260928-MIK-L29 curator (follow-up after the coordinator's test-only edit, staged; the change set is still 24 files over `b54d1b0331f67454bcf245a7a338b04900181c3c`): **Todo resolved.** The debugging `console.log('HELD', …)` block of case 13 (old lines 488-492) was removed and nothing else changed; the file's 14 cases pass and eslint and prettier are clean (coordinator). The Todo is replaced by "No additional work", the row that cited the removed block is dropped, and the review-fix cases row was re-measured by the exact −5 shift (`400-508` → `400-503`). No verification stamp was advanced: the file is new and uncommitted; closeout owns the real stamp.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:06:02+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`; review R3 and post-sync pass-with-notes, with R3-1 and R3-2 fixed): created this card for the new component tests MIK-R29 adds (14 cases over real served bodies, the dashboard half written by worker B), recording the fix-round cases (F2, F4, F6, F9, F11, F13, N2, the R2 in-flight note, F17) and a Todo for the leftover `console.log` in case 13. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
