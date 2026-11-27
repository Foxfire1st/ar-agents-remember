# mcp/src/agents_remember/cli/__main__.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`cli/__main__.py` is the umbrella `agents-remember` console entrypoint: a single front door
that dispatches subcommands. Its subcommands include `dashboard`, `memory-citations`,
`memory-backfill`, `memory-briefs`, `handoff-check`, `knowledge-ingest`, `knowledge-bootstrap`, `knowledge-format`,
`knowledge-convert`, `knowledge-convert-states`, `knowledge-validate`, `knowledge-index`, `knowledge-worklist`, `knowledge-routes`,
`knowledge-census`, `knowledge-copies`, `explainer-browser`, `tool-log-stats` (MIK-R108 rule 8), `paseo`, `provider-limits`, `upgrade-user-settings` and `removed-stores` — and
further CLI adapters slot in as subparsers. Backed by the
`agents-remember = agents_remember.cli.__main__:main` console script.

Owns the one Agents Remember command parser and subcommand dispatch.

## Code Commentary

`build_parser()` builds an `argparse` parser with a required subcommand group and registers
each subparser through its adapter's own `add_arguments`. Finite commands dispatch through
`_run_finite_command`; `dashboard` retains its adapter directly:
`dashboard.add_arguments`/`dashboard.run`, `memory_citations.add_arguments`/`memory_citations.run`,
`memory_backfill.add_arguments`/`memory_backfill.run`, `memory_briefs.add_arguments`/`memory_briefs.run` (registered under `_register_memory_commands` to refresh derived `briefs/` in a converted external memory checkout),
`knowledge_ingest.add_arguments`/`knowledge_ingest.run`,
`knowledge_bootstrap.add_arguments`/`knowledge_bootstrap.run`,
`knowledge_format.add_arguments`/`knowledge_format.run`,
`knowledge_convert.add_arguments`/`knowledge_convert.run`,
`knowledge_validate.add_arguments`/`knowledge_validate.run`,
`knowledge_index.add_arguments`/`knowledge_index.run`,
`knowledge_worklist.add_arguments`/`knowledge_worklist.run`,
`knowledge_routes.add_arguments`/`knowledge_routes.run`,
`knowledge_census.add_arguments`/`knowledge_census.run`,
`knowledge_copies.add_arguments`/`knowledge_copies.run`,
`explainer_browser.add_arguments`/`explainer_browser.run`,
`paseo_runtime.add_arguments`/`paseo_runtime.run`, `provider_limit_hold.add_arguments`/`provider_limit_hold.run` and
`tool_log_stats.add_arguments`/`tool_log_stats.run`. For public commands, `main(argv=None)`
parses and dispatches to `args.func(args)`, returning its int exit code. Before that public parser,
the internal `leaf_enclosure_start.COMMAND` child-process route delegates to its own entry point;
it is not an additional advertised public subcommand. Each finite command and the internal child
route owns one `definition_scope`; dashboard dispatch stays outside that finite scope.

**The two knowledge authoring subcommands are two different admissions, and the help text says which.**
`knowledge-ingest` is described as "the knowledge write plane's production entry point" for a
*leaf's* curator hand-off list; `knowledge-bootstrap` is described as "the taskless bootstrap's
production entry point", which is what a repository with no leaf reaches. They are separate
adapters rather than one adapter with a mode, because the two resolve different admissions
(a leaf enclosure contract, and the settings document's repository entry) and the destination is
derived in both cases rather than passed.

`knowledge-format` is a third knowledge subcommand of a different nature: it reads and writes
only the text knowledge files named on its command line (the MIK-R21 canonical formatter) and
touches no store, no leaf and no admission. It formats and checks the named file shapes.

`knowledge-convert` (MIK-R24, MIK-R46) converts a memory working tree with its
`knowledge.sqlite` into text knowledge. Card citations remain anchored at the code
commit named by `lastVerifiedCommitHash`, read through `--code`; the whole result
validates before writes and only conversion-format version `1` is supported. The
command commits nothing. Its help names the first step of the first-conversion procedure (MIK-R46 rule 6): without an attributed baseline convert the root
in place, then adopt; with an official line convert one new leaf’s memory worktree
as its first memory change, then close out and land. Other open lines cross through
`worktree_sync` with `merge-memory`. The command, its read-only legacy-database
reader and conversion-format version 1 are permanent product parts; retirement
requires a separate developer decision, because other clones can retain unconverted lines.

`knowledge-convert-states` serves a separate conversion of already-converted memory. The command defaults to planning and writes the state-format conversion only on explicit apply.

`knowledge-validate` (MIK-R22) is the formatter's read-only companion: the curator's standalone run of the
mandatory knowledge validator over a memory working tree, against a code checkout and optional
base commits. It writes nothing, and like the formatter it has no effect on unconverted memory: it
reports such a tree as out of scope and exits 0.

`knowledge-index` (MIK-R23) builds or reuses the derived knowledge index of one memory tree — a
working tree's captured state, or a Git tree read through objects — in an untracked cache outside
any Git working tree, and prints its key, state and counts as JSON. It only reads the selected memory tree.

`knowledge-worklist` (MIK-R08) computes the change-to-knowledge worklist of a leaf from its series
contract (persisted beside the contract, exactly as the curator's memory-quality run does) or of four
explicitly named sides, and prints it as JSON. It exits 0 for a complete worklist, 1 for an incomplete one
and 2 when none applies (both memory sides unconverted).

`knowledge-routes` (MIK-R04) is the curator's read-only view of family routes: for each family record of a memory working tree it prints the routes, the route state (`unrealized_family`, `route_unassigned`, uncovered realizations, emptied routes) and the mechanical route suggestion, labelled `mechanical`. It never writes a route, and on unconverted memory it answers "no family records".

`knowledge-census` (MIK-R20) has two actions. `inventory` pins a census baseline (a code commit and a memory commit) and writes its `baseline.json` and `inventory.json` into a *converted* memory working tree through the census writer, which refuses an unconverted tree; `report` only reads, printing each census's Doc12 measures with their counts, its dispositions and its routes' governing statuses. Claims, assessments and statuses are written through the writer's Python API, not this CLI. On unconverted memory `report` answers "no census under knowledge/census/".

The memory-maintenance and migration adapters are reached only from here, so the umbrella is
the one place a new CLI surface becomes reachable. Their flags, exit statuses and refusals
belong to the adapters; this module owns subparser registration and the finite-command definition scope.

`explainer-browser` is registered in the knowledge-command section although it is a runtime
surface: it reports, or fetches, the Playwright module and Chromium the explainer publishes with
(`cli.explainer_browser`). It starts no product process of its own and changes no installation state
beyond that product-owned browser folder.

The MCP server keeps its own separate `agents-remember-mcp` console script — harness MCP
configs launch the server by that exact name, so it is never folded into this umbrella.

### Role Runtime and Scope

The paseo command group joins existing knowledge-ingest, taskless bootstrap and knowledge format/convert/validate/worklist routes. Preserve one parser owner: PNT runtime management and MIK converted writer/gate commands coexist rather than replacing or duplicating one another.

## Invariants And Boundaries

- `agents-remember-mcp` is **not** a subcommand here; renaming or absorbing it would break
  harness MCP registrations.
- Subcommand wiring stays declarative (`add_arguments` + `set_defaults(func=...)`) so each
  adapter owns its own flags.
- The subcommand group is required, so invoking `agents-remember` with no subcommand is a usage
  error rather than a default action.
- This module dispatches and owns the finite-command definition scope. A new subcommand is a
  registration line here plus an adapter module that owns its arguments and its exit code.

## Current source contract

The knowledge-command registry also exposes handoff-check, delegating its arguments and execution to cli.handoff_check. It reads producer lists against a named code tree and optional memory directory; it is separate from knowledge-ingest and supplies no write or acceptance authority.

- Registers read-only handoff-check command. [20]

## Evidence

- The command parser registers text conversion and standing/state conversion separately. [24]
- The derived-state adapter selects a plan by default and exposes an explicit apply operation. [25]

### Repo-Internal References

- The `dashboard` subcommand adapter this dispatches to. [1]

- The peer CLI adapter pattern. [2]

- The memory-citations adapter, registered the same declarative way. [3]

- The memory-backfill adapter: its `--contract` is the write guard that keeps a history rewrite off the official memory repository. [4]
- The separate MCP server console entry that stays standalone. [5]
- The `knowledge-ingest` subparser this umbrella registers for a leaf's curator hand-off list. [6]

- The `knowledge-copies` subparser adds: retired knowledge-database leftover copies listed with their deciding rule (`--apply` deletes MIK-R26 rule 6 names), registered the same declarative way. [15]

- The `upgrade-user-settings` subparser performs the explicit whole-file move from the old coordination settings file to the user configuration directory, with `--coordination-root` and `--dry-run`.

The original source already registered upgrade-user-settings and its adapter before this change added handoff-check; the earlier caption’s “this leaf” does not identify L62. Earlier caption retained as prose; its original citation used mcp/src/agents_remember/cli/__main__.py at blob `6e7bd5a18da5ea781594e67999b9b01f305937d4`. Reference 18 now carries the current clause and current source targets; it does not retain those earlier targets.

Retained authoring-row wording:

Finding: The runtime-command registry registers upgrade-user-settings with its existing adapter; handoff-check is registered separately in the knowledge-command registry.

Anchor:

Source: mcp/src/agents_remember/cli/__main__.py

### Runtime Source References

Retained authoring-row wording:

Finding: Frozen implementation of build_parser supporting the stated file behavior.

Anchor:

Source: mcp/src/agents_remember/cli/__main__.py

- The umbrella registers the explainer's browser command beside the knowledge commands. [21]

- **The `knowledge-bootstrap` subparser: the taskless entry, registered the same declarative way.** [7]
- **The `knowledge-format` subparser: the text knowledge files’ canonical formatter.** [8]
- **The `knowledge-convert` subparser: conversion of a memory tree and its database into the text format.** [9]
- **The `knowledge-validate` subparser: the curator’s standalone run of the knowledge validator.** [10]
- **The `knowledge-index` subparser: the derived knowledge index of one memory tree, built or reused and reported.** [11]
- **The `knowledge-worklist` subparser: the change-to-knowledge worklist of a leaf or of four named sides.** [12]
- **The `knowledge-routes` subparser: the read-only family route report with the mechanical suggestion.** [13]
- **The `knowledge-census` subparser: the migration census’s inventory and report.** [14]
- Frozen implementation of main supporting the stated file behavior. [17]

- Frozen implementation of build_parser supporting the stated file behavior. [16]

- The runtime-command registry registers `provider-limits` and `upgrade-user-settings` with their adapters; `handoff-check` is registered separately in the knowledge-command registry. [18]


- Registers `memory-briefs` under `_register_memory_commands` to refresh derived `briefs/` in a converted external memory checkout. [26]
