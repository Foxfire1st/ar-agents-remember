# mcp/src/agents_remember/serving/paseo/paseo_provision.py

## Governing Overview

[overview](../overview.md)

## Purpose

Converges the configured install, home config, plugin and daemon while reporting exact changes.

## Code Commentary

provision_runtime stages the exact pinned version before activation, validates owned daemon record and listen address, changes start-only settings around stop/start, and acknowledges the loaded plugin stamp after successful load. A no-change pass uses read-only native calls. Preserve packet-stated rollback/activation interruption limits rather than claiming every failure leaves all prior state untouched.

The host release comes from the packaged contract, the npm run uses the product's Node and installs from the shipped lock, and the install intent gets `provision_for_install`, which reads the no-stop admission before any write and re-checks a live host at the irreversible sites. `_converge_daemon` reports a late restart-required setting while keeping the host running.

Install defers an observed live Node transition before acquisition or home changes. Explicit terminal provision performs the restart and, only after the replacement host starts successfully, reports its observed earlier sibling product Node folder as no longer used by that host. The report deletes no files and makes no claim about other processes using that folder.

Before every stop of its own running host (for a replacement install, for a start-only setting, and the cleanup after a failed start), a pass compares the running host's harness-home values with what the new host would get: the provider's `env` from the settings, else this process's environment. A difference refuses with `harness-home-would-change` before anything is stopped, unless the pass came from `provision_with_home_change` (the terminal `paseo provision --accept-harness-home-change`). The report carries `inheritedHarnessHomes` and `harnessHomeRemedy` for the host found at the start of the pass.

The setting, embed, plugin-copy and plugin-load changes are recorded with the descriptions from `paseo_install_plan`, so the install preview names the same actions; provider entries are reported by id only, and a provider write to a running daemon records its reload.

## Evidence

- The converge pass and its install entry. [1]

- The no-stop admission read. [2]

- Only the prior sibling product Node is reported unused; files are retained. [3]

- The harness-home comparison runs before the stop of an owned host. [4]
- The explicit provision that accepts a harness-home change. [5]
- Home-file changes are recorded with the shared plan descriptions. [6]
