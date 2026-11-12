# mcp/tests/test_fixture_recorded_paths.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Recorded payloads keep the paths they were recorded with, by design.

## Code Commentary

MIK-R82 rule 7: recorded payloads in test fixtures keep the `/tmp/...` paths they were recorded with; they name no developer and no test opens them. The guard test states this rule in its text.

`fixture_text` decompresses .gz bytes before both recorded-path scans. Planted developer-local and /tmp payloads exercise the unchanged path rule; malformed gzip raises rather than becoming an empty recording. The tests do not open the recorded payload paths. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence
- Recorded-path fixtures with developer-local paths are refused; recorded `/tmp` paths pass. [1]

- `fixture_text` decompresses .gz bytes before both recorded-path scans. Planted developer-local and /tmp payloads exercise the unchanged path rule; malformed gzip raises rather than becoming an empty recording. The tests do not open the recorded payload paths. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [2]
