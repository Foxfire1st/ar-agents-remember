# mcp/src/agents_remember/serving/paseo/paseo_plugin_files.py

## Governing Overview

[overview](../overview.md)

## Purpose

Owns AR-managed plugin copy, embed list and loaded-content stamp inside the configured daemon home.

## Code Commentary

The plugin is copied into home/agents-remember and loaded from that copy, not live source bytes. sync_plugin_copy and write_embed change only when content differs; tree_digest binds owned bytes. The loaded stamp records only content the running plugin confirmed. Plugin UI implementation itself belongs to the plugin source slice.

L96: the module moved from `cli/paseo_plugin_files.py` into `serving/paseo/`; its package-data source root now resolves two parents up with `parents[2]`.

## Evidence

- The home-owned plugin files and their content checks. [1]
