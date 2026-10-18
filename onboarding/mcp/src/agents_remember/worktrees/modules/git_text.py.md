# mcp/src/agents_remember/worktrees/modules/git_text.py

## Governing Overview

[overview](overview.md)

## Purpose

Small lossless text primitives shared by Git publication and message cleanup.

## Code Commentary

`_transport_safe_git_diagnostic` renders surrogateescaped text using backslash replacement into valid UTF-8 output. `_nul_records` splits NUL-framed reads and discards empty separators; it does not normalize ordinary record bytes or acquire publication authority.

## Invariants And Boundaries

The extracted helper retains its caller-owned operation and refusal boundary; this card is source inspection, not a new product execution or publication grant.

## Evidence

- Small lossless text primitives shared by Git publication and message cleanup. [1]

- NUL-framed records discard empty separators without whitespace normalization. [2]
