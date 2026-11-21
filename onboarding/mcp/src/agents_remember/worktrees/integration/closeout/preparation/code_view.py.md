# mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_view.py

## Governing Overview

[Owning overview](overview.md)

## Purpose

Physical code execution views for selected preparation, bound to the canonical logical memory pair.

## Code Commentary

### Logic

`observe_selected_prepared_code_view` reopens the exact journal-selected code intent and output, rechecks raw commit and physical Git facts, and binds the caller's logical pair to the physical read root. The observation creates no prepared output or memory attribution.

Existing code is checked with `ExistingGitPreparationBinding`. Created code uses the admitted private capability and an authorization callback that reopens the selected record and checks the bound policy. The evidence is the selected record and Git proof, independent of a worker lease or worker event. Both paths verify the code domain.

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


- The selected-record path reuses strict existing-code or sealed private-code proof without inventing a worker lease. [2]
- Selected record and intent currentness are rechecked around observation. [3]
- The execution view binds the exact output bytes, raw commit/tree, and logical pair. [4]


### Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

No distinct cross-repository evidence source is configured for this file.

- Selected-record read-only observation reloads the exact original output and constructs a physically proved logical-pair-bound code view. [1]

- Only exact selected-output reproof remains; the fresh prepare/running-handoff APIs were removed. [5]
