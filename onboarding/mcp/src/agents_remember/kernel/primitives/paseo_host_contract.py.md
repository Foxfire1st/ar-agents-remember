# mcp/src/agents_remember/kernel/primitives/paseo_host_contract.py

## Governing Overview

[overview](overview.md)

## Purpose

Release-owned host and Node pins; settings never select another build.

## Code Commentary

`HOST_CONTRACT` is read from the packaged `package_data/paseo_host/contract.json`; `PASEO_PACKAGE`, `PASEO_VERSION` and `NODE_VERSION` are derived from it, and every consumer takes its version from these names rather than from a local literal or the settings block.


**L184 — INV-JS6GJ7.** The pin is read from here, so the version the contract agrees with is stated here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Evidence

- The contract load and its three derived names. [1]
