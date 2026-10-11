# mcp/src/agents_remember/serving/paseo/paseo_plugin_files.py

## Governing Overview

[overview](../overview.md)

## Purpose

Owns AR-managed plugin copy, embed list and loaded-content stamp inside the configured daemon home.

## Code Commentary

`publish_role_agent` merges the started agent's role/task/reportPath into `agents-remember/role-agents.json` for the event-driven plugin. Unchanged records avoid a rewrite; filesystem trouble returns false instead of failing a role start. The Python reader filters valid fact records, whereas the plugin's TypeScript reader fails visibly for malformed present data. Fact publication is not proof that a live plugin loaded it or sent a turn-end line.

The managed plugin copy lives in home/agents-remember rather than directly at the source path. `sync_plugin_copy` and `write_embed` write only differing content; `tree_digest` hashes owned local bytes. The provisioner computes local plugin/embed hashes, checks the CLI reports the plugin running, then calls `write_loaded_stamp` with those expected hashes. This is a local bookkeeping stamp, not a plugin-confirmed byte/hash acknowledgement or proof of live consumption. Plugin UI implementation belongs to its source slice; no live acknowledgement was executed here.

L96: the module moved from `cli/paseo_plugin_files.py` into `serving/paseo/`; its package-data source root now resolves two parents up with `parents[2]`.

## Evidence

- The home-owned plugin files and their content checks. [1]
