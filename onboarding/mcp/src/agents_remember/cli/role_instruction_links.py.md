# mcp/src/agents_remember/cli/role_instruction_links.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Rewrites the relative Markdown link destinations of a launch's instruction text into absolute paths, resolved from the source file the text came from, so a link still reaches its file after the text is delivered or frozen elsewhere.

## Code Commentary

`relative_destinations` finds the destinations of inline links, images and reference definitions outside fenced, indented and inline code. Absolute paths, `{{detail:...}}` placeholders and destinations with a URL scheme are left alone. Code is masked without moving offsets, so a found span indexes the original text.

`bind_markdown_links(text, source, targets)` resolves each relative destination against `source`'s folder (an empty path names `source` itself), substitutes a mapped target where `targets` holds the resolved path, percent-quotes the result and keeps any query and fragment. `cli/role_instruction_details` passes the frozen detail files as `targets`, so a link to another detail reaches its frozen copy, and every other link its file in the shipped composition corpus.

`require_no_unbound_links` raises `CapsuleDeliveryError` when text still holds a relative destination; it guards a baseline that has no source origins to bind it from.

## Evidence

- Relative destinations are found outside code; absolute, placeholder and scheme destinations are skipped. [1]
- Each destination is resolved from its source, mapped to a frozen target when one exists, and keeps its query and fragment. [2]
- Text without source origins may not keep a relative link. [3]
- Code spans and fences are masked without moving offsets. [4]
