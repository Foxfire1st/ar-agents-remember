# mcp/tests/test_witness_driver_helpers.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Unit pins for the pure pieces of the L108 sandbox witness driver (MIK-R108 E4/E7): the directory snapshot and the call recorder. The driver itself runs by hand against a hermetic world; these tests are its exact lifecycle consumer.

## Code Commentary

### Logic

- `TestWitnessHelpers` pins snapshot shape (files with sizes, missing stays missing) and the recorder behavior the driver depends on.

### Invariants And Boundaries

- These tests pin helpers only; the two-world run they serve is executed manually and binds its frozen evidence file.

## Evidence

- Snapshots list files with sizes; missing roots stay missing. [1]
