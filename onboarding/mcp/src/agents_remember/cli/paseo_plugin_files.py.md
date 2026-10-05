# mcp/src/agents_remember/cli/paseo_plugin_files.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Owns AR-managed plugin copy, embed list and loaded-content stamp inside the configured daemon home.

## Code Commentary

The plugin is copied into home/agents-remember and loaded from that copy, not live source bytes. sync_plugin_copy and write_embed change only when content differs; tree_digest binds owned bytes. The loaded stamp records only content the running plugin confirmed. Plugin UI implementation itself belongs to the plugin source slice.

## Evidence

- Frozen implementation of sync_plugin_copy supporting the stated file behavior. [1]
- Frozen implementation of write_embed supporting the stated file behavior. [2]
- Frozen implementation of write_loaded_stamp supporting the stated file behavior. [3]
