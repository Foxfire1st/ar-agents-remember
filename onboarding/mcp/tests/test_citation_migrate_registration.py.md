# mcp/tests/test_citation_migrate_registration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_citation_migrate_registration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T23:30+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

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

## Code Commentary

### Logic

`CitationMigrateRegistrationTests` (60) covers the two surfaces a caller depends on:

- **All three surfaces agree** — `test_the_tool_is_registered_advertised_and_has_a_response_model`
  (63) builds a real `FastMCP` server through `register_memory_tools` and requires `citation_migrate`
  to appear in the server's `list_tools()`, in `PUBLIC_TOOLS`, **and** in
  `PUBLIC_TOOL_RESPONSE_MODELS`. Advertising the name on one surface and not another is exactly the
  recorded defect, so a partial registration fails.
- **The payload wrapper reaches the application tool** — `test_the_payload_builder_reaches_the_application_tool`
  (77) patches `citation_migrate_tool` and calls `citation_migrate_payload`, requiring one call with
  `dry_run=True` and an `operation` of `citation_migrate`. The real tool validates its scope before it
  resolves anything, so the double answers the shape the application entry point actually returns.

`CitationMigrateReachesTheMigrationTests` (103) covers the reach itself:
`test_the_tool_invokes_the_migration_over_the_leaf_memory_onboarding_root` (106) makes **one real call
through the registered tool** against a scratch coordination root and requires it to arrive at
`migration.migrate_onboarding_root` with the leaf's own memory onboarding root and both tree roots,
after the write guard has run. Red-before-green was observed, not assumed: before the registration the
tool was absent from the server's tool list.

### Conventions

- The registration mirrors `citation_fix` exactly — same `_leaf_memory_writer_scope` guard with
  `operation="citation_migrate"`, same mandatory `contract_path`, same
  `document` / `expected_snapshot` / `exclude` request shape — so the two repair routes cannot drift
  into two different authorization models for one operation class.
- The server is constructed through the real `register_memory_tools` entry point rather than by
  inspecting a registry dict, because the defect being pinned was a *wiring* omission.
- Scratch coordination roots are throwaway; the contract path is a fixture leaf contract, so the
  guard's real resolution path is exercised.

### Invariants And Boundaries

- **A registered tool is not a reachable tool until the server restarts.** The registration takes
  effect on the next server start; a daemon booted before the change still has no such tool. The
  registration is the permanent repair; the leaf's own migration run was a disclosed by-hand
  invocation because the running server (booted 2026-09-16 from `d6d39c1b`) could not expose a tool
  registered after it booted. This card records that restart requirement rather than implying the
  live process changed.
- **The three surfaces are one contract.** Adding the handler without the roster row, or the roster
  row without the response model, is an incomplete repair and this module fails on it.
- **Migration is a write operation and stays guarded.** Reachability does not loosen the leaf-scoped
  write guard; the test asserts the guard ran, not that it was bypassed.

## Docs References

No Domain Documentation source is configured for this repository; both the tool and its
advertisement surfaces are repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source applies; the subject is the repository's own MCP surface. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The application entry point whose reachability this module pins. | `citation_migrate_tool` | mcp/src/agents_remember/application/memory_tools.py:245-276 |
| The migration the registered tool must actually arrive at. | `migrate_onboarding_root` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:675-726 |
| The payload wrapper between the registered handler and the application tool. | `citation_migrate_payload` | mcp/src/agents_remember/mcp/tools/memory.py:113-130 |
| The registration surface that wires the handler onto the server. | `register_memory_tools` | mcp/src/agents_remember/mcp/registration/memory.py:36-40 |
| The advertised-name roster the tool must appear in. | `PUBLIC_TOOLS` | mcp/src/agents_remember/models/tools/public_roster.py:22-91 |
| The response-model registry that keeps the advertised name typed. | `PUBLIC_TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:243-247 |
| The typed response envelope the registry maps the name to. | `CitationMigrateResponse` | mcp/src/agents_remember/models/memory.py:137-153 |

## Cross-Repo References

No external repository boundary is exercised; the gate that made the CLI route unusable from a leaf is
this repository's own checkout confinement.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T23:30+02:00 — 260915-CAPS-L21 curator: created this card for a source file **new in this
  leaf** (S0's registration, which is the permanent repair for the recorded `D44` defect; the leaf's own
  migration run used a disclosed by-hand runner because the running daemon cannot expose a tool
  registered after it booted). Anchors and ranges were read from the current worktree source; the file is
  untracked at this tip, so verification metadata is pinned to this leaf's code base commit `997305a9`
  and the governed closeout stamps the real code commit. No hash or fingerprint was invented here.
