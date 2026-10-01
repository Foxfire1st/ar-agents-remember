# mcp/src/agents_remember/application/runtime/startup.py

## Governing Overview

[overview](overview.md)

## Purpose

Initializes MCP-process application collaborators and owns the one application-layer gateway that
hands the MCP adapter its boot-resolved serving-build payload. Since `260915-KS-L23` it also owns the
**ruler stamp** the measuring surfaces carry, so a memory-quality or citation count says which build
produced it.

## Code Commentary

### Logic

`initialize_mcp_application` migrates recognized durable logs without the dashboard-owned notifier
log, then installs ambient lifecycle state. `mcp_serving_build_payload` converts the cached serving
stamp to the strict shared wire model at the application boundary; MCP registration never imports
the serving domain directly. Dashboard autostart remains a separate startup hook.

`measuring_build_stamp` (`:36-51`) is the second reader of that same process-cached identity, and it
exists because of the measurement D-33 recorded: the MCP surface answers a tool call from a **fixed**
serving build while the candidate under curation may carry different code, and until this stamp existed
a checklist reader could not tell a candidate-ruler count from a serving-build-ruler count. It returns
`{"servingBuild": <resolved payload as wire JSON>}` — a dict copy of the identity
`process_serving_build()` resolved once per process, not a probe — with `dirty` riding along so an
uncommitted serving tree reads as such instead of being taken for the commit it names. Its consumers are
the memory-quality controller's three public entry points and the two citation tools; the omission of
`drift_check` is deliberate, because a tree-integrity count is not a curation count.

### Conventions

Migration runs before any strict store can parse current records; ownership boundaries determine
which process may migrate which log.

### Invariants And Boundaries

- Migration is one-way, idempotent deployment work.
- MCP startup does not mutate the dashboard-owned notifier log.
- No dual-schema reader is installed.
- MCP transport reaches serving identity through this application entry point only.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- MCP startup migrates its owned logs before ambient installation. [1]
- The application boundary returns the one cached, strict serving-build payload. [2]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
