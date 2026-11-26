# mcp/src/agents_remember/application/file_briefs/titles.py

## Governing Overview

[Area overview](../overview.md)

## Purpose

Chooses the display title used by a file brief and its short answer.

## Code Commentary

A stored title displays after whitespace normalization. For an untitled rule the reader uses the first six words of its statement and adds an ellipsis when there are more words. The display never writes a title to the rule record.

## Evidence

- The title selector distinguishes an existing title from a derived display title. [1]
