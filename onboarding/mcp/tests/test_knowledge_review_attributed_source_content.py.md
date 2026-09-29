# mcp/tests/test_knowledge_review_attributed_source_content.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_review_attributed_source_content.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T17:20:02+02:00 |
| lastVerifiedCommitHash | `e40c314ca55305f7e4334b4e8e16a10297f6f175`|
| lastVerifiedCommitDate | 2026-09-29T18:13:06+02:00|
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

**The eight cases:**

| Case | Property |
| --- | --- |
| `test_an_unchanged_path_a_recorded_realization_links_opens_as_context_without_counting` | both-snapshot and before-only links admit; each side is the pair's own blob; re-listing gives the same entries and `listed_total` |
| `test_an_unchanged_path_no_recorded_realization_links_is_still_refused` | an unlinked unchanged path refuses, naming both snapshots' answers |
| `test_a_path_linked_only_in_another_comparison_is_refused_for_this_one` | an earlier generation's link does not admit the path into the current pair; the earlier pair still opens it from its own record |
| `test_after_the_live_tree_moves_the_listed_pair_keeps_its_exact_attributed_bytes` | the frozen pair serves its historical bytes; an unrecorded superseded pair refuses rather than using current knowledge; the rewritten path becomes an ordinary change |
| `test_a_closed_leaf_opens_its_attributed_path_from_the_retained_generation` | with the worktree group removed, the retained generation admits exactly the same paths |
| `test_a_padded_spelling_is_never_admitted_as_attributed_context` | four whitespace paddings of a linked, an unlinked and a changed path all refuse (L43-R1-F1) |
| `test_a_selection_bound_below_the_scope_cannot_refuse_a_linked_path` | with `SELECTION_ITEM_LIMIT=1` the scope read refuses, yet the linked path still opens (L43-R1-F2) |
| `test_an_unreadable_snapshot_leaves_the_link_undetermined_rather_than_absent` | a corrupt after half: a before-linked path still opens; an unlinked path refuses as undetermined, never with the established-negative sentence (L43-R1-F2) |

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
| The lane marker, the three population paths and the two refusal constants. | `pytestmark`; `ATTRIBUTED_PATH`; `BEFORE_ONLY_PATH`; `UNRELATED_PATH`; `_PADDINGS`; `_NOT_LINKED` | mcp/tests/test_knowledge_review_attributed_source_content.py:58-58; mcp/tests/test_knowledge_review_attributed_source_content.py:61-61; mcp/tests/test_knowledge_review_attributed_source_content.py:63-63; mcp/tests/test_knowledge_review_attributed_source_content.py:65-65; mcp/tests/test_knowledge_review_attributed_source_content.py:67-67; mcp/tests/test_knowledge_review_attributed_source_content.py:69-69 |
| Fixture and helpers: fresh enclosure with knowledge halves, freeze, refusal and attributed assertions. | `attributed_fixture`; `_freeze`; `_refused`; `_attributed` | mcp/tests/test_knowledge_review_attributed_source_content.py:72-76; mcp/tests/test_knowledge_review_attributed_source_content.py:79-85; mcp/tests/test_knowledge_review_attributed_source_content.py:92-99; mcp/tests/test_knowledge_review_attributed_source_content.py:102-109 |
| **Attributed admission without counting, and the unlinked refusal.** | `test_an_unchanged_path_a_recorded_realization_links_opens_as_context_without_counting`; `test_an_unchanged_path_no_recorded_realization_links_is_still_refused` | mcp/tests/test_knowledge_review_attributed_source_content.py:117-150; mcp/tests/test_knowledge_review_attributed_source_content.py:153-164 |
| **Comparison isolation and historical bytes.** | `test_a_path_linked_only_in_another_comparison_is_refused_for_this_one`; `test_after_the_live_tree_moves_the_listed_pair_keeps_its_exact_attributed_bytes`; `test_a_closed_leaf_opens_its_attributed_path_from_the_retained_generation` | mcp/tests/test_knowledge_review_attributed_source_content.py:167-197; mcp/tests/test_knowledge_review_attributed_source_content.py:200-247; mcp/tests/test_knowledge_review_attributed_source_content.py:250-269 |
| **The two review-fix cases: exact spelling, and a link scope size cannot fail or an unread half cannot negate.** | `test_a_padded_spelling_is_never_admitted_as_attributed_context`; `test_a_selection_bound_below_the_scope_cannot_refuse_a_linked_path`; `test_an_unreadable_snapshot_leaves_the_link_undetermined_rather_than_absent` | mcp/tests/test_knowledge_review_attributed_source_content.py:272-296; mcp/tests/test_knowledge_review_attributed_source_content.py:299-323; mcp/tests/test_knowledge_review_attributed_source_content.py:326-350 |
| The population paths the fixture's knowledge links. | `INTEGRATION_PATH`; `RESOLUTION_PATH`; `UNPARSED_PATH` | mcp/tests/read_scope_test_support.py:115-115; mcp/tests/read_scope_test_support.py:119-119; mcp/tests/read_scope_test_support.py:125-125 |
| The lane row and the read-scope consumer row this module adds. | "mcp/tests/test_knowledge_review_attributed_source_content.py" | mcp/tests/test-evidence-lanes.toml:135-135; mcp/tests/evidence-lifecycle.toml:1523-1523 |
| The owners under test. | `admit_source_path`; `recorded_realization_link` | mcp/src/agents_remember/application/review_source_admission.py:86-128; mcp/src/agents_remember/application/review_source_realization_link.py:109-152 |

## Cross-Repo References

No cross-repository behavior is measured in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): No content impact: citation ranges only. MIK-R08 moved lines in `evidence-lifecycle.toml`, `test-evidence-lanes.toml`, and the rows here that cite them were re-pointed to the same constructs (by the installed `memory-citations --fix` where it could regenerate a range, and otherwise by the exact base-to-candidate line map). No claim, anchor or source file of this card changed.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`mcp/tests/evidence-lifecycle.toml` and `mcp/tests/test-evidence-lanes.toml`) were re-pointed by the exact base-to-working line map (multi-anchor rows the installed fixer declined); no claim wording changed. No verification stamp was advanced.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`evidence-lifecycle.toml`, `test-evidence-lanes.toml`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.
- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): No content impact: re-pointed 2 citations into `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml` through the exact base-to-candidate line map after this leaf's behaviour-preserving splits and catalog/lane/pin repairs; each moved range cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): created this card for the new evidence module of the attributed unchanged source-content admission — five A1 cases plus the three R1-fix cases (padded spelling, lowered selection bound, unreadable half). Verification stamp names the code base; the module exists only in the uncommitted candidate and closeout owns the real stamp.
