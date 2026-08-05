# mcp/src/agents_remember/providers/lifecycle/docker_runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/docker_runtime.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00|
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`docker_runtime.py` owns the shared Docker adapter helpers used by CGC and
GrepAI lifecycle modules.

## Code Commentary

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| CGC backend lifecycle uses Docker inspection, container-state summaries, mount matching, image locks, and FalkorDB ping polling. | "def cgc_backend_ping" | mcp/src/agents_remember/providers/cgc/lifecycle/backend.py:122-122 |
| GrepAI backend, embedder, and runner lifecycles use Docker inspection, container-state summaries, and network helpers. | "def docker_wait_for_postgres", "def grepai_embedder_health", "class GrepaiStackResults" | mcp/src/agents_remember/providers/grepai/lifecycle/backend.py:51-51; mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py:137-137; mcp/src/agents_remember/providers/grepai/lifecycle/runner.py:340-340 |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B20 curator: replaced the `n/a` table rows with
  exact anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-05-31T12:30+02:00 — Dropped the "ensures Docker networks and network attachments" claim from Logic; the `docker_ensure_network` and `docker_ensure_container_network` mutation helpers were removed, leaving only the read-only `docker_container_networks` fact helper (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: `raise_docker_ping_timeout` -> `NoReturn` so `docker_wait_for_ping` type-checks on all paths; behavior-preserving (commit `0549b28`).
- 2026-05-28T12:32+02:00: Updated after Docker status helpers began emitting normalized container state, health, and uptime summaries.
- 2026-05-25T21:14+02:00: Created from the Docker adapter portion of the former shared lifecycle common module.
