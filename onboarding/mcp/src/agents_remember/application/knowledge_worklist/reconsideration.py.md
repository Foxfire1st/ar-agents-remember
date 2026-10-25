# mcp/src/agents_remember/application/knowledge_worklist/reconsideration.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**MIK-R14's worklist registrant: a decision whose `reconsider_on` target changed in the leaf becomes a
`reconsideration_candidate` item.** It is step 8 of `compute.py` (after L10's step 7). Importing it registers the
kind with its four declarations: subject `reconsider:<DEC-ID>#<alternative index>`, the facts (`decision`,
`alternative`, `option`, `alternativeStatus`, `reconsiderWhen`, `decisionStatus`, `changed`), the satisfying row
(ordinarily the leaf's `reconsideration` row with that subject, `still_rejected` or `raise`, but not a noncurrent candidate refresh) and the owner MIK-R14. The run
returns the items, each with `satisfiedBy`, and a `reconsideration.links` summary of every link it evaluated.

## Code Commentary

### Logic

- **What is read.** Every decision of **K_B** (`_Evaluation.run`), each of its `reconsider_on` links through
  L13's `reconsider_links` (only links that name a `rejected` or `deferred` alternative). A decision absent from
  K_B raises nothing: it was authored in this leaf (worker note 10, like MIK-R08's K_B-only invariants).
- **Superseded decisions are skipped.** Supersession is derived from the decisions of **K_B and K_C**,
  while link evaluation still ranges over K_B decisions only. A successor authored in the candidate therefore
  silences its base decision even when a linked target changed. Each skipped link reports `skipped: superseded`,
  `trigger: null` and the `successors` IDs (`_skipped`). A candidate decision without that supersession
  suppresses nothing and raises no item merely by being new. This extends Q5 through MIK-R148@v1; it does not
  add a trigger or change the meaning of the two answering rows.
- **Triggers (rule 1), one per target type** (`_evaluate`):
  - a record ID (`_record_trigger`): `record_file` when its record file's location or bytes differ K_B→K_C
    (`KnowledgeSide.record_file`, as MIK-R08 compares records), else `history_row` when this leaf's history file
    in K_C holds a row about it with one of `TRIGGERING_DISPOSITIONS` (`history.row_about`);
  - a `DEC-` target never fires: the summary notes "one hop: a change to a decision never chains on" (rule 3);
  - a `route:<dir>` target first fires `route_absent` when CodeTrees has at least one base path and no candidate path beneath the directory. Otherwise a qualifying family row fires `history_row` when either side gives the family a route equal to or under that directory (`.` covers all). Rerouted/retired/deleted dispositions qualify, as does a changed family row whose routes differ. A guarantee-only change does not. No registered row uses the route itself as subject.
  - an anchor (`_anchor_trigger`) is classified by L08's own `Classifier.classify_anchor`, like an entry but never
    one: `touched` or `moved_or_absent` fires `anchor`; `stale_at_base` fires `anchor_stale` (review F3, ruling
    05:31:11), so a stale link anchor asks for a judgment instead of going quiet. The summary records the class.
  - a requirement endpoint (`_requirement_trigger`) resolves through L13's `resolve_requirement_endpoint` from the
    run's `coordination_root`, then `requirement_approval` reads the owning task's manifest. An unresolved endpoint
    or no coordination root never fires (`approvalState: unknown`); otherwise the summary records
    `approvalState`, `latestApproved` and any `detail`, and the link fires `requirement_version` only when the
    approved version is newer than the link's (`newer_than`). The fired facts carry `version` and, since review F4,
    `latestPacket`, so the writer re-points to exactly what the curator judged.
- **Items (rules 3 and 5).** `_item` makes one item per alternative with at least one fired link. `facts.changed`
  lists every fired link without its `subject` and `identity`: `link` (the index in `links`), `target` (the
  `link_target_key` spelling, through `_target_key`), `trigger` and the trigger's own facts (`paths`, `row`,
  `rowSubject`, `disposition`, `entry`, `version`, `latestApproved`, `latestPacket`). The item ID is the registry's
  `item_id` over the kind, the subject and each fired link's `[link, target, trigger, identity]`, so a new change
  to the same target gives a new ID while the subject stays the same.
- **`satisfiedBy` and currentness.** Ordinary triggers use the leaf's subject row. A candidate reauthored anchor at the linked reconsider_on position is first classified; when it differs from the base target and is not current at C, refresh_not_current remains open regardless of an ordinary answering row. The current link must be restored to K_B or made current. Superseded decisions remain a separate prior exemption. Fresh gate/direct evaluations additionally observe the candidate target and can discard the repaired currentness trigger before judging any remaining ordinary trigger; this is not blanket row satisfaction of a stale target.
- **Summary.** `reconsideration_candidates` returns `ReconsiderationRun(items, {"links": evaluated})`, which
  `compute.py` persists as the document's `reconsideration` key.

### Conventions

- Items are sorted by subject; the summary lists links in decision-ID order, each with `subject`, `link`,
  `target` and `trigger` (`null` when it did not fire).
- Nothing reads `reconsider_when` except to copy it into the facts (packet Exclusions: no prose evaluation).

### Invariants And Boundaries

- **A `reconsider_on` link fires only on the packet's triggers, one hop only; an unresolved endpoint or a task
  without a manifest never fires.** Candidate invariant. Realized by `_evaluate` and its four trigger methods,
  the `_DECISION_PREFIX` guard and the `endpoint.state != "resolved"` / `newer_than` conditions; proved by
  `test_a_revised_assumption_surfaces_the_rejected_alternative`,
  `test_a_triggering_history_row_surfaces_and_other_dispositions_do_not`,
  `test_a_linked_anchor_triggers_when_touched_or_absent_and_not_otherwise`,
  `test_a_requirement_endpoint_triggers_only_on_a_newer_approved_version`,
  `test_one_hop_a_decision_change_never_chains_on` (which fails with the guard removed),
  `test_a_route_target_fires_only_through_a_rerouting_or_retiring_row` and
  `test_a_stale_link_anchor_raises_and_still_rejected_reanchors_it`; on real data by the worker's scratch leaf
  (1 candidate before the change, 3 after, `MIK-R04@v1` unresolved with `trigger: null`).
- **The link anchor is never an entry.** It is classified with kind `link` and never joins the run's `entries`
  (asserted in the anchor trigger test).
- **Unconverted memory reads are unchanged.** The registrant runs only inside a worklist, which exists only on a
  converted leaf; the real (unconverted) L14 contract gives `leaf_worklist → None` on the base and L14 builds
  (`unconverted.txt`).

### Todos

- **Current correction to historical R6-1.** Reverting code after a still_rejected anchor refresh can now surface refresh_not_current in this same leaf. The earlier next-leaf-only/loud-and-one-row-clears-it limitation is no longer the current contract: an invalid current target needs restoration or repair, not another unchanged judgment row.
- **L09:** an unanswered candidate blocks closeout (D29) through the gate's generic rule.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R14@v2` of task
`260928_maintained-invariant-knowledge` and its leaf document `14_reconsideration-surfacing.json` (rulings
2026-09-30T04:37:56 to 11:53:13); they live outside the code and memory repositories, so they are named here and
not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References




- Base-only reconsideration evaluation includes route absence and noncurrent candidate-refresh refusal, with both-side supersession retained [1]



- The route dispositions and the decision prefix of the one-hop guard. [2]
- The kind registered with its facts, satisfying row and owner. [3]

- What the triggers read: both sides, the anchor classifier, the owner and the coordination root. [4]

- The run's items and link summary. [5]

- A superseded link reports skipped, null trigger and successor IDs. [6]


- Supersession uses K_B and K_C decisions while link evaluation remains K_B-only. [7]


- Skipped-link summary or fired-link evaluation. [8]

- Record targets: route, one-hop note, record file, then a triggering row. [9]



- Route absence needs no history row; family fallback accepts equal or nested routes and no route-subject row [10]





- Candidate anchor refreshes are checked for currentness before ordinary base-anchor trigger classification [11]


- A requirement fires only when resolved and a newer version is approved; facts carry `latestPacket` (F4). [12]

- The item facts/ID and row satisfaction use the run's superseded set. [13]

- The entry point `compute.py` calls. [14]
- The packet's conforming example: a revised assumption surfaces the rejected alternative. [15]
- `rerouted` fires and `no_impact` does not. [16]
- `touched` and `moved_or_absent` fire, `carried` does not, and the link joins no entries. [17]
- Only a newer approved version fires; no manifest, an unresolved endpoint or no root never does. [18]
- One hop: D12 raises nothing when D18 changes. [19]
> Retained historical citation wording: The predecessor route-row-only regression caption is historical; the now-released test source asserts route_absent without a row. Its original group remains inherited custody, not the old proposition renewed. [20]
- A superseded decision raises nothing and its links are listed skipped. [21]
- A stale link anchor raises `anchor_stale`. [22]



- A candidate successor suppresses the base decision and lists its ID; the stored rule requires supplied context. [24]

- Without a successor the changed target still raises. [25]

- An unrelated candidate decision suppresses nothing and raises no item itself. [26]



- The closeout gate recomputes its worklist and reads no earlier persisted document. [27]

- Direct landing computes its worklist over exact sides before judging. [28]

- The registered row predicate keeps the two-argument satisfying-function call. [29]

### Cross-Repo References

The requirement trigger reads a task under the coordination root (`tasks/<repository>/<path>/requirements/manifest.json`)
through `requirement_endpoint.py`; the task documents are coordination artifacts outside the code repository.

- The manifest read happens in the resolver module, from the resolved task root. [23]


### Source-assertion qualification

The unrelated candidate fixture carries no `reconsider_on` link, so its absence
assertion alone is not a stimulus-rich proof about newly wired candidate links.
The source evaluation loop remains base-only. Cited assertions are not a fresh
collection or execution result. Supersession rationale formerly attributed to
a3d79e94 is convergently owned by the landed MIK-R148 account above.


## Current source contract

Route reconsideration now fires when a route had files at B and none at C without needing a history row; family-row fallback accepts a family route equal to or beneath the requested directory rather than requiring exact membership. Candidate reauthored reconsider anchors that are not current at C raise refresh_not_current.

No registered row has the route itself as its subject. A noncurrent refresh is not answered merely by still_rejected/raise: restore the base link or make the target current. Supersession is checked separately and takes precedence; the direct gate also re-observes restored/current targets before judging remaining ordinary triggers. Base-only link evaluation and the one-hop decision-target guard remain.

These spans and input-card identities were independently rechecked after the supported L61 sync. Source observation supplies no test execution, installed-host acceptance or semantic verdict for unrelated inherited material.


- Directory absence fires without a history row; fallback family routes may be equal or nested. [30]

- A reauthored candidate reconsider anchor is checked for currentness before the base-anchor trigger. [31]

- Current reconsideration facts use the shared satisfying predicate after deriving supersession. [32]

- A noncurrent refresh remains open even with an ordinary answering row, except superseded decisions. [33]

- The gate independently observes restoration/currentness before judging remaining triggers. [34]





- The route-target test checks that `no_impact` and unchanged-route `changed` family rows do not fire, a `retired` family row does, and directory absence without a history row fires `route_absent`. Source caption: `test_a_route_target_fires_only_through_a_rerouting_or_retiring_row` [20]




> Retained earlier card wording; superseded by the current account above:
> - A route target fires only through a rerouting or retiring row; a route whose files are gone and which no history row records fires a `route_absent` change rather than nothing. [20]
