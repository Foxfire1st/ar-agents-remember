# mcp/src/agents_remember/application/review_source_realization_link.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_source_realization_link.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T04:01:40+02:00 |
| lastVerifiedCommitHash | `8a2d4b478971bf40cca0f24d5e5d24a0844bd563`|
| lastVerifiedCommitDate | 2026-09-30T04:16:14+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

Answers one question for the source-content admission owner: **does a realization recorded in the
knowledge this comparison binds link this exact path?** It reads no source bytes and decides nothing
else; `application/review_source_admission.py` turns the answer into an admission or a refusal.

It exists because a statement can be realized by code the task did not change. The inventory stays
exactly the measured change set, and a reviewer still has to be able to read that unchanged code — but
only when **this** comparison's own recorded knowledge points at it (ICR-R03@v1 under the 2026-09-28
admission ruling, with R26 subject/comparison isolation preserved).

## Code Commentary

### Logic

**Which comparison's knowledge (`_bound_knowledge`).** The baseline is already required to be the
leaf's recorded base, so only the after tree can differ. When the requested after tree is the
candidate the leaf's review binds now, the knowledge is that same resolution's two halves (a live
leaf's halves, or a closed leaf's reopened generation). Otherwise the pair is superseded: the leaf's
published comparison generations are walked newest-first (`read_generation_refs`), the first whose
manifest records exactly the requested pair is reopened through `resolve_committed_leaf_review`, and
its retained halves answer. With no such generation the answer is a **determined** "no knowledge is
bound to the requested comparison" — the knowledge the leaf holds now is never substituted. A
generation that records the pair but cannot be reopened is **undetermined**.

**Which halves (`_halves`).** Before and after, except that a half a closed leaf's generation manifest
did not retain is left out rather than looked for elsewhere.

**Which spelling (`_anchor_spelling`).** The requested path must validate as a `PathSeed` **and** the
validated value must equal the request string. The seed rule strips surrounding whitespace, so without
the equality a padded spelling (`" src/x.py"`, a trailing tab or newline) would be answered with the
link of the path it normalizes to (L43-R1-F1). A non-anchor spelling is a determined negative.

**One half's answer (`_side_reading`).** The snapshot's identity is resolved from the file with
`open_read_context`, then the read owner's exact claim-at-path query `fetch_realizations_at_path` is
run on a read-only connection. That query expands no family, so the selection bound that caps scope
reads cannot turn a linked path into a refusal (L43-R1-F2). A missing file or a storage, SQLite, OS
or value error while resolving or querying makes the half `unread` with its cause; a row is `linked`;
no row is `not_linked`.

**The answer (`RealizationLink`).** `linking_sides` names the halves that link the path; `detail` is
one sentence naming the comparison and what each half answered (`_sentence`), which the admission
owner carries verbatim into its admission detail or refusal. `determined` is false exactly when no
half links the path and some bound knowledge was not read — one established link is enough to admit.

### Conventions

`__all__` publishes `RealizationLink` and `recorded_realization_link`. Intermediate values
(`_SideReading`, `_BoundKnowledge`) are frozen dataclasses, not wire models. The module re-uses
existing owners (knowledge read, committed-leaf reopen, generation refs/manifest, namespace record)
and adds no store, schema or second reader; the direct `fetch_realizations_at_path` use follows the
same two-step pattern as `application/review_attribution.py`.

### Invariants And Boundaries

- **Only the requested comparison's knowledge answers.** Current pair → the resolution's halves;
  superseded pair → only a generation that recorded exactly that pair; otherwise nothing. No other
  leaf, master or published dataset is consulted.
- **Exact spelling only.** A path is linked only for the exact string a recorded anchor carries.
- **Anchor staleness is not a criterion.** A recorded anchor whose blob no longer matches still links
  its path for reading (Architect ruling closing L43-R1-F4 (1)); the content read beside it shows the
  bytes the requested endpoints actually hold.
- **Unreadable knowledge supports no admission and no negative.** It yields an undetermined answer
  with its cause.
- **Two connections, no mislabel.** Identity is checked in one read-only connection and the claim
  query runs in a second; R2 judged every file-swap interleaving to be at worst a false refusal, never
  an admission of an unlinked path.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of which comparison, which fact, what is not a criterion, and why unreadable knowledge is undetermined.** | "Which comparison."; "What is not a criterion." | mcp/src/agents_remember/application/review_source_realization_link.py:1-38 |
| The published surface and the half order. | `__all__`; `_SIDES` | mcp/src/agents_remember/application/review_source_realization_link.py:66-66; mcp/src/agents_remember/application/review_source_realization_link.py:69-69 |
| **The answer value: linking halves, the stated sentence, and whether the negative was established.** | `RealizationLink` | mcp/src/agents_remember/application/review_source_realization_link.py:74-91 |
| **The entry point: bind the comparison, check the spelling, read the namespace, ask each half.** | `recorded_realization_link` | mcp/src/agents_remember/application/review_source_realization_link.py:109-152 |
| **Exact-spelling check: the validated seed must equal the request string.** | `_anchor_spelling` | mcp/src/agents_remember/application/review_source_realization_link.py:155-166 |
| **Comparison binding: current pair, recorded superseded pair, or nothing — never the leaf's current knowledge.** | `_bound_knowledge` | mcp/src/agents_remember/application/review_source_realization_link.py:172-232 |
| Halves a closed leaf's generation did not retain are not read. | `_halves` | mcp/src/agents_remember/application/review_source_realization_link.py:235-246 |
| **One half asked by the exact claim-at-path query, with unreadable kept apart from not linked.** | `_side_reading`; `_sentence` | mcp/src/agents_remember/application/review_source_realization_link.py:252-276; mcp/src/agents_remember/application/review_source_realization_link.py:279-285 |
| The read owner's identity resolution and exact claim-at-path query this module re-uses. | `open_read_context`; `fetch_realizations_at_path` | mcp/src/agents_remember/application/knowledge_read.py:108-141; mcp/src/agents_remember/memory/knowledge/read_queries.py:226-260 |
| The generation owners that bind a superseded pair to its retained knowledge. | `read_generation_refs`; `read_manifest`; `task_root_for_review`; `resolve_committed_leaf_review` | mcp/src/agents_remember/application/review_comparison_generation.py:615-649; mcp/src/agents_remember/application/review_comparison_generation.py:725-753; mcp/src/agents_remember/application/review_comparison_generation.py:564-572; mcp/src/agents_remember/application/review_committed_leaf.py:174-216 |
| The namespace record (the record beside the bytes, or, since MIK-R25, a derived knowledge index's own namespace) and the path-seed shape rule. | `review_namespace`; `PathSeed` | mcp/src/agents_remember/application/review_candidate_resolution.py:391-430; mcp/src/agents_remember/models/knowledge/read.py:128-155 |
| **Cases: cross-comparison refusal, recorded historical bytes after the tree moves, closed leaf, padded spellings, and the lowered selection bound.** | `test_a_path_linked_only_in_another_comparison_is_refused_for_this_one`; `test_after_the_live_tree_moves_the_listed_pair_keeps_its_exact_attributed_bytes`; `test_a_closed_leaf_opens_its_attributed_path_from_the_retained_generation`; `test_a_padded_spelling_is_never_admitted_as_attributed_context`; `test_a_selection_bound_below_the_scope_cannot_refuse_a_linked_path` | mcp/tests/test_knowledge_review_attributed_source_content.py:167-197; mcp/tests/test_knowledge_review_attributed_source_content.py:200-247; mcp/tests/test_knowledge_review_attributed_source_content.py:250-269; mcp/tests/test_knowledge_review_attributed_source_content.py:272-296; mcp/tests/test_knowledge_review_attributed_source_content.py:299-323 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It reads only the knowledge snapshots bound
to one leaf's comparison in one repository namespace.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T04:01:40+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): No content impact on this card's own source, which is unchanged. **Reopened claim re-read and reworded:** `review_namespace` in `review_candidate_resolution.py` gained the derived-index fallback (`_index_namespace`), so the namespace row now names it; its range (`391-430`) was projected by the installed fixer, and the bullet that fixer wrote for this row was removed because the claim was reworded. No verification stamp was advanced.
- 2026-09-28T18:18:00+02:00 — 260921-ICR-L47 curator (post-sync re-measure after the Architect's `worktree_sync` onto code `eda947325ccbe0791973953265278597e968a34a` / memory `6ccb9b615e383174c22f110a6492e6231a4e261f`; L47 candidate tree `5f22717e68041d6819e9671cee2ab30e4d3d3e13`): No content impact: citation ranges into files L44, L45 or L47 moved (`mcp/src/agents_remember/application/review_candidate_resolution.py`, `mcp/src/agents_remember/models/knowledge/read.py`) were re-measured against the post-sync code; each re-pointed row held its anchors in its own measurement tree (`eda94732` or the pre-sync L47 candidate `72efa4bb`) and holds them after the line mapping, or names a literal that occurs exactly once in the post-sync file within five lines of its cited place. Claim wording unchanged. No stamp advanced.
- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): created this card for the new owner of the comparison-bound realization-link question behind attributed unchanged source reads. It records the comparison binding (current pair, exactly recorded superseded pair, or nothing), the exact-spelling rule (L43-R1-F1), the exact claim-at-path query that scope size cannot fail and the undetermined answer for unreadable knowledge (L43-R1-F2), and the Architect ruling that a stale anchor still links. Verification stamp names the code base; the module exists only in the uncommitted candidate and closeout owns the real stamp.
