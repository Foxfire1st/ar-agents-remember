# dashboard/src/panels/detail-panel/masterSeries.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The master/series navigation suite split from `DetailPanel.test.tsx` by the
260731-EFA-L8 test split. Pins native master and sprint indexes, child drill-in and parent return through served membership keys.

## Code Commentary

The suite follows served sprint → commanded master → leaf child keys. Separate ID/name cells and parent return remain; a declared child or commanded master lacking an authored summary opens an honest not-authored page rather than an invented document.

### Logic

Seeds native entries and explicit taskTree parent/child membership, not parallel series/lifecycle indexes. Navigation follows served qualified keys; no linkedLifecycleId cross-series jump remains.

### Invariants And Boundaries

Uses shared seedTaskEntries/taskTree fixtures. One index, separate step/substep cells, intentional skip/done wording, served membership order and task-specific numbers remain asserted. Major progress stays 6/7 with seven marks and 6 of 7 done in the opened page; nested steps do not inflate that count. Markdown remains in Further-notes views. These seeded assertions are not backend count derivation or executed navigation.

### Todos

None recorded.

The disagreement case checks a separate subheading count, once-only served discrepancy rows and navigation only to present native records. A disagreement-only child block stays visible; counts are not folded into live child counts and rendering does not invent or repair a task document.

## Evidence

- Master-page discrepancies retain their own count, full row identity and present-record navigation without duplicating the child index. [2]

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References


- Seeded navigation/static-target and discarded-history assertions remain; projected major progress is 6/7 with seven marks and 6 of7 done, not executed evidence. [1]



### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.

## 260821-CLIVE Discarded-Before-Start Proof

Discarded history remains separate from live children and exposes number/name, reason and proof fingerprint with Back restoring the live row. childJson/childMarkdown witness fixture conformance, not rendered content. Current navigation follows served child/parent keys, not linkedLifecycleId cross-series jumps; no discard timestamp or live 0/1 assertion is added.
