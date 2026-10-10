# mcp/tests/test_fixture_recorded_paths.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Recorded payloads keep the paths they were recorded with, by design.

## Code Commentary

MIK-R82 rule 7: recorded payloads in test fixtures keep the `/tmp/...` paths they were recorded with; they name no developer and no test opens them. The guard test states this rule in its text.

## Evidence

- Recorded-path fixtures with developer-local paths are refused; recorded `/tmp` paths pass. [1]
