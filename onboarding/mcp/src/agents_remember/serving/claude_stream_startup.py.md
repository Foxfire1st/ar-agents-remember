# claude_stream_startup.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns the ordered Claude stream-json startup negotiation: structured initialize plus synthetic
non-query bootstrap first, followed by token-free dynamic model-catalog enumeration before the
steady-state reader takes ownership of stdout.

On an install at or above the sub-agent-text floor the adapter runs this negotiation TWICE — once per
launched process — over the same transport object, because the floor verdict is only provable from the
first `system/init`. Both passes read frames inline; the long-running state reader starts only after
the surviving pass, so nothing else competes for stdout during either negotiation or the stop between
them.

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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

No configured domain documentation could be checked.

### Repo-Internal References

The protocol module provides the exact frames and the catalog module performs model-local
normalization.

- Initialize, non-query bootstrap, and `list_models` frame shapes are explicit protocol primitives. [1]
- The catalog parser returns a normalized snapshot only after current-model reconciliation. [2]

### Cross-Repo References

No external repository boundary is implemented by startup negotiation.

No meaningful cross-repo references found.
