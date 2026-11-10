# mcp/src/agents_remember/kernel/primitives/mcp_settings_location.py

## Governing Overview

[overview](overview.md)

## Purpose

Names the one location of the MCP tool-server settings file (the authority file that carries `coordinationRoot` and `paseoRuntime`): `agents-remember-settings.json` in the user's Agents Remember config directory, beside the user's role settings file.

## Code Commentary

`mcp_settings_path()` takes `user_settings_path()` (`$XDG_CONFIG_HOME/agents-remember/settings.json`, or `~/.config/agents-remember/settings.json` when `XDG_CONFIG_HOME` is unset) and swaps the file name, so the two files share a directory but stay separate authorities. A relative `XDG_CONFIG_HOME` raises `UserSettingsLocationError` from the user-settings helper; this module adds no check, reads nothing and creates nothing.

Two callers use it: `cli.discovery.discover_config` selects this file independently of the working directory when no `--config` is given, and `install.mcp_settings.copy_mcp_settings` creates it once from the workspace's older `.claude/mcp/agents-remember-settings.json`. `application.user_settings_init` writes only the role settings file and never this one.

## Evidence

- The MCP settings file is the user settings path with the file name `agents-remember-settings.json` [1]
- The user settings path comes from `XDG_CONFIG_HOME` or `~/.config` and refuses a relative `XDG_CONFIG_HOME` [2]
- Command-line discovery selects this one user-config file and refuses it without an existing absolute `coordinationRoot` [3]
- Install copies the older workspace settings file to this location only when the destination is absent [4]
