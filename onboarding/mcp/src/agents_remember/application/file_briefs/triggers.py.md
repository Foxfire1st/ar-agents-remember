# mcp/src/agents_remember/application/file_briefs/triggers.py

## Governing Overview

[Area overview](../overview.md)

## Purpose

Refreshes derived source briefs after admitted writes to converted memory.

## Code Commentary

A full refresh uses the resulting memory tree and the writing operation's paired code commit. A touched refresh maps changed cards and records to source paths, including former record locations when the earlier index is available. Both require effective Git exclusion of `briefs/`. The mapper includes ordinary source files named `overview.py`.

## Evidence

- The post-write hook refreshes current sources and uses former locations when the earlier index is available. [1]
- The source mapper skips the exact route artifact names and keeps ordinary source-file names. [2]
