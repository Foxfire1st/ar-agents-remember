# mcp/src/agents_remember/serving/paseo/paseo_remedy.py

## Governing Overview

[overview](../overview.md)

## Purpose

The explicit configured terminal transition when a live host cannot migrate in place.

## Code Commentary

`provision_command` constructs `agents-remember paseo provision --config` with the shell-quoted active settings file, or the explicit active-file placeholder. `terminal_provision_remedy` wraps that same command with the outside-host restart/session-loss warning; `frame_descriptor` exposes the raw command for an older-plugin notice. Neither helper executes it.

## Evidence

- The terminal remedy text. [1]

## Current contract evidence

- `provision_command` constructs `agents-remember paseo provision --config` with the shell-quoted active settings file, or the explicit active-file placeholder. `terminal_provision_remedy` wraps that same command with the outside-host restart/session-loss warning; `frame_descriptor` exposes the raw command for an older-plugin notice. Neither helper executes it. [2]
