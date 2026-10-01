# mcp/src/agents_remember/providers/cgc/lifecycle/installation.py

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`installation.py` owns CodeGraphContext install, status, and doctor
operations.

## Code Commentary

### Logic

The module installs the CGC Docker runner image, cleans old source artifacts,
reports Docker-image patch status as a field of install/status/doctor results,
initializes runtime layout state, and runs doctor checks through the runner
image. Status now inspects the watcher container, requires it to be running for
`ok`, includes normalized container state, reports `lastRefresh` from runtime
state, and exposes an `indexingState` field for MCP current-state consumers.

`indexingState` comes from a real probe chain, not container liveness alone.
`cgc_indexing_state_probe()` first checks scan markers in the watcher's
container logs since container start: `Performing initial scan` without a
matching `Initial scan complete` means `indexing`. Otherwise
`cgc_graph_content_state()` queries the backend with `GRAPH.RO_QUERY`, counting
File nodes in the repo's graph, and classifies the result as `indexed`,
`empty`, `backend-unreachable`, or `unknown`. A running watcher over an empty
graph therefore reports `empty`, the state that exposed the 2026-06-09
silent-data-loss incident instead of masking it.
Install-all also coordinates backend installation and per-root install results
from settings. There is no longer a standalone public `patch` action: managed
patches are baked into the runner image during build, so patch state surfaces
only as a Docker-image marker within the install/status/doctor results. Host
site-packages patch inspection and host-venv patch application helpers have been
removed from this lifecycle path.

### Invariants And Boundaries

- Patches are owned by the Docker runner image build; status should report the
  Docker-image patch mode rather than inspecting host site-packages.
- CGC lifecycle code must not inspect, create, or patch a coordination-root
  host venv as an executable fallback.
- Runtime source artifacts under the code repository are cleanup targets; active
  provider runtime belongs under coordinator provider roots.
- Process start/stop and bounded CGC commands belong in sibling lifecycle
  modules and must use Docker runner commands.
- CGC status should not be ok when the runner image exists but the repo watcher
  container is not running.
- Graph content probes must use `GRAPH.RO_QUERY`, never `GRAPH.QUERY`: a plain
  query auto-creates an empty graph key as a side effect, so a read probe would
  manufacture the very `empty` state it is checking for.
- `redis-cli` exits 0 even when the server returns an error reply, so probe
  classification must inspect the reply text rather than trust the exit code.

## Evidence

### Repo-Internal References

- CGC layout and backend settings come from the CGC core module. [1]
- CGC backend install/start behavior is delegated to the backend module. [2]
- Docker runner image build and command helpers live in the runner module. [3]
