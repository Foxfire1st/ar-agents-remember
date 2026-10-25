# mcp/tests/test_git_object_memo.py

## Governing Overview

[governing overview](overview.md)

## Purpose

One request makes the same Git lookup of the same object once (MIK-R81 rule 7).

## Code Commentary

The suite checks same object lookup twice starts one child; distinct lookups each start a child; mutable lookups are never memoized; outside the scope nothing is memoized; failure is never kept later creation reads fresh; supported workdir runs separate. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

`ReplaceFreshnessTests` adds the unchanged replacement-sensitive controls moved from the runner suite. Both modules import `_init` and `_commit` from the shared test-support owner; neither keeps a duplicate fixture.

## Evidence


- One request makes the same Git lookup of the same object once (MIK-R81 rule 7). [1]


- Replacement-sensitive freshness remains executable in its moved test class; shared fixture helpers keep their own direct owner. [2]
