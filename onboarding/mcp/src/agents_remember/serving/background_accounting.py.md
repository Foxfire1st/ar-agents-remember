# mcp/src/agents_remember/serving/background_accounting.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Attribute actual executing-thread CPU and wall intervals to every wired serving owner, record projector wake reasons/domains/paths, and expose cumulative plus trailing diagnostics. Bounded detail and monotonic aggregate buckets report incomplete cutoff windows honestly; process share is context, not owner CPU. Offloaded cancellation drains the worker and synchronous publication is separately measured.

## Code Commentary

Attribute actual executing-thread CPU and wall intervals to every wired serving owner, record projector wake reasons/domains/paths, and expose cumulative plus trailing diagnostics. Bounded detail and monotonic aggregate buckets report incomplete cutoff windows honestly; process share is context, not owner CPU. Offloaded cancellation drains the worker and synchronous publication is separately measured.

The retained catalog has nine labels: projection, landing-refresh, terminal-observation, metrics, held-delivery, river-compaction, warmup, event-tail and startup. The terminal-observation label now accounts for the retained leaf archive recovery loop; it does not revive terminal refresh. L113 removed the agent-notifier, relay-death-watch and conversation-ingestion record sites, so their unused constants and catalog entries are absent. Surviving accounting and budgets remain governed by the existing owners.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- Nine retained labels account for wired serving work after three retired record owners were removed; actual executing-thread CPU, bounded detail, honest incomplete windows and worker drain remain the existing accounting contract. [1]
