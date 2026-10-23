# mcp/src/agents_remember/observer/reducer_impl/_attention.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pure deterministic attention ranking over the provider, drift, setup and worktree-start occurrences and the five native kinds — permission wait, held message, stalled task, landed notice, abandoned notice — that `_attention_native.py` builds from the task, host, held-store and terminal facts of the pass, with no session-stale/lifecycle alarm builder.

## Code Commentary

`build_attention_queue` sorts by severity, descending wait and ID and folds only dismissible rows against matching current acknowledgements: a live native cause keeps its place whatever the acknowledgement store holds, because it clears only when its own cause ends. Provider/setup/start occurrences end through complete native-reader recovery/removal proof; unknown health or a missing projected node is not recovery. Drift uses actionable fingerprints: equal or missing fingerprints preserve acknowledgement; changed complete findings can resurface. A later timestamp alone is not a new occurrence. Worktree debt remains independently operational, not a synthesized session status.

## Evidence boundary

This account is current source interpretation only. It creates no executed test/host/bootstrap result and supplies no new CODE or MEMORY grade.
