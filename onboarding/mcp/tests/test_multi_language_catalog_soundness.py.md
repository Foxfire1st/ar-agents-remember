# mcp/tests/test_multi_language_catalog_soundness.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Table-driven unit-regression test suite proving catalog completeness, positive binding accuracy with wrappers, negative soundness, per-language qualifier policies and honest refusals, pure-move round-trip agreement across anchor consumers, ambiguous-suffix defaults and `languages.json` overrides, and catalog schema validation plus `languages warm --all`.

## Code Commentary

Seven test functions iterate over `PILOT_FIXTURES` and `LONG_TAIL_FIXTURES` from `multi_language_soundness_fixtures.py` to stay within `pyproject.toml` collection budgets while verifying all 15 core pilots and all 56 `tree-sitter-language-pack` languages:

- `test_catalog_declares_15_pilots_and_50_plus_language_pack_entries_with_honest_tiers` checks that all 15 core pilots declare `pypi_wheel`, `verified`, pinned wheels, and `tagsQuerySha256`, that 50+ `language_pack` entries declare honest `guaranteeTier` values (including `best_effort`), that `.h`/`.m`/`.v`/`.scm` sit in `ambiguous_suffixes`, and that `LONG_TAIL_FIXTURES` matches every `language_pack` ID.
- `test_15_core_pilots_positive_binding_wrappers_and_negative_soundness` asserts exact `(start, end)` spans for every expected symbol and rejects every forbidden trap across all 15 pilots.
- `test_15_core_pilots_qualifier_policy_and_honest_refusal` checks `extents.qualified_spans` across all pilot qualifier cases and honest refusals on flat languages or unresolved qualifiers.
- `test_15_core_pilots_pure_move_round_trip_code_anchors_read_anchors_and_citation_fix` and `test_50_plus_language_pack_entries_positive_negative_and_pure_move_soundness` use `_assert_pure_move_round_trip` (via `_shifted_source`, `_write_sidecar`, and `_PureMoveCase`) to prove `CodeSnapshot.resolve`, `read_anchors.observe_anchor`, `currentness_observe.observe_entry`, and `reference_state.fix_references` agree when a construct moves inside a file.
- `test_ambiguous_suffixes_default_occurrence_only_and_resolve_with_languages_json_override` verifies `.h`, `.m`, `.v`, and `.scm` stay unbound by default and resolve cleanly through `languages.json` suffix and glob overrides with pure-move round trips.
- `test_catalog_schema_validation_for_guarantee_tier_qualifiers_and_warm_all_cli` checks `LanguageCatalogError` refusals for invalid `guaranteeTier`, `qualifiers.separators`, and `separatorKinds`, and exercises `agents-remember languages warm --all --json`.

## Relationships

Registered once in `unit-regression` in `mcp/tests/test-evidence-lanes.toml` and declared as an exact consumer of `multi_language_soundness_fixtures.py`, `knowledge_conversion_test_support.py`, `_user_settings_guard.py`, and the portable Node `package-lock.json` in `mcp/tests/evidence-lifecycle.toml`.

## Evidence

- `_assert_pure_move_round_trip` proves `CodeSnapshot.resolve`, `read_anchors.observe_anchor`, `currentness_observe.observe_entry`, and `reference_state.fix_references` agree across a pure move. [1]
- The seven table-driven tests prove catalog completeness, pilot positive/negative soundness, qualifier policy and honest refusals, pilot and 56-language-pack pure-move round trips, ambiguous-suffix `languages.json` overrides, and schema validation plus `languages warm --all`. [2]
- `mcp/tests/test-evidence-lanes.toml` selects `test_multi_language_catalog_soundness.py` in `unit-regression`. [3]
