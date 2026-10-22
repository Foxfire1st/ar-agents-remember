# mcp/src/agents_remember/serving/paseo/paseo_daemon_config.py

## Governing Overview

[overview](../overview.md)

## Purpose

Writes private provider configuration and the daemon agent-tools setting.

## Code Commentary

Provider entries may contain environment secrets, so write_provider_entries writes the private config file rather than putting values on command lines. The preceding config and written digest support exact rollback; accept_provider_entries acknowledges confirmed native config. Recovery does not invent a second configuration store.

L96: the module moved from `cli/paseo_daemon_config.py` into `serving/paseo/`; only its intra-package imports changed.


**L184 — two links, two obligations.** The daemon read is this module's job, so the unread marker's origin is here (the report-only and port rules above). What this module adds for extra arguments is inspection of the host's configured `extraArgs` so a start can record what the host already carries; that part belongs to the extra-argument obligation, not to the usage-report rule, and it decides no limit. The daemon read is declared here as a port serving may call, and a failure names the harness whose map went unread — no cli import is made from this layer. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Evidence

- The private provider write with its rollback files. [1]
