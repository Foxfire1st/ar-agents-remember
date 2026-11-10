# mcp/tests/test_paseo_install_contract.py

## Governing Overview

[overview](overview.md)

## Purpose

The focused install-contract cases: the host step runs after the earlier steps and once, a block added after server start is read at the call, the preview changes nothing, the build pin wins every settings selector, a failing host step keeps the earlier result with ok false, an absent block is named, and the host preview lists the same ordered actions a real provision then takes.

## Code Commentary

The module drives the application install and its answer projection through
`paseo_runtime_test_support.FakePaseo`. For a provisioned or updated overflow answer, it checks
the delivered outcome and obtains full host/summary/Node facts from that call's newly filed
report. Exactly one new report identifies each call; `reportPath` is cross-checked when delivered,
not assumed present under a long root. Update facts and secret-marker absence are checked in the
updated report as well as in the bounded answer.

A dry run files no report in this direct-call fixture. It checks the delivered preview outcome
and the unshaped application's flags as separate evidence, with exactly two preview dispatches,
no provisioning and no mutation. This component evidence is not a retained full public-host
answer. Failure composition, provision-once, idempotence and reload-without-stop assertions remain.

`preview_matches_real` runs `paseo_install.preview_host` against the fake host, asserts it changed no file and made no host mutation, then runs the real `provision_for_install` and requires the same ordered `changes` list and `changed` flag. Through it the host-preview cases cover a first install (config, embed, plugin copy, daemon start, plugin install; a repeat preview is empty), a setting-only reload and a provider reload that names provider ids without their secret values, plugin copy/reload/enable/replacement, a restart-only setting that is reported as `restartRequired` and a deferred restart with no promised action, provider-file restoration, stale-record and install-leftover cleanup of a stopped host, and Node acquisition and Node leftover cleanup with no CLI reinstall and an untouched daemon.

## Evidence



- The one-provision call-time read case. [1]




- The preview and failure-composition case. [2]




- The build-pin-wins case. [3]

- The preview-equals-real helper: no file or host mutation, then the same ordered actions as the real provision [4]
- First-install preview lists settings, destinations, plugin and start; a repeat lists nothing [5]
- Setting-only and provider reload previews name no secret value [6]
- Plugin copy, reload, enable and replacement previews match the real provision [7]
- A restart-only setting is named as deferred without promised actions [8]
- Stopped-host recovery, stale-record and install-leftover cleanup previews match [9]
- Node acquisition and Node leftover cleanup previews match, with the daemon untouched [10]
