# mcp/src/agents_remember/serving/paseo/paseo_node.py

## Governing Overview

[overview](../overview.md)

## Purpose

Fetches, verifies and atomically places the release-owned Node and never uses the shell's Node.

## Code Commentary

`ensure_node` accepts an existing valid target (reclaiming any owned partial archive or unpack staging first) and otherwise downloads under a bounded timeout, compares the archive SHA-256 with the contract, unpacks beside the target and renames it into place as one move. A foreign folder at the target is refused and never overwritten. Acquisition and existing-target failures after `product_node()` has selected a runtime are named `PaseoRuntimeFailure`s carrying version, platform, path, URL and cause; the two precondition refusals that happen before selection name their own facts instead — an unsupported platform (`node_platform_unsupported`) names the observed system and machine, and an invalid XDG value (`xdg_path_invalid`) names the variable and path.

`node_status` is a read-only comparison of the observed owned host executable with the absolute contract Node path. It reports the expected Node, observed executable and a Node restart requirement only when an observed executable differs; installed target presence does not hide an older running Node. Both public status paths consume this same result.

## Evidence


- The acquisition entry point with exclusion and reclamation. [1]


- The verified whole placement. [2]


- The bounded download. [3]


- The shared read-only Node mismatch comparison. [4]
