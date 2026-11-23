# mcp/tests/test_git_object_memo.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Checks that an eligible repeated successful Git object lookup reuses its answer within one request for the same repository and object.

## Code Commentary

Batch blob tests verify exact binary and empty bodies, a private spool that closes on success or failure, and refusal of invalid frames. The real-Git allocation case compares traced peak with the bytes returned by the selected batch.

The suite checks same object lookup twice starts one child; distinct lookups each start a child; mutable lookups are never memoized; outside the scope nothing is memoized; failure is never kept later creation reads fresh; supported workdir runs separate. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Evidence



- Within an active request memo, an eligible repeated successful Git object lookup reuses its answer for the same repository and object. [1]



- Replacement-sensitive freshness remains executable in its moved test class; shared fixture helpers keep their own direct owner. [2]
