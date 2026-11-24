# mcp/src/agents_remember/serving/paseo/paseo_plugin_files.py

## Governing Overview

[overview](../overview.md)

## Purpose

Owns AR-managed plugin copy, embed list and loaded-content stamp inside the configured daemon home.

## Code Commentary

`publish_role_agent` and `reconcile_role_agents` share one facts-file lock for read, comparison, merge and atomic replacement of `agents-remember/role-agents.json`. Registration writes UTC time and the current boot ID when available. A positive archive can reclaim a row when its archive timestamp is strictly newer than the stored registration, regardless of boot. An older row without a usable registration time can be reclaimed on positive archive evidence. A closed seat and a generic ended state without archive time supply no archive evidence. Reconciliation can also reclaim an unchanged row on exact absence after receipt judgment. Recovery supplies missing rows from receipts with the observation-start timestamp, and leaves concurrent registrations in place. The plug-in reads those facts and separately publishes host activity. Filesystem failure does not certify publication or delivery.

The managed plugin copy lives in home/agents-remember rather than directly at the source path. `sync_plugin_copy` and `write_embed` write only differing content; `tree_digest` hashes owned local bytes. The provisioner computes local plugin/embed hashes, checks the CLI reports the plugin running, then calls `write_loaded_stamp` with those expected hashes. This is a local bookkeeping stamp, not a plugin-confirmed byte/hash acknowledgement or proof of live consumption. Plugin UI implementation belongs to its source slice; no live acknowledgement was executed here.

L96: the module moved from `cli/paseo_plugin_files.py` into `serving/paseo/`; its package-data source root now resolves two parents up with `parents`.

## Evidence

- The home-owned plugin files and their content checks. [1]
