# mcp/tests/test_review_family_member_sources.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_family_member_sources.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T16:42:25+02:00 |
| lastVerifiedCommitHash | `9b2f775f1ab0fca5f82b4f661785dd8216d4a8b3` |
| lastVerifiedCommitDate | 2026-09-28T17:43:09+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

**Each family member's realization sources carry their own recorded locator and resolved range, measured
through the production path (ICR-R31@v1).** A reviewer needs the exact region each claim attributes, so
these cases pin that every source reference carries the anchor's structured recorded locator, the line
ranges the read's own anchor resolver placed it on in *that side's* exact recorded blob, and the state
naming which of those facts the side established — and that the fields the roster already published keep
their values.

**Every value comes from the production path.** Claims are authored through the store's own realization
operation, the two sides are two real datasets and two real commits in a real Git repository, and the
roster is read through `read_family_roster` with the anchor resolver each side's read context selects. No
case parses a `detail` sentence; ranges are compared with the lines the fixture wrote.

## Code Commentary

### Logic

**One module-scoped fixture, two sides.** `build_sources_fixture` builds the shared read-scope store
(`read_scope_test_support.build_read_scope_fixture`), commits `BEFORE_TEXT` (with `alpha` at lines 1-2 and
`beta` at 5-6) and a second file `src/double.py` defining `alpha` twice, then commits `AFTER_TEXT` (the same
file with `gamma` appended, so the blob changes but `alpha`'s lines do not). It authors seven claims on the
before dataset — two symbol claims on different members in one file, a `line_range`, a `file`, a symbol the
bytes do not define, a range past the blob's end (50-60 of six lines) and the double definition — then
copies that dataset to an after dataset and re-attests `alpha` against the after blob. `roster_sources`
opens one side with `open_family_side`, reads the fixture family with `read_family_roster`, closes the side
and indexes every carried source by claim id.

| Case | What it pins |
| --- | --- |
| `test_two_members_in_one_file_carry_their_own_locators_ranges_and_rationale` | two members in one file are two sources with distinct locators, ranges (1-2 and 5-6), roles and stored rationales; a `line_range` resolves to its recorded range; a `file` locator is `whole_file` with no range; the JSON wire carries the structured values |
| `test_a_changed_file_keeps_its_unchanged_attributed_range_on_each_side` | a changed blob whose attributed lines did not move keeps range 1-2 on both sides, each with its own observed blob |
| `test_an_unresolved_locator_is_stated_with_its_recorded_locator_and_no_range` | an undefined symbol is `unresolved`/`recorded_blob_mismatch` with its recorded locator and no range; claims recorded against the before blob are unresolved on the after side and never placed on the new bytes; a read naming no tree is `not_requested`/`unresolved` for every source |
| `test_a_recorded_range_past_the_blob_end_is_unresolved_with_no_range` | lines 50-60 of a six-line exact blob keep `exact_recorded_blob`, carry no range, are `unresolved`, and the detail states the line count |
| `test_a_symbol_defined_twice_carries_every_defining_range` | a doubly-defined symbol carries both ranges, in order |
| `test_the_existing_source_fields_keep_their_published_values` | the wire is exactly the nine legacy fields plus `locator`, `resolved_ranges`, `locator_state`, and the legacy values — including the `detail` sentence — are unchanged |

### Conventions

- The module is registered in `mcp/tests/test-evidence-lanes.toml` `unit-regression` and carries
  `pytestmark = pytest.mark.evidence_unit`; it is also a registered consumer of the shared
  `read_scope_test_support.py` artifact in `mcp/tests/evidence-lifecycle.toml`.
- Git is driven with real `git` subprocess calls in a temporary directory; no production state is touched.

### Invariants And Boundaries

- **A test here never reads a region out of prose.** The only `detail` assertion is the legacy-value
  equality and the stated line count for the out-of-range case.
- **This is a real-boundary module.** Unlike the value cases in `test_review_family_context_values.py`, every
  source here is produced by the store, the resolver and the roster owner.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The rows name the fixture, the reader and each case, plus the owners they drive.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two texts, their attributed lines, the double definition and the past-end range the fixture writes. | `BEFORE_TEXT`; `ALPHA_LINES`; `PAST_END_LINES`; `DOUBLE_ALPHA_LINES` | mcp/tests/test_review_family_member_sources.py:47-62 |
| **The legacy source fields whose values must not change.** | `LEGACY_FIELDS` | mcp/tests/test_review_family_member_sources.py:66-78 |
| **The fixture: seven before claims, a copied after dataset and the re-attested after claim over two real commits.** | `build_sources_fixture` | mcp/tests/test_review_family_member_sources.py:109-156 |
| **One side's roster read through the production owners, indexed by claim.** | `roster_sources` | mcp/tests/test_review_family_member_sources.py:229-255 |
| Two members in one file, and the line-range and file-locator states. | "test_two_members_in_one_file_carry_their_own_locators_ranges_and_rationale" | mcp/tests/test_review_family_member_sources.py:262-290 |
| The unchanged attributed range on both sides of a changed file. | "test_a_changed_file_keeps_its_unchanged_attributed_range_on_each_side" | mcp/tests/test_review_family_member_sources.py:293-311 |
| Unresolved locators keep their recorded value and carry no range. | "test_an_unresolved_locator_is_stated_with_its_recorded_locator_and_no_range" | mcp/tests/test_review_family_member_sources.py:314-336 |
| A range past the blob end is unresolved on the exact blob. | "test_a_recorded_range_past_the_blob_end_is_unresolved_with_no_range" | mcp/tests/test_review_family_member_sources.py:339-351 |
| A doubly-defined symbol carries both ranges. | "test_a_symbol_defined_twice_carries_every_defining_range" | mcp/tests/test_review_family_member_sources.py:354-361 |
| The legacy fields keep their values. | "test_the_existing_source_fields_keep_their_published_values" | mcp/tests/test_review_family_member_sources.py:364-385 |
| The projection under test. | `member_source` | mcp/src/agents_remember/application/review_family_sources.py:27-51 |
| The resolver that fills the ranges. | `_observed_line_range` | mcp/src/agents_remember/memory/knowledge/read_anchors.py:303-351 |
| The lane registration. | "mcp/tests/test_review_family_member_sources.py" | mcp/tests/test-evidence-lanes.toml:181-181 |
| The shared-fixture consumer registration. | "mcp/tests/test_review_family_member_sources.py" | mcp/tests/evidence-lifecycle.toml:1497-1497 |

## Cross-Repo References

No cross-repository behavior is exercised; the Git repository and datasets are temporary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-28T16:42:25+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): created this one-to-one card for the production-path cases of ICR-R31@v1's member-source locators — distinct regions for two members in one file, an unchanged range on both sides of a changed file, explicit unresolved states, a range past the blob end, a double definition and unchanged legacy fields. The module is untracked at the base commit, so `lastVerifiedCommitHash` names the leaf base and the verified basis is the working-tree delta on top of it; the closeout records the real commit.
