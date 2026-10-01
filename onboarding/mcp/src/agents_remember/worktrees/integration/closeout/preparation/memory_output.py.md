# mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py

## Governing Overview

[Owning overview](overview.md)

## Purpose

Prepare code and memory-content outputs after memory certification, without publishing logical refs.

## Code Commentary

### Logic

`PreparedMemoryOutputs` carries the handoff plus exactly code and memory outputs. `_MemoryIntentSelection` supplies the memory parent, admitted tree, existing proof, and write decision. `prepare_memory_outputs` reopens current certification, selects the genuine code output, and either creates memory content or retains the actual existing memory HEAD. No ledger output, mapping lookup, ledger blob comparison, or third preparation leg remains.

For a created memory output, `_intent` renders `normalizedMessage` through the kernel's one `Code-Commit` renderer against the candidate's code commit. The stored message is exactly what private execution uses and finalization publishes; attribution is inside the hashed object. For a no-write output the message and private root are absent, so an unchanged memory HEAD can be reused even when a memory write/message is not enabled.

Existing reuse keeps the historical raw HEAD tree as `admittedTree` and separately carries `existingMemoryProof.certifiedContentTree`. The kernel reproves that only root memory.md separates these trees. Created memory uses the cache-free certified tree directly. Each selected memory intent retains its exact Gate-5 certificate, and previously selected outputs are physically reproved.

Only a real write-enabled output stages the logical memory content. Staging uses `MEMORY_CACHE_EXCLUDE`, removes the cache from the real index, requires the staged tree to equal the certified candidate, and reopens current certification again. These index changes do not advance either logical branch.

### Conventions

Use the named source owners directly. The earlier introduction and verification records remain historical facts; the current uncommitted candidate changes the behavior described here. The existing commit-verification metadata is retained until its owner records a real committed source revision.

### Invariants And Boundaries

The memory-content message uses the single kernel renderer; nothing appends attribution after the selected message or commit object is created. Existing raw HEAD/tree identities must never be relabelled as the cache-free certificate subject. New private memory output must exclude the cache, while unchanged historical memory is reused without a synthetic mapping-only commit.

The inspected production tree still has no caller of `certification/execution.execute_selected_closeout`. The committed producer census checks the renderer call; neither that census nor focused disposable boundary checks establish a public end-to-end certification result. The owning runtime evidence is required for execution, delivery, or acceptance claims.

### Todos

No additional source-local TODO is asserted by this maintenance pass.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

No external domain source is configured.

### Repo-Internal References

These source owners establish the behavior and boundaries above. Citation ranges were read from the current uncommitted candidate.

- The bundle has code and memory outputs only. [1]
- Created memory uses the one renderer; no-write intent has no message or private root. [2]
- Memory attribution is appended to the caller's body by one shared renderer. [3]
- Selected output is reobserved, with actual existing HEAD bytes reused for no-write memory. [4]
- Output selection binds raw legacy trees separately and stages only certified non-cache content for actual writes. [5]
- The stored normalized message becomes the private commit message. [6]
- The committed census checks that every listed producer reaches the shared renderer. [7]

### Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

No distinct cross-repository evidence source is configured for this file.
