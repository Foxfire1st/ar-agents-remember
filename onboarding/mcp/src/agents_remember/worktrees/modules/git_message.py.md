# mcp/src/agents_remember/worktrees/modules/git_message.py

## Governing Overview

[overview](overview.md)

## Purpose

Git-compatible publication-message validation and cleanup before publication.

## Code Commentary

`_cleaned_message` derives the effective cleanup/comment settings, preserves verbatim mode, applies whitespace/comment and optional scissors behavior, and refuses invalid modes, an empty effective message or unavailable auto-comment character before publication. Last matching comment setting wins. `_stripspace` works on exact text rather than a decoded subprocess transformation so embedded carriage returns retain their intended semantics. This helper normalizes a proposed message; it creates no commit or ref.

## Invariants And Boundaries

The extracted helper retains its caller-owned operation and refusal boundary; this card is source inspection, not a new product execution or publication grant.

## Evidence

- Git-compatible publication-message validation and cleanup before publication. [1]
