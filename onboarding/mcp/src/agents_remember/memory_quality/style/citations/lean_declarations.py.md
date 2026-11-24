# mcp/src/agents_remember/memory_quality/style/citations/lean_declarations.py

## Governing Overview

[Overview](../../overview.md)

## Purpose

Find the names and inclusive line extents of source-written Lean declarations.

## Code Commentary

The scanner tracks command indentation, declaration keywords and their attached documentation, attributes and command wrappers. The declaration keyword line is separate from the first attached line. Recognized peer commands end the open extent. Continuations keep it open, and trailing blank and comment lines are trimmed. An unnamed instance ends the previous extent without supplying a name.

## Relationships

The scope walker supplies namespace parts for qualification. A `_root_` name bypasses namespace qualification. Each declaration receives a full name when every retained scope gives it the same qualification.

## Evidence

- `declarations` scans the masked physical lines and emits named source extents. [1]
