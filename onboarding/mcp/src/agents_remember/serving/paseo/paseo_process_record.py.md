# mcp/src/agents_remember/serving/paseo/paseo_process_record.py

## Governing Overview

[overview](../overview.md)

## Purpose

Proves that the home process record names that home's Paseo supervisor.

## Code Commentary

inspect_record combines recorded PID with live process command/cwd facts. Stale records may be removed only under their classified state; foreign or unreadable process identity is refused. This protects home-addressed native stop/start, whose upstream PID check alone does not prove home ownership.

The Paseo 0.11.1 stop description is boot-identity-first: a record from another boot is abandoned, with the older age check used when boot identity is unavailable. That upstream liveness rule still does not prove that a reused PID belongs to this home; the product's independent process-identity check remains necessary. A record from the older release has no boot id and follows the fallback, not a new product compatibility branch.

L96: the module moved from `cli/paseo_process_record.py` into `serving/paseo/`. `read_process` now also records the process executable (`/proc/<pid>/exe`) and the carried session-variable names through the product's `carried_session_variables`, which the start/status outcomes report without values.

## Evidence

- The home record trust rule remains an independent check of the recorded PID's actual home and process. [1]
- The process facts include executable and session-variable names, never values. [2]
- The module describes the 0.11.1 boot-id-first stop predicate without treating liveness as proof of home ownership. [3]
