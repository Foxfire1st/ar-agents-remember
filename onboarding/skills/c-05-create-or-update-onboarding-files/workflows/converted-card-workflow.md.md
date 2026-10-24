# skills/c-05-create-or-update-onboarding-files/workflows/converted-card-workflow.md

## Governing Overview

[Repository overview](../../../overview.md)

## Purpose

Canonical authoring workflow for converted file cards and route overviews: Markdown is the authored explanation, native citation authoring owns references, and the knowledge writer owns realizations, proofs and history. Root `skills/` is the authoring source and the packaged copy the tool server serves is its only generated copy, so no harness starter package inherits this contract any more.

## Code Commentary

Converted Markdown has no legacy metadata or Update History. The Curator writes citation-table inputs, then the document-scoped fixer resolves them against the code candidate and converts them to numbered prose over sidecar references. Existing-key reauthoring replaces the old cited line; orphan removal leaves surviving keys unchanged. Preview/apply results are examined for refusal, unreadable inputs and unresolved targets rather than just ok=true.

Converted carryover selects paired content and missing records, validates and commits nothing; the recovery Curator authors own rows and ordinary closeout owns publication. It is not the former forbidden legacy copy/metadata/commit apply. The current source names where that procedure lives: `c-10-adopt-memory-baseline` `workflows/carryover-from-branch.md`, the retained recovery-leaf → curator-row → normal-closeout publication sequence behind `memory_carryover_plan` / `memory_carryover_apply`. Route indexes stay uncommitted caches regenerated with `route_index_refresh`, scoped to the leaf's contract.

Body maintenance comes before anchors. Mechanical blob/content/line refreshes do not count as authored card changes. Moved behavior carries its entries through writer-owned covers before creating current prose and retiring the old sidecar. Deleted-source cleanup first checks whether behavior moved; surviving callers' references are retargeted to actual replacements or removed.

The newly built normal gate accepts current source-bound updated/no_impact statements; updated needs a counted card/reference change, and realization/proof-only changes do not count. A governing route has its own subject. L53's own changed cards are exempt from updated rows under amended rule 1 and answered by their measured counted changes; that rollout qualification is not the general post-landing workflow. Sidecar JSON, source pins and reference numbers are never manually fabricated.

## Evidence

### Repo-Internal References

- Converted prose, citation targets and sidecar writers have distinct ownership; route overviews preserve purpose-first layout. [1]
- Native citation preview/apply resolves new and exact-key references and exposes refused/unresolved results. [2]
- Move/delete handling preserves behavior and entry ownership, then ordinary current-row treatment answers the source and route. [3]

## Inherited Source-Epoch Commentary

The following account preserves the former distribution-copy card and its useful explanations, history and warnings. It is inherited scope, not a second current contract or a fresh certification of its dated/currentness, tool, provider, registry, execution or permission claims. The canonical account above retains its existing attribution and qualifications; the authored source below is the authority for the file. Historical reference labels in this quotation are provenance labels, not reference identities of this card.

> # mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/converted-card-workflow.md
>
> ## Governing Overview
>
> [mcp route overview](../../../../../../../overview.md)
>
> ## Purpose
>
> **The c-05 skill's workflow for converted memory: how a curator creates and maintains a card once the memory tree
> holds `knowledge/layout.json` (L37).** It replaces `file-level-onboarding-workflow.md` on converted
> trees. This is the packaged copy that `runtime_install` ships; the canonical source is
> `skills/c-05-create-or-update-onboarding-files/workflows/converted-card-workflow.md`, and the harness starter
> copies are generated from it by `scripts/sync-skills.py`. All copies are byte-identical.
>
> ## Code Commentary
>
> The newly built normal onboarding answer is the current source-bound updated/no_impact judgment: updated additionally needs authored Markdown or nonmechanical references changes; realizes/proves-only edits do not count. Every governing route has its own subject, and later covered-source movement reopens the answer. Moves preserve behavior/entry ownership before retiring the old card; gone-path references refuse publication/landing rather than granting permanent advisory immunity. These statements supersede the older counted-edit-or-row gate wording in the retained account. This L53 rollout itself uses amended rule1 counted card changes, without updated rows or later backfill.
>
> - Current curation contract separates normal judgment domains from rollout and lifecycle ownership. (historical reference 10)
>
> ### Logic
>
> The workflow states, in order:
>
> - **What a converted card is.** Two files at the mirrored path: the Markdown (title, governing overview, purpose,
>   commentary, evidence) and the sidecar (references, and the `realizes` and `proves` entries). The Markdown has no
>   metadata table, no Update History and no citation tables. Evidence is `- <finding> [n]` lines; `[n]` names
>   `references["n"]`. Target kinds are `code`, `test`, `requirement`, `external` and `unresolved`; anchor locators
>   are `symbol`, `line_range` and `file`.
> - **Create a card for a new source file.** Write the Markdown with a citation table (`| Finding | Anchor |
>   Source |`), then preview the finite cards of the change in one citation-fix call and repair them
>   in one call, with `documents` or repeated CLI `--document`; singleton `document` remains valid.
>   Converted selection needs no `--expected-snapshot`. Read the full detail's `authoring` block:
>   `authoredReferences`, `createdSidecars`, `unresolvedTargets`, `refused`, `unreadableSidecars`. The refusal reasons
>   include two tables with no blank line between them when either is a citation table: a delimiter row (every cell
>   three dashes or more) inside a table; the reason names the line, and a blank line above the second header fixes it.
> - **Refresh a card after the code changed.** Prose is edited directly. One reference is re-authored by replacing
>   its `- <finding> [n]` line with a one-row table whose finding ends in `[n]`; a leftover line with the same number
>   refuses the card. Mechanically moved anchors are re-recorded by the same run and never count as a change.
> - **Remove a reference**: delete its line and run the fixer on that card; a tree-wide run never removes one.
> - **A source file moved or was deleted**: entries first, through the writer (`moved` rows with the new path, or
>   covers with `remove: true`), then the card and the old sidecar, then the other cards that cite the file.
> - **Answer every changed-source card and its nearest governing route** with a current
>   `onboarding:<path>` or `onboarding:<route>/overview` row through `knowledge-ingest`.
>   `updated` requires a counted Markdown or nonmechanical `references` change; `no_impact`
>   gives the reviewed reason the card still holds. A counted edit alone never answers.
>   The writer binds the row to the covered source contents, so another source edit requires
>   the row to be named again. Mechanical anchors and realization/proof-only changes do not count.
> - **Never on converted memory**: a metadata table, an Update History entry, `lastVerifiedCommit*`, a citation table
>   left after the fixer ran, hand-written sidecar anchors or reference numbers, and `memory_carryover_apply`.
>
> ### Conventions
>
> - The workflow is instruction text only; the behaviour it describes is `memory/conversion/card_authoring.py` (the
>   authoring), `memory_quality/reference_state.py` (the re-recording) and the writer (`knowledge-ingest`).
>
> ### Invariants And Boundaries
>
> - **Never write sidecar JSON by hand.** The fixer authors `references`; the writer authors `realizes` and
>   `proves`.
> - Name the finite card list to avoid an unrelated whole-tree sweep; batch selection keeps the same
>   per-card authoring/refresher semantics and does not hand-write sidecar JSON.
> - The statement "Numbers are not reused" has one known exception: a removed highest number is reused by a later
>   run.
> - With a document named, the fixer's result lists that document's stale references only, and the MCP
>   status answers counts and first actionable entries; complete authoring/stale populations stay
>   in detail. A named list preserves that same selection isolation per card.
>
> ### Todos
>
> - None recorded.
>
>
> The overview contract reads from purpose: title, governing overview, then `## What This Repo Is`, `## What This Area Is` or `## Purpose`; construction follows, then invariants/boundaries, and all citation lines stand together at the end. An overview change belongs in its applicable body section, never a leaf- or date-named section. The instruction states validator refusals for misplaced purpose, dated/leaf sections and nonterminal citation lines; source instruction is not evidence that a validation invocation ran.
>
> ## Evidence
> ### Docs References
>
> No domain documentation source is configured for this repository (`system/sources.md` carries no
> `Domain Documentation` entries). The design authority is the L37 decisions of 2026-10-01T10:06:02 and 11:12:11 in `37_cutover-to-text-storage.json`, with `MIK-R21@v1`, `MIK-R24@v1` rule 5 and `MIK-R30@v1`; it lives outside the code and memory
> repositories, so it is named here and not cited as a row.
>
> No configured live documentation source was available for this pass.
>
> ### Repo-Internal References
>
> - What a converted card is, and that sidecar JSON is never written by hand. (historical reference 1)
>
> - Creating a card for a new source file: the Markdown, the citation table, one fixer run and the refusal reasons. (historical reference 2)
>
> - Refreshing a card: prose, re-authoring one reference by its number, and mechanical moves. (historical reference 3)
> - Removing a reference, and the moved-source and deleted-source procedures. (historical reference 4)
> - Every changed file and governing overview needs a current updated or no-impact row; counted edits alone never answer, and converted cards keep no legacy metadata or Update History. (historical reference 5)
> - The c-05 skill routes converted memory to this workflow. (historical reference 6)
> - The authoring the workflow drives. (historical reference 7)
>
> - The refusal for two tables with no blank line between them. (historical reference 8)
>
> ### Cross-Repo References
>
> No meaningful cross-repo references found: the workflow is repository-local instruction text.
>
> No cross-repo boundary is crossed by this file.
>
> - Overview authoring is purpose-first, changes belong in their body section, and citation lines terminate the overview. (historical reference 9)

Inherited reference 1 commentary (not a revalidated target):

> What a converted card is, and that sidecar JSON is never written by hand.
>
> Anchor: "Never write sidecar JSON by hand."

Inherited reference 10 commentary (not a revalidated target):

> Current curation contract separates normal judgment domains from rollout and lifecycle ownership.

Inherited reference 2 commentary (not a revalidated target):

> Creating a card for a new source file: the Markdown, the citation table, one fixer run and the refusal reasons.

Inherited reference 3 commentary (not a revalidated target):

> Refreshing a card: prose, re-authoring one reference by its number, and mechanical moves.
>
> Anchor: "Refresh a card after the code changed"

Inherited reference 4 commentary (not a revalidated target):

> Removing a reference, and the moved-source and deleted-source procedures.
>
> Anchor: "Remove a reference"

Inherited reference 5 commentary (not a revalidated target):

> Every changed file and governing overview needs a current updated or no-impact row; counted edits alone never answer, and converted cards keep no legacy metadata or Update History.
>
> Anchor: lines 156-183

Inherited reference 6 commentary (not a revalidated target):

> The c-05 skill routes converted memory to this workflow.
>
> Anchor: "Converted Memory"

Inherited reference 7 commentary (not a revalidated target):

> The authoring the workflow drives.

Inherited reference 8 commentary (not a revalidated target):

> The refusal for two tables with no blank line between them.

Inherited reference 9 commentary (not a revalidated target):

> Overview authoring is purpose-first, changes belong in their body section, and citation lines terminate the overview.

## Canonical Source Ownership

The authored file is the canonical contract; its measured byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. The following whole-file reference locates that authored contract; it does not convert inherited statements into executed or whole-card acceptance.

- The authored source owns this contract; the distribution copy is not a separate authority. [4]
