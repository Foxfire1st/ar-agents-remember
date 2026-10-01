# mcp/src/agents_remember/memory/knowledge/detection_walk.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The deterministic walk: which recorded facts match which declared detection condition.**

This module owns the **detector** half of `KS-R14@v1`. It reads what the read policy's selection and the
diff policy's two-sided comparison already produce — it is not a second selection rule — and it emits
facts-only signals in a declared deterministic total order. The record's write, read, comparison and
retention paths are `memory/knowledge/detection.py`; the two are split along the property each one
protects rather than along a call boundary. The walk owns **no SQL, no transaction and no lock**.

Four properties are enforced here rather than documented:

- **The walk is structural.** `detect_review_conditions` reads the comparison's *recorded* facts — which
  claims' source observations moved, which items the union held, what each anchor resolved to — and never
  the bytes behind them. A budget change and a comments-only change over the same attributed files
  therefore produce the **same** condition identity and the same signal identity, which is the
  acceptance shape of the responsibility boundary: the detector reports a changed observation and the
  curator decides what it means.
- **Every signal is assembled once.** `_emit` is the only place a signal is built, so the required field
  set, the closed vocabularies and the derived detail string cannot be satisfied on one path and skipped
  on another.
- **A group keeps every contributing match.** A grouped signal carries each contributing claim's own
  relationship path and edges, because grouping is permitted and losing what was grouped is not.
- **One identity names one signal.** A union item is the union's unit, and one realization claim
  *record* can be spoken for by more than one item — a claim carrying two coverage items is two
  recorded facts about one record, not one. A single-item condition therefore groups under the record
  identity only while that identity names exactly one item, and under the **item** identity exactly
  when several items share the record, because two signals under one identity are not an order over a
  set of signals and the run's own reproducibility rule refuses them.

## Code Commentary

### Logic

**The input is the comparison, unchanged.** `DetectionWalkInput` carries the repository and governing
route, the shipped `KnowledgeDiffResult`, the sides that were read, the declared member name, an optional
scope manifest, the comparison's own unmapped changed paths, and whether the scan was truncated. The
unmapped paths are carried through rather than dropped, because dropping them would hide exactly the
changes a reviewer most needs to see.

**The walk classifies, and never re-derives.** `_claim_facts` reduces one union realization item to the
recorded facts the classification reads — path, locator kind, role, whether the source *observation*
changed, whether a record field changed, whether the claim was removed from the after side, the anchor's
resolution and its recorded and observed source identities — and reads no source bytes. `_family_members`
reads the membership edges the union holds; `_family_revision_ids` reads the family revisions in the
comparison's own stream order.

**The five conditions, and what each is about.** `detect_review_conditions` emits:

- `source_changed_on_both_sides_joined_to_same_family` — a family revision with **two or more**
  contributing members whose source observations changed;
- `one_sided_source_change_with_recorded_siblings` — exactly one contributing member, with at least one
  recorded non-contributing sibling;
- `edited_invariant_family_or_evidence_record` — a changed invariant, family or evidence record;
- `absent_anchor` — a claim whose anchor resolved `path_absent`, recorded on the **after** side;
- `removed_or_reparented_attribution` — a claim the after side no longer holds, recorded on the **before**
  side.

**The order is declared, not incidental.** `_signal_id` is a `uuid5` over
`ar-detection/v1/<condition>/<group_key>`, so a signal's identity is a function of *which recorded group*
the condition is about and which condition it is — never of the bytes behind the group. Two walks over
the same recorded structure therefore produce the same ordered sequence of identities, which is what
makes reproducibility a comparison of two sequences rather than of two sets, and why a scenario and its
harmless control produce the same signal identity rather than two signals that merely share a condition.
`_emit` returns the condition's index in the declared vocabulary beside the group key, and the walk sorts
on exactly `(condition index, group key)`.

**The group key is read from the comparison, and a shared record is regrouped onto the item.**
`_claim_facts` seeds a claim's `group_key` from the same expression it already used for the recorded
identity — `str(item.record_id or item.item_id)` — and `_regroup_shared_items` then replaces it with the
**item** identity for exactly those claims whose record identity names more than one realization item in
this union (`_ClaimFacts.group_key` is the field `_claim_signal` groups under; the family and
record-change conditions keep their own keys). The reason is that a condition about a single attribution
is a condition about the item that carried the recorded fact: naming two of them by the record they share
emits two signals under one identity, and `build_detection_run`'s deterministic-total-order rule refuses
the whole run for it — correctly, because an order that names an identity twice is not an order over a
set. Both keys are read from the comparison rather than from enumeration position, so two walks over the
same recorded structure still produce the same ordered identities, the ordinary one-item case keeps the
identity it has always had, and the relationship *path* is untouched: a path's edges name the claim
record, which is what the record identity is for.

**Limitations are derived from recorded facts, never added by habit.** `_walk_limitations` appends
`unmapped_changed_paths` when the comparison advertised one, `truncated_scan` when the walk was
truncated, `missing_attribution` when any recorded change is `anchor_resolved_elsewhere`,
`unsupported_locator` when the scan met a locator no extractor in this increment supports,
`no_counterpart_read` under the `trigger_side_only` declaration, and
`records_present_outside_the_declared_selection` when the comparison itself recorded that omission — then
the unconditional `no_semantic_assessment_performed`. That derivation matters because the signal's own
validator refuses a limitation with no omission behind it *and* an omission with no limitation.

**The declared input set is read off the comparison rather than asserted.** `_recorded_input_set` records
the discriminator the declaration requires; under a union declaration the counterpart probe comes from
`_probe_from`, which reads each reported union item's own coverage value — the shipped vocabulary, not a
second one — so the probe is R08's recorded answer rather than a re-run beside it. An empty union is a
*recorded* probe over no items, which is different from a missing probe: the union declaration is refused
for a missing one, never for an empty one. `_granularity` returns the granularity the recorded locator
kind actually supports — `attributed_span_changed` for `line_range`/`byte_range`, `source_file_changed`
otherwise — and no finer one.

### Conventions

- The walk's own helpers are private (`_emit`, `_family_signal`, `_record_change_signal`,
  `_claim_signal`, `_regroup_shared_items`); its public surface is `DetectionWalkInput` and
  `detect_review_conditions`, and
  `__all__` says so.
- **Grouped and single-claim signals are built by different builders on purpose**: `_family_signal`
  retains every contributing match with its own path and the contributing/sibling distinction, while
  `_claim_signal` records one claim on the side that held it.
- `_has_unread_locator` and `_declared_probe_omission` read the comparison's own recorded values
  (`anchor.resolution`, `omissions[].reason`) rather than re-deriving them, so a signal's declaration and
  the comparison's record cannot disagree.
- The module records the shipped boundary it does not cross by naming it in the docstring, so a reader
  can check that this is not a second selection rule.

### Invariants And Boundaries

- **Nothing about the bytes behind a changed observation can move a signal's identity or its order.**
  That is the whole point of deriving identity from the recorded group key and ordering by the declared
  condition vocabulary.
- **One identity names one signal, and the key that guarantees it is read from the comparison.** A
  record identity shared by several union items cannot name the single-item signals about them; the
  item identity takes over there, and where it is read from is what keeps the order a function of the
  recorded structure rather than of the order the items happened to arrive in (the run builder refuses
  an order that names one identity twice, before anything is recorded).
- **One place builds a signal.** A new condition cannot be emitted through a path that skips the required
  field set, the closed vocabularies or the rendered detail.
- **A grouping never loses a contributing match**: each one keeps its own relationship path, its edges
  and its reached item.
- **The walk materializes nothing.** It reads the union R08 already materialized and returns values; the
  manifest it records when no destination has been verified is a *reference* whose destination is
  deliberately not the durable route, so resolution reports it unresolved until that route exists.
- **Boundary.** No SQL, no store, no transaction, no lock, no file access, and no publication; and no
  classification of anything the comparison did not record.

### Todos

None recorded. The walk's `unmapped_changed_paths` and truncation flags come from the caller, so a caller
that neither advertises nor truncates gets the complete-for-declared-policy status — which is a bounded
scan result and is not upgraded to a claim about attribution accuracy.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The walk's whole input: the shipped comparison, the sides read, the declaration, the manifest reference and the comparison's own advertised gaps. [1]
- **The stable signal identity, derived from the recorded group key rather than from the bytes behind it.** [2]
- **The regroup that keeps one identity per signal: the record identity while it names one union item, the item identity exactly when several items share the record, both read from the comparison.** [3]
- The recorded facts one union realization item is reduced to, reading no source bytes. [4]
- The membership and family-revision reads the family conditions classify on. [5]
- **The five declared conditions and the declared deterministic total order: the condition vocabulary's own order first, then the recorded group key.** [6]
- **The grouped signal that keeps every contributing match, its path, its edges and its sibling set.** [7]
- The single-claim signal recorded on the side that held it. [8]
- **The one place a signal is assembled: the required field set, the derived limitations and the rendered detail.** [9]
- **The limitations derived from recorded facts, plus the unconditional one — never a limitation with no omission behind it.** [10]
- The unsupported locator read as a declared scope limitation rather than a negative match. [11]
- The omission read from the comparison's own recorded reason, so declaration and omission cannot disagree. [12]
- **The recorded input set built from the declaration's own discriminator, with the probe read off the union rather than re-run.** [13]
- The observed granularity one locator kind supports, and no finer one. [14]
- **The unretained manifest reference: a real reference at a destination that is deliberately not the durable route, so it resolves unresolved rather than being fabricated as retained.** [15]
- The comparison the walk reads and the item shape it classifies on. [16]
- The declared conditions and declared input sets the walk emits from. [17]
- The record half: the store's own refusals, the write path and the read path this walk's values are handed to. [18]
- **The cases that measure the scenario/control identity, the declared order, the retained group and the unsupported locator.** [19]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
