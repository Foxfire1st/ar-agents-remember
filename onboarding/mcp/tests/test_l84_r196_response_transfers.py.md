# mcp/tests/test_l84_r196_response_transfers.py

## Governing Overview

[overview](overview.md)

## Purpose

Proves that the field tables of the Curator worklist reference (`skills/l-01-agent-lifecycles/reference/curator/worklist.md`) name exactly the fields of the `knowledgeWorklist` and `knowledgeGate` blocks a memory-quality result actually carries, and that the bounded answer leaves both blocks out.

## Code Commentary

`documented_fields` reads the backticked first-column names from the reference's tables before and after the sentence "`knowledgeGate` is the compact gate judgment.". `proof_cases` builds the whole result from `knowledge_briefs` for a complete and an incomplete worklist, each with a passing and a refused `GateResult` (open item, incomplete run and validator findings plus one report-only finding), and the bounded answer from `quality_result_answer`.

- In every case the worklist block has exactly the six documented fields and the gate block exactly the ten, with the counts and states the gate result implies.
- An absent computation yields no block, and the bounded answer omits both knowledge blocks while still naming the report and attestation paths.

The module locates the reference from `Path.cwd()`, so it must run from the repository root.

## Evidence

- Documented field names are read from the reference's two tables. [1]
- Proof cases cross worklist completeness with passing and refused gates. [2]
- Every documented field matches the actual whole result. [3]
- Absent computations are absent blocks and the bounded answer names only the artifacts. [4]
- The reference is located from the current working directory. [5]
