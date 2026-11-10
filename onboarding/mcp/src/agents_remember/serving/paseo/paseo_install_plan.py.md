# mcp/src/agents_remember/serving/paseo/paseo_install_plan.py

## Governing Overview

[overview](../overview.md)

## Purpose

The read-only plan behind the `runtime_install` host preview, and the descriptions of product-owned actions that the real provision records, so the preview and a real run name the same actions.

## Code Commentary

`planned_changes` describes what a successful install pass would record, in the real pass's order: Node install or leftover removal; configuration leftovers and an unfinished provider write's recovery; stale-record removal; the host install or replacement, or staging leftovers; live then start-only settings, with a provider reload on a running host; embed and plugin-copy writes; a daemon start when no owned host runs; and the plugin's load operation. It writes, reloads and starts nothing, and plans no change when the install's admission holds a restart back. Late command failures and changes by another process are reported only by the real run.

`setting_change`, `home_changes` and `plugin_changes` are the functions `paseo_provision` records its changes with. Provider entries appear only as `providerIds`, never their values. When the product Node or the CLI is not installed, or a provider recovery is pending, the plan reads the configured document as it would be after recovery (`provider_recovery_plan`) instead of asking the CLI; `installed_manifest_version` gives the preview the CLI version from its package manifest when the product Node cannot run it or a restart is held back; and a plugin registered in a stopped daemon's file counts as loading on start. The module also owns the staging and previous-install directory names.

## Evidence

- The ordered, read-only plan; no change when a restart is held back. [1]
- A setting is described with provider ids only. [2]
- The embed and plugin-copy writes a pass will make. [3]
- The single plugin load operation after a wrong-path registration is removed. [4]
- The installed CLI version read from its manifest. [5]
- A plugin registered in a stopped daemon's file counts as loading on start. [6]
