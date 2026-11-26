# mcp/tests/test_moment_composer.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Checks both leaf start notices on paired code and converted-memory fixtures.

## Code Commentary

The cases cover tracked and untracked paths with non-ASCII names, moved rule summaries and readable moment files. A tight-limit case checks that the pointer stays complete.

## Evidence

- Both moment kinds retain non-ASCII paths and write the moved rule’s full text. [1]
