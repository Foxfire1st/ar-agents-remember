# mcp/src/agents_remember/cli/__main__.py

| Field                  | Value                                         |
| ---------------------- | --------------------------------------------- |
| repository             | agents-remember                               |
| path                   | `mcp/src/agents_remember/cli/__main__.py`     |
| doc_type               | `file-level-onboarding`                       |
| lastUpdated            | 2026-09-29T07:08:34+02:00                     |
| lastVerifiedCommitHash | `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d`    |
| lastVerifiedCommitDate | 2026-09-29T09:20:54+02:00|
| governingOverview      | `../../../overview.md`                         |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`cli/__main__.py` is the umbrella `agents-remember` console entrypoint: a single front door
that dispatches subcommands. It registers **ten** of them — `dashboard`, `memory-citations`,
`memory-backfill`, `knowledge-ingest`, `knowledge-bootstrap`, `knowledge-format`,
`knowledge-validate`, `knowledge-index`, `knowledge-routes` and `review-record-comparison` — and
further CLI adapters slot in as subparsers. Backed by the
`agents-remember = agents_remember.cli.__main__:main` console script.

## Code Commentary

`build_parser()` builds an `argparse` parser with a required subcommand group and registers
each subparser through its adapter's own `add_arguments`, setting `func=<adapter>.run`:
`dashboard.add_arguments`/`dashboard.run`, `memory_citations.add_arguments`/`memory_citations.run`,
`memory_backfill.add_arguments`/`memory_backfill.run`,
`knowledge_ingest.add_arguments`/`knowledge_ingest.run`,
`knowledge_bootstrap.add_arguments`/`knowledge_bootstrap.run`,
`knowledge_format.add_arguments`/`knowledge_format.run`,
`knowledge_validate.add_arguments`/`knowledge_validate.run`,
`knowledge_index.add_arguments`/`knowledge_index.run`,
`knowledge_routes.add_arguments`/`knowledge_routes.run` and
`review_comparison_record.add_arguments`/`review_comparison_record.run`. `main(argv=None)` parses and
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

`knowledge-validate` (MIK-R22) is its read-only companion: the curator's standalone run of the
mandatory knowledge validator over a memory working tree, against a code checkout and optional
base commits. It writes nothing, and like the formatter it has no effect on unconverted memory: it
reports such a tree as out of scope and exits 0.

`knowledge-index` (MIK-R23) builds or reuses the derived knowledge index of one memory tree — a
working tree's captured state, or a Git tree read through objects — in an untracked cache outside
any Git working tree, and prints its key, state and counts as JSON. It only reads the tree; the
installed runtime does not call it before MIK-R37.

`knowledge-routes` (MIK-R04) is the curator's read-only view of family routes: for each family record of a memory working tree it prints the routes, the route state (`unrealized_family`, `route_unassigned`, uncovered realizations, emptied routes) and the mechanical route suggestion, labelled `mechanical`. It never writes a route, and on today's unconverted memory it answers "no family records".

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
| The `dashboard` subcommand adapter this dispatches to. | `run` | mcp/src/agents_remember/cli/dashboard.py:258-293 |
| The peer CLI adapter pattern. | `main` | mcp/src/agents_remember/cli/context_packet.py:20-63 |
| The memory-citations adapter, registered the same declarative way. | `add_arguments`; `run` | mcp/src/agents_remember/cli/memory_citations.py:53-117; mcp/src/agents_remember/cli/memory_citations.py:120-184 |
| The memory-backfill adapter: its `--contract` is the write guard that keeps a history rewrite off the official memory repository. | `add_arguments`; `run` | mcp/src/agents_remember/cli/memory_backfill.py:41-73; mcp/src/agents_remember/cli/memory_backfill.py:76-97 |
| The separate MCP server console entry that stays standalone. | `main` | mcp/src/agents_remember/mcp/__main__.py:5-8 |
| The `knowledge-ingest` subparser this umbrella registers for a leaf's curator hand-off list. | `knowledge_ingest`; "knowledge-ingest" | mcp/src/agents_remember/cli/__main__.py:49-57 |
| **The `knowledge-bootstrap` subparser this leaf adds: the taskless entry, registered the same declarative way.** | `knowledge_bootstrap`; "knowledge-bootstrap" | mcp/src/agents_remember/cli/__main__.py:58-66 |
| **The `knowledge-format` subparser `260928-MIK-L21` adds: the text knowledge files' canonical formatter, the umbrella's sixth registered subcommand.** | `knowledge_format`; "knowledge-format" | mcp/src/agents_remember/cli/__main__.py:67-72 |
| **The `knowledge-validate` subparser `260928-MIK-L22` adds: the curator's standalone run of the knowledge validator.** | `knowledge_validate`; "knowledge-validate" | mcp/src/agents_remember/cli/__main__.py:73-78 |
| **The `knowledge-index` subparser `260928-MIK-L23` adds: the derived knowledge index of one memory tree, built or reused and reported.** | `knowledge_index`; "knowledge-index" | mcp/src/agents_remember/cli/__main__.py:79-84 |
| **The `knowledge-routes` subparser `260928-MIK-L04` adds: the read-only family route report with the mechanical suggestion.** | `knowledge_routes`; "knowledge-routes" | mcp/src/agents_remember/cli/__main__.py:85-90 |
| **The `review-record-comparison` subparser `260921-ICR-L34` adds: the review comparison's production caller.** | `review_comparison_record`; "review-record-comparison" | mcp/src/agents_remember/cli/__main__.py:91-99 |

## Update History
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): the umbrella now registers **ten** subcommands. Added `knowledge-routes` (MIK-R04) to the Purpose list and the registration list, a paragraph for it and its row. The module docstring now names it too. The ingest, bootstrap, format, validate, index and review rows were re-pointed by the exact line shift (one import line, six registration lines), their claims unchanged. The verification stamp is unchanged; closeout owns it.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): the umbrella now registers **nine** subcommands. Added `knowledge-index` (MIK-R23) to the Purpose list and the registration list, a paragraph for it and its row. Re-measured the ingest, bootstrap, format and validate rows after the one-line import insertion and the six-line registration insertion. The verification stamp is unchanged; closeout owns it.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): the umbrella now registers **eight** subcommands. Added `knowledge-validate` (MIK-R22), its paragraph and its row. Re-measured the ingest, bootstrap and format rows after the six-line insertion, and corrected the format row's "seventh subcommand", which is no longer true. The verification stamp is unchanged; closeout owns it.
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): **the umbrella gains its seventh subcommand, `knowledge-format`.** MIK-R21 adds the text knowledge files' canonical formatter as `cli/knowledge_format.py`; this module registers it with the same declarative pair (`:63-68`). The Purpose count moves from six to seven, the Code Commentary's registration list gains the `knowledge_format` pair, and a paragraph records that this subcommand touches only the files it is given and is not called by the installed runtime before MIK-R37. The `knowledge-ingest`, `knowledge-bootstrap` and `review-record-comparison` rows were re-pointed to their shifted ranges (`:45-53`, `:54-62`, `:69-77`), and the `review-record-comparison` row no longer claims to be the reason the count is six. The adapter's own flags and exit codes are recorded on its card (`cli/knowledge_format.py.md`), not re-cited here. The earlier six-subcommand entries below are history. No verification stamp was advanced: the candidate is uncommitted and closeout owns the real stamp.
- 2026-09-28T18:18:00+02:00 — 260921-ICR-L47 curator (post-sync re-measure after the Architect's `worktree_sync` onto code `eda947325ccbe0791973953265278597e968a34a` / memory `6ccb9b615e383174c22f110a6492e6231a4e261f`; L47 candidate tree `5f22717e68041d6819e9671cee2ab30e4d3d3e13`): No content impact: citation ranges into files L44, L45 or L47 moved (`mcp/src/agents_remember/cli/dashboard.py`) were re-measured against the post-sync code; each re-pointed row held its anchors in its own measurement tree (`eda94732` or the pre-sync L47 candidate `72efa4bb`) and holds them after the line mapping, or names a literal that occurs exactly once in the post-sync file within five lines of its cited place. Claim wording unchanged. No stamp advanced.
- 2026-09-25T22:00:00+02:00 — 260921-ICR-L34 curator (leaf `260921-ICR-L34`, uncommitted change set on `ar/260921-icr-l34-ar`, code base `a9a1a41bba535803421470bd17d858657177cb5f` plus the working-tree delta): **the umbrella gains its sixth subcommand, and the count is corrected rather than extended.** `260921-ICR-L34` (D62) registers `review-record-comparison`, the CLI caller that gives the review comparison's freeze owner its first production caller outside the test suite; the registration is the same declarative pair (`add_arguments` + `set_defaults(func=...)`, `:61-69`) and the adapter owns its own flags and exit code. The body above said the parser registered **five** subcommands and listed them; it now says six and names this one, and the Code Commentary's registration list gained the sixth pair. The `260921-ICR-L29` entry below, which correctly said the count was five *then*, is history and not current policy. **No verification stamp was advanced** — the candidate is uncommitted, so no commit carries the content a stamp would claim to have verified, and the governed closeout owns the real code and memory commits.
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

