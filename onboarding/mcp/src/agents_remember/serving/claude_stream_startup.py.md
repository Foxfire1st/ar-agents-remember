# claude_stream_startup.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_startup.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash | `38c3fd81bdf851dce96e9b2b14e2bff741e7b383` |
| lastVerifiedCommitDate | 2026-07-21T11:31:07+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns the ordered Claude stream-json startup negotiation: structured initialize plus synthetic
non-query bootstrap first, followed by token-free dynamic model-catalog enumeration before the
steady-state reader takes ownership of stdout.

## Code Commentary

### Logic

`_StartupCollector` accepts only the correlated control initialization, matching `system/init`, and
successful synthetic bootstrap result needed for protocol readiness. `negotiate_claude_startup`
bounds that collection with a timeout. `negotiate_claude_catalog` then sends `list_models`, reads one
correlated response, and delegates normalization to the catalog parser using the current model from
`system/init` — and, since 260718-CHATS-L5F R2, also threads the caller's requested launch key
(`expected_launch.model_key`, passed by `harness_control_claude`) into the parser's
`_select_current_model` so that when several catalog rows share one `resolved_model`, current-model
selection resolves to the requested alias rather than collapsing onto the default alias.

### Conventions

Stable local request ids make fixture and runtime correlation explicit. Timeout is only a bound on
waiting; it never substitutes for a required frame. Catalog negotiation completes before any
long-running state-reader task starts.

### Invariants And Boundaries

- Startup and catalog enumeration submit no model query or visible user prompt.
- The current model must be reconciled with the returned catalog by the parser; no default is guessed.
  When a requested launch key is known it is threaded to the parser so a resolved-model collision
  resolves to the requested alias, not the default (R2).
- Disconnect, timeout, or an unexpected frame fails loudly. Pane, prompt, log, and timing heuristics
  are not readiness or catalog evidence.
- Exact CLI versions are fixture evidence only, not a production gate.

### Todos

None known for L1; launch-model/effort flags are owned by the later launch leaf.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The protocol module provides the exact frames and the catalog module performs model-local
normalization.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Initialize, non-query bootstrap, and `list_models` frame shapes are explicit protocol primitives. | L56-L82 | [claude_stream_protocol.py](claude_stream_protocol.py) |
| The catalog parser returns a normalized snapshot only after current-model reconciliation. | L15-L31; L85-L97 | [claude_stream_capabilities.py](claude_stream_capabilities.py) |

## Cross-Repo References

No external repository boundary is implemented by startup negotiation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R2 — `negotiate_claude_catalog` threads the
  caller's requested launch key into `parse_list_models_response` so current-model selection compares
  like-for-like when catalog rows share a `resolved_model` (the claude `opus[1m]` refused-pair fix
  seam). Verification metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: documented ordered dynamic catalog
  negotiation before the stdout reader, token-free discovery semantics, and current-model
  reconciliation; replaced obsolete exact-version language.
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
