# mcp/tests/test_citation_migrate_registration.py

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

`CitationMigrateRegistrationTests` covers the two surfaces a caller depends on:

- **All three surfaces agree** — `test_the_tool_is_registered_advertised_and_has_a_response_model`
  builds a real `FastMCP` server through `register_memory_tools` and requires `citation_migrate`
  to appear in the server's `list_tools()`, in `PUBLIC_TOOLS`, **and** in
  `PUBLIC_TOOL_RESPONSE_MODELS`. Advertising the name on one surface and not another is exactly the
  recorded defect, so a partial registration fails.
- **The payload wrapper reaches the application tool** — `test_the_payload_builder_reaches_the_application_tool`
  patches `citation_migrate_tool` and calls `citation_migrate_payload`, requiring one call with
  `dry_run=True` and an `operation` of `citation_migrate`. The real tool validates its scope before it
  resolves anything, so the double answers the shape the application entry point actually returns.
- **The configured-authority refusal is named, and only it is translated** —
  `test_citation_tools_name_a_configured_contract_authority_refusal` patches each tool's
  application entry point with a `ConfiguredContractAuthorityError` and requires `ok: false`, the status
  `configured-contract-authority-invalid`, the failing side and name in `detail`, and the next action
  `developer-decision` from both payload builders;
  `test_citation_tools_propagate_other_authority_errors` requires an unrelated `AuthorityError`
  to leave both builders as the same exception object, so widening either catch fails.

`CitationMigrateReachesTheMigrationTests` covers the reach itself:
`test_the_tool_invokes_the_migration_over_the_leaf_memory_onboarding_root` makes **one real call
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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; both the tool and its
advertisement surfaces are repository-owned.

No configured `Domain Documentation` source applies; the subject is the repository's own MCP surface.

### Repo-Internal References

- The application entry point whose reachability this module pins (unchanged by MIK-R24, whose converted-format routing covers `citation_check` and `citation_fix` only). [1]
- The migration the registered tool must actually arrive at. [2]
- The payload wrapper between the registered handler and the application tool. [3]

- The registration surface that wires the handler onto the server. [4]
- The advertised-name roster the tool must appear in. [5]
- The response-model registry that keeps the advertised name typed. [6]
- The typed response envelope the registry maps the name to. [7]

- The two new cases pin the configured-authority refusal and the unchanged propagation of every other authority error. [8]

### Cross-Repo References

No external repository boundary is exercised; the gate that made the CLI route unusable from a leaf is
this repository's own checkout confinement.

No meaningful cross-repo references found.
