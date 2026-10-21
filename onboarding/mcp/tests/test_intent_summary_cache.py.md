# mcp/tests/test_intent_summary_cache.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Declare exact native intent-summary HTTP reuse, refusal freshness, consumed-input invalidation and finite dependency/age/size bounds over controlled Git and converted-memory fixtures.

## Code Commentary

The composed TestClient route compares counted/unavailable bodies with the native summary. Conditional304 avoids recounting and computational Git children; _reads deliberately excludes working-view status and object-store count-objects freshness checks. Code edits with restored timestamps, memory edits, real-index changes, HEAD and comparison-record edits invalidate before settling.

Closed-record object loss and later restoration retain the owner refusal/count semantics. Timestamp-only index touches reuse; changed index bytes reopen; unobservable index reads require native production each time. Refused live/closed reads can settle, while restoration during an unavailable production must not bind that refusal to the restored object. The wrapper now intercepts summarize_review, the current supplied-resolver seam.

Dependency/value histories stay bounded at the configured capacity, and unchanged summary inputs do not scan40 versus4000 unrelated note files. A deliberately held summary reader permits task, file-diff and master HTTP reads to complete on another worker. Shared named hang guards and finally release protect that controlled concurrency assertion.

A movable clock checks native reproduction beyond the default age, input invalidation inside the age and recomputation after the admission table evicts an old key. Injected readers now take the optional comparison argument; the eviction assertion names the four-part repo/master/leaf/None key. The cases do not separately compare two numbered summaries or authenticate their record resolution.

## Invariants And Boundaries

These are declared in-process fixtures, not a native fleet latency/CPU result or fresh execution. Zero computational Git is narrower than no Git at all. Real Git commands and fixture memory edits occur only when these tests run; this card performs neither. Numbered port-shape accommodation alone does not prove distinct recorded comparisons were read.

## Evidence

- Freshness-only children are excluded; counted/conditional and input-invalidating cases retain native equality. [9]
- Index/object/address/refusal checks keep native unavailable versus counted facts. [10]
- Unrelated note populations are not walked and restoration during summarize_review cannot settle the prior refusal. [11]
- A blocked numbered-shape reader permits unrelated changeset requests. [12]
- Clock, changed-input and admission-eviction cases retain bounded reuse with a four-part summary key. [13]
