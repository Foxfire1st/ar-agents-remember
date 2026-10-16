# dashboard/src/panels/detail-panel/model.ts

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

Pure reader helpers for bounded text, parsed-time decisions, registers/prose, major-step marks and served ancestry; no series/slug selection fallback.

## Code Commentary

### Logic



`docChain(entry, tasks)` follows served parent keys with a seen-key cycle guard, using exact task entry selection for ancestors; missing parents end the chain.

### 260928-MIK-L126 Current Delta — Newest-First Decision Ordering

`orderDecisionsNewestFirst` orders entries by parsed recorded time, newest first, independently of storage order. Equal timestamps retain input order. Unparseable timestamps follow parseable entries and retain their input order among invalid peers. The preview and whole-log reader call this shared helper; its comparator does not establish how a backend writer stores records.



### Form and bounded-reader model

`docForm` reads the served summary form; identity uses entry.key rather than a transient content object. Child grouping and stage counts come from served entries, not document-status classification.

Registers require a register heading and a parseable table; canonical slots are Judgment then Priority. Free-form Further notes exclude structured sections, recognized registers and a byte-identical objective repeat. `boundedText` checks both eight-line and character limits so a single huge paragraph cannot render unbounded. Review summaries read the supplied whole-round count rather than deriving it from a capped list. An ancestry chain follows served parent keys and never invents a series fallback. Optional prose/completion/dependency fields remain content fields, not topology inference. stepMarkStates emits one state per major step, not nested marks. A done parent stays done; otherwise an inProgress or done child promotes the parent to current before blocked/next fallback. Entry major-step totals remain served facts; full nested rendering stays with taskBlocks.

### Execution-graph and discarded-subtask view fields

TaskSummary retains optional executionGraphView and discarded audit data as supplied. Graph display and discard history remain separate from live membership/counts; this model does not fabricate absent fields.

### Conventions

Pure functions only — no React, no stores.

### Invariants And Boundaries

Navigation uses entry keys and exact canonical references in indexRows; no linkedLifecycleId or local slice fallback remains.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- Decision ordering is parsed-time descending, stable for ties and invalid peers, with invalid timestamps after valid ones. [3]










### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
