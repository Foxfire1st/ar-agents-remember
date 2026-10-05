# mcp/src/agents_remember/cli/__main__.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`cli/__main__.py` is the umbrella `agents-remember` console entrypoint: a single front door
that dispatches subcommands. It registers **fourteen** of them — `dashboard`, `memory-citations`,
`memory-backfill`, `knowledge-ingest`, `knowledge-bootstrap`, `knowledge-format`,
`knowledge-convert`, `knowledge-validate`, `knowledge-index`, `knowledge-worklist`, `knowledge-routes`,
`knowledge-census`, `review-record-comparison` and `paseo` — and
further CLI adapters slot in as subparsers. Backed by the
`agents-remember = agents_remember.cli.__main__:main` console script.

Owns the one Agents Remember command parser and subcommand dispatch.

## Code Commentary

`build_parser()` builds an `argparse` parser with a required subcommand group and registers
each subparser through its adapter's own `add_arguments`, setting `func=<adapter>.run`:
`dashboard.add_arguments`/`dashboard.run`, `memory_citations.add_arguments`/`memory_citations.run`,
`memory_backfill.add_arguments`/`memory_backfill.run`,
`knowledge_ingest.add_arguments`/`knowledge_ingest.run`,
`knowledge_bootstrap.add_arguments`/`knowledge_bootstrap.run`,
`knowledge_format.add_arguments`/`knowledge_format.run`,
`knowledge_convert.add_arguments`/`knowledge_convert.run`,
`knowledge_validate.add_arguments`/`knowledge_validate.run`,
`knowledge_index.add_arguments`/`knowledge_index.run`,
`knowledge_routes.add_arguments`/`knowledge_routes.run`,
`knowledge_census.add_arguments`/`knowledge_census.run`,
`review_comparison_record.add_arguments`/`review_comparison_record.run` and
`paseo_runtime.add_arguments`/`paseo_runtime.run`. `main(argv=None)` parses and
dispatches to `args.func(args)`, returning its int exit code.

**The two knowledge subcommands are two different admissions, and the help text says which.**
`knowledge-ingest` is described as "the knowledge write plane's production entry point" for a
*leaf's* curator hand-off list; `knowledge-bootstrap` is described as "the taskless bootstrap's
production entry point", which is what a repository with no leaf reaches. They are separate
adapters rather than one adapter with a mode, because the two resolve different admissions
(a leaf enclosure contract, and the settings document's repository entry) and the destination is
derived in both cases rather than passed.

`knowledge-format` is a third knowledge subcommand of a different nature: it reads and writes
only the text knowledge files named on its command line (the MIK-R21 canonical formatter) and
touches no store, no leaf and no admission. Until the text knowledge layout goes live (MIK-R37) the
installed runtime never calls it; it exists so the file shapes can be formatted and checked.

`knowledge-convert` (MIK-R24) converts a memory working tree, with its `knowledge.sqlite`, into the text
knowledge format. Every card's citations are anchored at the code commit its `lastVerifiedCommitHash` names,
read from the object store of `--code`. The command validates the whole converted tree before writing
anything, refuses any conversion-format version other than `1`, and commits nothing: committing a
conversion to a real line is MIK-R37's, or a crossing sync's. No installed route calls it before
MIK-R37; later leaves use it to make the converted scratch copies their evidence runs on.

`knowledge-validate` (MIK-R22) is the formatter's read-only companion: the curator's standalone run of the
mandatory knowledge validator over a memory working tree, against a code checkout and optional
base commits. It writes nothing, and like the formatter it has no effect on unconverted memory: it
reports such a tree as out of scope and exits 0.

`knowledge-index` (MIK-R23) builds or reuses the derived knowledge index of one memory tree — a
working tree's captured state, or a Git tree read through objects — in an untracked cache outside
any Git working tree, and prints its key, state and counts as JSON. It only reads the tree; the
installed runtime does not call it before MIK-R37.

`knowledge-worklist` (MIK-R08) computes the change-to-knowledge worklist of a leaf from its series
contract (persisted beside the contract, exactly as the curator's memory-quality run does) or of four
explicitly named sides, and prints it as JSON. It exits 0 for a complete worklist, 1 for an incomplete one
and 2 when none applies (both memory sides unconverted, which is every production leaf before MIK-R37).

`knowledge-routes` (MIK-R04) is the curator's read-only view of family routes: for each family record of a memory working tree it prints the routes, the route state (`unrealized_family`, `route_unassigned`, uncovered realizations, emptied routes) and the mechanical route suggestion, labelled `mechanical`. It never writes a route, and on today's unconverted memory it answers "no family records".

`knowledge-census` (MIK-R20) has two actions. `inventory` pins a census baseline (a code commit and a memory commit) and writes its `baseline.json` and `inventory.json` into a *converted* memory working tree through the census writer, which refuses an unconverted tree; `report` only reads, printing each census's Doc12 measures with their counts, its dispositions and its routes' governing statuses. Claims, assessments and statuses are written through the writer's Python API, not this CLI. On today's unconverted memory `report` answers "no census under knowledge/census/".

The memory-maintenance and migration adapters are reached only from here, so the umbrella is
the one place a new CLI surface becomes reachable. Their flags, exit statuses and refusals
belong to the adapters; this module contributes only the subparser registration.

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
- This module dispatches; it implements no operation of its own. A new subcommand is a
  registration line here plus an adapter module that owns its arguments and its exit code.

## Evidence

### Repo-Internal References

- The `dashboard` subcommand adapter this dispatches to. [1]
- The peer CLI adapter pattern. [2]
- The memory-citations adapter, registered the same declarative way. [3]
- The memory-backfill adapter: its `--contract` is the write guard that keeps a history rewrite off the official memory repository. [4]
- The separate MCP server console entry that stays standalone. [5]
- The `knowledge-ingest` subparser this umbrella registers for a leaf's curator hand-off list. [6]
- **The `knowledge-bootstrap` subparser this leaf adds: the taskless entry, registered the same declarative way.** [7]
- **The `knowledge-format` subparser `260928-MIK-L21` adds: the text knowledge files' canonical formatter, the umbrella's sixth registered subcommand.** [8]
- **The `knowledge-convert` subparser `260928-MIK-L24` adds: the conversion of a memory tree and its database into the text format.** [9]
- **The `knowledge-validate` subparser `260928-MIK-L22` adds: the curator's standalone run of the knowledge validator.** [10]
- **The `knowledge-index` subparser `260928-MIK-L23` adds: the derived knowledge index of one memory tree, built or reused and reported.** [11]
- **The `knowledge-worklist` subparser `260928-MIK-L08` adds: the change-to-knowledge worklist of a leaf or of four named sides.** [12]
- **The `knowledge-routes` subparser `260928-MIK-L04` adds: the read-only family route report with the mechanical suggestion.** [13]
- **The `knowledge-census` subparser `260928-MIK-L20` adds: the migration census's inventory and report.** [14]
- **The `review-record-comparison` subparser `260921-ICR-L34` adds: the review comparison's production caller.** [15]

### Runtime Source References

- Frozen implementation of build_parser supporting the stated file behavior. [16]
- Frozen implementation of main supporting the stated file behavior. [17]
