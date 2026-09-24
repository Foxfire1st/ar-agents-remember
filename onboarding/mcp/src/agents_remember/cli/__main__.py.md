# mcp/src/agents_remember/cli/__main__.py

| Field                  | Value                                         |
| ---------------------- | --------------------------------------------- |
| repository             | agents-remember                               |
| path                   | `mcp/src/agents_remember/cli/__main__.py`     |
| doc_type               | `file-level-onboarding`                       |
| lastUpdated            | 2026-09-14T17:20+02:00                        |
| lastVerifiedCommitHash | `86639933d61528387ce106dbd4d7a334bd468671`    |
| lastVerifiedCommitDate | 2026-09-24T18:51:31+02:00|
| governingOverview      | `../../../overview.md`                         |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`cli/__main__.py` is the umbrella `agents-remember` console entrypoint: a single front door
that dispatches subcommands. It registers **five** of them — `dashboard`, `memory-citations`,
`memory-backfill`, `knowledge-ingest` and `knowledge-bootstrap` — and further CLI adapters slot
in as subparsers. Backed by the `agents-remember = agents_remember.cli.__main__:main` console
script.

## Code Commentary

`build_parser()` builds an `argparse` parser with a required subcommand group and registers
each subparser through its adapter's own `add_arguments`, setting `func=<adapter>.run`:
`dashboard.add_arguments`/`dashboard.run`, `memory_citations.add_arguments`/`memory_citations.run`,
`memory_backfill.add_arguments`/`memory_backfill.run`,
`knowledge_ingest.add_arguments`/`knowledge_ingest.run` and
`knowledge_bootstrap.add_arguments`/`knowledge_bootstrap.run`. `main(argv=None)` parses and
dispatches to `args.func(args)`, returning its int exit code.

**The two knowledge subcommands are two different admissions, and the help text says which.**
`knowledge-ingest` is described as "the knowledge write plane's production entry point" for a
*leaf's* curator hand-off list; `knowledge-bootstrap` is described as "the taskless bootstrap's
production entry point", which is what a repository with no leaf reaches. They are separate
adapters rather than one adapter with a mode, because the two resolve different admissions
(a leaf enclosure contract, and the settings document's repository entry) and the destination is
derived in both cases rather than passed.

The memory-maintenance and migration adapters are reached only from here, so the umbrella is
the one place a new CLI surface becomes reachable. Their flags, exit statuses and refusals
belong to the adapters; this module contributes only the subparser registration.

The MCP server keeps its own separate `agents-remember-mcp` console script — harness MCP
configs launch the server by that exact name, so it is never folded into this umbrella.

## Invariants And Boundaries

- `agents-remember-mcp` is **not** a subcommand here; renaming or absorbing it would break
  harness MCP registrations.
- Subcommand wiring stays declarative (`add_arguments` + `set_defaults(func=...)`) so each
  adapter owns its own flags.
- The subcommand group is required, so invoking `agents-remember` with no subcommand is a usage
  error rather than a default action.
- This module dispatches; it implements no operation of its own. A new subcommand is a
  registration line here plus an adapter module that owns its arguments and its exit code.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `dashboard` subcommand adapter this dispatches to. | `run` | mcp/src/agents_remember/cli/dashboard.py:212-247 |
| The peer CLI adapter pattern. | `main` | mcp/src/agents_remember/cli/context_packet.py:20-67 |
| The memory-citations adapter, registered the same declarative way. | `add_arguments`; `run` | mcp/src/agents_remember/cli/memory_citations.py:48-101; mcp/src/agents_remember/cli/memory_citations.py:104-165 |
| The memory-backfill adapter: its `--contract` is the write guard that keeps a history rewrite off the official memory repository. | `add_arguments`; `run` | mcp/src/agents_remember/cli/memory_backfill.py:41-73; mcp/src/agents_remember/cli/memory_backfill.py:76-97 |
| The separate MCP server console entry that stays standalone. | `main` | mcp/src/agents_remember/mcp/__main__.py:5-8 |
| The `knowledge-ingest` subparser this umbrella registers for a leaf's curator hand-off list. | `knowledge_ingest`; "knowledge-ingest" | mcp/src/agents_remember/cli/__main__.py:41-48 |
| **The `knowledge-bootstrap` subparser this leaf adds: the taskless entry, registered the same declarative way.** | `knowledge_bootstrap`; "knowledge-bootstrap" | mcp/src/agents_remember/cli/__main__.py:50-58 |

## Update History
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **body update — the two-subcommand record gains the write plane's own naming.** The card already recorded both subcommands and their different admissions; it now also records that `260921-ICR-L32` corrected the mounted tool description and two module docstrings to name **both** of these entry points where they named one, so this CLI's five-subcommand inventory and the write plane's own description agree. No claim, anchor or citation range changed by the wording added here. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.

- 2026-09-24T09:20+02:00 — 260921-ICR-L29 curator (uncommitted change set on `ar/260921-icr-l29-ar`,
  base `0d7910f9d646161c414ed6543453536a3c749d49`): **the umbrella gains its fifth subcommand, and a
  stale sentence in this card is corrected rather than extended.** The body above said the parser
  registered **three** subcommands; that sentence had already been false since `knowledge-ingest` was
  registered, and this leaf adds `knowledge-bootstrap` beside it, so the count and the list are now
  the five the parser really builds. The registration is the same declarative pair
  (`add_arguments` + `set_defaults(func=...)`, `:50-58`) and the adapter owns its own flags and exit
  code, so this module's contribution is still one registration line. Two reference rows were added:
  the `knowledge-ingest` subparser (`:41-48`) and this leaf's `knowledge-bootstrap` subparser
  (`:50-58`). **No verification stamp was advanced** — the candidate is uncommitted, so no commit
  holds the content a stamp would claim to have verified, and the governed closeout owns the real
  code and memory commits.
- 2026-09-18T18:20+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **re-read this card's reopened claim against the construct its range now covers, and RETAINED its wording** — `add_arguments`; `run`, cited at mcp/src/agents_remember/cli/memory_citations.py:48-101 and `:104-165`. The cited ranges hold `def add_arguments(parser: argparse.ArgumentParser) -> None:` at `:53` and `def run(args: argparse.Namespace) -> int:` at `:120`, which is exactly what the claim says the memory-citations adapter registers the same declarative way through; the claim is true as written. A **generated anchor-range projection** had rewritten the range mechanically, which is why the citation was not shown to be current until an agent read it — this is that reading. No range was substituted or deleted, and the verification stamp is **not** advanced.
- 2026-09-18T16:13:35+00:00: Generated citation repair: `run` repointed to mcp/src/agents_remember/cli/dashboard.py:212-247. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-14T17:20+02:00 — 260913-LCA-L3 (uncommitted change set on `ar/260913-lca-l3-ar`, base
  `7317108b`): the umbrella gained the `memory-backfill` subparser, registered through
  `memory_backfill.add_arguments` + `set_defaults(func=memory_backfill.run)`, so the body now names
  all three subcommands the parser builds instead of `dashboard` alone and records that the
  maintenance and migration adapters are reachable only from here. Repaired the three stale
  reference anchors this pass re-derived — `dashboard.run` 161-196 → 174-209, `context_packet.main`
  17-60 → 20-67, `mcp/__main__.py` 8-8 → 5-8 — and corrected `governingOverview` from the
  repository-root `../../../../overview.md` to this route's `../../../overview.md`, which is what the
  sibling `cli/memory_citations.py` card already points at. Verification metadata remains
  closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 6 citation findings for the dashboard, context-packet, and MCP console entry points.

- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4a: the umbrella `agents-remember`
  dispatcher with the `dashboard` subcommand. Verification metadata pinned until closeout
  stamps the 4a code commit.

