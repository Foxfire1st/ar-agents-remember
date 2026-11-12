# scripts/check-host-contract.py

## Governing Overview

[overview](../overview.md)

## Purpose

Release concordance for the shipped host pin, plugin SDK and complete npm lock.

## Code Commentary

`check` reads the contract, the host manifest, the lock and the plugin manifest and returns every mismatch: the manifest and lock root dependencies, the host package's locked version, the plugin's development SDK pin and the Node archive entries' URL/SHA-256 shape. It is run by the release steps and exercised by `test_host_release_contract`.

## Evidence

- The concordance check over contract, manifest, lock and plugin. [1]
