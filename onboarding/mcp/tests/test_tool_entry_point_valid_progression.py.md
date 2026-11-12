# mcp/tests/test_tool_entry_point_valid_progression.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Tests for valid public progression.

## Code Commentary

The tests drive the public canonical progression -- preview, approved closeout, integration, real landing record, cleanup -- through the tool surface. A driven tool's delivered wire answer is judged by the world's single reader — the `payload` arm already implies the valid whole result read back from the answer's log — while the direct whole-result validations of the checkpoint support stay as they are.

## Evidence

- Each driven tool's delivered answer classifies `payload` through the world's single reader. [2]
