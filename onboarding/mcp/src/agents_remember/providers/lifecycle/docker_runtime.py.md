# mcp/src/agents_remember/providers/lifecycle/docker_runtime.py

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`docker_runtime.py` owns the shared Docker adapter helpers used by CGC and
GrepAI lifecycle modules.

## Code Commentary

Container inspection returns no snapshot for a nonzero inspect command, malformed JSON, or an empty/non-list payload; a missing Docker executable remains a typed provider error. Missing state yields explicit missing/unknown fields instead of a healthy container. Timestamp parsing truncates fractional seconds to microseconds, normalizes UTC, and treats zero/invalid timestamps as unknown; uptime cannot be negative. cit:([`docker_command`; `docker_inspect_container`; `docker_container_state_summary`; `parse_docker_timestamp`], mcp/src/agents_remember/providers/lifecycle/docker_runtime.py:18-22; mcp/src/agents_remember/providers/lifecycle/docker_runtime.py:25-37; mcp/src/agents_remember/providers/lifecycle/docker_runtime.py:47-67; mcp/src/agents_remember/providers/lifecycle/docker_runtime.py:84-107).

### Logic

The module resolves the Docker executable, inspects containers and images,
reads published port and mount metadata, normalizes container state summaries,
normalizes host paths, reads the set of networks a container is connected to,
checks local image presence, and waits for FalkorDB ping health. Container summaries
include Docker state, running flag, normalized `startedAt`, computed uptime
seconds, and health status.

### Invariants And Boundaries

- Docker absence is an error; provider lifecycle code must not fall back to
  host binaries.
- The helpers expose Docker facts and requested mutations, but provider-owned
  modules decide what those facts mean.
- Container-state helpers are fact normalization only; current provider state
  aggregation lives in `providers/current_state.py`.
- FalkorDB ping polling is shared here because it is Docker health plumbing for
  the CGC backend container.

## Evidence

### Repo-Internal References

- CGC backend lifecycle uses Docker inspection, container-state summaries, mount matching, image locks, and FalkorDB ping polling. [1]
- GrepAI backend, embedder, and runner lifecycles use Docker inspection, container-state summaries, and network helpers. [2]
