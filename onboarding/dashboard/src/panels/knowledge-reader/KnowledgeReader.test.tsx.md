# dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx

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

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement: real served answers, SCRATCH-AUTHORED curation, only `fetch` stubbed. [1]
- The captured bodies and the request-to-body map. [2]
- The file, directory, root-summary and test-file cases. [3]
- The invariant, family, decision and incident, and census cases. [4]
- Navigation, and failures named. [5]
- The review-fix cases: code spans, located lines and a failed source, the derived header, side failures and stale answers, unreadable links. [6]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
