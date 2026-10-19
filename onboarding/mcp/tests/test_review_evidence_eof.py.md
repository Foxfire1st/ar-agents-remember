# mcp/tests/test_review_evidence_eof.py

## Governing Overview

[overview.md](overview.md)

## Purpose

The evidence reader's end-of-object cases: a bounded read that runs past the end of the object it reads ends at that last line and is complete, a remaining count is stated only where the read measured it, and no continuation leads at or past the end.

## Code Commentary

The five cases hold MIK-R182@v1 against the shipped reader rather than a stand-in. The six-line object read at lines 1–100 comes back `present` at line 6 with zero remaining, no continuation and no limit, and a detail that names that line; the 450-line object read at 1–1000 states page one's page-bound remainder as 50 known lines, then reaches the end on page two as `present` at line 450, and the concatenated continuations rebuild the object's exact bytes. A 64-byte window that never measured the object's end states its remainder as `unknown` with no count, while a read started at the object's end (its end offset, one past the last existing byte) and a read started one line past the end both get the measured range absence the scan already gives a start line past the end, never an empty line. The comparison world is the packet module's own `world` fixture, so the cases drive the landed owners instead of inventing side states; this module exists on its own because the packet module is already past the repository's armed file-size limit.

## Evidence

- The six-line object read at lines 1–100 is present at its last line, with no remaining line, continuation or limit. [1]
- A page that reaches the object's end is present at its last line, and the pages of its continuations rebuild the object's bytes. [2]
- A byte-capped window that never measured the end states its remainder as unknown, not as the requested difference. [3]
- A read started at the object's end gives the measured range absence, not an empty line. [4]
- A start line one past the object's end is also a measured range absence. [5]
