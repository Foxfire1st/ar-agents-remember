# mcp/tests/test_curator_coherence_closed_out.py

## Governing Overview

[overview](overview.md)

## Purpose

Protect the historical closed-out coherence response separately from pre-closeout live readiness.

## Code Commentary

A real published coherence authority is paired with completed closeout cells. Status and validate, each parsed through the typed response model, then report closed-out with recorded code/memory commits and record digest, not a comparison to later working bytes: the live-source observation and currentness check fail the case if they are reached. Before closeout that shortcut is unavailable: both actions answer `current` or `valid` and carry no commit fields. Without a record the result remains absent.

## Evidence

No external Domain Documentation source is configured for this repository. The following source witnesses establish the contract, not a new execution receipt.

- For both status and validate, a completed closeout answers `closed-out` with its code and memory-content commits and the coherence record digest, without comparing the live candidate. [1]

- The shortcut never invents a missing record. [2]

- Before the closeout, status and validate answer current or valid without code or memory commit fields. [3]
