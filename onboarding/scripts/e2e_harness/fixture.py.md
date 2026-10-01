# fixture.py

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Builds the disposable repository, coordination topology, canonical task documents, architect brief,
runtime settings, and Codex/MCP configuration needed for each clean-room replication.

## Code Commentary

### Logic

`create_fixture` lays out isolated code, memory, coordination, Codex-home, and tmux roots. It compiles
the real architect template from canonical doctrine, writes validated task topology and settings,
initializes the disposable Git repository, and points Codex at the deterministic Responses server
plus candidate MCP command. The generated MCP registration explicitly whitelists the dynamic
`TMUX_TMPDIR`, so Codex's stdio child creates role sessions in the same fixture-owned tmux server
used by liveness checks and teardown.

### Conventions

Fixture paths are deliberately short because hosted control uses Unix sockets. Generated values are
explicit inputs to the returned frozen `E2EFixture`; later phases do not rediscover them by scanning.

### Invariants And Boundaries

- The architect brief is compiled from the canonical template, never duplicated as fixture prose.
- The fixture MCP command addresses the candidate checkout and project-owned Python runtime.
- The candidate MCP inherits `TMUX_TMPDIR`; omission would split session creation from the
  fixture's liveness and cleanup namespace.
- Production starter behavior is not rewritten by this test configuration.
- All repositories and ports are run-local and disposable.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

- The fixture uses repository-owned task and template contracts as its authority. [1]

### Repo-Internal References

- Fixture construction returns every run-owned path and canonical task address explicitly. [2]
- Codex config binds the deterministic Responses endpoint, candidate MCP server, and fixture tmux namespace. [3]

### Cross-Repo References

No live sibling repository supplies fixture behavior.

- Disposable repositories are initialized inside the run root. [4]
