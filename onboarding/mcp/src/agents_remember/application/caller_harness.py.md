# mcp/src/agents_remember/application/caller_harness.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Name the host provider that is the calling chat's own harness, and report `None` when no offered provider is.

## Code Commentary

`normalize_harness_name` folds a client name to its comparable key: lower case, every run of non-alphanumerics a single dash, nothing around it; a non-string or an empty result is no name at all. `provider_for_caller` reads the MCP client name the transport reports in `initialize`, never an argument a caller sets, and compares it with the provider ids the host catalog offers: an equal key matches, a client name that says more than an id matches on its leading part, an id that says more than the client name matches on a whole dash-separated segment. No harness name is written in this module, so a launch names no harness of its own and AR invents none; a name matching nothing leaves the identity unknown, and unknown is reported as unknown rather than replaced by the first provider the host lists. The launch applies the answer in `cli.role_launch_request_rules.with_caller_harness`, which refuses a caller whose harness cannot be hosted by naming the harnesses the host can run.

## Evidence

- The comparable key a client name and a provider id are both folded to. [1]
- The one match rule: equal, leading part either way, or a whole dash-separated segment. [2]
- Maps a client name onto an offered provider and returns nothing when none matches. [3]
- A model-only bootstrap call is served on the calling chat's own harness, and a provider the bound harness does not offer is refused before a seat exists. [4]
