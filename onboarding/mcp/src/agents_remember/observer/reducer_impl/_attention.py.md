# mcp/src/agents_remember/observer/reducer_impl/_attention.py

## Governing Overview

[overview](../overview.md)

## Purpose

Attention queue: rank what needs the human from the reduced surfaces. Pure and deterministic: every source contributes one small builder and the queue sorts by (severity, wait, id). Dismissals suppress lifecycle-bound items until a newer triggering signal re-surfaces them.

## Code Commentary

- `_ask_text`
- `build_attention_queue`
- `_is_dismissed`
- `_signal_after`
- `_await_summary`
- `_lifecycle_attention`
- `_gate_node`
- `_attach_gates`
- `_gate_attention`
- `_provider_attention`
- `_drift_attention`
- `_drift_attention_detail`
- `_setup_attention`
- `_start_attention`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/observer/reducer_impl/_attention.py`.

## Evidence

### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.
