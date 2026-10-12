# mcp/tests/test_paseo_install_contract.py

## Governing Overview

[overview](overview.md)

## Purpose

The focused install-contract cases: the host step runs after the earlier steps and once, a block added after server start is read at the call, the preview changes nothing, the build pin wins every settings selector, a failing host step keeps the earlier result with ok false, and an absent block is named.

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

## Evidence


- The one-provision call-time read case. [1]


- The preview and failure-composition case. [2]


- The build-pin-wins case. [3]
