# mcp/test_support/agents_remember_test_support/testing/tool_answer_fixtures.py

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Provides a real temporary root of controlled width for tests that measure rendered paths in tool answers.

## Code Commentary

`fixed_width_row_case_root` creates its directory under `/tmp`. When the caller specifies a width, the helper pads the prefix using the encoded path length and accounts for the eight-character suffix added by the temporary-directory API. While the fixture is active, the process's XDG configuration, data and cache variables point into its owned directory. On exit, the fixture restores the environment and removes the directory.

## Relationships

The citation, packaging and memory-quality answer tests use the helper for real path measurements. They retain their own evidence fixtures and assertions.

## Evidence

- The helper owns the real temporary root, width calculation, local XDG paths and cleanup. [1]
