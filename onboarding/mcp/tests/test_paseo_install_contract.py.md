# mcp/tests/test_paseo_install_contract.py

## Governing Overview

[overview](overview.md)

## Purpose

The focused install-contract cases: the host step runs after the earlier steps and once, a block added after server start is read at the call, the preview changes nothing, the build pin wins every settings selector, a failing host step keeps the earlier result with ok false, and an absent block is named.

## Code Commentary

The module drives `run_runtime_install` through `paseo_runtime_test_support.FakePaseo` and asserts the host part's shape, the read-at-call behavior and the failure composition.

## Evidence

- The one-provision call-time read case. [1]
- The preview and failure-composition case. [2]
- The build-pin-wins case. [3]
