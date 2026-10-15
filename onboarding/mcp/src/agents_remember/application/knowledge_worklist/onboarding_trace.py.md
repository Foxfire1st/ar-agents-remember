# mcp/src/agents_remember/application/knowledge_worklist/onboarding_trace.py

## Governing Overview

[Application overview](../overview.md)

## Purpose

Resolve the paired memory sides, storage settings and exact candidate source blobs used to compute and persist onboarding-trace worklist items.

## Code Commentary

`ONBOARDING_TRACE_KIND` registers card and route-overview subjects with `sources`, `markdown`, `sidecar`, `countedChange` and `sourceBlobs` facts. The ordinary MIK-R53 satisfying rule requires the leaf's current row: `updated` also needs a counted Markdown/reference change; `no_impact` needs the current source binding. A counted card change alone is not the new ordinary rule. [31]

`TraceSideRequest` names K_B, K_C, the code repository/base and optional held conversion/cache. `onboarding_trace_sides` reads candidate directory bytes or its exact Git tree and the pinned memory base. Its retained low-level conversion branches return no trace sides when neither side is converted, report mixed-format or missing-version inputs as incomplete, and reuse a held converted base or the conversion cache when needed. These helper branches do not authorize a caller to bypass the separate converted-memory floor. Only onboarding, history and the layout marker feed the comparison. [32]

`trace_context` first reads the memory worktree's own storage settings, then resolves the contract context; a failed resolution uses the strict default storage. Existing selectors record the bytes actually consumed and observed absences, not a disconnected before/after guess. [32]

`worktree_code_blobs` captures committed and uncommitted source files in C through the standard candidate-tree reader; deleted paths yield `None`, which the pure gate renders as absent. Git read failures are not unchanged-source evidence. `worklist_onboarding` accepts this blob mapping explicitly, computes the trace over the worklist's own changed paths, forwards its `identicalChanges` as `source_groups`, and merges its items. The merged list sorts by kind/subject, retains source facts and satisfying row identities, recomputes its digest, and lists unnecessary rows separately. Side/history failures make the worklist incomplete instead of silently shortening it. [33]

Amended R53 rule 1 is a bounded pre-landing exception for this leaf's own measured changed cards; it does not change the ordinary source-bound doctrine or authorize unsupported `updated` rows, changed-card `no_impact`, or later backfill.

## Evidence

### Repo-Internal References

- Registration and ordinary row/source requirement. [31]
- Side inputs, conversions and actual settings reads. [32]


- The exact candidate blob map and identical-change source groups reach the complete trace merge [33]



### Docs References

The task's amended R53 rule 1 is external coordination authority, not new source-code enforcement. No separate live domain source was used for this repair.


## Current source contract

The bridge passes document.identicalChanges as source_groups into onboarding_trace_result alongside the exact captured code_blobs and changed paths. This keeps the gate comparison aware of the complete source set of an equal-change representative.

The bridge does not invent groups, recapture code or authorize counted edits alone. Ordinary source-current onboarding rows and the separate side/input-failure handling still govern; no historical leaf-specific exception becomes general authoring authority.

These spans and input-card identities were independently rechecked after the supported L61 sync. Source observation supplies no test execution, installed-host acceptance or semantic verdict for unrelated inherited material.


- The bridge forwards actual identical-change groups and captured code blobs into onboarding trace evaluation. [34]
