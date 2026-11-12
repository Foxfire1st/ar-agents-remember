# mcp/tests/test_canvas_kit.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The kit's own contracts: the manifest ships the named minimum and nothing more, every byte is accounted for by size and digest, and each entry carries the licence it was read from.

## Code Commentary

- A file present in the package but absent from the manifest fails the suite, so the kit cannot grow silently.
- Every dependency inside a bundle has its licence beside it.

## Evidence

- The case `test_the_manifest_ships_the_named_minimum_kit_and_nothing_more` protects this behaviour. [1]
- The case `test_every_shipped_byte_is_accounted_for_by_size_and_digest` protects this behaviour. [2]
