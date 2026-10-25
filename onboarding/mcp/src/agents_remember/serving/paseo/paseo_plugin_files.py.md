# mcp/src/agents_remember/serving/paseo/paseo_plugin_files.py

## Governing Overview

[overview](../overview.md)

## Purpose

Owns AR-managed plugin copy, embed list and loaded-content stamp inside the configured daemon home.

## Code Commentary

`publish_role_agent` is the sole role-facts writer. It holds one facts-file lock across read/filter/merge and atomic replacement of `agents-remember/role-agents.json`; the plugin reads these facts and publishes host activity separately. Readable host publication stamps registration with bootId and UTC time. Prior same-boot ended facts without close time, or eventAt <= registration time, cannot prune that registration; later ends or a different boot may reclaim it on publication. The current agent’s supplied registration is then merged. Missing publication does not invent an end. Filesystem trouble returns false; unchanged merged facts avoid replacement, though renewed registration time can change the record. Python filters valid stored facts; malformed present plugin input is not silently declared healthy. Facts-file replacement is not atomic with host publication/native launch and acknowledges neither plugin consumption nor turn-end delivery.

The managed plugin copy lives in home/agents-remember rather than directly at the source path. `sync_plugin_copy` and `write_embed` write only differing content; `tree_digest` hashes owned local bytes. The provisioner computes local plugin/embed hashes, checks the CLI reports the plugin running, then calls `write_loaded_stamp` with those expected hashes. This is a local bookkeeping stamp, not a plugin-confirmed byte/hash acknowledgement or proof of live consumption. Plugin UI implementation belongs to its source slice; no live acknowledgement was executed here.

L96: the module moved from `cli/paseo_plugin_files.py` into `serving/paseo/`; its package-data source root now resolves two parents up with `parents`.

## Evidence

- The home-owned plugin files and their content checks. [1]
