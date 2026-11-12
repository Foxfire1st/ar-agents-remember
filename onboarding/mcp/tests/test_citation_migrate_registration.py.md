# mcp/tests/test_citation_migrate_registration.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Pin the retained citation-fix wiring and narrow authority refusal while recording migration
MCP retirement separately from application-level migration reachability.

## Code Commentary

The registration case builds a test server and requires citation_migrate absent from the
registered names, public roster and response models. The two historically plural authority
cases now iterate citation_fix only. Their assertions pin configured-contract refusal fields,
no operation envelope key, and unchanged propagation of the same unrelated AuthorityError
object. They do not test a current migration MCP payload adapter.

The application migration reachability case and legacy migration routine were removed by this task. The retained module contains the negative registration/API/legacy-path assertions and two citation_fix-only authority/error-propagation cases. It does not exercise a current migration payload adapter, leaf migration guard or production migration. The earlier reachability defect remains historical context, not a current test assertion or execution receipt.

## Current evidence


- Negative registration/roster/model assertions for citation_migrate. [9]



- Retained citation_fix-only configured-contract-authority refusal assertions. [10]


- Retained citation_fix-only same-exception propagation assertion. [11]


## Historical superseded account (non-operative)

Prior two-tool registration/refusal descriptions below are preserved history, not the
current advertised roster or current test assertion scope.



Pins that **`citation_migrate` is reachable as an MCP tool, not only as a CLI subcommand.**

The recorded defect (S0 of `260915-CAPS-L21`): `citation_migrate_tool` existed in
`application/memory_tools.py` with exactly one caller — the `memory-citations --migrate` CLI
subcommand — and no MCP registration. A running server therefore could not reach it at all, and the
CLI could not reach a live leaf either: from the primary checkout it is refused outright, and from a
linked worktree it is confined to a disposable coordination root that cannot contain a leaf contract.
The result was **481 superseded citation tables that no governed route could convert for six weeks** —
the target citation format entered with `5920ea2b` on 2026-08-05, and every master built since
inherited tables nothing could read.

This is the class of defect where a capability exists, is tested in isolation, and is still
unreachable: nothing fails, because nothing calls it. So the cases here assert the *advertisement* and
the *reach* separately, and the whole point is that a name present on one surface and missing from
another is the defect itself.

## Retained Test Boundaries

The negative registration case constructs a test server and asserts citation_migrate absent from its tool list, public roster and response models. It also asserts the application migration/source-index adapters and named legacy citation/update-history paths absent, the surviving three-check registry, and removed schema/CLI operands. The other two cases protect citation_fix only: configured-contract authority is translated with its exact refusal identity and recovery action, while an unrelated AuthorityError propagates as the same exception object. These are source-described assertions, not tests executed by this draft or live-server acceptance. Server restart remains necessary to adopt changed registration; no current migration registration is proposed.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; both the tool and its
advertisement surfaces are repository-owned.

No configured `Domain Documentation` source applies; the subject is the repository's own MCP surface.

### Repo-Internal References




- The registration source is tested to leave citation_migrate absent. [4]



- The public roster is tested to leave citation_migrate absent. [5]



- The response-model registry is tested to leave citation_migrate absent. [6]



- The source assertion checks the surviving citation_fix schema has neither expected_snapshot nor exclude. [7]



- The two citation_fix-only cases pin the exact configured-contract refusal and unchanged propagation of unrelated authority errors. [8]

### Cross-Repo References

No external repository boundary is exercised; the gate that made the CLI route unusable from a leaf is
this repository's own checkout confinement.

No meaningful cross-repo references found.
