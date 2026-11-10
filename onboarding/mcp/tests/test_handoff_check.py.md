# mcp/tests/test_handoff_check.py

## Governing Overview

[overview](overview.md)

## Purpose

Tests the producer handoff checker’s frozen-tree validation and read-only command boundary.

## Code Commentary

The module exercises malformed producer entries, supported and unsupported proof spellings, repoint target checks and candidate-bearing fields. Record-link checks require memory and a stored unretired record; fired-link judgment remains with the writer. It checks the named committed tree rather than changed working files and snapshots code, memory, task and runtime bytes while forbidding writer and working-tree capture calls. A clean producer list prints exactly the clean line, the writer-checked fired link and the not-run record links, and a `--worklist` input is rejected by the parser with exit 2 instead of being checked. These are assertions in the test source, not evidence of a run.

## Evidence

- Producer, proof, record-link and candidate-field cases distinguish checker validation from writer judgment. [1]

- The named-tree and byte-snapshot cases assert read-only behavior and invocation-error status. [2]

- A clean producer prints exactly three lines, and a worklist input is an unrecognized argument with exit 2. [3]
