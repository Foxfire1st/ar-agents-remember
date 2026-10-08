# mcp/src/agents_remember/kernel/primitives/paseo_node_paths.py

## Governing Overview

[overview](overview.md)

## Purpose

Release-owned Node paths and the supported host platform.

## Code Commentary

`product_node` refuses any system, machine or /proc situation other than Linux x86_64, then builds the managed Node root beside the product's python and paseo folders and the archive cache under the user's cache folder from the contract's archive entry. `xdg_home` treats an unset or empty value as the home default and refuses a relative override instead of resolving it under the current working directory.

## Evidence

- The platform refusal and managed paths. [1]
- The unset-or-empty XDG default rule. [2]
