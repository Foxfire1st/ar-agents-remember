# skills/c-05-create-or-update-onboarding-files/workflows/converted-card-workflow.md

## Governing Overview

[Repository overview](../../../overview.md)

## Purpose

Canonical authoring workflow for converted file cards and route overviews: Markdown is the authored explanation, native citation authoring owns references, and the knowledge writer owns realizations, proofs and history. Generated copies inherit this contract.

## Code Commentary

Converted Markdown has no legacy metadata or Update History. The Curator writes citation-table inputs, then the document-scoped fixer resolves them against the code candidate and converts them to numbered prose over sidecar references. Existing-key reauthoring replaces the old cited line; orphan removal leaves surviving keys unchanged. Preview/apply results are examined for refusal, unreadable inputs and unresolved targets rather than just ok=true.

Body maintenance comes before anchors. Mechanical blob/content/line refreshes do not count as authored card changes. Moved behavior carries its entries through writer-owned covers before creating current prose and retiring the old sidecar. Deleted-source cleanup first checks whether behavior moved; surviving callers' references are retargeted to actual replacements or removed.

The newly built normal gate accepts current source-bound updated/no_impact statements; updated needs a counted card/reference change, and realization/proof-only changes do not count. A governing route has its own subject. L53's own changed cards are exempt from updated rows under amended rule 1 and answered by their measured counted changes; that rollout qualification is not the general post-landing workflow. Sidecar JSON, source pins and reference numbers are never manually fabricated.

## Evidence

### Repo-Internal References

- Converted prose, citation targets and sidecar writers have distinct ownership; route overviews preserve purpose-first layout. [1]
- Native citation preview/apply resolves new and exact-key references and exposes refused/unresolved results. [2]
- Move/delete handling preserves behavior and entry ownership, then ordinary current-row treatment answers the source and route. [3]
