# dashboard/src/panels/file-viewer/useFilesTree.ts

| Field | Value |
| ---------------------- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/file-viewer/useFilesTree.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-06-29T09:06+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

The `@headless-tree/react` adapter for the File Viewer: one async tree per side (`code` |
`onboarding`), both rooted at the selected `{repo, scope}`. It drives the two explorer columns over
the L1 files API without a per-node endpoint — the library owns async loading, selection, and keyboard
nav, and this hook supplies the data loader and Enter-to-open wiring.

## Code Commentary

### Logic

`useFilesTree(repo, scope, side, onOpen)` returns `useTree<DirEntry>`. `rootItemId = encodeId(repo,
scope, "")`; item ids pack `{repo, scope, path}` joined by a separator that never appears in a path
(NUL, per the header), so the scope is baked into every id and re-rooting can't collide across scopes.
Because `rootItemId` carries `{repo, scope}`, changing either (via the per-tree key) re-roots the whole
tree. `dataLoader.getChildren` returns `[]` when no repo is selected, else calls `listDir`
(`/api/files/list`) — which returns BOTH `code[]` and `onboarding[]` for a directory — picks this
side's array, caches each child `DirEntry` by id, and returns the child ids. `dataLoader.getItem`
resolves a node from that cache (L1 has no per-node read), falling back to a synthesized dir entry from
the decoded path. `onPrimaryAction` (keyboard Enter) calls `onOpen` only when the item is not a folder.
`features` = `asyncDataLoaderFeature` + `selectionFeature` + `hotkeysCoreFeature`.

### Invariants And Boundaries

Mouse folder expand/collapse is NOT owned here — `FileTree`'s own onClick owns it; this hook owns only
async loading, selection, keyboard nav, and Enter-to-open. The per-id cache is the only node store
(L1 exposes no per-node endpoint), so `getItem` must never assume a node was preloaded. The separator
must stay a character that cannot occur in a path, and the scope segment must remain in the id, or
re-rooting could collide across scopes.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `FileTree` renders this tree and owns the mouse click handler (folder toggle + file open). | `FileTree` | dashboard/src/panels/file-viewer/FileTree.tsx:44-96 |
| `listDir`, `DirEntry`, and `Scope` come from the L1 files client. | `listDir`, `DirEntry`, `Scope` | dashboard/src/data/files.ts:13-13; dashboard/src/data/files.ts:31-37; dashboard/src/data/files.ts:113-114 |
| `FileViewer` mounts one tree per side, re-keyed on `{repo}:{scope}:{side}`. | `FileViewer` | dashboard/src/panels/file-viewer/FileViewer.tsx:278-278 |

## Update History

- 2026-08-03T02:42:21+02:00 — W3-B04 curator: curated 1 table citation (1 total), supplying exact anchors and path; the scoped fixer generated all final extents.

- 2026-06-29T09:06+02:00 — Created for operations-integration L2 (File Viewer): the per-side async
  Headless Tree hook (one tree per `code`|`onboarding` side, rooted at `{repo, scope}`, `getChildren`
  over `/api/files/list` with a per-id `DirEntry` cache and Enter-to-open). Verification metadata pinned
  to the task base until closeout stamps the L2 code commit.
