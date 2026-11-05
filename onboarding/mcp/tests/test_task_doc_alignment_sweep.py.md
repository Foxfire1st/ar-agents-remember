# mcp/tests/test_task_doc_alignment_sweep.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Tests the answer-only sibling requirement sweep attached to task-document creation and requirement changes.

## Code Commentary

Declared missing siblings remain unavailable instead of becoming empty requirements; undeclared siblings are not read and malformed declared documents remain errors. The suite checks requirement identity extraction, terminal filtering and the threshold between individual rows and a count plus master location. It also compares written document bytes with and without the sweep, keeping response observations separate from task content. Reading these cases establishes no fresh passing run.

## Evidence

- Sibling states, missing declarations and malformed inputs preserve their distinct meanings. [1]
- Creation and requirement edits carry deduplicated sibling identities and omit terminal or irrelevant cases. [2]
- The sweep response stays bounded and remains separate from the written task document. [3]
