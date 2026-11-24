# mcp/tests/test_lean_symbol_anchors.py

## Governing Overview

[Overview](overview.md)

## Purpose

Exercise Lean symbol anchoring through the writer and recorded reader.

## Code Commentary

The synthetic fixtures cover namespace and section layout, declaration prefixes and continuations, masked literals, instances and pinned spelling rules. They distinguish full-name precedence, whole-name lookup and ambiguity in a written name. The alias case checks a separate binding for each named slot, a shared command extent and the next declaration’s own extent.

## Relationships

The scope cases verify that exact keys stay unverifiable when possible command tokens leave different lawful namespace readings. Other cases check scope agreement and the continued availability of a verified neighboring name.

## Evidence

- This test checks the writer's qualified-name suggestions and the reader's two defining extents. [1]
- The writer and recorded reader agree on source extents for alias binders and the following definition. [2]
