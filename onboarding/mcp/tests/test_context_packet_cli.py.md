# mcp/tests/test_context_packet_cli.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Regression cases for the retained context-packet CLI and its drift-detail-limit contract,
not for removed provider options or another MCP tool.

## Code Commentary

A temporary Git repository and trusted fixture settings isolate `main(argv)`. The ordinary
call must exit successfully and deliver a versioned packet. The explicit drift case wraps
the real summary helper, checks that `--drift-detail-limit 3` reaches its behavior-layer
keyword argument, and verifies the delivered actionable sample respects that limit.

The remaining assertions distinguish CLI argument forwarding from delivered composition; there is no separate pure complete-count/truncation control in this module. Helpers create fixture repositories and settings only, not an acceptance or landing operation on the user repository.

## Boundaries

Reading these assertions records their intended evidence facets, not that they were
executed now. No provider indexing, real host launch, memory certification or full-suite
success follows from the sample-limit checks.

## Evidence


- The complete file owns the behavior and limits described above; documentation/tests are not fresh execution evidence. [1]


## External and cross-repository evidence

No Domain Documentation entries are configured in the resolved source registry.
This card claims only the package-local source contract; no external runtime or
cross-repository acceptance evidence is inferred.
