# mcp/tests/tool_entry_point_world.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

The one world the tool entry-point tests drive.

## Code Commentary

It builds the fixture world, calls registered tools through it and closes its sessions so the sweep and progression tests share one owner.

## Evidence

- The file realizes its current contract at the corrected candidate. [1]
