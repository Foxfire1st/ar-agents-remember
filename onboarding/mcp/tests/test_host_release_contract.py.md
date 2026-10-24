# mcp/tests/test_host_release_contract.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Holds the release-side contract of the Paseo host: the plugin pin and the lock entry or archive a release
names must agree, a retired selector is announced once on each public command and the dashboard line, and a
whole-file upgrade preserves the historical host block and every other settings family as user-file bytes.
The user-settings location guard refuses an old location before parsing either old or existing new bytes.

## Code Commentary

### Logic

Cases drive the CLI, `install.runtime`, `paseo_provision`, `paseo_start` and the daemon, with
`_user_settings_guard` writing the settings tree through `user_settings_location`.

- **Release concordance.** `test_plugin_pin_drift_fails_release_concordance` fails a drift between the plugin
  pin and the release, and `test_release_concordance_rejects_mismatched_lock_entry_or_archive` rejects a
  mismatched lock entry or archive.
- **Sandbox ports.** `test_public_sandbox_ports_reach_the_command_with_defaults_preserved` keeps the defaults
  when no port is given, and `test_public_sandbox_ports_refuse_invalid_live_and_equal_values_before_actions`
  refuses an invalid, live or equal pair before anything acts.
- **One notice.** `test_retired_selector_notice_once_on_each_public_command_and_dashboard_line` prints the
  retired-selector notice once per public command and on the dashboard line.
- **Old location.** The historically named
  `test_host_and_all_standalone_starters_refuse_old_location_before_any_write` now calls only
  `require_user_settings_path`: it refuses before parsing an old file or an existing user file, and preserves
  both byte sequences. The retired starters no longer provide a renderer path to invoke.
- **Upgrade.** `test_whole_file_upgrade_retains_configured_host_and_all_other_families` upgrades the settings
  file as a whole and retains the configured host and every other family.
- **Sandbox isolation.** `test_sandbox_environment_reads_only_its_own_user_settings` keeps a sandbox reading
  only its own settings.

### Conventions

Cases assert on the settings bytes after the command as well as on its answer, so an accidental rewrite is
visible.

### Invariants And Boundaries

- A release names one plugin pin, and the lock entry or archive must agree with it.
- The user-settings location guard refuses an old location before parsing settings; it never migrates silently.

## Evidence

- The plugin pin drift case. [1]
- The lock and archive concordance case. [3]

- The notice-once case. [4]
