# mcp/tests/test_citation_index_resilience.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_citation_index_resilience.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T10:35+02:00 |
| lastVerifiedCommitHash | `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` |
| lastVerifiedCommitDate | 2026-09-17T10:09:37+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l14-ar` uncommitted source; base `0346da9c572e1eb913a8eb4130e9a9e9d37343c8` |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Pin the three behavioural claims `CAPS-R14@v1` makes about the citation source index: the index
**honours the shared exclusion register from each of its three sources independently**, the ruled
caps **skip and report rather than refuse**, and the quality surface **cannot be bricked** by
either.

The module's own docstring names the two defects it makes impossible. A cap used to refuse the
whole tree (`citation source-index input exceeds the 4194304-byte per-file cap: [...]` was raised
as an *error* out of the mandated contract-scoped `memory_quality_check`, so a large or vendored
tree made the quality surface the thing that blocked work instead of the thing that describes it),
and enumeration ignored the shared exclusion register entirely. The developer's 2026-08-20 ruling
is the contract the caps cases assert: an oversized file is **skipped with a report entry naming
it and its size**, the aggregate default is **512 MiB applied to the post-exclusion/post-skip
set**, the caps are settings-overridable through `onboarding.citationIndex`, and a hard stop
remains only past **~2 GiB**.

## Code Commentary

### Logic

`Fixture` builds one disposable tree per case — a code root, a memory root carrying
`system/settings.json`, and a card citing a source range — so each case can compare a population
before and after exactly one rule is introduced. `FixtureCase.setUp` creates it under a temporary
directory that is removed afterwards; nothing outside it is read or written.

The five classes and what each one defends:

| Class | Defends |
| --- | --- |
| `TheExclusionRegisterIsHonouredFromEachSourceIndependently` | one case per source: `pathRules.exclude`, the code repo's `.gitignore`, and a caller-supplied exclude. Also the durable record (the register parsed back **out of the published manifest file**, not from memory), the non-Git fallback under rule interaction, the pinned divergence from Git, and the one-authority-per-root parity between the two acquisition routes. |
| `TheRuledCapsSkipAndReportRatherThanRefuse` | the per-file skip names the path **and** its stat size with the index still built; a total above the ruled default reports; the hard stop names offenders, the cap and the next step; every `onboarding.citationIndex` key overrides while the module constants stay default; the file-count cap names its fixing route; a malformed block is refused by name. |
| `TheQualitySurfaceCannotBeBricked` | the reported, actionable states: a capped index reported on the citation check, an unreadable source named with its path, an unbuildable index as a reported state with a `nextStep`, the closeout gate's own declared check group degrading identically, and a document with no code root saying so rather than passing. |
| `TheRegisteredCitationSurfaceCarriesTheCallerExcludes` | the caller-exclude surface itself: the registered `citation_fix` MCP tool declares `exclude`, and the CLI declares a repeatable `--exclude` option. |
| `TheCapsThatStayAsTheyWere` | the two caps the ruling did **not** move — the database cap and the file-count cap — so a later edit cannot widen them unnoticed. |

### The divergence case, and why it is written the way it is

`test_the_register_admits_a_negated_file_under_an_excluded_directory_where_git_does_not` measures
**both sides**: Git's answer comes from a real repository (`git check-ignore -q vendor/keep.py`
exits 0, so Git ignores the file), while the register's answer comes from a plain directory
carrying the same `.gitignore` bytes (`vendor/keep.py` admitted, `vendor/lib.py` excluded,
`gitignoreAuthority: register`). The case exists so the divergence between the register's contract
and Git's cannot be mistaken for an accident, and it is falsifiable: making the matcher
Git-faithful kills both this case and the L14R-4 class case.

### Conventions

- Each case protects one distinct reading, and the module states which one in its own
  `WHAT DEFENDS WHAT` table.
- Cap values are read from the shipped constants (`PER_FILE_CAP`, `AGGREGATE_CAP`, `HARD_STOP`)
  rather than restated as literals, so a case reddens if a constant moves rather than silently
  testing an old number.
- The module is registered in the `unit-regression` evidence lane
  (`mcp/tests/test-evidence-lanes.toml`) and is a declared consumer of the lifecycle catalog.

### Invariants And Boundaries

- No case asserts that D7/D8's repository-wide citation backlog was repaired here; that backlog is
  another leaf's and is sized in its own ledger entry.
- No case reads or writes outside its own temporary root.
- The module never asserts an acceptance result: the fresh-user chain is
  `mcp/tests/test_fresh_user_harness.py`'s subject and
  `scripts/e2e_harness/run_fresh_user.py`'s transcript.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| A settings exclude removes a file and the register records the rule that did it. | `test_a_path_rules_exclude_removes_a_file_and_the_register_records_the_rule` | mcp/tests/test_citation_index_resilience.py:210-229 |
| A `.gitignore` rule removes a file and the register records the pattern. | `test_a_gitignore_rule_removes_a_file_and_the_register_records_the_pattern` | mcp/tests/test_citation_index_resilience.py:231-256 |
| A caller exclude narrows one call and only that call. | `test_a_caller_supplied_exclude_narrows_one_call_and_only_that_call` | mcp/tests/test_citation_index_resilience.py:258-267 |
| The rule set survives on the durable record, parsed back out of the published manifest. | `test_the_published_manifest_carries_the_rule_set_that_produced_the_index` | mcp/tests/test_citation_index_resilience.py:269-296 |
| The non-Git fallback keeps a directory rule while a negation exists. | `test_the_non_git_fallback_keeps_a_directory_rule_while_a_negation_exists` | mcp/tests/test_citation_index_resilience.py:298-332 |
| The register's deliberate divergence from Git, pinned on both sides. | `test_the_register_admits_a_negated_file_under_an_excluded_directory_where_git_does_not` | mcp/tests/test_citation_index_resilience.py:334-374 |
| One root gives one `gitignoreAuthority` on both acquisition routes. | `test_one_root_gives_one_gitignore_authority_on_both_acquisition_routes` | mcp/tests/test_citation_index_resilience.py:376-406 |
| A caller exclude that cannot mean anything is refused by name. | `test_an_exclude_that_cannot_mean_anything_is_refused_by_name` | mcp/tests/test_citation_index_resilience.py:408-415 |
| An oversized file is skipped and reported with its path and size, index still built. | `test_an_oversized_file_is_skipped_and_reported_with_its_path_and_size` | mcp/tests/test_citation_index_resilience.py:421-436 |
| A total above the ruled 512 MiB default reports instead of refusing. | `test_a_total_above_the_ruled_default_reports_instead_of_refusing` | mcp/tests/test_citation_index_resilience.py:438-455 |
| The hard stop names the offenders and the next step. | `test_the_hard_stop_names_the_offenders_and_the_next_step` | mcp/tests/test_citation_index_resilience.py:457-483 |
| Every settings key overrides a cap while the module constants stay default. | `test_citation_index_settings_override_every_cap_and_the_constants_stay_defaults` | mcp/tests/test_citation_index_resilience.py:485-523 |
| The file-count cap refuses with the route that fixes it. | `test_the_file_count_cap_refuses_with_the_route_that_fixes_it` | mcp/tests/test_citation_index_resilience.py:525-536 |
| A malformed `citationIndex` block is refused by name. | `test_a_malformed_citation_index_block_is_refused_by_name` | mcp/tests/test_citation_index_resilience.py:538-557 |
| A capped index is reported on the citation check rather than raising. | `test_a_capped_index_is_reported_on_the_citation_check` | mcp/tests/test_citation_index_resilience.py:581-594 |
| An unreadable source is reported with its path. | `test_an_unreadable_source_is_reported_with_its_path` | mcp/tests/test_citation_index_resilience.py:596-611 |
| An index that cannot be built is a reported state carrying a `nextStep`. | `test_an_index_that_cannot_be_built_is_a_reported_state_with_a_next_step` | mcp/tests/test_citation_index_resilience.py:613-629 |
| The closeout gate's own declared check group degrades the same way. | `test_the_closeout_gates_own_check_group_degrades_the_same_way` | mcp/tests/test_citation_index_resilience.py:631-656 |
| A document with no code root says so rather than passing. | `test_a_document_with_no_code_root_still_says_so_rather_than_passing` | mcp/tests/test_citation_index_resilience.py:658-665 |
| The registered `citation_fix` MCP tool declares `exclude`. | `test_the_registered_tool_declares_exclude` | mcp/tests/test_citation_index_resilience.py:682-689 |
| The CLI declares a repeatable `--exclude` option. | `test_the_cli_declares_a_repeatable_exclude_option` | mcp/tests/test_citation_index_resilience.py:691-707 |
| The database cap and the file-count cap are unchanged by the ruling. | `test_the_db_cap_and_file_count_cap_are_unchanged` | mcp/tests/test_citation_index_resilience.py:713-720 |
| The ruled numbers the caps cases assert against. | `MAX_SOURCE_BYTES`; `MAX_SOURCE_FILE_BYTES`; `MAX_SOURCE_HARD_STOP_BYTES` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:21-28 |
| The caller-exclude surface the last two cases read. | `citation_fix` | mcp/src/agents_remember/mcp/registration/memory.py:100-124 |

## Cross-Repo References

No sibling-repository contract defines these values.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T10:35+02:00 — 260915-CAPS-L14 curator: created this card for the test module the leaf adds. Records the two defects the module makes impossible (a cap that refused the whole tree out of the mandated check, and an enumeration that ignored the shared exclusion register), the developer's 2026-08-20 ruling the caps cases assert, the five classes and what each defends, and the divergence case that measures Git's answer and the register's answer separately so the difference cannot read as an accident. States that the module does **not** claim the repository-wide D7/D8 citation backlog was repaired here. Verification metadata is left at this leaf's synced base `0346da9c` with a `reviewedWorkingCandidate` row, because the candidate is deliberately uncommitted — the governed closeout stamps the real code commit and no hash or digest was invented here.
