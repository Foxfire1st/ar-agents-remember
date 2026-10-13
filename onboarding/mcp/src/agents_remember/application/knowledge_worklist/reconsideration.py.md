# mcp/src/agents_remember/application/knowledge_worklist/reconsideration.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**MIK-R14's worklist registrant: a decision whose `reconsider_on` target changed in the leaf becomes a
`reconsideration_candidate` item.** It is step 8 of `compute.py` (after L10's step 7). Importing it registers the
kind with its four declarations: subject `reconsider:<DEC-ID>#<alternative index>`, the facts (`decision`,
`alternative`, `option`, `alternativeStatus`, `reconsiderWhen`, `decisionStatus`, `changed`), the satisfying row
(the leaf's `reconsideration` row with that subject, `still_rejected` or `raise`) and the owner MIK-R14. The run
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
  - a `route:<dir>` target (`_route_trigger`, ruling Q1) fires only through `history_row`: a row of this leaf
    with disposition `rerouted`, `retired` or `deleted` whose subject is the route itself or a family whose routes
    in K_B or K_C contain the directory (exact string match, review F8). A family `changed` row also fires when
    its routes differ between K_B and K_C; a guarantee-only change with unchanged routes does not.
    No directory-absence trigger exists, and the validator keeps allowing route targets;
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
- **`satisfiedBy`.** The leaf's rows by subject (from K_C's history file of the owner leaf) feed
  `reconsideration_item_open`, with the superseded-decision IDs derived by this run; `satisfiedBy` names the row
  or is `null`. Superseded links are skipped before item construction. The gate and direct judge recompute
  their worklist, so their unchanged two-argument predicate receives only items of that fresh evaluation,
  not an old persisted superseded item (MIK-R148 rule3, architect ruling a00091c0).
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

- **Accepted note R6-1 (ruling 11:53:13):** after a `still_rejected` refresh, reverting the anchored code in the
  same leaf leaves the link at content that never lands, so the next leaf raises the same subject as
  `anchor_stale`. It is loud, not silent, and one answer clears it.
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


- The module docstring: base-only link evaluation, both-side supersession, unchanged triggers and row meanings. [1]

- The route dispositions and the decision prefix of the one-hop guard. [2]
- The kind registered with its facts, satisfying row and owner. [3]
- What the triggers read: both sides, the anchor classifier, the owner and the coordination root. [4]
- The run's items and link summary. [5]

- A superseded link reports skipped, null trigger and successor IDs. [6]


- Supersession uses K_B and K_C decisions while link evaluation remains K_B-only. [7]


- Skipped-link summary or fired-link evaluation. [8]

- Record targets: route, one-hop note, record file, then a triggering row. [9]

- A route fires through rerouting/retiring/deleting rows, or a changed family row whose routes differ. [10]

- An anchor classified like an entry; `stale_at_base` fires `anchor_stale` (F3). [11]
- A requirement fires only when resolved and a newer version is approved; facts carry `latestPacket` (F4). [12]

- The item facts/ID and row satisfaction use the run's superseded set. [13]

- The entry point `compute.py` calls. [14]
- The packet's conforming example: a revised assumption surfaces the rejected alternative. [15]
- `rerouted` fires and `no_impact` does not. [16]
- `touched` and `moved_or_absent` fire, `carried` does not, and the link joins no entries. [17]
- Only a newer approved version fires; no manifest, an unresolved endpoint or no root never does. [18]
- One hop: D12 raises nothing when D18 changes. [19]
- A route target fires only on a retiring row; code gone with no row raises nothing. [20]
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
