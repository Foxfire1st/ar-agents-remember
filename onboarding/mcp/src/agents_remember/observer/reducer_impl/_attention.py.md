# mcp/src/agents_remember/observer/reducer_impl/_attention.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pure deterministic attention ranking over provider, drift, setup and worktree-start occurrences, with no session-stale/lifecycle alarm builder.

## Code Commentary

`build_attention_queue` sorts by severity, descending wait and ID and suppresses matching current acknowledgements. Provider/setup/start occurrences end through complete native-reader recovery/removal proof; unknown health or a missing projected node is not recovery. Drift uses actionable fingerprints: equal or missing fingerprints preserve acknowledgement; changed complete findings can resurface. A later timestamp alone is not a new occurrence. Worktree debt remains independently operational, not a synthesized session status.

## Evidence boundary

This account is current source interpretation only. It creates no executed test/host/bootstrap result and supplies no new CODE or MEMORY grade.
