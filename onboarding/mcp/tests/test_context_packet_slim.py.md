# mcp/tests/test_context_packet_slim.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Protect the compact context_packet transport independently from the full packet builder.

## Code Commentary

The checks distinguish an ordinary compact answer from the full CLI/application packet: compact roots, optional task/actions, serving build and pair remain, while repeated policy blocks are absent. The ordinary hermetic fixture is token-counted against the packet’s bound; no test receipt for the current checkout is created by reading this card.

Action controls distinguish behind/drifted/partial-index states from clean state. Registered taskless and leaf calls check openable roots and task document, task/master identity and commit-shaped build/pair values. The retained log assertions compare delivered compact fields, not an assurance that the log contains every omitted policy block.

## Evidence

- The ordinary compact fixture checks retained roots/build and omitted repeated blocks. [1]
- A registered partial-index fixture exposes its action line. [2]
- Registered leaf and taskless fixtures open named roots and validate task/build/pair fields. [3]
