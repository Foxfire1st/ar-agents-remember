# mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py

## Governing Overview

[serving projections overview](../overview.md)

## Purpose

Current enclosure and Engine Room fact readers. This module no longer reads gates, inbox pickups or expectation rows.

## Code Commentary

read_enclosures and read_engine_process_facts reuse a supplied per-tick ContractSnapshot, skip malformed contracts and derive leaf-worktree ownership rather than presenting root integration contracts as live processes. Engine enrichment distinguishes contract/guidance, best-effort local Git status and immutable published landing facts. refresh_engine_process_landing updates only the volatile published landing tail while retaining the other computed inputs. Missing/broken status degrades explicitly instead of breaking the tick; current cached local status does not trigger a new remote observation.

## Evidence boundary

This account is current source interpretation only. It creates no executed test/host/bootstrap result and supplies no new CODE or MEMORY grade.

