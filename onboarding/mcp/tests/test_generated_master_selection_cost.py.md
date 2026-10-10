# mcp/tests/test_generated_master_selection_cost.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Retained rule-8 proof on the generated master: the 100001-file nested tree is rebuilt and the bounded selection request set is proven independent of tree size, with aggregate bytes under the fixed 1000000 ceiling and the no-notes case preserved. The pinned dashboard replies are re-verified against the live tree on every run.

## Code Commentary

Three cases: the selection-change bytes are bounded and independent of tree size (masked big/small equality), the noteless master stays bounded, and the pinned selection answers match the live generated masters. The connector rebuilds the exact tree, so the fixture cannot drift from serving behavior unnoticed.

## Evidence

- Selection-change bytes are bounded and independent of tree size. [1]
- The noteless master stays bounded. [2]
- Pinned selection answers match the live generated masters. [3]
