# mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_view.py

## Governing Overview

[Owning overview](overview.md)

## Purpose

Physical code execution views for selected preparation, bound to the canonical logical memory pair.

## Code Commentary

### Logic

Observation requires an already selected original output, reloads typed stored objects, rechecks raw commit and physical Git facts, and binds the canonical logical pair to the actual read root. `prepare_code_view` performs preparation first; `observe_prepared_code_view` only reopens the existing view. Neither fabricates historical memory attribution for an in-flight pair.

`observe_selected_prepared_code_view` can reprove a journal-selected output after the running worker has returned. It validates the selected record and uses the same kernel observers instead of claiming a live worker lease. Existing code is checked with a strict `ExistingGitPreparationBinding`; created code uses the named private capability and a callback that reopens the original record and policy. Both paths remain code-domain checks, even if a file happens to be called memory.md.

### Conventions

Use the named source owners directly. This source was introduced in landed commit `245057ab16e19afdaabd5c188c9576b22e0c0870`. The earlier introduction and verification records remain historical facts; the current uncommitted candidate changes the behavior described here. The existing commit-verification metadata is retained until its owner records a real committed source revision.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

Physical code execution root and logical code/memory pair identity are separate facts. The memory cache option cannot relax this code view, and a constructed view is not a replacement for its selected raw output or owning journal.

### Todos

No additional source-local TODO is asserted by this maintenance pass.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

No external domain source is configured.

### Repo-Internal References

These source owners establish the behavior and boundaries above. Citation ranges were read from the current uncommitted candidate.

- The running-owner observation reloads the selected output and builds a bound physical view. [1]
- The selected-record path reuses strict existing-code or sealed private-code proof without inventing a worker lease. [2]
- Selected record and intent currentness are rechecked around observation. [3]
- The execution view binds the exact output bytes, raw commit/tree, and logical pair. [4]
- Preparation precedes a fresh observation when the caller requests a prepared view. [5]

### Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

No distinct cross-repository evidence source is configured for this file.
