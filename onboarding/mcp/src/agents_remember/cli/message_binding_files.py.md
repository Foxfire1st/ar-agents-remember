# mcp/src/agents_remember/cli/message_binding_files.py

## Governing Overview

[Governing overview](../../../overview.md)

## Purpose

Owns canonical receipt projection bytes and equality checks for that saved file.

## Evidence

- The receipt projection uses compact sorted JSON and a final newline. [1]
- The helper distinguishes absence from an exact regular file and refuses other content. [2]
