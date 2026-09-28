# mcp/src/agents_remember/models/knowledge/diff.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/diff.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T08:30:00+02:00 |
| lastVerifiedCommitHash | `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` |
| lastVerifiedCommitDate | 2026-09-29T00:17:28+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The whole vocabulary of one baseline-to-candidate comparison: its two sides, its union items, its
declared limits and its expansion.** It holds no SQL, no Git resolution and no authority decision. It
exists as its own module because a comparison is a *different claim* from a read, and the differences
have to be **unrepresentable rather than merely discouraged**.

## Code Commentary

### Logic

`KnowledgeDiffRequest` pairs **one** selector with **two** `KnowledgeDiffSide`s, an optional
`DisplayFilter`, a `KnowledgeDiffBudget` (display only, default 32) and an optional `continuation`.
`KnowledgeDiffResult` is a `page` or a `refused`, never both, and carries the binding, the per-side
counts, the per-side revision groups, the limitations, the omissions, the side absences, the expansion
and the page.

**Four properties are the contract, and each is enforced at model construction:**

1. **Two snapshots, one selector policy, and no field that could carry a second one.**
   `KnowledgeDiffSide.selector` is the only thing this leaf adds to R07's selection contract: an explicit
   selector a side may name **in place of** the request's own seed, which is what makes *"an explicit
   revision selector may address different before/after revision IDs"* a value rather than a special
   case inside the policy. The request has **no field** that could express a computed relevance, a
   ranking or an inferred impact, so the packet's forbidden second relevance rule is not representable
   here. See `memory/knowledge/read.py`'s `SelectionQuery.seed_override` for the one production path
   this field reaches, and §"A closed question" below.
2. **No semantic verdict, by construction.** `KnowledgeDiffSourceChange` carries `claim_id`, the two
   sides' observations, `record_field_changed`, `source_observation_changed`, `source_change_only`,
   `record_change_only` and `missing_side` — and **nothing that could hold a severity, a "strengthens",
   a "harmless" or a neutrality finding**. A source-only change is a changed *source observation* and
   can never read as a changed obligation, because the record's own field changes are a separate,
   separately typed collection (`changed_fields` on the item). The packet's second non-conforming
   example is structurally impossible rather than merely avoided.
3. **Origin is retained on every item.** `KnowledgeDiffItem` carries `before` and `after` payloads with
   their own selection reasons, so a relationship only the baseline reached is inspectable in a
   comparison whose candidate no longer traverses it. `coverage ∈ {selected_both,
   selected_before_only, selected_after_only, present_outside_selection, absent_from_snapshot}` keeps a
   record the other snapshot **holds but did not select** apart from one the snapshot **does not hold**
   — the design's own named misreading ("present-but-outside-the-other-selected-scope is not deletion").
4. **Limits are declared, not implied, and the declaration is checked in both directions.**
   `KnowledgeDiffResult._require_the_limitation_matches_the_omission` refuses a response that omitted
   something for a reason whose limitation it did not declare, **and** one that declared a limitation
   with no omission behind it. `no_semantic_assessment_performed` is unconditional: every comparison
   states it. The undetermined-attribution limit has **two** producers — the display's
   `_attribution_omissions` and the model's own `_attribution_not_measured` — so the validator
   learned the second one, and any later change to the limitation↔omission validator must keep both
   directions.

**The `record_transition` union is six states, and the two that matter most are
`superseding`/`superseded`.** A schema whose revisions are immutable in place makes "the statement
changed" a **pair** of records — the author's successor and the exact revision it names as its
predecessor — so a comparison that knew only `added` and `removed` would render every revised statement
as a deletion plus an unrelated addition. The pair is recognised from the authored predecessor edge
(`invariant_predecessor`, `family_predecessor`), **never** from a label, a display version or an
insertion order.

**Three construction-time invariants a consumer may rely on, plus the partition's own:**

| Model | What it refuses |
| --- | --- |
| `KnowledgeDiffPage` | `has_more == enumeration_complete`, and a `has_more` that disagrees with the presence of a continuation — a truncated comparison cannot be presentable as complete |
| `KnowledgeDiffCounts` | `items_returned + items_remaining != items_total`, and `displayed_total + suppressed_total > items_total` |
| `KnowledgeDiffResult` | being both a page and a refusal or neither; and a declared limitation disagreeing with its omissions in either direction |
| `SourceAttribution` | a repeated path, a bucket total that disagrees with its paths, an unavailable partition carrying a number, and a measured partition whose buckets do not sum — the three buckets are disjoint and exhaustive over the measured population by construction |

**`KnowledgeDiffCounts` keeps the comparison total and the display total apart on purpose.**
`items_total` is the whole comparison and `displayed_total` is this page's view of it, so a filter or a
budget moves the second and never the first, and a filtered response cannot be read as a smaller
comparison.

**The binding is the invalidation, and the digests are derived.** `KnowledgeDiffBinding` carries the
policy version, both declared logical snapshots, both resolved context digests, both side selector
digests and both code tree ids. `diff_binding_digest` is **computed from** the binding rather than
stored beside it, so a caller cannot present a digest that disagrees with the published identity, and a
candidate whose bytes changed presents another `after` identity and is refused rather than continued.

**The comparison has its own cursor decoder.** `continue_diff_from_cursor` is **not** R07's
`continue_from_cursor`: a read cursor positions a page in one selection and a comparison cursor
positions one in a union of two, so presenting either to the other operation is a caller's mistake and
both refuse it by name. `KnowledgeDiffCursor` carries `cursor_format =
"knowledge-diff-cursor/v1"`, the policy, the binding digest, the selector digest, the filter policy and
the position.

**The closed vocabularies.** `DiffItemKind` (five members), `DiffCoverage` (five), `DiffRecordTransition`
(six), `DiffOmissionReason` (**four** — `attribution_not_determined` added for the undetermined
bucket) and `DiffLimitation` (**five** — `unknown_attribution_changed_paths` beside
`unattributed_changed_paths`, two limits and not one: the first says no valid registered attribution
was established for a measured change, the second says that conclusion could not be reached at all)
are literals rather than free text, and
`DiffOmissionReason` is closed on purpose: `assessment_beyond_this_increment` was declared and then
**removed** in fix round 1 (`L8-F6`'s subject) because nothing in the package constructed it and no
limitation advertised it — a reason with no producer would be dead vocabulary the validator could not
check in either direction. `KNOWLEDGE_DIFF_FIELD_NAMES` is the nine compared record fields in declared
order; `selection_reasons` is deliberately absent, because which route of a selection reached a record
is a fact about a traversal and not about the record.

### Conventions

- Every state name is a literal; a caller branches on it, never on message text.
- A `*_change_only` flag is a statement about **which of two objects moved**, not about meaning: nothing
  in this module can label either one with a consequence.
- `DisplayFilter` selects **registered** relationships only (the authored `RealizationRole` a claim was
  recorded with) and refuses a repeated role. It may not select by a computed relevance, a size, a
  recency or an inferred impact, because none of those is a recorded fact.

### Invariants And Boundaries

- **Absence versus selection is structural.** `present_outside_selection` and `absent_from_snapshot` are
  separate members, and `SideAbsence` carries one side's own typed absence **beside** the page rather
  than replacing it — a comparison of two snapshots can legitimately find that one side holds nothing
  for the selector while the other holds records, and neither fact may be lost.
- **A gap is a value, and an undetermined gap is a different value.** `SourceAttribution` is the
  measured change population partitioned once — attributed, confirmed unregistered, undetermined —
  at the declared `changed_path` granularity, with each bound snapshot's inspection state beside it.
  `KnowledgeDiffExpansion` carries that value plus its three path lists, so a path appears in exactly
  one of them and a change nobody looked for is never listed as a change nobody registered. The
  expansion names both trees — never a branch, a working tree or `HEAD` — and carries no source
  text, because this increment reports the *attribution* of source.
- **Boundary.** This module declares shapes. It performs no selection, opens no database, runs no Git
  command, and decides no refusal identity.
- **A closed question, recorded so it is not re-opened.** The reviewer attacked the packet's *"R07's
  policy is the ONLY policy owner"* clause head-on and **could not falsify it**: `seed_override`
  parameterises **which seed** R07's one rule runs on and nothing else, no diff-side code re-derives
  selection, and the override is load-bearing rather than decorative (mutation `R30` — `effective_seed` →
  `self.seed` — kills a named node on an assertion). The owner recorded the acceptance. The alternative
  the packet forbids — a second relevance rule — is not constructible from this request shape.

### Todos

None recorded. One carried gap belongs to the owning seat's ledger rather than to this module: the
increment's own mutation taxonomy records **three covered gaps against this leaf** on the comparison's
lines (`M4`, `M8`, `M27`) and **one non-experiment** (`M23`), each with the input that would close it
named in `memory/knowledge/diff.py`'s card. `L8` carried its contested evidence items to `KS-R09`/`L9`
(ledger entries **A9**/**A10**); none of them is a behavioural defect.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The comparison policy version and the display budget that bounds what a page *shows* and never what the comparison *selected*. | `DIFF_POLICY_VERSION`; `DIFF_DISPLAY_MAX_ITEMS` | mcp/src/agents_remember/models/knowledge/diff.py:105-110 |
| **The closed vocabularies: item kinds, coverage, the six record transitions, the omission reasons and the five limitations.** | `DiffItemKind`; `DiffCoverage`; `DiffRecordTransition`; `DiffOmissionReason`; `DiffLimitation` | mcp/src/agents_remember/models/knowledge/diff.py:117-124; mcp/src/agents_remember/models/knowledge/diff.py:125-139; mcp/src/agents_remember/models/knowledge/diff.py:140-153; mcp/src/agents_remember/models/knowledge/diff.py:154-168; mcp/src/agents_remember/models/knowledge/diff.py:170-182 |
| **The nine compared record fields in declared order, with `selection_reasons` deliberately absent.** | `KNOWLEDGE_DIFF_FIELD_NAMES` | mcp/src/agents_remember/models/knowledge/diff.py:184-194 |
| **One side of a comparison: the exact snapshot and the per-side selector that is the one extension to R07's contract.** | `KnowledgeDiffSide` | mcp/src/agents_remember/models/knowledge/diff.py:197-220 |
| The display-only budget and the registered-role filter that refuses a repeated role. | `KnowledgeDiffBudget`; `DisplayFilter`; `filter_is_empty` | mcp/src/agents_remember/models/knowledge/diff.py:223-231; mcp/src/agents_remember/models/knowledge/diff.py:233-258 |
| The request: one selector, two sides, an optional filter, a budget and a position. | `KnowledgeDiffRequest` | mcp/src/agents_remember/models/knowledge/diff.py:260-269 |
| **The binding every continuation is checked against, and the digest derived from it rather than stored beside it.** | `KnowledgeDiffBinding`; `diff_binding_digest` | mcp/src/agents_remember/models/knowledge/diff.py:271-290; mcp/src/agents_remember/models/knowledge/diff.py:292-301 |
| **The record half versus the source half, with no field that could hold a verdict and a `missing_side` that is a reason rather than a third change statement.** | `KnowledgeDiffSourceChange` | mcp/src/agents_remember/models/knowledge/diff.py:303-331 |
| **One union item: both payloads, its coverage, its transition, its changed fields, the path that reached it and its source comparison.** | `KnowledgeDiffItem` | mcp/src/agents_remember/models/knowledge/diff.py:333-370 |
| The omission value, the per-side absence, and the per-side revision groups kept apart because they can differ. | `OmittedChanges`; `SideAbsence`; `SideRevisionGroups`; `side_revision_groups` | mcp/src/agents_remember/models/knowledge/diff.py:372-384; mcp/src/agents_remember/models/knowledge/diff.py:386-399; mcp/src/agents_remember/models/knowledge/diff.py:401-417 |
| **The one granularity every attribution count is stated at, the three buckets, the four link labels and the three side states.** | `ATTRIBUTION_GRANULARITY`; `AttributionBucket`; `AttributionLink`; `AttributionSideState` | mcp/src/agents_remember/models/knowledge/diff.py:435-435; mcp/src/agents_remember/models/knowledge/diff.py:437-437; mcp/src/agents_remember/models/knowledge/diff.py:444-454; mcp/src/agents_remember/models/knowledge/diff.py:456-456 |
| **One side's contribution and how completely it was inspected — a link count, never a path count.** | `AttributionSide` | mcp/src/agents_remember/models/knowledge/diff.py:459-471 |
| **One measured changed path in exactly one bucket, with the links that put it there and the purported mappings carried beside them.** | `ChangedPathAttribution` | mcp/src/agents_remember/models/knowledge/diff.py:473-507 |
| **The partition value: one population divided once, with the disjoint-plus-exhaustive validator and the three bucket accessors.** | `SourceAttribution` | mcp/src/agents_remember/models/knowledge/diff.py:509-628 |
| **The expansion as a value: both trees and both roots, the reproducing command, the carried partition and its three path lists.** | `KnowledgeDiffExpansion` | mcp/src/agents_remember/models/knowledge/diff.py:630-662 |
| **The counts that keep the comparison total and the display total apart, and refuse their own arithmetic contradiction.** | `KnowledgeDiffCounts` | mcp/src/agents_remember/models/knowledge/diff.py:664-693 |
| The per-snapshot counts carried whole, and the statement that they are counts and not verdicts. | `KnowledgeDiffSummary` | mcp/src/agents_remember/models/knowledge/diff.py:695-705 |
| **The truncated comparison that cannot be presentable as complete.** | `KnowledgeDiffPage` | mcp/src/agents_remember/models/knowledge/diff.py:707-731 |
| **The result that is a page or a refusal, never both, and whose declared limitations are checked against its omissions in both directions.** | `KnowledgeDiffResult` | mcp/src/agents_remember/models/knowledge/diff.py:733-829 |
| **The comparison's own cursor and the two functions that encode and decode it — deliberately not the read's decoder.** | `KnowledgeDiffCursor`; `diff_cursor_for`; `continue_diff_from_cursor` | mcp/src/agents_remember/models/knowledge/diff.py:831-845; mcp/src/agents_remember/models/knowledge/diff.py:847-864; mcp/src/agents_remember/models/knowledge/diff.py:866-887 |
| The canonical spelling of one filter's effect, bound into a continuation. | `filter_policy` | mcp/src/agents_remember/models/knowledge/diff.py:889-892 |
| **The node that measures the absence the request shape cannot carry: nine verdict words searched over the whole serialized response, with a positive control.** | "test_no_field_of_a_comparison_can_carry_a_strengthening_or_harmlessness_verdict" | mcp/tests/test_knowledge_diff_boundaries.py:481-507 |
| **The node that holds the two change statements apart, and the node that measures the limitation validator.** | "test_the_two_change_statements_are_separate_fields_and_neither_implies_the_other"; "test_a_comparison_that_declares_a_limit_it_did_not_establish_fails_construction" | mcp/tests/test_knowledge_diff_boundaries.py:510-540; mcp/tests/test_knowledge_diff_scope.py:577-649 |
| **The node that measures the truncated comparison, whose failing assertion sits at `:716` on the frozen file.** | "test_a_truncated_comparison_cannot_be_presented_as_a_complete_one" | mcp/tests/test_knowledge_diff_scope.py:652-713 |
| The one member this leaf added to the operation union, and the vocabulary the new refusals reuse. | `KnowledgeOperation`; `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:36-147; mcp/src/agents_remember/models/knowledge/result.py:151-222 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every statement runs against values the
caller supplied; no second repository, ledger or coordination path is read.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): No content impact: re-pointed 2 citations into `mcp/tests/test_knowledge_diff_scope.py` through the exact base-to-candidate line map after this leaf's behaviour-preserving splits and catalog/lane/pin repairs; each moved range cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.

- 2026-09-22T08:30:00+02:00 — 260921-ICR-L4 curator (uncommitted change set on `ar/260921-icr-l4`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the vocabulary gained the attribution partition for ICR-R04@v1.** `ATTRIBUTION_GRANULARITY` (`changed_path`), `AttributionBucket` (three), `AttributionLink` (four — the two `outside` members are different facts), `AttributionSideState` (three), `AttributionSide`, `ChangedPathAttribution` and `SourceAttribution` (634 → 892 lines) with the disjoint-plus-exhaustive validator that refuses a repeated path, disagreeing totals, an unavailable partition carrying a number, and buckets that do not sum. `DiffOmissionReason` gained `attribution_not_determined` and `DiffLimitation` gained `unknown_attribution_changed_paths` — two limits, not one — with the model's own `_attribution_not_measured` as the undetermined limit's second producer beside the display's. The "gap is a value" section now states the partition and its three lists; every reference row was re-derived against this candidate. **Stamp accounting:** old verification rows name the last real commit; this leaf's claims were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `KnowledgeOperation` in the row 177 of this card from mcp/src/agents_remember/models/knowledge/result.py:37-75 to mcp/src/agents_remember/models/knowledge/result.py:36, the extent of the construct the claim is about (the checker named line(s) [36, 152, 349] as its live location); re-pointed `KnowledgeRefusalCode` in the row 177 of this card from mcp/src/agents_remember/models/knowledge/result.py:36 to mcp/src/agents_remember/models/knowledge/result.py:80, the extent of the construct the claim is about (the checker named line(s) [80, 151] as its live location)
- 2026-09-17T03:15+02:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): created this one-to-one card for the comparison's vocabulary and reviewed it against the leaf's frozen bytes. It states the four properties enforced at construction — the per-side selector as the **only** extension to R07's contract with **no field able to carry a second relevance rule**; the record half and the source half as separately typed collections with **no field that could hold a verdict**, which is how the packet's second non-conforming example is made unrepresentable; origin retained on every union item and `present_outside_selection` kept apart from `absent_from_snapshot`; and the limitation/omission check that runs **in both directions** — plus the six-state `record_transition` union whose `superseding`/`superseded` pair is recognised **only** from the authored predecessor edge. It records the three construction-time invariants, the comparison's own cursor decoder (deliberately not the read's), the derived binding digest that makes a candidate change invalidate a continuation by construction, and the removal of `assessment_beyond_this_increment` as a reason with no producer. **The closed `seed_override` question is recorded here with the reviewer's evidence** so a successor does not spend a round on it. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
