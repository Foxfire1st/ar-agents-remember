# mcp/tests/test_review_family_member_sources.py

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

Pins each family member's recorded source locator and the range resolved in its exact selected Git blob.

## Code Commentary

The fixture commits real source files and builds both knowledge sides through read_scope_test_support and its test-only row store. Production read_family_roster and its side-selected anchor resolver supply the output. The test exercises read and projection behavior.

Assertions preserve per-member role/rationale and distinguish symbol/range resolution, whole-file locators, missing or stale locators and ranges beyond the recorded blob. A symbol defined twice carries both defining ranges. Each side keeps its own observed blob and the same attributed range. Alpha’s JSON-mode model dump keeps the nine legacy fields beside the structured locator fields. No range is inferred by parsing a detail sentence.

### Logic

**One module-scoped fixture, two sides.** `build_sources_fixture` builds the shared read-scope store
(`read_scope_test_support.build_read_scope_fixture`), commits `BEFORE_TEXT` (with `alpha` at lines 1-2 and
`beta` at 5-6) and a second file `src/double.py` defining `alpha` twice, then commits `AFTER_TEXT` (the same
file with `gamma` appended, so the blob changes but `alpha`'s lines do not). It authors seven claims on the
before dataset — two symbol claims on different members in one file, a `line_range`, a `file`, a symbol the
bytes do not define, a range past the blob's end (50-60 of six lines) and the double definition — then
independently builds the after text-backed dataset from the six reused claims plus the re-recorded
`alpha` claim against the after blob. No baseline database-byte copy constructs this population. `roster_sources`
opens one side with `open_family_side`, reads the fixture family with `read_family_roster`, closes the side
and indexes every carried source by claim id.

| Case | What it pins |

| --- | --- |

| `test_two_members_in_one_file_carry_their_own_locators_ranges_and_rationale` | two members in one file are two sources with distinct locators, ranges (1-2 and 5-6), roles and stored rationales; a `line_range` resolves to its recorded range; a `file` locator is `whole_file` with no range; the JSON-mode model dump carries the structured values |

| `test_a_changed_file_keeps_its_unchanged_attributed_range_on_each_side` | a changed blob whose attributed lines did not move keeps range 1-2 on both sides, each with its own observed blob |

| `test_an_unresolved_locator_is_stated_with_its_recorded_locator_and_no_range` | an undefined symbol is `unresolved`/`recorded_blob_mismatch` with its recorded locator and no range; the reused beta, range and file claims are unresolved on the after side and retain their recorded locators without ranges; a read naming no tree is `not_requested`/`unresolved` for every source |

| `test_a_recorded_range_past_the_blob_end_is_unresolved_with_no_range` | lines 50-60 of a six-line exact blob keep `exact_recorded_blob`, carry no range, are `unresolved`, and the detail states the line count |

| `test_a_symbol_defined_twice_carries_every_defining_range` | a doubly-defined symbol carries both ranges, in order |

| `test_the_existing_source_fields_keep_their_published_values` | the JSON-mode model dump has exactly the nine legacy fields plus `locator`, `resolved_ranges`, `locator_state`, and the legacy values — including the `detail` sentence — are unchanged |

### Conventions

- The module carries `pytestmark = pytest.mark.evidence_unit`.
- Git is driven with real `git` subprocess calls in a temporary directory; no production state is touched.

### Invariants And Boundaries

- **A test here never reads a region out of prose.** The only `detail` assertion is the legacy-value
  equality and the stated line count for the out-of-range case.
- The cases build fixture rows, then read and resolve them through the production roster. The JSON assertions inspect model dumps directly.

### Todos

None recorded.

## Retained Historical Accounts

The memory baseline `81cfe4a8` recorded the following source-epoch accounts. They preserve that earlier card's observations and citation custody; they do not measure the current corpus or establish a historical event commit.

> Retired at the fifth freeze d59c3493: mcp/tests/evidence-lifecycle.toml:3324-3324 - the bytes it recorded now occur 67 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:1955-1955 - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.

> The shared-fixture consumer registration. In merged A3 this reference cites all 5 artifact blocks whose exact consumers list names this module. The earlier occurrence count and first-occurrence wording described unrelated narrow text, already unrelated in the parked source, and did not establish this module's consumer membership. Those targets are replaced by this complete membership set. Former member identity is not recovered or claimed. [Past-epoch source caption, detached from live reference 35. Recorded citation custody: mcp/tests/evidence-lifecycle.toml blob b9e272ef623574e517181e36b3dc949a3ac78e19 (available); mcp/tests/evidence-lifecycle.toml blob 0b04e782b9627695554aeeebd05967506794d78d (available); historical event commit not identified. No historical event or intent inferred.]

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_two_members_in_one_file_carry_their_own_locators_ranges_and_rationale` supplies the current fixture or assertion described above. [15]
- `test_a_changed_file_keeps_its_unchanged_attributed_range_on_each_side` supplies the current fixture or assertion described above. [16]

- `test_an_unresolved_locator_is_stated_with_its_recorded_locator_and_no_range` supplies the current fixture or assertion described above. [17]

- `test_a_symbol_defined_twice_carries_every_defining_range` supplies the current fixture or assertion described above. [18]
- `test_the_existing_source_fields_keep_their_published_values` supplies the current fixture or assertion described above. [19]

- The module builds both sides through read_scope_test_support, whose row construction uses the test-only knowledge row store. [20]

The rows name the fixture, the reader and each case, plus the owners they drive.

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References (continued)

- The fixture defines both shared-file texts, their attributed line ranges, the past-end range and both definitions in the duplicate-symbol file. [22]

- **The legacy source fields whose values must not change.** [23]

- **The fixture: seven before claims, an independently built matching after population and the re-recorded alpha claim over two real commits.** [24]

- **One side's roster read through the production owners, indexed by claim.** [25]
- Two members in one file, and the line-range and file-locator states. [26]
- The unchanged attributed range on both sides of a changed file. [27]

- Unresolved locators keep their recorded value and carry no range. [28]

- A range past the blob end is unresolved on the exact blob. [29]
- A doubly-defined symbol carries both ranges. [30]
- The legacy fields keep their values. [31]
- The projection under test. [32]
- The resolver that fills the ranges. [33]

### Cross-Repo References

No cross-repository behavior is exercised; the Git repository and datasets are temporary.

No meaningful cross-repo references found.

### Repo-Internal References (continued)

- The `unit-regression` lane selects `mcp/tests/test_review_family_member_sources.py`. [34]






- RowStore writes text-tree fixture rows without the retired production admission plane. [21]


- The lifecycle catalog lists the module as an exact consumer of `mcp/tests/_user_settings_guard.py`, `mcp/tests/anchor_fixture_models.py`, `mcp/tests/fixtures/repository_profiles/node/package-lock.json`, `mcp/tests/knowledge_review_fact_test_support.py`, `mcp/tests/knowledge_rows_test_support.py`, `mcp/tests/read_scope_test_support.py`. [35]

