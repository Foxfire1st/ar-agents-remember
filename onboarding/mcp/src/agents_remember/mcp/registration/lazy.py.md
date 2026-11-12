# mcp/src/agents_remember/mcp/registration/lazy.py

## Governing Overview

[Route overview](overview.md)

## Purpose

A lazy view of the payload builders, so declaring a tool reaches no builder until a call does.

## Code Commentary

- Attribute access imports the payload-builder package on first use and no earlier, which is what keeps that package unloaded at discovery.
- A name the package does not re-export is looked for in the package's own submodules rather than reported missing from a package that simply never exported it.
- When no submodule carries the name, the package's own error is re-raised rather than a guessed module path being written.

## Evidence

- The builder package is imported on first attribute access and no earlier [1]
- A name the package does not carry is searched for in its own submodules, and the package's own error is re-raised when none has it [2]
- One lazy view is the module's whole surface [3]
