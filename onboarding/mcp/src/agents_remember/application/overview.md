# mcp/src/agents_remember/application/ - MCP Application Layer Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| lastUpdated | 2026-09-30T20:36:31+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82` |
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| sourceRoute            | `mcp/src/agents_remember/application/`     |
| doc_type               | `route-local-overview`                     |
| governingOverview      | `../../../overview.md`                     |

## 260921-ICR-L44 A Family Member's Sources Carry Their Own Region, Projected By A Dedicated Owner

The family roster read (`review_family_rosters.py`) no longer projects realization claims itself: each
member's claims go through `review_family_sources.member_source`, a focused owner of one claim → one
side-bound `ReviewFamilyMemberSource`. Beside the fields the roster already published, every source now
carries — per side and per claim — the anchor's structured recorded `locator`, the `resolved_ranges` that
side's anchor resolver placed it on in the exact recorded blob, and a `locator_state`
(`resolved` / `whole_file` / `unresolved` / `not_observed`) stated through the model's one rule. Role and
rationale are carried exactly as stored and a claim read without them is refused. Nothing in this route
resolves, searches or re-anchors a range, and no region is ever read from the `detail` sentence: the
ranges are the resolver's (`memory/knowledge/read_anchors.py`). Two members realized in one file therefore
keep two regions, and a side holding other bytes than the claim recorded states `unresolved` with no
range.

| Finding | Anchor | Source |
| --- | --- | --- |
| The one projection of a realization claim into its source reference. | `member_source` | mcp/src/agents_remember/application/review_family_sources.py:27-51 |
| The roster's member composition calling it once per claim. | `member_source` | mcp/src/agents_remember/application/review_family_rosters.py:523-523 |

## Exact sibling retention in curator family successors

The family authoring plane accepts explicit stored-membership references on a successor declaration. The selected rows must belong to declared predecessors of the same family; no roster is inferred. The planner adds successor edges to unchanged invariant revisions through the existing batch writer, binds the retention set and bases into the declaration’s retry content, and checks contradictory retirement only among eligible effects, preserving original refused-entry reasons. Coverage distinguishes retained revisions from added edges and leaves projected counts unmeasured.

| Finding | Anchor | Source |
| --- | --- | --- |
| Validate explicit retained endpoints before composing existing family commands. | `_retained_memberships` | mcp/src/agents_remember/application/curator_family_planning.py:617-664 |
| Measure unchanged siblings separately from added edges. | `_guarantee_outcomes` | mcp/src/agents_remember/application/curator_family_coverage.py:160-229 |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Curator candidate source continuity

Leaf curation captures the exact working source through curator_candidate_source. candidate_progression is the explicit operation that advances only a draft candidate code tree after matching the predecessor receipt and logical dataset under the existing lock. Normal candidate opening remains strict; knowledge, allocation state and the original before half do not move with this operation. Receipt-to-resolution conversion is shared by first-generation establishment and progression.

## Review history and authored invariant scope

Known roster limit: a continuation made only of realization items can complete its read walk while the page-local member projection drops those links. This is a projection concern, not missing published knowledge; the roster owner must preserve continuation-only sources before completeness can support that interpretation.

Closed leaves with no frozen generation read exact recorded memory endpoints through review_recorded_knowledge and label reconstructed history. Frozen reviews retain their own operands. review_unchanged_knowledge prepares a normal code-only comparison through existing candidate/baseline/freeze owners. curator_scope requires explicit applicability, conditions and exclusions and knowledge_curator_ingest binds that meaning into retry identity.

| Finding | Anchor | Source |
| --- | --- | --- |
| `read_recorded_knowledge` owns the behavior described above. | `read_recorded_knowledge` | mcp/src/agents_remember/application/review_recorded_knowledge.py:52-82 |

## Authored realization rationale per target, required at admission

Leaf `260921-ICR-L45` (ICR-R20@v1 repair; developer ruling "require rationale"; Architect rulings
2026-09-28T12:17:09, 16:15:11 and 16:38:58+02:00) changes what the curator writer stores as a
realization claim's explanation. The writer used to fill a missing rationale with the generated sentence
"The statement is realized at <path>." and store it as though authored; most stored realization claims
held only that sentence. Now **no rationale is generated**. Ownership is split across three modules on
this route:

- `curator_realization_authoring` owns the realization a target authors: each hand-off target may carry
  its own `rationale` and `role`, which win over the entry-level `realization_rationale` /
  `realization_role` (an explicit default, not a fallback); the two halves resolve independently, and a
  role stated nowhere is `unclassified`. It also owns the five named admission refusals —
  `realization_value_not_text`, `realization_role_unknown`, `realization_governing_route_absent_literal`,
  `realization_rationale_absent`, `realization_rationale_too_long` — each naming the entry and every
  offending target by position, path and locator.
- `knowledge_curator_ingest` asks those checks in `_resolve_creation`, after the scope check and **before
  `_creation` mints any identity**, so a refused entry writes no journal key and no row while its sibling
  entries commit; `_TargetPlan.citation()` passes the resolved rationale through unchanged; and
  `_content_digest` adds a target's own stated keys only when it states them, so older allocation
  journals still replay.
- `curator_stored_revisions` answers from the candidate's rows which recorded revisions are already
  stored. That one answer marks replays and exempts an **already committed** operation from admission:
  its exact retry replays and can publish exactly as at base (including operations committed before
  targets carried a rationale), while changed content under its key is still `allocation_content_conflict`
  and a recorded-but-uncommitted allocation is still checked.

The hand-off target shape the writer accepts is `{path, locator, governing_route?, rationale, role?}`
(see `skills/l-01-agent-lifecycles/templates/curator-handoff-list.md`); a missing route is spelled by
omitting the key, never by the word `absent`. Stored claims holding the old generated sentence are never
rewritten; replacing them needs authored successors. This supersedes the earlier statement on this route
that the ingest introduced "no new required producer input".

| Finding | Anchor | Source |
| --- | --- | --- |
| Per-target resolution and the ordered admission checks. | `EntryRealization`; `realization_refusal` | mcp/src/agents_remember/application/curator_realization_authoring.py:134-174; mcp/src/agents_remember/application/curator_realization_authoring.py:249-280 |
| The admission call before minting, with the committed-allocation exemption. | `_resolve_creation` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:2221-2253 |
| The citation carries the resolved rationale with no generated fallback. | `_TargetPlan` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:588-646 |
| The committed set read from the candidate's own rows. | `committed_revisions`; `stored_revisions` | mcp/src/agents_remember/application/curator_stored_revisions.py:22-32; mcp/src/agents_remember/application/curator_stored_revisions.py:35-41 |

## Comparison-bound attributed unchanged source content

The review's source-content read now opens two populations, and the decision is split across three
owners. `review_source_content` reads bytes at the two requested trees and assembles the expansion;
`review_source_admission` decides whether the path is admitted — a changed path of a measured change
set, or an unchanged path of a **measured** pair that a realization recorded in that comparison's own
knowledge is anchored at — and every other path is refused by name; `review_source_realization_link`
answers the link question with the knowledge read owner's exact claim-at-path query against the
comparison's own snapshots (the resolution's halves for the current pair, the retained halves of a
generation that recorded exactly a superseded pair, nothing otherwise). Attributed context is typed
`admission="attributed_unchanged"` with status `unchanged`, never enters the inventory or its counts,
and requires the exact spelling a recorded anchor carries. Unreadable knowledge makes the link
undetermined rather than absent. A stale anchor still admits; unmeasured and unfrozen superseded pairs
admit nothing (Architect rulings closing L43-R1-F4). Changed-path answers are unchanged from before.
**Extended by MIK-L31:** a tree comparison's proof entry anchored at the path links it too (`_proof_at_path` over
the derived index's `ix_entry`; ruling 2026-09-30T05:36:19 Q1, so a proof's focused card opens its test file in
full), and the admission sentence says "a realization or proof recorded for the path"; a dataset records no proofs
and admits exactly as before. An undetermined link over knowledge that was never created asks to **initialize** it
rather than restore or repair a snapshot (MIK-R31 rule 6, ICR-L43 review R2 O1).

| Finding | Anchor | Source |
| --- | --- | --- |
| The admission order and the three refusals; since MIK-L31 a proof link admits and the undetermined remedy names the cause. | `admit_source_path`; `_attributed_or_refused` | mcp/src/agents_remember/application/review_source_admission.py:86-128; mcp/src/agents_remember/application/review_source_admission.py:131-159 |
| The comparison binding and the exact per-half link query. | `_bound_knowledge`; `_side_reading` | mcp/src/agents_remember/application/review_source_realization_link.py:186-246; mcp/src/agents_remember/application/review_source_realization_link.py:266-295 |
| The content read hands the inventory to the admission owner before reading any byte. | `_content` | mcp/src/agents_remember/application/review_source_content.py:241-285 |

## 260921-ICR-L34 The Review's Comparison Gets A Producer, And The Namespace Comes From The Record Beside The Bytes

`260921-ICR-L34` (D62) is the leaf that made a leaf's review comparison **producible at all**, and it
settled two defects that stood in the way. What belongs at this route's altitude is the producer's
reach and the one rule that changed on this route.

**The freeze owner now has a shipped caller, and it is the CLI's, not a route's.**
`application/review_comparison_freeze.freeze_review_comparison` was a complete, measured production
operation with no caller outside the test suite, so no leaf could publish a generation and every
closed leaf's review reopened from `history:recorded-source-range` while the reviewer's whole knowledge
column rendered its empty state. The caller this leaf adds is
`agents-remember review-record-comparison`
([`cli/review_comparison_record.py`](../cli/review_comparison_record.py.md)): it resolves the contract's
own task context, composes through the surface's own resolution and composition, names the leaf's
standing generation as the successor's predecessor, and publishes only what that composition bound. Ordinary capture runs through the CLI while the leaf enclosure is live. Explicit L41 recovery also uses that CLI, naming the retained parent generation and original curator digest; it does not create a live candidate. The L11
section below records the boundary this supersedes; it is corrected in place there.

**The L34 boundaries and their later repair.** Ordinary capture still requires `resolved.candidate_identity`. L41 adds explicitly named retained-parent recovery through the retention owner, while a closed resolution continues to carry no live candidate identity. The other L34 defect concerned the namespace: the
namespace of a dataset was read from `candidate-receipt.json` **alone**, which a *candidate* half has
(the admission wrote it) and a **before** half placed by a run handed a published `--baseline` never
does — a published dataset is not an admitted candidate, and it carries `baseline-generation.json`
instead. The read therefore fell back to the requested repository name while the bytes were bound to a
namespace id, the storage owner refused the mismatch, and the freeze answered `candidate_dataset_absent`
— so **every leaf on the ordinary `knowledge-ingest --baseline` continuity route produced a comparison
that could not be frozen**, invisibly, because the seven fixture modules that pass hand-assembled pairs
exercise the *no-record* shape and the first-generation path leaves a receipt beside the empty half it
creates. `review_candidate_resolution.review_namespace` now reads **the record beside the bytes** — the
receipt when there is one, otherwise the before half's own generation record — and falls back to the
requested repository only when **neither** exists.

**One consequence for a reader of this route.** `/api/review/intent` and
`/api/review/intent/entries` now answer for a leaf of this master with a recorded comparison instead of
refusing `candidate_dataset_absent`, and the mounted reviewer renders the family plane — families, joint
guarantees, member statements, linked expressions and evidence — from the record rather than from an
empty sheet. Nothing in this route's *read* half changed to achieve that: the resolution, the
composition and the subject catalogue are the shipped owners, and the leaf that made the difference is
the one that gave their producer a caller and made a placed baseline openable.

**The generation-versus-range fork, measured across three leaves (the *three-leaf contrast*).** The
closed-leaf resolution's two answers are not a code-reading: `resolve_review_candidate` resolves
**L30** and **L28** — both closed, L28 with its whole worktree group absent, so
`contract.code_worktree.exists()` is `False` — through the closed-leaf branch, and both answer
`closed_leaf: recorded-source-range`, because neither published a generation; **L34**, which has,
answers `closed_leaf: recorded-comparison`. Measured by this leaf's adversarial verifier from the
out-of-checkout install and re-run independently by the orchestrator; the contrast is what makes
"a published record wins over the recorded range" an observation rather than an inference, and it holds
**either side of `worktree_cleanup`**, because cleanup removes the worktree group and not
`tasks/<repository>/<master>/enclosures/`.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The producer: the freeze's own production entry, and the caller this leaf gave it.** | `freeze_review_comparison`; `run` | mcp/src/agents_remember/application/review_comparison_freeze.py:239-258; mcp/src/agents_remember/cli/review_comparison_record.py:162-202 |
| **The record-beside-the-bytes namespace: the candidate's receipt when there is one, otherwise the before half's own generation record, otherwise (since MIK-R25) a derived knowledge index's own namespace, and the requested repository only when none of these answers.** | `review_namespace`; `read_baseline_generation`; `CANDIDATE_RECEIPT_NAME` | mcp/src/agents_remember/application/review_candidate_resolution.py:391-430; mcp/src/agents_remember/application/knowledge_baseline_generation.py:285-316; mcp/src/agents_remember/models/knowledge/snapshot.py:53-53 |
| Ordinary publication requires a live capture; explicit recovery revalidates the named retained parent capture without inventing a live identity. | `_unresolved_capture`; `_retained_capture` | mcp/src/agents_remember/application/review_comparison_retention.py:173-220; mcp/src/agents_remember/application/review_comparison_retention.py:223-275 |
| The case that measures the corrected rule on the real placed-baseline journey, and bites when it is reverted. | `test_the_placed_baseline_is_opened_under_its_own_recorded_namespace` | mcp/tests/test_knowledge_ingest_comparison_generation.py:329-370 |
| The closed-leaf resolution the record now feeds: the generation path first, the recorded source range only when no generation exists. | `resolve_committed_leaf_review`; `HISTORY_RECORDED_COMPARISON`; `HISTORY_RECORDED_SOURCE_RANGE` | mcp/src/agents_remember/application/review_committed_leaf.py:174-216; mcp/src/agents_remember/application/review_committed_leaf.py:88-88; mcp/src/agents_remember/application/review_committed_leaf.py:89-89 |

## 260921-ICR-L32 The Family Plane Is Read After The Candidate Is Admitted, And Two Owners Gain A Sibling

**The ordering defect that made an ordinary route unusable is fixed (D57).** In
`application/knowledge_curator_ingest.py`, `read_curator_planes(raw, paths.candidate, …)` read the family
plane **before** `_admitted_candidate(…, baseline=…)` created the candidate from the published baseline, so
the **first** ordinary `knowledge-ingest --contract` run of a baseline-forked leaf refused a membership naming
a family revision that its own baseline stores (`family_revision_not_stored`). The plane is now read against
the admitted candidate, with a fork-point fallback, so the ordinary **planning** run stops refusing while
still writing nothing by contract, and the committing run carries the membership through. The mutation proof
is the ordering itself: restore the premature read and both arms refuse again. `curator_ingest_planes.py`
carries the guard for that new read, including the typed `selected_input_unavailable` refusal for an
unreadable fork point rather than a traceback.

**The write plane's reachable entry points are named as two (D55).** `application/knowledge_ingest.py`'s module
docstring now says the seam it provided is **one of the two** routes the write plane is reachable from today,
the other being the taskless repository-foundation route — completed, not deleted.

**The family-authoring owner gains a test-side sibling (D54).** `mcp/tests/test_curator_family_authoring.py`
is split into 818 lines plus a 578-line purpose-named module, which is where the tests for
`curator_family_authoring.py` and `curator_ingest_planes.py` now live; nothing these owners do changed.

## Update History
- 2026-09-30T20:36:31+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): **The L32 review F5 carry is resolved** (ruling 2026-09-30T13:07:38): MIK-L34 marks every owner hunk a lane window draws, from `review_unexplained_lane.py`'s per-file response unchanged. The L32 section's F5 and Q5 clauses now say so (L34 kept the membership mapping). No application module changed; `hunkMarkers.ts` restates `_membership` and `_occurrences`' unknown-membership rule in its reason sentence and names this module as the rule's owner (review R1 N1).
- 2026-09-30T14:18:54+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): **route body updated.** Added the section "260928-MIK-L32 The Unexplained-Changes Lane: One Classification Of Changed Files And Hunks, Shared With The Gate" after L14's: the two new modules (linked cards), the four touched modules, every ruling (PS-1 already fixed by L31; 12:19:20 Q1-Q7 with Q2 carried to L37; 13:07:38 F1-F4 fixed, F5 carried to L34, F6 accepted; R2 pass; the L35 word-diff rerun on the synced tree), the five candidate invariants and seven rows. **Reopened claim reworded and re-anchored:** L31's cards-view row named `_entries_view`, which MIK-L32 replaced with `_focused`; it now names the focused call on a line-exact quote and is re-measured (`126-127; 233-240; 131-152`). The other moved rows were re-pointed by the installed fixer (its bullets kept) or by the exact base-to-staged shift. No verification stamp was advanced.
- 2026-09-30T12:07:20+00:00: Generated citation repair: "hunk.new_count > 0" repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:560-560. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T12:07:20+00:00: Generated citation repair: `_row_subjects` repointed to mcp/src/agents_remember/application/review_tree_knowledge.py:552-558. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T12:56:40+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db` plus the staged delta; first curated over `b54d1b03`, then merged with L29's landed curation after the sync onto code `ce459423` / memory `a6075c76`, L29's committed lines kept byte-identical): **route body updated for MIK-R14.** A new section after L31's, "260928-MIK-L14 Reconsideration Surfacing: A Changed Ground Reopens A Rejected Alternative": the three new modules (the worklist registrant, the writer's rows and refresh with its link states, the task-document question), the touched worklist and writer modules, every ruling from 01:45:56 to 11:53:13, the six candidate invariants and inertness; seven rows. L13's section now notes that its Q5/Q6 carry is met by L14. The rows the installed fixer declined were re-pointed by the exact line shift of this leaf's diff; the fixer projected or normalised the rest, and its generated bullets are kept. No verification stamp was advanced. **After the sync:** L29's section and this leaf's are both kept, this leaf's after L29's; L29's rows are kept as landed.
- 2026-09-30T12:15:39+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`; review R3 and post-sync pass-with-notes, R3-1 and R3-2 fixed): **route body updated for MIK-R29.** Added the section "260928-MIK-L29 The Path-Based Knowledge Reader" after L31's: the new `knowledge_reader/` sub-package and its eight cards (no sub-route overview, following the `knowledge_leaf/`, `knowledge_paging/` and `knowledge_worklist/` precedent), the reused read paths, every ruling, and the five candidate invariants, with four rows. The intake-flagged `review_source_content` port row was re-pointed by the exact base-to-staged line shift. No verification stamp was advanced: the change set is staged and uncommitted, and closeout owns the stamp.
- 2026-09-30T10:06:00+00:00: Generated citation repair: "a change elsewhere in the same file raises nothing" repointed to mcp/src/agents_remember/application/knowledge_worklist/__init__.py:26-26. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T10:06:00+00:00: Generated citation repair: `_relocate` repointed to mcp/src/agents_remember/application/knowledge_writer/authoring.py:1069-1080. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T10:06:00+00:00: Generated citation repair: "hunk.new_count > 0" repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:558-558. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): **route body updated for MIK-R31.** Added the section "260928-MIK-L31 Focused Expression Cards: Every Location Of The Selected Family, From The Pinned Trees" after L05's: the new `review_tree_entries.py` (carded), the cards read, pinning, snake_case and `facts.row` in `review_tree_knowledge.py`, the proof link and initialize remedy, the Q8 fix, every ruling (the carried L11, L25 Q2/F9/Q8, L10 and PS-1; 05:36:19 Q1-Q4; 06:10:21 R1; 06:47:03 R2; 09:38:03 R3 with R3-N1), and five candidate invariants. The attributed-unchanged section records the L31 extension, and two rows (the admission row, L25's tree-view row) are reworded. Six rows added.
- 2026-09-30T05:58:11+02:00 — 260928-MIK-L05 curator (uncommitted change set on `ar/260928-mik-l05`, code base `31d761a241055d67b85ef3908033856b78a86a57` plus the staged and unstaged delta): **route body updated for MIK-R05.** Added the section "260928-MIK-L05 Route-Chain Family Retrieval" at the end, after L10's: the new `knowledge_leaf/chain.py` (carded and governed here), the six touched modules, the rulings of 2026-09-30 03:32:18, 04:12:49 and 04:45:22, four candidate invariants and six rows. L01's Q6 bullet now says MIK-R05 resolved it. **Reopened claims reworded:** L01's `select_leaf`/`_order`, `prepare_leaf`/`_page` and `_leaf_response`/`_refused` rows; the last was re-measured by hand (`577-633; 646-660`), dropping a third range that pointed into the new `_revision_absent`.
- 2026-09-30T03:49:26+00:00: Generated citation repair: `PUBLISHED_DATASET_NAME` repointed to mcp/src/agents_remember/application/published_intent.py:177-177. No content impact: mechanical anchor-range projection bound to citation source snapshot 778874e9f7067e0c11ceadc4ef5d81e0b76e5e12eb31479c7b3ae9bc268513ab; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T03:49:26+00:00: Generated citation repair: "from agents_remember.models.read_files import FileReadStatus" repointed to mcp/src/agents_remember/application/read_files.py:73-73. No content impact: mechanical anchor-range projection bound to citation source snapshot 778874e9f7067e0c11ceadc4ef5d81e0b76e5e12eb31479c7b3ae9bc268513ab; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): **route body updated for MIK-R10.** Added the section "260928-MIK-L10 Unexplained Change Disposition: Every Unlinked Change Needs An Authored Answer" after L25's (the new, carded `knowledge_worklist/unexplained.py`; the coverage lookup; the answers; delete-only hunks; the leaf route's settling; the writer's row and refusal; rulings 01:56:39 Q1–Q4 and 03:24:28 N1–N3; the L31/L32 carry; the four candidate invariants), seven rows. The entry is in the first list. No verification stamp was advanced.
- 2026-09-30T02:31:31+00:00: Generated citation repair: `_without_proof` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:762-773. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:31:31+00:00: Generated citation repair: "a change elsewhere in the same file raises nothing" repointed to mcp/src/agents_remember/application/knowledge_worklist/__init__.py:24-24. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:31:31+00:00: Generated citation repair: `reconcile_planned_effects`; `plannedEffects` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:239-239; mcp/src/agents_remember/application/knowledge_worklist/compute.py:266-266. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:31:31+00:00: Generated citation repair: `_relocate` repointed to mcp/src/agents_remember/application/knowledge_writer/authoring.py:897-908. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T04:01:40+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): **route body updated for MIK-R25.** Added the section "260928-MIK-L25 The Reviewer On Git Trees: Four Trees, Pins, The Tree View, And The Archive Hook" after L13's: the four new modules (carded, governed here), the three touched review modules and the binding, every ruling (22:22:37 Q1–Q8; 23:15:34 F1–F9; 00:08:39; 01:00:07; 01:37:42; 02:12:06; 02:32:42) and the five candidate invariants, with six rows. **Reopened claims re-read:** the two `review_namespace` rows now name the derived-index fallback, and the pre-publication recheck row names the memory-candidate recheck. The other rows were projected or normalised by the installed fixer, or re-pointed by exact line shift. No verification stamp was advanced.
- 2026-09-30T03:13:03+02:00 — 260928-MIK-L13 curator (uncommitted change set on `ar/260928-mik-l13`, code base `3772cdcd008fcacdc5a86e264a3ef63e879ea544` plus the staged delta): **route body updated.** Added the section "260928-MIK-L13 Decision Records: The Writer Reports Requirement Endpoints" after L01's: the new `requirement_links.py`, the writer's `coordination_root` and the report's `requirementEndpoints` (review F3), the rulings, and the five candidate invariants. Three rows. No verification stamp was advanced.
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): **route body updated.** Added the section "260928-MIK-L01 The Family-Complete Leaf Read: One Path, Its Whole Family Neighbourhood" after L06's: the new `knowledge_leaf/` package (four new cards governed here), the touched `published_intent`, `knowledge_paging` and `knowledge_projection` modules, the five carried obligations, every ruling of 2026-09-29T23:21:57 and 2026-09-30T00:08:39, the five candidate invariants, and eight rows. **Reopened claim re-read and reworded:** L02's `bounded_block`/`_tail` row now says the tail collapses per seed kind. L02's package-map row was re-measured (`1-27` → `1-30`). The other rows were projected or normalised by the installed fixer, or re-pointed by exact line shift.
- 2026-09-29T23:56:29+00:00: Generated citation repair: `PUBLISHED_DATASET_NAME` repointed to mcp/src/agents_remember/application/published_intent.py:170-170. No content impact: mechanical anchor-range projection bound to citation source snapshot af78c18a536ac2f00d794dbac67f4d678cae173b43b31e0e7de2b8d520b727b6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T23:56:29+00:00: Generated citation repair: `_bind_index_state` repointed to mcp/src/agents_remember/application/published_intent.py:571-585. No content impact: mechanical anchor-range projection bound to citation source snapshot af78c18a536ac2f00d794dbac67f4d678cae173b43b31e0e7de2b8d520b727b6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:22:26+02:00 — 260928-MIK-L06 curator (uncommitted change set on `ar/260928-mik-l06`, code base `c493b55731545a090d6b81f504bf02e1e427ec74` plus the staged delta): **route body updated for MIK-R06.** Added the section "260928-MIK-L06 Family Route Maintenance: The Route Conditions In The Worklist, And A Moved Row That Relocates" after L11's (the new `knowledge_worklist/route_conditions.py`, step 6 and `Item.extra` in `compute.py`, the `_Run.document` split, the exported predicate, the writer's cover `path` and moved-row relocation), with the carried L04 decision, every architect ruling of 21:49:19 (Q1–Q7), 22:40:22 (F1, N1, N2, N6, N7) and 23:14:41, and the five candidate invariants. The L11 step-5 row into `compute.py` was re-measured by hand (`243-272` → `228-244`). No verification stamp was advanced.
- 2026-09-29T23:15:40+00:00: Generated citation repair: "a change elsewhere in the same file raises nothing" repointed to mcp/src/agents_remember/application/knowledge_worklist/__init__.py:22-22. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c718f054d6f4666aac0289d7878fea56fae3168ee18c9058b74578d7e9f7b0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): **route body updated for MIK-R11.** Added the section "260928-MIK-L11 Planned Invariant Effects Reconciliation: Declared Effects Against Delivered Rows" after L02's (the new `knowledge_worklist/planned_effects.py`, the worklist step, the fail-closed declaration read, the planned row through the writer, `set_field`), with every architect ruling of 2026-09-29T21:56:18 (Q1–Q5) and 22:35:34 (F1–F7) and the five candidate invariants. Rows citing the touched modules were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T19:58:00+00:00: Generated citation repair: `PUBLISHED_DATASET_NAME` repointed to mcp/src/agents_remember/application/published_intent.py:160-160. No content impact: mechanical anchor-range projection bound to citation source snapshot 1e041d3cc3624746d949d3346f148082cba5203cab5cbced9c44716f89831a84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T19:58:00+00:00: Generated citation repair: `_absence_refusal` repointed to mcp/src/agents_remember/application/knowledge_read.py:404-436. No content impact: mechanical anchor-range projection bound to citation source snapshot 1e041d3cc3624746d949d3346f148082cba5203cab5cbced9c44716f89831a84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): **route body updated for MIK-R02.** New section "260928-MIK-L02 Bounded Continuation Accepted By The Mounted Read: The Paging Package", after L30's: the new `knowledge_paging/` package (nine modules, each carded and governed by this overview; no sub-overview, following the `knowledge_worklist/` and `knowledge_currentness/` precedent), the four touched modules, every architect ruling (the carried L23 ruling; 19:56:40 Q1–Q7; 20:40:40; 21:32:34) and the five candidate invariants, not ingested. Seven rows. L03's published-intent row now cites `_tree_block`, which carries the `treeScope` since MIK-R02. **Reopened claim re-read and reworded:** the knowledge-read seam's entry-point row now says `select_knowledge_scope` was added beside the three; the one generated-repair bullet this pass's fixer wrote for it (`read_row_counts`) was removed. No verification stamp was advanced.
- 2026-09-29T19:00:20+00:00: Generated citation repair: `_without_proof` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:736-747. No content impact: mechanical anchor-range projection bound to citation source snapshot f243d6cd7f6b1214330608a0b5e372fb521b8035680e9d41a0f33ceb9d8057ab; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): **route body updated for MIK-R30.** New section "260928-MIK-L30 The Onboarding Trace Kind, Its Sides, And The Two Enforcement Points", after L03's: the new `knowledge_worklist/onboarding_trace.py` (carded, governed by this overview; no `knowledge_worklist/overview.md` was created, following the L08 and L03 precedent), the five touched modules, and every architect ruling (18:49:50, 19:23:45, 19:53:54). Five rows. Rows citing moved lines were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T18:08:42+00:00: Generated citation repair: `PUBLISHED_DATASET_NAME` repointed to mcp/src/agents_remember/application/published_intent.py:147-147. No content impact: mechanical anchor-range projection bound to citation source snapshot 704ba74355bb1716854facdd857416a0cc403be7304c687768829065b4665abc; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T19:59:41+02:00 — 260928-MIK-L03 curator (uncommitted change set on `ar/260928-mik-l03`, code base `e40c314ca55305f7e4334b4e8e16a10297f6f175` plus the working-tree delta and untracked files): **route body updated for MIK-R03.** Added the section "260928-MIK-L03 Stale Invariants Flagged At Read Time: The Currentness Package": the new `knowledge_currentness/` package (four cards, governed by this overview; no sub-overview, following the `knowledge_worklist/` precedent) and the published-intent block's `currentness`, with the architect rulings of 18:42:37 and 19:13:41 and the carried L28 stale-proof ruling. Five rows.
- 2026-09-29T15:42:43+00:00: Generated citation repair: `_without_proof` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:695-706. No content impact: mechanical anchor-range projection bound to citation source snapshot e0edc40115a57d64eee749407e3bb64382ff6c5a6884c16ce3f8938fb89031a7; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): **route body updated for MIK-R08.** Added the section "260928-MIK-L08 The Change-To-Knowledge Worklist Package, And The Writer's Carry": the nine-module `knowledge_worklist/` package (each module carded, governed by this overview; no sub-route overview was created, following the `knowledge_writer/` precedent), the writer's `carry.py`, the controller's recompute, the `LeafWorklistRecompute` binding and the settable `knowledgeMaintenanceScope`, with architect rulings 1, 2 and 5 and the review R1 rulings.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): **Route body update (MIK-R28).** New section: the new `knowledge_proofs.py` card and the three touched modules (`knowledge_writer/handoff`, `knowledge_writer/authoring`, the quality controller), with the architect rulings (the `path -k name` form; the "without proof" list is checklist-only and informational; rule 3 and the stale-proof clause move to L08/L03) and four rows. Rows citing the touched files elsewhere in this overview were re-pointed by the installed `memory-citations --fix`, with no wording change.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): **Route body update (MIK-R24).** New section: the new `read_files_format.py` card and the five touched modules (`read_files`, `memory_tools`, the quality controller, `worktree_services`, `code_anchors`), with the two architect rulings (legacy-format reads active; refusals inert) and four rows. The reopened ICR-L19 mounted-route row now names the renamed legacy-format case, and its models citation was re-measured (`80-80`). The other flagged rows were re-pointed by the exact line map, with no wording change.
- 2026-09-29T12:03:40+00:00: Generated citation repair: "from agents_remember.models.read_files import FileReadStatus" repointed to mcp/src/agents_remember/application/read_files.py:68-68. No content impact: mechanical anchor-range projection bound to citation source snapshot 75677f16e5ed8ed01a37a3496ecf058f05e2f85f804720849cd36afc05309a98; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): **route body updated — new section "260928-MIK-L12 The Curator Writer For All Knowledge Kinds, As Files"** for the new `knowledge_writer/` subpackage (8 new cards, governed by this overview) and the ruling that the database ingest and bootstrap modules on this route are unchanged until L26. No verification stamp was advanced.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): **route body updated.** Added the section "260928-MIK-L23 The Published-Memory Selection Selects A Converted Tree". The reopened `published_intent_block`/`read_published_intent` row of the `260921-ICR-L19` section was re-read against the working tree: the functions still resolve the publication, seed it and read one bounded page per path, so its wording is retained; its ranges and the other rows the +160-line delta moved were re-pointed by exact base-to-working line mapping. No verification stamp was advanced.
- 2026-09-29T05:52:51+00:00: Generated citation repair: `PUBLISHED_DATASET_NAME` repointed to mcp/src/agents_remember/application/published_intent.py:140-140. No content impact: mechanical anchor-range projection bound to citation source snapshot 08ce78606da3cc2a7c0249e0af5ee18d9cd313bdb4222c759c5a89e3e75efdf0; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): No content impact: re-pointed 8 citations into `mcp/src/agents_remember/memory/knowledge/evidence_records.py`, `mcp/tests/test_knowledge_review_source_endpoints.py`, `mcp/tests/test_knowledge_review_surface.py` through the exact base-to-candidate line map after this leaf's behaviour-preserving splits and catalog/lane/pin repairs; each moved range cites the same line content it cited at the landed base; the ranges whose cited case or codec moved verbatim now cite `mcp/tests/test_knowledge_review_resolution_and_route.py`. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T18:18:00+02:00 — 260921-ICR-L47 curator (post-sync re-measure after the Architect's `worktree_sync` onto code `eda947325ccbe0791973953265278597e968a34a` / memory `6ccb9b615e383174c22f110a6492e6231a4e261f`; L47 candidate tree `5f22717e68041d6819e9671cee2ab30e4d3d3e13`): No content impact: citation ranges into files L44, L45 or L47 moved (`mcp/src/agents_remember/application/knowledge_before_half.py`, `mcp/src/agents_remember/application/knowledge_diff.py`, `mcp/src/agents_remember/application/knowledge_review.py`) were re-measured against the post-sync code; each re-pointed row held its anchors in its own measurement tree (`eda94732` or the pre-sync L47 candidate `72efa4bb`) and holds them after the line mapping, or names a literal that occurs exactly once in the post-sync file within five lines of its cited place. Claim wording unchanged. No stamp advanced.
- 2026-09-28T17:15:46+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): body update — new section *Authored realization rationale per target, required at admission* for the two new modules (`curator_realization_authoring`, `curator_stored_revisions`) and the ingest's admission change; the KS-L43 sentence "no new required producer input" is qualified as superseded. The `_with_replays` claim was re-read (it now calls `curator_stored_revisions.stored_revisions`; wording still holds). All other ranges re-pointed through the exact base-to-candidate line map. No stamp advanced.

- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): added the route section for the new member-source owner `review_family_sources.py`, which the roster read now calls per claim and which carries each source's per-side locator, resolved ranges and locator state. Route meaning changed: projection moved to a dedicated owner; no read policy changed.

- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): **the source-content route gained two owners and one admitted population.** Added the section *Comparison-bound attributed unchanged source content* (the three-owner split, comparison binding, exact spelling, undetermined link, and the Architect's four scope rulings), qualified the L3 section's "a path in neither is refused" seam as extended, and re-pointed its seven rows whose constructs moved into `review_source_admission.py` or shifted up in `review_source_content.py`. File-level detail stays on the three module cards. No stamp advanced; closeout owns it.

- 2026-09-27T05:43:38+00:00 — Curator-authored re-citation of 1 investigated L41 source-linked claim(s). Each named registration or declaration was selected individually after the composite guarded projection declined. Prior explanation, refusal evidence, generated history and real verification stamps are preserved.

- 2026-09-27T05:30:43+00:00 — Authored scoped citation maintenance for 9 L41 source-range projection(s) resolved by the frozen source index. Only changed-source ranges were adopted from the preview; unrelated ranges, generated history and verification stamps are preserved.

- 2026-09-27T05:25:19+00:00 — Reconciled the L41 moved record/path owners and explicit retained-parent recovery boundary with current source. Prior generated history and real verification stamps are preserved.

- 2026-09-27T05:23:46+00:00 — Re-resolved 4 source-linked citation claim(s) against the extracted or shifted L41 owners. Each selected symbol uses its current declaration extent; other source references and prior generated history remain unchanged. Verification stamps remain closeout-owned.

- 2026-09-27T05:02:28+00:00 — Reconciled this route's durable assessment-history ownership and failure boundaries. Existing source/knowledge/evidence owners and authored judgment meaning are preserved; verification stamps remain closeout-owned.

- 2026-09-27T00:59:43+00:00 — Updated the family-read route account for exact sparse member updates. The existing membership and bounded read owners remain authoritative; no route, schema or selection policy changed.

- 2026-09-27T00:16:25Z — L39 W2: Reconciled family conflict eligibility at the existing parser boundary; no new owner or authority. Prior source and review history remain attributable.


- 2026-09-26T23:48:33Z — L39: Extended the existing authored-family application boundary with exact sibling-retention references and reporting. No new store, schema or writer owner; verification metadata remains closeout-owned.

- 2026-09-26T21:21:39Z — Recorded the bounded family-roster continuation concern for the owning route.
- 2026-09-26T21:14:33+00:00: Generated citation repair: `test_a_task_context_review_lists_the_complete_source_inventory_with_no_knowledge_at_all`; `test_the_production_inventory_keeps_an_unusual_filename_as_the_address_it_expands_by`; `test_a_non_utf8_pathname_leaves_the_review_openable_and_states_why_it_is_partial` repointed to mcp/tests/test_knowledge_review_source_endpoints.py:842-918; mcp/tests/test_knowledge_review_source_endpoints.py:921-962; mcp/tests/test_knowledge_review_source_endpoints.py:1011-1068. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T20:13:29Z — Recorded the exact-source capture and controlled candidate code-progression owners.
- 2026-09-26T19:49:05Z — Reconciled current route ownership and retained existing source and history boundaries.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `_identity` repointed to mcp/src/agents_remember/application/knowledge_curator_ingest.py:3518-3554. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `_identity` repointed to mcp/src/agents_remember/application/knowledge_curator_ingest.py:3518-3554. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:30:00+02:00 — 260921-ICR-L34 curator (leaf `260921-ICR-L34`, uncommitted change set on `ar/260921-icr-l34-ar`, code base `a9a1a41bba535803421470bd17d858657177cb5f` plus the working-tree delta): **route body updated — the review's comparison gets a producer and the namespace comes from the record beside the bytes.** The new section records the freeze's first shipped caller (the CLI's `review-record-comparison`, deliberately not a route, a pane or a closeout path, because the retention owner requires a captured candidate identity and both closed-leaf resolutions pass `None`), the two defects that stood in the way (the live-capture precondition; the receipt-only namespace rule that made the before half of every `knowledge-ingest --baseline` run unopenable and therefore every such leaf's comparison unfreezable), the corrected rule, and the measured **three-leaf contrast** that supports the generation-over-range fork across two closed leaves and this one. The L11 route boundary ("not wired to any route or read path … its consumer is a later leaf") and the L21 "realises the wiring" sentence are corrected in place, and the L22 namespace paragraph and two reference rows are corrected with dated blocks. **Citation accounting:** every range into `review_candidate_resolution.py` that this leaf's import block and rewritten function moved was re-derived against this candidate rather than shifted (`327-345`→`330-348`, `348-373`→`351-399`, `385-400`→`402-417`, `403-416`→`420-433`, `436-450`→`453-467`). No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **route body updated — the family plane is read after candidate admission.** The new section records the D57 ordering repair and its mutation proof, the guard on the new read (a typed `selected_input_unavailable` for an unreadable fork point), the two-name correction in `application/knowledge_ingest.py`'s docstring, and the test-side sibling that now owns the family-authoring cases. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.

## 260921-ICR-L28 The Curator's Family Plane And External-Source Plane Are Five Purpose-Named Owners

`260921-ICR-L28` (`ICR-R28@v2`, grounded family and invariant foundation) turns `ICR-R28`'s two
authored planes into five owners in this route, each answering one question and none restating another's
vocabulary. The obligations are the packet's: author a family identity, its **independent**
joint-guarantee revision and memberships linking **exact** family and invariant revisions where the
evidence justifies a joint obligation; keep a *deliberate* no-family outcome with its basis; never
report an **unexamined** entry as a family-free one; and retain an external source through
`Authorship.origin_refs` and a bounded manifest rather than through a fabricated Git anchor.

| Owner | What it answers | Size |
| --- | --- | --- |
| `curator_family_authoring.py` | What the hand-off list **declared**: the guarantees, memberships, retirements and no-family outcomes, and which of them are incoherent | 539 L |
| `curator_family_planning.py` | What those declarations **resolve to** against the candidate: allocated identity pairs, exact endpoints, and the four shipped commands | 766 L |
| `curator_family_coverage.py` | What the run's report **measured**: authored versus examined guarantees, added/reused/retired memberships, and the two entry sets | 287 L |
| `curator_ingest_planes.py` | Reading **both** planes once, before a single entry is planned, and each plane's own state | 285 L |
| `curator_source_manifest.py` | The external sources as a **bounded manifest** named by its own sha256, and the origin refs that bind to it | 456 L |

**Three outcomes stay three facts, end to end.** `member` places the entry's exact revision in the
families it names; `no_family` records the deliberate outcome with the basis it rests on — carried into
the revision's own recorded conditions, so the *dataset* distinguishes it, not only the report — and an
entry carrying no family key at all is **unexamined**, reported as such rather than as an empty family.
The same discipline governs the source plane: `external_sources: []` means the curator examined and
declared none, while omitting the key means it was not examined, and `manifest_written` is a fact
separate from "the list declared something" because a refused batch still wrote the file it had named.

**Identity is allocated, never derived.** A declaration's family identity pair is fresh `uuid4`
recorded in the candidate's own `curator-family-allocation-journal.json` under a retry key joined to the
enclosure's scope, so a repeat of one operation resolves to what it already holds while the same key
arriving with a **changed** guarantee is refused with the successor shape named. A membership identity
is `uuid5` over its two exact endpoints, so repeating one operation derives one row. Nothing is grouped
by a path, a directory, a route, a label or a shared anchor — that inference is the bulk import this
requirement exists to refuse.

**The seam is deliberately one-directional about the one question that needs a dataset.** Whether a
membership naming no declaration still resolves is a question about the candidate as much as about the
list, so `read_family_plane` does not answer it and `curator_family_planning._declarationfamily_refusal`
is its single implementation. A second copy in the read half was deleted in the fix round: it answered
a question that depends on the dataset, and no mutation could distinguish it.

**Nothing in this route writes.** The five owners read, resolve, plan and report; the commands travel
into the one batch `knowledge_ingest.py` builds, so the one writer and the one transaction remain the
only implementations, and the admitted destination's own `authorship` is what every drafted row's
provenance comes from.

**A closed false-sentence defect, recorded because the code's shape depends on it.** The operation
could report `family.state "recorded"` with a guarantee `authored` and a membership `added` over a
candidate holding **zero** family rows: the replay short-circuit asked the invariant-revision replay set
rather than the batch, so a plan whose revision already existed skipped the whole batch while the report
was still assembled from the plan. `curator_entry_commands` now gives a **replayed** entry its family
plane alone, `knowledge_curator_ingest._run` short-circuits on the pending command list, and
`_record_what_the_batch_will_write` keeps the allocation journals and the manifest behind that same
predicate.

## 260921-ICR-L15 Measured assessment currentness

`260921-ICR-L15` (`ICR-R15@v1`) replaces the one entry in the L14 record bundle that this route
**stated without measuring** with a measurement its own owner produces, and carries it to the payload
and to the sealed generation.

**A new module owns the measurement.** `application/review_assessment_currentness.py` (226 lines)
publishes two functions and one owner constant. `comparison_currentness_measurement(resolved)`
measures the identities the viewed comparison publishes — the resolution's two bound code endpoints,
the leaf it names and the enclosure contract it read — so it performs no I/O and cannot fail halfway.
`currentness_channel(collection, measurement, assessments)` states that measurement's availability in
**exactly three product states**: `recorded` (a measurement was performed, with the number of stored
bindings it was compared against), `none_recorded` (the authority answered and records no assessment —
a real zero rather than a silence) and `unavailable` (the authority could not be read, so nothing could
be measured). None of the three is a favourable default.

**The record bundle now produces it, and the placeholder constant is gone.**
`application/review_evidence_records.py` (869 → 879) produces the measurement in `review_records_for_resolution` —
where the L14 record-owner section below still describes a "non-measurement" — and
`_COLLECTION_OWNERS["assessment_currentness"]` names the real owner rather than a stand-in. The
unresolved-candidate path reports the collection `unavailable` beside the five owner collections
instead of leaving it out, because nothing resolved and so no measurement could be made. The constant
`_CURRENTNESS` — the module-level value that spelled "not measured" — **was DELETED**: that state is
now one of `currentness_channel`'s three answers, produced from a measurement, so a second spelling of
it would be the drift the L14 section's own rule forbids.

**The renderer takes the measurement instead of inferring from presence.**
`application/review_record_rendering.py` (473 → 488) replaced `ReviewRecordInputs.current` (a bare
mapping) with `currentness: AssessmentCurrentnessMeasurement | None`, and `subject_states` now
delegates to the shipped projection — `measured_binding_statuses(records.assessments,
records.currentness)` — rather than testing whether a currentness value was present at all. `None`
still means "no measurement was supplied", and that state keeps the projection's `stale` rather than
promoting an unmeasured assessment to `current`.

**The freeze's flag now means what its name says.** `application/review_comparison_freeze.py`
(744 → 747) carries `current_measured` as "a measurement was performed" rather than "a value was
present", so a sealed generation records whether the currentness axis was measured.

## 260921-ICR-L21 The Recorded Comparison Identifies What Closeout And Integration Delivered, And Recording Is Not A Gate

`260921-ICR-L21` (`ICR-R21@v1`, review-to-closeout identity continuity) closes the last gap between the
two halves of a task's evidence: a generation records what a review **read**, while closeout and
integration produce what the task **delivered**. A reader holding only "a comparison was made" could not
tell whether the historical review opens the pair the task actually landed. This route gained **two
purpose-named owners and one test module**, and `knowledge_review.py` — the master's global write mutex —
was **not touched at all** (byte-identical), because the seam policy moves a *touched* responsibility and
this leaf added none there.

- **The record and its vocabulary.** `models/knowledge/review_final_output_receipt.py` owns
  `FinalOutputReceipt`, its self-consistency validator and the one derived sentence. Its three-valued
  verdict exists because two values would have to call an unmeasured delivery `bound`: a generation that
  **selected** a knowledge operand and had no delivered dataset compared against it is `unmeasured`, not
  matched, and `bound` — the value a consumer keys on as coverage — requires a measured match on every
  channel the generation actually selected. `not-comparable` is likewise not a softer `differs`.
- **The operation.** `application/review_final_output_receipt.py` owns the selection (the generation
  store's own highest recorded index, with `no-generation` ≠ `unreadable` ≠ `ambiguous` and an ambiguous
  tie recording nothing), the receipt (published through the durable-evidence owner, one file per leaf,
  generation and phase), and the read-back (recorded / not-recorded / unreadable, beside the generations
  that supersede it — measured at read time, never written into the record).
- **It is wired into the production result surfaces.** `application/worktree_tools.py` attaches the
  selection to the closeout **preview** and the receipt to closeout **apply** and to **integration**;
  `application/review_comparison_reopen.py` gained a fourth channel, `final_output`, so reopening a
  recorded comparison reports the delivered code, memory and published-knowledge outputs beside the
  inputs it was compared against — which is this requirement's own sentence, read through the closed-leaf
  review route.
- **Nothing here can gate a transaction.** Recording runs after the Git transaction and its contract
  write, inside the result builder; the transaction owners call the never-raising wrapper, and a receipt
  that cannot be produced is reported as a state with its reason. A `moved` receipt deliberately does
  **not** block: the packet forbids adding a gate, and the remedy it names — publish a successor
  generation naming this one as its predecessor — is recorded in the receipt's own sentence.
- **Boundary: the reclamation owner has no shipped caller, and that is routed debt, not an omission.**
  `discard_final_output_receipts` states it plainly in its own docstring and names its consumers: an
  explicit retention/release pass and the acceptance corridor that measures reclamation (**ICR-R25@v1**,
  secondary the R11 retention/release route). It is the same shape the generation owner landed
  (`review_comparison_reclamation.py` is likewise a named owner no automatic caller invokes) — the receipt
  is retained evidence, and deleting it during ordinary cleanup would destroy the artifact the requirement
  asks to survive. **Reclamation is therefore not automatic at this candidate.**
- **Boundary: direct in-process callers of `git_worktree_manager.closeout_result` see no receipt**, because
  the production result surface is the MCP tool and `layers.toml` ranks `application` above `worktrees`;
  no shipped console script routes closeout or integration through the other caller.

This realises the wiring `260921-ICR-L11` recorded as a boundary — *"the freeze is deliberately not wired
to any route or read path; ICR-R21 wires it at closeout"* — and the per-file detail lives in the three new
sidecars. **What R21 actually wired is the identity, not the freeze:** it attaches the selected
generation to the closeout preview and the delivered receipt to closeout apply and integration, and it
adds the reopen's fourth channel. The freeze itself acquires its first shipped caller one leaf later,
from `260921-ICR-L34`'s `review-record-comparison` CLI; the L11 boundary above is corrected in place
there.

## 260921-ICR-L8 The Recorded Relationship Union Is Traversed, And Both Sides Of Every Association Are Displayed

`260921-ICR-L8` (`ICR-R08@v1`, movement and relationship evolution) is about one rule: a review must show
**both sides** of a changed realization, family membership and governing-route association while
preserving the canonical identity — because only the after graph is read today, so the old association
vanishes. This route gained **five** purpose-named owners, and `knowledge_review.py` gained an import
and **one call**:

- `application/review_relationship_movement.py` (583 L) — the traversal: the union both snapshots
  record, one movement per relationship, the pairing made **only** by the author's own records (the same
  row, or an authored predecessor edge of a withdrawn row), each pairing naming its recorded basis.
- `application/review_relationship_display.py` (858 L) — what one relationship is displayed as: both
  sides with the snapshot fact each one is, the authored succession/split/merge lineage, one gap per
  fact the display could not establish (with its side, code and reason), the address view the pane
  renders, and the sentences that may only state what was read.
- `application/review_recorded_relationships.py` (603 L) — the relationships one snapshot's union items
  record, its identity rows and its own authored edges, plus the authored-line reach.
- `application/review_governing_route.py` (258 L) — the reviewed identity's recorded route association
  on each snapshot, with `recorded`/`ungoverned`/`not_recorded` kept apart.
- `application/review_rename_inference.py` (331 L) — Git's own rename detection over the two bound tree
  objects, as a labelled inference that is never proof that an invariant moved.

**The ruling this route implements: the union is not bounded by the comparison's selected revision
page.** A read selects the revision a relationship cites, not the revisions that succeeded it, so an
association an author re-recorded onto a successor revision is recorded in the snapshot while being
outside the page. For every baseline-only side the traversal reads that citation's **authored successor
line** — every authored descendant, not just its head — through ICR-R07@v1's own head rule
(`revision_heads`, called rather than re-derived) and the shipped read owners (realizations by invariant
revision, memberships by family revision **and** by member revision), and it states an association it
finds there as one movement with both addresses. A line whose ends are several (a split that never
rejoins) or none (a cycle) yields the baseline side displayed as it stands plus
`successor_line_unresolved` with its shape — never the claim that nothing is recorded.

**One responsibility moved out of `review_source_inventory.py` before behavior was added.**
`_location`, `_realization_read_item` and `_change_state` left it (804 → 771 lines); the location is now
`review_relationship_display._location`, the change state is
`review_recorded_relationships.recorded_change_state`, and the payload selection the deleted helper
performed is `side_payload`/`read_snapshot_relationships`. `source_pane` takes the traversed
`relationships` sequence and renders its address view through the traversal module's own
`source_locations`, so there is one implementation and one import path.

**What the route does not do.** Nothing here selects, ranks or concludes; ICR-R04's attribution
partition and ICR-R07's head rule are called, never re-derived; the labelled rename inference is attached
after the movements exist and is never read back. The production path reaches `anchor_unresolved`,
`successor_line_unresolved` and `predecessor_records_no_relationship`, plus the transition
`outside_selection` and the state `ungoverned`; `anchor_unrecorded`, `identity_differs`,
`identity_not_recorded` and `route_not_recorded` are defensive-only for the graph the schema admits.
Mounting the collection in the browser pane is `ICR-R24`'s and the A06/A07/A24 journey is `ICR-R25`'s.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The traversal's own statement of the union, the author-only pairing, the ruling and the unresolved-and-never-denied rule.** | `relationship_movements`; `RelationshipSources` | mcp/src/agents_remember/application/review_relationship_movement.py:123-139; mcp/src/agents_remember/application/review_relationship_movement.py:142-177 |
| **The whole authored line is read, and the pairing rules: member-wise family pairing, the strict successor form, the withdrawal half.** | `_line_relationships`; `_replaced`; `_continues`; `_pairing_basis` | mcp/src/agents_remember/application/review_relationship_movement.py:227-274; mcp/src/agents_remember/application/review_relationship_movement.py:518-541; mcp/src/agents_remember/application/review_relationship_movement.py:544-580; mcp/src/agents_remember/application/review_relationship_movement.py:439-468 |
| **The display's tested search value, the two-sided and one-sided movements, and the basis sentences that reserve "head" for a row that is one.** | `ContinuationSearch`; `paired_movement`; `single_sided_movement`; `_BASIS_SENTENCES` | mcp/src/agents_remember/application/review_relationship_display.py:50-73; mcp/src/agents_remember/application/review_relationship_display.py:107-139; mcp/src/agents_remember/application/review_relationship_display.py:142-174; mcp/src/agents_remember/application/review_relationship_display.py:354-387 |
| **The reach: the head rule called from ICR-R07, the whole-line read, and the owner chosen by the kind of revision.** | `successor_line`; `read_line_relationships`; `revision_heads` | mcp/src/agents_remember/application/review_recorded_relationships.py:233-292; mcp/src/agents_remember/application/review_recorded_relationships.py:309-339; mcp/src/agents_remember/application/review_revision_comparison.py:81-94 |
| The route association, with the existence question asked before the route question. | `governing_route_movement`; `_route_side` | mcp/src/agents_remember/application/review_governing_route.py:59-93; mcp/src/agents_remember/application/review_governing_route.py:122-158 |
| **The labelled Git inference: the exact command, the three states, and the sentence that says it is not proof that the invariant moved.** | `git_rename_inference`; `with_rename_inferences`; `_inference_for` | mcp/src/agents_remember/application/review_rename_inference.py:96-125; mcp/src/agents_remember/application/review_rename_inference.py:155-177; mcp/src/agents_remember/application/review_rename_inference.py:238-288 |
| **The adapter's one call, and the pane that composes the traversal's own address view.** | `compose_review`; `source_pane`; `source_locations` | mcp/src/agents_remember/application/knowledge_review.py:334-574; mcp/src/agents_remember/application/review_source_inventory.py:560-613; mcp/src/agents_remember/application/review_relationship_display.py:76-104 |

## 260921-ICR-L9 The Subject Catalogue Is Enumerated From Both Snapshots, And Compare-To-Earn-A-Row Is Deleted

This route gained **one module and one mechanism replacement**, and the leaf they belong to
(`260921-ICR-L9`, primary requirement `ICR-R09@v1`) is about one rule: *every valid invariant/family
subject in the comparison's before/after population is reachable through the normal task review.*
The per-file detail lives in the new sidecar; what belongs at this route's altitude is the population
rule, the seam, and the deletion.

- **The catalogue has an owner.** `application/review_subject_catalogue.py` (150 lines) owns the entry
  half's enumeration: the union of **both** snapshots' own identity tables, read through the store's
  own `list_invariants`/`list_families`, with per-row `presence` (`before_only`/`after_only`/`both`)
  and the after side's label winning on overlap. Rows are globally kind-grouped — every invariant,
  including a retired one, precedes every family — the knowledge history is append-only, so a retired
  subject is neither gone nor unreviewable, and **listing an identity never runs the shipped
  comparison for it** (the served route is tripwired; measured `diff_calls=0` at 12 and 87 rows).
  Zero subjects is a valid catalogue beside the source inventory, and an unselectable subject is
  listed with the comparison's own typed refusal carried by the review it opens — no silent drops.
- **The seam is the same "keep the adapter a delegator" rule this route has applied five times
  before.** `application/knowledge_review.py` (841 → 757 lines) delegates `list_knowledge_review_entries`
  to `read_subject_catalogue` and fills the labelled totals (`total_subjects`/`invariant_total`/
  `family_total`); the per-subject compare-to-earn-a-row helpers (`_reviewable_entries`,
  `_recorded_identities`, `_selected_item_count`) are **deleted, not moved** — they were private to
  the adapter, so no alias is left and `__all__` is unchanged. The vocabulary carries the new fields:
  `ReviewEntry.presence` replaces `selected_item_count`, and `ReviewEntryListResult` gains the totals
  with their agreement validator (the `>=` rule R10's paging depends on).
- **Exactly one KS-era mechanism block was re-contracted, and the deletion is falsified beside the
  new rule.** The pane-types case in `test_knowledge_review_surface.py` measured the old
  "a subject the comparison cannot answer for is absent from the list" mechanism — the packet orders
  it replaced — and now asserts the catalogue contract (union, labels, presence, unrecorded-id
  exclusion, agreement with the shipped comparison). The ten-case `test_review_subject_catalogue.py`
  module (registered in both exact-scope consumer rows of `evidence-lifecycle.toml` and in the
  `unit-regression` lane) pins the union, the kind grouping with retired subjects, the one-sided
  retired/added openings, the statement-free family, the whole-row traversal, the carried refusal
  reason, the totals, the zero-subject boundary and the no-comparison tripwire. Routed, not closed:
  catalogue paging is R10's, cockpit/browser/keyboard journeys are R24's, relationship traversal over
  the now-complete family population is R08's, and typed-contract labels are R26's.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The new catalogue owner: both snapshots' identity tables, per-row presence, no comparison, no silent drops.** | `read_subject_catalogue`; `_union` | mcp/src/agents_remember/application/review_subject_catalogue.py:47-69; mcp/src/agents_remember/application/review_subject_catalogue.py:90-112
| **The adapter's delegation: the entry half resolves, calls the catalogue, fills the totals and assembles — the per-subject helpers deleted.** | `list_knowledge_review_entries`; `read_subject_catalogue` | mcp/src/agents_remember/application/knowledge_review.py:256-317; mcp/src/agents_remember/application/review_subject_catalogue.py:47-69 |
| **The presence vocabulary and the totals with their agreement validator.** | `ReviewSubjectPresence`; `ReviewEntry`; `ReviewEntryListResult` | mcp/src/agents_remember/models/knowledge/review.py:210-210; mcp/src/agents_remember/models/knowledge/review.py:341-359; mcp/src/agents_remember/models/knowledge/review.py:1128-1189; mcp/src/agents_remember/models/knowledge/review.py:1076-1076; mcp/src/agents_remember/models/knowledge/review.py:289-289 |
| **The ten catalogue cases and the re-contracted mechanism case.** | `test_the_catalogue_unions_both_snapshots_with_labels_and_presence`; `test_catalogue_loading_runs_no_comparison` | mcp/tests/test_review_subject_catalogue.py:232-249; mcp/tests/test_review_subject_catalogue.py:511-545; mcp/tests/test_knowledge_review_resolution_and_route.py:311-381 |

## 260921-ICR-L7 The Statement Sides Are Rendered From Selected Heads, And The Both-Sides Preference Is Deleted

This route gained **one module and one seam**, and the leaf they belong to (`260921-ICR-L7`, primary
requirement `ICR-R07@v1`) is about a single rule with a deletion behind it: *the primary statement
comparison uses an explicit before/after revision selection, and a retained predecessor both snapshots
happen to hold is never chosen for both sides.* The per-file detail lives in the new sidecars; what
belongs at this route's altitude is the rule, the seam, and the deletion.

- **Head selection now has an owner.** `application/review_revision_comparison.py` owns the one rule
  the packet states — a head is a retained revision with no recorded successor for that identity in
  the selected snapshot population, where "recorded successor" means an authored predecessor edge and
  nothing else. Unique heads compare head-to-head (before `r1` against after `r1 → r2 → r3` defaults
  to `r1` versus `r3`); a known-empty side stays an `ICR-R06@v1` addition/removal; multiple heads, a
  successor cycle, or a dangling authored edge yield explicit ambiguous/unresolved selections that
  still list every head and every retained revision; intermediate revisions stay selectable through
  the comparison's own per-side selector. No collection order, no both-sides presence, no timestamp
  and no text similarity participates.
- **The seam is the same "keep the adapter a delegator" rule this route has applied four times
  before.** `application/knowledge_review.py` (825 → 843 lines) gains one import plus the one call in
  `compose_review` that computes the selection from the comparison's own union items and the two
  snapshots' own authored edges, and `_knowledge_pane` renders it through the new `_selected_statements`
  — a compared or one-sided selection renders the heads' own recorded sides, an ambiguous or
  unresolved selection renders the explicit non-pair on both sides with empty conditions. The private
  both-sides preference (`_identity_item`, `_selector_record_id`) is **deleted, not forked**, and
  leaves no alias because nothing outside the adapter imported it. The recorded value lives outside
  the vocabulary file (`models/knowledge/revision_selection.py`) so that file stays under the soft
  rail, and is carried on the pane as the optional `revision_selection`.
- **Exactly two existing surface tests were rewritten from the old rule to ambiguity assertions, and
  the old rule is falsified beside the new one.** The pane case and the knowledge-only case now assert
  the explicitly ambiguous selection (the fixture's retry identity is branchy on both snapshots) with
  both sides `unresolved`; the ten new cases prove the two chain defaults with exact ids, selectable
  history, both forks, the one-sided removal, the cycle, the dangling edge, order-independence, and
  the pane's own head statements. Family-subject multi-revision choice beyond this packet stays
  R08/R09's; browser rendering of the recorded value stays R25's.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The new policy owner: the one head rule, what it reads, what it returns, and why it is its own module.** | `select_subject_revisions`; `revision_heads` | mcp/src/agents_remember/application/review_revision_comparison.py:1-31; mcp/src/agents_remember/application/review_revision_comparison.py:144-187; mcp/src/agents_remember/application/review_revision_comparison.py:81-94 |
| **The adapter's one call: the selection computed once in `compose_review` and rendered by the pane.** | `select_subject_revisions`; `_knowledge_pane`; `_selected_statements` | mcp/src/agents_remember/application/knowledge_review.py:965-1017; mcp/src/agents_remember/application/knowledge_review.py:1020-1043; mcp/src/agents_remember/application/knowledge_review.py:470-470; mcp/src/agents_remember/application/knowledge_review.py:464-464 |
| **The recorded value the policy returns into, carried on the pane.** | `ReviewRevisionSelection`; `revision_selection` |mcp/src/agents_remember/models/knowledge/revision_selection.py:54-150; mcp/src/agents_remember/models/knowledge/review.py:745-745|
| **The ten cases that measure the policy, and the two rewritten surface cases beside them.** | `test_a_unique_chain_defaults_to_the_first_before_head_versus_the_last_after_head`; `test_a_fork_on_the_after_side_is_an_explicit_ambiguity`; `test_the_review_pane_renders_the_selected_head_pairs_own_statements` | mcp/tests/test_knowledge_review_revision_selection.py:259-279; mcp/tests/test_knowledge_review_revision_selection.py:333-345; mcp/tests/test_knowledge_review_revision_selection.py:571-615 |

## 260921-ICR-L3 The Review's Content Read Becomes Its Own Owner, And A Path Is Admitted Only By A Measured Change Set

This route gained **one module and one seam**, and the leaf they belong to (`260921-ICR-L3`, primary
requirement `ICR-R03@v1`): `application/review_source_content.py` now owns opening **one review
inventory entry** into the actual content both bound code trees hold at its path. The review adapter is
untouched — it never owned this responsibility (the review payload carries no file text), so nothing had
to move out of it and it did not grow toward the rail; it is 831 lines before and after this leaf.

The module's own docstring states what it answers and what it refuses to own, and the three properties
are the reason it exists rather than living inside the adapter. The **generation is an input, not a
lookup**: the two tree object ids arrive with the request, are read back from the inventory the caller
is looking at, and are used to address the bytes, while the leaf's review is re-resolved only to
*measure* whether those ids are still the pair it binds — the answer travels as `currentness`, and a
working tree, `HEAD` or a newer candidate is never substituted. **Every side states its own truth**: a
side is `present`, `absent`, `binary`, `symlink`, `submodule` or `unavailable`, and `absent` (this
endpoint measured and holding nothing there) stays apart from `unavailable` (a measurement that was not
made, with its reason). **The content is real and bounded, never a reference**: text is carried to
2 MiB with the object's exact size beside it and `truncated` set when the carried text is a prefix.

The seam this leaf drew at this altitude is the path confinement, and it is the part a reader of this
route should carry away. A path is read only from a **measured change set**, and there are exactly two
sources: the requested generation's own change inventory, or — only when that measurement cannot be made
at all — the change set this leaf's review actually publishes (its recorded baseline against the
candidate tree it binds now). The admitting measurement is published on the answer as
`path_bound`/`path_bound_detail`, so a row always says which change set listed it. A path in neither is
refused by name in every state, which is what keeps this route a change-set read rather than a general
file reader over the recorded base. (Since 260921-ICR-L43 one further population is admitted — an
unchanged path of a measured pair that a recorded realization of the same comparison links — and the
admission policy lives in `review_source_admission.py`; see *Comparison-bound attributed unchanged
source content* above.) Two further admissions gate the read before any object is touched:
the two ids must be complete Git object identities, and the after generation must name a **tree** — a
commit, a blob or a tag this repository holds is refused by name, while an object it does *not* hold
stays a per-side `unavailable` measurement rather than a refusal, because refusing would hide the
readable side of a comparison that is otherwise inspectable.

What this module deliberately delegates is as load-bearing as what it owns: the change set is still the
inventory owner's `review_inventory` (called, never re-derived), the resolution and the currentness
recheck are `review_candidate_resolution`'s, the bytes are the kernel's byte-exact `read_git_blob_bytes`,
and the bounded decode plus the language id are the shipped file-transport primitives. The route reaches
it through a **third** `ServingCollaborators` port (`review_source_content`), wired by the composition
root, because `serving` ranks below `application`; the serving route model records that half. The
dashboard renderer (`dashboard/src/panels/review/SourceContent.tsx`) consumes the value and is on the
panels route.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the three properties it exists for, and of what it does not own — no diff, no re-measurement of the change set, no selection.** | `SOURCE_CONTENT_REFERENCE`; `EXPANSION_TEXT_BYTES` | mcp/src/agents_remember/application/review_source_content.py:70-70; mcp/src/agents_remember/application/review_source_content.py:75-75 |
| **The one entry point: resolve, screen the four admission facts, then read — with the currentness measurement taken after the bytes so it can only qualify them.** | `read_review_source_content` | mcp/src/agents_remember/application/review_source_content.py:110-131 |
| **The four admissions, each a distinct named refusal: a complete object identity per side, this leaf's recorded baseline, a *tree* as the after generation, and a path Git can be handed.** | `_inadmissible` | mcp/src/agents_remember/application/review_source_content.py:140-207 |
| **The after generation must be a tree: a commit, blob or tag this repository holds is refused by name, while a missing object stays a per-side measurement.** | `_non_tree_generation` | mcp/src/agents_remember/application/review_source_content.py:210-238 |
| **The confinement itself, now in the admission owner: a changed path of a measured change set (the requested generation's own, or, when that measurement is unavailable, the one this leaf's review publishes), or since L43 an unchanged path a recorded realization of the same comparison links — with the admission carried on the value.** | `admit_source_path`; `SourceAdmission` | mcp/src/agents_remember/application/review_source_admission.py:54-83; mcp/src/agents_remember/application/review_source_admission.py:86-128 |
| The refusals that keep the read confined, and the status an admitted path keeps when the pair's change set was not measured. | `_unconfined`; `_not_listed`; `SourceAdmission` | mcp/src/agents_remember/application/review_source_admission.py:162-193; mcp/src/agents_remember/application/review_source_admission.py:196-215; mcp/src/agents_remember/application/review_source_admission.py:54-83 |
| **The three generation statements — current, superseded, unmeasured — each of which ends by saying the content beside it is the requested generation's, byte for byte.** | `_currentness` | mcp/src/agents_remember/application/review_source_content.py:288-324 |
| **One endpoint's content with the three outcomes kept apart, and the entry's kind deciding before its bytes: a tree is not source, a gitlink is a recorded pointer with no bytes, a symlink mode is a link target.** | `_side_content`; `_entry_content` | mcp/src/agents_remember/application/review_source_content.py:346-365; mcp/src/agents_remember/application/review_source_content.py:368-390 |
| The two reasons no text form exists, and the bounded decode that carries a prefix rather than the whole object. | `_decoded`; `_binary_detail`; `_text_detail` | mcp/src/agents_remember/application/review_source_content.py:437-451; mcp/src/agents_remember/application/review_source_content.py:454-467; mcp/src/agents_remember/application/review_source_content.py:470-479 |
| **The tree read: a literal pathspec, because a measured pathname is an address and not a pattern, and the answer checked against the path that was asked about.** | `_tree_entry`; `_parsed_record` | mcp/src/agents_remember/application/review_source_content.py:491-515; mcp/src/agents_remember/application/review_source_content.py:518-531 |
| The exact reproduction line a reader acts on, and the second path check that refuses the spellings Git could not have reported. | `_reproduction`; `_addressable` | mcp/src/agents_remember/application/review_source_content.py:550-562; mcp/src/agents_remember/application/review_source_content.py:585-596 |
| **The owners this module calls instead of re-implementing: the inventory measurement and its side value, the resolution, and the shipped recheck.** | `review_inventory`; `source_tree_side`; `resolve_review_candidate`; `require_current_candidate_identity` |mcp/src/agents_remember/application/review_source_inventory.py:429-469; mcp/src/agents_remember/application/review_source_inventory.py:168-176; mcp/src/agents_remember/application/review_candidate_resolution.py:180-242; mcp/src/agents_remember/application/review_candidate_resolution.py:308-341|
| **The third collaborator port that carries this owner into the serving tier.** | `review_source_content`; `review_source_content_port` | mcp/src/agents_remember/serving/_app_common.py:484-484; mcp/src/agents_remember/cli/dashboard.py:123-133 |
| **The production-composition cases: both endpoints' own bytes against an independent `git show`, every non-text kind, a stated bounded expansion, generation binding across a branch advance, the unmeasured-generation confinement, a commit id refused, and the unwired process refused by name.** | `test_a_modified_file_opens_both_endpoints_own_bytes`; `test_a_pruned_base_blob_is_unavailable_on_its_side_while_the_candidate_side_is_served`; `test_an_unmeasured_generation_still_confines_the_path_to_a_measured_change_set`; `test_a_generation_that_names_a_commit_is_refused_rather_than_served` | mcp/tests/test_knowledge_review_source_content.py:269-311; mcp/tests/test_knowledge_review_source_content.py:599-638; mcp/tests/test_knowledge_review_source_content.py:641-676; mcp/tests/test_knowledge_review_source_content.py:679-719 |
## 260921-ICR-L14 The Review Carries Every Owner-Produced Record Collection, And An Empty Tuple Stops Meaning Three Things

**A new owner on this route, and it is the composition's record half.**
[`application/review_evidence_records.py`](review_evidence_records.py.md) is `ICR-R14@v1`'s production
owner: for one resolved candidate it reads **all five** owner-produced collections — the curator
authority's published assessments, the detection owner's signals, the evidence owner's verification
observations and evidence claims, and the review matrix's authored effects — plus the one quantity
nobody in this composition measures (dependency currentness), and hands them over as the bundle the
surface renders. It produces no record, re-derives no owner's content and decides nothing.

**What moved, and why this route is the one that changed.** `review_records_for` used to be a private
resolver at the bottom of [`knowledge_review.py`](knowledge_review.py.md) that read the published
assessments and returned an empty collection for an absent *or* an unreadable authority. That body is
gone rather than kept beside the new owner, and the adapter re-exports the name from its new home. The
adapter is **831 → 819 lines** while gaining the channel assembly, and the over-limit review adapter no
longer carries a responsibility the record owner can hold.

**The defect this removes is a three-way collapse.** An empty tuple used to stand for "the owner answered
and holds none", "expected content could not be read" and "this composition never asked". Availability is
now a fact **per collection**, carried as a
[`ReviewRecordChannel`](../models/knowledge/review_records.py.md) on the bundle and on
`ReviewEvidencePane.channels`: `recorded` / `none_recorded` / `unavailable` (with the owner's own refusal
as provenance and, where applicable, the exact unreadable identities) / `not_measured` / `not_selected`.
The model makes a favourable default unrepresentable — an unreadable authority carries **no** count, and
every non-answer must state what would produce one.

**Three behaviours a reader of this route should carry:**

- **One unreadable authority does not withdraw the readable collections.** Every read is guarded per
  collection, and inside the two multi-record collections the guard is per **record**: a damaged
  detection run, or a claim whose stored payload no longer decodes, is named on its channel
  (`unreadable`) while its siblings are supplied. That needed two new reads from this route's owners —
  `detection.recorded_run_ids` and `evidence_records.claim_ids` — so the guard could reuse each owner's
  own single-record reader instead of growing a second reader of the same tables.
- **The matrix-owned collections are reported from the matrix's own answer.** The two compositions call
  `with_selection_channels`: the subject composition passes the rows the view returned and the view's
  declared `rows_remaining` (through `_rows_remaining`), and the task-context composition — which reads
  no matrix — reports `not_selected` rather than an absence it never asked about.
- **Nothing is measured here that R15 owns.** The currentness channel states `not_measured` and names
  `review_assessment_store.assessment_currentness_for_record`, so no unmeasured assessment is promoted
  to `current`.

**What this route deliberately does not decide:** which records may be displayed as direct, historical
or related context (that is `ICR-R26@v1`'s applicability classification, and the bundle supplies the
records unfiltered), and what dependency currentness is (R15's measurement).

| Finding | Anchor | Source |
| --- | --- | --- |
| **The new production owner: the five collections plus the non-measurement, each read through its owner with its availability fact.** | `review_records_for`; `review_records_for_resolution`; `_COLLECTION_OWNERS` | mcp/src/agents_remember/application/review_evidence_records.py:170-195; mcp/src/agents_remember/application/review_evidence_records.py:198-235; mcp/src/agents_remember/application/review_evidence_records.py:136-143 |
| **The per-record guard that makes a damaged record survivable, and the two owner reads it composes.** | `_read_signal_runs`; `_claim_records`; `recorded_run_ids`; `claim_ids` | mcp/src/agents_remember/application/review_evidence_records.py:387-412; mcp/src/agents_remember/application/review_evidence_records.py:521-545; mcp/src/agents_remember/memory/knowledge/detection.py:565-579; mcp/src/agents_remember/memory/knowledge/evidence_records.py:838-850|
| **The availability vocabulary, and the validator that refuses a count no owner measured.** | `ReviewRecordChannel`; `ReviewRecordChannelState` | mcp/src/agents_remember/models/knowledge/review_records.py:47-53; mcp/src/agents_remember/models/knowledge/review_records.py:68-123 |
| **The selection channels, added where the matrix's own answer is; and the task-context position that never asked.** | `with_selection_channels`; `_matrix_rows_remaining` | mcp/src/agents_remember/application/review_evidence_records.py:274-299; mcp/src/agents_remember/application/knowledge_review.py:647-660 |
| **The adapter that lost the private resolver and re-exports the owner's, and the port the production app reads it through.** | `review_records_for`; `review_port` | mcp/src/agents_remember/application/knowledge_review.py:99-99; mcp/src/agents_remember/cli/dashboard.py:97-111 |
| **The cases that measure the whole thing through the production port, including the two per-record damage cases.** | `test_the_production_composition_supplies_every_owner_produced_record_class`; `test_a_damaged_detection_run_is_named_while_its_siblings_are_supplied`; `test_a_damaged_evidence_claim_is_named_while_its_siblings_are_supplied` | mcp/tests/test_knowledge_review_evidence_channels.py:566-618; mcp/tests/test_knowledge_review_evidence_channels.py:825-844; mcp/tests/test_knowledge_review_evidence_channels.py:847-870 |
## 260921-ICR-L4 The Attribution Accounting Gets An Acquisition Owner, And Every Route Reads One Partition

This route gained **one module** and the leaf it belongs to (`260921-ICR-L4`, primary requirement
ICR-R04@v1) is a single obligation: *every measured changed path belongs to exactly one attribution
bucket*. The per-file detail lives in the sidecars; what belongs at this route's altitude is the
split and the two rules that keep the routes from disagreeing.

- **Acquisition is one module, arithmetic is another, and the adapter stays a delegator.**
  `application/review_attribution.py` reads the two bound snapshots' registered mappings by exact
  path equality through the shipped lookup, observes each anchor, and decides each side's inspection
  state — and decides no arithmetic. The partition it hands those facts to lives beside the display
  seam (`memory/knowledge/diff_attribution.py`), and the adapter (`knowledge_review.py`) only hoists
  the observation once, hands it to both renderings, and carries the comparison's own partition
  verbatim through `_comparison_attribution`.
- **A review that compares no dataset still reports attribution, measured from its own pair.**
  `review_task_context.pair_attribution` opens each half read-only when it is there and carries an
  unreadable one as an unavailable side — with only the side that cannot be bound marked so — so a
  valid positive mapping on the readable side stays attributed with its incompleteness labeled, and
  nothing unreadable becomes a confirmed negative.
- **One owner for the unreadable-candidate refusal.** `review_candidate_resolution.py` now owns
  `unreadable_candidate_refusal`/`candidate_receipt_refusal`: the entry route, the subject route and
  the task-context route answer the same bytes with the same code, detail, next action and offending
  input.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The acquisition owner: exact-path lookup, only `exact_recorded_blob` resolving, unread sides licensing nothing, R05's damage and empty-generation readers consumed.** | `review_attribution`; `_RESOLVED_MAPPINGS`; `_damaged_half`; `_inspection_state` | mcp/src/agents_remember/application/review_attribution.py:181-211; mcp/src/agents_remember/application/review_attribution.py:100-100; mcp/src/agents_remember/application/review_attribution.py:359-379; mcp/src/agents_remember/application/review_attribution.py:334-356 |
| **The task-context pair measurement and the receipt asked twice, so a record that breaks mid-read is stated, never raised.** | `pair_attribution`; `_pair_without_namespace` | mcp/src/agents_remember/application/review_task_context.py:280-337; mcp/src/agents_remember/application/review_task_context.py:340-368 |
| **The comparison's reader over its own two open snapshots, and the adapter's verbatim carry.** | `_registered_mapping_reader`; `_comparison_attribution` | mcp/src/agents_remember/application/knowledge_diff.py:451-484; mcp/src/agents_remember/application/knowledge_review.py:595-605 |
| **The one refusal owner the three routes read.** | `unreadable_candidate_refusal`; `candidate_receipt_refusal` |mcp/src/agents_remember/application/review_candidate_resolution.py:460-475; mcp/src/agents_remember/application/review_candidate_resolution.py:478-491|
| **The pane that reads the partition instead of recomputing it, with every count scoped or reasoned.** | `source_pane`; `attribution_limitations`; `_remaining` | mcp/src/agents_remember/application/review_source_inventory.py:560-613; mcp/src/agents_remember/application/review_source_inventory.py:630-685; mcp/src/agents_remember/application/review_source_inventory.py:750-771 |

## 260921-ICR-L11 The Durable Comparison Generation: Five New Owners, One Keystone Record, And A Freeze Nothing Calls Yet

This route gained **five modules** and the leaf they belong to (`260921-ICR-L11`, primary requirement
ICR-R11@v1) is a single obligation: *a frozen comparison retains resolvable source, knowledge and
evidence inputs through cleanup and restart*. Everything a comparison actually reads is disposable —
both datasets live in a leaf's disposable knowledge root, the bound candidate is a tree that exists in
**no commit**, and the worktree holding both is removed by cleanup — so before this leaf a reader holding
only "a comparison was made" could re-read nothing at all. The per-file detail lives in the five new
sidecars; what belongs at this route's altitude is the split and the two boundaries.

- **The record is the keystone.** `application/review_comparison_generation.py` owns the immutable
  manifest, its layout under `<task_root>/notes/reports/comparison-generations/<leaf>/<generation-id>/`,
  the unavailable-history record, and the reads. It stores **references to owner-produced content and no
  semantic judgment**, its generation id is **re-derived from its own seal** and then checked a second
  time against the directory it was found in, and a `retained` knowledge side must carry identity **and**
  bytes by construction — which makes the packet's non-conforming example (a manifest holding only a
  digest of already-deleted SQLite bytes) unconstructible rather than merely discouraged.
- **Production is separate from retention, and retention from reclamation.**
  `review_comparison_freeze.py` is the act (resolve → compose → freeze, staged → validated → sealed →
  **one rename**), `review_comparison_retention.py` is where the bytes come from (custody measured
  against **named durable history only**; both halves copied by the storage snapshot owner), and
  `review_comparison_reclamation.py` is the two operations that may delete them (record first, measure
  the deleted digest, never alias today's data). `review_comparison_reopen.py` is the read-back: one
  state per channel, never one verdict, with `unavailable_channels()` naming exactly what did not
  resolve.
- **Custody is a measurement, and the branch it measures matters.** The leaf's code pin is created only
  when the history the caller **names** — the protected source branch plus the commits a task record
  landed — does not already hold the tree. The leaf's own disposable work branch is deliberately not one
  of the names: `worktree_abandon` force-deletes it and ordinary cleanup removes it, so a commit living
  only there is not custody, and a generation resting on it would lose its source side with the leaf.

**Two route-level boundaries, recorded as boundaries rather than defects.**

1. **The freeze has a production caller since `260921-ICR-L34`, and this boundary is superseded in
   part.** As L11 recorded it: nothing in *that* leaf called `freeze_review_comparison` from a serving
   surface, an HTTP route, the dashboard or a closeout path, and a reader was told not to read the
   absence of callers as dead code — the production entry is complete and measured by fifteen
   production-composition cases. Two things have changed since, and they are different things:
   **ICR-R21** wired the review-to-closeout *identity* into the closeout and integration results
   (a receipt and a fourth reopen channel) without calling the freeze; and **`260921-ICR-L34`** gave
   the freeze its first shipped caller outside the test suite, the CLI subcommand
   `agents-remember review-record-comparison`
   ([`cli/review_comparison_record.py`](../cli/review_comparison_record.py.md)), which composes the
   review exactly as the surface does and publishes what that composition bound. The freeze is
   therefore **still** not wired to a route, a pane or a closeout path — it is a command an operator
   runs while the leaf's enclosure is live — but "no caller" is no longer true, and a leaf that has
   published no generation still reopens from its recorded source range.
2. **A relocated coordination root degrades the reopened source channel to `missing`.** The record stores
   an absolute `task_root` / `contract_path` / `code_repository_root`, so the retained snapshot bytes and
   the cited task artifacts travel with the tree while the source channel resolves against the recorded
   repository path. That is ruled the boundary of **ICR-R12/R13**, which consume
   `reopen_comparison_generation` and own historical resolution.

The one route-level consequence a reader should carry: **the review surface's comparison can now outlive
the leaf that made it**, and what survives is a record of owner-produced identities — not a second
measurement, not a second store, and not a new source of authored truth.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The keystone record: the manifest, the layout under the one durable root, the deletion record, the re-derived id and the directory-name agreement.** | `ComparisonGenerationManifest`; `read_manifest`; `generation_identity`; `assemble_manifest`; `comparison_generations_root` | mcp/src/agents_remember/application/review_comparison_generation.py:405-498; mcp/src/agents_remember/application/review_comparison_generation.py:575-583; mcp/src/agents_remember/application/review_comparison_generation.py:615-649; mcp/src/agents_remember/application/review_comparison_generation.py:586-609; mcp/src/agents_remember/application/review_comparison_generation.py:524-527 |
| **The production entry: resolve and compose exactly as the surface does, then freeze only what that composition bound.** | `freeze_review_comparison`; `freeze_comparison_generation` | mcp/src/agents_remember/application/review_comparison_freeze.py:239-258; mcp/src/agents_remember/application/review_comparison_freeze.py:319-356 |
| **The one-rename publication, the convergence on an already-published record, and the reclaim paths that leave no stage and no unpublished pin.** | `_publish`; `_reuse_or_refuse`; `_reclaim` | mcp/src/agents_remember/application/review_comparison_freeze.py:438-462; mcp/src/agents_remember/application/review_comparison_freeze.py:465-497; mcp/src/agents_remember/application/review_comparison_freeze.py:531-542; mcp/src/agents_remember/application/review_comparison_freeze.py:367-429 |
| **The sweep that reclaims only from the dead, scoped to the one leaf directory the record names.** | `_sweep_stale_stages`; `_issuer_alive`; `_stage` | mcp/src/agents_remember/application/review_comparison_freeze.py:810-830; mcp/src/agents_remember/application/review_comparison_freeze.py:833-854; mcp/src/agents_remember/application/review_comparison_freeze.py:793-807 |
| **The whole definition of durable history for this feature — the protected source branch plus the recorded landed commits — and the reason the work branch is absent.** | `custody_names`; `retain_comparison_source` | mcp/src/agents_remember/application/review_comparison_retention.py:278-295; mcp/src/agents_remember/application/review_comparison_retention.py:134-170 |
| **Both halves copied through the storage snapshot owner, under the dataset's own bound namespace, with the two refusals that keep a storage error out of the freeze.** | `retain_knowledge_sides`; `_freeze_side` | mcp/src/agents_remember/application/review_comparison_retention.py:381-407; mcp/src/agents_remember/application/review_comparison_retention.py:478-534 |
| **The two deletion owners: the record written before the deletion, the measured digest, and the refusal that removes nothing.** | `release_comparison_code_object`; `discard_comparison_snapshots`; `_measure_and_remove` | mcp/src/agents_remember/application/review_comparison_reclamation.py:77-124; mcp/src/agents_remember/application/review_comparison_reclamation.py:174-210; mcp/src/agents_remember/application/review_comparison_reclamation.py:213-241 |
| **The read-back: one state per channel (four of them since ICR-R21@v1), `unavailable_channels()`, and the live pin measurement leading the release history.** | `ComparisonReopen`; `reopen_comparison_generation`; `ComparisonSourceChannel` | mcp/src/agents_remember/application/review_comparison_reopen.py:108-133; mcp/src/agents_remember/application/review_comparison_reopen.py:164-225; mcp/src/agents_remember/application/review_comparison_reopen.py:228-249 |
| **The one durable-root owner the layout asks instead of restating `<task_root>/notes/reports`.** | `durable_reports_root` | mcp/src/agents_remember/memory/knowledge/durable_evidence.py:58-69 |
| **The two typed failures this route's deletion and retention boundaries raise.** | `CodeObjectRetentionError`; `ComparisonReclamationError` | mcp/src/agents_remember/errors.py:180-190; mcp/src/agents_remember/errors.py:193-203 |
| **The cases that measure the whole journey, the convergence, the typed absences and the per-channel damage.** | `test_a_frozen_comparison_reopens_the_exact_content_after_restart_and_reclamation`; `test_an_exact_retry_converges_and_a_superseding_generation_names_its_predecessor`; `test_a_half_with_no_recorded_generation_freezes_as_typed_absence_never_as_inference`; `test_a_missing_or_damaged_retained_input_is_reported_per_channel` | mcp/tests/test_knowledge_review_comparison_generation.py:336-387; mcp/tests/test_knowledge_review_comparison_generation.py:713-764; mcp/tests/test_knowledge_review_comparison_generation.py:770-838; mcp/tests/test_knowledge_review_comparison_generation.py:558-600 |

## 260921-ICR-L6 The Statement Sides Get Their Own Owner, And A Present Value Stops Reading As An Absence

This route gained **one module and one seam**, and the leaf they belong to (`260921-ICR-L6`, primary
requirement ICR-R06@v1) is about a single rendering rule with a data contract behind it: *a knowledge
addition or removal renders the complete available statement alongside the explicit known-absent side*.
The per-file detail lives in the new sidecar; what belongs at this route's altitude is the boundary the
leaf drew and the one behavior it changed.

- **The statement-side projection now has an owner.** `application/review_statement_sides.py` owns
  what a statement side *is* — `side_content` (three outcomes: `absent`, `unresolved`, `present`+text),
  `side_conditions`, `read_side`, `field_changes` and `field_text` — where those five were private
  helpers inside `application/knowledge_review.py`. The rule the module exists for is that **a side's
  state is read, never inferred from an empty string**: "this snapshot selected no record" and "this
  snapshot holds the record but published no statement" are different facts about different snapshots,
  and an empty operand could not tell them apart. The mirror of the same move on the client is
  `dashboard/src/panels/review/KnowledgeStatements.tsx`, which owns how the two sides are *drawn*
  (including the one-sided diff and the available-content-with-reason path); the data contract and the
  rendering contract are now one file each.
- **The one behavior this leaf changed is a field row's value.** `ReviewFieldChange` declares that
  `None` on either value *is* the recorded fact that the field was absent on that side. The base
  adapter returned `None` for any `dict`, so a **changed structured field** — `provenance` is the
  shipped one — was served as `None` on both sides: an absence the snapshot does not hold, stated
  twice, on the one slot reserved for absence. Each side now carries `structured_value_text` of the
  value that side really holds, canonically rendered (sorted keys, one separator set), bracketed with
  the marker `<recorded as a structured value, rendered as compact JSON: …>` so the pane's rendering
  is distinguishable from an author's text, bounded by the row's own declared limit with a visible
  truncation, and never a wire change. `None` stays reserved for the two real absences.
- **The seam, recorded as the boundary rule it is.** The only change to `application/knowledge_review.py`
  is one import block and the four calls inside `_knowledge_pane`; the adapter kept its composition and
  grew no feature logic, which is the seam policy's "keep the adapter a delegator" rule applied. It is
  the **fourth** responsibility this adapter has handed out on this master line (after the candidate
  resolution, the source inventory and the record rendering), and it is the only one that leaves **no
  alias**: no module under `mcp/` imported the old private spellings, so `__all__` is unchanged. The
  adapter is now **831 lines**, down from the 1,126 the L5 section below records and the 888 this
  leaf's base carried.

The route-level consequence a reader should carry: **the review surface's pane-1 values are produced in
one place and consumed in one place.** A side that is not present can no longer become an empty operand
anywhere between the comparison and the DOM, and a field the comparison reports as *changed* can no
longer be displayed as two absences.

| Finding | Anchor | Source |
| --- | --- | --- |
| The statement-side projection's whole surface: the three-outcome side contract, the conditions reader, the comparison's own field roster, and the value reader that reserves `None` for absence. | `side_content`; `side_conditions`; `read_side`; `field_changes`; `field_text` | mcp/src/agents_remember/application/review_statement_sides.py:86-117; mcp/src/agents_remember/application/review_statement_sides.py:127-132; mcp/src/agents_remember/application/review_statement_sides.py:120-124; mcp/src/agents_remember/application/review_statement_sides.py:135-155; mcp/src/agents_remember/application/review_statement_sides.py:158-179 |
| **The structured-value projection: canonical, bracketed as the pane's own rendering, and bounded with a visible truncation.** | `structured_value_text`; `STRUCTURED_VALUE_LEAD`; `STRUCTURED_VALUE_TRUNCATION` | mcp/src/agents_remember/application/review_statement_sides.py:61-61; mcp/src/agents_remember/application/review_statement_sides.py:66-66; mcp/src/agents_remember/application/review_statement_sides.py:69-83 |
| **The contract that makes `None` mean absence — and therefore the reason a structured value is projected rather than nulled.** | `ReviewFieldChange`; `ReviewSideContent`; `ReviewSideState` |mcp/src/agents_remember/models/knowledge/review.py:507-518; mcp/src/agents_remember/models/knowledge/review.py:212-212; mcp/src/agents_remember/models/knowledge/review.py:234-259; mcp/src/agents_remember/models/knowledge/review.py:198-198|
| **The adapter's delegation: the import block and the four calls inside `_knowledge_pane`, with the composition unchanged.** | `side_content`; `side_conditions`; `field_changes`; `_knowledge_pane` | mcp/src/agents_remember/application/knowledge_review.py:1020-1043; mcp/src/agents_remember/application/knowledge_review.py:965-1017; mcp/src/agents_remember/application/knowledge_review.py:1000-1003 |
| **The production composition case: a changed structured field carries each side's own projection, the two differ, and each round-trips back to the stored authorship envelope.** | `test_a_structured_field_value_is_rendered_as_its_own_text_and_never_as_an_absence` | mcp/tests/test_knowledge_review_one_sided_statements.py:320-348 |
| The one-sided statement cases: the complete present-side statement beside the named absent side, with the comparison's own side-absence code. | `test_an_added_statement_renders_its_after_text_beside_a_named_absent_before`; `test_a_removed_statement_renders_its_before_text_beside_a_named_absent_after` | mcp/tests/test_knowledge_review_one_sided_statements.py:249-269; mcp/tests/test_knowledge_review_one_sided_statements.py:272-285 |
| The renderer that owns how the two sides are drawn, and the four branches it decides from declared state. | `KnowledgeStatements` | dashboard/src/panels/review/KnowledgeStatements.tsx:94-121 |

## 260921-ICR-L20 The Ordinary Publication Route Gets An Owner, And The Write Side Reaches The Read Side's Location

This route gained **one module and one seam**, and the leaf they belong to (`260921-ICR-L20`, primary
requirement ICR-R20@v1) is about a single question: where does a curator's *ordinary* run publish, and
how does it know the repository now holds what it wrote? The per-file detail lives in the new sidecar;
what belongs at this route's altitude is the boundary the leaf drew.

- **The publication decision now has an owner.** `application/knowledge_publication_route.py` owns
  exactly three: the declared location (resolved through `published_intent.published_dataset_path` for
  the enclosure's own coordination context — **one spelling**, so the location the writer reaches and
  the location a later read selects cannot drift apart), what the run admits is already there (derived
  from the `--baseline` bytes the run captured itself, never from a caller-typed identity), and the
  read-back through `resolve_published_intent` — the reader's own owner, in the same scope the write
  was made in. It **composes** what this route already had (`published_intent`, `knowledge_before_half`'s
  captured-dataset read, `knowledge_baseline_generation`'s `CapturedBaseline`) rather than
  reimplementing any of it, and it adds no store, no writer and no approval authority.
- **The seam is the same "keep the adapter a delegator" rule this route has applied twice before.**
  `cli/knowledge_ingest.py` owns the *selection* — which of the caller-named path, the declared
  location, or neither — and the route owns what the declared selection *means*; the CLI then delegates
  both renderings to a third file. The CLI is 692 lines where it was 541, and the 135-line report
  renderer left it for `cli/knowledge_ingest_report.py`, so the growth is R20's own decision surface
  (the destination, its three refusals, and the outcome-aware route line) rather than absorption.
- **An admission is not a publication, and this route's own detail says so.** An admission is made
  before the list is read, so a planning run and a batch that committed no entry both select a
  destination and publish nothing — which is why the module's `detail` stops at what was established
  and the *caller* completes the line from the run's report. Exit zero is not a publication claim, and
  `publicationRoute` / `publication` / `publishedIdentity` are the three fields that replaced it.
- **A consequence repair landed outside the leaf's own files.** `application/published_intent.py`'s
  module docstring and its `PUBLISHED_DATASET_NAME` comment said the ordinary write side *had to be*
  wired to this location and that doing so was ICR-R20's obligation; that is now past-tense ownership
  history beside the current route. The change is comment text only — the module's code is untouched —
  and it is recorded on that card as such.

The one route-level consequence a reader should carry: this repository's published knowledge has **one**
declared location, the ordinary write side publishes there through `--publish`, and the run states what
a *reader* will find there rather than leaving a successful exit to imply it.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The three decisions the new module owns: the declared location, the admission derived from the run's own captured baseline, and the read-back through the reader's owner.** | `declared_publication_location`; `admitted_destination`; `published_identity_read_back` | mcp/src/agents_remember/application/knowledge_publication_route.py:115-132; mcp/src/agents_remember/application/knowledge_publication_route.py:135-199; mcp/src/agents_remember/application/knowledge_publication_route.py:202-250 |
| **The three values those decisions travel as, and the exports that make them this module's public surface.** | `DeclaredPublicationLocation`; `DestinationAdmission`; `PublishedIdentityReadBack`; `__all__` | mcp/src/agents_remember/application/knowledge_publication_route.py:68-80; mcp/src/agents_remember/application/knowledge_publication_route.py:83-94; mcp/src/agents_remember/application/knowledge_publication_route.py:97-112; mcp/src/agents_remember/application/knowledge_publication_route.py:58-65 |
| The declaration this module resolves against, and the reader's owner the read-back goes through — both reused unchanged. | `published_dataset_path`; `resolve_published_intent`; `PUBLISHED_DATASET_NAME` | mcp/src/agents_remember/application/published_intent.py:160-160; mcp/src/agents_remember/application/published_intent.py:177-177; mcp/src/agents_remember/application/published_intent.py:283-299; mcp/src/agents_remember/application/published_intent.py:302-326; mcp/src/agents_remember/application/published_intent.py:147-147 |
| The context owner that decides *which* memory root the declared location is. | `contract_context` | mcp/src/agents_remember/worktrees/modules/context.py:38-77 |
| **The CLI side of the seam: the destination selection it now owns, its three refusals, and the route line it completes from the report.** | `_Destination`; `_destination_conflict`; `_selected_destination`; `_publication_route`; `_read_back` | mcp/src/agents_remember/cli/knowledge_ingest.py:288-299; mcp/src/agents_remember/cli/knowledge_ingest.py:321-357; mcp/src/agents_remember/cli/knowledge_ingest.py:307-318; mcp/src/agents_remember/cli/knowledge_ingest.py:402-414; mcp/src/agents_remember/cli/knowledge_ingest.py:622-635; mcp/src/agents_remember/cli/knowledge_ingest.py:434-447 |
| **The renderer that left the CLI, carrying the two facts the route added to the run's answer.** | `summary`; `payload` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:34-76; mcp/src/agents_remember/cli/knowledge_ingest_report.py:79-128 |
| The consequence repair this landing forced, stated on the card where the claims live. | `PUBLISHED_DATASET_NAME` | mcp/src/agents_remember/application/published_intent.py:177-177 |
| **The cases that drive the whole route through the shipped CLI over a production-shaped enclosure.** | `test_the_ordinary_route_publishes_to_the_declared_location_and_reads_it_back`; `test_an_explicit_update_replaces_the_dataset_the_run_forked_from` | mcp/tests/test_knowledge_ingest_publication_route.py:266-315; mcp/tests/test_knowledge_ingest_publication_route.py:406-487 |

## 260921-ICR-L18 The Comparison Baseline Gets An Owner, And The Half Is Filled Once

This route gained **one module and one boundary**, and the leaf they belong to (`260921-ICR-L18`,
primary requirement ICR-R18@v1) is about a single question: what is a comparison's before side when the
same path is both the baseline a run forks from and the dataset it publishes to? The per-file detail
lives in the new sidecar; what belongs at this route's altitude is the boundary the leaf drew.

- **The half's generation now has an owner.** `application/knowledge_baseline_generation.py` owns the
  durable generation record (`baseline-generation.json` beside the dataset), the four-state read of what
  the half holds (`absent` / `recorded` / `adopted` / `damaged`), the one first placement, and the
  deliberate rebase with recorded lineage. It **composes** the two modules this route already had —
  `knowledge_before_half.py` for the layout and the reads, `knowledge_first_generation.py` for the
  establishment — rather than reimplementing either, and it adds no store, journal or approval authority.
- **The half is filled once, and a standing baseline is replaced only by an explicit act.** A second
  successful run whose `--baseline` is the first run's *publication* places nothing: it names the
  generation the half holds, its dataset identity, and `--rebase-baseline`, which is the only input that
  may begin a new generation. Without that argument a differing baseline is kept as the comparison's
  original — which is what stops the deletion the review exists to show from being reported present on
  both sides with an empty delta.
- **The failure contract is an ordering, not a message.** A rebase publishes its **record first**, so the
  one window it can leave is the previous bytes beside a record that disagrees with them (the named
  `damaged` state) and never replacement bytes with no record (which would read `adopted` and relabel the
  replacement as the original). A first placement into an *empty* half deliberately keeps dataset-first,
  where a dataset without its record is truthfully an adopted baseline. A failure names the leg that
  refused **and** re-reads the half, because the write owner flushes the directory after the rename and a
  leg can therefore fail after its bytes landed.
- **The seam the leaf crossed, recorded as the boundary rule it is.** `cli/knowledge_ingest.py` gave up
  the placement machinery it used to own — `_place_fork_point`, `_establish_first_generation`,
  `_placeable_baseline` and its local `_CapturedBaseline` are gone from it, and its
  `_place_review_baseline` is now a pure seam — and is **541 lines** where it was 620. What stays in the
  CLI is the one question only the run's own report can answer: *whether* this run may fill anything at
  all. That is the seam policy's "keep the adapter a delegator" rule applied to a second responsibility,
  and it is the same split `260921-ICR-L1` applied to the review resolution.

The one route-level consequence a reader should carry: a comparison's before side is either the dataset
the leaf forked from or an explicit record of the generation it began from, it is never quietly
re-pointed behind the identity it already had, and a generation's id is **derived** from the facts its
record names, so a verifier can recompute it.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The generation owner: the record, the four-state read, the one first placement, and the deliberate rebase with lineage.** | `BaselineGeneration`; `read_standing_generation`; `place_original_baseline`; `rebase_comparison_baseline` | mcp/src/agents_remember/application/knowledge_baseline_generation.py:108-160; mcp/src/agents_remember/application/knowledge_baseline_generation.py:354-373; mcp/src/agents_remember/application/knowledge_baseline_generation.py:579-612; mcp/src/agents_remember/application/knowledge_baseline_generation.py:615-657 |
| **The one decision the module owns, and the four ordered answers behind it.** | `fill_admitted_before_half`; `_place_or_keep` | mcp/src/agents_remember/application/knowledge_baseline_generation.py:464-500; mcp/src/agents_remember/application/knowledge_baseline_generation.py:551-576 |
| **The two publication legs whose order is the failure contract, and the read-back that states the outcome.** | `_publish_generation`; `_publish_dataset_leg`; `_publish_record_leg`; `_failed_placement` | mcp/src/agents_remember/application/knowledge_baseline_generation.py:660-696; mcp/src/agents_remember/application/knowledge_baseline_generation.py:699-712; mcp/src/agents_remember/application/knowledge_baseline_generation.py:715-738; mcp/src/agents_remember/application/knowledge_baseline_generation.py:741-760 |
| **The derived rather than minted generation id a reader can recompute, and the lineage validator that refuses a record whose fields contradict each other.** | `generation_identity`; `_lineage_agrees_with_the_index` | mcp/src/agents_remember/application/knowledge_baseline_generation.py:319-348; mcp/src/agents_remember/application/knowledge_baseline_generation.py:140-160 |
| **The CLI side of the seam: the one gate that decides whether the run may fill the half, and the handoff that delegates what the half then is.** | `_placement_refusal`; `_place_review_baseline` | mcp/src/agents_remember/cli/knowledge_ingest.py:497-521; mcp/src/agents_remember/cli/knowledge_ingest.py:524-562 |
| The new argument, and the invocation refusal that fires before the contract is read. | `--rebase-baseline`; `run` | mcp/src/agents_remember/cli/knowledge_ingest.py:680-716 |
| The two sibling owners this module composes rather than reimplements. | `read_before_half`; `establish_first_generation` | mcp/src/agents_remember/application/knowledge_before_half.py:257-286; mcp/src/agents_remember/application/knowledge_first_generation.py:102-126 |
| The successful journey, the two retries and the deliberate rebase, driven through the shipped CLI on a real enclosure. | `test_a_second_successful_ingest_over_one_path_keeps_the_original_baseline`; `test_an_exact_retry_and_a_refused_changed_retry_keep_the_original_baseline`; `test_a_deliberate_rebase_begins_a_recorded_generation_with_explicit_lineage` | mcp/tests/test_knowledge_ingest_comparison_generation.py:153-209; mcp/tests/test_knowledge_ingest_comparison_generation.py:212-260; mcp/tests/test_knowledge_ingest_comparison_generation.py:263-326 |
| **Every way a placement refuses or loses a leg without losing the baseline, including the two flush windows that forced the "did not report success" wording.** | `test_a_half_that_records_no_generation_keeps_its_baseline_as_the_original`; `test_a_rebase_whose_record_leg_fails_leaves_the_original_baseline_in_place`; `test_a_rebase_whose_dataset_leg_fails_names_the_damage_it_left`; `test_an_obstructed_generation_record_path_is_damage_and_not_an_absent_record` | mcp/tests/test_knowledge_ingest_failure_windows.py:122-166; mcp/tests/test_knowledge_ingest_failure_windows.py:321-395; mcp/tests/test_knowledge_ingest_failure_windows.py:398-476; mcp/tests/test_knowledge_ingest_failure_windows.py:479-525 |

## 260921-ICR-L5 The Review's Before Half Becomes A Named Module, And A First Generation Becomes Establishable

This route gained **two modules and one seam**, and the leaf they belong to (`260921-ICR-L5`,
primary requirement ICR-R05@v1) is about a single question: what is a comparison's *before* side when
a repository has no earlier dataset to fork from? The per-file detail lives in the two new sidecars;
what belongs at this route's altitude is the boundary the leaf drew.

- **The before half now has an owner.** `application/knowledge_before_half.py` owns the layout one
  before side occupies (the dataset under the name the review resolves, plus `baseline-origin.json`
  beside it), the origin record that says *which* generation its dataset is, and the readers that
  decide what the half currently is — the four states `absent` / `identified` / `unidentified` /
  `damaged`, read from the half rather than assumed. Its three distinctions are the route's: absent is
  not empty, identified is not unidentified, and damaged is neither. Every read answers with a reason
  instead of raising, because a file that is not a dataset is an *input* fact for all three of its
  callers: the ingest admission reading a selected fork point, the ingest CLI inspecting the half it is
  about to fill, and the review refusing a comparison whose side cannot be opened.
- **A repository's first generation is established, not left absent — and the populated candidate is
  never its own origin.** `application/knowledge_first_generation.py` owns the act: the empty dataset
  is built by the shipped creation owner under the namespace and exact input pair the *committed
  candidate's own record* names (never re-derived, and never a copy of the candidate, which would
  display the first addition as present on both sides), the generation is identified by the origin
  record written beside it, and the whole half is built in a private stage and exposed by one
  `atomic_replace`, so a failure leaves either a complete identified half or nothing at all. A half
  that already holds a dataset is never rewritten, relabelled or replaced.
- **The seam the leaf crossed, recorded as the boundary rule it is.** The only change to
  `application/knowledge_review.py` is one import plus **two call sites** for
  `unreadable_half_refusal` — `compose_review` and the entry-list route — so a side that is present but
  cannot be read is a named refusal on both routes instead of an `apsw.NotADBError` raised out of the
  per-subject comparison. That is the seam policy's "keep the adapter a delegator" rule applied: the
  readers, the four states and the refusal all live in the new module, and what stays in the adapter is
  only *where* in the two routes the answer is stated. It is recorded here as a fact rather than as a
  claim of a general cleanup: this leaf did not move a responsibility **out** of the adapter. The
  over-rail condition that was true when this section was first written is **resolved by the merge**:
  the adapter was 1,281 lines at this leaf's base against the seam policy's 1,200-line hard rail, and
  leaf `260921-ICR-L1`'s landed extraction (which the sync brought into this candidate) moved the
  resolution out, leaving a 1,126-line delegating adapter — 1,113 lines at L1's own reading, before
  this leaf's 13 lines landed on top. The rail is met in the merged candidate; neither leaf's own pass
  could state that, because neither saw the other's change.

The two route-level consequences a reader should carry: the review's before side is now either the
dataset the leaf forked from or an explicit record of the generation it began, and neither is ever a
freshly empty dataset answering a *selected* input that was missing or corrupt — that case is the
shipped `selected_input_unavailable` refusal naming the path and the reason, checked on the resume path
as well as on the clone path.

| Finding | Anchor | Source |
| --- | --- | --- |
| The before half's layout, its origin record, and the four states a writer must consult before it writes anything. | `read_before_half`; `BeforeHalf`; `BaselineOrigin`; `unreadable_half_refusal` | mcp/src/agents_remember/application/knowledge_before_half.py:89-120; mcp/src/agents_remember/application/knowledge_before_half.py:123-137; mcp/src/agents_remember/application/knowledge_before_half.py:257-286; mcp/src/agents_remember/application/knowledge_before_half.py:347-377; mcp/src/agents_remember/application/knowledge_review.py:142-142 |
| The establishment: read the half first, take the admission from the committed candidate's own record, build privately, promote once. | `establish_first_generation`; `_candidate_admission`; `_expose_first_generation` | mcp/src/agents_remember/application/knowledge_first_generation.py:102-126; mcp/src/agents_remember/application/knowledge_first_generation.py:157-187; mcp/src/agents_remember/application/knowledge_first_generation.py:205-228 |
| **The two call sites this leaf added to the adapter, and the one refusal they state.** | `compose_review`; `list_knowledge_review_entries`; `unreadable_half_refusal` | mcp/src/agents_remember/application/knowledge_review.py:256-317; mcp/src/agents_remember/application/knowledge_review.py:334-574; mcp/src/agents_remember/application/knowledge_review.py:298-298; mcp/src/agents_remember/application/knowledge_before_half.py:347-377 |
| The admission's own check of a selected baseline, which reads it on every run, resume included. | `_selected_baseline`; `_admitted_candidate`; `selected_input_unavailable_refusal` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1619-1640; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1561-1616; mcp/src/agents_remember/memory/knowledge/refusals.py:882-901 |
| The CLI's two filling paths, the one gate they share, and the cold-start branch that reaches the establishment. | `_place_review_baseline`; `_place_or_keep`; `_establish_first_generation`; `_placement_refusal` | mcp/src/agents_remember/cli/knowledge_ingest.py:497-521; mcp/src/agents_remember/cli/knowledge_ingest.py:524-562; mcp/src/agents_remember/application/knowledge_baseline_generation.py:551-576; mcp/src/agents_remember/application/knowledge_baseline_generation.py:503-516 |
| The cases that measure the operation at the CLI, and one that measures the review surface's before half. | `test_a_cold_start_cli_run_establishes_an_identified_first_generation_before_half`; `test_a_lost_or_corrupt_selected_baseline_is_refused_by_name_and_establishes_nothing`; `test_a_before_side_that_is_present_but_unreadable_refuses_by_name` | mcp/tests/test_knowledge_curator_ingest_list.py:2086-2151; mcp/tests/test_knowledge_review_resolution_and_route.py:134-172; mcp/tests/test_knowledge_curator_ingest_list.py:1899-2013 |

## 260915-KS-L41 The View Front Door: One Seed Frontier, Membership From Its Own Table, And A Pair That Is Completed

This route owns the two application modules a knowledge *read* passes through, and this leaf changed
both. `knowledge_view_render.py` is where a view decides what it selects, and the change here is that
**the path seed is now one frontier computed once per reader and applied by every view that can be
seeded**. `_seed_revisions` resolves the request's optional `source_path` to the revisions realized
there and keeps the two honest answers apart — `None` means "no seed was named" and an empty set means
"a path was named and it selects nothing" — so a path recorded nowhere returns no rows instead of
falling back to everything. `_seed_memo` attaches that answer to the **reader object** (under
`_SEED_MEMO_ATTRIBUTE`, so it lives exactly as long as the reader the seam already opened and closed),
`_seeded_realizations` is the memoised front door, and `_seed_selects` is the single predicate whose
`None` selects everything and whose set selects only its members. Two derived frontiers follow from it:
`_seeded_family_revisions` selects a family **through the recorded membership** naming a revision the
path realizes — a family is not a file, so no path can be matched against a family directly — while
`_selected_invariant_revisions` returns the revision frontier as a set so `source_context` can apply it
to both its registered realizations and the authored decisions attached to those revisions. That last
point is what closed the measured defect: `_source_context_candidates` ignored `source_path` entirely,
so a real path and a path that was never recorded both returned every realization in the namespace.

The second change is that **family membership is read from the table membership is stored in**.
`_family_members` now calls `reader.family_member_rows()` — the port method `StoreViewReader` answers
from the dedicated `family_member` table — instead of `reader.rows("family_member")`. Membership is a
recorded generation-1 entity and is **not** duplicated into the `knowledge_record`/`record_revision`
envelope that generic read consults, so the named-kind read returned no members on a dataset that holds
them and the family view reported a joint guarantee, no members, no implementation locations and
`completeWithinDeclaredScope: true`. Both membership-derived row shapes now state their kind in the
family view's own vocabulary: `fact_kind="member"`, the closed set `FamilyRow` declares, rather than
`"family_member"` or the source-context view's `"registered_realization"`. The traversal a caller
measures is therefore `subject.revision_id` plus `fact_kind`, which is how the acceptance check reads one
path to the governing family, to that family's other member, and to that member's own code location.

The third change closes the context-construction defect at the boundary between this route and the mount:
the `(repository_root, code_tree_id)` pair a read context may carry is now **completed or not named at
all**. `_source_resolution` returns a caller-named root with that root's own current tree, uses the
mount's workspace default only when the caller names no repository *and* a tree can actually be resolved
from it, and otherwise names neither half; `_current_code_tree` shells `git -C <root> rev-parse HEAD^{tree}`
under a declared timeout and validates the answer against a tree-id pattern, returning `None` rather than
a guess. A context carrying one half of the pair is refused by its own model, so the old behaviour —
defaulting `repository_root` from the mount and leaving `code_tree_id` as the caller supplied it — turned
an ordinary minimal `knowledge_read` into a raised validation error out of the mounted tool. Two
properties the route already owned are preserved deliberately: the exact-invariant read still returns the
requested statement and only the realizations the same selection covers, and an ordering input outside
the four admitted ones still refuses rather than defaulting.

**Open question the review owns, recorded rather than settled.** A path-seeded family read filters
members and locations to the seed's frontier, while the unseeded / `familyRevisionId` read shows the
family's complete membership. Both are deliberate — a seeded read answers "what does this file's family
hold", an exact-revision read answers "what does this family hold" — and the review is asked to confirm
that split rather than read either as the other.

## 260915-CAPS-L4 The Capsule And Skill-Resource Application Boundary

This route gained one package, `skill_resources/`, which is the application half of the AR MCP surface
for **role capsules** and **reusable skills**. It carries two deliberately separate surfaces, and the
separation is the contract:

- **The capsule operation** (`capsule.py`, `operation.py`) is one narrow read-only call: admitted task
  binding in, typed capsule or a refusal-with-remedy out. It resolves the worktree enclosure, derives
  the seat from the task document's **own altitude** and validates the caller's `role` string against
  it — so the role argument is an input to a check and never the source of the seat — projects the task
  context through `application/task_projection/`, admits exactly the source files the canonical
  composition manifest routes, and compiles through `application/role_capsules/`. It reads no
  caller-named path and writes nothing.
- **The skills transport's reading half** (`catalog.py`, `frontmatter.py`, `provider.py`) builds the
  host discovery registry and serves the bytes one `skill://` resource addresses. Discovery and
  delivery are kept apart: a listing hands out metadata and cannot reach a body, one selected file is
  re-read on demand, containment inside the skill's own directory is proven **before** any byte is
  read, and the bytes are re-checked against the revision the catalog recorded.

Two cross-route facts a reader of this route should carry:

- **A refusal is a value, not an exception.** `CapsuleCompilationError` and `TaskProjectionSourceError`
  carry a stable status, an operator-legible detail and a named remedy, and `CapsuleCompileOutcome`
  keeps the binding it established in **both** shapes, so an operator always sees which seat and which
  revision the operation addressed.
- **The corpus is the packaged skills copy.** The default tree is the package's own generated
  `package_data/runtime/skills/` copy rather than the canonical root `skills/` tree, because publishing
  the packaged copy is what makes a served revision reproducible. A corpus root, its manifest and its
  publishing `origin` are admitted together.

The route's ordinary boundary holds unchanged: no MCP or protocol types are read at this layer, and the
`mcp` registration layer owns turning these values into tools and resources.

| Finding | Anchor | Source |
| --- | --- | --- |
| The capsule operation's four refusal-capable steps, each returning a value rather than raising. | `compile_task_capsule`; `CapsuleCompileOutcome` | mcp/src/agents_remember/application/skill_resources/capsule.py:111-153; mcp/src/agents_remember/application/skill_resources/capsule.py:205-236 |
| The seat is derived from the task document and the declared role is validated against it. | `_admitted_facts` | mcp/src/agents_remember/application/skill_resources/capsule.py:292-350 |
| Discovery is separated from delivery: the listing carries no body and one read is re-checked. | `build_skill_catalog`; `read_served_file` | mcp/src/agents_remember/application/skill_resources/catalog.py:75-95; mcp/src/agents_remember/application/skill_resources/catalog.py:117-148 |
| The served tree is the packaged runtime skills copy, and a corpus travels with its origin. | `shipped_skill_tree`; `shipped_composition_corpus` | mcp/src/agents_remember/application/skill_resources/provider.py:39-47; mcp/src/agents_remember/application/skill_resources/provider.py:50-63 |
| The application entry points the registration layer calls. | `role_capsule_compile_tool`; `skill_catalog_list_tool`; `skill_catalog_read_tool` | mcp/src/agents_remember/application/skill_resources/operation.py:68-89; mcp/src/agents_remember/application/skill_resources/operation.py:92-95; mcp/src/agents_remember/application/skill_resources/operation.py:98-107 |

## IAS Per-Contract Activation Application Boundary

The application layer composes selecting operations around one per-contract activation authority.
An atomic master is not exposed merely because its series contract exists: activation becomes
`reconciling`, that contract's exact code/external-memory bases are synchronized, and only an
exact-current result becomes `active`. The record is keyed by the canonical series contract, not the
protected source pair, so two atomic masters commanded by one sprint and sharing its code/memory
source branches hold independent records: the only activation waiting reason is
`atomic-series-reconciling` for a contract's own in-flight reconciliation, and a foreign master is
never a reason to wait. A retained conflict returns agent-owned continue/cancel guidance and leaves
the integration lock free between calls.

Status observes the stable enclosure-root sync journal independently from task-document health.
Application adapters translate failures into bounded tool results; they do not recreate the journal
from task prose, queue rows, or ambient Git. Task-document mutation remains an upstream application
flow: it publishes canonical truth, invalidates projections for semantic/readiness mutations, and never asks queue or
activation state for permission.

## 260831-LOCR-L37 The Stop-Only Application Boundary

This route gained one application entry point and no authority. `worktree_tools.py::worktree_pause_tool`
admits the configured contract through the shared gate (projecting a refusal under the operation name
`worktree_pause`), builds the same typed `WorktreeArgs` the other contract-addressed entry points build
— the contract path plus `config.orchestration.gate_policy` — and delegates to
`git_worktree_manager.pause_result`. It performs no Git, moves no ref, creates no commit, lands
nothing, writes no ledger row, and runs no auto-land seat hook, because nothing is retired and nothing
is finished.

That shape is the boundary. Every other mutating entry point on this route hands work to a worktree
owner that may publish; this one hands work to a route whose publication modules are structurally
unreachable (see `worktrees/modules/pause.py.md` and `mcp/tests/test_pause_is_not_publication.py`). The
application layer therefore does not decide whether to publish — there is no such decision on this
path to make.

`worktree_pause_tool` is the counterpart of `worktree_checkpoint_landing_tool` on the same file and the
opposite side of it: the checkpoint is the explicitly requested **publication** of an unfinished
master's accumulated line, and the pause is the stop that publishes nothing. Two entry points, two
registered tools, neither reachable from the other.

## CCR-R25 Actionable Refusal Boundary

`worktree_tools.py` routes the existing `RouteReviewError` through one pure refusal projector at
start/admission and direct closeout. With an exact contract the response carries only the
contract-bound `task_doc` operation and arguments; the required review payload remains caller input.
Certification admission preserves every original finding while promoting a route-review finding
through the same projector. These application paths report observed gate outcomes and do not create
reviews, mutate task documents, or provide a fallback authority.

## Current Structural Application Boundary

`application/structural/` translates ambient caller intent and document+role targets into authorized
plane-owned dispatch, messaging, seat management, and gate mutations. Runtime correlations remain
inside the transaction. Ordinary messages are replacement-aware; the initial dispatch brief is the
sole exact-pinned exception. Failed briefing retires a child only when the matching generation is
positively proven unbriefed; unreadable, missing, or contradictory evidence refuses reconciliation
without cleanup. Since 260821-ARSPAWN-L1
`dispatch_agent` resolves the caller by kind (plane seat vs ambient launcher resolved from the
process environment), keeps the plane structural path unchanged, and records caller-kind provenance
(`caller_kind` `plane`/`ambient`) through the `application/terminal_tools.py` spawn primitive onto
the catalog row and the `spawnedByKind` wire field.

ARSPAWN-L2 keeps that public surface but makes its seat transaction idempotent. The structural
child route now composes `dispatch_transaction.py` with the serving-owned per-seat lock and durable
brief evidence. Ordinary messages derive parent/child addresses without requiring a live occupant;
private occupant ids remain an execution detail and are never persisted into a complete structural
destination.

## Durable Lifecycle Application Boundary — detached worker removed

This section previously described `lifecycle/lifecycle_operation_worker.py` as the detached
application owner for closeout and integration, with its own packaged CLI composition root, the
explicit `lifecycle-operation` execution mode, and heartbeat/progress/terminal publication. That
module was deleted by the de-entanglement cut (commit `173bb01e`, "delete the detached lifecycle
worker and drive every fixture on the synchronous path"): the MCP tools now drive
`worktree_closeout_apply` and `worktree_integrate` in-process, and the record advance moved into
`worktrees/integration/lifecycle/lifecycle_operation_store.py`. The `application/closeout_door.py`
door adapter and the `application/lifecycle/legacy_operation_tool.py`,
`lifecycle_enclosure_tools.py` and `lifecycle_status_wait.py` entry points were deleted by the same
cut. There is no detached worker composition root or worker-execution mode on this route.

## 260915-CAPS-L15 The Launch Compiler Connects This Route To Production

**Route meaning changed: this route gained the member that makes the capsule chain exist in
production.** Before it, the compiler (L2), the admission/MCP surface (L4), the Codex carrier (L5) and
the eve carrier (L7) were each individually proven and **no production launch point supplied a capsule
to any session** — a dispatched seat and a free agent both launched with no instructions, and every
green test hand-supplied the intermediate value.

`application/role_capsules/launch.py` is the new member. It adds **no second routing rule**: a
task-attached seat goes through `compile_task_capsule` — the same operation the registered
`role_capsule_compile` MCP tool answers — and a taskless seat through `compile_admitted_capsule` with
the source set built by `routed_admission_for`, the same manifest rule `routed_admission_request` uses.
The operation is `orientation`, the registered operation's own default. It is reached from the
`serving`-rank launch points through the `LaunchCapsuleResolver` port (`serving/launch_capsule.py`),
filled at the composition root, because `serving` (17) may not import `application` (21) — the same
precedent `register_inbox_execution_evidence` set. The edge count between those layers is **0** and
stays 0.

Three facts a reader of this route needs:

1. **The free agent's absent task plane is minted here, once.** `FreeAgentSeatAdmission` is the only
   producer of a taskless `CapsuleAdmittedFacts`; the frozen DTO has no typed absence (all four identity
   fields are non-blank strings), so the absence is *named* — `task_reference = "free-agent:<role>"` —
   and deliberately does not parse as a task reference, so the task layer's own parser refuses it
   loudly rather than resolving it to a document that does not exist. The digest covers the admission
   the launch actually performed. This is convention **(B)** from the leaf's ruling; the typed-absence
   end state **(A)** is a successor obligation carried to the final-verification ledger, not done here.
2. **D13's second half lives in `skill_resources/capsule.py`.** The repair reads the code repository
   root out of the enclosure contract the caller already names (`_declared_repository_root`) — the
   registered tool exposes no repository field, so the contract is the authority rather than a second
   value smuggled in beside it — and carries the same resolved root onto `AdmittedEnclosure` so the task
   projection resolves against it instead of re-deriving (or failing to derive) one of its own. Without
   that second half the projection refused with `projection-binding-unresolved` in any tree whose
   repository does not sit directly under the workspace.
3. **`skill_resources` gained a seat-addressed routing entry point**, `CapsuleSeatAddress` +
   `routed_admission_for`, for a caller that has no task document and therefore no
   `CapsuleCompileRequest` to hand over — and must still use the one routing rule.

| Finding | Anchor | Source |
| --- | --- | --- |
| The launch compiler: the entry point the serving port is bound to, its named refusals, and the two admittances. | `compile_launch_capsule`; `_compile_admitted_task`; `_compile_free_agent` | mcp/src/agents_remember/application/role_capsules/launch.py:273-294; mcp/src/agents_remember/application/role_capsules/launch.py:297-359; mcp/src/agents_remember/application/role_capsules/launch.py:407-447 |
| The eve carrier path, which materializes L7's carrier and reads the admitted workspace back out of it. | `_compile_eve_task` | mcp/src/agents_remember/application/role_capsules/launch.py:362-404 |
| The free agent's named absence and its own content address; the only producer of a taskless admitted-facts value. | `FreeAgentSeatAdmission`; `free_agent_seat_admission`; `workspace_identity` | mcp/src/agents_remember/application/role_capsules/launch.py:125-196; mcp/src/agents_remember/application/role_capsules/launch.py:199-230; mcp/src/agents_remember/application/role_capsules/launch.py:233-246 |
| D13's dual repair: the root read out of the named contract, and the same root carried onto the projection request. | `_declared_repository_root`; `AdmittedEnclosure.code_repository_root`; `_projection`; `_enclosure` | mcp/src/agents_remember/application/skill_resources/capsule.py:364-416; mcp/src/agents_remember/application/skill_resources/capsule.py:419-443; mcp/src/agents_remember/application/skill_resources/capsule.py:275-289; mcp/src/agents_remember/application/skill_resources/capsule.py:262-289 |
| The seat-addressed routing rule and its address type, for a caller with no task document. | `CapsuleSeatAddress`; `routed_admission_for`; `routed_admission_request` | mcp/src/agents_remember/application/skill_resources/capsule.py:173-183; mcp/src/agents_remember/application/skill_resources/capsule.py:491-512; mcp/src/agents_remember/application/skill_resources/capsule.py:515-554 |
| The declared exports that make the new names this route's public surface. | `CapsuleSeatAddress`; `routed_admission_for` | mcp/src/agents_remember/application/skill_resources/__init__.py:20-31; mcp/src/agents_remember/application/skill_resources/__init__.py:66-95 |
| The registered MCP boundary the repair had to make usable, and the case that fails if the declared schema loses the field the resolution depends on. | `role_capsule_compile_tool`; `test_the_registered_capsule_operation_resolves_a_repository_through_its_schema` | mcp/src/agents_remember/application/skill_resources/operation.py:68-89; mcp/tests/test_capsule_launch_wiring.py:1019-1064 |
| The two production launch points that reach this member through the port. | `_spawn_launch_request`; `_open_terminal_response`; `resolve_launch_capsule` | mcp/src/agents_remember/application/terminal_tools.py:740-784; mcp/src/agents_remember/serving/_app_terminal_routes.py:239-348; mcp/src/agents_remember/serving/launch_capsule.py:275-314 |

## 260915-CAPS-L20 The Gate A Dead Declaration Now Reaches

This route's `memory_quality/controller.py` gained one consumer this leaf, and the consumer is the
point of the change rather than a detail of it.

`_attach_curator_checklist` now calls the memory-quality route's new
`check_governing_overview_resolution(scope.onboarding_root)` and publishes its summary on the
operation **response** under `governingOverviewResolution`: five counters, the findings, and the
observations. The findings then join the gated set through
`repair_findings.extend(row.to_dict() for row in governing_overviews.findings)` — `.findings`, never
`.observations` — so a dead governing declaration reaches the curator's completion loop instead of
being reported clean. That is `D3`/`D16`'s actual defect: the product checked that a source has a card
and never that the card's declared route resolves.

Two placements in the published summary are deliberate. It is attached to `response` rather than to
`payload`, because `response` is composed from `**payload` before this function runs and a key added
to `payload` here would never be published. And it stays out of `response["checks"]`, because that
mapping is the closed `AVAILABLE_CHECKS` population the certification catalog is validated against,
so a key outside that population would be a catalog item with no planned identity.

**The reach, stated with its condition.** The consumer that binds today is the curator's completion
loop: the full contract-scoped operation — `publish_curator_report` requires no `checks` subset —
publishes the count the curator iterates against. The closeout-admission consumer is the designed one
and sits behind `D32`: the readiness comparison lives inside `require_current_curator_coherence`,
which the checklist consults only after the raw status reaches `ready-for-closeout`, and no leaf on
this master has ever reached it. Both statements are true; stating only the first would overstate
today's reach and stating only the second would understate the fix.

## Purpose

`application/` owns operation-level MCP composition. Application entry points translate
trusted MCP runtime config plus typed tool arguments into package service calls
and JSON-compatible payload dictionaries. Domain placement follows what a tool
operates on: `task_reopen_tool` cit:([`task_reopen_tool`], mcp/src/agents_remember/application/task_docs/task_reopen.py:20-41) sits beside the task_doc application entry point because it
reopens a task, while worktree_tools keeps only genuine worktree operations (its
abandon now also ends the ambient lifecycle it anchors).

## Hot Path Summary

`worktree_tool_requests.py` carries only code/memory commit messages and landed commits. `worktree_tools.py` forwards that pair unchanged; `memory_tools.py` exposes baseline/carryover cache observations without a ledger commit argument. Adapters do not recreate retired guards or synthesize a third output.

## 260915-CAPS-L2 Role-Capsule Admission And Compile Boundary

`mcp/src/agents_remember/application/role_capsules/` is a **new package** on this route and the
only role-capsule code that touches the filesystem. It exists because the pure compiler in
`models/role_capsules/` deliberately opens no file: reading sources, resolving a confined root, and
turning a refusal into a value all belong here.

`compile_admitted_capsule(binding, request, projection=None)` is the whole surface. It admits via
`admit_capsule_sources`, recovers the manifest bytes from the admitted set, and calls the pure
compiler — converting a typed `CapsuleCompilationError` into a returned outcome rather than letting
it escape. `CapsuleCompilationOutcome` is **exactly one** of a compiled capsule or a refusal (its
`__post_init__` raises if neither or both are present), carries the manifest in both shapes, and
reports `semantic_digest` as `None` for a refusal because a refusal has no identity. A source tree
that cannot be read at all produces the same refusal shape as a selection defect, carrying the
admitted-facts half of the manifest, since those facts were true regardless.

Admission itself is **explicit rather than eager**: the caller names every path it wants read, and
the boundary proves containment **before any byte is read**, so a traversal attempt fails without
the root being probed outside itself. Requested paths are root-relative POSIX paths; the manifest
path is read but is not an instruction block, so it carries the reserved metadata identity
`meta:composition-manifest` and is composed into no capsule. The admitted order is fixed — manifest,
then `core`/`role`/`operation`/`specialization`, each alphabetical — so two admissions of one tree
are directly comparable.

**Decoding is not this layer's job.** This boundary records each source's bytes and their content
digest; the value layer (`models/role_capsules/sources.py`) is where a source is decoded and where
**`source-not-utf8`** is raised. Do not look for that code here, and do not add lenient decoding to
this boundary — a source that does not decode is a defect, not a file to be coerced.

The admitted set is proven against the locked plan by `models/role_capsules/source_set.py`, which
also requires **every declared skill's root file** to have been admitted — a skill reference without
admitted bytes has a fictional revision.

This package is also the **L3 seam for the later task projection**: it accepts any
`CapsuleTaskProjectionSource` and passes it through untouched. Task state is never read, rendered,
or rewritten at this boundary; verifying a projection's bytes against its declared digest happens
inside the pure compiler. **That projection is the task-context projection, not the closeout-queue
projection** — the two share a word and no owner, and the section below states the distinction.

## 260915-CAPS-L3 Task-Context Projection Boundary

`mcp/src/agents_remember/application/task_projection/` is a **new package** on this route and the
implementation of the seam the L2 boundary above only declared. It computes the smallest complete
task projection the bound role and operation need, from authority that already exists, and returns a
value: ten modules, 2,431 lines, and no writer anywhere in the package.

**Naming disambiguation — "projection" names two unrelated things in this repository.** This
package's *projection* is a **task-context projection**: one task document, its declared requirement
packets and its admitted worktree/branch binding, rendered as model-visible Markdown. The
**closeout-queue projection** is a different owner entirely — `tasks/document_refs.py::projection_sprints_affected_by_master`
and the closeout-queue writers compute *which sprints a write affects* so the disposable queue can
be rebuilt. The two share the word and nothing else: different inputs, different outputs, different
consumers, no shared type, no call path in either direction. A card or a reader that conflates them
is wrong; the new file-level cards under this package each carry the same disambiguation.

The package's whole shape follows from one requirement — the projection is **either complete or
refused**. There is no partial projection, no fallback branch, no nearest task match and no silent
scope widening. The sixteen `projection-*` refusal codes are declared by
`agents_remember.errors.TaskProjectionSourceError`, which subclasses `AgentsRememberError` directly
rather than the capsule family, because a projection failure happens *before* any capsule
compilation.

**The consumer contract (L4/L5/L7).** One resolution per admitted binding, one projection per
operation: `resolve_task_projection_scope` binds the admitted facts against the enclosure contract,
the coordination context and the task topology; `project_task_context` assembles the value;
`task_context_of` converts it into the compiler's frozen `CapsuleTaskContext`; and
`TaskProjectionSource` is that same thing behind the compiler's one-method protocol. The delivered
`markdown` carries its own binding block and revision, so an adapter delivers it verbatim instead of
re-rendering or re-ordering it.

**Two consumer obligations, both admissions rather than guesses.** The admitted task reference must
be the task layer's canonical key, `"<repository>/<path-under-tasks/<repository>>"`. A requirement
the bound task document declares as **exact text** needs an admitted, version-addressed packet
location — and the preferred route is to declare the packet on the task document as an
`approved-requirement-packet` reference, which the task-intent owner verifies and which needs no
consumer input. That typed route is the **standardized policy** (owner ruling of 2026-09-16T10:15 on
the L3 leaf document): requiring every consumer to supply a packet location would spread task
knowledge into transport adapters and turn a missing packet into a runtime surprise.

**The read plan is the requirement, not an optimisation.** `selection._READ_ALTITUDES` is a total
table over `(own altitude, parent bucket)` with no default branch, and one rule is load-bearing: a
leaf-altitude seat **never** reads a sprint-altitude ancestor. A leaf reads its own document plus
its immediate parent when that parent is a master; when the parent is a sprint, the leaf reads its
own document only and the sprint arrives as an expansion reference carrying its entry count. Only the
bound document's own decisions are injected, so "the smallest complete task projection" cannot
become "the whole series history".

**Nothing is clipped and nothing is silently dropped.** Every obligation, negative constraint and
failure obligation is carried verbatim from the packet that declares it — no length budget exists
anywhere in the package — and material deliberately not injected is named under "Expansion
references", so "referenced" is a visible decision with a link rather than an omission.

**Read-only is asserted, not claimed.** Nothing in the package imports a writer, a transport or a
task-JSON reader; a structural AST case walks every module and fails on any of them, and the live
probe digests the real task tree before and after both a successful projection and every refusal,
byte-identical. No cache write, status stamp or "helpful" repair belongs on this read path.

The Knowledge Substrate master is **not** a dependency: a later knowledge view plugs in through the
`TaskKnowledgeExpansionSource` protocol, no implementation ships, and with no source the projection
reports the channel as unadmitted instead of quietly omitting it.

## Detailed Route Context

This route owns the single closed configured-contract admission result/projector and the task-addressed application adapters over lifecycle location, controls, adoption, direct landing, and degraded status. The legacy-repair adapter and the closeout-door adapter were deleted as capabilities by the de-entanglement cut.

For 260731-EFA-L21, `runtime/startup.py` is the trusted MCP declaration boundary: it declares MCP
execution before loading runtime configuration. Dashboard foreground, daemon, and reload-worker
entry paths make the corresponding dashboard declaration in their CLI route. Undeclared linked
worktree entry paths therefore cannot inherit the deployed coordination root.

The current operation surfaces include `context_packet.py` and `coordination_tools.py` for context
assembly and resolver calls; `memory_scope.py` plus `memory_quality/controller.py` and
`memory_quality/runs.py` for canonical quality authority, execution, and bounded run retention;
`memory_tools.py` for drift, citations, route-index, init, baseline, and
carryover; `gate_tools.py` and `hosted_readiness.py` for gate/readiness operations;
`lifecycle/lifecycle_tools.py`, `operator_inbox_tools.py`, and `orchestration_tools.py` for lifecycle, inbox,
and orchestration operations; `runtime/startup.py` and `terminal_tools.py` for startup and terminal
operations; `provider_tools.py` for provider operations; `worktree_tools.py` for worktree operations;
`benchmark_tools.py`, `runtime/install.py`, and `runtime/skills.py` for benchmark, install, and skill
surfaces; `task_docs/task_doc_tools.py` for JSON-primary task-document authoring; `tool_response.py` for response
completion; `worktree_status.py` for status packets; and `read_files.py` for paired source/onboarding
reads. Route-index refresh still resolves context first and forwards repository/storage authority to
the deterministic builder.
Context and worktree application entry points forward `parent_task`/`leaf_id` into the source resolver, and task-doc
authoring writes `seriesContractPath` plus `enclosures[]` instead of the retired `contractPath`.

Contract-scoped memory quality is the curator's pre-closeout worklist over the leaf's dirty code and
memory worktrees. `memory_scope.py` resolves and freezes the exact leaf authority, code/onboarding
roots, and temporary code-base provenance; `memory_quality/controller.py` uses that identity for
both sync and bounded async execution. A bare repository-scoped call still targets official memory
and supplies no invented provenance; commit-derived verification stamps remain closeout-owned.
The `memory_quality/` package is a behavior-preserving ownership split of the former flat
controller and run-registry modules; it creates no facade, compatibility reader, or second quality
API.
**260707-HFX2-L11**: `worktree_tools.py`'s `worktree_integrate_tool`/
`lifecycle_finalize_task_tool` now compose completion-edge landing — after a successful non-dry-run
edge, when `config.retirement.auto_land_on_integration`/`auto_land_on_finalize` is on (both default
ON), `_auto_land_completed_seats` resolves the qualified leaf key and calls
`serving.landing.land_seats_for_leaf` for the edge's own role set (worker/reviewer at integrate,
manager/reviewer at finalize). Matching sessions are marked `status:"landed"` with provenance and
returned as `autoLandedSeats`; tmux sessions are not killed, so the dashboard can show an inspectable
landed archive. The helper body remains best-effort (`except Exception: return []`) so a catalog
fault can never fail an already-succeeded edge — landing is archive bookkeeping riding the edge,
never a gate on it.

## Parameter Objects: This Route Owns The Concepts

260731-EFA-L2 armed `PLR0913` (≤5 arguments) at full strength with no ignore and no `max-args`
override, and this route absorbed a large share of the resulting refactor. An application entry point's arguments
are now named concepts, defined **beside the application entry point that takes them** and imported by the
payload builder and the tool declaration:

| Module | Selected types it defines |
| --- | --- |
| `task_docs/task_ref.py` | `TaskRef` — the repo plus whichever locator a caller holds; shared by `resolve_context_tool`, `worktree_attach_tool`, `worktree_status_tool`. |
| `worktree_tool_requests.py` | `TaskIdentity`, `TaskBases`, `StartExecution`, `OperationControlRequest`, `CloseoutCommitMessages`, `CloseoutApproval`, `FinalizeTaskDocs` (+ `DEFAULT_TASK_BASES`, `DEFAULT_START_EXECUTION`, `PREVIEW_ONLY`, `NO_TASK_DOCS`). `worktree_tools.py` consumes these types and owns operation composition. |
| `memory_tools.py` | `MemoryBranches`, `CarryoverSelection`, `CarryoverCommitMessages` (+ their defaults). |
| `task_docs/task_doc_tools.py` | `TaskDocTarget`, `TaskDocEdit` (+ `NO_EDIT`). |
| `benchmark_tools.py` | `BenchmarkSelection`, `BenchmarkPreparation`, `CodexBenchmarkRun` (+ `ALL_CASES`, `DEFAULT_PREPARATION`, `DEFAULT_RUN`). |
| `provider_tools.py` | `ProviderQueryScope`, `GrepaiRepoScope`, `GrepaiSearchQuery`, `GrepaiTraceQuery` (+ `WORKSPACE_QUERY_SCOPE`, `ALL_INDEXED_REPOS`). |
| `runtime/` | Groups MCP startup, typed runtime-install delegation, and skill deployment without a package facade. |

This is a selected, not exhaustive, inventory. Other direct application-level request/target objects
are defined beside the gate, hosted-readiness, lifecycle, operator-inbox, orchestration, server-startup,
terminal, tool-response, and worktree-status entry points.

Two splits are load-bearing rather than cosmetic and must survive future edits: `CloseoutApproval`
stays separate from `CloseoutCommitMessages` (folding them would let a dry run read as an approved
apply), and `intent_note` stays outside `CarryoverSelection` (it is the approval, not part of what
is carried).

Application-only packing types stop at this boundary. Most MCP declarations keep flat published
signatures and build those objects in their bodies. Memory quality is the deliberate exception: its
strict discriminated request is itself the public contract, so FastMCP publishes one nested
sync/start/poll object and Pydantic rejects mixed mode fields.

## Route Model

- MCP transport lives in `mcp/registration/` (the `@server.tool()` declarations) and the
  `mcp/tools/` package (the payload builders); `mcp/server.py` is process wiring only.
- Application entry points should remain typed operation facades, not generic command
  runners.
- Domain behavior belongs in service modules such as `providers`,
  `worktrees`, `memory_quality`, `memory`, `benchmarks`, and `install`.
- Response shape validation happens after application entry point return through the model
  registry (`models/tools/tool_registry.py`), applied by the `mcp/tools/` payload
  builders. That is the LAST line of defence, not the only one: when a collaborator
  already returns a model or a `TypedDict`, an application entry point passes it through rather than
  re-validating an untyped dump (260731-EFA-L4) — a `ValidationError` raised at
  `model_validate` inside an application entry point lands on the tool path, where nothing catches it,
  whereas a type mismatch at the producer is a pyright error before the code ships.
- A vocabulary an application entry point decides is declared in the owning model/module and imported
  by the consumer, not retyped there (260731-EFA-L4; `FileReadStatus` is the worked example).
  cit:(["FileReadStatus = Literal["], mcp/src/agents_remember/models/read_files.py:20-32; mcp/src/agents_remember/application/read_files.py:44-46)

## Invariants And Boundaries

- Application entry points resolve repo IDs through `McpRuntimeConfig`; they should not
  accept arbitrary source or coordination roots from tool callers.
- Route-index application entry points must pass the resolver-owned repository identity and storage/path-rule
  settings into the kernel builder explicitly; the builder does not infer write authority from a
  filesystem location.
- Contract-scoped quality must measure the leaf memory tree against the leaf code worktree and pass
  the leaf base as unstamped comparison provenance. It must not stamp the dirty tree or give an
  official-memory call a synthetic comparison base.
- Provider, benchmark, and worktree application entry points should call package services
  directly rather than CLI `main(argv)` wrappers.
- Keep each application entry point file scoped by domain; do not rebuild the former
  `runtime/skills.py` focused entry point.
- Launch-capable provider operations re-read the on-disk authority fail-closed
  (containment R1, 260707-HFX-L1); application entry points must never launch providers off
  the boot-snapshot config, while stop/status/cleanup stay ungated.

L14: the task-doc application entry point accepts the additive `orchestrates` field (master-only) through create/set_field, feeding the dashboard's command hierarchy; docs without it are untouched.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two MCP payload builders are declared at these entry points. | "def skills_install_payload("; "def task_reopen_payload(" | mcp/src/agents_remember/mcp/tools/core.py:146-146; mcp/src/agents_remember/mcp/tools/task_doc.py:35-35 |
| `ResponseModel` is the public response-model base. | `ResponseModel` | mcp/src/agents_remember/models/base.py:66-88 |
| `TOOL_RESPONSE_MODELS` is the registry of public response models. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:163-253 |
| Canonical memory scope freezes official/leaf authority, both trees, and optional unstamped comparison provenance. | `MemoryScopeIdentity`; `resolve_memory_scope`; `resolve_leaf_memory_scope` | mcp/src/agents_remember/application/memory_scope.py:59-68; mcp/src/agents_remember/application/memory_scope.py:105-142; mcp/src/agents_remember/application/memory_scope.py:145-169 |
| The typed quality controller owns sync/start/poll execution and checklist publication without changing verification metadata. | `run_memory_quality_request`; `start_memory_quality_request`; `poll_memory_quality_request`; `_attach_curator_checklist` | mcp/src/agents_remember/application/memory_quality/controller.py:259-265; mcp/src/agents_remember/application/memory_quality/controller.py:268-274; mcp/src/agents_remember/application/memory_quality/controller.py:277-283; mcp/src/agents_remember/application/memory_quality/controller.py:517-681 |
| `route_index_refresh_tool` resolves context and supplies repository/storage authority. | `route_index_refresh_tool` | mcp/src/agents_remember/application/memory_tools.py:316-352 |
| `build_route_indexes` is the deterministic route-index builder. | `build_route_indexes` | mcp/src/agents_remember/kernel/route_index.py:184-235 |
| `worktree_status_packet` returns the `WorktreeSummary` the context packet embeds directly, so the state machine's output is checked at the producer. | `worktree_status_packet` | mcp/src/agents_remember/application/worktree_status.py:72-134 |
| `DriftSummaryPacket`, the typed drift seam `_drift_packet` returns. | "class DriftSummaryPacket(TypedDict):" | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:11-11 |
| `FileReadStatus` is defined in the models type. | `FileReadStatus` | mcp/src/agents_remember/models/read_files.py:29-29 |
| The application read-files entry point imports the wire type and decides the read status. | "from agents_remember.models.read_files import FileReadStatus"; "def _resolve_onboarding(" | mcp/src/agents_remember/application/read_files.py:73-73; mcp/src/agents_remember/application/read_files.py:262-294 |

Worktree start is async (GitHub #53): `worktree_tools.py` transfers the temp
lifecycle settings file to the background setup thread on a `starting` result,
forwards `retry_provider_setup`, and bounds worktree provider setup by
`timeoutCaps.providerSetupSeconds` instead of the docker-control default.

`context_packet.py` carries the opt-in branch-freshness section (GitHub #54):
`include_freshness`/`fetch_timeout` on the request feed
`kernel.git_freshness.read_branch_freshness` for the code and external-memory
repos plus informational computed-ledger status; the default stays
`not-checked` so everyday packets skip the remote fetch.

Gate-policy threading (260703-L8): `worktree_tools.py` resolves
`config.orchestration.gate_policy` and threads it into BOTH the closeout and the
integrate `WorktreeArgs`, so the module-level enforcement guards (closeout's
delegated-gate check, integrate's master-handover seam guard) always evaluate
the configured policy — never the all-human dataclass default. Omitting the
passthrough on either path silently reverts that guard to human-only semantics,
which is exactly the inert-consumer defect adversarial review 3 caught on the
integrate side.

Provider launch containment (260707-HFX-L1, containment R1): the provider,
worktree, and benchmark application entry points all treat the ON-DISK authority settings —
not the boot-snapshot config — as the provider launch authority.
`provider_tools.py` gates watcher `start`/`restart`/`invalidate-indexes` and
the launch-capable GrepAI/CGC query tools (one-shot runner containers) through
`require_provider_launch_authority` — fail-closed `ConfigError` when the disk
disables providers or cannot be read; `stop`/`status`/`shutdown-all` stay
legal. `worktree_tools.py` re-reads the authority before provider setup and
writes lifecycle settings from the LIVE map only when armed, attaching a
`providersAuthority` veto block to the result when the disk vetoed an armed
boot snapshot (the worktree itself is still created). `benchmark_tools.py`
passes the live authority's provider ids as `allowed_provider_ids` on both
benchmark requests, so a case manifest cannot arm providers disabled on disk.

Current working-candidate evidence for this route:

| Finding | Anchor | Source |
| --- | --- | --- |
| Application message transport contains only code and memory. | `CloseoutCommitMessages`; `memory_commit_message` | mcp/src/agents_remember/application/worktree_tool_requests.py:76-76; mcp/src/agents_remember/application/worktree_tool_requests.py:110-115 |
| Landing input carries the actual two outputs. | `LandedCommits` | mcp/src/agents_remember/application/worktree_tool_requests.py:118-128 |

## 260731-EFA-L4 — Typed Seams Where An Application Entry Point Meets A Producer

Two application entry points stopped re-validating something a collaborator already returned in a checked
form. The rule is the same in both: a `ValidationError` from `model_validate` inside a
application entry point surfaces from inside an `@server.tool()` handler that has no `except` for one, so
where a producer can be made to hand over a typed value, the mismatch becomes a pyright error
at the producer instead.

**`context_packet.py`.** `worktree=` is now `worktree_status_packet(context.contract_path)`
directly — the projection in `application/worktree_status.py` is signed `-> WorktreeSummary` and
constructs the model itself, so the previous
`WorktreeSummary.model_validate(worktree_status_packet(...))` was validating a model's own
dump. This is the application-side half of a real defect: `models/worktree.py` had hand-copied
six contract vocabularies that had each drifted from the contract's own, and the resulting
`ValidationError` fired here, inside the tool. `test_wire_vocabulary_exhaustiveness.py` records
the measurement — 165 of the 213 `series-contract.md` files on disk (77.5%) made
`context_packet` raise, across seven independent gaps. The vocabulary fix lives in the `models/`
route; what this route contributes is that the seam is now checked at the producer rather than
at runtime here. `_drift_packet` is correspondingly annotated
`-> DriftSummaryPacket` (from `memory_quality.integrity.onboarding_drift_check.models`) instead
of `-> dict[str, Any]`, so both of its returns — `not_checked()` and `run_drift_summary(...)` —
are checked against the shape `models/drift.py` expects.

**`read_files.py`** defines `FileReadStatus` in `models/read_files.py`
(`Literal["found", "missing", "disabled", "unsupported", "not_requested"]`).
`application/read_files.py` imports that alias, and `_resolve_onboarding` is the only function that
decides the value and returns `tuple[FileReadStatus, str | None, bool]`.
cit:([`FileReadStatus`], mcp/src/agents_remember/models/read_files.py:29-29)
cit:(["from agents_remember.models.read_files import FileReadStatus"], mcp/src/agents_remember/application/read_files.py:73-73)
cit:([`_resolve_onboarding`], mcp/src/agents_remember/application/read_files.py:262-291)
`VALID_FILE_READ_STATUSES = frozenset(get_args(FileReadStatus))` is the runtime half, derived from the
alias. The import direction is application → models, so the producer uses the single declared alias
without maintaining a second copy.

The `read_ar_files` status semantics are unchanged and still worth restating, because the alias
now carries them: this is the ONBOARDING lookup outcome, never a source-read condition. Source
presence rides the independent `source` field, which is why `found` alongside a missing
`source` is not a contradiction.

## 260731-EFA-L9 Route Impact

The application layer gained the provider lifecycle runtime
(`application/provider_runtime.py`, moved from `worktrees/modules/provider_teardown.py` and
absorbing `provider_async.py`'s setup launcher/status) and the default `WorktreeServices`
composition (`application/worktree_services.py`) binding the provider, memory-quality, and
citation-guard adapters into the worktrees service ports.

## L23 Structural Admission Translation

Application facades now consume centralized terminal refusal translation and
strict source-lineage projections. Context status validates those facts instead
of retyping them, and ambient attach attribution occurs only after a real
attachment, keeping blocked lineage out of successful lifecycle history.

## 260815-DAG-L3 Ambient Queue Authority (Transitional After CLIVE L2)

`application/closeout_queue.py` remains the hosted authority adapter for the sprint closeout queue.
It resolves the live seat from the terminal catalog, requires a canonical bound task document, and
constructs the internal `QueueActor`; role/task identity is absent from the public request. This
section records the pre-CLIVE queue design. In the L2 candidate, lifecycle recovery and controls
use the root journal, while some selected/in-flight/certified queue states remain transitional.
L3 owns removing that lifecycle-shaped queue schema and completing waiting-only projection.

## 260815-DAG-L4 L4 Application Authority Boundary

Application tools now bind lifecycle requests to configured coordination, task, code-repository, and memory-repository identity before dispatch. Worktree, task-document, topology, and memory entry points route protected mutations through the queue/repository authority plane and reject preview/apply drift.

## 260815-DAG-L14 Sprint-Linkage Route

`application/task_sprint_linkage.py` is the new application owner of the sprint↔master linkage
contract: one atomic `attach_master`/`detach_master` pair, the read-only `linkage_report`
surface, and the moved `validate_completed_master_row` for typed rows. `task_doc_tools` routes
the new operations and carries `linkageFacts` on sprint gets; `task_execution_topology` exposes
the shared `verify_sprint_judgment_ids`.

## 260815-DAG-L16 Seat-Independent Application Route

`application/closeout_queue.py` gains the declared-caller fallback (L16-R2): on
`ambient-seat-unavailable` the request-carried `caller` builds the identical `QueueActor` a seat
would, and a contradicting declared caller refuses. The route-review binding machinery extracted
from `task_doc_tools.py` into `application/task_doc_route_review.py` (L16-R6/R9, facade
re-export), and `application/direct_landing.py` is the error-translating application boundary of
the direct landing operation (L16-R8).

## 260815-DAG-L12 Route Impact

All three task-document writers thread the joined graph titles into the renderer (L12-R1/R4): `task_doc_tools.py` (`_graph_titles_for`/`_batch_graph_titles`), `task_execution_topology.py` (`_authoring_batch_titles`), and `task_sprint_linkage.py` (`_batch_graph_titles`) — publish and preview both label the sprint mermaid diagram with real master/leaf titles; batches without a graph fall back to ref-key labels.

## 260815-DAG-L15 Route Impact

New `application/memory_quality_runs.py` (bounded single-flight background run registry, L15-R7); `memory_tools` gained the async start/poll wrappers (including the `ok`-envelope gate-repair fix); `task_execution_topology`/`task_sprint_linkage` hardened the authoring dialect (served-build preflight, typed judgment-required, move-retargets-edge, node-kind order, `create=False` dry-run locks).

## 260815-DAG Master Full-Gate Repair Route Impact

Seven application modules moved into the new `application/task_docs/` sub-route (task_doc_tools, task_execution_topology, task_sprint_linkage, task_ref, task_reopen, task_doc_queue_scope, task_doc_route_review); importers updated.

## 260821-CLIVE-L1 Application Boundary

Application closeout adapters now preserve raw public observations only until the shared route-aware normalizer returns typed `effectiveInput`. Worktree apply submits validated admission to the lifecycle owner; preview and direct landing return the same effective plan. Typed refusals carry invalid fields, resolved leg state, and a corrected call. The worker rehydrates only accepted effective input and repairs derived recovery projection from operation-journal evidence. Application code neither derives queue selection nor treats queue state as lifecycle evidence.

## 260821-CLIVE-L2 Current Architecture

Current-contract mutation consumers branch only on accepted versus refused admission and reuse the exact accepted contract/location observation. Expected path/read/authority failures are translated once. Degraded status and the explicit legacy bridge are separate because they intentionally inspect unreadable or pre-adoption state; they are not mutation fallbacks.

The committed route now groups these application owners under `application/lifecycle/`. This is a package move, not a second API: configured-contract admission remains the one total mutation boundary, and durable journal authority remains below it in `worktrees/integration/lifecycle/`.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| Closed application admission. | `ConfiguredContractAdmission`; `admit_configured_contract`; `admit_configured_terminal_contract` | mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py:90-90; mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py:96-96; mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py:102-163; mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py:166-244 |
| Configured degraded location projection. | `LifecycleOperationPublicAddress`; `configured_lifecycle_operation_location`; `observe_contract_read_failure`; `primary_operation_projection` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_location.py:26-32; mcp/src/agents_remember/application/lifecycle/lifecycle_operation_location.py:58-68; mcp/src/agents_remember/application/lifecycle/lifecycle_operation_location.py:108-160; mcp/src/agents_remember/application/lifecycle/lifecycle_operation_location.py:187-212 |

## 260821-DAGQC-L2 Quality Controller And Direct-Landing Projection

Memory quality now has one focused application API: `memory_scope.py` freezes configured official
or leaf authority, and `memory_quality/controller.py` owns strict sync/start/poll execution,
complete run identity, checklist publication, capacity guidance, and nondisclosing polling.
`memory_tools.py` no longer repeats that failure family. The lifecycle direct-landing application
boundary separately keeps the closed result outcome authoritative while nesting journal recovery
state.

## 260824-PDLS Final Application Boundary

Public closeout and direct-landing adapters consume the shared configured-contract admission API,
while lifecycle worker service imports are deferred to execution. This keeps failure translation
total at one application boundary and prevents bootstrap import fan-out from pulling the service
graph into test collection.

## MCAR-L02 Structured Curator-Coherence Boundary

`curator_coherence.py` is the configured-contract application seam for the one
`status`/`prepare`/`publish`/`validate` coherence API. It delegates exact record/publication policy
to the closeout integration route and translates that complete domain failure family once. The
memory-quality controller uses the same currentness validator as closeout admission, exposing raw
quality readiness separately from combined `closeoutReady`; it cannot claim combined readiness
while the stable authority is absent or stale.

## MCAR-L03 Exact Memory-Candidate Route

The application plane now separates repository-only official diagnostics from acceptance-eligible
leaf work. Candidate memory quality admits one configured contract pair, preserves it through
async run identity and polling, revalidates around scanning/publication, and exposes the same pair
at closeout apply admission. Public refusal projection retains the named pair field and exact
contract-addressed repair arguments.

## Current CCR Composition And Remaining Authority Gaps

The task publication owner classifies exact field deltas and preflights affected scopes before canonical writes. Route-review and closeout admission now bind current normative task intent and direct evidence dependencies; typed intent refusals stay visible at the application boundary. Detached lifecycle workers and direct worktree paths preserve transaction identity and explicit approval/ref safety; normal closeout/integration do not automatically execute the repository certification profile. The default service graph still exposes explicit quality and memory tooling for callers that request it.

The full memory controller snapshots both working trees with external temporary indexes before scanning and revalidates those exact tree identities before checklist publication. Its `finalFullCatalog` reports executed catalog checks and missing authority; it explicitly supplies no affected-closure plan and cannot create R08 acceptance from checklist readiness. R05 frozen lifecycle admission/finalization, ordinary R16 durable telemetry and complete R07/R08 production orchestration remain unconstructed at this source. Terminal failure translation preserves classified organizational repair and actual Git recovery before supplying an otherwise missing typed rail failure.

## CCR-R18@v1 Task-Addressed Next-Step Bounding

260831-CCR-L18 added `bound_next_step` to `application/tool_response.py`: lifecycle tool responses omit any `nextStep` guidance whose arguments name a different task address than the response's own exact contract/enclosure path. File-level detail lives in that sidecar.

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.

## CCR-R12@v5 Current Application Boundary

Application adapters expose transaction previews, applies, observation, and recovery. Normal
closeout commits code, mechanically refreshes and commits substantive external memory when needed, then refreshes the consumer ledger cache;
normal integration publishes a prepared pair under explicit handover/ref authority. Neither path
automatically runs strict code quality, memory quality, selected certification, curator coherence,
or independent review. Full suites remain an explicit developer request.

## Pull-Request Landing Records Through The Same Writer

A pull request lands code on the remote; it never moves refs locally, so `worktree_integrate` cannot
express it. `worktree_tools.py::worktree_record_landing_tool` is the application entry point for that
route. It admits the configured contract through the same refusal projector, builds a
`git_worktree_manager.WorktreeArgs` carrying `landed_code_commit` and `landed_memory_content_commit`, then
calls `git_worktree_manager.record_landing_result`. The point of the
entry point is that it shares `worktree_integrate`'s one contract write
(`worktrees/modules/landing_record.py`), so the terminal `integration` cell has exactly one
definition regardless of how the code landed; a commit that is not reachable from a landing target is
refused, so the cell cannot be set from a commit that landed nowhere.

`worktree_tool_requests.py::LandedCommits` is the parameter object that route owns: `code` is the
commit the PR landed on the protected branch, and the memory output is optional because C-11 carryover
may not have run yet when the landing is recorded — the cleanup guard checks carryover separately and
refuses until it is done.

## Checkpoint Landing Gets Its Own Application Entry Point (260831-LOCR-L30)

The application layer gained a second landing entry point beside the PR tail.
`worktree_tools.py::worktree_checkpoint_landing_tool` admits the configured contract, refuses through
the same projector, builds `WorktreeArgs` with `approved=not dry_run`, the typed `strategy` and the
configured `gate_policy` (the same master-exit seam pass-through `worktree_integrate_tool` uses), and
delegates to `git_worktree_manager.checkpoint_landing_result(args, configured.contract)`.

The entry point is deliberately as thin as its integrate sibling: eligibility, the series authority,
and the recorded state all live below it, and it runs none of the completion-edge work
`worktree_integrate_tool` performs — in particular no `auto_complete_seats` call, because a checkpoint
retires nothing. It is also the only landing entry point that does not need the master to be finished,
which is exactly why it is a separate tool rather than a flag on `worktree_integrate`: a caller that
invokes it has chosen a non-final landing on purpose.

**260831-LOCR-L34 corrected this entry point's published docstring, and the correction is
substantive.** It had said the route drops only the two "master is finished" assumptions; the route
also required a **completed closeout**, which is why it was unreachable in both directions — a partial
master could never satisfy it, and a complete one was refused by the downgrade guard. The docstring now
names the full refusal set (`worktree_integrate` proves the task document `Completed`, one landed
enclosure per canonical leaf, **and a completed closeout**) and states that the checkpoint captures the
master's own live code and memory work-branch tips and proves their Git source ancestry
before landing exactly those. Published text is the only thing a client reads, so it is contract rather
than comment. The preview/apply parity invariant that produced this repair is inventoried on the
`worktrees/overview.md` route and in `memory_quality/overview.md`.

## 260915-KS-L1 Knowledge Composition Seam

## 260915-CAPS-L7 The Eve Capsule Produce Side

This route gained one module, `application/knowledge.py`, and no new authority. It is the composition seam between
admitted authority and the concrete knowledge store, and it is the **only** consumer of
`memory.knowledge` (rank 12) from this layer (rank 21).
This route gained one package, `eve_capsule/`, which is the **produce side** of the eve
capsule/workspace binding seam. It is deliberately not a second compiler: it calls the L4 capsule
surface and the L3 task projection and **transports a decided value** into the carrier file one bound
eve runtime reads before its first model call. It orders nothing, selects nothing and re-renders
nothing.

What it does: `write_authorship` assigns the provenance envelope's `operation_id` and `recorded_at` rather than
accepting them; `admitted_knowledge_destination` binds a resolved path, namespace and envelope into the typed
handle a storage operation receives; `admitted_revision_request` attaches a draft to that destination so provenance
is **not** a parameter; `initialize_knowledge_namespace` refuses an occupied destination as a resume attempt;
`open_admitted_knowledge_store` opens read-only; and `create_knowledge_revision` delegates the insert and closes in
a `finally`.
The load-bearing boundary for a reader of this route:

What it deliberately does not do: it holds no schema and no durable state, it performs no admission check of its
own (`admitted_knowledge_destination` confers no authority by itself — it exists so the store receives a typed
handle rather than a bare path), and it exposes **no acceptance or promotion operation**. The store manufactures no
acceptance; `state_at_origin` and `acceptance_ref` remain authored data.
- **Admission precedes execution.** `materialize_eve_binding` returns the compiler's or projection's
  own refusal and writes **no carrier** on any refusal path, so a runtime that cannot be bound correctly
  is never handed something to run. It also reads the carrier back and requires it to parse equal.
- **The projection is re-derived and compared, not trusted.** The compile outcome does not carry the
  projection it read, so the module resolves the same scope and requires the task context to be
  **byte-identical** to the one the capsule carries; a disagreement is refused rather than silently
  becoming the carrier's task facts.
- **Write surfaces are role authority, and the fallback is the smallest set.** A worker gets the
  workspace and its report surface, a curator adds the memory surface, and an undeclared role gets the
  worker's set — so a role whose scope nobody declared cannot inherit the memory write. A surface the
  role's table names but nobody admitted is a refusal, not a silent narrowing.
- **The carrier lives outside the admitted workspace**, in a caller-admitted epoch directory, because
  the runtime's own file tools are confined to the workspace root and the instructions it applies must
  not be a file the model can rewrite.

The direction is the point and it is what the `layers.toml` charter paragraph records: a lower-ranked owner —
`worktrees` (10) and `memory_quality` (11) among them — receives `models.knowledge` values or an already-prepared
result from this layer, and never imports the storage package.
**The seam's other half is not in this route.** The format is `models/eve_capsule_carrier.py`; the
launch-time proof is `serving/eve_runtime_launch.py::verify_capsule_binding`; and the in-process reader
is `eve_runtime/agent/lib/capsule.ts`. **The produce side now has a production caller** (since
`260915-CAPS-L15`): `application/role_capsules/launch.py::_compile_eve_task` calls
`materialize_eve_binding` for a wired launch point, and the carrier it writes is verified by the
runtime's own gate from the launch's own captured cwd and env, then read at the live runtime's system
block (`notes/reports/260915-CAPS-L15-evidence/E8-fix-r1-production-chain.txt`). The `L7R-4` transfer
that asked for this is therefore discharged on the **produce** side — "the produce side has a
production caller, verified at the consumer's gate" — while the **live-seat** half for a dispatched eve
seat still waits on the inherited settings-chain gate (**D22**, owner **L17**). The test fixture is no
longer the only caller, and neither half should be read as the other.

| Finding | Anchor | Source |
| --- | --- | --- |
| The provenance envelope is assigned here, not accepted from a payload. | `write_authorship` | mcp/src/agents_remember/application/knowledge.py:117-137 |
| The admitted-destination constructor that confers no authority by itself. | `admitted_knowledge_destination` | mcp/src/agents_remember/application/knowledge.py:140-156 |
| Provenance and namespace come from the destination rather than from the request. | `admitted_revision_request` | mcp/src/agents_remember/application/knowledge.py:159-172 |
| Initialization refuses an occupied destination as a resume attempt. | `initialize_knowledge_namespace` | mcp/src/agents_remember/application/knowledge.py:175-205 |
| The read open and the delegating insert, both closing in a `finally`. | `open_admitted_knowledge_store`; `create_knowledge_revision` | mcp/src/agents_remember/application/knowledge.py:208-219; mcp/src/agents_remember/application/knowledge.py:222-236 |
| The layer charter paragraph that fixes the one-way direction this seam implements. | "[package.memory]" | layers.toml:206-222 |
| The storage operation this seam delegates to. | `create_revision` | mcp/src/agents_remember/memory/knowledge/store.py:291-325 |
| The produce side added to this route, and the read-back-equals-written and no-carrier-on-refusal rules. | `materialize_eve_binding` | mcp/src/agents_remember/application/eve_capsule/__init__.py:147-206 |
| The projection agreement check that makes the re-derivation a check rather than a second opinion. | `_admitted_projection`; `_require_matching_task_context` | mcp/src/agents_remember/application/eve_capsule/__init__.py:228-261; mcp/src/agents_remember/application/eve_capsule/__init__.py:264-279 |
| The role-authority write surfaces and the smallest-set fallback. | `write_scopes_for`; `ROLE_WRITE_SURFACES` | mcp/src/agents_remember/application/eve_capsule/__init__.py:85-88; mcp/src/agents_remember/application/eve_capsule/__init__.py:327-365 |
| The capsule surface this package consumes and does not re-implement. | `compile_task_capsule` | mcp/src/agents_remember/application/skill_resources/capsule.py:205-236 |
| The launch-time proof and the in-process reader that consume the carrier this route produces. | `verify_capsule_binding`; `loadVerifiedCapsule` | mcp/src/agents_remember/serving/eve_runtime_launch.py:466-515; eve_runtime/agent/lib/capsule.ts:109-143 |
| The production caller the produce side gained: an eve launch through the wired launch points materializes this carrier, and the launch runs in the workspace the carrier admits. | `_compile_eve_task`; `compile_launch_capsule` | mcp/src/agents_remember/application/role_capsules/launch.py:362-404; mcp/src/agents_remember/application/role_capsules/launch.py:273-294 |
| The test fixture that supplied this seam's inputs before a production caller existed. | `fixture_carrier_for` | mcp/tests/eve_capsule_test_support.py:573-627 |
| The production-chain evidence: the consumer's own gate accepts the launch point's carrier, and the live runtime's system block carries it. | `resolve_runtime_spec`; `verify_capsule_binding` | mcp/src/agents_remember/serving/eve_runtime_launch.py:312-348; mcp/src/agents_remember/serving/eve_runtime_launch.py:466-515 |

## 260915-KS-L2 The Graph Operations Join The Seam

The same module gained the graph half's eight operations and eight request builders, and the seam's contract did
not change: the builders attach the destination's `authorship` and `repository_id` exactly as
`admitted_revision_request` does, and each operation opens the admitted destination, delegates to the owning graph
module and closes in a `finally`. The one builder with an extra parameter is `admitted_claim_request`, which takes
the anchor endpoint — naming an existing anchor and recording a new one in the same transaction are different
inputs, and the seam must not collapse them.

**The boundary a later reader most needs is the one that did not move: this module still has no non-test importer
in `mcp/src`.** Its only importers are `mcp/tests/test_knowledge_store.py` and
`mcp/tests/test_knowledge_relation_rules.py`, so its green composed-path test is evidence about the seam's
behaviour, not evidence that the seam is wired into any registered tool or entry point. The typed write boundary
that will consume it is `KS-R03`'s.

| Finding | Anchor | Source |
| --- | --- | --- |
| The graph request builders, all attaching the destination's provenance and namespace. | `admitted_family_request`; `admitted_anchor_request`; `admitted_member_request`; `admitted_claim_request` | mcp/src/agents_remember/application/knowledge.py:342-352; mcp/src/agents_remember/application/knowledge.py:351-360; mcp/src/agents_remember/application/knowledge.py:366-375; mcp/src/agents_remember/application/knowledge.py:378-386; mcp/src/agents_remember/application/knowledge.py:389-401 |
| The eight graph operations, each open-delegate-close. | `create_knowledge_family`; `create_knowledge_anchor`; `create_knowledge_family_member`; `create_knowledge_realization_claim`; `remove_knowledge_realization_claim` | mcp/src/agents_remember/application/knowledge.py:438-447; mcp/src/agents_remember/application/knowledge.py:462-471; mcp/src/agents_remember/application/knowledge.py:486-495; mcp/src/agents_remember/application/knowledge.py:495-504; mcp/src/agents_remember/application/knowledge.py:510-519; mcp/src/agents_remember/application/knowledge.py:522-531 |
| The graph modules the new operations delegate to. | `create_family_revision`; `create_source_anchor`; `create_family_member`; `create_realization_claim` | mcp/src/agents_remember/memory/knowledge/families.py:133-160; mcp/src/agents_remember/memory/knowledge/anchors.py:51-70; mcp/src/agents_remember/memory/knowledge/memberships.py:88-107; mcp/src/agents_remember/memory/knowledge/realizations.py:61-81 |
| The composed-path case that drives admit -> create -> reopen -> read through this seam. | "test_the_application_seam_authors_a_graph_through_an_admitted_destination" | mcp/tests/test_knowledge_relation_rules.py:566-680 |
| The closeout certification's own source index, or a named refusal with the operator move. | `_admitted_source_index` | mcp/src/agents_remember/application/prepared_certification.py:424-446 |
| The candidate route that index is acquired over, so the gate sees the register the route records. | `_run` | mcp/src/agents_remember/application/prepared_certification.py:449-568 |

## 260915-KS-L3 The Candidate-Write Boundary Joins The Seam

The same module gained the candidate-write boundary, and the seam's contract still did not change: every new
entry point opens the admitted destination, delegates and closes in a `finally`, and provenance keeps coming from
the destination rather than from the payload.

Three additions matter to a later reader:

- **`resolve_candidate_context` / `build_candidate_context` are the only way a batch's dataset precondition is
  built.** The application opens the destination read-only, reads the identity the candidate actually holds
  (`OpenedKnowledgeStore.snapshot_identity()`) and seals the whole resolution into a context digest. A caller
  therefore cannot hand-write the dataset identity its batch will be compared against — `CandidateResolution`
  deliberately has no field for it — and the operation re-derives the seal inside its own transaction.
- **`change_knowledge_candidate` passes `destination.authorship` into the operation as a keyword argument**, so no
  part of a submitted batch can become the stored author, authorization or instant. The batch is a value; the
  authority is the admission's.
- **The two label operations** (`set_knowledge_invariant_label`, `set_knowledge_family_label`) are the same
  open/delegate/close shape over the two guarded label edits.

**The boundary that did not move, and that a later reader most needs: this module still has no non-test importer
in `mcp/src`.** Adding `change_knowledge_candidate` inside `application/knowledge.py` does not give the module an
importer — a `grep` for one is still empty — so the seam's composed-path cases are behaviour evidence about the
boundary and not evidence that it is wired into any tool. The packet makes transport wiring an explicit later
extension, and the worker report's claim that `KS-R03` "resolved" that observation was withdrawn in review.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two label operations the seam exposes. | `set_knowledge_invariant_label`; `set_knowledge_family_label` | mcp/src/agents_remember/application/knowledge.py:239-252; mcp/src/agents_remember/application/knowledge.py:255-264 |
| The context resolution and its pure sealing step. | `resolve_candidate_context`; `build_candidate_context` | mcp/src/agents_remember/application/knowledge.py:267-287; mcp/src/agents_remember/application/knowledge.py:290-315 |
| The batch operation that takes its provenance from the destination. | `change_knowledge_candidate` | mcp/src/agents_remember/application/knowledge.py:318-331 |
| The resolution shape whose missing dataset-identity field makes the read the only source of that value. | `CandidateResolution`; `KnowledgeContext` | mcp/src/agents_remember/models/knowledge/candidate.py:659-676; mcp/src/agents_remember/models/knowledge/candidate.py:498-529; mcp/src/agents_remember/models/knowledge/candidate.py:638-655; mcp/src/agents_remember/models/knowledge/candidate.py:656-656; mcp/src/agents_remember/models/knowledge/candidate.py:236-277 |
| The lane rules the seam's entry point reaches, and the operation that applies them. | `change_candidate`; `require_writable_lane` | mcp/src/agents_remember/memory/knowledge/candidate.py:64-83; mcp/src/agents_remember/memory/knowledge/candidate.py:86-105 |
| The composed-path case that drives the boundary end to end through this seam. | "test_a_late_invalid_command_rolls_back_every_earlier_insert_in_the_batch" | mcp/tests/test_candidate_batch_transaction.py:62-109 |
| The case that proves the operation refuses a context smuggled past the model seal. | "test_a_context_smuggled_past_the_model_seal_is_refused_by_the_operation" | mcp/tests/test_candidate_batch_transaction.py:1120-1160 |

## 260918-TSIP-L6 Three Application Entry Points Stop Losing The Envelope

Every repair in this leaf that a *caller* can observe lands on this route.

**`T34` — the provider surface.** `provider_tools.py` now declares one refusal per provider
operation in `_PROVIDER_REFUSAL_SITES` (`:109-195`), with `provider_refusal_payload` (`:196-220`)
for a tool that can return and `provider_refusal_result` (`:221-239`) for a tool whose owner
raises. `resolve_grepai_query` (`:240-274`) and `resolve_cgc_capability` (`:275-294`) are the
guards the two families call first, so `grepai_search`, `grepai_trace` and the six `cgc_*` tools
answer `ok: false` with a refusal identity, a reason and `provider_watchers` as the way out
instead of a traceback. That is the shape `provider_status_tool` (`:35-42`) and
`provider_diagnostics_tool` (`:43-50`) already used on this route.

**`T34` — memory baseline adoption.** `memory_tools.py::memory_baseline_adopt_tool` (`:393-432`)
catches the new typed `BranchAuthorityUnavailable` and answers through
`_baseline_adopt_refusal` (`:433-459`). The catch is narrow on purpose: the other `RuntimeError`s
on that path refuse a state the caller must understand and change, and they keep raising.

**`T54` — the response's own address.** `tool_response.py::bound_next_step` (`:58-99`) is the only
thing connecting process-global ambient guidance to the response that carries it, and both of its
escapes are closed: a response that declares no contract path has its guidance withheld rather
than emitted unchecked, and any disagreeing path spelling withholds the hint.
`_names_the_same_place` (`:31-57`) accepts the contract file or the directory that immediately
contains it — no wider. `complete_tool_response` (`:131-145`) is unchanged; the guard sits inside
`_attach_lifecycle_tail` (`:112-130`), so every response this route completes passes through it.

## Update History
- 2026-09-24T10:20+02:00 — 260921-ICR-L29 curator, **fix-round bytes** (uncommitted change set on
  `ar/260921-icr-l29-ar`, base `0d7910f9d646161c414ed6543453536a3c749d49`; gate `verify-l29-round2.md`,
  first line `pass-with-findings`): **re-read against the fix-round bytes.** The manifest paragraph above gained the carry-forward: owed entries are carried into the next run's record and re-derived against that run's own store read, and the record is written by any committed run including one whose batch wrote nothing. The four purpose-named owners' sizes in the table above are unchanged except `knowledge_bootstrap_staging.py` 439 → 530 and `knowledge_bootstrap.py` 473 → 577. **No verification stamp was advanced** — the candidate is
  uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base
  `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **route body updated for the five owners `ICR-R28@v2`
  added, and their six file-level cards are created in this pass.** The section records the three
  outcomes that must stay three facts, the allocated-never-derived identity rule, the single
  implementation of the undeclared-key answer, and the closed defect that made a replayed revision skip
  its own family plane while the report still claimed the rows. **Citation accounting:** every range
  this route carries into `application/knowledge_curator_ingest.py` was re-derived against this
  candidate's bytes (the module grew 3587 → 3861) rather than shifted by a remembered delta; the rows
  the product reported as `citation_anchor_absent_from_range` were re-anchored to the constructs they
  name, and no claim and no row was dropped. No verification stamp was advanced: the candidate is
  uncommitted and the governed closeout owns the real stamp.
- 2026-09-23T12:00:00+02:00 — 260921-ICR-L15 curator (candidate uncommitted; basis: leaf base commit `3103e1142a3ded8a843c3e5bbefca14861ba4a58` plus the working-tree delta): **route body update for measured assessment currentness (`ICR-R15@v1`), and three enforced citation rows re-pointed.** The section above records the new owner (`application/review_assessment_currentness.py`, 226 lines) and the three product states its channel can state, the record bundle's production of the measurement with `_CURRENTNESS` deleted, the renderer's `currentness: AssessmentCurrentnessMeasurement | None` field replacing the bare `current` mapping, and the freeze's `current_measured` flag now meaning "a measurement was performed". **Citation accounting:** the L14 production-owner row's first range widened `review_evidence_records.py:174-214` → `171-214` (its declaration is at 171), and the two per-record damage cases re-pointed to their own extents in `mcp/tests/test_knowledge_review_evidence_channels.py` (`:695-717` → `:825-844` for `test_a_damaged_detection_run_is_named_while_its_siblings_are_supplied`, `:719-745` → `:847-870` for `test_a_damaged_evidence_claim_is_named_while_its_siblings_are_supplied`). Finding and Anchor wording unchanged; per-file detail lives in the seven sidecars. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, the header's `lastVerifiedCommitHash`/`lastVerifiedCommitDate` values are untouched, and the governed closeout owns the real stamp.
- 2026-09-23T09:35:00+02:00 — 260921-ICR-L21 curator (uncommitted change set on `ar/260921-icr-l21`, base `972b44cc07b307929535fe7974d6a30d53c9c4f1`): **route body update for review-to-closeout identity continuity (`ICR-R21@v1`), and the route gained two purpose-named owners plus one test module.** The section above records the split (the record and its vocabulary in `models/knowledge/review_final_output_receipt.py`, the operation in `application/review_final_output_receipt.py`), the three result attachments in `application/worktree_tools.py` (+12 lines, all delegation), the fourth reopen channel, and the two boundaries: **recording is not a gate** (the never-raising wrapper is what the transaction owners call, so a receipt that cannot be produced is a state and never a refusal) and **the reclamation owner has no shipped caller** — routed debt to ICR-R25@v1 with the R11 retention/release route secondary, so reclamation is *not* automatic at this candidate. `application/knowledge_review.py` was **not touched** (byte-identical), because the seam policy moves a touched responsibility and this leaf added none there — the L11 section's recorded boundary that "ICR-R21 wires it at closeout" is now realised. **Citation accounting:** the three `review_comparison_reopen.py` ranges in the L11 row above were re-derived at their constructs' own extents (the module moved 699 → 730 lines with the fourth channel) rather than shifted by a delta, and the read-back row's wording now says four channels rather than three. Per-file citations live in the three new sidecars. No verification stamp was advanced: the candidate is uncommitted and closeout owns the real stamp.
- 2026-09-22T16:35:00+02:00 — 260921-ICR-L9 curator (candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61`, this leaf's base): **route body update for the subject catalogue (`ICR-R09@v1`).** The route gained `application/review_subject_catalogue.py` and this overview gained the L9 section (the population rule, the seam, and the compare-to-earn-a-row deletion); the L7 section's rows into `knowledge_review.py`/`review.py` were re-derived against the moved candidate. **Stamp accounting:** the verification pair names the leaf's base; closeout owns the stamp.
- 2026-09-22T11:39:00+02:00 — 260921-ICR-L13 curator, **L7-aftershock citation repairs: four rows re-cited to the landed `knowledge_review.py` declarations.** L7's pass cited its uncommitted candidate's positions; the landed file moved them (`select_subject_revisions` import `:90-93`, `_knowledge_pane` `:712-759`, `_selected_statements` `:760-785`, `_selector_kind_or_absence` `:615-626`). Each claim re-read against its declaration with wording retained. No verification stamp was advanced: the candidate is uncommitted and closeout owns the stamp.
- 2026-09-22T10:40:00+02:00 — 260921-ICR-L7 curator (uncommitted change set on `ar/260921-icr-l7`, base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **this route gained one module and the head-selection seam (new section above).** `application/review_revision_comparison.py` owns the explicit revision-comparison policy; `application/knowledge_review.py` (825 → 843 lines) gains one import plus the one `compose_review` call and loses the private both-sides preference, with `_knowledge_pane` rendering the selection through `_selected_statements`. **Enforced rows re-cited in the same pass:** the L6-section delegation ranges (`side_content` import `93-96` → `101-105`, `_knowledge_pane` `694-727` → `714-761`), the selection-channel row (`_rows_remaining` `542-553` → `562-574`), the comparison-reader row (`_comparison_attribution` `459-469` → `480-492`), the composition row (`_selector_kind_or_absence` `597-606` → `617-628`), the inventory-limit row (`_limitations` `628-651` → `670-695`), the entry-operation row (now three ranges `206-286`/`287-320`/`341-367`), and the before-half case row (`809-847` → `865-905`). Header names this leaf's candidate row. No verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the stamp.
- 2026-09-22T09:20:00+02:00 — 260921-ICR-L4 curator (gate repair pass on the merged line): **enforced rows re-cited** (seam/binding/cursor/page/absence/test/refusal/scope/namespace/task-context rows to merged declarations; stale duplicate CandidateResolution row dropped; Hot Path rows in `__init__.py.md` re-pointed). Wording unchanged; no stamp advanced.
- 2026-09-22T09:15:00+02:00 — 260921-ICR-L4 curator (sync-merge resolution of the parked candidate against the landed line, merged base code `d21bc8a6` / memory `75bb4d65`): **additive union with landed `260921-ICR-L14`/`260921-ICR-L3`.** Both sides' sections and history kept; the L4 section above stands beside L14's record-owner section and L3's content-read section. Header names the merged production line on the stamp and this leaf's candidate row. No verification stamp was advanced.
- 2026-09-22T08:30:00+02:00 — 260921-ICR-L4 curator (uncommitted change set on `ar/260921-icr-l4`, base `d80a0513e928ef29a973527d09597c82c96fde87`; merged line counts at resolution: adapter 825, task-context 376): **this route gained one module and the attribution split (new section above).** `application/review_attribution.py` owns acquisition; `review_task_context.py` owns the pair measurement (184 → 372 lines); `review_candidate_resolution.py` owns the unreadable-candidate refusal (402 → 448); `knowledge_diff.py` supplies the reader (819 → 866); `knowledge_review.py` stays a delegator (831 → 837) with the hoisted observation and `_comparison_attribution`; `review_source_inventory.py` renders the partition (523 → 804) with scoped counts. One file-level card created, six updated (plus three in models/memory-knowledge and four test cards in the same pass). No verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the stamp.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T23:15:00+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **this route gained one module and one seam.** `application/review_source_content.py` (733 lines) now owns opening one review inventory entry into the actual content both bound code trees hold at its path; its vocabulary lives in `models/knowledge/review_source_content.py`, its route and third `ServingCollaborators` port are on the serving route, and its renderer is on the panels route. The section above records the three properties the module exists for (the generation is an input rather than a lookup; every side states its own truth with `absent` and `unavailable` kept apart; the content is real, bounded to 2 MiB and never a reference) and the **seam** a reader of this route should carry away: a path is read only from a **measured** change set — the requested generation's own, or, when that measurement cannot be made, the change set this leaf's review publishes — with `path_bound`/`path_bound_detail` naming which, and a path in neither refused in every state. It also records the two further admissions (complete object identities, and a **tree** as the after generation, with a commit/blob/tag refused by name while a missing object stays a per-side measurement) and the ownership the module deliberately leaves alone (`application/knowledge_review.py` is untouched at 831 lines, and the change set, the resolution, the currentness recheck, the byte-exact blob read and the bounded decode are the shipped owners'). **Citation accounting:** every range in the new section was derived from its construct's own extent in this candidate; one inherited stale row was re-derived in the same pass — the ingest-CLI row citing `add_arguments`/`run` carried `:133-209`/`:360-409` from before L20's renumbering, and those constructs are `:171-262`/`:660-692` now (the same values L20's own entry above records, which the row itself had not been updated to). No claim was deleted or re-worded for convenience. **No verification stamp was advanced**: the candidate is uncommitted, the stamp rows keep the production line this document was read against (`d80a0513…`, committed `2026-09-21T19:51:20+02:00`), and the governed closeout owns the real stamp.
- 2026-09-21T22:45:00+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **route body updated for a new owner and a removed collapse.** `application/review_evidence_records.py` joins this route as `ICR-R14@v1`'s production record owner — every owner-produced collection for one resolved candidate, plus a stated non-measurement for dependency currentness — and `knowledge_review.py`'s private `review_records_for` left the adapter for it (the name survives as a re-export, and the adapter is 831 → 819 lines while gaining the channel assembly). The section records the three-way collapse this removes (an empty tuple standing for "holds none", "could not be read" and "never asked"), the per-collection and per-record guards that keep one unreadable record from withdrawing its siblings, the two owner reads those guards needed, the matrix-owned channels reported from the matrix's own answer, and the two responsibilities this route deliberately leaves to R26 and R15. Six reference rows and one section were added; no earlier section was re-worded, because each of them records its own leaf's increment. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained as recorded (`d80a0513…` / `2026-09-21T19:51:20+02:00`), which is the production line this reading was against; the candidate row added at the top names the uncommitted candidate, no stamp was invented, and the governed closeout's metadata refresh owns the real one.
- 2026-09-21T22:16+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **the mechanically projected ranges this document was carrying were re-read against the constructs they now name, and the projection records were replaced by this review.** The mechanical anchor-range projection this leaf's citation pass ran wrote ``compose_review`` → mcp/src/agents_remember/application/knowledge_review.py:296-392 into this document's Update History. This pass read each affected claim against the construct inside the range it now cites — the wording is retained where the construct supports it and the range was left as the projection re-derived it only after that reading — so the ranges are curator-read evidence rather than unreviewed projections, and the projection bullets are superseded by this entry rather than kept beside it. The claims are not otherwise re-worded, no anchor was renamed, no citation was dropped and no verification stamp was advanced: the candidate is uncommitted and the governed closeout's own metadata refresh owns the real stamp.
- 2026-09-21T19:16:12+00:00: Generated citation repair: "def read_knowledge_review(" repointed to mcp/src/agents_remember/application/knowledge_review.py:161-161. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T20:44:00+02:00 — 260921-ICR-L11 curator, **memory-side sync conflict resolved as a UNION with the incoming `260921-ICR-L20` line; no side and no claim was dropped.** The header keeps both candidate rows and one `lastUpdated`; both sections are kept — this leaf's `260921-ICR-L11` section and `260921-ICR-L20`'s, each in the position its own pass wrote it — and both history entries are kept with this leaf's first. **Citation accounting:** this document carries no range into the two test manifests; its ranges into `durable_evidence.py` (`:58-69`), `errors.py` (`:180-190`, `:193-203`) and the new application modules were re-read against the merged code line and are unchanged. **No claim was corrected here.** **No verification stamp was advanced** — the stamp rows are outside the conflict and keep the incoming `945ddad6a9c90fbf5d7eef7546b9e69714c6c4fc` / `2026-09-21T18:46:40+02:00`.
- 2026-09-21T20:20:00+02:00 — 260921-ICR-L11 curator (uncommitted change set on `ar/260921-icr-l11`, base `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`): **this route gained five modules and the leaf's keystone record.** `260921-ICR-L11` (ICR-R11@v1) added `review_comparison_generation.py` (the immutable manifest, its layout under the one durable root, the deletion record, the re-derived generation id and the directory-name agreement), `review_comparison_freeze.py` (the production entry, the one-rename publication, the stale-stage sweep and reclaim-on-failure), `review_comparison_retention.py` (custody measured against **named durable history only**, both halves copied by the storage snapshot owner), `review_comparison_reclamation.py` (the two deletion owners, the record written before the deletion, the measured digest) and `review_comparison_reopen.py` (per-channel states and `unavailable_channels()`). The section records the two route-level boundaries as boundaries rather than defects: **the freeze is deliberately not wired to any route or read path** — ICR-R21 wires it at closeout, so the absence of callers is not evidence of dead code — and a **relocated coordination root degrades the reopened source channel to `missing`**, ruled the boundary of ICR-R12/R13, which own historical resolution and may record a relative repository identity or add a resolution input. Five file-level cards were created in the same pass, and the two typed failures the retention and reclamation boundaries raise were added to `errors.py`'s card. Verification metadata is **not** advanced on the previous values: the candidate is uncommitted and the governed closeout owns the stamp.
- 2026-09-21T18:35+02:00 — 260921-ICR-L20 curator, **memory-side sync conflict resolved as a UNION with the incoming `260921-ICR-L6` line; no side and no claim was dropped.** Both sections are kept: `260921-ICR-L6`'s statement-side section first and this leaf's publication-route section after it. Every range the resolution keeps was then re-derived against the merged candidate rather than shifted by a remembered delta (every row in the two sections was read against the merged candidate, and the adapter rows this document carries took the merged extents (`compose_review` `:377-452`, `_open_dataset_pair` `:455-500`, `_review_matrix` `:503-530`, `_selector_kind_or_absence` `:575-584`)); where both sides cited the same construct the merged extent was taken, and two claims that had become untrue in the merged state were corrected rather than kept in two wordings (the composition row named four constructs against three ranges and now cites all four). **No verification stamp was advanced:** the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is exactly what the incoming line recorded (`9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75` / 2026-09-21T18:13:19+02:00 where that line carried it), this leaf's candidate reading was recorded in the entry as metadata and not as a stamp, and the governed closeout owns the real commit.
- 2026-09-21T18:20:00+02:00 — 260921-ICR-L6 curator (uncommitted change set on `ar/260921-icr-l6`, merged base `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **this route gained one module and one seam, and the entry was revised at the sync so the document states the merged line rather than either side of it.** `application/review_statement_sides.py` now owns the pane-1 statement-side data contract (the three-outcome side state that is read rather than inferred from empty text, the essential conditions, the comparison's own field roster, and the `None`-means-absence value reader with its labelled canonical `structured_value_text` projection); `application/knowledge_review.py` is 888 → **831 lines** and delegates through one import block and four calls inside `_knowledge_pane`; and the wire-visible delta is that a **changed structured field** no longer serves `None` on both sides but each side's own projection. The section states plainly that this is the **fourth** responsibility the adapter has handed out on this master line and the only one that leaves no alias. The renderer half lives in `dashboard/src/panels/review/KnowledgeStatements.tsx`. **Corrected rather than merged:** the sibling-module ranges this document cites were re-derived against the merged tree where L18's line was stale — `unreadable_half_refusal` is `knowledge_before_half.py:347-377`, `REVIEW_CANDIDATE_RELATIVE_ROOT` is `review_candidate_resolution.py:77-77` and the two published half-names are `83-84` — while the L18-owned ingest and generation ranges are kept as L18 measured them because that code is L18's. **Sync accounting:** this document's memory-side conflict was resolved as an **additive union** — leaf `260921-ICR-L18`'s section is kept whole above/below this one, and this leaf's section and entry are kept whole beside it; no side was chosen wholesale and no claim was dropped. One observed gap is recorded rather than repaired: L18's section on this document arrived from the landed memory line **without an Update History entry of its own**, so this resolution preserved it exactly as it was carried and invented no record for another seat. Verification metadata is **not** advanced: the stamp is L18's `71a4433e686b3380af97a0836bb82bab2c8f2aad` / `2026-09-21T16:29:06+02:00`, which this leaf neither advances nor regresses, and the candidate is uncommitted so the governed closeout owns the real stamp.
- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **body update for the route's new module and the seam this leaf drew.** This route gained `application/knowledge_publication_route.py` (the ordinary publication route's three decisions: the declared location, the admission derived from the run's own captured baseline, and the read-back through the reader's owner) and lost nothing: it composes `published_intent`, `knowledge_before_half`'s captured-dataset read and `knowledge_baseline_generation`'s `CapturedBaseline` rather than reimplementing them. The section states the boundary at this route's altitude — the CLI owns the *selection* and the route owns what the declared selection means, with the renderer extracted to `cli/knowledge_ingest_report.py` so the CLI's growth is R20's own decision surface — and records the one consequence repair outside the leaf's files (`published_intent.py`'s docstring and its `PUBLISHED_DATASET_NAME` comment, text only). **Citation accounting:** every range this section carries into the new module, the CLI, the renderer and the test module was derived from its construct's own extent in this candidate rather than carried, and the rows this document already carried into `cli/knowledge_ingest.py` were re-derived in the same pass — the module renumbered completely (541 → 692 lines), so `_placement_refusal` `:292-316` → `:477-501`, `_place_review_baseline` `:319-357` → `:504-542` and `run` `:360-409` → `:660-692`. No claim was dropped and no row was deleted. No verification stamp was advanced; the governed closeout owns it.
- 2026-09-21T15:25+02:00 — 260921-ICR-L5 curator, **the second quality pass's enforced rows re-read and re-cited; every one of them was a range that had drifted out from under its anchor.** Rows repaired here by re-deriving each range from the construct's own extent in the merged candidate, with claim wording retained because each claim still states what the code does: the `read_knowledge_view` row, whose anchor resolves in `application/knowledge_views.py` rather than in the adapter, so the row now cites the operation's owner (`86-112`). No verification stamp was advanced — the working tree still differs from every recorded stamp, so closeout owns that stamp.
- 2026-09-21T15:10+02:00 — 260921-ICR-L5 curator, **the quality checklist's enforced rows on this document re-read and re-cited against the merged candidate.** The entry-operation row now cites `_reviewable_entries` beside `list_knowledge_review_entries` and `_selected_item_count`, because the anchor the claim's own words need is the one that exists in this file while the operation itself now lives in the adapter at `:207-288`; the two reopened claims the checklist named (`compose_review`, and `resolve_review_candidate`, which did not exist at this document's recorded verification commit) were re-read against their current anchored constructs and their wording retained, because each still states what the code does. The `read_knowledge_view` claim in the L20 section was left as it stands rather than re-cited: it asserts what the matrix read contributes, and its anchor resolves in `application/knowledge_views.py`, which is the operation's owner. No verification stamp was advanced — the working tree differs from every recorded stamp on this document and closeout owns that stamp.
- 2026-09-21T14:30+02:00 — 260921-ICR-L5 curator, **the sync's memory-side conflict in this document resolved as a UNION with the sibling module's file attribution kept and every range re-derived against the merged candidate.** The reference table of the section below now cites the resolution, the pair preflight, the namespace read and the three `REVIEW_*` constants where they live (`application/review_candidate_resolution.py`) while the adapter keeps only what it still owns, and the `list_knowledge_review_entries`, `_selected_item_count`, `review_records_for`, `_compare` and `read_knowledge_view` ranges were re-measured against the merged 1,126-line adapter -- L1's own last pass measured 1,113 lines, before this leaf's 13 lines landed on top. This leaf's own section above is kept whole and one claim in it **was corrected rather than merged**: it said the adapter's over-rail condition was carried forward, which the merge resolved by moving the resolution out. No verification stamp was advanced.
- 2026-09-21T14:15+02:00 — 260921-ICR-L5 curator (uncommitted change set on `ar/260921-icr-l5`, code base `f745e16659c5602252bb185a2ffccc356c2bde26`): **this route gained two modules, and the section above states the boundary the leaf drew.** `application/knowledge_before_half.py` (the before half's layout, its origin record and its four-state read) and `application/knowledge_first_generation.py` (all-or-nothing establishment through the shipped creation owner, under the committed candidate's own recorded namespace and input pair) are new files; `application/knowledge_review.py` gained one import and two call sites for `unreadable_half_refusal`, and `application/knowledge_curator_ingest.py` gained `_selected_baseline`, which reads a selected baseline on every run — resume included — so an unreadable fork point is the shipped `selected_input_unavailable` refusal rather than a run that proceeds without it. The section records the seam-policy position honestly: the adapter stayed a delegator, and it was already over the 1,200-line rail at this leaf's base (1,281 lines), so that condition is carried forward rather than resolved -- and the merge **resolved it**: L1's landed extraction moved the resolution out, so the adapter is 1,126 lines in the merged candidate against the 1,200-line rail. **Citation accounting:** every range into the two changed modules was re-derived from its construct's own extent rather than carried — this leaf moved every anchor below `:1325` of `knowledge_curator_ingest.py` and every anchor below `:36` of `knowledge_review.py` — including the ranges no checklist row named. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained exactly as recorded; no stamp was advanced or invented and no commit was made.
## Update History
- 2026-09-21T00:20+02:00 — 260915-KS-L47 curator (uncommitted change set on `ar/260915-ks-l47-ar`, code base `be325216416326a66950c9e320ff8d08f41e5d66`, memory base `2f415d930d1f8122ae0226bd296add3265600749`): **body update for the route this leaf's change set touches — the two write-path repairs this leaf lands in `knowledge_curator_ingest.py` -- the retry guard bound to the whole normalized semantic write intent, and explicit anchor reuse refused before the plan exists -- plus the recorded (not repaired) migration/census usability gap and the withdrawn false universal in the digest docstring. The route section above states the acceptance each repair closes.** This is a body change and not a metadata-only refresh: the route section carries statements the overview did not make before. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained exactly as recorded, because no commit contains this body and no stamp was measured on it; no stamp was advanced or invented. No commit was made.
- 2026-09-20T20:56+02:00 — 260915-KS-L48 curator (uncommitted change set on `ar/260915-ks-l48-ar`, code base `f745e16659c5602252bb185a2ffccc356c2bde26`, memory base `c0e559efdf9f3b6ac81be1925329b04c06d27b4c`): **the reopened `_replayed_outcome` claim re-read against the committed bytes and re-cited, with both questions the checklist puts to a reopened claim answered here.** (1) Does the construct the new range covers support what the claim's own words state? Yes. The claim reads "The idempotency key, the content guard, and the replay decided from the dataset", and `_replayed_outcome` (`mcp/src/agents_remember/application/knowledge_curator_ingest.py:1175-3529`) is still the entry a replay is reported by: this leaf gave it the stored route outcomes beside the plan (`_replayed_outcome(plan, routes)`), and it renders each route `reused` because the candidate already holds the association, so the wording stands unchanged. (2) Did the range arrive by mechanical anchor-range projection, or was it rebound from a mention? By projection: the range this row carried (`knowledge_curator_ingest.py:3138-3155`) had been written by the product's mechanical fixer (`ccr-r10@v1`) and went stale when the construct moved to `3241-3254`. Both ranges on the row were therefore re-derived by hand from the constructs' real extents after reading them — `_replayed_outcome` `3138-3155` → `3241-3254` and `_with_replays` `1720-1727` → `1753-1760` — and no delta was added to an old number. The mechanical fixer was not run on this document, so no generated repair bullet is written and no claim in this document is reopened on this edit's account.
- 2026-09-20T17:56:44+00:00: Generated citation repair: `_cycle01_reused_label_identity` repointed to mcp/tests/test_knowledge_curator_ingest_list.py:2309-2426. No content impact: mechanical anchor-range projection bound to citation source snapshot 0ec9923f9ff96eb03f47df0807f31aee273debc483ca458b826f6919fe15bd3f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:23:31+00:00: [mechanical projection record, RETIRED 2026-09-24T10:20+02:00 by the 260921-ICR-L29 curator] A mechanical anchor-range projection was run on this date against citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; a projected range is not a reading of the claim it points at, so this line is retained as a historical record only and is not evidence that the citation is current. The hand-derived ranges in this document's tables are the ones in force.
- 2026-09-20T17:17:10+00:00: [mechanical projection record, RETIRED 2026-09-24T10:20+02:00 by the 260921-ICR-L29 curator] A mechanical anchor-range projection was run on this date against citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; a projected range is not a reading of the claim it points at, so this line is retained as a historical record only and is not evidence that the citation is current. The hand-derived ranges in this document's tables are the ones in force.
- 2026-09-20T17:17:10+00:00: [mechanical projection record, RETIRED 2026-09-24T10:20+02:00 by the 260921-ICR-L29 curator] A mechanical anchor-range projection was run on this date against citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; a projected range is not a reading of the claim it points at, so this line is retained as a historical record only and is not evidence that the citation is current. The hand-derived ranges in this document's tables are the ones in force.
- 2026-09-20T14:20+02:00 — 260915-KS-L43 curator, **memory-side sync conflict resolved as a UNION; no side dropped.** The memory source branch advanced to `92f444b04` (260915-KS-L45) while this leaf's curation was in flight, so the sync's re-apply conflicted in this file. Both sides were kept because both are true: 260915-KS-L45's landed additions (the Intent-review entry path, the two published half-names `REVIEW_BASELINE_DIRECTORY`/`REVIEW_CANDIDATE_DIRECTORY`, the `missing_dataset_half` pair preflight, the receipt-derived `review_namespace`, and the enumerating reads) and this leaf's 260915-KS-L43 edits (the allocated-identity/derived-citation split, the retry key and its journal, the explicit anchor reuse, and the recovery's journaled decisions with the bounded cycling refusal). Where the two sides carried the same row in different line numbers, the row was re-measured against the moved line rather than picked: L45 curated against `fb719f89` and this leaf's source moves every citation below `:306` of `knowledge_curator_ingest.py` and renumbers `cli/knowledge_ingest.py` entirely, so the surviving ranges are the post-merge measurement for both. One **contradiction** is recorded rather than silently resolved: the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` frontmatter pair is L45's (recorded against the moved line, the newest verification on record), while the candidate reading recorded in the entry is this leaf's reading — two different claims, kept beside each other instead of one overwriting the other. No verification stamp was advanced by this leaf.
- 2026-09-20T14:20+02:00 — 260915-KS-L43 curator (uncommitted change set on `ar/260915-ks-l43-ar`, code base `fb719f89`): **this route gained the L43 section, and the L39 section's identity claim had its scope corrected rather than being called false.** L39 stated the identity move as complete: "identity stopped being a function of the code base commit", every id a `uuid5` over the repository's namespace. That was true of the citation identities and was false of the invariant and its first revision, whose only distinction was the entry's local hand-off label — so two independent tasks numbering an entry `R-LOCAL` and stating different truths were handed one record, and production sync refused `duplicate_identity` on it. The new section states the developer's 2026-09-20 ruling at route altitude: the label carries no identity meaning, the API allocates and persists the canonical identity, continuity is by **naming** the stored identity (`invariant_id`, and now a target's `anchor_id`), and a retry rides a separate idempotency key; the anchor is keyed on the allocated revision and the claim on its own two endpoints; and **scoping the stored identity to the authoring enclosure is named as the forbidden design rather than the repair**. The recovery route beside this plane gained its own paragraph, because a two-conflict retained merge used to alternate forever (twelve applications to the cap, no settlement) and now journals every accepted decision and refuses to cycle (two applications, settled). The L39 section's two identity paragraphs were corrected in place: the "identity does not move with the baseline" paragraph now says which identities that was true of and that a reused label is not a claim that two entries are one record, and the "two constructs in one file" paragraph records that L43 sharpened the discriminator. The L30 section's `derived_identities` paragraph was corrected the same way, and five rows were re-measured (`_TargetIdentities`/`_target_identities` already shifted by the citation fixer, the operation and selection ranges to their own extents) with seven rows added for the allocation machinery, the citation keys, the explicit-reuse input, the recovery pair and the case that measures the ruled semantics. No verification stamp was advanced and no verification row was touched: the candidate is uncommitted and closeout owns the real code and memory commits; the entry names the candidate this reading was performed against. No commit was made.
- 2026-09-20T14:20+02:00 — 260915-KS-L43 curator, **the two projected ranges are disposed of by real re-citations, not by a note.** The generated repairs of 12:00:25 moved the ranges of the `_identity` rows and of the `_admitted_candidate` row mechanically, and a mechanically projected range is unverified evidence: the projection picks the declaration it writes, so it satisfies its own currency test by construction. This entry replaces both. Each row was re-read at the construct its range now covers: `_identity` is `mcp/src/agents_remember/application/knowledge_curator_ingest.py:3176-3212`, and the row's words — that identity derives over the repository's own namespace and never the enclosure's base commit — are what that function's own docstring and body state, with the discriminator now naming what each citation identity is *about*; `_admitted_candidate` is `:1257-1299`, and the row's words — that admission resumes, forks a selected baseline or creates an empty candidate — are what that function states. Both rows were **re-cited deliberately after reading the constructs**; the wording of both is **retained**, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-20T14:20+02:00 — 260915-KS-L43 curator, **the two projected ranges are disposed of by real re-citations, not by a note.** The generated repairs of 12:00:25 moved the ranges of the `_identity` rows and of the `_admitted_candidate` row mechanically, and a mechanically projected range is unverified evidence: the projection picks the declaration it writes, so it satisfies its own currency test by construction. This entry replaces both. Each row was re-read at the construct its range now covers: `_identity` is `mcp/src/agents_remember/application/knowledge_curator_ingest.py:3176-3212`, and the row's words — that identity derives over the repository's own namespace and never the enclosure's base commit — are what that function's own docstring and body state, with the discriminator now naming what each citation identity is *about*; `_admitted_candidate` is `:1257-1299`, and the row's words — that admission resumes, forks a selected baseline or creates an empty candidate — are what that function states. Both rows were **re-cited deliberately after reading the constructs**; the wording of both is **retained**, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `create_revision` repointed to mcp/src/agents_remember/memory/knowledge/store.py:291-325. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): **this route gained the reviewer's entry operation and the three facts that make a live pair actually resolvable.** The body now records (1) `list_knowledge_review_entries` — the subjects the resolved pair can be compared on, resolved through the identical operation the comparison uses and offered only when the shipped `diff_knowledge_scope` answered for that identity, with a refused subject **dropped rather than listed with a zero**; (2) the two **published** half-names `REVIEW_BASELINE_DIRECTORY`/`REVIEW_CANDIDATE_DIRECTORY`, exported because the ingest CLI derives its candidate directory from the same names, which is what makes the authored candidate and the reviewed candidate one directory; (3) `missing_dataset_half`, the preflight that turns an absent half into the typed `candidate_dataset_absent` refusal naming **which** half, where before an absent baseline raised a storage error from inside side construction; and (4) `review_namespace`, which reads the namespace from the candidate's own sealed receipt because the dataset is bound to a namespace id — measured on this leaf's fixture as `bound to 40d350a6-…, not to the requested repository namespace agents-remember`, a failure every live review of a real candidate would have hit. Six reference rows were re-cited to their constructs' current extents and five were added. No verification stamp was advanced.
- 2026-09-20T06:50+02:00 — 260915-KS-L40 curator (uncommitted CYCLE-02-remainder change set on `ar/260915-ks-l40-ar`, code base `f79f4db7`): **route body updated.** This route's third knowledge seam changed shape: `application/knowledge_merge.py`'s `merge_conflicted_stages` now returns `KnowledgeStageSettlement(settled, conflict, refusal, detail)` instead of a boolean, so the engine's typed refusal and its row-level `MergeConflict` travel out of the seam instead of being discarded at it, and the four ways a path never reached the adapter are named rather than collapsed into one `False`. The same module passes the caller's one `AuthoredReconciliation` through to the adapter unchanged. `application/worktree_tools.py`'s `worktree_sync_tool` now takes the paired `resolution: SyncResolutionInput | None` (the action plus the decision it may carry) rather than a bare `resolution_action`, pairing forced by the `PLR0913` ceiling and by the driver refusing the two as a pair. A body change, not a metadata-only refresh.

- 2026-09-20T03:57:45+00:00: Generated citation repair: `resolve_knowledge_merge_base` repointed to mcp/src/agents_remember/application/knowledge_merge.py:59-75. No content impact: mechanical anchor-range projection bound to citation source snapshot ef4a9932e0393a408ecd0f26b5bc2e0e1e335ad90b9e47a16092ffd6f3403af3; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T03:57:45+00:00: Generated citation repair: `KnowledgeMergeSeamDefect` repointed to mcp/src/agents_remember/application/knowledge_merge.py:90-91. No content impact: mechanical anchor-range projection bound to citation source snapshot ef4a9932e0393a408ecd0f26b5bc2e0e1e335ad90b9e47a16092ffd6f3403af3; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T03:57:45+00:00: Generated citation repair: `ConflictCommits` repointed to mcp/src/agents_remember/application/knowledge_merge.py:223-234. No content impact: mechanical anchor-range projection bound to citation source snapshot ef4a9932e0393a408ecd0f26b5bc2e0e1e335ad90b9e47a16092ffd6f3403af3; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T02:12+02:00 — 260915-KS-L32 memory-side conflict resolution (uncommitted; this worktree, code base `7dcec036`, merged tree = L30's landed `7ca3ac48` plus this leaf's four modified paths): **resolved two reference-table hunks in this route overview.** Both rows cite files this leaf did not modify, so upstream's ranges were kept: `models/knowledge/candidate.py:659-676; 498-529; 638-655; 656-656; 236-236` for the resolution-shape row (upstream's side is also the superset — this leaf's side had dropped `498-529`, `638-655` and `656-656`, all of which are restored rather than deleted, and both sides agree on the class's own extent `659-676`), and `mcp/tests/test_knowledge_read_boundaries.py:502-502; 772-772` for the baseline-nodes row, whose two quoted anchors were read at exactly those `def` lines in the code worktree (this leaf's side cited the wider `499-502; 759-772`, which also holds them). No claim was re-worded, no anchor, row or citation dropped, and no verification stamp advanced.
- 2026-09-20T01:37+02:00 — 260915-KS-L31 curator (uncommitted change set on `ar/260915-ks-l31-ar`, base `7dcec036`): range repair only; every claim's wording and every anchor set kept. Two rows were re-derived against the tree this leaf's own line moves left behind. The L3 candidate-write row's `CandidateResolution` citation was a mechanically projected range set (`:182-223; :498-529; :638-655; :656-656; :236-236`) that stops one line short of the declaration every time, so it read the class's neighbours rather than the class; it now cites the declaration's own extent `mcp/src/agents_remember/models/knowledge/candidate.py:659-676` beside `KnowledgeContext` at its own class extent `mcp/src/agents_remember/models/knowledge/candidate.py:236-277` — the four projected ranges held neither named anchor and were dropped rather than carried, and the duplicate row beside it already cites `:83-424`. The L7 read-seam row's two quoted test names had moved again (the L23 residue entry repointed them to `:499-499`/`:759-759`; the declarations now stand at `:502` and `:772`), so each now cites its own declaration extent, `mcp/tests/test_knowledge_read_boundaries.py:502-533` and `:772-807`. No verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-20T01:36+02:00 — 260915-KS-L33 curator (uncommitted change set on `ar/260915-ks-l33-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): No route impact: this route overview was re-read against this leaf's one changed governed source, `application/knowledge_curator_ingest.py`, and nothing in this body moved. The change is internal to that module's producer contract — the realization role a curator hand-off entry stores is now the word its producer stated, validated against the shipped vocabulary, or the vocabulary's own non-answer, and it is no longer inferred from locator syntax — and this overview states no realization-role derivation, no role/locator equivalence and no curator-ingest citation rule, so no bullet, boundary or reference row here held a claim that became false. The L33 entry below records the same review in prose; this entry carries the exact in-band marker the route-overview refresh gate requires, bound to the uncommitted candidate `ar/260915-ks-l33-ar` on base `7dcec036`. No verification stamp is advanced by this entry: the governed closeout owns the real code and memory commits, and no acceptance claim is made.
- 2026-09-20T00:55+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): hand-read the two enforced rows this route overview carries. One is cleared (`CandidateResolution` in "The resolution shape whose missing dataset-identity field makes the read the only source of that value."): its first range `182-223` no longer reached the class the claim names, so it was replaced with the class's own extent at `candidate.py:659-676`; every other range in the row was left as written. The other row ("D13's dual repair…") still cannot pass: its anchor `` `AdmittedEnclosure.code_repository_root` `` is a dotted spelling that occurs nowhere in the tree — the attribute it names is declared at `capsule.py:198` inside `AdmittedEnclosure` (`186-202`) and read onto the projection request at `capsule.py:282` — so the anchor, not the range, is what needs re-wording; that is the claim's own content and is left for a curator. The range that used to cite the class's own block (`186-202`) was nonetheless replaced with `275-289`, which holds the projection-request read the claim's second half is about; no claim was re-worded, no anchor or range was dropped to silence a finding, and no verification stamp was advanced. No commits.
- 2026-09-19T22:49:08+00:00: Generated citation repair: `merge_resolved_knowledge_datasets` repointed to mcp/src/agents_remember/application/knowledge_merge.py:74-83. No content impact: mechanical anchor-range projection bound to citation source snapshot e67b35357c3610162648ff9c1506b2bd840c93c142fe18de408cd68cfbaf5daa; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 2 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `test_a_baseline_read_serves_a_task_free_context_and_reaches_the_whole_selected_scope`; `test_a_continuation_naming_a_position_past_the_selection_refuses_rather_than_escaping`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 2 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `overview.md:839` (`CandidateResolution`, `KnowledgeContext`); `overview.md:1094` ("test_a_baseline_read_serves_a_task_free_context_and_reaches_the_whole_selected_scope", "test_a_continuation_naming_a_position_past_the_selection_refuses_rather_than_escaping").
- 2026-09-19T19:54+02:00 — 260918-TSIP-L6 (uncommitted change set on `ar/260918-tsip-l6-ar`, base `a1351504`): recorded the route's three caller-visible repairs — the provider refusal sites (`T34`, eight tools), memory baseline adoption answering `BranchAuthorityUnavailable` in the envelope (`T34`), and the guidance guard that binds a response's guidance to its own address (`T54`). Every citation range re-derived against the repaired files. Verification metadata stays closeout-owned.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `CURRENT_GENERATION` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:482-482. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `CURRENT_GENERATION` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:482-482. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: `GENERATIONS` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:456-466. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: `CURRENT_GENERATION` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:479-479. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: `CURRENT_GENERATION` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:479-479. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_the_application_seam_is_read_only_carries_the_operation_and_moves_no_selection" repointed to mcp/tests/test_knowledge_family_composition_boundaries.py:615-615. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "def skills_install_payload("; "def task_reopen_payload(" repointed to mcp/src/agents_remember/mcp/tools/core.py:146-146; mcp/src/agents_remember/mcp/tools/task_doc.py:35-35. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: added the section above — `memory_quality/controller.py` now consumes the new governing-overview check and extends its findings into the gated repair set, with the publication placements (`response`, not `payload`; outside the closed `AVAILABLE_CHECKS` mapping) recorded as deliberate. Verification metadata advanced to this leaf's frozen code base.
- 2026-09-17T11:40+02:00 — 260915-CAPS-L14 curator: recorded this route's share of the leaf's change. `application/prepared_certification.py` (one of this leaf's 13 modified tracked paths) now acquires its citation source index through the new **`_admitted_source_index`**, which converts a `SourceIndexError` into a named `CertificationContractError` (`citation-source-index-unavailable`) carrying the cause and the operator move — so the closeout gate cannot be bricked by an index it did not choose, while satisfiable caps still skip and report. `application/memory_tools.py` gained `_citation_trees` and the `excludes` field on `CitationOperationScope`, the one construction point that carries a caller's own excludes plus the memory layer's settings into all four citation operations. Added the two reference rows above. Also **moved the `prepared_certification.py` file card** to this route: the source left `worktrees/integration/closeout/` in `806649b9` and the card had been left behind, so it resolved to a file that no longer exists. Verification metadata is left at this leaf's synced base `0346da9c`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code commit.
- 2026-09-17T09:55+02:00 — 260915-CAPS-L15 curator: **the produce side gained the production caller this
  route recorded as missing, so the body was corrected rather than annotated.** The L7 section's closing
  paragraph said "the produce side has no production caller yet — the only caller is the test fixture"
  and routed the wiring to `CAPS-R15@v1`. That wiring now exists:
  `application/role_capsules/launch.py::_compile_eve_task` calls `materialize_eve_binding` for a wired
  launch point, the runtime's **own** gate accepts the carrier from the launch's own captured cwd and env,
  and the live runtime's system block carries it (`E8`). The paragraph now states which half of the
  `L7R-4` transfer is discharged — **the produce side has a production caller, verified at the
  consumer's gate** — and which half is not: a dispatched eve seat still cannot start, because the next
  refusal is the inherited settings-chain gate (`D22`, owner **L17**). The reference table gained the
  production caller, the production-chain evidence row, and the corrected `verify_capsule_binding` range,
  and the fixture row no longer stands in for the missing caller. Verification metadata moves to this
  leaf's base `15fa0e2c`; the candidate is deliberately uncommitted, so the governed closeout stamps the
  real code commit and no hash or fingerprint was invented here.
- 2026-09-16T20:42+02:00 — 260915-CAPS-L7 curator: this route gained `eve_capsule/`, the **produce
  side** of the eve capsule/workspace binding seam, recorded in the new
  `## 260915-CAPS-L7 The Eve Capsule Produce Side` section. It is not a second compiler: it calls the
  L4 capsule surface and the L3 projection and transports a decided value into the carrier one bound eve
  runtime reads. The section names the load-bearing boundaries a reader of this route needs — admission
  precedes execution (no carrier is written on any refusal path, and the written carrier is read back and
  required to parse equal); the projection is re-derived and required to be byte-identical to the
  capsule's task context rather than trusted; write surfaces follow the role authority table with the
  **smallest** set as the fallback so an undeclared role cannot inherit the memory write; and the carrier
  lives outside the admitted workspace so the instructions are not a file the model can rewrite. It also
  states where the seam's other half lives (models carrier format, serving launch proof, TypeScript
  in-process reader) and that **the produce side has no production caller yet** — wiring one is
  `CAPS-R15@v1`'s obligation under an explicit transfer, not a closure. Verification metadata moves to
  the leaf's synced base `23cc7a72`; the candidate is deliberately uncommitted, so the governed closeout
  stamps the real code commit and no hash or fingerprint was invented here.
- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator (uncommitted change set on `ar/260915-caps-l4`,
  base `b00a4ac2`): added the `skill_resources/` package to this route and recorded its two
  deliberately separate surfaces — the narrow read-only capsule operation (seat derived from the task
  document's altitude, role string validated and never authoritative, source set routed by the
  canonical composition manifest, no caller-named path) and the skills transport's reading half
  (discovery registry separated from delivery, containment proven before the read, bytes re-checked
  against the recorded revision). Recorded two facts a reader of this route needs: a refusal is a typed
  **value** carrying status, detail and remedy with the binding preserved in both shapes, and the served
  corpus is the **packaged** `package_data/runtime/skills/` copy rather than the canonical root
  `skills/` tree (a corpus root, its manifest and its publishing origin are admitted together). Stated
  that the route's ordinary boundary is unchanged: no MCP or protocol types are read at this layer.
  Verification metadata remains closeout-owned; no acceptance claim is made.
## 260915-KS-L4 The Snapshot Lifecycle Joins As A Second Seam

The route gained one module, `application/knowledge_snapshot.py`, and no new authority. It is the **second
composition seam**: the candidate lifecycle (create, clone, open, disposal authorization) and snapshot publication
are a different composed operation from the single candidate write, and keeping them apart leaves each entry point
readable as one intent rather than one module with two jobs.

Three things matter to a later reader:

- **The write destination is derived, not passed twice.** `candidate_write_destination` builds the
  `AdmittedKnowledgeDestination` from the admitted candidate's own layout, so a caller cannot write into one
  database and publish another; `admitted_candidate_destination` is the typed handle the admitted-authority path
  calls after its own checks, and it **confers no authority by itself** — it exists so a deserialized request
  cannot become admitted input.
- **Two publication entry points share one contract.** `publish_knowledge_snapshot` freezes and installs one
  candidate's point, while `publish_prepared_knowledge_snapshot` installs an already-frozen stage through the
  *same* path — so a caller that produced a validated closed database (a merged result, an import, a restored
  artifact) reaches a destination atomically against an expected identity, with no second install route to keep
  correct.
- **The read-side gate is exposed, not decided.** `knowledge_publication_state` returns the comparison between a
  live candidate and the closed snapshot a read is about to answer from; the caller decides what to do about a
  difference, because publishing is an explicit operation and no read may publish rows.

**Two non-claims the ruled design made explicit are recorded here because a later reader will look for them.**
This seam **creates no Git commit** — the published snapshot is a closed file, and capturing it into a memory tree
is the existing candidate-tree owner's operation — and **no IAS landing is reachable from it**; the writable
candidate belongs to the experimental master. And the wiring boundary did **not** move: like
`application/knowledge.py`, this module has **no non-test importer in `mcp/src`**, so its composed-path cases are
behaviour evidence about the boundary and not evidence that any tool is wired to it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The admitted-destination constructor that confers no authority by itself. | `admitted_candidate_destination` | mcp/src/agents_remember/application/knowledge_snapshot.py:67-82 |
| The write destination derived from the candidate layout rather than passed twice. | `candidate_write_destination` | mcp/src/agents_remember/application/knowledge_snapshot.py:85-99 |
| The three lifecycle delegations. | `create_knowledge_candidate`; `clone_knowledge_candidate`; `open_knowledge_candidate` | mcp/src/agents_remember/application/knowledge_snapshot.py:102-107; mcp/src/agents_remember/application/knowledge_snapshot.py:110-115; mcp/src/agents_remember/application/knowledge_snapshot.py:118-123 |
| The two publication entry points that share one contract. | `publish_knowledge_snapshot`; `publish_prepared_knowledge_snapshot` | mcp/src/agents_remember/application/knowledge_snapshot.py:134-139; mcp/src/agents_remember/application/knowledge_snapshot.py:142-147 |
| The read-side publication gate exposed rather than decided. | `knowledge_publication_state` | mcp/src/agents_remember/application/knowledge_snapshot.py:150-155 |
| The storage operations the seam delegates to, including the two locks that are never nested. | `create_candidate`; `publish_candidate_snapshot`; `publish_prepared_snapshot` | mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:88-100; mcp/src/agents_remember/memory/knowledge/publication.py:66-111; mcp/src/agents_remember/memory/knowledge/publication.py:114-170 |
| The disposal verdict whose authority the caller owns. | `authorize_candidate_disposal` | mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:144-176 |
| The composed-path harness that drives the seam end to end through the public operations. | `build_case`; `publish` | mcp/tests/snapshot_lifecycle_test_support.py:178-205; mcp/tests/snapshot_lifecycle_test_support.py:358-380 |

## 260915-KS-L5 The Merge Joins As A Third Seam

The route gained one module, `application/knowledge_merge.py`, and still no new authority. It is the **third
composition seam**, and it exists for the same reason as the second: a guarded common-base merge is a different
composed operation from a single candidate write, and a different one again from the lifecycle/publication half, so
each entry point stays readable as one intent rather than one module with three jobs. The three seams now divide
this route's knowledge surface cleanly — the write, the lifecycle-and-publication, and the merge — which is why
this module was added rather than more entry points on either sibling.

Two things matter to a later reader:

- **It resolves, merges, and returns the typed value unchanged.** `resolve_knowledge_merge_base` proves the three
  input identities, their structure and the Git base claim, returning the resolution; `merge_resolved_knowledge_
  datasets` runs the guarded merge against a proven base and returns the whole structural outcome, including the
  coverage of both deltas and the publication state when a destination was named. A failure is the storage layer's
  typed refusal, so a caller composing a tool response branches on one code rather than catching an exception.
- **The adapter is callable rather than wired.** No Git merge driver is installed, no attribute is configured and
  no commit is created anywhere on this path: the module is the exact seam a later, separately reviewed change
  would call. That is the requirement's own boundary — this increment supplies evidence and a callable boundary,
  not production configuration. *(**Superseded in part by `260915-KS-L31`**: the separately reviewed change
  arrived and the adapter now has one production caller, `worktrees/knowledge_conflict.py`, through the
  `merge_conflicted_stages` half recorded in the L31 section at the end of this route. The Git non-claims in
  this bullet survive the wiring unchanged.)*

The result this seam returns carries **no compatibility verdict**: a `structurally_merged` outcome is a statement
about the candidate's structure and nothing about whether the merged knowledge is correct. The wiring boundary also
did **not** move: like its two siblings, this module has **no non-test importer in `mcp/src`**, so its cases are
behaviour evidence about the boundary and not evidence that any tool is wired to it. *(**Superseded by
`260915-KS-L31`**: exactly one non-test importer exists now, and the L31 section names it and the structural
reason the driver half could not live in the worktree module that calls it.)*

| Finding | Anchor | Source |
| --- | --- | --- |
| The base-resolution entry point and its refusal-or-resolution contract. | `resolve_knowledge_merge_base` | mcp/src/agents_remember/application/knowledge_merge.py:59-75 |
| The merge entry point, including the carried statement that the result holds no compatibility verdict. | `merge_resolved_knowledge_datasets` | mcp/src/agents_remember/application/knowledge_merge.py:78-87 |
| The defect the layer below makes unreachable. | `KnowledgeMergeSeamDefect` | mcp/src/agents_remember/application/knowledge_merge.py:90-91 |
| The two storage operations this seam delegates to, in the order the seam exposes them. | `resolve_merge_base`; `require_session_capability` | mcp/src/agents_remember/memory/knowledge/merge_base.py:75-109; mcp/src/agents_remember/memory/knowledge/merge.py:131-163 |
| The vocabulary the seam takes and returns unchanged. | `MergeBaseRequest`; `MergeRequest`; `MergeOutcome` | mcp/src/agents_remember/models/knowledge/merge.py:221-251; mcp/src/agents_remember/models/knowledge/merge.py:286-325; mcp/src/agents_remember/models/knowledge/merge.py:478-520 |
| The unit node that drives the conforming merge end to end through the public operations. | "def test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate(" | mcp/tests/test_knowledge_guarded_merge.py:307-376 |
| The published-file freeze and install contract the merge's last step reuses rather than duplicating. | `freeze_closed_snapshot`; `publish_prepared_snapshot` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:92-137; mcp/src/agents_remember/memory/knowledge/publication.py:114-170 |

## 260915-KS-L6 The Portable Export/Import Joins As A Fourth Seam

The route gained one module, `application/knowledge_export.py`, and still no new authority. It is the **fourth**
composition seam over the experimental knowledge substrate, beside the single candidate write
(`knowledge.py`), the candidate-lifecycle/publication seam (`knowledge_snapshot.py`) and the guarded merge
(`knowledge_merge.py`), and it exists for the same reason as the three before it: exporting and importing a
whole dataset is a different composed operation from any of them, and keeping them apart leaves each entry
point readable as one intent.

- **It hands over and returns unchanged.** `export_knowledge_artifact` and `import_knowledge_artifact` delegate
  to `export_knowledge_dataset` / `import_knowledge_dataset` and return the storage layer's typed result as it
  is, so a caller branches on `state`/`refusal` rather than on an application-level wrapper.
- **Two halves are read-only and produce no database at all.** `validate_knowledge_artifact` answers whether an
  artifact is a complete export of a supported generation and what logical dataset it holds, and
  `canonical_body_of_artifact` returns that dataset's canonical body — **after validating it**, because a body
  is what a comparison is made of and a refused artifact has no identity to compare.
- **A refusal is a value on both halves**, including the file read: `read_knowledge_artifact` returns
  `selected_input_unavailable` for a path it cannot read and `invalid_export` for bytes that are not UTF-8,
  and nothing on this boundary raises an `OSError` or a `UnicodeDecodeError` for a caller to catch.
- **Two non-claims are carried where a reader of the artifact looks for them**: an export is **not** a filtered
  read response and **not** a Markdown projection, and an import creates **no Git commit** and restores **no
  Git ancestry**. Capturing an artifact into a memory tree, or committing a restored database, stays with the
  existing candidate-tree and closeout owner.

The wiring boundary did **not** move: like its three siblings, this module has **no non-test importer in
`mcp/src`**, so its evidence is behaviour evidence about the boundary and not evidence that any tool is wired
to it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The seam's five entry points and the non-claims it carries in its own docstring. | `export_knowledge_artifact`; `import_knowledge_artifact`; `validate_knowledge_artifact`; `read_knowledge_artifact`; `canonical_body_of_artifact` | mcp/src/agents_remember/application/knowledge_export.py:60-63; mcp/src/agents_remember/application/knowledge_export.py:66-74; mcp/src/agents_remember/application/knowledge_export.py:77-96; mcp/src/agents_remember/application/knowledge_export.py:99-109; mcp/src/agents_remember/application/knowledge_export.py:112-126 |
| The defect the layer below makes unreachable. | `KnowledgeArtifactSeamDefect` | mcp/src/agents_remember/application/knowledge_export.py:129-130 |
| The storage operations this seam delegates to. | `export_knowledge_dataset`; `import_knowledge_dataset`; `read_artifact` | mcp/src/agents_remember/memory/knowledge/export_import.py:136-196; mcp/src/agents_remember/memory/knowledge/export_import.py:199-250; mcp/src/agents_remember/memory/knowledge/export_import.py:263-296 |
| The vocabulary this seam takes and returns unchanged. | `ExportRequest`; `ExportResult`; `ImportRequest`; `ImportResult`; `PortableValidation` | mcp/src/agents_remember/models/knowledge/portable.py:36-44; mcp/src/agents_remember/models/knowledge/portable.py:101-133; mcp/src/agents_remember/models/knowledge/portable.py:47-63; mcp/src/agents_remember/models/knowledge/portable.py:66-98; mcp/src/agents_remember/models/knowledge/portable.py:136-176 |
| The nodes that drive the conforming round trip and the filtered-response refusal through the public seam. | "test_a_populated_dataset_round_trips_to_an_equal_logical_dataset"; "test_a_filtered_read_response_cannot_validate_as_a_complete_export" | mcp/tests/test_knowledge_portable_roundtrip.py:356-427; mcp/tests/test_knowledge_portable_roundtrip.py:712-739 |

## 260915-KS-L7 The Selective Read Joins As A Fifth Seam

The route gained one module, `application/knowledge_read.py`, and still no new authority. It is the **fifth**
composition seam over the experimental knowledge substrate, beside the candidate write (`knowledge.py`), the
candidate-lifecycle/publication seam (`knowledge_snapshot.py`), the guarded merge (`knowledge_merge.py`) and the
portable export/import (`knowledge_export.py`), and its subject is a different composed operation again: one
bounded, snapshot-consistent page of the recorded scope a seed names.

**Three boundaries this seam owns, each because getting it wrong is a different kind of wrong:**

- **The read is read-only, and that is how a refusal persists nothing.** The connection is opened through
  `open_read_only_database`, so the strongest statement available is a `SELECT`; "a refused read left the file
  byte-identical" is a property of the handle rather than a rollback the code remembers. `read_row_counts` is the
  measurement half — the same read-only handle, so a caller can take per-table counts before and after a refusal
  and compare.
- **A baseline read needs no task.** `task_ref=None` is served: the seam never resolves a leaf contract, never
  asks an enclosure owner for one and never fabricates a task, because planning has to be able to read recorded
  knowledge before a leaf exists.
- **A continuation is a binding, not a position.** Snapshot, context, selector, policy and schema are checked
  **before the file is opened** — a cursor binding another selection is a defect of the request and not a fact
  about the bytes, and reporting it as a snapshot problem would send the caller to re-select a dataset they
  selected correctly — while the manifest and the position are checked **after** the selection exists, before any
  page is built. No cursor refusal returns a partial page.

**The ordered sequence inside the one connection**: verify the declared snapshot through **three separate
comparisons** (namespace, schema generation, logical dataset — the schema check is its own statement rather than
a corollary of the digest, because a context can keep the file's real digest while declaring another generation);
select the scope; decide the typed absence (`registration_absent` for a path with no recorded claim,
`selector_absent` for an identity the snapshot does not hold, and a **recorded** identity with no memberships and
no claims served as an empty-but-real selection); check the continuation against the selection; cut the page; and
turn a page too small for its next item into `page_budget_too_small` with the exact minimum.

**`open_read_context` is the constructor, and it is what keeps the snapshot honest:** it opens the file
read-only, reads the logical identity the file actually holds and returns a context naming **that** snapshot, so a
caller cannot hand-write the snapshot a read will be verified against — it can only resolve one, and the read
compares that resolution again against the file it opens.

**Two non-claims are carried in the module's own docstring.** Every failure this seam models is a typed refusal
inside the result, but the one class that does **not** reach it is a caller passing an object which is not one of
the two typed models: that is a programming error at the call site rather than a modeled read failure, and the
signature is what the boundary claim rests on. And a caller whose input is rejected must be able to tell an
absence from a malformed input: the seam never reports a path absent for a spelling the read path refused.

The wiring boundary did **not** move: like its four siblings, this module has **no non-test importer in
`mcp/src`**, and the requirement's own boundary is explicit that the public tool name stays separate from the
concrete application function.

| Finding | Anchor | Source |
| --- | --- | --- |
| The seam's three original entry points (MIK-R02 later added `select_knowledge_scope` beside them). | `read_knowledge_scope`; `open_read_context`; `read_row_counts` | mcp/src/agents_remember/application/knowledge_read.py:144-166; mcp/src/agents_remember/application/knowledge_read.py:108-141; mcp/src/agents_remember/application/knowledge_read.py:634-650 |
| **The read-only handle, the request-level cursor check before the file is opened, and the ordered sequence.** | `_read_inside_snapshot`; `_select_and_page` | mcp/src/agents_remember/application/knowledge_read.py:195-225; mcp/src/agents_remember/application/knowledge_read.py:234-264; mcp/src/agents_remember/application/knowledge_read.py:267-298 |
| **The three snapshot comparisons, each naming the comparison that fired.** | `_snapshot_identity_refusal` | mcp/src/agents_remember/application/knowledge_read.py:321-360 |
| **The scope-dependent half of the binding, including a position past the end of the selection.** | `_continuation_refusal`; `_manifest_binding_mismatch` | mcp/src/agents_remember/application/knowledge_read.py:363-384; mcp/src/agents_remember/application/knowledge_read.py:543-563 |
| The two absence codes and the recorded-but-empty selection served rather than refused. | `_absence_refusal` | mcp/src/agents_remember/application/knowledge_read.py:404-436 |
| The storage layer this seam delegates to. | `select_recorded_scope`; `page_of_scope`; `anchor_resolver_for` | mcp/src/agents_remember/memory/knowledge/read.py:193-238; mcp/src/agents_remember/memory/knowledge/read.py:762-816; mcp/src/agents_remember/memory/knowledge/read_anchors.py:76-88 |
| The vocabulary this seam takes and returns. | `KnowledgeReadContext`; `KnowledgeReadRequest`; `KnowledgeReadResult`; `KnowledgeReadPage` | mcp/src/agents_remember/models/knowledge/read.py:200-247; mcp/src/agents_remember/models/knowledge/read.py:262-272; mcp/src/agents_remember/models/knowledge/read.py:278-288; mcp/src/agents_remember/models/knowledge/read.py:417-448; mcp/src/agents_remember/models/knowledge/read.py:451-477 |
| **The nodes that drive the task-free baseline read and the binding refusals through the public seam.** | "test_a_baseline_read_serves_a_task_free_context_and_reaches_the_whole_selected_scope"; "test_a_continuation_naming_a_position_past_the_selection_refuses_rather_than_escaping" | mcp/tests/test_knowledge_read_boundaries.py:502-502; mcp/tests/test_knowledge_read_boundaries.py:772-772 |

## 260915-KS-L8 The Comparison Joins As A Sixth Seam

The route gained one module, `application/knowledge_diff.py`, and still no new authority. It is the **sixth**
composition seam over the experimental knowledge substrate, beside the candidate write, the
candidate-lifecycle/publication seam, the guarded merge, the portable export/import and the selective read,
and its subject is a different composed operation again: **one comparison of two named knowledge snapshots
and two named code trees, for one selected invariant or family.**

**Four boundaries this seam owns, each because getting it wrong is a different kind of wrong:**

- **The selection is R07's, run twice.** Each side goes through the one policy on **that side's own**
  read-only connection; the whole of this module's contribution to the selection contract is that a side may
  name its own exact revision (`seed_override`), which is what lets a before revision and an after revision
  be addressed separately.
- **A candidate change invalidates a continuation, because the binding says so.** The cursor binds a digest
  over both declared snapshots, both resolved contexts, both code trees and both selectors, so a candidate
  whose bytes changed has another `after` identity and is refused with `continuation_binding_mismatch`
  rather than continued. **The invalidation is the binding, not a check someone has to remember to write.**
- **A missing side refuses, and no `HEAD` is substituted.** An absent or unreadable database, or a side
  naming a snapshot the file does not hold, is refused by name; nothing here reaches for a working tree, a
  branch or `HEAD`, and the expansion's command names the two **requested** trees.
- **Absence on one side is reported, not raised.** A side whose own selector named nothing recorded still
  leaves the other side's union served, with that side's absence carried in `side_absences` — which is what
  "the removed before-side realization remains in the diff" means at the seam. The operation refuses
  outright only when **neither** side selected anything, and that refusal names the side that earned it.

**The ordered sequence, and the two properties that make it safe.** Both files are opened read-only; **both
sides are verified before either is selected** (namespace, schema generation, logical digest — three
separate comparisons per side, with the schema check its own statement rather than a corollary of the
digest), so a union can never be built from one verified snapshot and one file that turned out not to be the
snapshot it declared. And the **request-level** cursor bindings — policy, selector digest, display filter —
are decided **before** the comparison binding, so a caller who changed the question is told that rather than
being sent to re-select a dataset they selected correctly. No cursor refusal returns a partial page.

**`open_diff_side` is the constructor, and `diff_row_counts` is the measurement half.** A side can only be
*resolved* from the identity the file actually holds, so a caller cannot hand-write the snapshot a side is
verified against; and the row counts are taken through the same read-only handle, so "a refused comparison
persisted nothing" is measured rather than asserted. The two database paths are separate arguments from the
sides on purpose: **a side is an identity and a path is where the bytes currently are.**

**The non-claim is the module's own docstring, in the form the requirement wrote it.** The comparison reports
facts and comparisons of facts; it does not rank, score, approve, certify neutrality or decide that a change
has no consequence, and **it has no field that could** — which the boundary module measures over the
serialized response. A filtered or partial response declares its limits and cannot claim the complete
semantic review it did not perform.

The wiring boundary did **not** move: like its five siblings, this module has **no non-test importer in
`mcp/src`**, and no MCP tool name is introduced here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The seam's four entry points. | `diff_knowledge_scope`; `open_diff_side`; `git_tree_difference_probe`; `diff_row_counts` | mcp/src/agents_remember/application/knowledge_diff.py:166-181; mcp/src/agents_remember/application/knowledge_diff.py:184-238; mcp/src/agents_remember/application/knowledge_diff.py:132-163; mcp/src/agents_remember/application/knowledge_diff.py:850-866 |
| **The ordered body: verify both sides before either selection, select each side with the one policy, compare, collect absences, refuse an empty union, display, page.** | `_select_and_compare`; `_select_side` | mcp/src/agents_remember/application/knowledge_diff.py:382-448; mcp/src/agents_remember/application/knowledge_diff.py:506-522 |
| **Both sides verified before either is selected, and the three comparisons inside each.** | `_any_side_snapshot_refusal`; `_side_snapshot_refusal` | mcp/src/agents_remember/application/knowledge_diff.py:487-503; mcp/src/agents_remember/application/knowledge_diff.py:768-801 |
| **The binding computed before either file is opened, and the per-side effective selector it digests.** | `_binding`; `_effective_selector` | mcp/src/agents_remember/application/knowledge_diff.py:295-312; mcp/src/agents_remember/application/knowledge_diff.py:315-318 |
| **The cursor check order: policy, selector, filter, then the snapshot pair.** | `_cursor_mismatch` | mcp/src/agents_remember/application/knowledge_diff.py:733-765 |
| **The page arithmetic: the comparison total on every page, the cumulative returned, and the display's own two numbers beside it.** | `_page` | mcp/src/agents_remember/application/knowledge_diff.py:525-569 |
| The per-side absence vocabulary and the recorded-but-empty selection served rather than refused. | `_side_absences`; `_side_absence_refusal`; `_selector_is_recorded` | mcp/src/agents_remember/application/knowledge_diff.py:580-607; mcp/src/agents_remember/application/knowledge_diff.py:610-622; mcp/src/agents_remember/application/knowledge_diff.py:625-651 |
| The four input classes a failed read is mapped onto. | `_reading_failure` | mcp/src/agents_remember/application/knowledge_diff.py:241-264 |
| **The nodes that drive the real candidate write, the missing side, and the substituted-snapshot refusal through the public seam.** | "test_a_candidate_that_changed_after_a_continuation_refuses_the_continuation"; "test_a_missing_side_refuses_and_substitutes_no_other_snapshot"; "test_a_side_naming_another_snapshot_of_its_own_file_refuses_before_any_page" | mcp/tests/test_knowledge_diff_boundaries.py:342-380; mcp/tests/test_knowledge_diff_boundaries.py:320-339; mcp/tests/test_knowledge_diff_boundaries.py:455-495 |

## 260915-KS-L10 The Generation Registry Reaches The Seam

This leaf changed no authority in this route and added no module, but two of the helpers the seam calls now
behave differently and a reader of `application/knowledge.py` must not assume the old behaviour.
`read_row_counts` (`knowledge_read.py`) and `diff_row_counts` (`knowledge_diff.py`) previously iterated the
**pinned generation-1 table list**; they now resolve the **selected generation from the dataset they open**
(`generation_of_database`) and iterate *that* generation's tables and columns, which is what makes a
generation-2 dataset's coverage and row counts describe the dataset rather than the build. The composition
seam's own contract is unchanged: it still confers no authority, still assigns the provenance envelope rather
than accepting one, still exposes no acceptance or promotion operation, and `application` remains the only
consumer of `memory.knowledge` from this layer.

**One consequence worth stating plainly for a caller**: a dataset created through this seam now declares
**generation 2** (`CURRENT_GENERATION`), so a freshly initialized namespace is a generation-2 dataset with six
more tables than the generation-1 files earlier leaves produced. Opening either kind works — the open path
selects the generation from the file's own `PRAGMA user_version` — but an operation that compares two datasets
refuses a **mixed-generation** pair before any session exists rather than silently skipping the tables one side
lacks.

| Finding | Anchor | Source |
| --- | --- | --- |
| The read-side row counts now resolve the dataset's own generation instead of the build's table list. | `read_row_counts` | mcp/src/agents_remember/application/knowledge_read.py:634-650 |
| The diff-side row counts do the same, so coverage describes the dataset it measured. | `diff_row_counts` | mcp/src/agents_remember/application/knowledge_diff.py:850-866 |
| The generation selector both now call, and the declaration a created store makes. | `generation_of_database`; `CURRENT_GENERATION` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:510-527; mcp/src/agents_remember/memory/knowledge/schema_generations.py:482-482 |
| **The generation selector both now call — which reads the dataset's own declared version and refuses an unregistered one rather than widening.** | `generation_of_database` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:510-527; mcp/src/agents_remember/memory/knowledge/schema_generations.py:413-413 |
|**The declaration a created store makes, which is the registry's last entry rather than a second literal — generation 5 since `KS-R18@v1` appended it.**|`CURRENT_GENERATION`| mcp/src/agents_remember/memory/knowledge/schema_generations.py:482-482 |
| **The generation selector this route's read and diff helpers call, which reads the dataset's own declared version and refuses an unregistered one rather than widening.** | `generation_of_database` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:510-527 |
| **The declaration a created store makes: the registry's last entry, which is generation 5 since `KS-R18@v1`.** | `CURRENT_GENERATION` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:482-482 |
| **The registry whose tip that entry is, ordered oldest first so the newest supported generation is its last member rather than a second literal that could drift from the tuple.** | `GENERATIONS` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:459-469 |
| **The generation gate the binding write applies before any row exists: a dataset that predates the table is refused with the observed generation as a fact, never migrated or widened.** | `require_binding_generation` | mcp/src/agents_remember/memory/knowledge/citations.py:293-313 |
| **The two members this leaf registered on the shared operation vocabulary.** | "author_citation_binding"; "read_citation_closure" | mcp/src/agents_remember/models/knowledge/result.py:120-120; mcp/src/agents_remember/models/knowledge/result.py:121-121 |
| The generation selector both now call, and the declaration a created store makes. | `generation_of_database`; `CURRENT_GENERATION` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:510-527; mcp/src/agents_remember/memory/knowledge/schema_generations.py:482-482 |

## 260915-KS-L11 The Facet Selection Joins As A Sixth Seam

The route gained one module, `application/knowledge_facets.py` — the layer's thirty-second Python module
and the sixth seam — and no new authority. It is the **sixth composition seam** beside `knowledge.py`, `knowledge_snapshot.py`, `knowledge_merge.py`,
`knowledge_export.py` and `knowledge_read.py`, and it is a seam rather than more entry points on the read
because the facet aggregate is a **different selection**: `read_facet_scope` declares its own policy name
(`authored-judgment-facets/v1`), takes one seed and returns one complete page, and it shares no code path
with `KS-R07@v1`'s recorded-scope read.

Three boundaries the module owns, and the reason each is the shape it is:

- **The read-only handle is how "a refused facet read persisted nothing" is structural.** The connection is
  opened through `open_read_only_database`, so the strongest statement available is a `SELECT`; the property
  is a fact about the handle rather than a rollback the code has to remember.
- **The declared snapshot is verified before anything is selected, in three separate comparisons** —
  namespace binding, schema generation, logical dataset — each returning `snapshot_unavailable` with
  expected and observed as facts. A context describing another dataset is refused by name rather than
  answered from whatever bytes the path happens to hold.
- **The selection is complete or it refuses.** A selection past `FACET_SELECTION_ITEM_LIMIT` becomes the
  shipped `selection_incomplete` carrying its count and bound; there is no cursor, so a caller never
  receives a page it could read as the whole aggregate when it is not.

**One distinction a later reader must not flatten:** a seed naming nothing recorded is `selector_absent`,
while a *recorded* facet record with no attachments and no supersession edges is a real page reporting zero
counts. The module reads that fact (`seed_recorded`) rather than inferring it from an empty item list, so
"nothing is there" and "the record is there and carries nothing yet" stay different answers.

**The wiring boundary did not move:** like its five siblings this module has no non-tool importer in
`mcp/src`, so its cases are behaviour evidence about the seam rather than evidence that it is reachable from
a registered tool. `read_facet_scope` is in the module's `__all__`, and no MCP tool name was introduced.

## 260915-KS-L15 The Assessment Read Joins The Quality Controller
The memory-quality controller gains one read and one input, and the route's shape is otherwise
unchanged. `curator_knowledge_review_summaries` reads the **already-published** curator-coherence
authority — the same authority the full scoped run already resolves — and summarises its stored
assessment collection into the rows the checklist's factual `knowledgeReview` section renders. It is
the controller's second read of that authority on a full run and not a second resolution, and it
decides nothing about what it reads.
The read is deliberately **not** an input to `curatorActionableCount`, and a subject with no stored
assessment produces no row at all rather than a favourable one. This route remains a typed operation
facade: the summaries travel into `CuratorChecklist.knowledge_review`, whose default keeps every
existing caller unchanged.

## 260915-KS-L17 The Composition Seam
The route gained one module, `application/knowledge_composition.py` — the layer's **fifth read-only
application seam** beside `knowledge_read.py`, `knowledge_snapshot.py`, `knowledge_merge.py` and
`knowledge_export.py` — and no new authority. It admits a dataset path and a repository namespace and
delegates to the two memory modules that own the acts: `follow_composition_scope` for the
declared-policy traversal and `family_revision_view` for the Family projection.
**The traversal is a read, not a write, and it is not the retrieval read.** This is the one sentence a
later reader must not flatten. Following declared composition edges under a declared policy version is
a *different operation* from `read_knowledge_scope`: this seam does not touch that function, its
selection policy or its advertised frontier, and the operation name it carries
(`follow_family_composition`) is its own member of the operation vocabulary rather than a variant of
the read's. A caller that wants the recorded-scope selection asks for that operation; a caller that
wants declared composition edges followed asks for this one.
Three boundaries the module owns, and the reason each is the shape it is:
- **The read-only handle is how "a refused traversal persisted nothing" is structural.** The
  connection comes from `open_read_only_database`, so the strongest statement available is a
  `SELECT`; the property is a fact about the handle rather than a rollback this code remembers, and
  the boundary case asserts the dataset's bytes are identical before and after a refusal.
- **The projection reports and never traverses.** `family_view` returns `reported` or `refused`, and a
  family revision this namespace does not hold is **refused rather than reported empty** — an empty
  report would be indistinguishable from a revision that genuinely records nothing.
- **Every modelled failure is a typed refusal inside the result, not an exception.** An unknown policy
  identity or version, a not-permitted edge, a step past the declared bound and a missing family
  revision all arrive as `KnowledgeRefusal` values; a traversal that cannot be reported as a
  *complete* scope returns the refusal rather than a truncated scope.
| Finding | Anchor | Source |
| --- | --- | --- |
| The traversal seam: it carries its own operation and opens through the read-only handle. | `follow_family_composition` | mcp/src/agents_remember/application/knowledge_composition.py:83-112 |
| **The projection seam: a family revision this namespace does not hold is refused, not reported empty.** | `family_view` | mcp/src/agents_remember/application/knowledge_composition.py:115-133 |
| The one open path, whose handle is the shipped read-only connection and whose schema is the one the file declares. | `open_read_only_store` | mcp/src/agents_remember/application/knowledge_composition.py:136-159 |
| The published seam surface: two operations and their two value types. | `__all__` | mcp/src/agents_remember/application/knowledge_composition.py:49-56 |
| **The case that stamps the seam: read-only, its own operation, and no movement of the retrieval selection.** | "test_the_application_seam_is_read_only_carries_the_operation_and_moves_no_selection" | mcp/tests/test_knowledge_family_composition_boundaries.py:615-615 |

## Update History
- 2026-09-20T02:25+02:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): **cleared the one enforced `table_row_cell_count_mismatch` finding this route overview carried, and cleared it by deleting the empty cell rather than widening the table.** The L7 seam's reference row *"The nodes that drive the task-free baseline read and the binding refusals through the public seam."* ended in a stray fourth cell (`|  |`) under a three-column header, which GFM truncates silently; the extra cell holds nothing, so removing it loses no content and leaves the row matching its own `| Finding | Anchor | Source |` header and delimiter. The row's claim, both quoted anchors and both ranges (`mcp/tests/test_knowledge_read_boundaries.py:502-502` and `:772-772`, each the declaration line the L7 pass repointed) are unchanged, and no other row of the table was touched. No verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits. No commits.
- 2026-09-18T18:04:10+00:00: 260915-KS-L23 residue clearance (seat A, follow-up): the L23 reference-table cell's `_attach_curator_checklist` citation moved from `mcp/src/agents_remember/application/memory_quality/controller.py:363-441` to `mcp/src/agents_remember/application/memory_quality/controller.py:465-638`. The earlier entry in this pass kept the call site inside `_execute_memory_quality`; the reopen item asks a different question -- whether some cited range contains the changed construct's **declaration** line -- and the checklist publication is the function declared at 465, which is also the occurrence this claim is about. The other three citations (`:249-255`, `:258-264`, `:267-273`) are unchanged, the wording is retained, and nothing was deleted. Verification stamp not advanced: the code is uncommitted and closeout owns the stamp.
- 2026-09-18T17:58:12+00:00: 260915-KS-L23 residue clearance (seat A, follow-up): the L23 reference-table cell that names the quality controller's three entry points still cited their pre-rewrite spans. `run_memory_quality_request` repointed from `mcp/src/agents_remember/application/memory_quality/controller.py:110-120` to `:249-255`, `start_memory_quality_request` from `:111-143` to `:258-264`, `poll_memory_quality_request` from `:146-208` to `:267-273` — each is that entry point's current definition (it delegates to its `_run`/`_start`/`_poll` implementation through `_stamped`), read back in the code worktree. The fourth citation, `_attach_curator_checklist` at `:363-441`, is unchanged: the range holds the call site in `_execute_memory_quality` that performs the publication this claim names. No anchor, row, claim or range was deleted and no wording changed. Verification stamp not advanced: the code is uncommitted and closeout owns the stamp.
- 2026-09-18T17:54:26+00:00: 260915-KS-L23 residue clearance (seat A): re-read and repointed the five rows in this document that cite a construct this leaf's own line moves left behind; every claim's wording, anchor set and range shape kept. `generation_of_database` in the L10 reference table repointed from `mcp/src/agents_remember/memory/knowledge/schema_generations.py:385-385`, `:413-447`, `:475-492` and `:507-507` to `mcp/src/agents_remember/memory/knowledge/schema_generations.py:510-527` (its definition) beside `CURRENT_GENERATION` at `:482-482`; the same anchor repointed from `:346-363`, `:34-46`, `:413-413`, `:475-492` and `:507-507` to `mcp/src/agents_remember/memory/knowledge/schema_generations.py:510-527`; and again in the L10 body table from `:282-282`, `:310-447`, `:475-492` and `:507-507` to `mcp/src/agents_remember/memory/knowledge/schema_generations.py:510-527` beside `CURRENT_GENERATION` at `:482-482`. In the L7 table, `"test_a_baseline_read_serves_a_task_free_context_and_reaches_the_whole_selected_scope"` repointed from `mcp/tests/test_knowledge_read_boundaries.py:465-497` to `:499-499` and `"test_a_continuation_naming_a_position_past_the_selection_refuses_rather_than_escaping"` from `:725-762` to `:759-759` — the two quoted test names are declared on exactly those lines, and the retired spans stopped one and three lines short of them respectively. The retired ranges named no construct these claims are about (module prose, registrations and the 385/413/447 bodies of other generation declarations). Verification stamp not advanced: the code is uncommitted and closeout owns the stamp.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `GENERATIONS` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:425-434. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `CURRENT_GENERATION` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:447-447. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `CURRENT_GENERATION` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:447-447. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 3 generated projection bullet(s) by hand while resolving the memory sync** — `CURRENT_GENERATION`, `generation_of_database`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.
- 2026-09-18T06:30:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read each of this card's reopened claims against the construct as the merged line now stands, confirmed the cited range is current, and retired 1 generated projection bullet(s) by hand** — `GENERATIONS`. A mechanically projected range is unverified evidence, which is exactly why the check kept these claims reopened until an agent had read the construct they point at; the claims' wording is retained because each states what the construct does, and the ranges are the declarations the claims are about. Verification metadata advances to the merged base commit `15fe8678`.
- 2026-09-18T05:45:00+00:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `a0665505`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the range recorded in the row above is the one that now holds its anchor. The anchors concerned: `author_citation_binding`; `read_citation_closure`. No claim wording changed, and the verification metadata advances to the landed base because the claims were re-read against the current source.
- 2026-09-18T05:00:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): **re-read this route's composition seam and added its section.** The route gained a **fifth read-only application seam** — `knowledge_composition.py` — beside `knowledge_read`, `knowledge_snapshot`, `knowledge_merge` and `knowledge_export`. The section states the three boundaries the seam owns: it opens through the shipped read-only handle so a refused traversal persists nothing and "changed nothing" is a property of the handle rather than a rollback; it carries `follow_family_composition` as its **own operation**, so a caller that wants declared composition edges followed asks for that operation and not for the retrieval selection; and every modelled failure is a typed refusal inside the result rather than an exception. It also records that a family revision this namespace does not hold is refused rather than reported empty. Verification metadata is **not** advanced over unreviewed content; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-18T04:05:00+00:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): added the **citation-binding operations** section and **corrected a stale number this route's body stated as a fact**. The new section records the two things a reader of this route needs: the seam's own contract is unchanged (no authority conferred, the provenance envelope assigned rather than accepted, no acceptance or promotion operation, `application` still the only consumer of `memory.knowledge` from this layer), while two operation members now travel through it — authoring a binding and reading a selected prose view's closure — so both go through the same admitted path as every other knowledge operation rather than a second entry point beside it. It also records the generation gate the binding write applies, a dataset that predates the table being refused with the observed generation as a fact. **The L10 section's body said a dataset created through this seam declares generation 2; that was true when L10 wrote it and is false now**, so it is corrected in place to say the declaration follows the registry's last entry — generation 5 since this leaf appended the citation-binding table — rather than being restated as a literal a later generation would falsify. One corrupted citation cell was also repaired by hand: the row naming `generation_of_database` and `CURRENT_GENERATION` had a range that attempted to cover both declarations at once, which is not one extent, so it is **split into two rows, one anchor each**, with the anchors cited at their own declarations. Re-reading it also let the generated projection bullet that had produced the old range be removed, because a mechanically projected range is unverified evidence and an agent has now read both declarations. Verification metadata advances to the leaf's base commit `e963a01c` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read the controller this route governs against the changed source and wrote the section above. `application/memory_quality/controller.py` gained `curator_knowledge_review_summaries`, which summarises the already-published curator-coherence authority's assessment collection for the checklist's factual section and decides nothing about it; the route stays a typed operation facade and the summaries are deliberately not an input to `curatorActionableCount`. The reference rows that cite the controller were re-derived from the current file while re-reading it, because the leaf's insertion moved every anchor below it: `MemoryQualityExecution` is now `:93-111`, `_resolve_execution` `:317-337` and `_attach_coherence_readiness` `:714-741`. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
## 260915-KS-L12 The Supporting-Record Read Joins As A Seventh Seam
`KS-R12@v1` adds the route's seventh application seam, `application/knowledge_evidence.py`, beside the
knowledge, snapshot, merge, export, read, facet and detection surfaces. It exposes exactly one operation,
`read_evidence_scope`: one explicit context, one seed, one complete page. Like every seam here it decides
no authority and holds no durable state — it admits a context, delegates selection to the memory layer,
and returns the typed result unchanged.
Two properties are worth a reader's attention, because each is the reason a whole family of failures is
not reachable. **The read is read-only by construction**: the connection is opened through the shipped
read-only opener, so the strongest statement available to the operation is a `SELECT`, and 'a refused
evidence read left the file byte-identical' is a property of the handle rather than a rollback the code
has to remember. **The declared snapshot is verified before anything is selected**: the file must be bound
to the requested namespace, must implement the generation the context declares, and must hold the declared
logical dataset — the same three comparisons the recorded-scope read and the facet read make, so a context
describing another dataset is refused by name rather than answered from whatever bytes the path holds. The
artifact resolution is a read-time fact and never a rewrite: a caller may declare a local artifact root so
a recorded repository-relative path resolves against real bytes, and the stored record is served exactly
as written whatever the resolution says.
The route's *write* half does not get a new seam name. `application/knowledge.py` gains the supporting-record
half — `admitted_evidence_request` and `write_knowledge_evidence` — because the write already had one seam
and this is one more act through it, not a second boundary. The dispatch is on the command the request
carries rather than on a caller-supplied name, so a caller cannot ask for one act and submit another.
**Nothing in either half touches the two shipped selections.** The evidence selection declares its own
policy name, has its own seeds and its own item stream, and appears in neither the recorded-scope nor the
facet response — which is why their serialized pages stay unchanged.

## 260915-KS-L16 The Family-Integrity Pipeline's One Operation, And The Retention It Proves

`KS-R16@v1`'s Normative Requirement asks for **one** operation over the three record leaves, and this route
owns it: `application/knowledge_family_integrity.py`'s `family_integrity_report` opens a dataset
**read-only** through the shipped `open_read_only_store`, constructs the registered review scope, reads the
recorded detection run back, groups its facts, composes the five separated statuses, measures each authored
record's currentness and routes the groups into the existing curator worklist. `FamilyIntegrityRequest` and
`FamilyIntegrityReport` are its two value types and `COMPOSE_REPORT_OPERATION` names it for dispatch. Like
every seam on this route it **decides nothing itself**: each of those acts belongs to the module that owns
it, and this file is only the seam that puts them in the packet's order.

**Two of the five status owners are not this leaf's to report, and that is enforced rather than
documented.** `CALLER_REPORTED_STATUS_OWNERS` names the structural validator and the verification runner:
each reports its own fact, so the request carries their two statuses verbatim and the pipeline **refuses a
request that omits one** instead of filling it with a plausible value — a pipeline that invented another
owner's status would be the collapse §4.1 forbids, wearing the other owner's name. The detector's status is
derived from the signals the run recorded, the curator's from the records that are stored, and the
authority's from the currentness comparison this leaf measures. The report carries the shipped
actionability formula's own three terms and the family-review row count beside them, identifies the
validator that decides closeout readiness, and has **no field that could refuse a merge, block a closeout or
add a fourth term**: nothing here is a gate.

**The retention half is a proof, not a claim.** `publish_review_evidence` publishes a finding and the
manifest needed to interpret it through `KS-R18@v1`'s durable route and **reads them back from the exact
destination**, because the design declined to certify cleanup retention and a destination nobody read back
is an assumption rather than evidence. `ReviewEvidenceRetention` carries that proof and
`worklist_row_disposable` is the guard on the other side of it: a worklist row is not disposable while it is
the only pointer to the evidence that interprets it. The destination is `<task_root>/notes/reports/` —
outside the enclosure root and outside the worktree group by construction — and the module neither widens
that set nor writes into an enclosure's own `reports/` directory, which cleanup removes.

## 260915-KS-L20 The View Seam, The Renderer, And The Projection That Writes No Canonical Byte

`KS-R20@v1` adds the route's eighth, ninth and tenth application seams, and all three follow the discipline
the existing seven set: they resolve their own context, decide no authority, hold no durable state, and
return a typed payload rather than a second shape.

**`application/knowledge_views.py` is the seam, and its two load-bearing acts are both refusals of
convenience.** The snapshot a view declares comes from the shipped `open_read_context`, which reads the
identity the dataset at that path actually holds -- so a view cannot be handed a snapshot a caller wrote
down, and the three comparisons the other seams make (bound namespace, declared generation, declared logical
digest) are made here for the same reason. And the continuation is checked **before any row is read**:
`require_continuation_snapshot` refuses a token presented against another snapshot with both identities
named, and the caller receives no page at all -- there is no re-resolution and no partial answer. `_RENDERERS`
and `_PAYLOADS` are two tables keyed by the same five names on purpose: one says which renderer produces a
view's rows and the other says which payload class validates them, so a view whose renderer and payload
disagree fails at construction rather than at a reader. `VIEW_RENDERER_VERSION` is the one renderer version a
view and a projection both record, and `RECORDED_GRAPH` and `TRAVERSAL_POLICY` name two of the four inputs
`ViewCompleteness` is scoped to, as values rather than as prose.

**`application/knowledge_view_render.py` is where the five views are actually decided, and four properties
are enforced together because a renderer satisfying three of them is a renderer that will lose the
fourth.** Ordering comes from one of the four admitted inputs and it is named: `order_candidates` is the only
ordering path, it dispatches through the registry, and it reports per position which input produced it and
whether that input is authored or mechanical -- there is no comparator that is not a registered rule and **no
fallback**, because an input the registry does not admit raises `UnadmittedOrderingInput`. A value that
cannot be classified is **withheld, not emitted**: `_classified` returns `None` when a candidate has neither
a recorded author nor a registered mechanical rule and the caller turns that into an
`UnresolvedLimitation`, which is how requirement 2.1's forbidden third class, null and default are all
unrepresentable rather than merely absent. The declared tiebreak is the **only** lexical order -- when every
declared key ties, positions are assigned by record identity ascending under `ordering.declared-tiebreak`
and that is reported `mechanical` -- and nothing here reads a symbol name's spelling, a path prefix, a
directory depth, a file extension or a repository location, nor another view's result. Two runs at one
snapshot are byte-identical, because every input is a recorded value or a registered constant and nothing is
read from the clock, the environment, the filesystem or a live count a page boundary could move. The
authored side arrives through `CR20-6`'s intake decision: an authored no-consequence claim must be a stored
record while the packet's Exclusions forbid a new canonical record kind, so it is carried inside an
already-registered kind -- the `decision` facet of `KS-R11@v1`, whose `decider` is the author, whose `reason`
is the rationale and whose `outcome` carries the determination -- and a facet whose declared priority is not
the canonical decimal spelling is **not** read as a priority; the row it would have ordered is reported as
an unresolved limitation instead.

**A realization row is now emitted only for a revision the same read selected, and the front door accepts
a path.** Both selection paths apply one frontier: an exact invariant-revision read no longer returns a
location belonging to another invariant or to another family's member, because the row that realizes an
unselected revision is a different subject's answer rather than a second view of this one; and the family
view returns its members and those members' locations beside the joint guarantee, not the guarantee alone.
The seed that makes the front door reachable without a discovered revision id is optional and its absence
is not an error: `_seed_revisions` returns "no restriction" when the request names no source path, the
revisions realized at that path when it does, and an empty set when the path is recorded as realized
nowhere — an answer that selects nothing rather than a fallback to everything — with the spelling validated
by the shipped `PathSeed` rule on the request model itself.

**`application/knowledge_projection.py` renders Markdown and JSON as sibling views from the same resolved
records, and it places authored text without producing any.** There is no model call, no summary, no score
and no reassessment in it: a displayed disposition is the recorded disposition, a displayed status is the
stored status, and an unassessed claim renders as unassessed rather than as favourably assessed, so
requirement 4.4's "renderers do not call an LLM to invent fresh explanation" is true of this module by
construction rather than by review. Every artifact it emits carries the three recorded values -- stable
identity, source snapshot and renderer/profile version -- and a payload whose snapshot cannot be read is
**not projected at all**: it is reported as an unresolved projection input, because requirement 4.3 forbids
an artifact without all three. `PROJECTION_NOT_AN_EXPORT` is written into the rendered file itself, so the
distinction between a projection and `KS-R06@v1`'s portable export is a fact on disk rather than a
convention. The Markdown renderer writes an invariant's essential conditions **before** the statement's
prose and writes an explicit omission line when the view could not carry them (requirement 4.8: a compact
projection may shorten prose it is licensed to shorten and may not drop the conditions under which the
invariant applies), and a detection signal and an authored description stay separately attributed as two
blocks with their own provenance lines and **no merged field** combining them (requirement 4.9). It writes
nothing itself: `project_knowledge` builds a plan and hands it to the injected writer.

## 260915-KS-L22 The Intent Reviewer's Adapter, And The Tier That Owns The Composition

`application/knowledge_review.py` is this route's new adapter, and it **selects nothing**. It resolves
the candidate a task context names, calls the shipped comparison and the shipped review-matrix view,
and assembles their results into the payload the review vocabulary declares. No scope is computed, no
frontier is widened, no reference is re-resolved and no row is re-diffed here: `diff_knowledge_scope`
(R08's comparison) and `read_knowledge_view` (L20's review matrix, asked for its five record kinds)
are consumed exactly as their owners publish them, and every identity, count and ordering the payload
carries is the shipped operation's own value rather than a second derivation of it.

Where it sits is a rank decision, not a preference. `layers.toml` ranks `serving` below
`application`, so the HTTP shim may not import the read, diff and view operations this adapter
composes; the composition therefore lives at this tier and the dashboard reaches it through a port on
`ServingCollaborators` that the composition root wires — the same shape the launch-capsule compiler
already uses on this route. One value is shared across the seam: the transport parses
`ReviewSurfaceRequest` from its query string and this composition consumes that same value, so there
is one spelling of "what was asked" instead of a wire shape and a domain shape to keep in agreement.

The candidate comes from canonical task context only. A repository, a master and a leaf id are the
inputs; the leaf's enclosure contract is located from the recorded task root — never from a
caller-supplied path — and the two datasets are derived from that contract's own recorded worktree
group, inside the leaf's disposable local root. A path-shaped selector, a leaf with no readable
contract, and a leaf whose worktree is not live each refuse by name, and an absent dataset **half**
refuses as `candidate_dataset_absent` rather than substituting another dataset: the current `HEAD`, a
guessed worktree path and a browser-supplied path are all unreachable from these inputs.

**The pair's two directory names are published, and its absent half is preflighted.**
`REVIEW_BASELINE_DIRECTORY` and `REVIEW_CANDIDATE_DIRECTORY` are exported rather than private, because
two owners now read them: this adapter resolves the pair it reviews from them, and the ingest CLI
derives the candidate directory it authors into from the same two names — one spelling, so "the
candidate the leaf authored" and "the candidate the review resolved" are the same directory rather than
two conventions that happen to agree today. `missing_dataset_half` runs before any comparison in both
of this route's operations and the refusal **names which half** is missing (`baseline` or `candidate`),
because "author a candidate" and "place the dataset this candidate forks from" are different next
actions a reader cannot choose between from the words "the datasets are absent"; before the preflight,
an absent baseline raised a storage error from inside side construction instead of producing the typed
refusal.

**The pair is opened under the namespace recorded beside each dataset.**
> **Corrected by `260921-ICR-L34` (see that section at the top of this document).** The paragraph below
> as first written said the namespace is read from the candidate's **receipt** alone, and that a
> dataset with no receipt keeps the requested repository. That was false for a **before** half placed
> by a run handed a published `--baseline`: such a half has no receipt (a published dataset is not an
> admitted candidate) and carries the before half's own `baseline-generation.json` instead, so the read
> fell back to the requested repository name while the bytes were bound to a namespace id and the
> storage owner refused the mismatch — which made **every leaf on the ordinary `knowledge-ingest
> --baseline` route** unfreezable with `candidate_dataset_absent`. The current rule reads the record
> beside the bytes and falls back to the requested repository only when **neither** record exists.

A request names a *repository*; a dataset the write plane placed is bound to a *namespace id* derived
from it, and a side opened under the requested repository spelling refuses against the dataset's own
binding — measured on this leaf's fixture as `bound to 40d350a6-…, not to the requested repository
namespace agents-remember`, which in the live product would have failed the review of every real
candidate. So `review_namespace` reads the namespace from the record standing beside the bytes — the
candidate's own sealed **receipt** (`candidate-receipt.json`) when there is one, otherwise the before
half's own generation record (`baseline-generation.json`, written by the ingest's placement owner) —
and both sides and the review matrix are opened under that. A dataset with **neither** record beside it
(a fixture, a caller-assembled pair) keeps the requested identity as it always did, and a record that
exists but cannot be read is refused rather than guessed past.

**The route's second half lists the subjects the comparison can be reached on.**
`list_knowledge_review_entries` resolves through the identical operation the review does — canonical
task context only, one contract, one derived root — and then offers a subject **exactly when the
shipped comparison reaches it**: the candidate's own recorded invariant and family identities are read
through the store's own `list_invariants`/`list_families`, each is compared for that identity through
`diff_knowledge_scope`, and only the identities the operation answers with a page are listed. A subject
the comparison refused is **dropped rather than listed with a zero**, because an entry that opens a
refusal is worse than no entry at all; a candidate that records no identity the pair can compare yields
an empty list, which the caller renders as no entry rather than as an invitation to name one. Nothing
is recorded to make that true and no ranking is applied here, so this is an enumeration and not a
selection policy in disguise.

The records the renderer is given come from their owners too. `review_records_for` reads the published
assessment collection from the curator authority's own publication through the shipped loader, not
through a second reader of the same bytes, and an absent or unreadable authority is an empty
collection rather than an error — a candidate with no published assessment is one whose subjects
display `unassessed`, which the surface must be able to show truthfully. No `current` measurement is
supplied, so the shipped projection reports an unmeasured assessment stale rather than promoting it.

> **Superseded in part by `260921-ICR-L1` (see that section at the end of this document).** The
> resolution this section describes as the adapter's own is now
> `application/review_candidate_resolution.py`'s and is imported/re-exported here, and the candidate side
> no longer supplies "no root or tree id": it binds both from the capture, against the contract's
> recorded base commit. The paragraphs above are retained as the L22 record of the reasoning at that
> time; where they and that section disagree, the section is what the code does.

| Finding | Anchor | Source |
| --- | --- | --- |
| The comparison operation: resolve, then compose, with a refused resolution returned before any comparison runs. | "def read_knowledge_review(" |mcp/src/agents_remember/application/knowledge_review.py:203-226|
| The shipped comparison it composes and adds nothing to, and the adapter call that invokes it — now one step of a composition that measures the inventory first and branches on the selector. | `diff_knowledge_scope`; `_compare` | mcp/src/agents_remember/application/knowledge_diff.py:184-238; mcp/src/agents_remember/application/knowledge_review.py:507-522 |
| L20's review-matrix view, asked for the five record kinds, and the extracted step that reads it. | `read_knowledge_view`; `_review_matrix` | mcp/src/agents_remember/application/knowledge_views.py:86-112; mcp/src/agents_remember/application/knowledge_review.py:785-827 |

| The candidate resolved from task context, never from a caller's path — now the sibling module's operation, which this adapter delegates to and re-exports. | "def resolve_review_candidate(" | mcp/src/agents_remember/application/review_candidate_resolution.py:139-211 |
| The published assessment collection as the renderer's input. | "def review_records_for(" | mcp/src/agents_remember/application/knowledge_review.py:806-831 |
| The rank that puts the composition at this tier rather than in `serving/`. | `application`; `application` | layers.toml:44-56 |
| The disposable candidate root the two datasets are read from — defined in the sibling module and re-exported here so the ingest CLI keeps one spelling. | `REVIEW_CANDIDATE_RELATIVE_ROOT` | mcp/src/agents_remember/application/review_candidate_resolution.py:104-109; mcp/src/agents_remember/application/knowledge_review.py:132-158 |
| **The two published half-names, defined in the sibling module and re-exported here because the ingest CLI authors into the same root this adapter reads.** | `REVIEW_BASELINE_DIRECTORY`; `REVIEW_CANDIDATE_DIRECTORY` | mcp/src/agents_remember/application/review_candidate_resolution.py:110-114; mcp/src/agents_remember/application/review_candidate_resolution.py:96-96; mcp/src/agents_remember/application/knowledge_review.py:136-151 |
| **The pair preflight: the absent half named as `baseline` or `candidate`, so the refusal says which dataset to author and which to place — reached only when a subject was named, because a task-context review compares no dataset — and, since leaf `260921-ICR-L5`, the sibling fact beside it, a side that is present but cannot be read.** | `missing_dataset_half`; `unreadable_half_refusal` | mcp/src/agents_remember/application/review_candidate_resolution.py:367-387; mcp/src/agents_remember/application/knowledge_before_half.py:347-379 |
| **The namespace read from the record beside the bytes — the candidate's sealed receipt when there is one, otherwise the before half's own `baseline-generation.json` — with a derived knowledge index's own namespace next (since MIK-R25), the requested repository used only when none of these answers, and an unreadable record refused rather than guessed past. Corrected in place by `260921-ICR-L34`: the receipt-only rule made every `knowledge-ingest --baseline` leaf unfreezable.** | `review_namespace`; `CANDIDATE_RECEIPT_NAME`; `read_baseline_generation` | mcp/src/agents_remember/application/review_candidate_resolution.py:391-457; mcp/src/agents_remember/models/knowledge/snapshot.py:53-53; mcp/src/agents_remember/application/knowledge_baseline_generation.py:285-316 |
| **The entry operation: the same resolution, one comparison per recorded identity, and a refused subject dropped instead of listed with a zero — with the unreadable-half refusal stated before that loop.** | `list_knowledge_review_entries`; `_reviewable_entries`; `_selected_item_count`; `unreadable_half_refusal` | mcp/src/agents_remember/application/knowledge_review.py:250-305; mcp/src/agents_remember/application/knowledge_before_half.py:347-379 |
| **The identities the entry list enumerates, read through the store's own two list operations rather than a query written here.** | `_recorded_identities`; `list_invariants`; `list_families` | mcp/src/agents_remember/application/knowledge_review.py:296-308; mcp/src/agents_remember/memory/knowledge/store.py:181-197; mcp/src/agents_remember/memory/knowledge/store.py:199-214 |


## 260915-KS-L32 The Front Door's Path Seed, And The One Frontier Both Selections Share

Two corrections land in the view renderer, and they are the same correction stated twice: a view answers
about the subject it selected and nothing else. The first is a membership gap. A family read used to return
the joint guarantee and the detection signals and nothing else, so a caller asking which obligations a
family admits — and where they are implemented — was shown neither, while the payload still declared its
scope complete. `_family_members` and `_member_locations` now append the `family_member` rows the request
selected and the realization rows those members name, classified mechanically under the module's third
registered rule `REGISTERED_ROLE_RULE = ("ordering.registered-role", 1)` because membership is *recorded*
(the edge carries both revision ids and its own provenance) rather than authored — so those rows carry a
rule rather than an author, exactly as a trigger-derived row names `DETECTION_RULE`. The second is the
frontier itself. The invariant view always filtered its invariant rows by the requested revision while every
realization row in the namespace was appended unconditionally, so an exact revision read returned the
requested statement **plus** realizations belonging to other invariants — including ones in a different
family. Both loops now select on the same frontier, and the family view's member locations are filtered to
the members that read selected for the same reason: a realization answers "where is this realized", so one
realizing a revision this view did not select attributes a location to the wrong statement. With no
revision and no seed the frontier is every revision, which is the broader view the operation already
offered, so the filter restricts only where the caller asked it to. The front door itself is
`ViewRequest.source_path`, a request field validated by constructing the shipped `PathSeed` rather than by
restating its rule, resolved by `_seed_revisions` to the revisions realized at that path: an ordinary code
hit can now ask what governs it through path → invariant → family without first discovering an invariant or
family revision id.

## 260915-KS-L43 The Ingest Allocates A New Truth's Identity, And A Citation's Stays Derived

`mcp/src/agents_remember/application/knowledge_curator_ingest.py` is this route's curator write plane, and this
leaf changed **what an identity is a function of** one layer further than L39 did.

**The label is not an identity input, and a new truth's identity is allocated rather than derived.** L39 moved
the derivation off the recorded base commit onto the repository's own namespace — correct, and still the rule
for a *citation* — but it left the entry's local hand-off label as the discriminator for the invariant and its
first revision. So two independent tasks that both numbered an entry `R-LOCAL` and stated different truths were
handed one invariant and one revision; production sync then refused `duplicate_identity` on that row and
offered only to discard one of two truths that had never been in conflict. Under the developer's 2026-09-20
ruling that reading is wrong: `R-LOCAL` is a **local hand-off label**, the knowledge API **allocates and
persists** the canonical identity, continuity across a task boundary is by **explicitly naming the stored
identity**, and a retry rides a **separate idempotency key**. `_creation` now hands each new creation operation
a fresh `uuid4` pair — no task, no enclosure, no branch, no baseline, no label — and records it in the
candidate's own `curator-allocation-journal.json` under a key scoped by the enclosure's task identity;
`_with_replays` asks the dataset whether a repeat already stored the revision, and a repeat is reported
`replayed` with the identities it already holds rather than re-issued. The ruling's other forbidden design is
named on the route as well: **scoping the stored identity to the authoring enclosure is not the repair** —
enclosure identity scopes the retry key and distinguishes creation operations, and nothing else about it
enters an identity.

**A citation's identity stays derived, and each part is now keyed on what it actually is.** The route identity
is unchanged (a scope governs a path, so N anchors in one file are N associations with one row). The **anchor**
is keyed on the **allocated revision id**, with the locator's qualified name as the disambiguator *inside* one
creation — so two constructs in one file are still two anchors, and two independent tasks citing one construct
now mint two instead of aliasing onto one. The **claim** is neither a scope nor a place but the authored edge
from one exact revision to one exact anchor, and it is keyed on exactly those two endpoints: keyed on the label
it minted ONE identity for two genuinely different realizations, which is the row production sync refused.
**Explicit reuse is expressible on both layers**: an entry revising an obligation names `invariant_id` (already
shipped), and a target citing a place the dataset already records now names `anchor_id`, which uses that stored
identity verbatim and authors no anchor row — `CuratorCitation.declares_anchor` carries it into the write
module, exactly as `declares_invariant` does for a successor.

**The recovery route moved with it.** Sibling to this plane, `worktrees/sync_transaction.py` now journals every
authored decision a side has already accepted and re-enters the merge with all of them, because a decision that
settles one conflict has to still hold when the merge goes on to the next; and a row an already-accepted
decision answered that comes back anyway earns a **bounded refusal** (`sync-resolution-cycling`) naming the
exact row and the two honest next steps, instead of re-offering a decision that has already been made and had
its effect. Measured: twelve applications to the cap and no settlement before, two applications and a settled
merge after.

The route boundary is unchanged: no symbol extractor of its own, no onboarding write, no third root, no export,
no lane parameter, and no new required producer input — a producer supplies exactly what it supplied before. *(Since leaf `260921-ICR-L45` a producer must also author a realization rationale per new target; see* Authored realization rationale per target, required at admission *above.)*

| Finding | Anchor | Source |
| --- | --- | --- |
| The allocation: a fresh `uuid4` pair per creation operation, and the journal the retry is found by. | `_Allocation`; `_Allocations`; `_creation`; `_record_allocations` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:664-700; mcp/src/agents_remember/application/knowledge_curator_ingest.py:703-718; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1980-2019; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1956-1977 |
| The idempotency key, the content guard, and the replay decided from the dataset. | `_retry_key`; `_content_digest`; `_require_minted_content`; `_with_replays`; `_replayed_outcome` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1841-1853; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1856-1908; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2022-2047; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2050-2057; mcp/src/agents_remember/application/knowledge_curator_ingest.py:3599-3612; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1584-1797 |
| The one derivation, now taking a discriminator that names what each citation identity is about. | `_identity` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:3519-3555 |
| The route, anchor and claim identities minted together, each keyed on what it is: the path, the allocated revision, and the revision-plus-anchor edge. | `_TargetIdentities`; `_target_identities`; `_Authoring` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:677-687; mcp/src/agents_remember/application/knowledge_curator_ingest.py:649-661; mcp/src/agents_remember/application/knowledge_curator_ingest.py:721-732; mcp/src/agents_remember/application/knowledge_curator_ingest.py:735-787; mcp/src/agents_remember/application/knowledge_curator_ingest.py:700-713 |
| The explicit-reuse input on a target, and the write module field that carries it. | `_named_anchor_id`; `CuratorCitation` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:2512-2534; mcp/src/agents_remember/application/knowledge_ingest.py:86-104 |
| The recovery's journaled decisions and its bounded cycling refusal. | `_reconcile_knowledge_resolution`; `_reconcile_progress_refusal`; `SyncSideRecord` | mcp/src/agents_remember/worktrees/sync_transaction.py:693-752; mcp/src/agents_remember/worktrees/sync_transaction.py:755-784; mcp/src/agents_remember/worktrees/sync_transaction_state.py:50-102 |
| The case that measures the ruled semantics at the public boundary: two sibling enclosures, one reused label, two statements, distinct stored identities, and continuity by naming the stored id. | `_cycle01_reused_label_identity` | mcp/tests/test_knowledge_curator_ingest_list.py:3009-3126 |


## 260915-KS-L39 The Ingest's Identities Move To The Repository, And The Front Door Reaches The Baseline

`mcp/src/agents_remember/application/knowledge_curator_ingest.py` is this route's curator write plane — the layer that turns one orchestrator hand-off list into one
admitted candidate batch — and this leaf changed what its identities are a function of.

**Identity stopped being a function of the code base commit.** `_identity` derived every id it minted over
`_enclosure(contract)`, which is the enclosure's recorded base commit. That made one repository's knowledge
a function of the baseline it happened to be read at — the same obligation under the same local label was a
different record at each baseline, while two different repositories that shared a base commit were handed
the **same** record identity. Every id is now a `uuid5` over the repository's own `repository_id`: the
namespace is read from the dataset the run selected (derived under `_INGEST_NAMESPACE` only as a cold-start
fallback), and `ingest_curator_list` resolves it **before** planning so that one value — carried on the
`_Source` the planner reads — reaches every mint in the run rather than one value per step.

**What this paragraph described was true of the citations and only of them, and L43 corrected the scope.** The
"identity does not move with the baseline" rule holds for the route, anchor and claim, which are still
derived this way. It did not hold for the invariant and its first revision: those were derived from the entry's
local hand-off label, so they were stable across baselines *and* identical across two independent tasks that
numbered an entry the same way — the collision L43 repaired by allocating them. See the L43 section above; the
sentence that read "the same obligation under the same local label was a different record at each baseline"
remains true as history of the base-commit rule and is **not** a claim that a reused label identifies one
record.

**Two constructs in one file are two stored records.** The stored `anchor_id` and `claim_id` were keyed on
the written path and the entry id alone, so one entry citing `resolve_budget` and `other` in a single
`pkg/module.py` reached the batch with the same `source_anchor` twice and was refused `duplicate_identity`.
They are now minted together with the route id by `_target_identities` into one `_TargetIdentities` value,
and the anchor and the claim carry a discriminator that names what each of them is about rather than one
shared key. L43 sharpened which discriminator that is — the anchor on the allocated revision with the
locator's qualified name inside it, the claim on its revision-plus-anchor edge — because carrying the
entry id left two independent tasks aliasing onto one claim. The **route** deliberately stays keyed on the
path: a route is a scope that governs a path, so N anchors in one file are N associations with one route row
rather than N rows.

**The front door reached the selection this route already accepted.** `IngestSelection.baseline` existed and
`_admitted_candidate` already forked a selected dataset; the CLI did not declare the argument, so no
production caller could select one. The adapter now declares `--baseline` and passes it through, which is
what makes task B begin from task A's published knowledge instead of from an empty candidate. A run that
selects none is unchanged: the first task of a repository still creates an empty candidate.

The route boundary is unchanged: the operation still adds no symbol extractor of its own (a symbol is
resolved through the shipped `bound_definitions`), no onboarding write, no third root, no export, and no
lane parameter; the two-leg route transaction and the publication step keep the shapes the L30 and L32
sections describe.

| Finding | Anchor | Source |
| --- | --- | --- |
| The one derivation, keyed on the repository's own id rather than the enclosure's base commit. | `_identity` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:3519-3555 |
| The route, anchor and claim identities minted together, discriminated by the locator's qualified name. | `_TargetIdentities`; `_target_identities` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:607-619; mcp/src/agents_remember/application/knowledge_curator_ingest.py:649-661; mcp/src/agents_remember/application/knowledge_curator_ingest.py:735-787 |
| The operation that resolves the repository identity before planning, and the selection value the front door hands it. | `ingest_curator_list`; `IngestSelection` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1096-1113; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1116-1243; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1019-1036 |
| The admission that forks a selected baseline instead of creating an empty candidate. | `_admitted_candidate` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1561-1616; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1594-1594 |
| **The adapter that declares the baseline argument and passes it into that selection — and, since 260915-KS-L45, derives its candidate directory from the contract and places the baseline into the review's own half.** | `add_arguments`; `run`; `_place_review_baseline` | mcp/src/agents_remember/cli/knowledge_ingest.py:184-282; mcp/src/agents_remember/cli/knowledge_ingest.py:680-716; mcp/src/agents_remember/cli/knowledge_ingest.py:524-562 |
| The route, anchor and claim identities minted together, each keyed on what it is — L43's split lives in the section above. | `_TargetIdentities`; `_target_identities` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:607-619; mcp/src/agents_remember/application/knowledge_curator_ingest.py:649-661; mcp/src/agents_remember/application/knowledge_curator_ingest.py:735-787 |
| The adapter that now declares the baseline argument and passes it into that selection. | `add_arguments`; `run` | mcp/src/agents_remember/cli/knowledge_ingest.py:184-282; mcp/src/agents_remember/cli/knowledge_ingest.py:680-716 |


## Update History
- 2026-09-20T05:17+02:00 — 260915-KS-L39 curator (uncommitted CYCLE-01 change set on `ar/260915-ks-l39-ar`, base `756c47b37fa16324a836a44336655413d10fffaa`): **this route's body gained the L39 section above**, which states the three route-level facts this leaf changed inside the curator write plane: the identity derivation moving off `_enclosure(contract)` onto the repository's own `repository_id` (resolved before planning so one value reaches every mint), the anchor and claim identities gaining the locator's qualified name while the route stays one scope per path, and the CLI's `--baseline` reaching the selection this route already accepted so a next task begins from a prior task's published knowledge. The route's boundaries are unchanged: no second symbol extractor, no onboarding write, no third root, no export, no lane parameter, and publication still performed by the run that committed the candidate. This is a body change, not a metadata-only refresh: the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` rows are left exactly as they were and no stamp is advanced, because the candidate is uncommitted and closeout owns the real code and memory commits; the entry names the candidate this reading was performed against.
- 2026-09-20T00:46:52+02:00 — 260915-KS-L32 curator (uncommitted change set on `ar/260915-ks-l32-ar`, code base `7dcec036`, memory base `66b2ae8a`): **added the L32 section and extended the L20 renderer paragraph** — the family read now returns its members and their implementation locations, and both selection paths apply one frontier so an exact revision read no longer returns another subject's realization row; the L20 paragraph gained the corresponding sentences plus the optional `ViewRequest.source_path` seed, which is the change to `models/knowledge/view.py` at this route's boundary. The body changed substantively; no verification stamp advanced, because every source named is modified in the delivered working tree and closeout owns the stamp. This document's `knowledge_read_boundaries` and `candidate.py` citation rows remain stale for reasons this leaf did not cause and could not repair without the blocked `citation_fix` pass; they are reported, not papered over.
- 2026-09-18T19:18+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **added the L23 section** — the application seam's three changes stated at route altitude: `measuring_build_stamp()` stamped onto the memory-quality response at all three entry points and onto the citation responses (item 26 / D-33), `worktree_tools.py`'s start gate restated to its actual condition with the `Requires` lines reported rather than enforced (item 8 / D-17), and the `read_steps` response shape its own model declares (item 20 / D-9). It also records which of the checklist's rows are **not** curation debt (`affected.closure` and `coherence.record` are blocked by construction; the drift summary is diagnostic and does not enter `curatorActionableCount`) and that the refresh-attestation gate is the one that does, which is why every changed-source sidecar carries a body edit or an exact no-impact entry. The body changed substantively; no verification stamp moves — every source named is modified in the delivered working tree and closeout owns the stamp.
- 2026-09-18T18:10+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **added the L22 section** — the thin adapter `application/knowledge_review.py`, its composition of R08's `diff_knowledge_scope` and L20's `read_knowledge_view` with no selection of its own, the `layers.toml` rank that keeps the composition at this tier, and the candidate resolution and published-assessment read from the owners' own paths. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns that stamp.
- 2026-09-18T15:30+02:00 — 260915-KS-L20 curator (uncommitted change set on `ar/260915-ks-l20`, base `9f88a6de`): **added the L20 section** -- the three seams this route gains for `KS-R20@v1`; the view seam's two refusals of convenience (the snapshot resolved from the dataset rather than declared, and the continuation checked before any row is read with no partial answer); the four properties the renderer enforces together (a named ordering input with no fallback, an unclassifiable value withheld rather than emitted with an empty class, the declared tiebreak as the only lexical order, and byte-identical runs at one snapshot); the `CR20-6` intake decision that carries the authored claim inside an already-registered `decision` facet; and the projection seam that places authored text without producing any, records all three values or refuses to project, and keeps conditions and attributions separate. The metadata block above now names this leaf's candidate as what was read; the body was changed substantively and this entry is the history record, not a metadata-only refresh.
- 2026-09-18T14:05+02:00 — 260915-KS-L16 curator (uncommitted change set on `ar/260915-ks-l16`, base `7b1db4e0`): **added the L16 section** — the route's one new module and its single end-to-end operation, the two status owners the request must carry verbatim and the refusal that keeps the pipeline from inventing them, the counts the report carries with no field that could make it a gate, and the retention proof that publishes to `<task_root>/notes/reports/` and reads the bytes back from the exact destination. The metadata block above now names this leaf's candidate as what was read; the body was changed substantively and this entry is the history record, not a metadata-only refresh.
- 2026-09-18T06:40+02:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **re-read this route overview against the current source and repaired the citation ranges the leaf's addition moved.** It added the **supporting-record seam** section — the route's seventh application seam and its one read operation — and refreshed the write half's account of where the two supporting-record entry points live. The body above is the substantive update; the route's own source scope moved because the leaf both adds modules to it and appends two entries to the registry it documents.
- 2026-09-18T06:40+02:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 2 generated projection bullet(s) by hand** — `generation_of_database`, `CURRENT_GENERATION`, `worktree_status_packet`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.
- 2026-09-18T00:25+02:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): recorded the route's **sixth composition seam**, `application/knowledge_facets.py` — one context, one seed, one complete page, under its own declared policy `authored-judgment-facets/v1`. The body states the three boundaries the module owns (the **read-only handle** that makes "a refused read persisted nothing" structural; the **three snapshot comparisons** run before any selection, each naming expected and observed; and the **complete-or-refused** selection with no cursor), the distinction a reader must not flatten (**a seed naming nothing is `selector_absent`, while a recorded record with no attachments is a real page with zero counts**, read from `seed_recorded` rather than inferred from an empty list), and gives the seam its correct position in the running count, since the module's own docstring numbers it the fifth while naming five predecessors. The wiring boundary is re-recorded because it did **not** move: no non-tool importer in `mcp/src`, no MCP tool name, and no shared code path with `KS-R07@v1`'s selection — which is why a shipped seed's serialized page stays byte-identical. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): **route meaning changed for two helpers, with no new authority.** `read_row_counts` and `diff_row_counts` no longer iterate the pinned generation-1 table list: they resolve the **selected generation from the dataset they open** and iterate that generation's tables, so a generation-2 dataset's coverage and row counts describe the dataset rather than the build. The body records that the seam's own contract is unchanged (no authority conferred, provenance assigned rather than accepted, no acceptance or promotion operation, still the only consumer of `memory.knowledge` from this layer), that a namespace initialized through this seam now declares **generation 2** so it carries six more tables than the generation-1 files earlier leaves produced, and that opening either kind works because the open path selects the generation from the file's own `PRAGMA user_version` while a **mixed-generation** comparison refuses before any session exists. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-17T03:31:11+02:00 — **Historical stamp carried from the incoming official line** (merge HEAD `12bd7fd3`; the live stamp for this file is the later synced value in the metadata table above, which closeout re-stamps): `lastUpdated` 2026-09-15T00:56:17+00:00; `lastVerifiedCommitHash` `806649b91bdce18f7b915bfbbf6727967f4e7a88`; `lastVerifiedCommitDate` 2026-09-16T12:23:53+02:00; the candidate reading taken against `ar/260913-lca-l9` uncommitted source; base `bb65a2073228c5e143b055a470f39c6c9e2f4d9d`.
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): stamped the untimestamped Update History entries with this document's own commit clock
- 2026-09-17T03:15+02:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): recorded the route's **sixth composition seam**, `application/knowledge_diff.py` — one comparison of two named knowledge snapshots and two named code trees — and the four boundaries it owns: **R07's selection run twice** with the per-side exact-revision address as the only addition to the selection contract; **the binding as the invalidation** (a candidate whose bytes moved presents another `after` identity and is refused rather than continued, so the invalidation is not a check someone has to remember to write); **a missing side refuses with no `HEAD` substituted**; and **one side's absence reported rather than raised**, with the operation refusing outright only when neither side selected anything. It records the two properties that make the ordered body safe (**both sides verified before either is selected**; the request-level cursor checks decided **before** the comparison binding, so a caller who changed the question is told that), the three separate snapshot comparisons per side, the page arithmetic that keeps the comparison total and the display's two numbers apart, the four typed failure classes the read maps, `open_diff_side` as the constructor that stops a caller hand-writing a side's identity, and `diff_row_counts` as the measurement half of the persisted-nothing property. It carries the module's own non-claim in the requirement's words — the comparison has **no field that could** rank, score, approve or decide neutrality, which the boundary module measures over the serialized response — and records that the wiring boundary did **not** move: like its five siblings the seam has **no non-test importer in `mcp/src`** and introduces no MCP tool name. Every storage-layer citation in the L7 section above was re-derived, because the L8 docstring insertion moved `read.py`'s anchors. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): recorded the route's **fifth composition seam**, `application/knowledge_read.py`, and the three boundaries it owns: the **read-only handle** that makes "a refused read persisted nothing" structural (with `read_row_counts` as the measurement half), the **task-free baseline read** that never fabricates a leaf, and the **cursor as a binding** whose request-level checks run before the file is opened while its manifest and position checks run where the selection exists — with no cursor refusal ever returning a partial page. The card records the ordered sequence and the three separate snapshot comparisons (namespace, schema generation, logical dataset) where the schema check is its own statement rather than a corollary of the digest, the two absence codes with the recorded-but-empty selection served rather than refused, and `open_read_context` as the constructor that stops a caller hand-writing the snapshot a read is verified against. It carries the seam's two non-claims in the module's own terms (every modelled failure is a typed refusal, while a caller passing a non-model object is a programming error at the call site; and a caller must be able to tell an absence from a malformed input) and records that the wiring boundary did **not** move — like its four siblings the seam has no non-test importer in `mcp/src`. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l07`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T17:45+02:00 — 260915-KS-L6 curator (uncommitted change set on `ar/260915-ks-l06`, base `7db50f8f`): recorded the fourth composition seam — `application/knowledge_export.py` — and why the portable export/import boundary is its own module rather than more entry points on any sibling: the four seams now divide the knowledge surface into the write, the lifecycle-and-publication, the merge, and the portable artifact, so each entry point stays readable as one intent. The card records the five entry points (two pure delegations, the read-only validation that produces **no database at all**, the value-or-refusal file reader whose two failures carry different codes, and the body that is handed out only for an artifact the validator accepted), the two non-claims the ruled intent made explicit (an export is not a filtered read response or a Markdown projection; an import creates no Git commit and restores no Git ancestry), and the wiring boundary that did **not** move: like its three siblings, this module has no non-test importer in `mcp/src`. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l06`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): recorded the third composition seam — `application/knowledge_merge.py` — and why the guarded common-base merge is its own module rather than more entry points on either sibling: the three seams now divide the knowledge surface into the write, the lifecycle-and-publication, and the merge, so each entry point stays readable as one intent. The card records the resolve-then-merge pair returning the storage layer's typed values unchanged, the carried absence of any compatibility verdict, and the non-claim the ruled design made explicit: **the adapter is callable rather than wired** — no Git merge driver, attribute or commit exists on this path, and activation is an explicit later change. The wiring boundary is re-recorded because it did not move: like its two siblings, this module has no non-test importer in `mcp/src`. Verification metadata remains closeout-owned.
- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): recorded the second composition seam — `application/knowledge_snapshot.py` — and why the lifecycle/publication half is its own module rather than more entry points on `application/knowledge.py`: each entry point stays readable as one intent. The card records the derived write destination (so write and publish cannot name different files), the two publication entry points sharing one install contract, and the read-side gate being exposed rather than decided. **Two non-claims are stated rather than left to inference**: the seam creates no Git commit (capturing a published file into a memory tree is the existing candidate-tree owner's operation) and no IAS landing is reachable from it. The wiring boundary is re-recorded because it did not move: like `application/knowledge.py`, this module has no non-test importer in `mcp/src`. Verification metadata remains closeout-owned.
- 2026-09-16T10:30+02:00 — 260915-CAPS-L3 curator: route body updated for the task-context projection package (`CAPS-R03@v1`), which **implements the seam the L2 section above only declared** — L2 accepted any `CapsuleTaskProjectionSource` and passed it through; this package is the thing that fills it. Added the `260915-CAPS-L3 Task-Context Projection Boundary` section: the complete-or-refused rule and why the refusal family sits outside the capsule family, the L4/L5/L7 consumer contract, the two admissions with the **typed `approved-requirement-packet` route as the standardized policy** (owner ruling 2026-09-16T10:15), the total read plan with its never-read-a-sprint-ancestor rule, the no-clipping and referenced-is-not-omitted rules, and read-only as an asserted property. **Records the naming disambiguation explicitly**: this route now owns a *task-context* projection, which is not the *closeout-queue* projection owned by `tasks/document_refs.py::projection_sprints_affected_by_master` and the closeout writers — same word, unrelated owners, inputs, outputs and consumers. Also added the disambiguation sentence to the L2 section's L3-seam paragraph so a reader arriving there is not left to guess. Verification metadata remains closeout-owned; no acceptance claim is made.
- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base
  `60e0820e`): recorded the graph operations joining the seam — eight builders that attach the destination's
  provenance and namespace exactly as the revision builder does, eight open-delegate-close operations, and the one
  builder that takes the anchor endpoint because naming an anchor and recording one are different inputs — and
  recorded the boundary that did not move: the seam still has **no non-test importer in `mcp/src`**, so its
  composed-path test is behaviour evidence and not wiring evidence, and the consuming write boundary is `KS-R03`'s.
  Verification metadata remains closeout-owned.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base
  `67b21aeb`): recorded the new `application/knowledge.py` composition seam — assigned rather than parameterized
  provenance, the typed admitted-destination handle that confers no authority, the occupied-destination refusal, the
  absent acceptance/promotion operation, and the one-way import direction the `layers.toml` charter paragraph
  fixes. Verification metadata remains closeout-owned.
- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Corrected application argument/result routing, record landing and checkpoint authority. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: added the stop-only application boundary to the body. The
  route gained `worktree_pause_tool`, which admits the configured contract, builds the same typed
  `WorktreeArgs` its siblings build and delegates to `git_worktree_manager.pause_result` — performing no
  Git, no ref move, no commit, no landing, no ledger write and no auto-land hook, because nothing is
  retired and nothing is finished. Recorded that this is the one mutating entry point here whose
  delegate cannot reach a publication module, so the application layer makes no publish-or-not decision
  on that path, and that it is the counterpart of `worktree_checkpoint_landing_tool` on the opposite
  side of the pause/publication split. Verification metadata remains closeout-owned; no acceptance
  claim.
- 2026-09-13T14:24:00+02:00 — 260831-LOCR-L36 activation re-keying: corrected the IAS application
  boundary from one source-pair activation authority to the per-contract activation record — each
  canonical series contract owns its record, sibling masters sharing a protected source pair never
  wait on one another, and the only waiting reason is `atomic-series-reconciling` — with no shipped
  document quoted by this route claim. Source documentation only; verification metadata remains
  closeout-owned and no acceptance or test claim is made.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T09:15+00:00 — 260831-LOCR-L34: recorded the corrected `worktree_checkpoint_landing_tool`
  docstring on this route — the published text had omitted the completed-closeout requirement, which
  was the reason the route was unreachable — and pointed to the preview/apply parity invariant
  inventory on the worktrees route overview and in `memory_quality/overview.md`. Content change, not a
  range repoint; verification metadata remains closeout-owned and no acceptance claim is made.
- 2026-09-12T02:55+02:00 — 260831-LOCR-L30 checkpoint landing: recorded the new
  `worktree_checkpoint_landing_tool` entry point on this route, its admission/argument/delegation
  shape, why it runs no completion-edge work, and why it is a separate public tool rather than a flag
  on `worktree_integrate`. Content change, not a range repoint; verification metadata remains
  closeout-owned.
- 2026-09-11T23:05:00+00:00: Pull-request landing curation: recorded the new `worktree_record_landing_tool` entry point and its `LandedCommits` parameter object, and why it shares the single landed-integration writer with `worktree_integrate` instead of writing the integration cell itself. Content change, not a range repoint.
- 2026-09-11T10:26:37+02:00 — De-entanglement cut cleanup at code commit `2fa5e81f`: rewrote the "Durable Lifecycle Application Boundary" section from the deleted detached worker to the in-process synchronous route, removed the deleted legacy-repair and closeout-door adapters from the hot-path summary, and recorded the deletions of `application/closeout_door.py` and the `application/lifecycle/` worker, legacy-tool, enclosure-tool and status-wait entry points. Only cut-affected claims were reconciled; this route's other claims were not re-read in this pass, so verification metadata remains pinned. Source documentation only; no acceptance or certification claim.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.
- 2026-09-10T02:27:58+02:00 — CCR-L42 parity curation: No route impact: curator preparation and closeout now run the shared sidecar and route body/history validators independently; this route's ownership and source semantics remain unchanged. No acceptance claim is made.
- 2026-09-08T16:05:21+02:00 — CCR-L38 source-grounded candidate pass: recorded the unified route-review refusal boundary across application start/admission, certification, and direct closeout. Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.
- 2026-09-05T07:22+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Corrected task/memory package paths and semantic invalidation; recorded exact tree revalidation, profile service composition, and remaining R05/R16/R07/R08 gaps. Verification records source review, not execution or acceptance.
- 2026-09-05T06:12+00:00 — Composed retained CCR route contributions without replacing sibling knowledge; preserved prior source-verification metadata and historical entries.
- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 route impact: recorded the `bound_next_step` task-address guard in `tool_response.py`.
- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: re-anchored the controller row of the application overview (run/start/poll/attach to 98-108/111-143/146-208/363-441) shifted by the CCR-R08 +57-line controller insertion. Citation-only re-anchor; no content impact.
- 2026-08-29T21:46+02:00 — MCAR-L03: documented exact-pair admission, async revalidation, and
  closeout application reporting. Verification remains closeout-owned.
- 2026-08-29T08:52+02:00 — MCAR-L02 A005: added the configured curator-coherence application
  boundary and shared memory/closeout readiness join. Verification remains closeout-owned.
- 2026-08-26T12:30+02:00 — 260821-ARSPAWN-L2 route impact: structural dispatch now composes one
  canonical-seat transaction with bounded evidence-based retry, and structural messages remain
  addressable through vacancies. Verification remains closeout-owned.
- 2026-08-26T12:30+02:00 — 260821-ARSPAWN-L2 final curation: narrowed failed-dispatch cleanup to
  positively proven pre-brief generations and recorded unknown-state reconciliation refusal. No
  test execution is claimed.
- 2026-08-26T08:55+02:00 — Finalized the IAS source-pair application boundary label against the
  frozen pass-13 candidate.
- 2026-08-25T17:21+02:00 — Reconciled the final admission, failure-projection, and deferred-import
  boundaries. Verification remains closeout-owned.
- 2026-08-25T08:27+02:00 — 260824-PDLS wave 004: reconciled the final `memory_quality/` package split, moved the preserved sidecars, and verified the route against emergency-landed code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is not Dagger certification.
- 2026-08-24T21:43+02:00 — File-size route refresh: extracted the worktree request/default concept
  owner from the operation facade. One model definition remains; operation behavior and public tool
  packing are unchanged. Verified at source commit `23d35f77`.
- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: added the canonical quality scope/controller route and authoritative direct-landing outcome projection. Verification metadata remains pinned until architect-owned closeout.
- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: recorded the `application/lifecycle/` package layout, repointed current source evidence, and verified the governed L2 route at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.
- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: route claims reconciled to accepted candidate tree `4241908c`; verification metadata remains closeout-owned.
- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1 route impact: `application/structural/agent_tools.py` resolves the dispatch caller by kind (plane vs ambient launcher from the process environment) and records caller-kind provenance through the `application/terminal_tools.py` spawn primitive (`spawnedByKind` wire field + catalog row); the plane structural path is unchanged. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.
- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair route impact: the task-doc authoring modules moved to the new `application/task_docs` sub-route. Verified at code commit e5cb139f.
- 2026-08-20T21:30+02:00 — 260815-DAG-L15 route impact: new memory_quality_runs registry, async start/poll quality wrappers, preflight + typed-refusal authoring dialect, create=False dry-run locks. Verified at code commit de3a0fd9.
- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   L12 title threading across the task-doc, topology-authoring, and sprint-linkage writers (publish + preview). Verified at code commit b7f2c8e2.
- 2026-08-20T09:35+02:00 — 260815-DAG-L16 route impact: closeout-queue application boundary gains
  the declared-caller fallback; route-review binding extracted to
  `application/task_doc_route_review.py`; `application/direct_landing.py` added. Verified at code
  commit a9d50e08.
- 2026-08-20T05:04+02:00 — 260815-DAG-L14 route impact: new `application/task_sprint_linkage.py`
  owns the atomic sprint↔master linkage operations; `task_doc_tools` routes them and carries
  `linkageFacts`; `task_execution_topology` shares the judgment verifier. Verified at code commit
  8071a644.
- 2026-08-19T22:32+02:00 — 260815-DAG-L13 route impact: `task_doc` dropped the removed
  `migrate_execution_topology` operation (`author_execution_graph` now bootstraps graph-less
  sprints), sprint creation scaffolds the empty canonical planning registers with write-time shape
  validation, and structural manager dispatch surfaces an atomic-sequential lane-blocked series
  bootstrap as a `StructuralOutcome` payload; the application-route model is unchanged.
  Verification remains closeout-owned.
- 2026-08-19T08:55+02:00 — 260815-DAG-L11 route impact: `task_reopen_tool` moved from
  `task_doc_tools.py` into the new `application/task_reopen.py` module (facade re-export keeps the
  surface stable), and `task_doc` gained the `author_execution_graph` operation dispatched to
  `task_execution_topology.py`; the application-route model is unchanged. Verification remains
  closeout-owned.
- 2026-08-18T12:00:00+00:00 — No route impact: L9 adds `inventory_execution_topology` (read-only pre-migration enumeration) to `task_execution_topology.py`; the application-route model is unchanged.
- 2026-08-18T09:10+02:00 — No route impact: renamed the atomic 'barrier' concept to 'blocker' throughout; route purpose unchanged.
- 2026-08-17T12:30+02:00 — No route impact: 260815-DAG-L5 extended the lifecycle-operation worker with repair evidence; the application-layer purpose is unchanged.
- 2026-08-15T23:38+02:00 — 260815-DAG-L4: reconciled this governing route with the frozen integration-authority implementation and forcing surface. Verification remains closeout-owned.
- 2026-08-15T11:25+02:00 — L3 static-gate route impact: extracted task-doc queue-scope
  classification into a focused application owner while retaining the dispatcher as the sole
  locked publication entry point.
- 2026-08-15T11:07+02:00 — L3 Dagger repair: task publication now derives queue governance from
  commanded graph scope while leaving genuinely standalone/light documents ungoverned; lifecycle
  diagnostics retain typed queue refusal status.
- 2026-08-15T09:10+02:00 — 260815-DAG-L3 route impact: recorded ambient queue authorization and
  lifecycle-operation correlation as application-owned translations. Verification remains
  closeout-owned.
- 2026-08-15T03:10:06+02:00 — 260815-DAG-L1 targeted-Dagger repair: the application owner keeps
  explicit migration fail-closed and now has forcing proof for invalid migration envelopes,
  unresolved or wrong-kind targets, and out-of-repository authoring. An unreachable duplicate
  validation translation was removed rather than exempted from coverage.
- 2026-08-15T02:42:41+02:00 — 260815-DAG-L1 review repair: the application policy now treats
  master aliases as cross-document authority, revalidating every affected sprint on supported
  identity edits or master-kind replacement and returning structured migration classifications
  through the same owner.
- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1 route impact: `task_execution_topology.py` is the new
  application owner for exact cross-document topology validation and finite atomic migration;
  `task_doc_tools.py` delegates rather than duplicating that policy.
- 2026-08-14T06:25+02:00 — L23 final candidate review: task/worktree entry points now enforce
  candidate-bound route review and transitive source lineage at admission and exit while the
  detached lifecycle worker remains the sole long-operation application composition root.
  Verification provenance remains closeout-owned.
- 2026-08-13T08:47+02:00 — L23 integration-gate repair: routed startup/runtime-install/skill-install through the new cohesive `application/runtime/` child overview and preserved direct domain imports instead of a facade. Verification metadata remains closeout-owned.
- 2026-08-13T00:00+02:00 — 260731-EFA-L23 post-closeout worker-authority repair: documented the detached lifecycle-operation declaration before service/config loading and its deliberate non-daemon boundary. The owner reports 46 focused tests, Ruff clean, and diff-check clean. Verification remains closeout-owned.
- 2026-08-12T20:20+02:00 — L23 curator: documented application ownership of lineage refusal/status translation; verification remains closeout-owned.
- 2026-08-12T16:52+02:00 — 260731-EFA-L23 packaged-worker route review: the detached CLI now owns
  default worktree-service composition before task-addressed dispatch, closing the installed-worker
  unbound-service failure while preserving the application/worktree port split. Verification
  provenance remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: added the detached durable lifecycle application owner and exact recovery boundary; verification provenance remains closeout-owned.
- 2026-08-11T14:40+02:00 — Recorded the current pre-closeout memory-quality boundary: a leaf-scoped
  call compares unstamped cards from the contract's code base against the dirty worktree, while
  official-memory calls do not invent provenance and closeout still owns real-commit stamps.
- 2026-08-10T19:57:55+02:00 — 260731-EFA-L21 route impact: recorded declaration-before-config-load
  at the MCP application startup boundary and its separation from undeclared linked-worktree CLI
  execution. Verification metadata remains pinned until closeout stamps the L21 code commit.
- 2026-08-08T14:38+02:00 — 260731-EFA-L9 route impact: recorded the provider-runtime and
  worktree-services composition additions. Verification metadata pinned until closeout stamps the
  L9 code commit.
- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer semantic correction: corrected the task-reopen anchor, expanded the
  hot-path inventory, marked parameter examples as selected, and reversed the FileReadStatus ownership
  claim to match the model/application source split.
- 2026-08-02T20:33+02:00 — 260731-EFA-L6 curator W1-B03 final-index reconciliation: post-S31 final-index movement repaired the one stale `route_index_refresh_tool` citation range (`application/memory_tools.py:266-266` → `:288-288`) using warm snapshot `a4f8c991b75ef019cd8b5f10c1daa9d41694df6116b569453bd0815b4efa2817`; scoped fix/recheck recorded zero source reads, tokenization, parsing, and build. Verification metadata remains pinned until closeout.
- 2026-08-02T17:00+02:00 — 260731-EFA-L6 curator W1-B03: repaired 6 citation rows and 1 prose citation with exact anchors and source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: route moved. `mcp/src/agents_remember/controllers/` was renamed to `application/` and `worktrees/status.py` moved in as `application/worktree_status.py`, so this route overview and all 14 child sidecars moved with the source. Adopted the leaf's vocabulary throughout: the package is "the application layer" and one function is "an application entry point". Route model, tool surface and behavior are unchanged — the old name was MVC vocabulary that described nothing about the contents. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:26+02:00 — 260731-EFA-L4 curator: **body corrected.** Added the route-impact
  section above for the two changed controllers, plus two invariants the route now follows but did
  not state: pass through a collaborator's already-checked value instead of re-validating its dump
  (because a `ValidationError` inside a controller lands on the uncaught tool path), and declare a
  controller-decided vocabulary in the controller and let the wire model import it. Recorded
  `context_packet.py`'s `worktree=worktree_status_packet(...)` passthrough — verified
  `worktrees/status.py:worktree_status_packet` is signed `-> WorktreeSummary` — and `_drift_packet`'s
  `-> DriftSummaryPacket` annotation. Recorded `read_files.py` as the new home of `FileReadStatus`
  and `VALID_FILE_READ_STATUSES`, with `_resolve_onboarding` typed to it, and flagged the
  models→controllers import direction explicitly with the no-cycle check I actually ran (imported
  `agents_remember.models.read_files` standalone; `controllers/read_files.py` has no
  `models.read_files` import). The 165-of-213 figure is quoted from
  `test_wire_vocabulary_exhaustiveness.py`'s module docstring, which is where it is measured; the
  vocabulary repair itself is a `models/` route fact and is documented there. Added three reference
  rows to the 2-column table. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: added the **Parameter Objects** section — the new
  `task_ref.py` module and the concept types each controller now defines — and corrected the Route
  Model's transport line: the `@server.tool()` declarations left `server.py` for the new
  `mcp/registration/` package. Verification metadata pinned until closeout stamps the L2 code
  commit.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: `memory_tools.py` now forwards the resolved code
  repository identity and storage/path-rule authority into deterministic route-index generation.
- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 route impact: controller overview now documents
  `_auto_land_completed_seats`, `serving.landing.land_seats_for_leaf`, the `auto_land_on_*` gates,
  and `autoLandedSeats`; successful completion lands chats for archive inspection instead of
  retiring them. Verification metadata pinned until closeout stamps the HFX2-L11 commit.
- 2026-07-08T02:43+02:00 — 260707-HFX-L8 route impact (seat lifecycle: retirement + live identity +
  turn-state, issue #12): `worktree_tools.py`'s integrate/finalize controllers gained a completion-edge
  auto-retire composition (`_auto_retire_completed_seats`, config-gated default ON, best-effort —
  the ENTIRE retire body is exception-guarded, widened in the R2/F1 fix round so a catalog I/O fault
  can never fail an already-succeeded edge) returning `autoRetiredSeats` on both tool results. The
  controller still stays a typed operation facade — retire mechanics live in `serving/retire.py`, this
  is composition only. Verification metadata pinned until closeout stamps the HFX-L8 commit.
- 2026-07-07T16:50+02:00 — 260707-HFX-L1 route impact (provider containment R1): `provider_tools.py`
  gates launch-capable watcher actions and query tools on the live on-disk authority
  (`require_provider_launch_authority`, fail-closed; stop/status/shutdown-all ungated),
  `worktree_tools.py` re-reads the authority before provider setup (live-map settings when armed,
  `providersAuthority` veto block otherwise, worktree creation unaffected), and
  `benchmark_tools.py` threads the live provider-id set as `allowed_provider_ids` into both
  benchmark requests. Verification metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-07-06T23:59:58+02:00 — L14 route impact (body): task_doc_tools carries the additive master-only `orchestrates` field end-to-end. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T23:59:30+02:00 — 260703-L14 (visual hierarchy + chat grouping) route impact: `task_doc_tools.py` added `orchestrates` to the `set_field` whitelist (`_MUTABLE_FIELDS`) — a flat string list, master-only via the schema backstop. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T03:20+02:00 — No route impact: 260703-L9 reuses `_guards.require_repo` unchanged as the repo allow-list boundary for the new `serving/notes.py` API; no controller changed.
- 2026-07-05T19:10+02:00 — 260703-L8 route impact (cycle 6, small): `worktree_integrate_tool` now threads `config.orchestration.gate_policy` into integrate `WorktreeArgs` (mirroring the closeout path), so the integrate-side master-handover guard evaluates the configured policy instead of the all-human dataclass default. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T12:32+02:00 — No route impact: 260703-L4 only threads
  `config.orchestration.gate_policy` through `worktree_tools.py` into closeout
  args; controller boundaries and public controller responsibilities are
  unchanged. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-03T00:35+02:00 — L11 route impact: task_reopen_tool joins task_doc_tools (task domain); worktree_abandon_tool ends its anchored ambient lifecycle.
- 2026-07-02T18:35+02:00 — No route impact: operations-integration L7 fixed the native argv inside the
  typed `cgc_dependencies` wrapper (`provider_tools.py`) from the stale `analyze dependencies` to the
  current `analyze deps` subcommand. The controller surface, tool names, and response envelope are
  unchanged, so the route model this overview describes is unaffected (detail in the file sidecar).
  Verification metadata pinned until closeout stamps the L7 commit.
- 2026-06-29T22:57+02:00 — No route impact: `task_doc_tools.py` gained the `remove_subtask` op (CRUD
  delete: drop the master row + delete the leaf doc unless `keep_file`); the controller stays a typed
  operation facade, so the route model is unchanged (detail in the task_doc_tools.py file sidecar; task
  260629_post-landing-cleanup L2).
- 2026-06-29T21:24+02:00 — No route impact: `task_doc_tools.py` now refuses `kind="light"` and defaults
  an absent `kind` context-awarely (subTask under a leaf contract, else master); the controller stays a
  typed operation facade, so the route model this overview describes is unchanged (detail in the
  task_doc_tools.py file sidecar; task 260628_post-landing-cleanup).
- 2026-06-28T22:41+02:00 — No route impact: operations-integration L1 extracted `read_files.py`'s path-confinement + sidecar-pairing helpers into `kernel/sidecar_pairing.py` (behavior-preserving; `read_ar_files` re-imports them under their former private names). `read_files.py` stays a typed operation facade and no controller signature/surface changed, so the route model this overview describes is unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the L1 code commit.
- 2026-06-26T20:18+02:00 — Task 21 route impact: `task_doc_tools.py` remains the task-document authoring
  controller and now also composes same-root leaf-to-master row sync through the task service layer.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T16:15+02:00 — No route impact: re-verified `task_doc_tools.py`
  against the source-branch `replace` controller (`_replace` preserves the existing JSON path and
  refuses slug/kind path drift); lifecycle-gate API consolidation does not change the controller
  route model.
- 2026-06-26T15:33+02:00 — No route impact: task 25 preserves `task_doc_tools.py`'s
  source-branch `replace` operation; lifecycle-gate API consolidation does not change the controller
  route model, and operation-level detail remains in file sidecars. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: controllers now route `parent_task` and `leaf_id` through context/worktree operations, and `task_doc_tools.py` creates `seriesContractPath` plus `enclosures[]` references instead of the retired `contractPath`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T23:04+02:00 — Dashboard task 14 adds `lifecycle_finalize_task_tool` to `worktree_tools.py`. The controller remains a typed operation facade: it confines coordination paths, builds `FinalizeArgs`, and delegates branch-edge proof, cleanup verification, and task-document reconciliation to `worktrees/modules/finalize.py`.
- 2026-06-23T01:40+02:00 — No route impact: slice 07b v1, `read_files.py` now passes `repo.repo_id` to `emit_read_packet` so the `read.packet` carries `data.repoId`; the controller stays a typed operation facade delegating emission to the `observer` service, so the route model this overview describes is unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the slice-07b code commit.
- 2026-06-23T00:53+02:00 — No route impact: slice 07 S5 retargets the `read_files.py` compact-reset docstring only — the `compact-reset.json` producer is deferred to the post-3.0 agentic-control-plane (no session-hook producer), with the consumer (`_maybe_reset_served`) + `refresh=true` kept as defensive scaffolding; no controller signature or behavior changed, so the route model this overview describes is unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-06-22T22:33+02:00 — Slice 07: added `read_files.py`, the `read_ar_files` controller (paired source+onboarding batch reads of ≤5 repo-relative paths, with its own path-confinement guard, route-index onboarding lookup, session-deduped overview front-door, and facts-only `read.packet`); added it to the Hot Path Summary. It stays a typed operation facade — resolution lives in the controller so a later dashboard `GET /api/files` route can reuse it — so the route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-06-19T07:23+02:00 — No route impact: slice 3c R5 adds a `dry_run` param + a `_preview` helper to `task_doc_tools.py` (renders + diffs the would-be doc and returns `rendered`/`diff`/`wouldLose` without writing); the controller stays a typed operation facade, so the route model this overview describes is unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T06:03+02:00 — No route impact: slice 3c R4 adds `statusNote` to `_MUTABLE_FIELDS` and drops the master-only guard on `set_section` (a leaf may upsert freeform sections; the schema validator backstops) in `task_doc_tools.py`; the controller stays a typed operation facade, so the route model this overview describes is unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T05:15+02:00 — No route impact: slice 3c R3 adds `codeExamplesNote` to `_MUTABLE_FIELDS` in `task_doc_tools.py` so `set_field` can record the deferred-examples note; the controller stays a typed operation facade, so the route model this overview describes is unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-14T00:16+02:00 — No route impact: slice 3c commit 3 adds master ops (`set_subtask`/`set_section`) + master `create` handling to `task_doc_tools.py`; the controllers stay typed operation facades, so the route model this overview describes is unchanged (detail in the file sidecar).
- 2026-06-13T22:34+02:00 — Slice 3c commit 1: added `task_doc_tools.py`, the op-dispatched controller behind the `task_doc` authoring tool (load/create the `ar-task-document/v1` JSON, apply one edit, re-render the markdown); added it to the Hot Path Summary. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T18:45+02:00 — No route impact: slice 2c adds the observer-attribution wiring to `worktree_tools.py` (`_attribute_start`/`_attribute_attach` driving `ambient().promote`/`attach`); the controllers stay typed facades delegating behavior to the `observer` service, so the route model this overview describes is unchanged (detail in the file sidecar).
- 2026-06-11T06:47+02:00 — Issue #62 worktree-only closeout: `worktree_tools.py` dropped the `direct_closeout_*` controllers, so the Hot Path Summary now describes it as the worktree-operations facade only.
- 2026-06-10T09:56+02:00 — No route impact: sub-task D adds `worktree_sync_tool` as another typed worktree operation facade in `worktree_tools.py` (path confinement + forwarding); the route model this overview describes is unchanged (detail in the file sidecar).
- 2026-06-10T09:30+02:00 — No route impact: sub-task B's `worktree_tools.py` change is a plumbing-only forward of `stale_base_choice` into `WorktreeArgs`; the controller surface this overview describes is unchanged (detail in the file sidecar).
- 2026-06-10T08:39+02:00 — GitHub #54 sub-task A: `context_packet.py` gained the opt-in freshness section (`include_freshness`, kernel-backed code/memory branch freshness, `ledgerMapsCodeHead`).
- 2026-06-10T07:40+02:00 — GitHub #53: `worktree_tools.py` start controller hands the temp lifecycle settings file to the background setup thread (skip-unlink on a `starting` result), forwards `retry_provider_setup`, and bounds worktree provider setup by `timeoutCaps.providerSetupSeconds` instead of the docker-control default.
- 2026-06-06T03:43: Re-verified against the current controller surface (9 files incl. `_guards.py` and per-domain tool modules); corrected `mcp/tools.py` references to the `mcp/tools/` package; re-stamped to `7123da56`.
- 2026-05-28T19:52+02:00: Created after the MCP controller surface split out of the former `skill_tools.py` mega-facade.
  `27242ecb`): recorded the candidate-write boundary joining the seam — the context resolution that reads the live
  dataset identity and seals it (the only way a batch's precondition is built, because `CandidateResolution` has no
  dataset-identity field), the batch operation that takes `destination.authorship` so a payload cannot supply
  provenance, and the two label operations — and re-recorded the boundary that did **not** move: the seam still has
  no non-test importer in `mcp/src`, adding a function inside the module does not create one, and the worker
  report's "resolved" claim about that observation was withdrawn in review. Verification metadata remains
  closeout-owned.
## 260915-KS-L23 The Application Seam: The Ruler, The Two Tool Legs, And The Start Gate

Three of this route's modules changed for `KS-R23@v1`, and each change is about a **caller being able
to trust what the application layer told it**.

**The ruler (item 26 / D-33).** `runtime/startup.py::measuring_build_stamp()` reports the build a
caller is actually executing, and `memory_quality/controller.py` stamps it onto the memory-quality
response at **all three** entry points (`run_memory_quality_request`,
`start_memory_quality_request`, `poll_memory_quality_request`) — the same field `memory_tools.py`
adds to the citation responses. It exists because the MCP tool surface executes a *fixed serving
build*, so before this leaf a curator could not tell a candidate-ruler count from a serving-build
one. The checklist's own `pairIdentity` always named the candidate's content; the build stamp is what
names the ruler that judged it.

**The two tool legs.** `worktree_tools.py`'s start gate said it was protecting a persistent
lifecycle when its actual condition is *this session's own current lifecycle is bound to another
enclosure* (D-17, item 8), and a leaf's declared `Requires` lines remain operator discipline — the
gate reports them, it does not enforce them, and the module says so now. `memory_tools.py` gained the
`read_steps` response shape its own model declares (D-9, item 20) and the serving-build stamp on
`citation_fix` / `citation_migrate`, so a repair count also names its ruler.

**What a reader of this route should carry forward.** `controller.py` is where the curator checklist
is assembled, and the three findings that are *not* curation debt are constructed there:
`affected.closure` is `blocked` because the memory-quality route passes
`affected_closure_plan_digest=None` (the plan is compiled by the **certification** route, carried
into the certificate as `affectedClosurePlanDigest`), `coherence.record` is `blocked` until the
leaf's own coherence authority is current, and `integrity.onboarding_drift_check.summary` is
**diagnostic** — it does not enter `curatorActionableCount`. The refresh-attestation gate in the same
module is the one that does: it refuses a changed source whose sidecar body is unmodified or carries
only refreshed metadata/history, which is why every changed-source sidecar in this leaf either has a
body edit or an exact `No content impact:` entry.

## 260915-KS-L31 The Merge Adapter Gains Its Driver

This route's third seam stopped being reachable only by a caller that already knew how to compose it. The
change is one module's worth of new surface in `application/knowledge_merge.py` and one caller in
`worktrees/`, and the two halves are split by the layer contract rather than by taste.

- **The dataset half lives here, and it has to.** `merge_conflicted_stages(destination, stages,
  repository_root, commits)` takes the three materialised Git index stages of one conflicted path, reads
  each stage's identity with `dataset_identity`, opens the left stage read-only to decode the single
  `repository` row the base claim is about, composes `resolve_knowledge_merge_base` with
  `merge_resolved_knowledge_datasets`, and returns **one boolean**: settled or not. It is the lowest layer
  that *may* read a dataset's identity — a module under `worktrees/` is forbidden from importing the memory
  domain at all, which the layer test enforces — so the worktree module hands it three paths and receives
  the boolean. `ConflictCommits` groups the three commits one conflicted merge spans, because the adapter
  requires all three together and a base claim naming two of them would not be a claim.
- **The Git half lives in `worktrees/knowledge_conflict.py`.** Materialising the index stages binary-safely
  (through `git checkout-index`, not a text-decoding read of a SQLite file) and staging the settled result
  are worktree facts. Its `settle_knowledge_conflicts` returns the paths it could **not** settle, and that
  tuple is the contract with the sync transaction: what comes back is exactly what the agent is still asked
  to resolve.
- **The Git non-claims survive the wiring, and that is the point worth carrying forward.** No merge driver is
  installed, no attribute is configured, no commit is created on this path, and nothing here takes a
  compatibility verdict. What changed is *who calls it*: before, an agent facing a conflicted binary
  knowledge database had to discover `resolve_knowledge_merge_base` and `merge_resolved_knowledge_datasets`
  and drive them by hand; now the sync transaction routes the merge and the adapter still decides it. A
  structurally merged result says the union is valid, never that the combined knowledge is correct.
- **A refusal is preserved rather than swallowed.** Every way of not settling — a stage that is not a
  dataset, an adapter refusal (a schema disagreement above all), a publication that did not happen — returns
  `False`, so the path stays conflicted for the agent. The routing narrows the agent's work instead of
  hiding any of it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The driving entry point: three materialised stages in, one settled-or-not boolean out, and the identity read only this layer may perform. | `merge_conflicted_stages` | mcp/src/agents_remember/application/knowledge_merge.py:113-181 |
| The three commits one conflicted merge spans, grouped because the adapter's base claim needs them together. | `ConflictCommits` | mcp/src/agents_remember/application/knowledge_merge.py:223-234 |
| The one non-test importer this module gained, the Git half that cannot live here, and the single-path entry point the authored retry re-enters. | `settle_knowledge_conflicts`; `settle_knowledge_conflict`; `_materialise_stages` | mcp/src/agents_remember/worktrees/knowledge_conflict.py:201-238; mcp/src/agents_remember/worktrees/knowledge_conflict.py:241-257; mcp/src/agents_remember/worktrees/knowledge_conflict.py:138-158 |
| The transaction seam that routes the conflict and narrows the agent's list. | `_continue_memory_merge` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:383-415 |
| The layer rule that forces the split, enforced by a test rather than documented. | `test_lower_ranked_owners_do_not_import_the_memory_domain` | mcp/tests/test_knowledge_store.py:839-857 |

## Update History
- 2026-09-19T23:20+00:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): added this section because this route's third seam gained its driver, and corrected the two L5 sentences the change falsifies — the *callable rather than wired* bullet and the "no non-test importer" sentence now carry inline supersession pointers to this section instead of being silently left to mislead. The section records the two-module split and why the layer contract forces it, the boolean refusal contract, the preservation of every Git non-claim, and the exact importer. No verification stamp advanced; closeout owns it.

## Update History
- 2026-09-20T06:50+02:00 — 260915-KS-L40 curator (uncommitted CYCLE-02-remainder change set on `ar/260915-ks-l40-ar`, code base `f79f4db7`): **route body updated.** This route's third knowledge seam changed shape: `application/knowledge_merge.py`'s `merge_conflicted_stages` now returns `KnowledgeStageSettlement(settled, conflict, refusal, detail)` instead of a boolean, so the engine's typed refusal and its row-level `MergeConflict` travel out of the seam instead of being discarded at it, and the four ways a path never reached the adapter are named rather than collapsed into one `False`. The same module passes the caller's one `AuthoredReconciliation` through to the adapter unchanged. `application/worktree_tools.py`'s `worktree_sync_tool` now takes the paired `resolution: SyncResolutionInput | None` (the action plus the decision it may carry) rather than a bare `resolution_action`, pairing forced by the `PLR0913` ceiling and by the driver refusing the two as a pair. A body change, not a metadata-only refresh.
- 2026-09-20T05:48+02:00 — 260915-KS-L41 curator (uncommitted change set on `ar/260915-ks-l41-ar`, code base `756c47b3` at this leaf's cut and `f79f4db745ad00b908d6ce4871d0b4ab2320207c` after the L39 sync, memory base `da33325c` at the cut and `37d0787571bfbf92890049ee0614fa159012be39` after it): **added the L41 section, which is the route impact of the mounted view front door's own repair.** The section is new at the top of the route's change narrative and states the three behaviours this leaf changed in `application/knowledge_view_render.py`: the path seed is one frontier computed once per reader (`_seed_revisions`, `_seed_memo`, `_seeded_realizations`, `_seed_selects`, with `_seeded_family_revisions` and `_selected_invariant_revisions` as its two derived frontiers) and `_source_context_candidates` now applies it at all; family membership is read through `reader.family_member_rows()` from the dedicated `family_member` table rather than through the generic envelope kind read, with both membership-derived row shapes stating `fact_kind="member"`; and the `(repository_root, code_tree_id)` pair is completed or not named at all inside `_source_resolution` / `_current_code_tree`. It also records, as an open question rather than as settled behaviour, that a path-seeded family read is filtered to the seed's frontier while the unseeded or `familyRevisionId` read shows complete membership. **This insertion shifts every heading below it**, so the three off-route cards that cite this document by line were re-read and repointed in the same pass rather than left to rot: `application/__init__.py.md`'s `## Hot Path Summary` cell now reads `275-282` (it was `107-107; 225-232`, and `107-107` was already stale before this leaf — it is a body paragraph, not the heading the claim names), `application/skill_resources/__init__.py.md`'s section-extent cell now reads `68-108` (the L4 section moved by the same `+50`), and `application/runtime/skills.py.md`'s document-range cell now reads `1-362`. No claim was re-worded to fit a stale pointer, and `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained as recorded — the candidate is uncommitted and the governed closeout owns the real stamp.

## 260915-KS-L42 The Curator Ingest Report's Own Identity Sentence, Corrected To The Rule The Code Follows

**This route's impact is one public field in `application/knowledge_curator_ingest.py`, and the field was the last place an obsolete rule survived.** `IngestReport.derived_identities` described identity as `uuid5` over "the enclosure's recorded code base commit … plus the written path for a target" — the rule the module followed before `_identity` moved to the repository's own namespace, and the exact sentence a verification round was misled by when it read a minted identity as baseline-scoped. The field was corrected here to name the fixed `_INGEST_NAMESPACE` and the repository's own namespace identity, and **L43 corrected it again** (see that section): it now states the split the code actually implements — the invariant and its first revision are **allocated** by the API and recorded under an idempotency key scoped by the enclosure's task identity, while a citation's route, anchor and claim are **derived** — plus both negatives: no allocated identity contains the enclosure, the branch, the baseline or the label, and the derived half's stable component is the repository namespace and never the recorded base commit. The module docstring carries the same split.

**The sentence is now checkable against the derivation rather than against a phrase.** The guarded assertion lives in `mcp/tests/test_knowledge_curator_ingest_list.py`'s `test_the_report_names_the_candidate_its_receipt_the_lane_and_the_exact_inputs`, an already-collected case because both lanes stand at their ceilings: the base commit must not appear in the field, the field must name the repository namespace, and `_identity` is compared with `uuid5(_INGEST_NAMESPACE, f"{repository_id}|invariant|E-named|")`. A phrase check would have passed on the stale text, so the case runs the rule instead.

**What did not move.** The resolution tree is still the leaf's own code line and the recorded `source_identity` is still that tree's blob; admission (resume, baseline-fork, create), the publication leg, the route leg and the refusal vocabulary are untouched by this change. The claim row in this route's reference table that names `_enclosure` as the helper the report's identity sentence names was corrected in the leaf's own card, not here, because this overview carries no row for that field.

## Update History
- 2026-09-20T07:30+02:00 — 260915-KS-L42 curator (uncommitted CYCLE-02 repair change set on `ar/260915-ks-l42-ar`, code base `74c6c693`): **route body updated.** The section above is appended at the end of this route's change narrative, so no existing heading moved — which this document's own history has had to repair twice for off-route cards that cite it by line. It records the route's own impact for this leaf: the corrected `IngestReport.derived_identities` field and module docstring in `application/knowledge_curator_ingest.py`, the guarded assertion that holds the field to the derivation rather than to a phrase, and the boundary that nothing about admission, publication or the route leg moved. No reference row in this document cited the field, so none needed re-pointing; the card's candidate reading recorded in the entry now names this leaf's candidate and `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained as recorded.



## 260915-KS-L44 The Family And Invariant Realization Rows Report The Location They Were Recorded With

**This route's impact is two projections in `application/knowledge_view_render.py`, and it is a repair rather than an addition.** `render_family` (`:1039-1083`) and `render_invariant` (`:987-1033`) now copy `candidate.role`, `candidate.path` and `candidate.locator` into the `FamilyRow` / `InvariantRow` they build, so a family or invariant read that answers "where is this realized" reports a place. The location was never missing from the pipeline: `_member_locations` (`:769-799`), `_family_candidates` (`:678-725`) and `_invariant_candidates` (`:547-613`) already set all three fields on the candidate they hand over, and **none of those three functions was touched** — the projection was dropping an answer it had been handed, and the two models that receive it (`models/knowledge/view.py`'s `FamilyRow` and `InvariantRow`) declared no field for it. Both views decode the one stored locator through the same `_LOCATOR_ADAPTER` (`:904`) the source-context view already used, so all three views now agree about one claim's place; nothing is derived and no filename is read out of an authored rationale — which is the point, because the original fixture's rationale happened to contain a filename and a variation whose rationale names none is what separated a carried location from a plausible-looking one.

**What did not move, and why the two row models differ in shape.** The path seed, the membership read through `family_member_rows()`, the one-frontier realization selection and the exact detection-run selection are all unchanged; the family and source-context response sets are byte-identical before and after apart from the three fields, and `source_context` was not moved at all — the family and invariant views were brought onto the already-correct one rather than all three being moved together. `InvariantRow` is also the model behind the invariant view's `fact_kind="statement"` rows, so the three fields appear there as explicit `null`s, which is this surface's existing convention (`knowledge_read_payload` serializes with `model_dump(mode="json")` and no `exclude_none`, exactly as `SourceContextRow.anchor_state` is already emitted as null).

**One boundary is now stated where a caller meets it, and nothing was widened into a contract.** `mcp/tools/knowledge.py`'s `ReadToolRequest` docstring records that `databasePath` and `repositoryId` **are** the knowledge selection and that the caller owns both: the runtime config, a repository's coordination declaration and the memory layer's settings carry no knowledge database or namespace, no shipped helper or filename convention resolves a repository or a task to a knowledge SQLite path, and the namespace is minted at ingestion — so the cold-planning discovery path the external recheck asked about does not exist in this product. That is recorded as the finding it is; exposing a discovery mechanism (a settings key, a `context_packet` field, a resolver) is a product decision and was deliberately **not** taken here.

**Sibling sweep, measured and closed.** An AST cross-check of every `Candidate(...)` construction against every row model's declared fields, plus a read of each renderer, over five renderers and five row models, found **no third instance**: the two rows that ever carried a location candidate field into a view whose declared answer needs it are exactly the family member-location rows and the invariant realization rows, and both are now fixed. `ReviewMatrixRow` and `CurationQueueRow` drop `role`/`fact_kind`/`statement`/`path`/`locator`, but no candidate feeding either view sets a `path` or a `locator`, so there is nothing to drop; `SourceContextRow` and `FamilyRow` never have `essential_conditions`/`conditions_omitted` set on any candidate, so those are dead payload fields rather than dropped answers; and `ViewSourceRow` is the reader port's own DTO, not a rendered row. Recorded here so the next reader does not re-run the hunt.

## Update History
- 2026-09-21T12:40+02:00 — 260915-KS-L44 curator (uncommitted CYCLE-03 change set on `ar/260915-ks-l44-ar`, code base `2a96eb88`): **route body updated.** The section above is appended at the end of this route's change narrative, so no existing heading moved and no off-route card that cites this document by line needed repointing. It records this route's own impact for the leaf — the two projections that now carry a realization row's recorded location, the three candidate builders deliberately **not** touched because they already set it, the single locator decoder all three views share, the explicit-`null` convention on the row kind that has no location, the knowledge-selection boundary now stated in `mcp/tools/knowledge.py`'s `ReadToolRequest` docstring as a finding rather than widened into a contract, and the completed sibling sweep with its scope. Three cards outside this leaf's change set that cite `models/knowledge/view.py` by line were re-read and repointed in the same pass; that repair is recorded on that file's own card rather than here. No verification stamp was advanced; the candidate is uncommitted and the governed closeout owns the real stamp.

## 260915-KS-L47 Two Write-Path Claims The Application Layer Now Actually Keeps

This route's ingest entry point carried two of the three failures the master-exit review confirmed, and
both are repaired in `knowledge_curator_ingest.py`. **The retry guard is now bound to the whole
normalized semantic write intent.** `_content_digest` gained `dispositionSource`, `namedInvariantId`,
`predecessors` as an ordered list, the normalized `RealizationRole` the write path stores, and
`roleRationale`; `entry_id` and the derived `declares_invariant` stay out on purpose, which the function's
own docstring now states instead of the withdrawn universal that it digested "every fact the stored truth
is made of". A material field change under a held key therefore refuses `allocation_content_conflict`
with both digests named, where before it returned exit 0, `batchState: replayed`, no refusal and an
unchanged database. **Explicit anchor reuse is now resolved through the stored anchor.**
`_require_stored_anchor` reads the named identity through `_Source.anchors` (candidate then baseline) and
requires the supplied path, blob and locator to agree with it, refusing `anchor_reuse_mismatch` or
`anchor_id_not_stored` **before the plan exists** -- the measured defect returned `changed` and published
while the receipt and the stored claim named different constructs -- and it is invoked inside
`_plan_target_inner` after the supplied target is observed and before `_target_identities` adopts the
named anchor as the claim endpoint. The read itself goes through the memory layer's new public
`read_anchor`, so the intake does not re-derive how an anchor row is decoded.

The migration/census usability gap this leaf recorded stays a recorded gap rather than a repair: no CLI
was built here, and `KS-R21`'s "shipped candidate operation" is the existing batch writer, which a fresh
probe used successfully. Nothing else this route owns changed.

## 260921-ICR-L1 The Review Adapter Delegates Its Resolution, And The Endpoints Are Exact

This route gained one module and lost one responsibility. **`application/review_candidate_resolution.py`
is now the sole owner of the live review's exact source endpoints and of the dataset pair**, and
`application/knowledge_review.py` imports and re-exports its names instead of defining them. The move is
the packet's own instruction ("move a touched responsibility out of the over-limit review adapter before
adding behavior; do not duplicate its implementation") and the module's stated second reason is the
repository's file-size rail: the adapter was 1281 lines before the change and 1113 after.

**What the resolution now binds, where before it bound one side and deliberately declined the other.**
The **baseline** is the enclosure contract's recorded `code_base_commit` and the **candidate** is the
tree `capture_future_code_candidate` derives through a private index — the leaf's `HEAD` with every
staged, unstaged and eligible untracked change applied, ignored paths still excluded, the real Git index
left byte-identical. The candidate side supplies **both** a code root (`contract.code_worktree`) and a
tree id (`captured.codeCandidateTree`). The superseded behaviour is stated here because this route's L22
section still describes it: `candidate_code_root` used to be `None`, on the recorded reasoning that a
live leaf's uncommitted line had no tree id, and the comparison therefore reported the source expansion
it could not make instead of resolving one. A contract that records **no base commit** is now refused by
name (`candidate_unresolved`, `offending_input="baseline"`) rather than half-resolved, because a
baseline endpoint that cannot be bound is a state a caller must act on, not a `None` to read past.

**The endpoints are re-checked at the last possible moment, and that is the adapter's own new
behaviour.** `compose_review` calls `require_current_candidate_identity` after the comparison and the
review-matrix read and immediately before it builds the payload; the shipped capture owner is re-run and
any field that disagrees produces the named refusal carrying **both** complete identities
(`expected`/`observed`) and the exact side that moved. The recheck is deliberately not part of
resolution: a capture that was current when it was taken can be stale by the time a payload would be
returned, and a moved input must not be published as the candidate's own comparison. The stated next
action is to reopen the review so the candidate is captured again — the surface substitutes neither the
moved `HEAD`, nor another branch, nor a different working tree.

**What did not move.** Selection, the comparison (`diff_knowledge_scope`), L20's review matrix, the five
published remaining counts, the staleness/submission coupling, the entry list and the receipt-derived
namespace are all unchanged, and the adapter still selects nothing. The three published path constants
keep their single spelling and their import path: the sibling module defines them, the adapter re-exports
them, and `cli/knowledge_ingest.py` still reads them from `application.knowledge_review` — which is what
keeps "the candidate the leaf authored" and "the candidate the review resolved" one directory.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The resolution's new home: the module's own statement of what it binds, why the working tree is never an endpoint, and that every failure is a named state.** | `code_base_commit`; `capture_future_code_candidate` | mcp/src/agents_remember/application/review_candidate_resolution.py:1-28 |
| **The bound endpoints: the recorded base commit on one side, the captured add-all candidate tree on the other, with the root travelling beside each tree id.** | `resolve_review_candidate`; `ReviewCandidateResolution` | mcp/src/agents_remember/application/review_candidate_resolution.py:132-177; mcp/src/agents_remember/application/review_candidate_resolution.py:180-242 |
| The recorded base as a precondition, refused by name rather than half-resolved. | `resolve_review_candidate` (recorded-base refusal) | mcp/src/agents_remember/application/review_candidate_resolution.py:180-242 |
| **The capture is the shipped owner's, wrapped rather than re-implemented, and its own mid-capture head check is what makes a moved head a named state.** | `_captured_candidate`; `capture_future_code_candidate` |mcp/src/agents_remember/application/review_candidate_resolution.py:511-525; mcp/src/agents_remember/worktrees/modules/future_code_candidate.py:25-52|
| **The pre-publication recheck (for a tree comparison, the memory candidate is recaptured first, MIK-R25) and the refusal that carries both identities, with the one recapture action.** | `require_current_candidate_identity`; `_moved_candidate_refusal`; `_CAPTURE_INPUTS` |mcp/src/agents_remember/application/review_candidate_resolution.py:118-122; mcp/src/agents_remember/application/review_candidate_resolution.py:308-341; mcp/src/agents_remember/application/review_candidate_resolution.py:344-367|
| **The adapter's new call site: the recheck runs after the reads and before the payload, and a moved input refuses the whole render.** | `compose_review` (endpoint recheck) | mcp/src/agents_remember/application/knowledge_review.py:334-574 |
| The adapter's re-export of the sibling surface, which is what keeps the ingest CLI's import resolving. | `__all__`; `resolve_review_candidate` | mcp/src/agents_remember/application/knowledge_review.py:199-213; mcp/src/agents_remember/application/knowledge_review.py:49-129 |
| **The pair preflight and the record-beside-the-bytes namespace remain the sibling module's, and this route's two operations still call them. The namespace rows' ranges and their wording were corrected by `260921-ICR-L34`, which made the second record answer.** | `missing_dataset_half`; `review_namespace` |mcp/src/agents_remember/application/review_candidate_resolution.py:370-388; mcp/src/agents_remember/application/review_candidate_resolution.py:391-430|
| **The case module that measures this route's half of the change through the real resolution, the real capture, the real comparison and the served payload.** | `test_the_rendered_review_publishes_the_endpoints_and_reaches_the_whole_candidate`; `test_a_capture_input_that_moves_before_publication_is_refused_by_name` |mcp/tests/test_knowledge_review_source_endpoints.py:473-532; mcp/tests/test_knowledge_review_source_endpoints.py:538-562|

## Update History
- 2026-09-21T13:07:00+02:00 — 260921-ICR-L1 curator (uncommitted change set on `ar/260921-icr-l1`, code base `f745e166`): **route body updated.** The section above is appended at the end of this route's change narrative, so no existing heading moved and no off-route card that cites this document by line needed repointing. It records this route's own impact for the leaf: the review adapter's resolution moved out into `application/review_candidate_resolution.py` and is imported/re-exported here; the endpoints are now exact (recorded base commit plus captured add-all candidate tree, with a root beside each tree id) where the L22 section still describes a candidate side that supplied neither; a contract recording no base commit is refused by name; and `compose_review` re-checks the captured identity immediately before building the payload, refusing by name with both identities when an input moved. **the candidate reading recorded in the earlier entries is untouched and no verification stamp was advanced** — the candidate is uncommitted and closeout owns the real stamp. Eleven reference rows of the `260915-KS-L22` section cited `application/knowledge_review.py` by line; the resolution's departure (1281 → 1113 lines) invalidated all of them, and each was re-read and re-derived in the same pass: the six rows naming a construct that now lives in the sibling module were re-pointed at that module (or, where the construct is the adapter's own call site, at the adapter's current extent), and the four rows whose ranges had run past the end of the shrunken file were replaced with the extents their anchors occupy now.

## 260921-ICR-L19 The Ordinary Read Selects And Reads The Repository's Published Intent

**This route gained one module and one returned half, and the leaf they belong to (`260921-ICR-L19`,
primary requirement ICR-R19@v1) answers a question the paired read could not: "what did this repository
already intend here?".** `application/published_intent.py` is the selection the ordinary route was missing
— from the `CoordinationContext` the read already carries it resolves the repository's published knowledge
dataset, resolves the source-resolution pair recorded anchors are observed against, seeds the shipped
selective read with the paths the caller asked about (or with exact record identities), and shapes one
bounded page per seed. It is not a second read: the page is built by `application/knowledge_read.py`'s
`open_read_context` + `read_knowledge_scope`, **which this leaf deliberately did not touch** — the gap was
the caller, not the read.

**Three route-level facts a reader should carry.** (1) The route **declares** the location it reads and the
ordinary write side has to publish there: no shipped owner computes or defaults a publication destination
today (`IngestPublication.destination_path` is whatever the caller's `--publish-to` names, and a run that
names none commits without publishing), so wiring the ordinary publisher to this one location is
ICR-R20@v1's obligation and the two-consecutive-task journey that proves task A's publication lands where
task B's planner looks is ICR-R25@v1's. (2) *Which* memory root is read follows the resolved scope with
**no fallback between the two**: the canonical external memory root when no enclosure is in scope, the
contract's memory **worktree** inside a leaf — so a publication that is not on the line being read is
reported `not-recorded`, never substituted from the other root. (3) **No task, leaf or enclosure is
required to read intent**: the route's only input is the context, and `task_ref` is left unset.

**Every failure is a named state, and that is what makes the attach additive.** `not-recorded` is returned
only when the location holds no file system entry at all; a directory, a dangling link or a device sitting
there is `unusable`, as are bytes that are not a dataset of this code and a dataset bound to another
repository's authority home (refused by name, with no rows served). A path no recorded anchor could carry
is refused **as a seed** rather than answered with an absence this read never observed, and an identity the
snapshot does not hold is the read's own `selector_absent` — a fact about this snapshot, never a claim that
the obligation does not exist. Because every one of those answers is carried inside the block,
`application/read_files.py`'s attach cannot cost the caller the paired source and onboarding bytes this
route exists to return: the block is attached on every call, including when the repository publishes
nothing yet, because an omitted block is indistinguishable from a route that never ran.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The new module's public surface: resolve the repository's publication, seed it with the requested paths, and read one bounded page per path.** | `published_intent_block`; `published_dataset_path`; `read_published_intent` | mcp/src/agents_remember/application/published_intent.py:464-479; mcp/src/agents_remember/application/published_intent.py:482-511; mcp/src/agents_remember/application/published_intent.py:283-299 |
| **The named states the route answers with, and the guard that makes "never silently select another repository" a verified fact.** | `resolve_published_intent`; `_absence_state`; `_authority_mismatch` | mcp/src/agents_remember/application/published_intent.py:249-273; mcp/src/agents_remember/application/published_intent.py:302-326; mcp/src/agents_remember/application/published_intent.py:431-461; mcp/src/agents_remember/application/published_intent.py:619-636; mcp/src/agents_remember/application/published_intent.py:587-604; mcp/src/agents_remember/application/published_intent.py:372-389 |
| **The shipped read the new route delegates to, reused unchanged by this leaf.** | `open_read_context`; `read_knowledge_scope` | mcp/src/agents_remember/application/knowledge_read.py:108-141; mcp/src/agents_remember/application/knowledge_read.py:144-166 |
| **The ordinary read's attach point, and the response field the block travels on.** | `read_ar_files_tool`; "published_intent"; `published_intent` | mcp/src/agents_remember/application/read_files.py:106-181; mcp/src/agents_remember/application/read_files.py:148-148; mcp/src/agents_remember/models/read_files.py:80-80 |
| **The cases that measure this route's half of the change: the application-layer route, and the named absence a repository that publishes nothing reports. Since MIK-R24 both measure the database block through `published_intent_block` directly, and the two mounted-route cases assert that an unconverted tree is read as `legacy-format`.** | `test_the_ordinary_read_returns_the_published_intent_at_its_exact_identities`; `test_a_repository_that_publishes_nothing_reports_not_recorded`; `test_the_mounted_route_returns_no_knowledge_section_for_unconverted_memory` | mcp/tests/test_read_ar_files.py:434-469; mcp/tests/test_read_ar_files.py:471-480; mcp/tests/test_read_ar_files.py:709-723 |


## 260921-ICR-L2 The Review Adapter Delegates Three More Responsibilities, And The Task Context Becomes The Entry

**Route meaning changed: this route gained three modules and the Intent Reviewer can now be opened
without a subject.** `application/knowledge_review.py` (1113 → 863 lines) keeps its role as the thin
adapter and public entry, and hands three responsibilities to modules named for what they own:
`application/review_source_inventory.py` measures the exact, status-bearing change inventory of the
bound tree pair and renders the source pane; `application/review_record_rendering.py` renders the
record collections the caller supplied into the evidence and submission values; and
`application/review_task_context.py` composes the entry that needs no selected subject. `__all__` is
unchanged and every moved name is re-exported, so the ingest CLI and the existing test modules keep
importing from the same place.

**`compose_review` now measures the inventory first and unconditionally**, from the two tree ids the
resolution bound, *before* any dataset is opened and before the selector branch. That ordering is the
route-level fact: a task with no recorded invariant — or with no datasets at all — still has a source
review, because the one half of a review that cannot depend on a knowledge selection is measured
before anything that can refuse. A request whose `selector` is `None` is then answered by
`task_context_review` with `comparison=None`, `staleness.state="not_compared"` and a knowledge pane in
the `task_context` selection state — and, since the sync that brought leaf `260921-ICR-L5`'s landed work
into this candidate, with a **third** state for a half that is present but cannot be read: that fact is
*stated* (the pane's reason plus `limitation:knowledge_half_unreadable`) instead of refusing the review
that never reads a dataset; a request that names a subject keeps the shipped path through the
new `_open_dataset_pair` and `_review_matrix` steps, including every refusal it already had. The
inventory's own state is declared at the top level beside the comparison's limits
(`limitation:source_inventory_unavailable`, `limitation:source_inventory_partial`), so a limit is never
only inside a pane.

**One Git observation now serves two consumers.** `application/knowledge_diff.py`'s
`git_tree_difference_probe` — the comparison's expansion seam — became a one-line delegation to
`review_source_inventory.tree_difference_observation`, so the expansion and the review's inventory read
one measurement through one delimiter-safe interface (NUL-delimited `--raw -z`/`--numstat -z`) rather
than two implementations that could disagree about which paths changed.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The route's new owner of the source half: the inventory's own statement of why it is measured from the pair, why the Git interface is delimiter-safe, and why a failed measurement is a state rather than an empty list.** | `partial`; `available` | mcp/src/agents_remember/application/review_source_inventory.py:1-30 |
| **The one observation both the review's inventory and the comparison's expansion read, with the two Git questions it asks.** | `tree_difference_observation`; `_RAW_ARGS`; `_NUMSTAT_ARGS` | mcp/src/agents_remember/application/review_source_inventory.py:87-88; mcp/src/agents_remember/application/review_source_inventory.py:87-87; mcp/src/agents_remember/application/review_source_inventory.py:194-236 |
| **The inventory value and the two honesty rules: the count is the list's own length, and a name that is not valid text is carried by its byte form in a measured, partial inventory.** | `review_inventory`; `is_text_path`; `byte_form`; `inventory_limitations` | mcp/src/agents_remember/application/review_source_inventory.py:179-191; mcp/src/agents_remember/application/review_source_inventory.py:239-249; mcp/src/agents_remember/application/review_source_inventory.py:252-261; mcp/src/agents_remember/application/review_source_inventory.py:429-469 |
| **The source pane: the inventory first and unconditionally, then the comparison's own attribution facts carried verbatim or stated as not measured.** | `source_pane` | mcp/src/agents_remember/application/review_source_inventory.py:560-613 |
| **The record renderer, and the one reason it is a module: two compositions render the same records, so one copy is what keeps an unassessed collection reading identically in both.** | `ReviewRecordInputs`; `refused`; `submission`; `evidence_pane`; `subject_states`; `signal`; `observation` | mcp/src/agents_remember/application/review_record_rendering.py:109-141; mcp/src/agents_remember/application/review_record_rendering.py:271-294; mcp/src/agents_remember/application/review_record_rendering.py:122-149; mcp/src/agents_remember/application/review_record_rendering.py:152-176; mcp/src/agents_remember/application/review_record_rendering.py:191-196; mcp/src/agents_remember/application/review_record_rendering.py:199-226; mcp/src/agents_remember/application/review_record_rendering.py:229-268; mcp/src/agents_remember/application/review_record_rendering.py:451-473; mcp/src/agents_remember/application/review_record_rendering.py:476-493|
| **The task-context entry: no comparison faked, the inventory rendered in all three states, the candidate re-checked before publication, and the reason it states — including an absent dataset half.** | `task_context_review`; `task_context_detail`; `_task_context_pane` | mcp/src/agents_remember/application/review_task_context.py:93-191; mcp/src/agents_remember/application/review_task_context.py:204-234; mcp/src/agents_remember/application/review_task_context.py:237-277; mcp/src/agents_remember/application/review_task_context.py:170-193 |
| **The composition that measures first and branches second, so no knowledge availability can remove a source change from the list.** | `compose_review`; `_open_dataset_pair`; `_review_matrix`; `_selector_kind_or_absence` | mcp/src/agents_remember/application/knowledge_review.py:334-574; mcp/src/agents_remember/application/knowledge_review.py:748-782; mcp/src/agents_remember/application/knowledge_review.py:785-827; mcp/src/agents_remember/application/knowledge_review.py:905-914; mcp/src/agents_remember/application/knowledge_review.py:866-875 |
| **The declaration of the inventory's own limit at the top level of the response.** | `_limitations`; `inventory_limitations` |mcp/src/agents_remember/application/knowledge_review.py:939-962; mcp/src/agents_remember/application/review_source_inventory.py:179-191|
| **The comparison's expansion seam is now a delegation, so this route has one implementation of "what did these two trees change".** | `git_tree_difference_probe`; `tree_difference_observation`; `_RAW_ARGS` | mcp/src/agents_remember/application/knowledge_diff.py:166-181; mcp/src/agents_remember/application/review_source_inventory.py:87-87; mcp/src/agents_remember/application/review_source_inventory.py:194-236 |
| **The cases that measure the route's new entry and the source half through the real composition and the real route.** | `test_a_task_context_review_lists_the_complete_source_inventory_with_no_knowledge_at_all`; `test_the_production_inventory_keeps_an_unusual_filename_as_the_address_it_expands_by`; `test_a_non_utf8_pathname_leaves_the_review_openable_and_states_why_it_is_partial` | mcp/tests/test_knowledge_review_source_endpoints.py:829-905; mcp/tests/test_knowledge_review_source_endpoints.py:908-949; mcp/tests/test_knowledge_review_source_endpoints.py:998-1055 |


## Update History
- 2026-09-21T15:43:00+02:00 — 260921-ICR-L2 curator, **the second sync's memory-side conflict in this document resolved as a union: the landed `260921-ICR-L19` section and this leaf's section both stand, and one range on the master line was corrected rather than merged.** Kept from the master line: L19's published-intent route section in full (the new `application/published_intent.py`, the declared publication location with its R20/R25 obligations, the memory-root rule with no fallback, the named-state discipline that keeps the attach additive, and its four reference rows), plus its history entry and its read-files range repairs (`read_files.py:62-62`, `_resolve_onboarding:235-267`). Kept from this leaf: the L2 section at the end of this narrative, its reference rows and its two history entries. **Corrected rather than merged:** L19's history entry records that `compose_review` "is declared at `knowledge_review.py:386-496`" — that was true of L19's own candidate, which did not carry this leaf's uncommitted rewrite; in the merged 888-line adapter `compose_review` is declared at **371-446** (and the refusal inside it at 460), so the L5 row that cites it was re-pointed and the correction is stated here rather than left in two wordings. No claim was dropped and none was invented; no verification stamp was advanced.
- 2026-09-21T15:17:00+02:00 — 260921-ICR-L2 curator, **the sync's memory-side conflict in this document resolved as a union, and four ranges on the master side corrected rather than merged.** Kept from the master line: L5's `unreadable_half_refusal` fact on the pair-preflight and entry-operation rows, its sibling-declaration citations, and its statement that the entry route refuses before the per-subject loop. Kept from this leaf: the L2 section at the end of this document, the inventory-first composition, and the re-derived ranges for everything this leaf moved. **Corrected rather than merged:** `read_knowledge_review` moved to `161-189` in the merged 888-line adapter; the shipped-comparison row's `knowledge_review.py:499-538` became `527-566` (and `diff_knowledge_scope` is cited where it lives, `knowledge_diff.py:176-230`); the review-matrix row now names the extracted `_review_matrix` at `497-524` beside `read_knowledge_view`; the two published half-names moved to the constants' single span `77-87` and the merged `__all__` `125-142`; and `review_namespace`/`missing_dataset_half` moved to `300-325`/`279-297`. No claim was dropped and none was invented.
- 2026-09-21T15:14+02:00 — 260921-ICR-L19 curator (uncommitted change set on `ar/260921-icr-l19`, code base `0fca5c69`): **route body updated; two enforced citation rows repaired; the document's two reopened claims re-read and recorded as stamp-class.** The section above is appended at the end of this route's change narrative, so no existing heading moved and no off-route card that cites this document by line needed repointing. It records this route's own impact for the leaf: the new `application/published_intent.py`, the three decisions it owns, the declared publication location with the write-side obligation named as ICR-R20@v1's, the memory-root rule with no fallback, and the named-state discipline that keeps the attach additive — plus that `application/knowledge_read.py` was deliberately **not** touched. **Range repairs (the checklist's two enforced rows, both in this document):** the read-files status row's two cells and the two prose `cit:` pointers on the same constructs were re-derived against the candidate rather than shifted — the `FileReadStatus` import to `read_files.py:62-62` (was `:52-52`) and `_resolve_onboarding` to `:235-267` (was `:218-218` / `:209-238`) — because this leaf's insertions moved those declarations; no claim wording changed. **The two reopened claims, re-read against the candidate and retained:** (a) `compose_review` is declared at `knowledge_review.py:386-496` and still states the one refusal (`unreadable_half_refusal` at `:396`), so the L5 row's wording and its ranges both hold as written; (b) `resolve_review_candidate` is declared at `review_candidate_resolution.py:130-194` and the recorded-base precondition it names still refuses by name at `:164-174` when the enclosure contract records no base. Both findings close only when this document's verification stamp advances past the commit that predates the sibling module — a closeout-owned stamp this uncommitted candidate cannot truthfully receive — so they are recorded here as **stamp-class leftovers**, not as repairs. No verification stamp was advanced and the entries still name the earlier candidates; the governed closeout owns the stamp. No commit was made.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, code base `702714fc`): **route body updated.** The section above is appended at the end of this route's change narrative, so no existing heading moved. It records this route's own impact for the leaf: three responsibilities extracted from the review adapter into `review_source_inventory.py`, `review_record_rendering.py` and `review_task_context.py` (the adapter 1113 → 863 lines, `__all__` unchanged, every moved name re-exported); the composition measuring the source inventory **first and unconditionally** so knowledge availability cannot remove a source change from the list; the selector-less request answered as the task context with `comparison=None`, `not_compared` and the `task_context` selection state; the inventory's own limit declared at the top level; and the comparison's expansion seam reduced to a delegation so the route has **one** Git observation. Eleven reference rows below cite this leaf's changed files; the mechanical pass and this curator pass re-derived them against the candidate, and three rows of the L1 section above were re-pointed at the same time. **No verification stamp was advanced** — the candidate is uncommitted and closeout owns the real stamp.

## 260921-ICR-L10 The Page Arithmetic Gets Its Own Module, And The Adapter Offers A Cursor To The Collection It Names

`260921-ICR-L10` (`ICR-R10@v1`) carries the two bounded collections' existing snapshot-bound cursors
through review composition. The new module on this route is `review_pagination.py`: the page arithmetic
and the reset mapping, beside the review adapter rather than inside it. **It mints no cursor and
re-derives no binding** — the continuation a page publishes is the owner's own opaque token, the
comparison's `knowledge-diff-cursor/v1` for the knowledge collection and the view's snapshot-bound
continuation for the records one — and it reads `total`/`returned`/`remaining` off the owners'
`KnowledgeDiffCounts` and `ViewCounts` rather than subtracting two of them to invent the third.

The adapter (`knowledge_review.py`) grew the wiring and stays a delegator: a request's cursor is offered
to the collection it names, the comparison and the matrix are read at that position, and the one page the
request named is published beside the panes — with the refusal it earned when a requested page could not
be served. Two refactors came with it and a reader should know they are renames rather than new
behavior: `_rows_remaining` is now `_matrix_rows_remaining` (it takes the matrix's own selection rather
than a bare view result), and the task-context branch of the selection channels is now the extracted
`without_selected_matrix`, one implementation of "this review read no matrix".

`review_evidence_records.py` gained `MatrixSelection` — the published page, the owner's own remainder
and any refusal — so a stated remainder always names the action that reaches it, and a refused read is
reported `unavailable` rather than as a measured zero. The one distinction the fix rounds turned into
code: only the owners' binding-mismatch code is a moved generation and earns the new-generation action;
everything else is `comparison_page_unreadable` with the owner's own remedy, and the two directions are
told apart by asking the owner's own decoder rather than by reading refusal text.

## Update History
- 2026-09-23T00:20:00+02:00 — 260921-ICR-L10 curator (candidate `ar/260921-icr-l10`, uncommitted; base `dcf35a0e0fc06bccdafd22390b7588b0aea811bc`): **route body updated.** **the page arithmetic gets its own module, and the adapter offers a cursor to the collection it names.** New `review_pagination.py` owns how a page is stated and the reset mapping, mints no cursor and re-derives no binding; `knowledge_review.py` gained the wiring (with `_rows_remaining` renamed to `_matrix_rows_remaining` and the task-context branch extracted as `without_selected_matrix`); `review_evidence_records.py` gained `MatrixSelection` so a stated remainder always names the action that reaches it and a refused read is `unavailable` rather than a measured zero; `review_task_context.py` calls the extracted branch. Only the owners' binding-mismatch code counts as a moved generation. Existing rows that cited these files were re-derived against this candidate. No verification stamp was advanced: nothing in this leaf is committed, so the merge/commit stamp is closeout's.
## 260921-ICR-L26 Two Owners For Record Applicability, And An Adapter That Classifies Once

`260921-ICR-L26` (`ICR-R26@v1`, subject and comparison isolation) is the leaf that closes F09 on this
route: the review adapter used to hand the candidate-wide review matrix and every supplied assessment to
the selected subject's panes, so a valid assessment of a **sibling** invariant appeared in both panes of
a different invariant. Complete delivery (`ICR-R14@v1`) and correct attribution are separately
falsifiable, and this leaf is the attribution half. The route gained **two** purpose-named owners and the
adapter gained one call:

- `application/review_recorded_selection.py` (617 L) — **the recorded population one selection reaches**:
  the selected subject (through ICR-R07's own narrowing, so a revision seed resolves the identity its
  union item carries), the revisions the selection **records** for it, the identities its recorded
  relationship rows reach with the spelling that reached each, and ICR-R07's own **page-bound** retained
  list kept deliberately separate from the recorded revisions. It reads the page-independent half from
  the two snapshots' own owners and merges it **under** the comparison's page facts, so the recorded
  population only ever grows past what the page showed.
- `application/review_record_applicability.py` (1101 L) — **which supplied record may be displayed
  beside that subject, and why**: one projection, six treatments (`direct`, `historical`, `context`,
  `candidate`, `unresolved`, `unrelated`) decided from the record's own recorded bindings, the
  comparison generation and the recorded relationship paths, plus the six-way count of every supplied
  collection. A record of another subject is either a labelled context row — true subject, recorded
  relationship, the record's **kind**, author and role, and none of its finding — or it is counted
  `unrelated` and not handed to a pane at all.

**The ruling this route implements: a page decides what is displayed, never what a record means.** The
classification reads the selection, not `page.items`; at page sizes default/32/8/4/3/2/1 the treatments,
the context signature and the summaries are identical, and exactly the one genuinely unreachable subject
is counted `unrelated` at every size. A malformed binding — a record carrying an identity where a
revision belongs, or a revision of another identity — is `unresolved` with its references, never matched
against the selection's revisions; a `direct` sentence cites ICR-R07's published retained list **only**
when that page-bound list really carries the matched revisions.

**What moved, and why the adapter did not grow.** `knowledge_review.py` is 1034 → 1036 lines: it calls
`review_applicability(...)` once before either pane, hands both panes
`applicability.displayed_rows(rows)`, reads the pane's selection from the projection rather than taking
it twice, and **loses** `_authored_effect`/`_unresolved_author` to
`review_record_rendering.py` (311 → 473), which is now the surface's labelled renderer and declares the
`ReviewApplicabilityProjection` port so the dependency stays one-way.
`review_evidence_records.py` is 840 → 862: the R14 bundle gains **exactly one** field, the claim's own
recorded subject revision (`_claim_subject_revision`, invariant-revision subjects only — a facet subject
is reported as the absence it is). `review_task_context.py` is 376 → 390: a review that selected no
subject labels every supplied record `candidate`, the one label that claims neither a subject nor a
failed resolution.

**Boundaries recorded, not closed.** ICR-R15 measures dependency currentness separately (a
knowledge-only generation move leaves a record `direct`, because only the code tree is comparable on a
record — the remedy is R11's published knowledge-generation identity or R15's own measurement); a
deep second-order family hop belongs to `ICR-R31@v1`; browser A14/A15 acceptance belongs to
`ICR-R25@v1`; and the classification costs one extra read-only pass over the two snapshots per
selected-subject review.

## Update History
- 2026-09-23T02:45:00+02:00 — 260921-ICR-L26 curator (candidate `ar/260921-icr-l26`, uncommitted; production line at this leaf's base `2edad477bcd9127a90e4618d345ce34ef7e6a6d9`, confirmed from the enclosure contract): **route body updated for record applicability (`ICR-R26@v1`).** The section above records the two new owners and what each answers, the page-versus-selection ruling and its measured consequence, the malformed-binding rule, the `direct` label's honest basis, the adapter's +2 lines with the two renderers moved out, the one field the R14 bundle gained, and the four boundaries routed to other leaves. **Citation accounting:** every row on this overview that cited `knowledge_review.py`, `review_record_rendering.py`, `review_evidence_records.py` and `review_task_context.py` by line was re-derived against this candidate, because this leaf moved them; the enforced rows are recorded in each file's own card. **Stamp accounting:** no verification stamp was advanced — the header already names the leaf's base as the production line the reading was taken against, and nothing in this leaf is committed, so the governed closeout owns the real stamp.
## 260921-ICR-L12 The Committed Or Closed Leaf Reopens Its Recorded Comparison

`260921-ICR-L12` (`ICR-R12@v1`) adds **one** owner to this route and changes one landed
responsibility inside it. The owner is
[`review_committed_leaf.py`](review_committed_leaf.py.md) (687 L): the resolution of a committed or
closed leaf's code-and-intent comparison from the records the task kept, reached only through
`review_candidate_resolution.resolve_review_candidate`'s closed-enclosure branch. A published
comparison generation is the authority for the comparison it froze — its two retained snapshots, its
two recorded code objects, read in the repository the record names — and a leaf that published none
exposes its **recorded source range** through R01's own `recorded_committed_range` while stating, as a
typed absence, that no intent generation was ever recorded for it.

**What the landed responsibility changed.** `resolve_review_candidate` gained `recorded=` and no longer
answers `candidate_not_live` for a closed enclosure: that code now names only the state in which
nothing is live **and** nothing is recorded, and a recorded endpoint the repository cannot resolve
answers `candidate_unresolved` instead. The live candidate root now names the **repository** that holds
the object rather than the disposable checkout, which is what makes a reopened comparison reproduce the
live one byte for byte. `_leaf_contract` is public as `recorded_leaf_contract`, because two resolutions
must read the same enclosure. `ReviewCandidateResolution` carries the `closed_leaf` record that names
which record answered.

**What the composition gained.** `knowledge_review.py` (1036 → 1077 L) delegates `recorded=` on both
resolutions, asks a closed leaf's pair refusal before the shipped one, and publishes the record's own
declared facts as top-level `history:` tokens; `review_task_context.py` states the record's own intent
absence in its detail sentence; `review_evidence_records.py` reads the records of the record the request
named; `models/knowledge/review.py` (1189 L, under its rail) gained `ReviewHistoryRef` and the request
field; `serving/review.py` admits the one historical spelling and refuses every other in its own 400
vocabulary. **A declared absence and unavailable content are never worded as each other** — the
partition reads R11's own `TYPED_ABSENCE_STATES` — and nothing falls back to the current branch tip,
`HEAD` or today's knowledge.

**Boundaries recorded, not closed.** `ICR-R24@v1` owns the leaf-history drill-down navigation (this
leaf provides the addressable target only), `ICR-R17@v1` owns live refresh, and `ICR-R25@v1` owns the
assembled A17/A23 browser acceptance. The one suppression this leaf adds is the local import's
`# noqa: PLC0415 - cycle` in the resolution module; no limit and no rail was widened.

## Update History
- 2026-09-23T04:31:21+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): **route body updated for historical committed-leaf review (ICR-R12@v1).** The section above records
the one new owner and both of its paths, the landed resolution change (a closed enclosure resolves from
its records; the live candidate root is the repository that holds the object), the adapter's delegating
growth, the declared-limit vocabulary, the three boundaries routed to other leaves, and the single
suppression this leaf adds. **Citation accounting:** every row on this overview that cited
`knowledge_review.py`, `review_candidate_resolution.py`, `review_task_context.py`,
`review_evidence_records.py` and `models/knowledge/review.py` by line was re-derived against this
candidate, because this leaf moved them. **Stamp accounting:** no verification stamp was advanced — the
header already names this leaf's base as the production line the reading was taken against, and nothing
in this leaf is committed, so the governed closeout owns the real stamp.

## 260921-ICR-L17 The Comparison's Identity And Its Staleness Get Their Own Owner

`260921-ICR-L17` (`ICR-R17@v1`) adds **one module** to this route and takes two private helpers out of
the adapter.

- **The new owner.** [`application/review_comparison_staleness.py`](review_comparison_staleness.py.md)
  is the seventh purpose-named owner this route has extracted from `knowledge_review.py`. It carries the
  comparison's own declared identity (`comparison_identity`) and the staleness that identity earns
  against a *previous* binding a refresh read supplies (`review_staleness`). It hashes nothing, resolves
  nothing and re-derives nothing: the digest an assessment was bound against is the one the comparison
  owner published.
- **What the adapter lost.** `knowledge_review.py` is **1077 → 1041 lines**; its private
  `_comparison_identity` and `_staleness` are **deleted, not annotated**, because nothing under `mcp/`
  imported them — so `__all__` is unchanged and no importer had to learn a new home. `compose_review`
  now calls the sibling's two names, computes the identity **once**, and reads the state once for both
  the published `staleness` value and the submission state, so the two cannot disagree about the same
  comparison.
- **The previous identity moved onto the request.** `read_knowledge_review` and `compose_review` lost
  their `previous_binding_digest` keyword; the value travels on
  `ReviewSurfaceRequest.previous_binding_digest`, admitted by `serving/review.py` and supplied by the
  client's refresh control.
- **One prose fact a reader should carry.** The adapter's docstring paragraph that names the extracted
  owners was advanced from "Five more responsibilities" to "Six more responsibilities" by this leaf,
  while it names **seven** modules — it already named six under a heading of "Five" before this leaf, so
  the count is one behind its own list and this leaf's addition did not close the gap.


## Update History
- 2026-09-23T06:50:00+02:00 — 260921-ICR-L17 curator (candidate `ar/260921-icr-l17`, uncommitted; production line at this leaf's base `c422dc00273d4ae7a5d8c9c8db97365b8c85d640`, confirmed from the enclosure contract): **this route gained one module and the review adapter lost its two staleness helpers (`ICR-R17@v1`).** `application/review_comparison_staleness.py` owns the comparison's declared identity and the staleness it earns against a carried previous binding; `knowledge_review.py` is 1077 → 1041 lines with `_comparison_identity` and `_staleness` deleted rather than aliased, and the previous identity now travels on the request instead of as a keyword. **Citation accounting:** the rows into the adapter were re-derived from each construct's own declaration on the 1041-line candidate — `_knowledge_pane` `:931`, `select_subject_revisions` (called at `:471`, declared in `review_revision_comparison.py`). **Stamp accounting:** the verification pair names this leaf's base; closeout owns the stamp.

## 260921-ICR-L22 The Sync Rebinds The Review: Two Owners, And The Read That Renders What It Measured

`260921-ICR-L22` (`ICR-R22@v1`, managed Git recovery rebinding) is the leaf that closes F6's
non-conforming example on this route — *the old review stays current while its scratch datasets lag the
merged memory line*. A managed sync carries both of the review's inputs onto the official line, and until
this leaf neither the sync's own journal nor the reopen channel made the **live** review read say so. The
route gains **two** purpose-named owners, and the adapter gains one call:

- `application/review_sync_rebinding.py` (**733 L**) — **the durable rebinding record and its readers**:
  one file per (leaf, generation) under the task's own reports root, written by
  `record_review_sync_rebinding` (`:271`) from values owners produced (the generation store's own
  selection, the shipped `capture_future_code_candidate`, and the ordinary publication route at the
  declared location), read by `read_review_sync_rebinding` (`:376`), checked against the generation by
  `rebinding_names_the_generation` (`:441`), listed by `read_review_sync_rebindings` (`:479`) and
  reclaimed by `discard_review_sync_rebindings` (`:505`), with `rebinding_file_name` (`:265`) naming the
  location and `ReviewSyncRebindingRead` (`:242`) carrying the three-valued read
  (`recorded` / `not-recorded` / `unreadable`). It measures owners' values and re-implements none of them,
  and **nothing in it can refuse a sync**.
- `application/review_sync_movement.py` (**334 L**) — **the read half**: `review_sync_movement` (`:87`)
  answers what the leaf's own syncs measured against the generation the live read selected, or `None` when
  there is no measurement *of that generation* — a located record that describes another one is reported
  as the absence it is rather than as the movement it claims — and
  `review_staleness_with_sync_movement` (`:309-334`) folds a measured movement into the staleness the
  payload publishes. **The movement outranks the reader's carried identity**, because it is the stronger
  fact: R17's `current` would otherwise let the moved review keep reading as untouched, which is the
  packet's own non-conforming example, and the submission state follows automatically because the payload
  refuses a `stale` comparison for submission.

**What moved, and what the adapter lost.** `knowledge_review.py` is **1041 → 1054 lines**: it imports the
two names at `:143-146`, reads the measurement once at `:475`
(`sync_movement = review_sync_movement(resolved)`), folds it into the staleness it already published at
`:476-478`, and passes the value to the payload at `:537`. Nothing was deleted from the adapter and no
seam moved; the value's own field, vocabulary and validator live on the models route
(`sync_movement: ReviewSyncMovement | None` on the payload), which is where the state a `stale` movement
carries is refused if it disagrees with what was measured.
`application/worktree_tools.py` is **1030 → 1035 lines**: the `worktree_sync` tool imports the attachment
at `:14` and now returns it at `:371-375` (`rebinding_result_block(configured.contract, payload)`), which
is deliberately *after* the transaction has finished its Git work and written its contract — the
rebinding measures what the sync resolved and never participates in the transaction's admission, so a
sync that cannot be measured is returned unchanged, carrying the reason.

**The reopen channel gained a fifth kind.** `application/review_comparison_reopen.py` is
**730 → 778 lines**: `ComparisonReopen.sync_rebinding` (`:202`) carries what this leaf's own managed syncs
measured against the generation the reopen resolved, populated at `:360` inside `_read_and_measure`
(`:308`) through the new private `_measured_rebinding` (`:367`), which re-checks a located record against
the generation and reports `not-recorded` with the reason when the record's own recorded identities are
not that generation's. It is **one value rather than a tuple** because a rebinding measures one generation
and a later sync replaces it — one file per (leaf, generation) — while the generations themselves are
retained history; and it is `not-recorded` rather than `None` when a generation *was* measured and no sync
reported against it, because "no managed sync has run" and "a sync ran and recorded nothing" must not read
as the same answer.

**What this route deliberately does not do.** The record changes no dataset, publishes no successor
generation and grants no clearance: the remedy it names is the successor that
`application/review_comparison_freeze.freeze_review_comparison` freezes with the judged generation as its
`parent`, so supersession is a lineage a reader resolves rather than a claim the record makes. Nothing here
re-runs a comparison, and nothing here is a review authority beside the shipped one.

## Update History
- 2026-09-23T20:30:00+02:00 — 260921-ICR-L23 curator (memory worktree only; no code changed, no commits; leaf base `473ad8242bb4c22bdabed5d5253767350381eb3e` plus the working-tree delta): **four route-level reference rows were re-anchored, and the route's governed sources gained the raw-Git boundary.** `knowledge_review.py` folds the new `external_git_movement` reading into the staleness it publishes, `review_sync_movement.py` owns the fold, `review_task_context.py` measures the boundary on the task-context entry too, `worktree_tools.py` attaches the statement to the closeout and integration results, and `review_external_git_movement.py` is this leaf's new module. The repaired rows are `select_subject_revisions` (`501`), the two side values import-and-call sites (`146-148`, `1037-1040`), `_selector_kind_or_absence` (`903-912`) and the CLI case (`1892-2006`). **No verification stamp was advanced**: the candidate is uncommitted, so no commit holds the content a stamp would claim to have verified, and the governed closeout owns the real code and memory commits.
- 2026-09-23T17:15:00+02:00 — 260921-ICR-L22 curator (uncommitted change set on `ar/260921-icr-l22`, base `e605822eb3bf83bf63a45963c5f51d5fc28859ee):` **route body updated for managed-sync rebinding (`ICR-R22@v1`).** The section above records the two new owners and what each answers, the measurement-versus-absence rules the read keeps, the adapter's measured **+13** lines with the read at `:475`, the fold at `:476-478` and the payload value at `:537`, the sync tool's attachment at `:371-375` after the transaction has completed, and the reopen's fifth channel at `:202` with its generation check at `:367`. **Citation accounting:** every range in the section above was measured on this candidate; rows already on this overview that cite `knowledge_review.py`, `worktree_tools.py` or `review_comparison_reopen.py` by line were **not** touched, because the curator repairs citation ranges separately, per row — this leaf moved all three modules' lines, so those rows read lower than they did. **Stamp accounting:** no verification stamp was advanced — the header's verification pair names this leaf's recorded base `e605822e` because nothing in this leaf is committed, and the governed closeout owns the real stamp.

## 260921-ICR-L31 The Comparison-Bound Family Review Context

The existing family-context composition discovers direct family identities through the invariant read policy, then resolves each independently on both bound snapshots through the family owner and authored head rule. Primary membership absence cannot erase a known family’s counterpart or pin it to a retained historical predecessor. Explicit family revisions remain exact, memberless competing heads remain ambiguous, and genuinely absent/unreadable scope remains distinct.

The roster owner still reads each selected family revision’s own guarantee, exact memberships and bounded content/claims. Continuation advances its existing comparison/subject-bound walk; a complete final page need not carry the whole roster. No extra family is discovered through sibling rosters. Primary invariant operands, evidence and complete source inventory remain independently composed by their existing owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| Direct policy discovery is separated from independent family composition. | `_applicable_invariant` | mcp/src/agents_remember/application/review_family_context.py:545-566 |
| Both family sides use the existing family/head/roster owners. | `_entry` | mcp/src/agents_remember/application/review_family_context.py:572-635 |
| Ambiguity remains explicit rather than selecting a membership-bearing head. | `_selection` | mcp/src/agents_remember/application/review_family_context.py:677-722 |

## Update History

- 2026-09-27T02:21:35Z — L40: Updated the current R31 route account for independent family context; no schema, store, traversal or writer authority changed. Prior route history and verification stamps remain unchanged.


- 2026-09-24T09:20+02:00 — 260921-ICR-L29 curator (uncommitted change set on `ar/260921-icr-l29-ar`,
  base `0d7910f9d646161c414ed6543453536a3c749d49`): **route body updated for the taskless knowledge
  bootstrap (`ICR-R29@v1`).** This route gained **five purpose-named owners** and the ingest operation
  it already carried was rebound from a document to a value. The section below is **appended at the end
  of this document's change narrative rather than inserted at its head**, so that no existing heading
  and no reference range on any card that cites this overview by line moved; that is a deliberate
  choice, and this entry is the history record for it. **Citation accounting:** the five new owners'
  cards cite their own declarations at this candidate's lines; no existing row on this overview was
  re-pointed, re-worded or deleted. **Stamp accounting: no verification stamp was advanced** — the
  candidate is uncommitted, so no commit holds the content a stamp would claim to have verified, and
  the governed closeout owns the real code and memory commits.
- 2026-09-24T02:20:00+02:00 — 260921-ICR-L31 curator, **reopened enclosure** (`260921-icr-l31b`, same base `fdf3e4b6cfe73040d35cbfd4d8b93fd55369e499`): **route body updated for the corrected roster-completion semantics.** The paragraph above records what the reopen changed in this route's governed source — ``_roster_detail`` states the completed case in two forms because ``complete`` is the walk's flag, so a roster read in one page is the roster whole while a walk whose final page is a continuation says that instead — and what it deliberately left alone: the read, the composition, the cursor handling, the refusals and the seal-verifying guarantee path. The route's own L31 section was **re-measured, not merely re-stamped**: the roster read's ranges moved by this delta's +12-line insertion and the cross-file page value's by the model module's insertions, and the section above names the corrected semantics rather than the pre-correction ones. **No route impact was claimed as absent and no no-route-impact judgment was published** — this is real body content, and the memory-refresh attestation this route carried for a changed governed source is answered by it. **Stamp accounting: no verification stamp was advanced.** The header's verification pair still names this leaf's recorded base ``fdf3e4b6``, because the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-23T22:20:00+02:00 — 260921-ICR-L31 curator (uncommitted change set on `ar/260921-icr-l31`, base `4c000b11c5243e4a8e77c08e87984fff00c1d94b`): route body updated for the comparison-bound family review context (`ICR-R31@v1`) — the new composition and roster-read owners under this route, and the two thin callers that carry the value. Citation rows that this leaf's insertions moved were re-anchored to the declarations they name. No route impact was claimed as absent: the section above states what changed in the governed source and in this document.


## 260921-ICR-L29 The Write Plane Is Bound To An Admission, And A Repository With No Task Can Be Bootstrapped

`260921-ICR-L29` (`ICR-R29@v1`, knowledge bootstrap initialization publication and recovery) closes the
gap the packet states exactly: *the normal memory initializer never creates knowledge storage, while the
existing curator-list entry is enclosed-task-shaped; the first-write helper alone is not a taskless
bootstrap path.* Fabricating a development enclosure to satisfy that shape is refused by the bootstrap
handover, and a second write path is the parallel-store defect the preservation boundaries name — so the
delivery is **a second real admission, not a second write path.**

| Owner | What it answers | Size |
| --- | --- | --- |
| `knowledge_write_admission.py` | The facts one admitted write is bound to, and the enclosure adapter that derives them from a contract | 184 L |
| `knowledge_bootstrap_admission.py` | The taskless admission: real setup authority → the ordinary read route's context → the two exact checkouts' revisions | 435 L |
| `knowledge_bootstrap.py` | One bootstrap run: what it forks from, what is published back, and what remains (including the owed work carried forward) | 577 L |
| `knowledge_bootstrap_staging.py` | The staging's retained progress record, the reader that reconstructs it, and its bounded cleanup owner | 530 L |
| `knowledge_dataset_contents.py` | Which invariant revisions a dataset file holds, four-valued so absence is a measurement or an admission of ignorance | 207 L |

**One operation, two admissions.** `ingest_curator_list`'s first parameter is now a
`KnowledgeWriteAdmission` — coerced once by `as_write_admission`, which passes an existing admission
through untouched — and `load_contract` left the operation entirely. Every downstream owner is
unchanged: namespace, identity allocation, candidate, first generation, batch, snapshot and publication
are the shipped implementations, which is what makes "reuse the owners" a fact about the call graph
rather than a claim in a report.

**Provenance is a value, never a boolean.** `AdmissionProvenance` names the authority kind
(`leaf-enclosure` or `repository-bootstrap`), the exact document it was read from and the fact that made
it an admission. There is no `admitted=True` anywhere on the path: a caller cannot assert an admission,
it can only be handed one a resolver built after its own checks. The bootstrap resolver reads the
repository entry from the MCP settings document, resolves the coordination context with **no enclosure
selector** (so the memory layer is the repository's, not a task's worktree), requires the declared and
resolved memory roots to be equal, and reads both revisions from the real checkouts — a checkout that
cannot answer is a named refusal, never an empty revision.

**Three distinctions the memory of this route now keeps, because each one is a false sentence waiting to
happen.** A location with **no dataset file at all** is a *measured* absence, which is not the same fact
as a file that could not be read (`unavailable`); a walk that stopped (a page cap, a refusal) did **not**
establish absence for what it had not reached, so the report's `remaining` list and its `unmeasured` list
stay two fields rather than one longer list; and a run whose batch committed but whose publication was
refused writes a retained record that **says so**, instead of borrowing the success of the write half.
A fourth was added by the fix round and it is the one a resume depends on: the retained record's owed
entries are **carried into the next run's record and re-derived against that run's own store read**
(`outcome` `carried`), so a curator who narrows the hand-over list cannot delete the rest of the debt and
an entry the repository has since received stops being owed. The file is therefore read for two reasons —
to detect that it describes another operation, and to carry forward what it still owes — and the record
is written by **any committed run**, including one whose batch wrote nothing, because a record left
standing is how the owed work goes stale exactly when the candidate binding moved.
Exit status is never a publication claim: the report carries the destination read before the run, the
batch's own state, the publication owner's result, an independent read-back through the read route's own
owner, and the named remaining work.

**The taskless destination is derived, not accepted.** `--repo` names the repository and nothing on the
bootstrap CLI's surface can aim the destination elsewhere: it is `published_dataset_path(context)`, the
read route's own owner, so the writer and a later task's planner cannot disagree about where a
repository's knowledge lives. The staging root is derived from the resolved context's own temp root, and
its cleanup owner is the one irreversible act on this path, guarded by two reads rather than by an
inference about whether the run "finished".

## Sparse family member projection

The existing review_family_rosters owner resolves recorded membership only for exact revision IDs represented by the bounded page's content, membership or claim items. Sparse updates keep their claims reachable even when the membership row arrived elsewhere. The selected-content boundary, family guarantee owner, traversal policy, page limits and snapshot-bound cursors stay unchanged. A completed page completes the walk; it does not assert that the page alone contains all context.

## Assessment inputs retained with their comparison

The ordinary comparison producer collects R14 inputs for its already resolved pair and validates positive curator inputs, reserved pins and exact channel provenance before retention. review_curator_records supplies live authority records for live reads and only the bound immutable generation for history. Optional captured availability distinguishes measured-empty, unavailable and uncaptured history without changing old seals. Explicit review_comparison_recovery selects an exact parent and original curator digest; retention validates recorded source capture and exact snapshot identities without creating a live candidate or altering older generations.

## 260921-ICR-L47 The Changed-Intent Summary And The Shared Pair Preflight

**Route meaning extended (`ICR-R24@v3`).** The review composition gains a fourth read, answered before
the reviewer is opened: [`review_intent_summary.py`](review_intent_summary.py.md) counts, over the
reviewer's own resolution, the invariant and family (joint-guarantee) **head revisions** only the after
side holds (`+`) and only the before side holds (`−`), using `review_revision_comparison.revision_heads`
as the one head rule. A revised statement counts once on each side; every successor counts (a record-only
successor too, per the leaf ruling of 2026-09-28T16:15:11+02:00 on F3), except a same-content successor
whose realizations or members moved, which is carried as the typed `realization_only`/`membership_only`
count. Divergent heads make the answer `partial`; an unreadable pair is `unavailable` with its refusal and
no counts — never `+0 −0`. The count semantics are the master decision labelled 12:00 (clock-corrected by
the 12:10:21 entry) in `task.json`.

The catalogue and the summary refuse a pair by **one rule in one order**:
[`review_pair_preflight.py`](review_pair_preflight.py.md) (closed-leaf record absence, absent half,
unreadable half, unreadable receipt), extracted from `knowledge_review.list_knowledge_review_entries`
unchanged. The summary is wired as its own port by the composition root and served by
`serving/review_summary.py`.

**Known, routed.** The summary issues one revision-id query per identity per side; a grouped query would
make it constant (review R2 observation O-R2-3, a candidate for a later performance leaf). Not settled
behaviour to preserve.

| Finding | Anchor | Source |
| --- | --- | --- |
| The summary: preflight, both sides read, classification. | `intent_summary_of`; `_classify` | mcp/src/agents_remember/application/review_intent_summary.py:145-175; mcp/src/agents_remember/application/review_intent_summary.py:347-377 |
| The shared preflight in its fixed order. | `pair_preflight_refusal` | mcp/src/agents_remember/application/review_pair_preflight.py:34-42 |
| The catalogue caller delegating to it. | `list_knowledge_review_entries`; `pair_preflight_refusal` | mcp/src/agents_remember/application/knowledge_review.py:256-317 |

## 260928-MIK-L22 The Default Worktree Services Bind The Knowledge Validator

**Route meaning extended (MIK-R22@v1).** The default composition
[`worktree_services.py`](worktree_services.py.md) now binds one more adapter:
`knowledge_validation=GitKnowledgeValidation()`, from `memory_quality.knowledge_validator.commit_route`.
It implements `worktrees.services.KnowledgeValidationPort`, the port through which the worktree layer's
memory commit routes reach the mandatory knowledge validator without importing `memory_quality`. This
composition root is the only place it is bound; a process whose bundle lacks it refuses a converted memory
commit instead of skipping validation. Before MIK-R37 no production memory tree is converted, so binding
it changes no behaviour today.

| Finding | Anchor | Source |
| --- | --- | --- |
| The default bundle binds the knowledge validator. | `build_default_worktree_services`; `GitKnowledgeValidation` | mcp/src/agents_remember/application/worktree_services.py:210-222; mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py:31-80 |
| The port it satisfies. | `KnowledgeValidationPort` | mcp/src/agents_remember/worktrees/services.py:132-148 |

## 260928-MIK-L23 The Published-Memory Selection Selects A Converted Tree

**Route meaning extended (MIK-R23@v1).** [`published_intent.py`](published_intent.py.md) now also selects a
converted memory tree as a tree. When the memory root holds `knowledge/layout.json`,
`resolve_published_memory_tree` selects the derived index of that tree's current state (built or reused
under the coordination runtime by `memory/knowledge_index/`), and `published_intent_block` tries it before the
database selection; the block then names the tree (`memoryTree`) and every page its `indexState`, and a
partial index forces `enumerationComplete` to `false`. `select_knowledge_dataset` is the same resolution for
any caller-selected path: a converted tree's root or its published `knowledge.sqlite` location resolves to
the index, and any other path is returned unchanged — which is what the mounted `knowledge_read`,
`knowledge_diff` and `knowledge_project` tools now call. An unconverted memory root keeps the database
selection exactly as before, and the write side's `resolve_published_intent` is unchanged, so no writer
reaches the index.

| Finding | Anchor | Source |
| --- | --- | --- |
| The converted-tree selection for the ordinary read, tried first. | `resolve_published_memory_tree`; `published_intent_block` | mcp/src/agents_remember/application/published_intent.py:329-354; mcp/src/agents_remember/application/published_intent.py:464-479 |
| The one dataset resolution every knowledge read applies. | `select_knowledge_dataset`; `converted_memory_tree` | mcp/src/agents_remember/application/published_intent.py:365-378; mcp/src/agents_remember/application/published_intent.py:381-400 |
| A page from a partial index is never presented as complete. | `_bind_index_state` | mcp/src/agents_remember/application/published_intent.py:578-592 |

## 260928-MIK-L12 The Curator Writer For All Knowledge Kinds, As Files

`knowledge_writer/` is a new subpackage governed by this route overview (no overview of its own, following the
L22, L23 and L20 precedent for new subpackages). Its one operation is
[`write_knowledge(WriteRequest) -> WriteReport`](knowledge_writer/writer.py.md) (MIK-R12@v2):

- [`handoff.py`](knowledge_writer/handoff.py.md) reads the document — the producer's list, or `{entries, records,
  history}` — collecting every shape problem; the producer's thirteen fields are unchanged and every new key is
  the curator's. An entry that names no record is refused, never dropped.
- [`code_anchors.py`](knowledge_writer/code_anchors.py.md) captures the code candidate C (committed and
  uncommitted) and resolves `symbol` (exactly one binding), `line_range` and `file` locators into anchors with
  `blob` and `content`.
- [`memory_state.py`](knowledge_writer/memory_state.py.md) holds the memory tree's bytes, the operation's edited
  documents and the base (the memory worktree's `HEAD`), and does the atomic per-file write.
- [`authoring.py`](knowledge_writer/authoring.py.md) fills the mechanical fields: IDs minted or reused on a rerun
  from `origin.handoffEntry`, revisions once per leaf against the base (`admission`, `status` and `origin` are
  not meaning), origin with the evidence, realization and proof entries, and history rows with `before`/`after`
  covers written into the entries. Evidence for another leaf's record goes into this leaf's history row about it
  and never into that record's origin; without the row the run is refused.
- [`history_check.py`](knowledge_writer/history_check.py.md) checks every row of the owner's history file against
  the result with L07's checks; a contradicted row refuses the run.
- [`writer.py`](knowledge_writer/writer.py.md) renders canonically, runs the knowledge validator over the whole
  resulting tree, reports the MIK-R04 `writer_reports` rules instead of refusing them (every commit route still
  refuses them), and writes only when nothing refuses and `--commit` was given.
- [`report.py`](knowledge_writer/report.py.md) is the product: every record, entry, row and evidence outcome,
  or every problem and violation.

The writer writes converted memory trees only. By architect ruling the database modules on this route
(`knowledge_ingest.py`, `knowledge_curator_ingest.py`, `knowledge_bootstrap*.py`) are unchanged and remain the
production path for unconverted memory until MIK-R26 (leaf L26) retires them.

| Finding | Anchor | Source |
| --- | --- | --- |
| The operation: read, author, check history, render, validate, then write or refuse. | `write_knowledge` | mcp/src/agents_remember/application/knowledge_writer/writer.py:98-155 |
| Route rules are reports inside the writer only. | `_writer_split` | mcp/src/agents_remember/application/knowledge_writer/writer.py:176-191 |
| Another owner's origin is kept exactly; its evidence is queued for this owner's history row. | `_origin` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:248-283 |
| Every row of the owner's history file is checked against the candidate. | `owner_history_problems` | mcp/src/agents_remember/application/knowledge_writer/history_check.py:49-72 |


## 260928-MIK-L24 The Read Tool Switches On The Memory Format, And The Composition Binds The Crossing

**Route meaning extended (MIK-R24@v1 rules 5, 7, 8 and 9).** One new module and five touched ones on this
route:

- [`read_files_format.py`](read_files_format.py.md) (new) decides what `read_ar_files` returns beside a card.
  A converted tree (`knowledge/layout.json`) gives `format: text/v2`, the sidecar and resolved references.
  An unconverted tree gives `format: legacy-format` and a `legacy-format` knowledge section naming both
  conversion routes. [`read_files.py`](read_files.py.md) calls it. **Legacy-format reads are active in
  this build (architect ruling)**, so the database publication is no longer served through `read_ar_files`
  on an unconverted tree. The ICR-R19 route cases now measure that block directly, and the taskless
  knowledge tools are unchanged.
- [`memory_tools.py`](memory_tools.py.md) routes `citation_check` and `citation_fix` on a converted tree to
  `memory_quality/reference_state` (stale references are report-only; only mechanical moves are fixed).
- [`memory_quality/controller.py`](memory_quality/controller.py.md) refuses a contract-scoped run on an
  unconverted leaf tree whose official line is converted. That refusal is **inert until the official line
  is converted** (architect ruling).
- [`worktree_services.py`](worktree_services.py.md) binds `GitKnowledgeValidation(base_converter=GitBaseConverter())`
  (rule 7) and `knowledge_crossing=GitKnowledgeCrossing()` (rule 8). Both are inert for a merge in which no
  tree is converted.
- [`knowledge_writer/code_anchors.py`](knowledge_writer/code_anchors.py.md) now binds symbols through the
  shared `extents.qualified_spans`, with behaviour unchanged.

| Finding | Anchor | Source |
| --- | --- | --- |
| The format switch in the read tool. | `memory_format`; `legacy_published_intent`; `converted_card_parts` | mcp/src/agents_remember/application/read_files_format.py:29-32; mcp/src/agents_remember/application/read_files_format.py:35-49; mcp/src/agents_remember/application/read_files_format.py:65-93 |
| Citation tools route by format. | `citation_check_tool`; `citation_fix_tool` | mcp/src/agents_remember/application/memory_tools.py:173-209; mcp/src/agents_remember/application/memory_tools.py:233-276 |
| The rule 9 refusal in the quality controller. | `_execute_memory_quality` | mcp/src/agents_remember/application/memory_quality/controller.py:393-467 |
| The composition binds the base converter and the crossing. | `build_default_worktree_services` | mcp/src/agents_remember/application/worktree_services.py:210-222 |

## 260928-MIK-L28 Test Proofs Are Read Back, Named In Two Forms, And Listed When Missing

**Route meaning extended (MIK-R28@v1 rules 2, 4, 5 and 6).** One new module and three touched ones on this
route:

- [`knowledge_proofs.py`](knowledge_proofs.py.md) (new) reads `proves` entries back from a converted tree's
  derived index. `tree_view_proofs` gives `knowledge_read`'s `invariant` and `family` views their proofs;
  `invariants_without_proof` lists the live invariants no proof names, with the tests their migrated
  `origin.handoff.evidence` mentions. Both answer `None` for an unconverted tree, so nothing changes before
  MIK-R37.
- [`knowledge_writer/handoff.py`](knowledge_writer/handoff.py.md) reads a second evidence form: beside
  `path::name`, the pytest selection `path -k name` with one identifier, for `.py` files (**architect
  ruling**). A test module named without a test is a `TestFileMention`.
- [`knowledge_writer/authoring.py`](knowledge_writer/authoring.py.md) reports that mention `unresolvable`.
  A proof is still written only once the hand-off carries the curator's facet.
- [`memory_quality/controller.py`](memory_quality/controller.py.md) hands the checklist the "without proof"
  list. **The list is checklist-only and informational (architect ruling):** it never counts toward
  `curatorActionableCount` and adds no field to the wire summary.

Rule 3 (proofs in change detection) and the stale-proof clause are **not built on this route: by architect
ruling they move to L08 and L03**, which carry the proof test cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two readings of proofs. | `tree_view_proofs`; `invariants_without_proof` | mcp/src/agents_remember/application/knowledge_proofs.py:69-87; mcp/src/agents_remember/application/knowledge_proofs.py:157-190 |
| The evidence parser's two forms and the bare test module. | `tests_named_in`; `TestFileMention` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:125-133; mcp/src/agents_remember/application/knowledge_writer/handoff.py:136-158 |
| The bare test module is reported `unresolvable`. | `_cited_test` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:559-585 |
| The controller's informational input to the checklist. | `_without_proof` | mcp/src/agents_remember/application/memory_quality/controller.py:762-773 |

## 260928-MIK-L08 The Change-To-Knowledge Worklist Package, And The Writer's Carry

**Route meaning extended (MIK-R08@v2).** A new sub-package and four touched modules on this route:

- [`knowledge_worklist/`](knowledge_worklist/__init__.py.md) (new, nine modules) computes a leaf's worklist:
  [`code`](knowledge_worklist/code.py.md) (pinned zero-context hunks, line-range mapping, ranges and content
  identities), [`knowledge`](knowledge_worklist/knowledge.py.md) (K_B and K_C through the derived index's
  parser, in memory by **architect ruling 2**), [`classify`](knowledge_worklist/classify.py.md) (entry
  classes, with **definition 4 winning** when the blob is unchanged, and the knowledge-side changes),
  [`registry`](knowledge_worklist/registry.py.md) (item kinds and stable IDs),
  [`compute`](knowledge_worklist/compute.py.md) (the one-pass scope, items, gate linkage; a partial
  inventory is `incomplete`), [`leaf`](knowledge_worklist/leaf.py.md) (the sides from a contract, K_B by
  `Code-Commit` trailer, persistence, and `recompute_leaf_worklist`, which never raises),
  [`surface`](knowledge_worklist/surface.py.md) (what the integrity tool returns) and
  [`base_cache`](knowledge_worklist/base_cache.py.md) (the converted K_B, cached under
  `<coordination-root>/runtime/knowledge-worklist-bases`, never inside a working tree).
- [`knowledge_writer/carry.py`](knowledge_writer/carry.py.md) (new), called by
  [`writer.py`](knowledge_writer/writer.py.md) and reported by [`report.py`](knowledge_writer/report.py.md),
  re-records `carried` entries at C and updates only this leaf's own open history row (**ruling 5**).
- [`memory_quality/controller.py`](memory_quality/controller.py.md) recomputes the worklist on every
  contract-scoped run and hands it to the checklist as information.
- [`worktree_services.py`](worktree_services.py.md) binds `LeafWorklistRecompute` as the worktree layer's
  `KnowledgeWorklistPort`, the managed-sync trigger (**ruling 1**).
- [`task_docs/task_doc_tools.py`](task_docs/task_doc_tools.py.md) lets `set_field` set
  `knowledgeMaintenanceScope`.

The worklist is inert while both memory sides are unconverted, so the installed runtime is unchanged.

| Finding | Anchor | Source |
| --- | --- | --- |
| The package map. | "a change elsewhere in the same file raises nothing" | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:26-26 |
| The one recompute entry point and the port adapter. | `recompute_leaf_worklist`; `LeafWorklistRecompute` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:548-579; mcp/src/agents_remember/application/knowledge_worklist/leaf.py:582-591 |
| The writer's carry. | `carry_entries` | mcp/src/agents_remember/application/knowledge_writer/carry.py:65-90 |
| The controller's recompute. | `_knowledge_worklist` | mcp/src/agents_remember/application/memory_quality/controller.py:478-487 |

## 260928-MIK-L03 Stale Invariants Flagged At Read Time: The Currentness Package

**Route meaning extended (MIK-R03@v2).** A new sub-package and one touched module on this route:

- [`knowledge_currentness/`](knowledge_currentness/__init__.py.md) (new, four modules) computes each returned
  invariant's state at a code tree: [`observe`](knowledge_currentness/observe.py.md) (one entry's state,
  reusing the worklist's `CodeTrees.resolve` and the one content identity, and the observation cache),
  [`state`](knowledge_currentness/state.py.md) (`invariant_currentness`, the one function of (code tree,
  memory tree), and the rule-2 precedence) and [`surface`](knowledge_currentness/surface.py.md) (the block
  both read surfaces attach).
- [`published_intent.py`](published_intent.py.md) attaches `currentness` to the published-intent block for a
  converted tree.

**Architect rulings recorded on the cards (2026-09-29):**

- **Stale proofs (carried L28 ruling 1a).** Proofs are observed like realizations; a stale proof makes its
  invariant stale.
- **18:42:37.** `read_ar_files` observes at the tree it already resolved for its source (`HEAD^{tree}`),
  names it, and states that uncommitted edits are not reflected; `knowledge_read` counts only `codeTreeId`
  and never uses `HEAD`; the returned invariants and families, the extended cache key, and a missing
  line-range blob as `unverifiable` are accepted.
- **19:13:41.** Entry order: no tree → `unverifiable`; absent path → `stale`; unchanged blob → `current`;
  changed blob with an unsupported locator → `unverifiable`. Subprocess or index failures give
  `unverifiable` and never refuse a read, and failures are never cached. The cache is bounded at 8,192
  entries. The counts cover every invariant carried, named or in full. With a read-wide reason, entries are
  compact.

Both surfaces attach the block only for a converted memory tree, so the installed runtime is unchanged.

| Finding | Anchor | Source |
| --- | --- | --- |
| The package map. | "Stale invariants flagged at read time" | mcp/src/agents_remember/application/knowledge_currentness/__init__.py:1-14 |
| The check order and the cache contract. | `_decided_without_resolving`; `_OBSERVATION_CAPACITY` | mcp/src/agents_remember/application/knowledge_currentness/observe.py:238-255; mcp/src/agents_remember/application/knowledge_currentness/observe.py:80-80 |
| The one state function. | `invariant_currentness` | mcp/src/agents_remember/application/knowledge_currentness/state.py:148-198 |
| The block, which never raises. | `read_currentness` | mcp/src/agents_remember/application/knowledge_currentness/surface.py:104-122 |
| The published-intent block's resolved tree and `treeScope`, inside the bounded block since MIK-R02. | `_tree_block`; `_TREE_SCOPE` | mcp/src/agents_remember/application/published_intent.py:514-536; mcp/src/agents_remember/application/published_intent.py:572-575 |

## 260928-MIK-L30 The Onboarding Trace Kind, Its Sides, And The Two Enforcement Points

**Route meaning extended (MIK-R30@v1).** One new module and five touched modules on this route carry the
onboarding refresh gate on history files for converted memory trees (the rule itself lives in
`worktrees/modules/onboarding_trace.py`):

- **`knowledge_worklist/onboarding_trace.py` (new, carded):** registers the `onboarding_trace` kind (subject
  `onboarding:<path>` or `onboarding:<route>/overview`; facts `sources`, `markdown`, `sidecar`,
  `countedChange`; satisfied by a counted change or a `no_impact` row), resolves the gate's sides (`None`
  where neither side is converted; an incomplete side for mixed formats; the converted base otherwise) and
  merges the items into the worklist's one list, sorted by `(kind, subject)`.
- **`knowledge_worklist/leaf.py`:** `leaf_onboarding_trace_sides`, the gate chooser both enforcement points
  call, and the one-list step after a complete run. **`knowledge_worklist/base_cache.py`:**
  `converted_base_files`, the shared read-or-convert path, with format v2 that also holds onboarding Markdown.
  **`knowledge_worklist/__init__.py`:** imports the module so the kind is always registered.
- **`memory_quality/controller.py`:** `_onboarding_refresh_gate` runs the new gate on a converted tree (one
  repair finding per missing trace, `onboardingTrace` on the response) and today's
  `validate_memory_refresh_attestations` otherwise. **`prepared_certification.py`:** the closeout validator
  dispatches the same way.
- **`knowledge_writer/authoring.py`:** `_onboarding_row` lets the curator author the `no_impact` row through
  the writer.
- **Architect rulings (2026-09-29):** 18:49:50 (1: only a counted change or a row on converted trees;
  2: the items go into the persisted worklist; 3: `onboarding:overview`; 4: the cache is v2 and holds the
  Markdown; 5: deletion left to MIK-R37; 6: the wiring outside the Scope list is accepted); 19:23:45 (N1:
  mixed formats are an incomplete side; N2: `(kind, subject)` order; N3: a v1 cache file is ignored and
  rewritten; N4: a side failure is named; N5: an unreadable sidecar never satisfies a trace); 19:53:54 (R2-1:
  `onboarding_item_open` agrees with the live gate; R2-2: an unreadable K_B sidecar is an incomplete input, an
  unreadable K_C sidecar keeps the item open, a readable repair counts).
- **Inert before MIK-R37:** every unconverted leaf keeps today's gate unchanged.

| Finding | Anchor | Source |
| --- | --- | --- |
| The kind's registration and its four fields. | `ONBOARDING_TRACE_KIND` | mcp/src/agents_remember/application/knowledge_worklist/onboarding_trace.py:75-89 |
| The sides, refusing mixed formats. | `onboarding_trace_sides` | mcp/src/agents_remember/application/knowledge_worklist/onboarding_trace.py:109-157 |
| The curator run's dispatch between the history-file gate and today's gate. | `_onboarding_refresh_gate`; `onboarding_trace_gate_for_context` | mcp/src/agents_remember/application/memory_quality/controller.py:709-759 |
| The closeout validator's dispatch. | `_realize_prepared_memory`; `leaf_onboarding_trace_sides` | mcp/src/agents_remember/application/prepared_certification.py:342-421 |
| The cache path shared by the worklist and the gate. | `converted_base_files` | mcp/src/agents_remember/application/knowledge_worklist/base_cache.py:140-172 |

## 260928-MIK-L02 Bounded Continuation Accepted By The Mounted Read: The Paging Package

**Route meaning extended (MIK-R02@v2).** A new sub-package and four touched modules on this route cut every
bounded knowledge read of a converted memory tree to one declared token threshold, and give every page the
one continuation the mounted `knowledge_read` resumes, whichever surface minted it:

- [`knowledge_paging/`](knowledge_paging/__init__.py.md) (new, nine modules, each carded and governed by this
  overview; no sub-overview, following the `knowledge_worklist/` and `knowledge_currentness/` precedent):
  [`threshold`](knowledge_paging/threshold.py.md) (8,000 `tiktoken:o200k_base` tokens, one constant),
  [`pager`](knowledge_paging/pager.py.md) (whole rows, the header reference, `oversized_row`),
  [`bindings`](knowledge_paging/bindings.py.md) (minting and the named refusals),
  [`scope_pages`](knowledge_paging/scope_pages.py.md) and [`view_pages`](knowledge_paging/view_pages.py.md)
  (the two paged responses), [`block_pages`](knowledge_paging/block_pages.py.md) (one bound for a whole
  `read_ar_files` block, deferred and collapsed seeds), [`currentness`](knowledge_paging/currentness.py.md)
  (MIK-R03 state once per page) and [`tree_read`](knowledge_paging/tree_read.py.md) (the converted-tree branch
  of `knowledge_read`). The token model is `models/knowledge/continuation.py`.
- [`published_intent.py`](published_intent.py.md): a memory-tree seed is prepared for the block
  (`_tree_page_block`), and `bounded_block` lays the seeds out within one threshold around `_tree_block`,
  which carries the threshold and the currentness; `PUBLISHED_INTENT_MAX_UTF8_BYTES` left the public API.
- [`knowledge_read.py`](knowledge_read.py.md): `select_knowledge_scope`, the whole verified selection a page
  is cut from, under the same guard as `read_knowledge_scope`.
- [`knowledge_currentness/surface.py`](knowledge_currentness/surface.py.md): the once-per-page seam
  (`evaluate_answer`, `record_of`, `named_uuids`, `failure_document`, public `CURRENTNESS_FAILURES`).
- [`knowledge_projection.py`](knowledge_projection.py.md): a projection over the 20,000-character artifact
  bound continues in parts, or refuses `oversized_row`, and never raises.

**Architect rulings recorded on the cards (2026-09-29):**

- **Carried from the L23 review.** `knowledge_project` no longer raises for a text over 20,000 characters.
- **19:56:40 (Q1–Q7).** The threshold bounds the knowledge block of a `read_ar_files` response as a whole,
  and remaining seeds are deferred; the database byte budget stays private until MIK-R26 (L26);
  `page.headerReference` is interim and L01 makes it a row; the threshold, not `limit`, bounds converted
  reads; the continuation binds the effective ordering and page 1's code tree; projection parts are split by
  the file limit, and the first-64-rows projection cap is carried to L01.
- **20:40:40 (review R1).** An empty `orderingInput` is refused; `oversized_row` is only a row too large on
  its own; the token carries no local path; the deferred tail collapses; currentness is taken at the walk's
  code tree, once per page, and counted in the threshold; a missing code root is refused by name; refusals
  state the threshold; L02's catalog re-pin is the Thirty-seventh.
- **21:32:34 (review R2).** The binding is the content-addressed Git tree ID plus a check that the resolved
  root holds it; the more-than-64-seeds edge (R2-1) is carried to L01; R2-2 is accepted as documented in
  c-04; R2-3 was fixed by the architect.

**Candidate invariants (not ingested; recorded here and on the cards):** no converted-tree response exceeds
the threshold, except a single oversized row, returned alone; every selected row appears exactly once across
pages and surfaces; a continuation whose binding does not hold is refused with no partial page; no cursor
state is kept on the server; unconverted reads are unchanged. **Inert before MIK-R37:** only a converted tree
reaches the new code, and unconverted reads were measured byte-identical to base.

| Finding | Anchor | Source |
| --- | --- | --- |
| The paging package map and the seam for MIK-R01 and MIK-R05. | "Bounded pages of a memory tree's knowledge" | mcp/src/agents_remember/application/knowledge_paging/__init__.py:1-30 |
| The one declared threshold. | `KNOWLEDGE_PAGE_THRESHOLD_TOKENS` | mcp/src/agents_remember/application/knowledge_paging/threshold.py:27-27 |
| A cut of whole rows: blocked versus oversized. | `cut_page` | mcp/src/agents_remember/application/knowledge_paging/pager.py:122-159 |
| One bound for a whole `read_ar_files` knowledge block, whose tail collapses per seed kind (leaf or scope) since MIK-R01. | `bounded_block`; `_tail` | mcp/src/agents_remember/application/knowledge_paging/block_pages.py:52-79; mcp/src/agents_remember/application/knowledge_paging/block_pages.py:82-91 |
| The converted-tree branch of `knowledge_read`. | `read_tree_page` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:212-251 |
| The whole verified selection a page is cut from. | `select_knowledge_scope` | mcp/src/agents_remember/application/knowledge_read.py:169-180 |
| A projection continues in parts or refuses by name. | `_parts`; `_oversized_row` | mcp/src/agents_remember/application/knowledge_projection.py:335-357; mcp/src/agents_remember/application/knowledge_projection.py:364-377 |

## 260928-MIK-L11 Planned Invariant Effects Reconciliation: Declared Effects Against Delivered Rows

**Route meaning extended (MIK-R11@v2).** A leaf's task document may declare, before implementation, the
invariant and family effects it expects (`expectedKnowledgeEffects`, owned by the task plane:
`tasks/document.py`). One new module and six touched modules on this route reconcile that declaration with
what the leaf's history rows deliver, and let the curator answer what was not delivered:

- [`knowledge_worklist/planned_effects.py`](knowledge_worklist/planned_effects.py.md) (new, carded, governed by
  this overview; no sub-overview, following the `knowledge_worklist/` precedent): registers the
  `planned_untouched` kind and reconciles each declaration against the leaf's own history file in K_C.
  `invariant:<ID>` + E matches only a `changed` row with effect E (or, for `retire`, a retiring `deleted`
  row); `family:<ID>` matches any `changed` family row; `new:<label>` matches an invariant new in K_C, of this
  leaf, whose `origin.handoffEntry` is the label; anything else, a `no_impact` row included, leaves it
  unmatched, and an ID K_C does not hold is `subject_unknown`. Every `touched_invariant`, `stale_invariant`
  and `reached_family` item is marked `planned` or `unplanned`.
- [`knowledge_worklist/compute.py`](knowledge_worklist/compute.py.md) (step 5: the marks and the items,
  sorted with the rest; `plannedEffects` in the document, outside the digest),
  [`leaf.py`](knowledge_worklist/leaf.py.md) (the declaration read through the task plane's strict lookup; an
  unreadable leaf document makes the run `incomplete`), [`surface.py`](knowledge_worklist/surface.py.md) (the
  tool rows carry `planning` and `plannedEffects`) and [`__init__.py`](knowledge_worklist/__init__.py.md) (the
  registering import).
- [`knowledge_writer/authoring.py`](knowledge_writer/authoring.py.md) (`_planned_row`, `_unresolved_ref`,
  `DecisionResolver`), [`handoff.py`](knowledge_writer/handoff.py.md) (the `ref` row key) and
  [`writer.py`](knowledge_writer/writer.py.md) (`WriteRequest.decisions`): the curator writes a **planned row**
  (`planned:<declared subject>#<effect>`, `realized_elsewhere` | `deferred` | `dropped`, with a `ref`) through
  `knowledge-ingest`; the writer refuses a ref that does not resolve, and resolves a `dropped` decision
  through the task owner at write time (a wave, with no task owner, refuses it).
- [`task_docs/task_doc_tools.py`](task_docs/task_doc_tools.py.md): `set_field` may write the declaration.

**Architect rulings recorded on the cards (2026-09-29):**

- **21:56:18 (Q1–Q5).** Q1: the reviewer-UI half of rule 7 is carried to L31; the marks stay in the persisted
  worklist, the curator checklist and `knowledge_integrity_check`. Q2: no real task document declares the
  field until the L37 install (the installed runtime refuses unknown task-document fields). Q3: the
  adversarial reviewer's role file gains the line that checks a declaration against its packet. Q4: `new:`
  matches writer-authored invariants only (legacy-converted records carry no `handoffEntry`). Q5: the detail
  choices — `requirementRef` as `<ID>@v<n>`; a `dropped` row cites a decision by its `at`, ambiguous
  duplicates refused; family declarations ignore the effect; stale invariants are marked; `deferred` refs are
  shape-checked only.
- **22:35:34 (review R1).** F1: a `dropped` decision resolves through the strict leaf lookup, and ambiguity
  refuses. F2: an unreadable leaf document makes the worklist `incomplete` with a named input, never
  `declared: false` (`leaf_maintenance_scope`'s fail-open read is carried to L09). F3: the four missing
  matching assertions were added. F4: worklists persisted before this build differ in digest from a
  recompute (the `planning` mark), carried to L09. F5 and F6 accepted. F7: whichever of L06 and L11 lands
  second renumbers its compute step and keeps L11's marking and sort over the combined items.

**Candidate invariants (not ingested; recorded here and on the cards):** with no declaration, every item is
`unplanned` and there are no `planned_untouched` items; a `planned_untouched` item is answered only by a
planned row that resolves its ref; an unreadable leaf document never reads as "nothing declared"; the
subject key is built from the declared subject and effect, never from list position; an absent field leaves
existing task-intent digests unchanged. **Inert before MIK-R37:** an unconverted leaf gets no worklist, and
the declaration is read only after the applicability probe.

| Finding | Anchor | Source |
| --- | --- | --- |
| The kind, registered on import. | `PLANNED_UNTOUCHED_KIND` | mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py:67-81 |
| The reconciliation and its matching. | `reconcile_planned_effects`; `_match` | mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py:154-181; mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py:184-200 |
| Step 5 of the run. | `reconcile_planned_effects`; `plannedEffects` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:249-249; mcp/src/agents_remember/application/knowledge_worklist/compute.py:286-286 |
| The declaration read fail-closed. | `leaf_expected_effects`; `strict_leaf_doc` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:152-161 |
| The planned row through the writer, and its ref check. | `_planned_row`; `_unresolved_ref` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:722-768; mcp/src/agents_remember/application/knowledge_writer/authoring.py:923-941 |

## 260928-MIK-L06 Family Route Maintenance: The Route Conditions In The Worklist, And A Moved Row That Relocates

**Route meaning extended (MIK-R06@v2).** A family's routes are its index into the codebase (MIK-R04); a route
that drifts from the code is stale memory. One new module and five touched modules on this route keep the
routes maintained with the code, and let the curator answer a directory move with the rows it means:

- [`knowledge_worklist/route_conditions.py`](knowledge_worklist/route_conditions.py.md) (new, carded, governed
  by this overview; no sub-overview, following the `knowledge_worklist/` precedent): registers the
  `family_route_condition` kind (subject `<FAM-ID>#<condition>`, owner MIK-R06) and evaluates
  `route_path_absent`, `route_emptied` (waived for an `unrealized_family`), `realization_uncovered` and
  `route_unassigned` over K_C's entries, judged where their files lie at C, on K_B's and K_C's route sets. A
  retired family raises nothing. The item is answered only by the leaf's family row with a disposition other
  than `no_impact` while the K_C record satisfies MIK-R04, and `family_route_item_open` is the stored
  predicate the gate (L09) will apply.
- [`knowledge_worklist/compute.py`](knowledge_worklist/compute.py.md) (step 6, `_route_items`; `Item.extra`
  carries `satisfiedBy`; `_Run.document` split into `_scope`, `_first_entries`, `_stale`, `_scope_document`
  and `_entries_document`) and [`__init__.py`](knowledge_worklist/__init__.py.md) (the kind and the predicate
  exported).
- [`knowledge_writer/handoff.py`](knowledge_writer/handoff.py.md) (a cover may carry `path`; a malformed path
  and remove-plus-path are named refusals) and [`authoring.py`](knowledge_writer/authoring.py.md) (a `moved`
  row relocates the entry into the new file's sidecar and re-anchors it at C; a path on any other disposition
  is refused). This closes the conformance gap of landed L12 that MIK-R06's directory-move evidence exposed.
- The checklist rendering of the new kind is `memory_quality/knowledge_worklist_section.py`'s (see the
  `memory_quality` overview).

**Architect rulings recorded on the cards:**

- **Carried from L04 (recorded before 2026-09-29T17:10:08).** A dead carried route, which the validator only
  reports (`R04.1-carried-route-absent`), becomes a mandatory item that needs a family row.
- **2026-09-29T21:49:19 (Q1–Q7).** Q1: reached families are evaluated on all four conditions; unreached
  families only for `route_path_absent` on a route this leaf's range killed (present at B, absent at C); a
  route already dead at B stays the validator's report for R19. Q2: both route sets are judged, and one family
  row answers all of a family's items. Q3: `route_unassigned` needs a non-empty route set that satisfies
  MIK-R04 (the `legacy-unassessed` waiver does not answer it), or retirement. Q4: a rename target is ambiguous
  when the family's renamed files under the affected route land in more than one outermost directory. Q5: the
  mechanical suggestion uses the rename-mapped locations when unambiguous; otherwise no suggestion, with
  `renameCandidates` and `unmappedLocations` listed. Q6: the writer's moved-row relocation. Q7: recorded on
  L09.
- **2026-09-29T22:40:22 (review R1).** F1: a malformed cover path is a named refusal. N1: conditions are judged
  at the entries' effective locations at C. N2: carried to L09. N6: complexity reduced (radon 10 or less).
  N7: a cover with both `remove` and `path` is refused. N3, N4, N5 and N8 accepted.
- **2026-09-29T23:14:41.** `recordSatisfiesRoutes` holds only when MIK-R04 holds both over the record as
  written and at the effective locations; `_Run.document` was reduced at the merge with L11.

**Candidate invariants (not ingested; recorded here and on the cards):** a family route problem the leaf
causes cannot survive its closeout without a non-`no_impact` family row and routes that satisfy MIK-R04; a
route already dead at B is not charged to an unrelated leaf; the stored predicate and the live `satisfiedBy`
agree; the writer refuses a malformed cover path rather than crashing; retired families raise nothing.
**Inert before MIK-R37:** an unconverted leaf gets no worklist, and the writer runs only on converted memory.

| Finding | Anchor | Source |
| --- | --- | --- |
| The kind, registered on import. | `FAMILY_ROUTE_CONDITION_KIND` | mcp/src/agents_remember/application/knowledge_worklist/route_conditions.py:113-138 |
| The stored predicate for the gate. | `family_route_item_open` | mcp/src/agents_remember/application/knowledge_worklist/route_conditions.py:141-154 |
| Reached families on all four conditions, others only on a killed route. | `conditions`; `_with_killed_routes` | mcp/src/agents_remember/application/knowledge_worklist/route_conditions.py:299-320; mcp/src/agents_remember/application/knowledge_worklist/route_conditions.py:355-367 |
| Step 6 of the run. | `_route_items` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:502-525 |
| The cover path, checked at parse time. | `_cover_path` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:595-614 |
| The moved row's relocation. | `_relocate` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:1069-1080 |

## 260928-MIK-L01 The Family-Complete Leaf Read: One Path, Its Whole Family Neighbourhood

**Route meaning extended (MIK-R01@v2).** A read seeded with one source path now returns, from a converted
memory tree's derived index, the path's own invariants, every family containing them with its guarantee and
routes, every member's statement, conditions and entries, and the advertised frontier: one family hop, in one
declared order, in one response when it fits the MIK-R02 threshold and otherwise as pages `knowledge_read`
continues. At intake a leaf read returned 3 of 25 items and never the family. One new package and six touched
modules on this route carry it:

- [`knowledge_leaf/`](knowledge_leaf/__init__.py.md) (new, 4 modules, each carded and governed by this
  overview; no sub-overview, following the `knowledge_paging/` precedent):
  - [`selection.py`](knowledge_leaf/selection.py.md): `select_leaf` builds the structure (which records and
    entries, in which order) and the manifest digest over row identities only; `leaf_rows` renders it at the
    walk's code tree; `leaf_counts` and `family_names`.
  - [`pages.py`](knowledge_leaf/pages.py.md): `PreparedLeaf`, which has `PreparedScope`'s shape, the `leaf`
    token resuming on `source_context`, and the literal `family_header_reference` first row.
  - [`currentness.py`](knowledge_leaf/currentness.py.md): `LeafCurrentness`, the page's `currentness` subset,
    merged with the scope subset in a mixed block.
- [`published_intent.py`](published_intent.py.md): a path seed of a converted tree is prepared by
  `prepare_leaf`; `_block_policy` sets the block's top-level `policyVersion`; `_SEED_FAILURES` adds
  `IndexMismatchError`.
- [`knowledge_paging/`](knowledge_paging/__init__.py.md): `block_pages` takes either prepared kind, collapses
  each kind separately and refuses a tail too long for one queue (`seed_queue_exceeded`); `tree_read` routes a
  fresh `source_context` path read and every `leaf` token to `_leaf_response`, adds `families` to the
  `invariant` view and names the memory tree on every refusal; `currentness` exposes `subset`; the package
  docstring names three paged responses.
- [`knowledge_projection.py`](knowledge_projection.py.md): `whole_views` projects a converted tree's view
  whole, with no 64-row cap.

**Carried obligations, each met (recorded on the cards):**

- The header reference is a literal first row of a leaf page that continues a family (L02 Q3, 2026-09-29
  19:56:40); a view page still names it in `page.headerReference`.
- The 64-row projection cut is removed on converted trees, and the database projection is unchanged (L02 Q7;
  accepted 23:21:57).
- A `repositoryRoot` with no commit is refused `selected_input_unavailable` by name (2026-09-29 21:17:07;
  `mcp/tools/knowledge.py`).
- No local path in a continuation: a resumed leaf walk resolves its repository from `repositoryRoot` or the
  workspace, and is refused by name when that repository lacks the tree (21:17:07).
- More than 64 queued seeds is the named refusal `seed_queue_exceeded` (R2-1, 21:32:34; accepted 23:21:57).

**Architect rulings recorded on the cards:**

- **2026-09-29T23:21:57 (Q1–Q7).** Q1: an invariant has no title and none is added; a `member_reference` row's
  title is the statement's first sentence cut to 80 characters, labelled `titleDerivedFrom: "statement"`. Q2:
  seed invariants are listed in their family header's `members` and not repeated as reference rows. Q3: proof
  entries are entries at the path and seed the read. Q4: conformance is the equal manifest digest; entry states
  follow each surface's code tree. Q5: the tree block's top-level `policyVersion` states
  `family-complete-leaf/v1` where the leaf read applies. Q6: route-chain families for entry-less paths are
  MIK-R05's (resolved by 260928-MIK-L05, below). Q7: a non-default `orderingInput` on a fresh leaf read is refused (one declared order).
- **2026-09-30T00:08:39 (review R1).** N1: helpers extracted so every function is 10 or less under radon. N2:
  identity seeds stay supported on a tree, and a test walks one through both surfaces and pins the mixed-block
  policy. N3: refusals on converted trees name the memory tree and index state. N4: one `advertised_family`
  row per frontier family, with `via`. N5: the block policy follows the seeds asked, even when all were
  refused. N6: `registration_absent` names realization and proof claims. N9: the c-04 rewrap. The catalog
  re-pin became the Thirty-ninth at the sync onto L11.

**Candidate invariants (not ingested; recorded here and on the cards):**

1. A converted leaf read returns the complete one-hop family selection, the same on both surfaces (equal
   manifest digest). Realized by `select_leaf` and one `PreparedLeaf` for both surfaces; proved by
   `test_a_path_selects_one_family_hop_in_the_declared_order`,
   `test_both_surfaces_return_one_selection_under_one_manifest`, and the 84/84 real-path walks of the worker
   and the reviewer's independent oracle.
2. A member already returned appears later only as a reference row. Realized by `_order`; proved by the
   selection test's `member_reference` assertions (fixtures only: the real tree has no shared member).
3. Every page continuing a family starts with a header reference row. Realized by `pages._page`; proved by
   the leaf-walk test and the adapted L02 40-member walk (`rows[0]`).
4. Refusals on converted trees name the memory tree. Realized by `tree_read._refused`; proved by
   `test_absent_and_partial_states_are_named`.
5. Unconverted reads are unchanged. Realized by the `memory_tree` branches; proved by the worker's
   byte-identical 69,481-byte comparison, the reviewer's byte-identical rerun at `c493b557`, and the 25
   database projections byte-identical to base.

**Inert before MIK-R37:** only a converted memory tree reaches the new code.

| Finding | Anchor | Source |
| --- | --- | --- |
| The leaf package statement. | "The family-complete leaf read of a converted memory tree" | mcp/src/agents_remember/application/knowledge_leaf/__init__.py:1-13 |
| The selection and its declared order, which since MIK-R05 ends with the route-chain rows. | `select_leaf`; `_order` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:142-152; mcp/src/agents_remember/application/knowledge_leaf/selection.py:270-298 |
| One prepared leaf for both surfaces, with the literal reference row and, since MIK-R05, a path page's `routeChain`. | `prepare_leaf`; `_page` | mcp/src/agents_remember/application/knowledge_leaf/pages.py:164-208; mcp/src/agents_remember/application/knowledge_leaf/pages.py:288-322 |
| A path seed of the block is read as a leaf. | `_tree_page_block`; `prepare_leaf` | mcp/src/agents_remember/application/published_intent.py:720-760 |
| The block's policy follows the seeds asked. | `_block_policy` | mcp/src/agents_remember/application/published_intent.py:539-549 |
| Each kind's tail, or the named queue refusal. | `_collapsed`; `SEED_QUEUE_EXCEEDED` | mcp/src/agents_remember/application/knowledge_paging/block_pages.py:42-42; mcp/src/agents_remember/application/knowledge_paging/block_pages.py:103-124 |
| The leaf response of the mounted read (since MIK-R05 of a path or a family seed), and refusals that name the tree. | `_leaf_response`; `_refused` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:577-633; mcp/src/agents_remember/application/knowledge_paging/tree_read.py:646-660 |
| A converted tree's view projected whole. | `_whole_view` | mcp/src/agents_remember/application/knowledge_projection.py:280-294 |

## 260928-MIK-L13 Decision Records: The Writer Reports Requirement Endpoints

**Route meaning extended (MIK-R13@v2).** The curator writer already wrote a `records` item of `kind: decision`
(MIK-R12); MIK-R13 adds no decision-specific authoring. On this route it adds requirement-endpoint reporting:

- [`knowledge_writer/requirement_links.py`](knowledge_writer/requirement_links.py.md) (new, carded and governed by
  this overview): for every record the run created, updated or left unchanged, each link whose target is a
  requirement reference `{task, packet, id, version}` is resolved by the requirement owner through
  `memory/knowledge/requirement_endpoint.resolve_requirement_endpoint`.
- [`knowledge_writer/writer.py`](knowledge_writer/writer.py.md): `WriteRequest.coordination_root` (optional);
  `write_knowledge` fills `WriteReport.requirements`, also on a refused run.
- [`knowledge_writer/report.py`](knowledge_writer/report.py.md): `EndpointOutcome`, the JSON key
  `requirementEndpoints`, and one text line per endpoint from `_endpoint_line` (review F3).
- [`knowledge_writer/__init__.py`](knowledge_writer/__init__.py.md): the module map names `requirement_links`.

An unresolved endpoint (no root, a repository outside `tasks/`, or the owner's refusal such as a version mismatch or
a missing packet) is **reported, never refused**: the link is written as authored. Resolution lives in the writer
because the validator (`memory_quality`) ranks below `memory` and commit routes carry no coordination root (ruling
2026-09-30T01:45:56 Q5/Q6). The CLI routes pass the root (`cli/knowledge_write_route.py`, and the bootstrap wave's
admitted authority, review F4).

- **Architect rulings.** 2026-09-30T01:45:56: Q1 `origin.task` plus the ruling named in the attached entry's
  evidence satisfies "origin names the task or ruling", and the `knowledge-bootstrap:<repo>` origin is valid wave
  provenance; Q2 `R13.3-governs` is report-only and a `reconsider_on` link to the chosen alternative is refused;
  Q3 the content rules apply to every decision, new or carried (the conversion exports none); Q4 packet rule 6
  (reads) is carried to L29; Q5 and Q6 are carried to L14 (reuse `resolve_requirement_endpoint`; guard
  `reconsider_on` index stability when alternatives are reordered; both met by L14, see its section below); Q7
  accepted; Q8 carried to L26 (the resolver
  moves with `requirement_owner.py` if `memory/knowledge` is retired). 2026-09-30T02:05:07 (review R1): F3 the
  render helper `_endpoint_line`, so `WriteReport.render` keeps its base complexity; F4 the bootstrap-wave test
  asserts a resolved endpoint through the admitted coordination root; F6 a decision is never an export for
  admission; F1 and F2 stay with L14 and L29; F5 accepted; F7 resolved by the sync onto L06.
- **Candidate invariants (not ingested; recorded on the cards):** (1) a decision has at least two alternatives and exactly one chosen; (2) every rejected or deferred alternative
  says when to reconsider; (3) superseded is derived, never stored; (4) an unresolved requirement endpoint is
  reported, never refused; (5) a decision is never treated as an export for admission. The fourth is realized on this route.

**Inert before MIK-R37:** the writer runs only on converted memory, and the new field defaults to `None`.

| Finding | Anchor | Source |
| --- | --- | --- |
| Each requirement link target of the run's records, with the owner's resolution. | `requirement_endpoints` | mcp/src/agents_remember/application/knowledge_writer/requirement_links.py:24-53 |
| The writer's coordination root and the report's endpoints. | `coordination_root`; `requirement_endpoints` | mcp/src/agents_remember/application/knowledge_writer/writer.py:87-87; mcp/src/agents_remember/application/knowledge_writer/writer.py:137-137 |
| One endpoint outcome; unresolved is reported, never refused. | `EndpointOutcome` | mcp/src/agents_remember/application/knowledge_writer/report.py:69-82 |

## 260928-MIK-L25 The Reviewer On Git Trees: Four Trees, Pins, The Tree View, And The Archive Hook

**Route meaning extended (MIK-R25@v1).** For a leaf whose memory is converted, a review comparison is four Git
trees — code base B, code candidate C, memory base K_B (the worklist's `paired_memory_commit`) and memory candidate
K_C — and each memory side is read through the MIK-R23 derived index of its tree. The landed review composition,
navigation, family context and UI run unchanged over those indexes (rule 6); **no database copy is created,
retained or read** (ruling 2026-09-29T22:22:37 Q1: the derived index is the permitted read path). Leaves whose
memory is unconverted — every production leaf before MIK-R37 — take exactly the old path.

Four new modules, each carded and governed by this overview:

- [`review_tree_comparison.py`](review_tree_comparison.py.md): capture, pin (`refs/ar/review/<task-directory>/<leaf>/<n>`,
  create-only, before publication) and record (`notes/reports/review-comparisons/<leaf>/<n>.json`) the four
  trees; reuse a record whose trees match, so a repeat read writes nothing (Q5, review F6); the converted base
  written as a Git tree (R24 rule 7); reopen from tree ids with `unavailable-history` for memory **and** code trees
  (review F4); `tree_resolution` for the landed composition.
- [`review_legacy_comparison.py`](review_legacy_comparison.py.md): a closed leaf of a converted repository with no
  tree record: `legacy-unavailable` knowledge sides with the code sides kept, or a committed four-tree comparison.
- [`review_tree_knowledge.py`](review_tree_knowledge.py.md): `GET /api/review/trees`'s port — the Git diff of the
  memory trees grouped by record and by source path, MIK-R03 currentness per side, and the MIK-R08 worklist view.
- [`review_artifact_cleanup.py`](review_artifact_cleanup.py.md): the archive hook (rule 5, D17), bound as the
  worktree layer's `ReviewArtifactCleanupPort` by [`worktree_services.py`](worktree_services.py.md).

Touched: [`review_candidate_resolution.py`](review_candidate_resolution.py.md) (`_live_resolution`, `trees`,
`knowledge_unavailable`, the memory recheck, `_index_namespace`),
[`review_committed_leaf.py`](review_committed_leaf.py.md) (`_converted_repository_resolution` and the declaration
helpers) and [`review_comparison_freeze.py`](review_comparison_freeze.py.md) (a tree comparison is never frozen).

- **Architect rulings.** 2026-09-29T22:22:37: Q1 no knowledge dataset or copy is opened; Q2 the panel for rules 2
  and 3 is carried to L31/L32; Q3 the report at `notes/reports/review-artifact-cleanup.json` and
  `taskArchive.reviewArtifacts`; Q4 the hook also cleans unconverted tasks once installed (recorded on L37); Q5 GET
  writes are idempotent and confined; Q6 the L23 seal fix with `INDEX_FORMAT` v2; Q7 the K_B choice, the committed
  rule and the same-repository limit accepted as listed; Q8 the pre-existing ICR L47 ValidationError carried to
  L31; the complexity split. 23:15:34 (review R1): F1 exact own-task selection; F2 the hook never raises; F3 a
  refused generation is held; F4 lost code trees reported; F5 one task-id function; F6 Q5 extended to the record
  and caches; F7 L37 states that archival deletes all legacy dataset copies including curator scratch copies; F8
  accepted; F9 key casing carried to L31. 2026-09-30T00:08:39: the record-driven sweep removed. 01:00:07: every
  deletion target derives from the archived task's own identity. 01:37:42: physical confinement. 02:12:06: the
  `task.json` id confirmation. 02:32:42: (a) review refs keyed by the task directory name only; (b) the trust line
  for legacy cleanup (the task folder's system-written control documents); the TOCTOU window accepted; the test
  split.
- **Candidate invariants (not ingested; recorded on the cards):** (1) a review comparison pins its candidates
  before it is shown, and a repeat read writes nothing; (2) archival deletes only targets derived from the archived
  task's own identity, confined to its physical folder; (3) review refs are named by the task directory name only;
  (4) a tree Git can no longer produce is reported `unavailable-history`, never substituted; (5) unconverted memory
  reads are unchanged. All five are realized on this route.

| Finding | Anchor | Source |
| --- | --- | --- |
| Capture, pin and record a live leaf's four trees; none for an unconverted leaf. | `live_review_trees`; `_record`; `_pin` | mcp/src/agents_remember/application/review_tree_comparison.py:217-235; mcp/src/agents_remember/application/review_tree_comparison.py:437-472; mcp/src/agents_remember/application/review_tree_comparison.py:490-514 |
| The review-ref namespace is the task directory name. | `review_task_id` | mcp/src/agents_remember/application/review_tree_comparison.py:173-181 |
| Reopen from tree ids, naming every tree Git can no longer produce. | `reopened_trees`; `_code_sides` | mcp/src/agents_remember/application/review_tree_comparison.py:634-649; mcp/src/agents_remember/application/review_tree_comparison.py:652-666 |
| The tree view: diff, currentness, worklist; since MIK-L31 also the focused cards' entries when invariants are named. | `read_review_trees` | mcp/src/agents_remember/application/review_tree_knowledge.py:102-128 |
| The archive hook, confined to the task. | `cleanup_review_artifacts`; `_Confinement` | mcp/src/agents_remember/application/review_artifact_cleanup.py:138-172; mcp/src/agents_remember/application/review_artifact_cleanup.py:195-229 |
| The live pair dispatches a converted leaf to trees. | `_live_resolution` | mcp/src/agents_remember/application/review_candidate_resolution.py:245-286 |

## 260928-MIK-L10 Unexplained Change Disposition: Every Unlinked Change Needs An Authored Answer

**Route meaning extended (MIK-R10@v2).** If the closeout gate covered only code that already has knowledge, new code
would never enter the graph (D8). The worklist now raises an item for every change the gate linkage leaves
unlinked, and the curator answers each one:

- [`knowledge_worklist/unexplained.py`](knowledge_worklist/unexplained.py.md) (new, carded, governed here like the
  package's other modules) registers `unexplained_hunk` and `unexplained_file`, owns the **coverage lookup** (a
  path is covered when K_B holds a realization entry at it, or when its governing onboarding route's latest census
  status is `migrated`; read at K_B, ruling 2026-09-30T01:56:39 Q4), and raises one item per unlinked hunk or
  non-text change in every changed file. Hunks with identical changed lines in one file share an item; a symlink
  or submodule is keyed by its C tree-entry object.
- **What answers an item.** Covered: an attach or author puts an entry over the change and links it, so the item
  is not raised (enforced by linkage, ruling Q1), or the leaf's `no_invariant` row with a reason. Uncovered: the
  file's onboarding trace (MIK-R30), bound by `settle_uncovered` after the leaf route computes it. A
  `no_invariant` row about an uncovered item answers nothing and is reported as unnecessary, report-only (the
  answering set is built from covered items only, ruling 03:24:28 N2).
- **Delete-only hunks** admit only `no_invariant`: [`compute.py`](knowledge_worklist/compute.py.md) links a
  delete-only hunk only through a K_B range at B, the strict reading of MIK-R08 definition 8 and a correction of
  L08's output (ruling Q2; four `changeSetBar.tsx` hunks on ICR L47). The symmetric insertion-only note is
  carried to L09 (ruling 03:24:28 N3).
- [`knowledge_worklist/leaf.py`](knowledge_worklist/leaf.py.md) reads K_B's route coverage (its Git tree and
  census blobs, or a converted base's cached files, where every route is `pending`); an unreadable census makes
  the run `incomplete` naming K_B. It then settles uncovered items and keeps needed `onboarding:<path>` rows out
  of MIK-R30's unnecessary rows (ruling Q3), as [`memory_quality/controller.py`](memory_quality/controller.py.md)
  does for the checklist (`_needed_rows_dropped`); onboarding rows that answer an item are never unnecessary.
- [`knowledge_writer/authoring.py`](knowledge_writer/authoring.py.md) writes the `no_invariant` row
  (`_unexplained_row`) and refuses an attach to a retired invariant (`_attaches_to_retired`);
  [`knowledge_writer/code_anchors.py`](knowledge_writer/code_anchors.py.md) checks a `file:` row subject against
  C (`file_subject_mismatch`).
- Complexity: every touched function is at most 10 (radon), the standing bar (ruling 03:24:28 N1). Item volume
  (160 on ICR L47) is by design; grouping for the curator is carried to L31/L32.

**Candidate invariants (not ingested; the code is inert until MIK-R37):** every changed hunk in range is either
explained by a knowledge change or answered by an explicit disposition, and an unexplained hunk keeps its item
open; a delete-only hunk can be answered only by a disposition, never by attach or author; `no_invariant` answers
only covered items, and a row about an uncovered item is reported unnecessary and closes nothing; unconverted
memory reads are unchanged (no worklist while both memory sides are unconverted).

| Finding | Anchor | Source |
| --- | --- | --- |
| The two kinds, registered on import. | `UNEXPLAINED_HUNK_KIND`; `UNEXPLAINED_FILE_KIND` | mcp/src/agents_remember/application/knowledge_worklist/unexplained.py:124-145 |
| Coverage by a realization entry in K_B or a migrated route. | `_coverage` | mcp/src/agents_remember/application/knowledge_worklist/unexplained.py:196-211 |
| The answering set from covered items only. | `unexplained_items` | mcp/src/agents_remember/application/knowledge_worklist/unexplained.py:392-417 |
| A delete-only hunk is linked only by a K_B range. | "hunk.new_count > 0" | mcp/src/agents_remember/application/knowledge_worklist/compute.py:560-560 |
| The leaf route settles uncovered items and keeps needed rows. | `_settled_unexplained` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:461-480 |
| The checklist keeps needed onboarding rows out of the unnecessary report. | `_needed_rows_dropped` | mcp/src/agents_remember/application/memory_quality/controller.py:684-706 |
| The no_invariant row and the retired-attach refusal. | `_unexplained_row`; `_attaches_to_retired` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:682-720; mcp/src/agents_remember/application/knowledge_writer/authoring.py:348-360 |

## 260928-MIK-L05 Route-Chain Family Retrieval: A Path Sees Every Family Whose Territory It Lies In

**Route meaning extended (MIK-R05@v2).** A read seeded with a source path now also returns, compactly, every
live family with a route equal to, or an ancestor of, the path's directory, even when the path realizes none of
its members: a new or unattributed file is the typical case. Families are listed only at their own routes
(MIK-R04, D20), so the read walks upward. The chain rows come after the MIK-R01 content, as rows of the same
selection under the same manifest and the same MIK-R02 threshold. A *family seed* returns one family's full
MIK-R01 content. One new module and six touched modules on this route carry it:

- [`knowledge_leaf/chain.py`](knowledge_leaf/chain.py.md) (new, governed by this overview): the chain
  (`chain_directory`, `_links`, labelled `mechanical`), `select_chain` over L23's `families_governing` (nearest
  route, then family ID; live families and members only), the compact `chain_row` with `memberAtSeed` and the
  `expand` family seed, `route_chain_block` (`governed` or `no_governing_family`), and `shorten_served`, the
  `served_earlier` rendering only `read_ar_files` applies.
- [`knowledge_leaf/selection.py`](knowledge_leaf/selection.py.md): `select_leaf` also selects the chain and is
  `None` only with no entry and no governing family; new `select_family`; `_order` appends `chain_family` rows
  last; `chainFamilies`; `LEAF_POLICY_VERSION` = `v2`.
- [`knowledge_leaf/pages.py`](knowledge_leaf/pages.py.md): a path or a family seed; each path page states
  `routeChain`, and `registration: registration_absent` when it has no entry; `absent_chain` for the refusal;
  an unknown family seed is `selector_absent`. [`knowledge_leaf/__init__.py`](knowledge_leaf/__init__.py.md)
  re-exports `select_family` and `absent_chain`.
- [`knowledge_paging/tree_read.py`](knowledge_paging/tree_read.py.md): the family seed on `source_context`
  (`_family_response`), one rule for a named revision on fresh read and resume (`_revision_absent`), the
  family-seed resume by any spelling (`_named_subjects`), and the refusal's `routeChain`.
- [`published_intent.py`](published_intent.py.md): a path's `registration_absent` refusal carries its
  `routeChain`. [`read_files.py`](read_files.py.md): `_chain_rendered` shortens an already-served chain entry
  to `served_earlier` through the lifecycle's served ledger; overview attachment is unchanged.

The knowledge index is untouched (no `INDEX_FORMAT` change), and `mcp/tools/knowledge.py` is untouched.

**Architect rulings recorded on the cards:**

- **2026-09-30T03:32:18 (Q1–Q5).** Q1: on converted trees `source_context` with `familyRevisionId` and no
  `sourcePath` is the family seed (the old behaviour ignored the family, a defect); projected UUIDs are
  accepted. Q2: families already expanded still get a chain row, marked `memberAtSeed` (rule 4: the chain
  includes every entry). Q3: nearest route first, then family ID; `routeChain` gives the directory and the
  link count; an entry-less path no route covers stays a refusal (`no_governing_family`). Q4: the policy is
  bumped to `family-complete-leaf/v2`, because continuations bind the policy version. Q5: skill c-04 gains
  one paragraph on chain rows and the family seed.
- **2026-09-30T04:12:49 (review R1).** F1: the new tests and the adapted leaf-read test were split so no test
  function is at radon C. F2: a v1 continuation is refused under v2 with `continuation_binding_mismatch`. F4:
  a named `familyRevisionId` (`ID@rev` or projected UUID) is normalised to the bare ID on a family-seed
  resume. F3 (the `routeChain` block moves the page-1 cut by one row) and F6 (the bare-ID `expand` survives
  revision bumps) are accepted as designed. F5: the catalog pin is renumbered after L10 lands.
- **2026-09-30T04:45:22 (review R2, R2-1).** A revision the tree does not hold is refused `selector_absent` on
  resume as on a fresh read, including a bare `ID@`; the Forty-first pin became final at the sync onto
  `31d761a2`.

**Candidate invariants (not ingested; the code is inert until MIK-R37):**

1. A leaf read returns the governing route chain after the leaf content, each chain row exactly once, within
   the bound. Realized by `select_chain`, `_order` (chain last) and L02's `cut_page`; proved by
   `test_the_chain_is_the_directory_and_its_ancestors_never_a_child_or_a_sibling`,
   `test_chain_entries_are_compact_after_the_leaf_and_name_a_member_at_the_seed` and
   `test_chain_entries_count_toward_the_threshold_and_resume_like_the_leaf`, and on scratch-routed real data by
   the 84/84 walks (each row once, within threshold, chain after the leaf; largest 7,957 tokens).
2. A continuation is bound to tree, policy and seed; resuming under another family, path, policy or tree is
   refused `continuation_binding_mismatch`. Realized by the shared binding checks, `_subject_refusal` and
   `_named_subjects`; proved by `test_a_family_seed_walk_resumes_under_any_spelling_of_its_family` (another
   family) and `test_a_continuation_minted_under_the_v1_policy_is_refused` (policy), with L02's binding tests.
3. A revision the tree does not hold is refused `selector_absent`, on fresh read and resume alike. Realized by
   `_revision_absent`; proved by `test_a_family_seed_is_named_by_id_revision_or_projected_uuid` and
   `test_a_family_seed_walk_resumed_naming_a_revision_the_tree_lacks_is_refused`.
4. Unconverted memory reads are unchanged. Realized by the `memory_tree` and text-format branches; proved by
   the worker's byte-identical 105,164-byte comparison against base on the real `knowledge.sqlite`, including
   a `source_context` read naming `familyRevisionId`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The chain module statement. | "Route-chain families of a seed path" | mcp/src/agents_remember/application/knowledge_leaf/chain.py:1-26 |
| The chain lookup and its order. | `select_chain` | mcp/src/agents_remember/application/knowledge_leaf/chain.py:88-118 |
| The chain rows last in the declared order. | `CHAIN_ROW` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:295-297 |
| The family seed's selection. | `select_family` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:155-168 |
| The family seed on the mounted read, and one rule for a named revision. | `_family_response`; `_revision_absent` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:525-535; mcp/src/agents_remember/application/knowledge_paging/tree_read.py:547-565 |
| The rendering only `read_ar_files` applies. | `_chain_rendered` | mcp/src/agents_remember/application/read_files.py:348-354 |

## 260928-MIK-L31 Focused Expression Cards: Every Location Of The Selected Family, From The Pinned Trees

**Route meaning extended (MIK-R31).** The reviewer's central reading path shows every code and test location of the
selected family's members as a focused card; this route supplies its data. One new module,
[`review_tree_entries.py`](review_tree_entries.py.md) (carded, governed here): `tree_entries` lists every
realization and proof entry of the named invariants in K_B or K_C and places it on the code base B and the
candidate C with the worklist's own `CodeTrees.resolve` (MIK-R08 definition 3), each side with its own authored
role and rationale (or facet), its MIK-R03 state through `observe_entry`, and the range's excerpt from that side's
exact blob (bounded at 400 lines or 48,000 characters). `absent` and `unavailable` are kept apart; an unresolved
side names its reason and carries no range; `changed`/`unchanged` is by content identity and `undetermined`
otherwise. Placements are remembered in a bounded 8,192-entry LRU keyed like the observation cache (answers only).

- **[`review_tree_knowledge.py`](review_tree_knowledge.py.md)** answers a query that names invariants with
  `_entries_view` (ruling 2026-09-30T05:36:19 Q2: the on-demand read; the leaf-wide view carries no entries, 637 KB
  measured otherwise); pins a numbered leaf-wide read to that comparison, using the live resolution only when it is
  that number (review F11, 06:10:21; R2-6's extra resolution accepted); re-keys every wire document to snake_case
  with `snake_keys` (MIK-L25 review F9, carried here); and finds history rows also by the subject an item's
  `facts.row` names (PS-1 from L10's post-sync review, accepted at 05:36:19; L32 need not repeat it).
- **[`review_source_admission.py`](review_source_admission.py.md) and
  [`review_source_realization_link.py`](review_source_realization_link.py.md)**: the proof link (ruling Q1) and the
  initialize remedy (rule 6 O1), as the section above records; the link answer is composed by `_link_of` (radon).
- **[`review_curator_records.py`](review_curator_records.py.md)**: the MIK-L25 Q8 `ValidationError` fixed. A
  closed leaf binding many missing curator artifacts (ICR-L47: 94) reads as an `unavailable` channel; a detail over
  the 20,000-character prose bound names the count and the first three artifacts and bounds the owner's error at
  4,000 characters, while a detail that fits keeps its landed wording exactly (review F6, R2-2). On L25's 29
  unconverted reads 26 are byte-identical to base; the other 3 were the `ValidationError`.

**Rulings.** Carried in: L11 (planned/unplanned marks, rendered on the card voices and the panel), L25 Q2 (the
panel), L25 F9 (snake_case), L25 Q8 (the `ValidationError`), L10 (unexplained items grouped by file and coverage),
PS-1 (`facts.row`). 05:36:19: Q1 proof admission; Q2 `invariants=` (at most 500, each key at most 64 characters
since F10); Q3 a SYNTHETIC-body test for the no-member first-page branch; Q4 roster order stays with MIK-R33 (L33).
06:10:21 (review R1): F1 one full file keyed by card; F2 "loaded n of m"; F3, F4, F6, F12 tests; F5 prose once only
with both sides present; F7 re-capture with provenance; F10 key bound; F11 comparison pinning. 06:47:03 (R2): the
pyright fix, R2-2, R2-3, R2-5 (`cardScope` counted on one side, capped), R2-6 accepted, R2-7. 09:38:03 (R3):
pass-with-notes; R3-N1 (`cardScope` may say "loaded 2 of 2 … load the rest" when only the narrower side is
incomplete) accepted as a note.

**Candidate invariants (not ingested; the code is inert until MIK-R37):**

1. **A card excerpt comes only from the pinned tree's exact blob, bounded, with per-side state.** Realized by
   `_placed`, `_in_blob`, `_excerpt`, `_change`. Proved by the cards-read cases in `test_review_git_trees.py` and the
   reviewer's `git cat-file` check on both sides of RLZ-CXH58B4W.
2. **Focused cards group expressions by (path, range) with the rationale directly above the excerpt, and a missing
   rationale is shown as a gap.** Realized in the dashboard (`focusedCards.ts`, `ExpressionCards.tsx`); proved by
   `ExpressionCards.test.tsx` and the real-data surface case.
3. **A bounded roster never reads as the whole family: the cards state the loaded n of m.** Realized by
   `cardScope` and `ScopeLine`; proved by the F2 and R2-5 cases.
4. **Card planning marks come only from a leaf-wide read of the same comparison.** Realized by the numbered-read
   pinning here and `FamilyReviewCenter.pinnedWorklist`; proved by the route case and the R2-3 surface case.
5. **Dataset reviews make no tree read.** Realized by the payload's `review:trees:<n>` token gating every tree
   read in the dashboard; proved by the surface's dataset case and the reviewer's mutation (15 tests fail when the
   gate is forced). The server side is unchanged for unconverted leaves (26 of 29 unconverted reads byte-identical;
   the 3 others were the `ValidationError`).

| Finding | Anchor | Source |
| --- | --- | --- |
| Every entry of the named invariants on B and C. | `tree_entries` | mcp/src/agents_remember/application/review_tree_entries.py:65-85 |
| Where an entry lands, and its bounded excerpt. | `_placed`; `_in_blob`; `_excerpt` | mcp/src/agents_remember/application/review_tree_entries.py:175-183; mcp/src/agents_remember/application/review_tree_entries.py:186-208; mcp/src/agents_remember/application/review_tree_entries.py:211-225 |
| The cards view (answered through `_focused` since MIK-L32, which replaced `_entries_view`), the pinned comparison, and the one wire casing. | "return _focused(query, trees, entries=tree_entries(trees, query.invariants))"; `snake_keys`; "def _comparison(" | mcp/src/agents_remember/application/review_tree_knowledge.py:126-127; mcp/src/agents_remember/application/review_tree_knowledge.py:233-240; mcp/src/agents_remember/application/review_tree_knowledge.py:131-152 |
| History rows by the item's subject and its `facts.row`. | `_row_subjects` | mcp/src/agents_remember/application/review_tree_knowledge.py:552-558 |
| A proof entry links its path in a tree index. | `_proof_at_path` | mcp/src/agents_remember/application/review_source_realization_link.py:298-314 |
| The over-length unreadable-owner detail summarised; a fitting one kept. | `_unreadable_detail` | mcp/src/agents_remember/application/review_curator_records.py:82-90 |

## 260928-MIK-L29 The Path-Based Knowledge Reader: One Read-Only Question Per Call, At Any Memory Tree

**New sub-package (MIK-R29): [`knowledge_reader/`](knowledge_reader/__init__.py.md).** The dashboard's Knowledge area
asks one read-only question per call, addressed by repository, memory tree and path or record ID, and needs no
task. The package has no route overview of its own, following the `knowledge_leaf/`, `knowledge_paging/` and
`knowledge_worklist/` precedent: this section governs its eight cards.

- [`__init__.py`](knowledge_reader/__init__.py.md): `read_knowledge_reader` and its nine views; the envelope
  (`view`, `state`, `selection`), `invalid-request` for a bad request, `unavailable` for a named read failure. An
  answer's own `selection` block overrides the default, which is how a resumed subtree page names the tree it measured
  (R3-1).
- [`selection.py`](knowledge_reader/selection.py.md): `published` (MIK-R23 rule 6's selection), a memory commit by its
  hexadecimal name (a Git-tree index), or `leaf:<scope>`; `not-converted` before any index is built; the code tree (a
  commit's `Code-Commit` pairing, or `HEAD` of the scope's checkout), `codeSource`, `codeNote` and the clean-tree
  `pinnedCommit`; the selector's choices with `commitsState`.
- [`files.py`](knowledge_reader/files.py.md): memory prose and sidecars, code listings and text; present, absent and
  unavailable kept apart; control characters refused before any Git call (F15); the blob size asked before its bytes,
  `binary` and `too-large` notices (F14); a directory given to the code view is `absent` (F18).
- [`paths.py`](knowledge_reader/paths.py.md): the explorer with live entry counts; the path view (prose with resolved
  references, entries by invariant with MIK-R03 states, member and routed families with their other locations,
  linking records with a decision in full); a directory bounded to its own level with its children and subtree size
  (F2); the without-proof list; `states_at`, the reader's one currentness call.
- [`subtree.py`](knowledge_reader/subtree.py.md): every live entry under a directory, paged by L02's pager and
  continuation under policy `knowledge-reader-subtree/1`, the envelope counted inside the bound; a resumed page
  measures at the walk's code tree (F16), and a tree the repository no longer holds is refused by name (R3-2).
- [`records.py`](knowledge_reader/records.py.md): summaries, a decision in full through L13's helpers (the rule carried
  from L13), links and numbered references with every target.
- [`truth.py`](knowledge_reader/truth.py.md): truth views per kind with links both ways (unreadable links named, F11),
  the census view through L20's report, the record list, and the code view at a locator (a malformed locator is a 400,
  F3).
- [`timeline.py`](knowledge_reader/timeline.py.md): the three-source timeline, newest first, over the converted history
  only; `-G` without `--pickaxe-all` (F1); `moved` against `re-anchored` (F5); a bounded cache of complete timelines
  keyed by tree (F7).

The reader reuses the landed read paths and re-derives none: L23's selection and `KnowledgeIndexCache.for_git_tree`,
L03's `invariant_currentness`, L05's `select_chain`, L13's decision helpers, L20's census report, L28's
`invariants_without_proof` and L08's `CodeTrees.resolve`. The only write is L23's derived-index cache under the
coordination runtime (ruling Q2).

**Rulings** (`29_path-based-knowledge-reader.json`). Carried from L13 (01:45:56): a decision's chosen and rejected
alternatives and its derived superseded status are shown whole in every view. 09:42:58: Q1/N1 the code tree per
selection (memory commit: its `Code-Commit` pairing; `published` and a leaf: `HEAD` of the checkout, matching L03;
revisit with L03 gap 1) and every answer names `codeTree`, `codeSource` and `codeNote`; Q2 the index cache is L23's
design; Q3-Q10 accepted as built; N2 the pinned link; F1-F14 as listed above (F10 accepted as a note). 10:44:14: F15,
F16, F17 (four mutant tests), F18, and the "more" in-flight guard. 11:24:12: pass-with-notes; R3-1 and R3-2; unsigned
tokens stay as L02 designs them.

**Candidate invariants (not ingested; the code is inert until MIK-R37):**

1. **The reader never writes a repository; it reads from the derived index and Git objects only.** Realized by the
   GET-only route and the read-only calls in `selection.py`, `files.py` and `timeline.py`; proved by
   `test_the_route_serves_every_view_and_the_reader_writes_nothing` and the published-tree snapshot case (refs,
   status, object counts and the index file unchanged), and by the worker's and reviewer's real-data snapshots.
2. **Every reader answer names the code tree it measured and its source.** Realized by
   `ReaderSelection.to_document` in the envelope and the subtree page's measured selection block; proved by the
   selection cases and `test_a_subtree_walk_measures_every_page_at_the_code_tree_it_began_at`.
3. **A directory view is bounded, and the full subtree is paged by a continuation bound to tree, policy and path; a
   resumed page measures at the walk's tree.** Realized by `path_view`, `_directory_summary`, `subtree_page`,
   `_resume` and `_at_walk_tree`; proved by the directory and subtree cases (every whole answer within the bound,
   another walk refused, page 2 at page 1's tree after a code commit) and the real root walk (179 entries, 2 pages).
4. **A failed source is shown as partial or unavailable, never as empty.** Realized by `FileRead`, `indexState` and
   `problems`, `commitsState`, `outgoingState`, `unverifiableReason` and the per-source timeline states; proved by
   `test_a_partial_index_and_an_unavailable_code_tree_are_named_where_they_apply`, the failed-timeline and
   unreadable-links cases, and the dashboard's failure cases.
5. **Unconverted memory reads are unchanged.** Realized by `not-converted` before any index is built; proved by
   the unconverted comparison (the landed routes byte-identical base against worktree, `4ab45ec3…` on `b54d1b03`) and
   no index created on an unconverted tree.

| Finding | Anchor | Source |
| --- | --- | --- |
| The entry point, its views and the envelope. | `READER_VIEWS`; `read_knowledge_reader` | mcp/src/agents_remember/application/knowledge_reader/__init__.py:56-66; mcp/src/agents_remember/application/knowledge_reader/__init__.py:72-89 |
| The three tree spellings and the code tree each measures at. | `open_selection`; `_checkout_code_tree`; `_paired_code_tree` | mcp/src/agents_remember/application/knowledge_reader/selection.py:167-187; mcp/src/agents_remember/application/knowledge_reader/selection.py:281-292; mcp/src/agents_remember/application/knowledge_reader/selection.py:295-309 |
| The bounded path view and the paged subtree at the walk's tree. | "def path_view("; "def subtree_page("; "def _at_walk_tree(" | mcp/src/agents_remember/application/knowledge_reader/paths.py:142-175; mcp/src/agents_remember/application/knowledge_reader/subtree.py:62-109; mcp/src/agents_remember/application/knowledge_reader/subtree.py:116-144 |
| A decision in full; the three-source timeline. | `decision_document`; `record_timeline` | mcp/src/agents_remember/application/knowledge_reader/records.py:119-157; mcp/src/agents_remember/application/knowledge_reader/timeline.py:83-106 |

## 260928-MIK-L14 Reconsideration Surfacing: A Changed Ground Reopens A Rejected Alternative

**Route meaning extended (MIK-R14).** The worklist gains a registrant and the curator writer gains a row kind, so a
decision's rejected or deferred alternative comes back up when a target its `reconsider_on` link names changes in a
leaf, and the curator records a judgment on it. Three new modules, each carded and governed here:

- [`knowledge_worklist/reconsideration.py`](knowledge_worklist/reconsideration.py.md): step 8 of the run. Every K_B
  decision's links (L13's `reconsider_links`) are evaluated on the packet's triggers: `record_file`, `history_row`
  (for a `route:` target only a row that reroutes, retires or deletes it, ruling 04:37:56 Q1), `anchor` (the run's
  own classifier through `classify.classify_anchor`, like an entry but never one), `anchor_stale` (review F3), and
  `requirement_version` (L13's resolver, then the owning task's manifest; facts carry `latestApproved` and
  `latestPacket`, F4). A decision target never fires (one hop), and a superseded decision is skipped and listed
  (Q5). One item per changed alternative, with `satisfiedBy` from the stored predicate, and a `reconsideration.links`
  summary of every evaluated link.
- [`knowledge_writer/reconsideration.py`](knowledge_writer/reconsideration.py.md): what a row's subject names, the
  `raise` question, and the `still_rejected` refresh. Only the fired links are refreshed (F1), to the judged state:
  a requirement re-pointed to the item's version and packet, an anchor mapped through the diff by the carry's
  `mapped_anchor`. Each fired K_C link is judged against its K_B target: unchanged (refreshed, one revision bump per
  leaf through the record path, F2), carried (an earlier refresh that still stands; written with no further bump,
  and a plain rerun writes identical bytes, R3-1 and R4-1), a new change (an earlier version or an anchor changed
  again: a plain rerun is refused naming the new item, and a row naming it in `items` is a new judgment, R4-3,
  R5-1 and the explicit answer of 10:39:15), a stale item (the worklist predates the change: recompute, 11:24:12),
  or re-authored (refused, N1, R5-2).
- [`knowledge_writer/open_questions.py`](knowledge_writer/open_questions.py.md): a `raise` row's question appended to
  the leaf task document's `openQuestions` through `task_doc`, preserving every existing question; a dry run when
  the row is authored, the append in a committing run before any file (`writer._append_raised`).

Touched modules: `knowledge_worklist/compute.py` (step 8, the classifier bound once), `classify.py`
(`_classify_anchor` split out, moved code), `leaf.py` and `__init__.py` (the coordination root, the kind);
`knowledge_writer/authoring.py` (`_reconsideration_row`, `_raise`, `_refresh`), `writer.py` (`worklist` and
`questions` on the request) and `carry.py` (the public `mapped_anchor`, the carry unchanged).

- **Rulings recorded here:** 01:45:56 (L13's carries: the resolver reused; index stability guarded by
  `R14.1-linked-alternative-order` in `memory_quality`), 04:37:56 Q1 to Q8 (Q4 and Q7 are recorded limits),
  05:31:11 F1 to F10 (F10 carried to L37), 06:17:11 N1 to N4, 07:13:54 with the 09:18:48 reconciliation (R3-1, one
  ruling with the duplicate N5), 10:05:18 and 10:39:15 (R4), 11:01:18 and 11:24:12 (R5), and 11:53:13 (R6 notes,
  including R6-1: a same-leaf revert after a refresh raises `anchor_stale` once in the next leaf, loud not silent).
- **Candidate invariants (not ingested):** (1) a `reconsider_on` link fires only on the packet's triggers, one hop
  only, and an unresolved endpoint or a task without a manifest never fires; (2) every new change to a judged target
  needs a new explicit answer, a rerun of the same answer is idempotent, and nothing absorbs an unjudged change;
  (3) `still_rejected` refreshes only the fired link, to the judged state mapped through the diff, and refuses a link
  that was re-authored or cannot be mapped; (4) `raise` puts the question in the task document before any knowledge
  file is written, and on failure writes nothing; (5) a linked alternative cannot be reordered to another index
  (R14.1); (6) unconverted memory reads are unchanged.
- **Inert before MIK-R37:** the registrant runs only inside a converted leaf's worklist and the rows only through the
  file writer; the real unconverted L14 contract gives `None` on the base and L14 builds.

| Finding | Anchor | Source |
| --- | --- | --- |
| The registrant's docstring: what is read, the triggers and the items. | "item kind: a decision whose reconsider target changed" | mcp/src/agents_remember/application/knowledge_worklist/reconsideration.py:1-39 |
| Step 8 in the run, with the run's own classifier. | "reconsideration = reconsideration_candidates("; "classifier = Classifier(inputs.code, inputs.base, renamed)" | mcp/src/agents_remember/application/knowledge_worklist/compute.py:237-238; mcp/src/agents_remember/application/knowledge_worklist/compute.py:259-275 |
| The link states a fired link is judged by. | `_link_state`; `_requirement_state`; `_anchor_state` | mcp/src/agents_remember/application/knowledge_writer/reconsideration.py:349-363; mcp/src/agents_remember/application/knowledge_writer/reconsideration.py:366-391; mcp/src/agents_remember/application/knowledge_writer/reconsideration.py:400-423 |
| The `still_rejected` refresh and the `raise` in the authoring step. | `_refresh`; `_raise` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:828-871; mcp/src/agents_remember/application/knowledge_writer/authoring.py:893-921 |
| The question through `task_doc`. | `TaskDocOpenQuestions` | mcp/src/agents_remember/application/knowledge_writer/open_questions.py:38-87 |
| The questions reach the task document before any file. | `_append_raised` | mcp/src/agents_remember/application/knowledge_writer/writer.py:167-173 |
| The carry's mapping, reused by the refresh. | `mapped_anchor` | mcp/src/agents_remember/application/knowledge_writer/carry.py:33-55 |

## 260928-MIK-L32 The Unexplained-Changes Lane: One Classification Of Changed Files And Hunks, Shared With The Gate

**Route meaning extended (MIK-R32, adopting ICR-R33@v1 with substitutions).** Changed source that no recorded entry's
range intersects becomes a first-class review destination, with its file count at the reviewer entry and its changed
lines classified per hunk. This route supplies the one classification and its three reads. Two new modules, each
carded and governed here:

- [`review_lane_classification.py`](review_lane_classification.py.md): the one classification of a tree
  comparison's changed paths (`TreeLane`, `open_tree_lane`). It has no hunk arithmetic of its own: hunks from
  `change_hunks` (definition 2), ranges from `CodeTrees.resolve` reached **only at the entry's recorded blob**
  (definition 3, `exact_recorded_blob`), intersection through `hits_old`/`hits_new` on the sides where a hunk changes
  lines, and a non-text change's gate linkage through `non_text_linked` (definition 8). Buckets: *attributed* (an
  entry supplies a range on a side), *unexplained* (no entry on either side, both read), *attribution unknown*
  (otherwise). Hunks: *linked*, else *attribution unknown* (an unread side, or entries that supply no range), else
  *unexplained*. Proof entries link like realizations. Reasons are bounded (ten named entries, clipped details).
- [`review_unexplained_lane.py`](review_unexplained_lane.py.md): `lane_summary` (the entry's count, file buckets
  only), `unexplained_lane` (the `Unexplained changes` and `Unknown attribution` destinations, the totals and every
  path's bucket) and `classify_changed_path` (the per-file response with links, invariant revisions, their keys and
  family occurrences with membership states, or a typed refusal).

Touched modules:
- `knowledge_worklist/code.py`: `change_hunks`, moved verbatim out of `compute._Run._path_hunks`;
- `knowledge_worklist/compute.py`: `_path_hunks` and `_file_covered` call `change_hunks` and the exported
  `non_text_linked`, so the gate and the lane share both definitions; the gate's output is unchanged;
- [`review_tree_knowledge.py`](review_tree_knowledge.py.md): `lane=files` and `file=<path>` dispatched through
  `_focused` (which replaces L31's `_entries_view`) and `_file_view`; every focused read reopens its comparison;
  MIK-R25's worklist view stays in the leaf-wide view;
- [`review_intent_summary.py`](review_intent_summary.py.md): a tree comparison's summary carries `attribution`, the
  lane's count, in the same request.

- **Rulings recorded here.** PS-1 (history rows by `facts.row`) was already fixed by L31 and is not repeated.
  2026-09-30T12:19:20: Q1 on tree comparisons the source explorer takes the lane's buckets (`paths`), so the explorer
  and the lane never disagree; dataset reviews keep the landed accounting; Q2 the exact-blob rule is the packet's
  (entries recorded at an older blob read unknown until re-recorded; 47 of 178 converted real entries, 18 files),
  carried to L37 as a check item; Q3 a gate-held non-text change is listed under `Unexplained changes` only for an
  attributed file, otherwise under `Unknown attribution` marked "gate unexplained"; Q4 an unexplained hunk in a file
  of unknown attribution stays in that file's `Unknown attribution` row (rule 10); Q5 the membership-state mapping is
  accepted and L34 may refine it (L34 kept it as mapped); Q6 the entry count shows even when the intent counts are refused (it is read from
  the trees directly); Q7 a rename counts as a deletion plus an addition, as in the gate. 13:07:38 (review R1
  pass-with-notes): F1 on tree comparisons the technical details follow the lane too; F2 `file=` values up to the
  route's 4,096 characters answer the typed 200 refusal, `offending_input` clipped; F3 the lane's gate linkage is
  `unknown`, never "gate unexplained", when either side's index has parse problems; F4 bounded reasons; F5 carried to
  L34 (markers for neighbouring hunks inside a focused window) and resolved there: every hunk a lane window draws
  carries its own intent mark; F6 notes accepted. Review R2: pass. Sync: L35's
  word-diff surface test was rerun on the L35-synced tree and passes.
- **Candidate invariants (not ingested; no speculative ingestion):**
  1. The reviewer classifies changed files and hunks through MIK-R08's definitions only: one classification shared
     with the gate (`change_hunks`, `CodeTrees.resolve`, `hits_old`/`hits_new`, `non_text_linked`).
  2. An entry supplies a range only when a side's blob is exactly its recorded blob (`TreeLane._place`).
  3. On tree comparisons, the explorer and the technical details take their attribution from the lane, so no two
     surfaces disagree (`paths`; the dashboard's `explorerAttribution` and `laneAttributionFacts`).
  4. The lane says unknown when the gate could not be computed, and never "gate unexplained" (`_gate`, both sides
     `complete`).
  5. Lane reads are bounded and validated; every answer to a validated request is typed (the route's bounds,
     `_refusal`'s clipped input, bounded reasons, `unavailable` instead of a traceback).
- **Inert before MIK-R37:** only a converted leaf's tree comparison reaches the lane; a dataset review makes no lane
  read, and 29 of 29 unconverted reads are identical to base once the new null `attribution` field is dropped (the
  served body omits it, `exclude_none`).

| Finding | Anchor | Source |
| --- | --- | --- |
| The one classification: where it differs from the gate, stated once. | "An entry supplies a range on a side only at its own recorded blob." | mcp/src/agents_remember/application/review_lane_classification.py:1-33 |
| The exact-blob rule and the hunk classes. | `_place`; `_classified` | mcp/src/agents_remember/application/review_lane_classification.py:286-312; mcp/src/agents_remember/application/review_lane_classification.py:491-499 |
| The gate's non-text linkage, unknown over a side not read whole (F3). | `_gate` | mcp/src/agents_remember/application/review_lane_classification.py:519-534 |
| The three reads. | `lane_summary`; `unexplained_lane`; `classify_changed_path` | mcp/src/agents_remember/application/review_unexplained_lane.py:87-110; mcp/src/agents_remember/application/review_unexplained_lane.py:129-155; mcp/src/agents_remember/application/review_unexplained_lane.py:226-244 |
| The shared hunk and non-text definitions. | `change_hunks`; `non_text_linked` | mcp/src/agents_remember/application/knowledge_worklist/code.py:337-356; mcp/src/agents_remember/application/knowledge_worklist/compute.py:592-598 |
| The lane and file reads dispatched; a focused answer. | "return _focused(query, trees, lane=unexplained_lane(trees))"; "def _file_view(" | mcp/src/agents_remember/application/review_tree_knowledge.py:122-127; mcp/src/agents_remember/application/review_tree_knowledge.py:216-230 |
| The entry's count on the summary. | "return summary.model_copy(update={\"attribution\": lane_summary(resolved.trees)})" | mcp/src/agents_remember/application/review_intent_summary.py:139-142 |

## Update History
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): **route body updated.** Added the section "260928-MIK-L22 The Default Worktree Services Bind The Knowledge Validator": the default composition binds `GitKnowledgeValidation` to the worktree layer's new `KnowledgeValidationPort`, and is the only place it is bound. No verification stamp was advanced.
- 2026-09-28T17:14:56+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): **route body updated — the changed-intent summary and the shared pair preflight (`ICR-R24@v3`).** New section appended at the end (appended rather than inserted, so the line-cited parts of this overview do not move). Displaced rows into `knowledge_review.py` were re-pointed from the base-to-candidate line mapping. No stamp advanced.
