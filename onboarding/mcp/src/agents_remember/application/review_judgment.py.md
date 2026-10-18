# mcp/src/agents_remember/application/review_judgment.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Project the selected invariant or family’s leaf-history judgments and proofs into one existing subject-review answer.

## Code Commentary

`review_judgment` requires an invariant/family selection, reports legacy/no-subject cases as unavailable, resolves raw identity from after with identity-only before fallback, and reads that leaf’s after-tree rows. `_answer` includes the raw subject and membership:<subject>, sorts by attempt then row ID, and preserves every selected attempt, including no_impact. Each projected row carries attempt, row/subject, disposition, optional effect/revision, reason, because, covered-entry or examined-member count, history path and closed flag. The three states are rows, none with the fixed no-judgment sentence, or unavailable with a reason. Proofs are attached after an unavailable history result too when the index remains readable; this is independent proof-entry currentness, not inference from a test result. No judgment is written.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. Requirement packets are task authority, not an implementation proof or a fresh acceptance.

### Repo-Internal References

- The same after-tree resolution supplies leaf judgment rows and proof currentness. [1]
- Raw and membership subjects include all attempts and distinguish rows/none/unavailable. [2]
- The row carries authored reason/because, counts and attempt-file provenance. [3]
