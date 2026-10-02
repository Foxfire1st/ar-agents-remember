# mcp/src/agents_remember/application/memory_quality/converted_base.py

## Governing Overview

[Application overview](../overview.md)

## Purpose

**The `knowledge.converted` check's comparison base: one base for every consumer (MIK-R24 rule 7; L37 review
R3-1).** The memory-quality run validates the converted working tree against the memory worktree's `HEAD`. When
`HEAD` is unconverted (the converting leaf before its closeout, or a line that has crossed) the base must be `HEAD`'s
conversion, exactly as the gate, the worklist and the writer see it. Then a carried reference to a file the
candidate deleted or moved is reported (`R22.6-carried-stale`), not refused as a newly written anchor
(`R22.6-anchor-path`).

## Code Commentary

### Logic

- `_port(code)` wraps `knowledge_writer.base_side.writer_bases` as a `KnowledgeBasePort`: `(memory root, candidate)
  -> (base, problem)`.
- `converted_check_base(scope, coordination_root)` is the port of a memory-quality run: the code root is the
  scope's quality code root, the fallback is the contract's code base commit B when the scope has a contract, and
  the cache is the coordination root's shared converted-base cache.
- `context_check_base(code_root, context)` is the port of a run that holds a coordination context (the closeout's
  quality phases and the prepared certification). B is the code base of the contract the context names, when it
  names one. A context without a coordination root (a bare diagnostic) gets no port, and the check then uses a
  converted `HEAD`.

### Conventions

- The port exists because `memory_quality/converted_check.py` ranks below the application layer and cannot reach
  the converted-base cache; the application binds it through `DriftCheckContext.knowledge_base`.

### Invariants And Boundaries

- The port holds no conversion logic of its own. It calls `writer_bases`, which reads the shared converted-base
  cache under the same key (memory commit, version, K_B's own `Code-Commit` or B) as the other readers. On a cache
  miss that call runs the conversion and stores it, so whichever reader runs first converts.
- A base that cannot be built comes back as the problem text, which the check reports as the refusing finding
  `R24.7-converted-base`.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R24@v1` rule 7 and the L37 decision of 2026-10-01T11:12:11 (R3-1) in `37_cutover-to-text-storage.json`; it lives outside the code and memory
repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: one base for every consumer of the converted check. [1]
- The base port of a memory-quality run. [2]
- The base port of a run that holds a coordination context; none without a coordination root. [3]
- The memory-quality run passes the port into the drift context. [4]
- The check's side of the port: its bases, and an unbuildable base as a finding. [5]

### Cross-Repo References

No meaningful cross-repo references found: the module binds two same-repository modules.

No cross-repo boundary is crossed by this file.
