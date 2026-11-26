# skills/l-01-agent-lifecycles/reference/curator/card-formats-and-citations.md

## Governing Overview

[overview](../../overview.md)

## Purpose

The Curator's detail for card, overview and entity-catalog layouts, card history dispositions and citation checks. The role and the curation operation keep scope, writer and handover authority.

## Code Commentary

The Curator role links this detail file from its Reference index under Cards/style; the file-card, repository-overview and route-overview templates link the scope section, and the onboarding-coherency template links the current-content section.

History: the subject's earlier rows are read before ingest. For invariants, `changed` changes the record's meaning and increments its revision, `moved` re-anchors without changing meaning, `deleted` removes entries or retires the invariant, `extended` adds an entry without changing meaning, and `no_impact` preserves meaning and the entry set, including admission, origin or slug-only changes. Family and onboarding rows keep their own schemas; a family row's `examined` list binds member revisions, and a member revision change after the row makes the row stale.

Layout: a file card explains one source file on its own, using the file-card template; overviews explain a cohesive area (not merely a directory) using the repository- or route-overview template. Overviews are purpose-first, explain construction and boundaries, put all citation lines last, and take a change in the section that owns its meaning. Cards and overviews carry no metadata stamps, card-local change history or completed citation tables; a numbered marker needs its sidecar reference, the fixer authors references, and the writer authors `realizes` and `proves`. An onboarding trace row is `updated` with a counted card change or `no_impact` with a reason.

Citations: evidence is authored as a Finding/Anchor/Source table for `citation_fix`, with `path:start-end` line ranges, a bare path for a whole file, or a `://` URL for evidence outside the paired code tree. Each changed claim, count and prose line reference is checked against code, a prose line reference lies inside its citation anchor, and passing structural checks and authentic anchors do not prove prose true. Changed cards are previewed and repaired in one `citation_fix` call with one `documents` list, not one call per card; the batch keeps successful cards and leaves refused ones, so a partial result is not a completed batch. Semantic or ambiguous items stay Curator decisions, and no unimplemented citation feature is claimed. Reference refresh, note revision, withdrawal and source-rename steps keep surviving numbers and move entries through the writer before the card.

A Lean citation can use the written declaration name or its full name. A full name distinguishes multiple verified matches. If the scope leaves both keys unverifiable, leave the Anchor cell empty and cite `path:start-end` in Source. Plain identifiers search ranged sources in row order. Extended Lean names can search bare Lean paths, which also keep their whole-file target.

Entity catalog: one selective `entities.md` with exact inventory and fingerprint headings, one fingerprint row per entity, and `git-blob-set-v1` SHA-256 fingerprints over sorted evidence paths; a changed fingerprint calls for review, not an automatic prose change.

## Evidence

- History dispositions for invariants, and family rows' own schema and `examined` binding. [1]
- Card and overview scope, templates and overview section order with citation lines last. [2]
- Cards keep current prose and numbered evidence only; the fixer and the writer own sidecar fields; trace rows are `updated` or `no_impact`. [3]

- Citation input format, external URLs and the rule that structural checks do not prove prose true. Lean citations use exact names, with ranged sources for plain identifiers and explicit line ranges for unverifiable scope. [4]

- One named `citation_fix` batch per wave, with partial results and refusals kept visible. [5]
- Refreshing, revising, withdrawing and renaming references. [6]
- Entity catalog scope, headings and fingerprint algorithm. [7]
- The Curator role links this detail file from its Reference index. [8]
