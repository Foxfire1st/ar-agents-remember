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

A separate pure `summarize_rows` control supplies more actionable rows than the selected
sample budget and checks counts remain complete while the sample is capped. These are
separate claims: parsed argument forwarding, delivered CLI composition, and pure truncation.
The helper creates only fixture repositories/settings; its Git work is not an acceptance
or landing operation on the user's repository.

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
