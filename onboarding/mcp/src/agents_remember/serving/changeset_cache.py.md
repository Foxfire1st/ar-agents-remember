# mcp/src/agents_remember/serving/changeset_cache.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Own one serving app’s bounded cache of native change-set reads and conditional response envelopes. Retained values are accelerators, not alternative change-set computation or review authority.

## Code Commentary

A request captures consumed input generations and stages newly computed values until a fresh end-of-read observation agrees. Unreadable, changing or evicted inputs prevent retention. Reads outside the app-owned context compute normally. Cached values are deep-copied so annotations cannot corrupt subsequent callers.

Results, repository layouts/manifests and object observations each default to 1,024 LRU entries; pending results and observed input sets are bounded too. Working generations include the relevant repository metadata, configuration and filesystem observations; immutable-range reads still revoke reuse when required objects disappear or are replaced. A prior object-absence proof also observes additions. These are reuse keys, not Git interpretation.

Successful HTTP bodies receive content-derived weak ETags; matching conditional requests return 304 without the body. Initial discovery, invalidation and native computation may run Git. Input observation still does filesystem work; “unchanged” is not a zero-work claim.

## Evidence

- New results are admitted only when all captured inputs remain readable and equal after the request. [1]
- All three retained tables are bounded and LRU. [2]
- Reuse requires exact observed generations and returns isolated copies; otherwise native computation runs. [3]
