# mcp/src/agents_remember/worktrees/modules/onboarding_trace.py

## Governing Overview

[worktrees/modules route overview](overview.md)

## Purpose

**The onboarding refresh gate on history files (MIK-R30@v1), for converted memory trees.** Today's gate
(`onboarding.py`) reads Update History entries and `lastVerifiedCommit*` metadata; a converted tree has
neither. This module is the replacement rule as a pure function: given the changed source files and the two
memory sides K_B and K_C as path-to-bytes maps, it raises one `onboarding_trace` item per card and per
nearest governing route overview, decides whether each is satisfied, and renders the repair findings, the
report-only findings and the closeout refusal. It reads no Git; the application layer
(`application/knowledge_worklist/onboarding_trace.py` and `leaf.py`) resolves the sides.

## Code Commentary

### Logic

- **Items (rule 2).** `onboarding_trace_result(context, changed_paths, sides)` raises:
  - one item with subject `onboarding:<path>` for every changed source whose storage is sidecar-backed
    (`_card_sources`, through the resolver's storage rules) **and** whose card (`onboarding/<path>.md` or its
    `.json` sidecar) exists on either side. A changed source with no card anywhere raises nothing here:
    today's missing-onboarding refusal owns it (`onboarding.py` `_require_onboarded_sources`);
  - one item per **nearest** governing route (`nearest_governing_route`: the nearest ancestor directory of
    `onboarding/<path>.md` holding `overview.md` in K_C, from `_routes`), subject
    `onboarding:<route>/overview`, or `onboarding:overview` for the root route (`route_subject`). The item's
    `sources` are every changed path that route governs.
- **Counted change (rule 3).** `counted_change` is `counted_markdown_change` (any byte change of the
  Markdown, creation and deletion included) or `counted_sidecar_change`. A sidecar change counts unless it
  is limited to anchors' `blob`, `content` and a `line_range` locator's `start`/`end`
  (`_without_mechanical_fields`, which recognises an anchor by `_is_anchor`: a `locator` mapping plus `blob`
  and `content`). Who made the change does not matter: the writer's carry, the reference fixer and a curator
  touching only those fields all count for nothing.
- **Satisfaction.** `TraceItem.open` is `unreadable or (not counted and row is None)`; `row` is the ID of
  the leaf's `no_impact` `OnboardingTraceRow` with the item's subject (`_history_rows`, reading
  `knowledge/history/<owner>.json` from K_C). An item's `id` is `sha256:[kind, subject, sources]`, the same
  formula as the registry's `item_id`.
- **Unreadable inputs, never a pass.**
  - `OnboardingTraceSides.incomplete` (mixed formats, no pairing, a conversion failure) yields no items and
    one `onboarding-trace-incomplete` problem.
  - An unparseable history file is one `onboarding-trace-history-unreadable` problem, and no row satisfies
    anything.
  - An unparseable **K_C** sidecar (`sidecar_unreadable`) keeps its item open whatever else changed, with
    the action "sidecar unreadable ... repair it through the writer"; `counted_sidecar_change` never counts
    an unreadable new sidecar, but counts a readable repair of an unreadable old one.
  - An unparseable **K_B** sidecar is one `onboarding-trace-base-sidecar-unreadable` problem naming the
    sidecar: the fixed base commit cannot be repaired in the leaf.
- **Output.** `OnboardingTraceResult` carries the items, the unnecessary rows (a row whose subject raised no
  item), the problems and the pairing. `ok` is no open item and no problem. `repair_findings` is one finding
  per problem plus one `onboarding-trace-missing` finding per open item naming the card or route, its sources
  and `required_action`; `report_only_findings` lists each unnecessary row as `onboarding-trace-unnecessary`,
  and since MIK-R10 each finding also carries the row's `subject` (additive), so the memory-quality controller
  can keep an `onboarding:<path>` row that answers an uncovered unexplained change out of that report
  (`_needed_rows_dropped`, ruling 2026-09-30T01:56:39 Q3);
  `refusal` is the closeout text naming every problem and open item; `brief` and `summary` are the tool and
  worklist views.
- **The stored-item predicate.** `onboarding_item_open(item, rows_by_subject)` applies both halves of the
  satisfying rule to an item **document** (what `knowledge-worklist.json` stores) for MIK-R09's generic gate.
  An item whose facts carry `sidecarUnreadable`, or that has no facts, is open regardless of its counted
  change or a row; otherwise it is open when `countedChange` is not `true` and no row has its subject.
  `TraceItem.to_document` writes `countedChange: false` and `satisfiedBy: null` for an unreadable item, so
  the stored document and the live gate cannot disagree.
- **Every history file of the leaf counts (L37, reopen ruling).** `_history_rows` reads the leaf's plain history
  file and each attempt-qualified file (`owner_history_attempt`) from the candidate, in attempt order, and merges
  them with `merged_leaf_history`: a later attempt's row about a subject supersedes the earlier one, and a row of
  the closed file still counts. Trace rows are presence-based, so a closed `no_impact` row still answers a
  reopened leaf's item for the same card. Any one unreadable file is the `onboarding-trace-history-unreadable`
  problem, naming that file.

### Conventions

- The module lives in the worktrees layer beside `onboarding.py` and imports only the kernel resolver, the
  canonical-JSON parser and the knowledge-file models; the sides arrive as mappings.
- Finding codes and the check name (`onboarding-trace`) are module constants.

### Invariants And Boundaries

- **On a converted tree only a counted change or a history row satisfies a trace** (architect ruling
  2026-09-29T18:49:50 (1)). A curator-coherence no-impact judgment, which satisfies today's body gate, does
  not count here; the `no_impact` row is the durable replacement for Update History (D23).
- **The root route's subject is `onboarding:overview`** (ruling 18:49:50 (3)), as MIK-R24's marker move
  writes it. A root-level source file literally named `overview` would share that subject; none exists.
- **The gate never passes on inputs it cannot compare.** Mixed formats and unestablished sides are an
  incomplete side with a named reason (ruling 19:23:45 N1); an unreadable K_B sidecar is an incomplete input
  (ruling 19:53:54 R2-2).
- **An unreadable sidecar never counts as a refresh** (ruling 19:23:45 N5): an unreadable K_C sidecar keeps
  its item open until the leaf repairs it, and a readable repair counts as a change (ruling 19:53:54 R2-2).
- **The stored-item predicate agrees with the live gate** (ruling 19:53:54 R2-1): `onboarding_item_open`
  over a stored item and `TraceItem.open` give the same answer, including for unreadable sidecars.
- **Only the nearest governing route is gated**, as today (preservation boundary).
- **Inert until the cutover.** Nothing calls this module unless K_B or K_C holds the layout marker; every
  production leaf before MIK-R37 keeps today's gate (`onboarding.py`).

### Todos

- MIK-R10 binds each uncovered `unexplained_*` item to this gate's item for its file
  (`knowledge_worklist/unexplained.settle_uncovered`); this module's items are read, never changed.
- MIK-R09 (L09) must enforce stored `onboarding_trace` items through `onboarding_item_open`, not through the
  registry's generic row lookup alone, which covers only the row half.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R30@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`30_onboarding-refresh-gate-on-history-files.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: items, satisfaction, the counted-change rule and findings. [1]
- The kind name and the finding codes. [2]
- Card and route subjects, the root route as `onboarding:overview`. [3]
- Anchors lose `blob`, `content` and line numbers before a sidecar comparison. [4]
- An unparseable sidecar is never a counted change; a readable repair of one is. [5]
- Sides that could not be established carry a named reason. [6]
- One item, its open state and its stored document. [7]
- The result, its repair and report-only findings, and the refusal. [8]
- Each unnecessary-row finding names its subject (MIK-R10). [9]
- The leaf's `no_impact` rows, or the unreadable-history problem. [10]
- The nearest governing route of a changed path. [11]
- The gate: card and route items, the incomplete side and the unreadable base sidecar. [12]
- The stored-item predicate L09 uses. [13]
- The row model a `no_impact` row validates against. [14]
- The memory-quality and closeout entry points that call the gate. [15]
- Only mechanical fields changed: the item stays open. [16]
- The stored predicate and the live gate agree on an unreadable K_C sidecar. [17]

- The leaf's rows come from all of its history files, read as one history. [18]

### Cross-Repo References

No meaningful cross-repo references found: the module compares two in-memory views of one memory
repository.

No cross-repo boundary is crossed by this file.
