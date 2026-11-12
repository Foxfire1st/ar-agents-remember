# mcp/src/agents_remember/serving/changeset_cache.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Own one serving app’s bounded cache of native change-set reads and conditional response envelopes. Retained values are accelerators, not alternative change-set computation or review authority.

## Code Commentary

A request captures consumed input generations and stages newly computed values until a fresh end-of-read observation agrees. Unreadable, changing or evicted inputs prevent retention. Reads outside the app-owned context compute normally. Cached values are deep-copied so annotations cannot corrupt subsequent callers.

Results, repository layouts/manifests and object observations each default to 1,024 LRU entries; pending results and observed input sets are bounded too. Working generations include the relevant repository metadata, configuration and filesystem observations; immutable-range reads still revoke reuse when required objects disappear or are replaced. A prior object-absence proof also observes additions. These are reuse keys, not Git interpretation.

Successful HTTP bodies receive content-derived weak ETags; matching conditional requests return 304 without the body. Initial discovery, invalidation and native computation may run Git. Input observation still does filesystem work; “unchanged” is not a zero-work claim.


## Current Behavior

the module now documents its id-keyed accepted gap in its own docstring (object loss and working-tree attribute/configuration changes are not observed per hit; a hit is the true diff of its ids until eviction or restart). `ChangesetCache` retains only results and repository layouts (no manifest table); `_working_generation` uses `working_generation` (Git status) and returns an `UNKNOWN_STATUS` stamp when Git cannot describe the view. `Retention(keep=..., unknown=...)` lets a refusal settle on an unknown stamp but never a success (`:92-107`, `:132-170`). `_Read.objects` is an OrderedDict bounded by `capacity` (`:115-130`, R1-07); `_Read.finish` checks the `abandoned` event before, during and after admission and withdraws values it already admitted when the read is abandoned (`:132-170`, R1-02). The lock covers only the maps; `_layout`/`_object_revision` run outside it. This supersedes the earlier '1,024 results, repository manifests and object observations' sentence and the unqualified 'errors and changing/unreadable inputs never become reusable results': a refusal may be kept on an unknown stamp, and there is no manifest table.

## Evidence


- New results are admitted only when all captured inputs remain readable and equal after the request.


- All three retained tables are bounded and LRU. [2]


- Reuse requires exact observed generations and returns isolated copies; otherwise native computation runs. [3]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/changeset_cache.py:84-92 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit c861abfeff33c9ef8f1ca066604c8f971b613361. Retired means the anchor no longer stands, not that the cited subject was deleted.
