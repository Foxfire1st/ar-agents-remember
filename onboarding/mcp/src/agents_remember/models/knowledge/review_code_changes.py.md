# mcp/src/agents_remember/models/knowledge/review_code_changes.py

## Governing Overview

[governing route overview](../overview.md)

## Purpose

Defines the leaf-wide implementation facts that can mark an invariant before anyone opens its family.

## Code Commentary

`ReviewCodeChange` names both the invariant’s raw identity and projected key, its `established`/`unknown`/`not_established` implementation fact, the proof and unresolved-range marks, and evidence/reason tuples. `ReviewCodeChanges` wraps a `facts` or `unavailable` answer with optional bounded detail and an invariant tuple. These are declarations: this module does not enforce a reason per unavailable/unknown state or compute which entries changed.

The application reads both memory sides, refuses unavailable sidecar/code scope as `unavailable`, and calls the same `implementation_facts` helper used by family review. It can reuse the worklist computation’s classifications. No roster, selected-subject review or source excerpt is loaded to define this fact population.

## Invariants And Boundaries

An unavailable answer is not zero code changes. Proof marks describe recorded proof entries, not a passing execution; established implementation is not proof of preservation or correctness. Comparison matching and browser badge precedence belong to consuming owners.

## Evidence

- Each invariant carries an implementation state with independent proof/range marks and evidence/reasons. [1]
- The whole-leaf wrapper distinguishes facts from unavailable; it has no cross-field validator. [2]
- The producer checks readable sides/code and reuses implementation_facts rather than a second code-change rule. [3]
