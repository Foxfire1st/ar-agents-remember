# mcp/tests/test_knowledge_review_attributed_source_content.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_review_attributed_source_content.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:56:40+02:00 |
| lastVerifiedCommitHash | `f9e1262283469df895c98dda5b9549a1bbad5b74`|
| lastVerifiedCommitDate | 2026-09-30T13:14:52+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Production-composition evidence for the **attributed unchanged** admission of the review's
source-content route (ICR-R03@v1 under the 2026-09-28 admission ruling): an unchanged file that a
realization recorded in the *same comparison's* knowledge links opens at that comparison's exact
endpoints, and every other unchanged path is still refused. The general confinement case for
arbitrary unchanged paths stays in the sibling `test_knowledge_review_source_content.py` and is kept.

Cases run through the real leaf enclosure and worktree, the real review route's inventory, the real
capture, the real comparison freeze and the real expansion route wired to the real application owner.
Bytes are compared against subprocess Git, never against the owner under test.

## Code Commentary

### Logic

**Fixture and helpers.** `attributed_fixture` builds a fresh live enclosure **with** both knowledge
halves (`build_endpoint_fixture` from the R01 source-endpoint suite); the sibling content suite builds
its own with `datasets=False`. Three paths from `read_scope_test_support` name the populations:
`ATTRIBUTED_PATH` (linked on both snapshots), `BEFORE_ONLY_PATH` (linked only by the before snapshot)
and `UNRELATED_PATH` (linked by neither). `_freeze` publishes the current comparison as a generation;
`_attributed` validates a served body with `ReviewSourceExpansion.model_validate` and asserts
`attributed_unchanged` / `unchanged` / `requested_generation`; `_refused` asserts a 400
`source_content_unresolved` naming the path. The listing, expansion and Git-observation helpers are
imported from the sibling content suite.

**The ten cases:**

| Case | Property |
| --- | --- |
| `test_an_unchanged_path_a_recorded_realization_links_opens_as_context_without_counting` | both-snapshot and before-only links admit; each side is the pair's own blob; re-listing gives the same entries and `listed_total` |
| `test_an_unchanged_path_no_recorded_realization_links_is_still_refused` | an unlinked unchanged path refuses, naming both snapshots' answers |
| `test_a_path_linked_only_in_another_comparison_is_refused_for_this_one` | an earlier generation's link does not admit the path into the current pair; the earlier pair still opens it from its own record |
| `test_after_the_live_tree_moves_the_listed_pair_keeps_its_exact_attributed_bytes` | the frozen pair serves its historical bytes; an unrecorded superseded pair refuses rather than using current knowledge; the rewritten path becomes an ordinary change |
| `test_a_closed_leaf_opens_its_attributed_path_from_the_retained_generation` | with the worktree group removed, the retained generation admits exactly the same paths |
| `test_a_padded_spelling_is_never_admitted_as_attributed_context` | four whitespace paddings of a linked, an unlinked and a changed path all refuse (L43-R1-F1) |
| `test_a_selection_bound_below_the_scope_cannot_refuse_a_linked_path` | with `SELECTION_ITEM_LIMIT=1` the scope read refuses, yet the linked path still opens (L43-R1-F2) |
| `test_an_unreadable_snapshot_leaves_the_link_undetermined_rather_than_absent` | a corrupt after half: a before-linked path still opens, and its admission detail starts "a realization or proof recorded for the path" (ruling Q1's wording, MIK-L31); an unlinked path refuses as undetermined, never with the established-negative sentence, and the damaged half's remedy is still "restore or repair" (L43-R1-F2) |
| `test_never_initialized_knowledge_asks_to_initialize_it` | with no knowledge halves at all (`datasets=False`), the link stays undetermined and the next action starts "initialize this leaf's knowledge", never "restore or repair" (MIK-R31 rule 6, ICR-L43 review R2 O1) |
| `test_a_tree_index_links_a_path_its_proof_entry_is_anchored_at` | an in-memory `ix_entry` with one proof links exactly its path; an index without `ix_entry` (a dataset) links none (MIK-R31 rule 5, ruling Q1) |

### Conventions

`pytestmark = pytest.mark.evidence_unit`. The module is registered in the `unit-regression` lane of
`mcp/tests/test-evidence-lanes.toml` and as a consumer of the `read_scope_test_support.py` artifact in
`mcp/tests/evidence-lifecycle.toml`; an unregistered test module fails the lane-manifest check. Each case
builds its own enclosure under `tmp_path`, and damage (copied halves, a corrupt half, a removed worktree
group) is applied to real artifacts.

### Invariants And Boundaries

- **Production composition only.** No prebuilt expansion or hand-assembled resolution is injected.
- **The inventory is never widened.** The first case asserts re-listing equality after attributed reads.
- **Comparison isolation.** The cross-comparison and moved-tree cases are the falsifiers for current
  knowledge standing in for a superseded comparison's knowledge; the worker's mutation runs broke them.
- **Undetermined is asserted as not absent** by string: `_NOT_LINKED` must not appear in the
  undetermined refusal.
- **Never initialized is asserted as not damaged**: its next action never says "restore or repair".
- The route-level proof admission (review F12) lives in `test_review_git_trees.py`; the unit case here covers the
  dataset side (no `ix_entry`).

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries).

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the admitted population and one case per property.** | "ICR-R03" | mcp/tests/test_knowledge_review_attributed_source_content.py:1-32 |
| The lane marker, the three population paths and the two refusal constants. | `pytestmark`; `ATTRIBUTED_PATH`; `BEFORE_ONLY_PATH`; `UNRELATED_PATH`; `_PADDINGS`; `_NOT_LINKED` | mcp/tests/test_knowledge_review_attributed_source_content.py:60-60; mcp/tests/test_knowledge_review_attributed_source_content.py:71-71; mcp/tests/test_knowledge_review_attributed_source_content.py:63-63; mcp/tests/test_knowledge_review_attributed_source_content.py:65-65; mcp/tests/test_knowledge_review_attributed_source_content.py:67-67; mcp/tests/test_knowledge_review_attributed_source_content.py:69-69 |
| Fixture and helpers: fresh enclosure with knowledge halves, freeze, refusal and attributed assertions. | `attributed_fixture`; `_freeze`; `_refused`; `_attributed` | mcp/tests/test_knowledge_review_attributed_source_content.py:74-78; mcp/tests/test_knowledge_review_attributed_source_content.py:81-87; mcp/tests/test_knowledge_review_attributed_source_content.py:94-101; mcp/tests/test_knowledge_review_attributed_source_content.py:104-111 |
| **Attributed admission without counting, and the unlinked refusal.** | `test_an_unchanged_path_a_recorded_realization_links_opens_as_context_without_counting`; `test_an_unchanged_path_no_recorded_realization_links_is_still_refused` | mcp/tests/test_knowledge_review_attributed_source_content.py:119-152; mcp/tests/test_knowledge_review_attributed_source_content.py:155-166 |
| **Comparison isolation and historical bytes.** | `test_a_path_linked_only_in_another_comparison_is_refused_for_this_one`; `test_after_the_live_tree_moves_the_listed_pair_keeps_its_exact_attributed_bytes`; `test_a_closed_leaf_opens_its_attributed_path_from_the_retained_generation` | mcp/tests/test_knowledge_review_attributed_source_content.py:169-199; mcp/tests/test_knowledge_review_attributed_source_content.py:202-249; mcp/tests/test_knowledge_review_attributed_source_content.py:252-271 |
| **The two review-fix cases: exact spelling, and a link scope size cannot fail or an unread half cannot negate.** | `test_a_padded_spelling_is_never_admitted_as_attributed_context`; `test_a_selection_bound_below_the_scope_cannot_refuse_a_linked_path`; `test_an_unreadable_snapshot_leaves_the_link_undetermined_rather_than_absent` | mcp/tests/test_knowledge_review_attributed_source_content.py:274-298; mcp/tests/test_knowledge_review_attributed_source_content.py:301-325; mcp/tests/test_knowledge_review_attributed_source_content.py:328-353 |
| **The MIK-L31 cases: the never-initialized remedy, and a proof entry's path linked in a tree index but not in a dataset.** | `test_never_initialized_knowledge_asks_to_initialize_it`; `test_a_tree_index_links_a_path_its_proof_entry_is_anchored_at`; "def _proof_at_path(" | mcp/tests/test_knowledge_review_attributed_source_content.py:356-369; mcp/tests/test_knowledge_review_attributed_source_content.py:372-385; mcp/src/agents_remember/application/review_source_realization_link.py:298-314 |
| The population paths the fixture's knowledge links. | `INTEGRATION_PATH`; `RESOLUTION_PATH`; `UNPARSED_PATH` | mcp/tests/read_scope_test_support.py:115-115; mcp/tests/read_scope_test_support.py:119-119; mcp/tests/read_scope_test_support.py:125-125 |
| The lane row and the read-scope consumer row this module adds. | "mcp/tests/test_knowledge_review_attributed_source_content.py" | mcp/tests/test-evidence-lanes.toml:144-144; mcp/tests/evidence-lifecycle.toml:1531-1531 |
| The owners under test. | `admit_source_path`; `recorded_realization_link` | mcp/src/agents_remember/application/review_source_admission.py:86-128; mcp/src/agents_remember/application/review_source_realization_link.py:116-151 |

## Cross-Repo References

No cross-repository behavior is measured in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T12:56:40+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db` plus the staged delta; first curated over `b54d1b03`, then merged with L29's landed curation after the sync onto code `ce459423` / memory `a6075c76`, L29's committed lines kept byte-identical): No content impact: citation-only repair. This card's source is unchanged; MIK-R14 inserted one `unit-regression` row at `test-evidence-lanes.toml:127` (`:126` before the sync onto L29) and one consumer line at `evidence-lifecycle.toml:839`, so every later row of either file moved down by one line. The rows citing those lines that the installed fixer declined were re-pointed by that exact shift (each row byte-identical to memory HEAD, its anchors checked in the base and shifted ranges). No verification stamp was advanced. **After the sync:** its lanes row was moved from this leaf's pre-sync numbering to the synced tree (+1 for L29's row at `:108`), mapped line for line.
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update. The case table records the two new cases (the never-initialized remedy, MIK-R31 rule 6 O1; the proof link in a tree index and none in a dataset, ruling 05:36:19 Q1) and the undetermined case's new assertion of the Q1 wording; the population constants row was re-pointed by the exact +2 import shift. One row added.
- 2026-09-30T05:58:11+02:00 — 260928-MIK-L05 curator (uncommitted change set on `ar/260928-mik-l05`, code base `31d761a241055d67b85ef3908033856b78a86a57` plus the staged and unstaged delta): No content impact: citation-only repair. This card's source is unchanged. Rows citing `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml` were re-pointed to the lines MIK-R05 moved, by the installed fixer or by the exact line shift where it declined (each such row byte-identical to memory HEAD, its anchors checked in the base and the shifted ranges); no claim was reworded.
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; rows citing lane rows after the one `unit-regression` row MIK-R10 inserted at `test-evidence-lanes.toml:124` (or catalog lines after `evidence-lifecycle.toml:836`) were re-pointed by the installed fixer or, where it declined, by the exact line shift over rows byte-identical to memory HEAD. No claim was reworded, so the fixer's bullets are kept. No verification stamp was advanced.
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; MIK-R01 moved lines in `evidence-lifecycle.toml` and `test-evidence-lanes.toml`, so citation ranges into it were projected by the installed `memory-citations --fix` or, for multi-anchor rows it declined, re-pointed by the exact base-to-staged line shift (each such row was byte-identical to memory HEAD).
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): No content impact: citation-only repair. Ranges into `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R11's changes, were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-staged line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): No content impact: citation-only repair. Ranges into `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R02's changes (or normalised by the installed fixer in the same pass), were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-staged line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): No content impact: citation-only repair. Ranges into `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R30's line insertions (or normalised by the installed fixer in the same pass), were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-working line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T19:59:41+02:00 — 260928-MIK-L03 curator (uncommitted change set on `ar/260928-mik-l03`, code base `e40c314ca55305f7e4334b4e8e16a10297f6f175` plus the working-tree delta and untracked files): No content impact: citation ranges only. MIK-R03 moved lines in `evidence-lifecycle.toml` (one consumer at `:832`) and `test-evidence-lanes.toml` (one row at `:112`), and the rows here that cite them were re-pointed to the same constructs (by the installed `memory-citations --fix` where it could regenerate a range, and otherwise by the exact base-to-candidate line map). The fixer also normalised passing ranges in rows that cite files this leaf did not change; those ranges are measurement-true. No claim, anchor or source file of this card changed.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): No content impact: citation ranges only. MIK-R08 moved lines in `evidence-lifecycle.toml`, `test-evidence-lanes.toml`, and the rows here that cite them were re-pointed to the same constructs (by the installed `memory-citations --fix` where it could regenerate a range, and otherwise by the exact base-to-candidate line map). No claim, anchor or source file of this card changed.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`mcp/tests/evidence-lifecycle.toml` and `mcp/tests/test-evidence-lanes.toml`) were re-pointed by the exact base-to-working line map (multi-anchor rows the installed fixer declined); no claim wording changed. No verification stamp was advanced.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`evidence-lifecycle.toml`, `test-evidence-lanes.toml`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.
- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): No content impact: re-pointed 2 citations into `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml` through the exact base-to-candidate line map after this leaf's behaviour-preserving splits and catalog/lane/pin repairs; each moved range cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): created this card for the new evidence module of the attributed unchanged source-content admission — five A1 cases plus the three R1-fix cases (padded spelling, lowered selection bound, unreadable half). Verification stamp names the code base; the module exists only in the uncommitted candidate and closeout owns the real stamp.
