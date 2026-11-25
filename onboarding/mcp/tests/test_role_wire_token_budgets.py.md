# mcp/tests/test_role_wire_token_budgets.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Executable CI gate for Turn-1 mechanical wire optimization: verifies per-role `core/every-role.md` filtering, durable corpus roots and compact `skill/`/`detail/` link reachability, symlink-confined `.details/` custody and canonical report exclusion, KV-cache byte-identical static prefixes, suffix/legacy-prefix handover envelope replay, conditional `first_read` deduplication and four-case `host.developerQuestionRoute` projection, direct and held Turn-1 appendix offload limits, and non-ratcheting `o200k_base` Phase 1 wire-token ceilings.

## Code Commentary

Standalone test functions cover compiler filtering across all 32 admitted `(role, operation)` pairs against `core/digest-map.json` while preserving full-source compiler seals (`test_filter_shared_block_32_admitted_pairs_and_digest_map`, `test_filter_shared_block_seal_launcher_absent_source_and_markdown_edges`), filesystem and archive-zip `durable_composition_corpus_root` transitions with compact vs standalone link binding (`test_durable_corpus_root_archive_transition_and_compact_links`), nested `<stem>.details/` interior symlink refusal and `canonical_execution_reports` exclusion (`test_nested_details_symlink_confinement_and_report_exclusion`), dual-format suffix/legacy-prefix replay preserving complete-file diagnostic priority and legacy bodies ending in suffix-shaped lines (`test_replay_legacy_prefix_new_suffix_and_diagnostic_priority`, `test_replay_tamper_symlink_and_locator_rebind`), and `.opening-message.md` restore vs tamper/mismatch refusals (`test_opening_message_sidecar_restore_and_refusals`).

`WireTokenBudgetMatrixTests` subclasses `role_first_message_support.FirstMessageMatrixBase` to capture actual host-bound `agent-create` prompts and opened held leaf prompts. `_wire_tokens` normalizes fixture `root`, isolated `HOME`, checkout corpus root, UUIDs, and every 64-hex SHA-256 digest (`HEX64_RE -> FIXED_HEX64`) for zero-variance `o200k_base` measurement. Matrix tests assert bare `PHASE_1_WIRE_TOKEN_CEILINGS` across all 8 default pairs with post-provider-exit compact link reachability (`test_eight_default_pairs_pass_wire_token_ceilings_and_send_links`), explicit appendix-allowance ceilings (`PHASE_1_HELD_APPENDIX_ALLOWANCE`, `PHASE_1_LAUNCH_APPENDIX_ALLOWANCE`) plus negative over-ceiling rejection and Rule 5 Unicode character capping (`test_held_openings_and_bounded_appendices_stay_capped`), cross-seat byte-identical static prefixes up to `## Launch Context` (`test_kv_cache_static_prefix_byte_identical_across_all_eight_pairs`), conditional `first_read` dedup and four-case `host.developerQuestionRoute` (`test_conditional_first_read_dedup_and_four_case_developer_question_route`), and direct/held offload boundary, replay, reuse, and failure-safety rules (`test_direct_opening_offload_boundaries_replay_and_heading_safety`, `test_held_opening_offload_reuse_distinct_batch_and_failure_safety`).

These are source-declared unit-regression tests, not live provider KV-cache measurements.

## Relationships

- Registered in `mcp/tests/test-evidence-lanes.toml` under `unit-regression` and in `mcp/tests/evidence-lifecycle.toml` as a consumer of its shared test support (`role_first_message_support.py`, `paseo_launch_test_support.py`, `paseo_runtime_test_support.py`, `curator_coherence_test_support.py`, `_user_settings_guard.py`, and the Node lockfile).
- Exercises `application/role_capsules/shared_block.py`, `application/role_capsules/wire_budget.py`, `application/skill_resources/provider.py`, `cli/role_brief_message.py`, `cli/role_handover_artifacts.py`, `cli/role_handover_file.py`, `cli/role_handover_projection.py`, `cli/role_handover_restore.py`, `cli/role_instruction_details.py`, `cli/role_instruction_links.py`, `cli/role_launch_preparation.py`, `cli/role_opening_offload.py`, `cli/role_launch_routes.py`, `cli/role_held_messages.py`, and `worktrees/role_reports.py`.

## Evidence

- `_wire_tokens` normalizes fixture root, isolated HOME, checkout corpus root, UUIDs, and all 64-hex digests for zero-variance `o200k_base` measurement. [1]
- Standalone filter, durable corpus, nested `.details/`, canonical report exclusion, dual-format replay, and `.opening-message.md` restore tests verify AC-1, AC-2, AC-4, and AC-6 contracts. [2]
- `WireTokenBudgetMatrixTests` gates all 8 default fresh base launch pairs, held/launch ordinary-Latin appendix allowances with negative rejection, 8-pair KV static prefix byte equality, four-case `host.developerQuestionRoute`, and direct/held offload boundaries. [3]
