# mcp/tests/test_curator_healing_contracts.py

## Governing Overview

[overview](overview.md)

## Purpose

Pins the `healing_findings` checker in `agents_remember_test_support.testing.curator_contracts`: it must catch instruction text that limits memory healing to one's own faults or routes all encountered debt away, and must not flag bounded routing or positive repair duties.

## Code Commentary

The first case feeds seventeen phrasings and requires exactly one finding each, `route-all-debt` for blanket routing or deferral of encountered debt and `own-fault-only` for repair limited to faults the reader caused. The second case requires no finding for the Curator role's own healing clauses (`ROLE_HEALING`), for a bounded "repair what you meet, route what needs code or another leaf" sentence, and for a duty to repair faults one's own work causes. The cases test the checker on literal text only; `test_curator_delivery_contracts.py` applies it to the shipped corpus.

## Evidence

- Each avoided-debt or own-fault-only phrasing yields exactly its one finding. [1]
- The role's healing clauses, bounded routing and positive repair duties yield no finding. [2]
