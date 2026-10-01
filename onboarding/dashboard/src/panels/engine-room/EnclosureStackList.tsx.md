# dashboard/src/panels/engine-room/EnclosureStackList.tsx

## Governing Overview

[engine-room overview](overview.md)

## Purpose

Renders the enclosure rail for the enclosure-centered Engine Room process map: a single-selection React Aria `ListBox` of worktree enclosures that drives which process the detail column shows. Each row surfaces an enclosure's leaf identity, parent task context, health, phase, and gate state (review, closeout, integration) from the server-composed `EngineProcessView`. Selection is controlled by the parent and keyed by `worktreeGroup`; this component derives no semantics and only presents the supplied views.

## Code Commentary

### Logic

One exported component, `EnclosureStackList`, taking `views: EngineProcessView[]`, the controlled `selectedKey: string | null`, and an `onSelect(key)` callback.

- The `ListBox` is `selectionMode="single"` with `disallowEmptySelection`; `selectedKeys` is `selectedKey ? [selectedKey] : []`. `onSelectionChange` receives a React Aria `Selection`: it bails on the `"all"` sentinel, then iterates the key set and calls `onSelect(key)` on the first `string` key before breaking — coercing React Aria's set-based selection back to the parent's single-key model.
- It maps each view's destructured `{ node, lifecycle }` to a `ListBoxItem` keyed/`id`'d by `node.worktreeGroup` (the stable enclosure identity that survives a fleeting→real promotion, 5f §8.3 — not the node `id`). `textValue` includes the leaf label, parent `taskName`, and repo so React Aria typeahead can match either identity.
- Each item body shows a health dot + `node.leafId || node.taskName` and a `phaseChip` carrying `node.phase`; the secondary line shows `taskName · repoName` when a leaf is present (otherwise just the repo), and a separate `stackMeta` chip row renders the optional `lifecycle.state` chip plus gate-state chips `review {node.humanReviewStatus}`, `closeout {node.closeoutStatus}`, and an `integ {node.integrationStatus}` chip shown only when integration is not `"not-started"` (5g G5 fix: repo off the chip row so the chips read cleanly; the rail scrolls vertically only — never horizontally).
- The `stackItem`, `healthDot`, and `phaseChip` Panda `cva` recipes are all driven by the `node.health` variant; `headWrap` is a local `css` flex helper. `data-testid` hooks (`enclosure-stack-list`, `enclosure-stack-item`) support the scenario tests.

### Invariants And Boundaries

- Fully controlled and presentational: it holds no state and re-derives nothing — `selectedKey` and the rendered order come straight from the parent/server (`views` preserves the server's deterministic process order).
- Keyed by `worktreeGroup`, not `node.id`: keeps selection (and the future promotion morph) stable when a fleeting start-progress node is replaced by its contract-anchored node.
- `disallowEmptySelection` plus the parent passing `[selectedKey]` means there is always exactly one selected enclosure once a selection exists; the `"all"` branch and the `typeof key === "string"` guard keep the single-key contract intact against React Aria's `Selection` union.
- `node.health` is the single styling driver across `stackItem`/`healthDot`/`phaseChip`; the integration chip is conditional on `node.integrationStatus !== "not-started"` and the lifecycle chip on `lifecycle` being present.

## Evidence

### Repo-Internal References

- `EnclosureStackList` component + props (`views`, `selectedKey`, `onSelect`) [1]
- Single-selection `ListBox`; `Selection` coerced to single key in `onSelectionChange` [2]
- Per-enclosure `ListBoxItem` keyed by `node.worktreeGroup`; `textValue` = taskName + repoName [3]
- Phase chip + gate-state chips (review/closeout/integration), conditional integ + lifecycle [4]
- `EngineProcessView` view type ({ enclosureKey, node, lifecycle }) [5]
- `EngineProcessNode` fields (worktreeGroup, phase, health, humanReviewStatus, closeoutStatus, integrationStatus) [6]
- `stackItem`/`healthDot`/`phaseChip` `health`-variant recipes [7]
- `stackList` layout keeps the enclosure rail vertically scrollable [8]
- `chip` styles define the compact status-chip presentation [9]
