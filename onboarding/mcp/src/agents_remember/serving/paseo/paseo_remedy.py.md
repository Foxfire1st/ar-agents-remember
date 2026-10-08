# mcp/src/agents_remember/serving/paseo/paseo_remedy.py

## Governing Overview

[overview](../overview.md)

## Purpose

The explicit configured terminal transition when a live host cannot migrate in place.

## Code Commentary

`terminal_provision_remedy` builds the `agents-remember paseo provision --config <file>` command from the settings' command config path (a placeholder when none is known) and states that it runs outside the host and ends agent sessions, running turns and pending prompts.

## Evidence

- The terminal remedy text. [1]
