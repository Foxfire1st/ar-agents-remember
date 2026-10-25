# mcp/src/agents_remember/application/review_curator_records.py

## Governing Overview

[application route overview](overview.md)

## Purpose

The live/pinned curator-record bridge for reviewer supporting collections is deleted.

## Code Commentary

The removed behavior selected current authority for live review, or a unique immutable curator-generation pin and complete artifact set for recorded review. No equivalent bridge is relocated into review_judgment. The new pane reads after-tree history and proofs instead. Curator-coherence retains its own durable files and authoring route; removal of this reader is not deletion of those files.

## Retained Historical Account

The following account describes the removed implementation only. Its present-tense clauses and numbered reference labels are historical, not current product promises or live citations. The current retirement boundary and surviving owners are documented separately.

> # mcp/src/agents_remember/application/review_curator_records.py
>
> ## Governing Overview
>
> [governing route overview](overview.md)
>
> ## Purpose
>
> Read the curator records belonging to one resolved comparison and provide their existing immutable artifact references.
>
> ## Code Commentary
>
> ### Logic
>
> Live reads address the current canonical authority; recorded reads select only the comparison manifest's unique reserved curator record pin. The bound digest is opened by the shared typed generation reader, and the entire artifact set, source line, assessment count and channel are checked. A missing pin with old uncaptured metadata stays not-selected; expected missing/corrupt pins are unavailable. Neither case follows today's canonical pointer.
>
> **An unreadable owner reads as `unavailable`, never as a failed review (MIK-L25 Q8, fixed in MIK-L31 and accepted at
> 2026-09-30T05:36:19).** A closed leaf can bind about a hundred owner artifacts (ICR-L47 binds 94); with them
> missing, the owner's error named every path and the channel detail listed them again (24,725 characters), over the
> 20,000-character prose bound, so the pydantic `ValidationError` failed the whole review. `_unreadable_detail`
> keeps the landed wording (`The curator owner could not be read (<paths>): <error>`) whenever it fits
> `PROSE_MAX_LENGTH`; only a detail over the bound names the count and the first `_NAMED_ARTIFACTS` (3) artifacts
> (`_artifacts_named`: "<n> bound artifacts, listed as unreadable; the first are …") and bounds the owner's own error
> to `_ERROR_CHARACTERS` (4,000) with a stated remainder (`_bounded`). The channel's `unreadable` field still lists
> every artifact. On L25's 29 unconverted reads, 26 are byte-identical to base; the only 3 that differ are the ICR
> L47 subject+records reads, which were a `ValidationError` on base and are now a `review` with the assessments
> channel `unavailable` and 94 unreadable artifacts.
>
> Positive explicit inputs must equal the immutable owner assessment objects, complete artifact set and one exact assessment channel. Omitted, duplicate or incompatible provenance refuses before capture. Explicit empty inputs retain their meaning and do not trigger an implicit live-owner lookup.
>
> ### Conventions
>
> Use the existing typed owners and exact recorded identities. Keep operation evidence and candidate provenance in task notes.
>
> ### Invariants And Boundaries
>
> Reserved owner names identify trusted curator inputs, not arbitrary evidence citations. The bridge returns records and availability; it does not author assessments, infer a semantic result or discard other readable channels. A non-applicable plane remains explicit unavailable metadata.
>
> ### Todos
>
> None recorded.
>
> ## Evidence
>
> ### Docs References
>
> No Domain Documentation source is configured. The repository declarations below support this contract.
>
> No configured domain source could be checked.
>
> ### Repo-Internal References
>
> The cited owners carry the behavior and failure boundaries described above.
>
> - Live and recorded reads select different explicit owner addresses; an unreadable owner is an `unavailable` channel with every artifact listed. (historical reference 1)
> - The detail keeps its landed wording when it fits the prose bound, and otherwise names the count and the first three artifacts with the error bounded. (historical reference 2)
> - Both branches pinned apart: 100 artifacts summarised, 10 kept exactly (review F6, R2-2). (historical reference 3)
> - Positive supplied records require complete matching owner provenance. (historical reference 4)
> - History reads only the pinned immutable generation. (historical reference 5)
> - Uncaptured history is distinct from missing expected content. (historical reference 6)
>
> ### Cross-Repo References
>
> No separate repository supplies this contract.
>
> No cross-repository reference is required.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. Requirement packets are task authority, not an implementation proof or a fresh acceptance.

### Repo-Internal References


- Current review composition supplies judgment/proofs and no supporting-record bundle or applicability call. [7]

- The surviving pane reads the addressed record’s after-tree leaf-history rows and proof entries; this is not a relocation of the removed behavior. [8]
