# dashboard/src/panels/review/LeafKnowledgeChanges.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Render the leaf-wide worklist and the selected record's items from the comparison-bound tree answer.
Open item facts, gate-owned verdicts, recorded witness effects, source attribution and currentness
remain distinct. Memory-file patches stay in the change-set viewer, not this worklist panel.

## Code Commentary

ItemLine now obtains its state from itemAnswer/itemAnswerText, not satisfied_by or the existence of
history rows. A bound supplied gate answer names answered/open/undecided and its actual witness or
reason. Only a matching delivered witness-row ID contributes rowEffect; the row's disposition is no
longer printed as the deciding state. A changed witness row without an effect retains effect not
recorded. No older attempts are fetched and no effect is inferred from reason, members or counts.

The display owner suppresses item states when the worklist is unbound. File/whole open counts require
complete nonabsent bound work, no incomplete inputs and a supplied non-undecided verdict for every
counted item; otherwise the summary adds no answered/open claim. Item lines can still expose supplied
bound states beside an explicitly incomplete worklist. These are different admission levels.

LeafWorklistView marks a worklist from another requested comparison unbound before rendering it. The
subject path separately requires the matching comparison and canonical record identity, then filters
by item subject; only complete bound work can state that no item names the record.

WorklistGroupsView keeps grouping and item populations with worklistGroups, labels the no-invariant
group with the current vocabulary and adds fileAnswer from the already-held worklist. Currentness and
GateLinkage retain explicit incomplete/partial states. Degraded sides show the owner's detail, and
legacy-unavailable adds the required sentence that code changes remain shown in full.

Identifier disclosures remain group-level; required open item subjects, places and reasons do not
move into them. File buttons keep their comparison-viewer callbacks. This module offers no curation
disposition, additional gate request or semantic acceptance operation.

## Invariants And Boundaries

A recorded row is not automatically an answered item. No absent/undecided count is invented as zero;
unknown supplied measurement stays explicit. The gate decides and this component displays. Historical
recorded-effect-after-disposition wording below describes the predecessor and is not current behavior.

## Historical source-epoch account — superseded where different

Original explanatory detail and producer/test observations are preserved below. Removed dataset or
evidence branches, old mount/population/state rules and earlier execution grades are historical only.
The current account and renewed source evidence govern; prose reference markers below are inert.

> ## Purpose
>
> Render the leaf's worklist in its own open reading view and the selected record's applicable worklist
> items in subject review. The comparison-bound tree read supplies currentness and worklist facts, not
> knowledge-file patches. Missing, incomplete, unbound and unavailable measurements stay explicit.
>
> The leaf's worklist as its own open view, plus the worklist items about the selected record under a subject's review. The view reports recorded facts one line per item in open groups, with status, currentness, gate linkage and file lines that open the change-set page. It lists no knowledge file and draws no patch; identifiers close into one list per group.
> ## Code Commentary
>
> ### Recorded reviewer judgments
>
> ItemLine prints the governing history row’s recorded effect after its disposition, reading the existing row document already delivered by the leaf-wide view. A changed row lacking an effect says effect not recorded; it does not infer an effect from its reason or family members. Earlier attempts belong to the separate reading-area recorded-step sequence: this worklist still names only the row that answers the item.
>
> - ItemLine prints the governing history row’s recorded effect after its disposition, reading the existing row document already delivered by the leaf-wide view. (historical reference 29)
>
> ### Read and measurement states
>
> `ReadNotice` renders loading, not-converted, unavailable/recovery and fallback-unavailable states as open
> status content. `completeWorklist` requires non-absent source, complete state, comparison binding and no
> incomplete entries. `WorklistProblems` names the missing measurement; it never infers no applicable item
> or complete gate linkage from an incomplete answer.
>
> ### Own worklist view and subject items
>
> - **Status line.** State, item measurement, source and comparison binding; absent/unavailable is not an
>   empty measured result. A comparison mismatch is named rather than silently adopted.
> - **Degraded sides.** One line for each knowledge side that is not available or was read from a partial
>   index (`degradedKnowledgeSides`).
> - **No embedded diff.** Neither `KnowledgeDiff` nor the old `LeafKnowledgeChanges`/`LeafKnowledgeNotice`
>   exports remain. Memory patches are comparison change-set reads, not worklist content.
> - **Currentness** (`Currentness`). Open per-side counts/reasons and non-current invariants not already
>   named by worklist items, with their non-current entries and reasons.
> - **Worklist groups** (`WorklistGroupsView`). Open knowledge, planned-undelivered, other-kind and
>   unexplained-file groups. One line per item exposes recorded state, history and facts; identifiers are
>   collected into one disclosure per group. File buttons call `onOpenPath` into the comparison viewer.
> - **Gate linkage** (`GateLinkage`). Complete and partial linkage have different text; an absent/incomplete
>   measurement does not claim all hunks measured.
> - **Subject items** (`SubjectWorklistItems`). Canonical record identity and comparison must match before
>   filtering items. Only a complete bound measurement can assert that no item names the selected record.
> - The panel offers no disposition of an item. The grouping (`worklistGroups`) and the linkage counts
>   (`hunkLinkage`) come from `worklistGroups.ts`; this file renders them.

## Evidence

### Docs References

No configured domain-documentation source was available. Current implementation claims use direct
source; requirement/provenance names are not fresh runtime evidence.

### Repo-Internal References

- The module renders own-view worklist and subject items without patches; history remains recorded fact, not a UI disposition. [11]
- The own worklist view composes status, groups, currentness/linkage and marks a mismatched comparison worklist unbound before display. [12]
- The read notice exposes pending, not-converted and unavailable/recovery states as open status. [13]
- Status distinguishes absent, partial/unbound and complete work, and obtains open/all-answered text only from the gate-state display owner. [14]
- Currentness exposes noncurrent records/entries not already named by worklist items. [16]
- Open file groups preserve coverage, supplied answer state and their existing comparison-viewer callbacks. [17]
- Linkage totals and incomplete work retain separate explicit states rather than inferred complete zero. [18]
- Item lines display supplied gate verdicts; only an exact delivered witness-row match contributes its recorded effect. [22]
- Completeness rule for the worklist measurement [23]
- Record worklist items filter by canonical subject identity and retain incomplete/empty distinctions. [24]
- Items about the record on the worklist view path [25]
- Open groups show current source facts and separately supplied gate answers without inferring a verdict from row presence. [26]
- Gate linkage states complete versus partial measured totals, not semantic acceptance. [27]
- The main worklist view handles comparison mismatch as unbound and keeps source-change viewing separate. [28]
- Only the gate-named witness row effect is appended to item answer text; row presence/disposition alone no longer decides the item state. [29]
- The shared display owner reads item_states only on a bound worklist and computes file/whole open counts only for complete, nonabsent work with no missing or undecided item verdict. [30]

### Cross-Repo References

No new cross-repository boundary is introduced by these presentation helpers.



