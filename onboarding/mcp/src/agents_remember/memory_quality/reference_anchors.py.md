# mcp/src/agents_remember/memory_quality/reference_anchors.py

## Governing Overview

[memory_quality route overview](overview.md)

## Purpose

**Reference anchors at the exact pair: one observation per anchor, the rule-1 census, and the repair classes the fixer and the curator split between them (MIK-R198 rules 1-2).** A code or test reference target carries an anchor — the source path, a locator inside it, the Git blob it was recorded against and the content identity of the located bytes. This module is one traversal over one knowledge tree and one paired code tree, and it resolves each anchor through the same product pieces the fixer runs, so the state reported here is the state the guard and the fixer see, never a parallel reading of the source.

## Code Commentary

### Logic

- `observe(sidecar, field, target, path, source)` classifies one anchor. An absent path is `stale:path-absent`. Located bytes equal to the recorded content with an equal blob are `current`; the same bytes with a moved blob are `stale:blob`, whose repair is the blob alone. Otherwise the shipped fixer's own `refreshed_anchor` decides: if it re-records the anchor, the state is `moved:range`; if it refuses, `_judged` names what is left for judgment.
- `_judged` and `_judged_range` keep the judgment cases distinct: a whole-file anchor whose content changed, a locator the paired tree cannot resolve (`stale:unresolved`), changed content that still resolves, more than one identical same-length range (`stale:ambiguous`, up to five starts named), and a range with exactly one identical match whose blob already matches — the fixer refreshes no such anchor, so the census reports `stale:content` and says to re-record it from the source read.
- `AnchorObservation` carries the sidecar, field, kind, path, rendered locator, the recorded and actual blob and content, the state, the repair and the reason; `to_document` renders the row the census and the bounded answer carry.
- `census(tree, source)` counts the observations into `states` and `repairs`, per-sidecar rows, per-source-route totals, and splits the affected sidecars into `documents` (repairable) and `judgmentDocuments`. `ok` holds only when no input is invalid and every observation is current; `debtCount` is the remainder of the denominator.
- `_source_route` takes a target's first path segment as its route, so `routes` accounts every route's targets by state and reconciles to the denominator.
- `_documents` and `_card_names` name the affected sidecars by their onboarding-relative card. A sidecar without a card cannot be named by a citation work order, which takes cards, so it is appended after the cards rather than dropped, and the curator chooses its route instead of assuming one.
- `unreadable_sidecars` names onboarding `*.json` files the product parser cannot read as sidecars; `rejected_sidecars` names readable files the tree parser refused because their location contradicts their own declaration, compared by physical path so an accepted sidecar declaring that path cannot hide the refused one (L191-A3-02). Both are reported, and either one makes the census incomplete.
- `observations_of` takes already-parsed sidecars, so a validator route parses the knowledge tree once instead of once per rule; it prefetches the distinct paths from the code tree before observing. `observations` parses the tree itself, through `_sidecars`, which keeps file and route sidecars only.
- `_parse_tree` and `_parse_document` import the validator's parser lazily: the validator package imports this module's rule module, so a module-scope import of its submodules would be a cycle.
- `census_for_memory` is the directory run: one converted memory directory against one code directory, through `knowledge_tree_from_directory` and `CodeDirectory`, with the memory path as the census's memory label.

### Conventions

- States, repairs and the rule id are module constants, and `render_locator` spells the three locator kinds as one comparable line: `file`, `symbol:<name>`, `line_range:<a>-<b>`.
- A repair is claimed only where the shipped fixer's function returns one; the module asks `refreshed_anchor` rather than re-implementing its rule, so the census can never promise a repair the fixer will refuse.

### Invariants And Boundaries

- **Mechanical and judgment classes are the fixer's, not a second opinion.** A test asserts the parity in both directions: nothing is promised that the fixer cannot do, and nothing repairable is sent to judgment.
- **Uncertainty is never relabelled as a false claim.** An absent path, an unresolvable locator, changed content and ambiguity keep distinct states and distinct reasons.
- **An incomplete census cannot answer `ok`.** An unreadable or location-refused sidecar is named and counted as an invalid input instead of leaving the denominator silently.
- **The census schedules repair; it does not repair and does not judge meaning.** It reads, classifies and names the cards; the fixer writes and a curator reads the source for the judgment cases.

### Todos

None recorded.

## Evidence

- The module states the four classes, the exact-pair requirement and the fixer reuse it is built on. [1]
- The census schema tag and the rule id the validator registers. [2]
- A locator is rendered as one comparable line for the three locator kinds. [3]
- Every start whose same-length lines carry the recorded content. [4]
- One anchor's state at one pair, and what closes it, decided through the shipped fixer's function. [5]
- The observation record, its `current` test and the row projection. [6]
- The judgment states the shipped repair rule refuses. [7]
- A range's judgment: ambiguous, one identical match the fixer will not refresh, or no identical range. [8]
- Every code or test target of one sidecar, with its `references.N.targets.I` field. [9]
- Already-parsed sidecars are observed, and the distinct paths are prefetched once. [10]
- Only file and route sidecars are observed. [11]
- The onboarding sidecars the product parser cannot read. [12]
- The readable sidecars the tree parser refused for their location, compared by physical path. [13]
- A target's source route is its first path segment. [14]
- The rule-1 census counts states, repairs, per-sidecar rows and per-route totals that reconcile to the denominator, and answers `ok` only when no input is invalid and every anchor is current. [15]
- The affected sidecars split into repairable and judgment documents. [16]
- Card names are split from the cardless remainder rather than dropping it. [17]
- The directory pair run the CLI calls. [18]
- The parser is imported lazily because the validator package imports this module's rule module. [19]
- Current is the only zero-debt state. [20]
- A same-blob anchor with a wrong locator is judgment because the fixer refuses it. [21]
- Route totals reconcile to the denominator. [22]
- Mechanical repair is claimed exactly where the shipped fixer repairs. [23]
- A range that appears twice is ambiguous and needs judgment. [24]
- A sidecar the parser refused is named and the census is not complete. [25]
- An accepted sidecar cannot alias a rejected one out of the accounting. [26]
- The directory census measures a working-tree pair. [27]
