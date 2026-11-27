# mcp/src/agents_remember/application/file_briefs/titles.py

## Governing Overview

[Area overview](../overview.md)

## Purpose

Chooses the display title used by a file brief and its short answer.

## Code Commentary

A stored title displays after whitespace normalization. For an untitled rule, `rule_title` delegates to `clause_title` to derive a readable first-clause fallback within `FALLBACK_MAX_CHARS` (80 characters) without mutating the record: whitespace-normalized statements at or under 80 characters are kept whole; longer ones cut at the first sentence separator (`. `, `? `, `! `) in characters 20–80 without an ellipsis, else at the last clause separator (`; `, `: `, ` — `, ` -- `, `, `) in 20–80 with ` …`, else at the last space up to 80 characters (stripping trailing `,;:`) or hard-cut at 80 characters with ` …`. The display never writes a title to the rule record.

## Evidence

- The title selector returns a normalized recorded title or derives a readable <=80-character first-clause fallback via `clause_title`. [1]
