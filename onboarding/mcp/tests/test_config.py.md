# mcp/tests/test_config.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers the configuration contract: two repository ids may not share one Git common directory, an external
memory root may not alias a configured code repository, the config file may not live inside the coordination
root, and a repository's certification profile or contract path must stay inside the root. The optional
`paseoRuntime` block is exact and fails loud, while a retired harness skill root is tolerated and never read.

## Code Commentary

### Logic

`write_json()` and `settings_payload()` build a settings document, and `McpConfigTests` loads it through the
real primitive (`runtime_config`, `providers.settings`, `paseo_runtime_settings`). `OrchestrationSettingsTests`
loads the global orchestration file.

- **Identity.** `test_two_repository_ids_cannot_share_one_git_common_dir` and
  `test_external_memory_cannot_alias_another_configured_code_repo` refuse two ids on one directory and an
  external memory aliasing a code repo.
- **Placement.** `test_config_must_not_live_inside_coordination_root` and
  `test_repository_contract_path_cannot_escape_coordination_root` keep the config file outside the
  coordination root and a contract path inside it.
- **Authority.** `test_loads_authority_settings` loads the authority settings, and
  `test_repository_certification_profile_reference_fails_closed` fails closed on a bad profile reference.
- **The runtime block.** `test_optional_paseo_runtime_block_is_exact_and_fail_loud` requires the block to be
  exact and to fail loud; a retired harness skill root is tolerated and left unread
  (`test_a_retired_harness_skill_root_is_tolerated_and_unread`, MIK-R196 rule 7), because the installed-copy
  root left the configuration contract.
- **Orchestration.** `test_human_pinned_kind_in_global_file_fails_boot` fails boot on a human-pinned kind in the
  global file.

### Conventions

Every case writes a settings document and loads it through the product's own reader, so a validation that
exists only in the test would not pass.

### Invariants And Boundaries

- A repository's identity is its Git common directory; two ids on one directory are refused.
- An unknown or retired key is tolerated and unread rather than silently honoured.

## Evidence

- Two repository ids cannot share one git common dir. [1]
- External memory cannot alias another configured code repo. [2]
- Config must not live inside the coordination root. [3]

- The authority settings load. [4]

- A repository certification profile reference fails closed. [5]
- A repository contract path cannot escape the coordination root. [6]
- A human-pinned kind in the global file fails boot. [7]

- The optional `paseoRuntime` block's exactness and fail-loud behaviour, including the tolerated retired skill root. [8]
