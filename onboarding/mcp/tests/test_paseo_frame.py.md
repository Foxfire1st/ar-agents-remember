# mcp/tests/test_paseo_frame.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

The frame chooses only the asking origin's configured embed URL, returns native server/workspace identity and keeps frame availability distinct from failed workspace opening. Missing configuration, unlisted origin and unreachable identity calls retain named states. It tests request-origin plumbing and bridge replies rather than live browser embedding.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]
