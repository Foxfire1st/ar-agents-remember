# mcp/tests/test_paseo_frame.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

The frame chooses only the asking origin's configured embed URL, returns native server/workspace identity and keeps frame availability distinct from failed workspace opening. Missing configuration, unlisted origin and unreachable identity calls retain named states. It tests request-origin plumbing and bridge replies rather than live browser embedding.

The origin/embed descriptor case now also pins `provisionCommand` to the active fixture settings file. The wired host-facts case includes that field in its expected answer but copies its value from the answer, so command construction is independently asserted by the origin case, not by that copy. These remain descriptor/protocol tests, not browser Retry, plugin upgrade or live provision execution.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]

## Current contract evidence

- The origin/embed descriptor case now also pins `provisionCommand` to the active fixture settings file. The wired host-facts case includes that field in its expected answer but copies its value from the answer, so command construction is independently asserted by the origin case, not by that copy. These remain descriptor/protocol tests, not browser Retry, plugin upgrade or live provision execution. [2]
