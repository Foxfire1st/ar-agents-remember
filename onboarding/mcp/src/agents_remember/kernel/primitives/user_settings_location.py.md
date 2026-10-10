# mcp/src/agents_remember/kernel/primitives/user_settings_location.py

## Governing Overview

[overview](overview.md)

## Purpose

The single user settings location and the refusal of its removed predecessor.

## Code Commentary

`user_settings_path` resolves `agents-remember/settings.json` under `XDG_CONFIG_HOME` or `~/.config`, refusing a relative override. `require_user_settings_path` refuses when the old coordination file exists — alone or beside the new file — naming both paths and the explicit upgrade command without reading or migrating contents. The starter generator emits these same stdlib-only definitions before AR is installed.

## Evidence

- The single user settings path under XDG_CONFIG_HOME or the standard user config directory. [1]
- The old-location refusal naming both paths and the upgrade command. [2]
