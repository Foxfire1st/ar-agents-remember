# dashboard/src/panels/engine-room/EnclosureStackList.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/engine-room/EnclosureStackList.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-24T08:09+02:00                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `EnclosureStackList` component + props (`views`, `selectedKey`, `onSelect`) | `EnclosureStackList` | dashboard/src/panels/engine-room/EnclosureStackList.tsx:27-85 |
| Single-selection `ListBox`; `Selection` coerced to single key in `onSelectionChange` | "single"; `onSelectionChange`; `typeof` | dashboard/src/panels/engine-room/EnclosureStackList.tsx:39-39; dashboard/src/panels/engine-room/EnclosureStackList.tsx:42-42; dashboard/src/panels/engine-room/EnclosureStackList.tsx:45-45 |
| Per-enclosure `ListBoxItem` keyed by `node.worktreeGroup`; `textValue` = taskName + repoName | `worktreeGroup`; `textValue` | dashboard/src/panels/engine-room/EnclosureStackList.tsx:58-60 |
| Phase chip + gate-state chips (review/closeout/integration), conditional integ + lifecycle | `phase`; `state`; `humanReviewStatus`; `closeoutStatus`; `integrationStatus`; "not-started" | dashboard/src/panels/engine-room/EnclosureStackList.tsx:69-69; dashboard/src/panels/engine-room/EnclosureStackList.tsx:73-77 |
| `EngineProcessView` view type ({ enclosureKey, node, lifecycle }) | `EngineProcessView` | dashboard/src/panels/engine-room/engineRoomTypes.ts:15-25 |
| `EngineProcessNode` fields (worktreeGroup, phase, health, humanReviewStatus, closeoutStatus, integrationStatus) | `EngineProcessNode` | dashboard/src/types/projection.ts:162-202 |
| `stackItem`/`healthDot`/`phaseChip` `health`-variant recipes | `stackItem`; `healthDot`; `phaseChip` | dashboard/src/panels/engine-room/layout.styles.ts:127-155; dashboard/src/panels/engine-room/layout.styles.ts:194-215; dashboard/src/panels/engine-room/layout.styles.ts:230-256 |
| `stackList` layout keeps the enclosure rail vertically scrollable | `stackList` | dashboard/src/panels/engine-room/layout.styles.ts:112-125 |
| `chip` styles define the compact status-chip presentation | `chip` | dashboard/src/panels/engine-room/stage.styles.ts:252-252 |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-03T02:39+02:00 — W3-B01 curator: curated the component, selection, item, phase/status, and style citations; the W3-REV-2 correction delta repaired four generated extents so single selection/key coercion, the keyed `ListBoxItem`/`textValue` implementation, the full phase/status-chip behavior, and the `chip` definition/styles are each supported. Verification metadata remains unchanged for closeout.

- 2026-06-24T08:09+02:00 — Engine Room leaf identity: stack rows now use `leafId` as the primary label when present and render the parent `taskName` plus repo as secondary context, so parallel series leaves no longer appear as duplicate parent tasks. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-17T16:15 — slice 5g G5 (side-panel fix): the repo label moved to its own `stackRepo` line above the
  status chips; the list now scrolls vertically only (`stackList` `overflowX: hidden` + `minWidth: 0` down
  the tree so the name ellipsizes and the phase pill never clips) and the left rail widened. Verification
  metadata pinned until closeout stamps the G5 code commit.
- 2026-06-16T01:55 — slice 5f S0: list keyed by `worktreeGroup` (was `node.id`); prop renamed
  `selectedId` → `selectedKey` to match. Keeps selection stable across a fleeting→real promotion.
  Verification metadata pinned until closeout stamps the S0 code commit.
- 2026-06-15T19:35 — Created for slice 5e: React Aria ListBox of enclosures (selectable; textValue carries phase + gate state). Verification metadata pinned until closeout stamps the 5e code commit.
