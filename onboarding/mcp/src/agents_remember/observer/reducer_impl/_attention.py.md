# mcp/src/agents_remember/observer/reducer_impl/_attention.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pure deterministic attention ranking over retained lifecycle, provider, drift, setup and worktree-start facts. Gate/ask/await-summary attachment builders are removed.

## Code Commentary

build_attention_queue uses server-computed ages and a total severity/wait/id order. Matching acknowledgements suppress the current triggering signal; a newer signal resurfaces, while targetless suppression belongs only to actionable drift. Enclosure debt remains with the hangar, and a quiet event-backed lifecycle differs from a synthesized paused worktree. Provider, setup and blocked-start alarms keep their own provenance instead of recreating gate/inbox nodes.

## Evidence boundary

This account is current source interpretation only. It creates no executed test/host/bootstrap result and supplies no new CODE or MEMORY grade.

