# mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py

## Governing Overview

[Owning overview](overview.md)

## Purpose

At-most-once journal-bound private Git execution for code and memory-content outputs.

## Code Commentary

### Logic

Each enabled code or memory-content output has the ordered create, materialize, and commit commands. These are command steps for one output, not three commit legs. There is no private ledger-output command in the current preparation model.

Each command start is selected before its single kernel call; actual exit/output hashes or unknown outcome are retained afterward. Live ownership and effective policy are reopened at action boundaries. Successful steps are not rerun, unresolved preparation is retained, and a named committed output is physically reobserved instead of discovering another commit. Shared execution does not advance logical branches.

### Conventions

Use the named source owners directly. This source was introduced in landed commit `245057ab16e19afdaabd5c188c9576b22e0c0870`. The earlier introduction and verification records remain historical facts; the current uncommitted candidate changes the behavior described here. The existing commit-verification metadata is retained until its owner records a real committed source revision.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

Private output proof stays strict over the complete admitted tree. The logical-memory cache projection belongs to existing-memory observation and finalization, not to this private checkout capability. A failed or unknown original commit may be inspected for its named output, but never rerun speculatively.

### Todos

No additional source-local TODO is asserted by this maintenance pass.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

No external domain source is configured.

### Repo-Internal References

These source owners establish the behavior and boundaries above. Citation ranges were read from the current uncommitted candidate.

- The selected leg must still match the retained intent. [1]
- The private binding retains the exact selected parent, admitted tree, message, and owner. [2]
- The capability reopens selection and actual private policy around commands. [3]
- Original commands are selected and their observed terminals retained once. [4]
- Output observation proves the named committed object and current policy. [5]
- Only an unstarted suffix runs; uncertain prior commands are retained for named-output recovery. [6]
- The selected intent supports only code and memory-content output legs. [7]

### Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

No distinct cross-repository evidence source is configured for this file.
