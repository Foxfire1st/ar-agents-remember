# mcp/src/agents_remember/memory/knowledge/detection_walk.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/detection_walk.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T05:15+02:00 |
| lastVerifiedCommitHash | `e963a01c6804570d597e451eaa069eaba66bd3ec`|
| lastVerifiedCommitDate | 2026-09-18T04:45:39+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l14` uncommitted source; base `4264dcc9decf50e64c863e9c6526ea09117be71b` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The deterministic walk: which recorded facts match which declared detection condition.**

This module owns the **detector** half of `KS-R14@v1`. It reads what the read policy's selection and the
diff policy's two-sided comparison already produce — it is not a second selection rule — and it emits
facts-only signals in a declared deterministic total order. The record's write, read, comparison and
retention paths are `memory/knowledge/detection.py`; the two are split along the property each one
protects rather than along a call boundary. The walk owns **no SQL, no transaction and no lock**.

Three properties are enforced here rather than documented:

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
  `_claim_signal`); its public surface is `DetectionWalkInput` and `detect_review_conditions`, and
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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The walk's whole input: the shipped comparison, the sides read, the declaration, the manifest reference and the comparison's own advertised gaps. | `DetectionWalkInput` | mcp/src/agents_remember/memory/knowledge/detection_walk.py:64-81 |
| **The stable signal identity, derived from the recorded group key rather than from the bytes behind it.** | `_signal_id` | mcp/src/agents_remember/memory/knowledge/detection_walk.py:84-94 |
| The recorded facts one union realization item is reduced to, reading no source bytes. | `_ClaimFacts`; `_claim_facts` | mcp/src/agents_remember/memory/knowledge/detection_walk.py:97-136 |
| The membership and family-revision reads the family conditions classify on. | `_family_members`; `_family_revision_ids` | mcp/src/agents_remember/memory/knowledge/detection_walk.py:152-179 |
| **The five declared conditions and the declared deterministic total order: the condition vocabulary's own order first, then the recorded group key.** | `detect_review_conditions` | mcp/src/agents_remember/memory/knowledge/detection_walk.py:182-247 |
| **The grouped signal that keeps every contributing match, its path, its edges and its sibling set.** | `_family_signal` | mcp/src/agents_remember/memory/knowledge/detection_walk.py:250-289 |
| The single-claim signal recorded on the side that held it. | `_claim_signal`; `_record_change_signal` | mcp/src/agents_remember/memory/knowledge/detection_walk.py:292-360 |
| **The one place a signal is assembled: the required field set, the derived limitations and the rendered detail.** | `_MatchedCondition`; `_emit` | mcp/src/agents_remember/memory/knowledge/detection_walk.py:363-414 |
| **The limitations derived from recorded facts, plus the unconditional one — never a limitation with no omission behind it.** | `_walk_limitations` | mcp/src/agents_remember/memory/knowledge/detection_walk.py:417-441 |
| The unsupported locator read as a declared scope limitation rather than a negative match. | `_has_unread_locator` | mcp/src/agents_remember/memory/knowledge/detection_walk.py:444-457 |
| The omission read from the comparison's own recorded reason, so declaration and omission cannot disagree. | `_declared_probe_omission` | mcp/src/agents_remember/memory/knowledge/detection_walk.py:467-477 |
| **The recorded input set built from the declaration's own discriminator, with the probe read off the union rather than re-run.** | `_recorded_input_set`; `_probe_from` | mcp/src/agents_remember/memory/knowledge/detection_walk.py:480-512 |
| The observed granularity one locator kind supports, and no finer one. | `_granularity` | mcp/src/agents_remember/memory/knowledge/detection_walk.py:515-520 |
| **The unretained manifest reference: a real reference at a destination that is deliberately not the durable route, so it resolves unresolved rather than being fabricated as retained.** | `_unretained_manifest` | mcp/src/agents_remember/memory/knowledge/detection_walk.py:523-542 |
| The comparison the walk reads and the item shape it classifies on. | `KnowledgeDiffResult`; `KnowledgeDiffItem` | mcp/src/agents_remember/models/knowledge/diff.py:501-520; mcp/src/agents_remember/models/knowledge/diff.py:318-340 |
| The declared conditions and declared input sets the walk emits from. | `DETECTION_CONDITIONS`; `DECLARED_INPUT_SETS` | mcp/src/agents_remember/models/knowledge/detection.py:124-149 |
| The record half: the store's own refusals, the write path and the read path this walk's values are handed to. | `record_detection_run`; `build_detection_run` | mcp/src/agents_remember/memory/knowledge/detection.py:263-289; mcp/src/agents_remember/memory/knowledge/detection.py:144-173 |
| **The cases that measure the scenario/control identity, the declared order, the retained group and the unsupported locator.** | "test_a_budget_change_and_a_comments_only_change_produce_the_same_condition_and_signal"; "test_the_declared_order_is_total_over_signal_identity_and_independent_of_item_order"; "test_an_unsupported_locator_is_a_declared_limitation_rather_than_a_negative_match" | mcp/tests/test_knowledge_detection_runs.py:293-324; mcp/tests/test_knowledge_detection_runs.py:339-372; mcp/tests/test_knowledge_detection_runs.py:373-399 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T05:15+02:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): created this one-to-one card for the detection walk. It records the three enforced properties (the walk is structural and reads no source bytes; one place assembles a signal; a group keeps every contributing match), the five conditions and what each is *about*, the identity derived from the recorded group key so a scenario and its harmless control produce the **same** signal identity, the declared total order as `(condition vocabulary index, group key)`, the limitations derived from recorded facts rather than added by habit and why (the signal's own validator refuses both a limitation with no omission and an omission with no limitation), the counterpart probe read off the union's own coverage value rather than re-run, the granularity taken from the recorded locator kind and no finer, and the deliberately unretained manifest reference that resolves unresolved until the durable publication route exists. Verification metadata is the leaf's base commit `4264dcc9`: the code commit does not exist yet and closeout owns that stamp.
