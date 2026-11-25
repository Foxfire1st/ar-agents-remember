# mcp/tests/test_writer_rule_titles.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Checks invariant title validation and persistence through the knowledge writer.

## Code Commentary

Paired Git fixtures exercise missing or overlong titles on new rules, untitled legacy revisions and preservation of the revision on a title-only write.

## Evidence

- A title-only write changes the stored title while retaining the statement and revision. [1]
