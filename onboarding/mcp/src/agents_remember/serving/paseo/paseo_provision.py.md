# mcp/src/agents_remember/serving/paseo/paseo_provision.py

## Governing Overview

[overview](../overview.md)

## Purpose

Converges the configured install, home config, plugin and daemon while reporting exact changes.

## Code Commentary

provision_runtime stages the exact pinned version before activation, validates owned daemon record and listen address, changes start-only settings around stop/start, and acknowledges the loaded plugin stamp after successful load. A no-change pass uses read-only native calls. Preserve packet-stated rollback/activation interruption limits rather than claiming every failure leaves all prior state untouched.

L96: the module moved from `cli/paseo_provision.py` into `serving/paseo/`. The host release now comes from the packaged contract, the npm run uses the product's Node and installs from the shipped lock, and the install intent gets `provision_for_install`, which reads the no-stop admission before any write and re-checks a live host at the irreversible sites. `_converge_daemon` reports a late restart-required setting while keeping the host running.

Install defers an observed live Node transition before acquisition or home changes. Explicit terminal provision performs the restart and, only after the replacement host starts successfully, reports its observed earlier sibling product Node folder as no longer used by that host. The report deletes no files and makes no claim about other processes using that folder.

## Evidence

- The converge pass and its install entry. [1]
- The no-stop admission read. [2]

- Only the prior sibling product Node is reported unused; files are retained. [3]
