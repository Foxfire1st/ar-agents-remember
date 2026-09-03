# mcp/src/agents_remember/kernel/sidecar_pairing.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/kernel/sidecar_pairing.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a` |
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[../../../overview.md](../../../overview.md)

## Purpose

`sidecar_pairing.py` is the shared, side-effect-free home for the 1:1
code↔onboarding sidecar resolution, the governing-route-index walk, and the
repo-relative path-confinement guard. It was extracted from
`application/read_files.py` (the `read_ar_files` tool) so the **same** logic backs
both the MCP tool and the dashboard `serving/files.py` HTTP API (L1 of the
operations-integration series) without either consumer importing the other — and,
critically, without the dashboard pulling in the side-effecting `read_ar_files`
application entry point, which emits a `read.packet` event and mutates the served ledger.

## Code Commentary

### Logic

Every function is pure over its `(root, rel)` arguments: it reads only the
onboarding / route-index files it is explicitly asked about, raises no domain
events, and writes nothing.

`confine_rel(code_root, requested)` is the path-confinement guard (formerly
`read_files._confined_rel`). It rejects an absolute path, then `resolve()`s the
candidate under `code_root` (following `..` and symlinks) and rejects it unless
`path_is_relative_to` the root — so a traversal token, a symlinked escape, or a
mid-path `..` is rejected, not just a literal `..`. Returns the posix-relative
form.

`route_sidecar_status(onboarding_root, rel)` walks the governing route-index chain
nearest-first via `_governing_indexes` / `_load_route_index`, asking
`route_index.sidecar_status` per index; the first index whose scope covers the path
decides (`present` / `absent`). When no governing `overview.index.json` exists, it
falls back to a direct `mirror_onboarding_path` file probe so a repo with sidecars
but no built index still resolves. `sidecar_body(onboarding_root, rel)` reads the
mirror sidecar and projects it through `meaningful_body`, returning `None` when the
file is absent or non-decodable.

`is_file_sidecar(onboarding_rel)` and `source_path_from_sidecar(onboarding_rel)`
are the reverse-mapping helpers added for `serving/files.py`. They mirror
`route_index._is_file_sidecar` / `_source_path_from_sidecar` on a posix-relative
**string**: the route/entity overviews (`overview.md` / `entities.md`), the route
index, and `bootstrap/` docs are NOT per-source sidecars (they are
overview-without-code nodes); any other `.md` is a 1:1 sidecar whose source path is
the rel with the trailing `.md` stripped.

### Invariants And Boundaries

- **Purity is the contract.** No events, no ledger writes, no ambient state — this
  is why the module is safe for the dashboard's read-only files API to import. The
  event/ledger side effects stay in `read_files.py`.
- **A missing sidecar is never an error.** `route_sidecar_status` returns `absent`
  and `sidecar_body` returns `None`; callers decide how to present "this source has
  no onboarding yet". The module raises only `AuthorityError`, and only from
  `confine_rel` on an out-of-root / absolute path.
- **The route index is authoritative when present.** The nearest-first governing
  walk decides; the mirror-file probe is only the fallback when no governing index
  exists. The `route_index` public surface (`sidecar_status` + the name constants)
  is consumed read-only; the small private prefix walk does not extend it.
- **Behavior-preserving extraction.** The moved helpers are byte-for-byte the
  originals; `read_files.py` imports `confine_rel` / `route_sidecar_status` /
  `sidecar_body` under their former private names, so the `read_ar_files` semantics
  and its test suite are unchanged.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `read_ar_files` application entry point that these helpers were extracted from; it imports them under their former private names. | `read_ar_files_tool` | mcp/src/agents_remember/application/read_files.py:77-133 |
| The dashboard files API that reuses this module (forward + reverse pairing, the path guard). | `resolve_onboarding` | mcp/src/agents_remember/serving/files.py:232-239 |
| `sidecar_status` + `INDEX_FILE_NAME` / `ROUTE_OVERVIEW_NAME` / `ENTITY_CATALOG_NAME` consumed read-only. | `sidecar_status`; `INDEX_FILE_NAME`; `ROUTE_OVERVIEW_NAME`; `ENTITY_CATALOG_NAME` | mcp/src/agents_remember/kernel/route_index.py:16-18; mcp/src/agents_remember/kernel/route_index.py:233-242 |
| The `meaningful_body` extractor applied to a sidecar body. | `meaningful_body` | mcp/src/agents_remember/kernel/onboarding_doc.py:94-108 |
| The mirror sidecar-path helper (`onboarding_root/<rel>.md`) used for the body read and the no-index probe. | `mirror_onboarding_path` | mcp/src/agents_remember/kernel/coordination_context/paths.py:42-52 |
| The `path_is_relative_to` confinement predicate used by `confine_rel`. | `path_is_relative_to` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:738-743 |
| The `AuthorityError` raised on an out-of-root / absolute path. | `AuthorityError` | mcp/src/agents_remember/errors.py:96-104 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T20:43+02:00 — W2-B08: anchored 5 sidecar-pairing reference claims with exact code anchors and corrected source paths; ranges remain generated by the scoped fixer. Verification metadata stays pinned until closeout.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-06-28T22:41+02:00 — Created for operations-integration L1: extracted the pure sidecar-pairing + path-confinement helpers from `controllers/read_files.py` (`confine_rel`, `route_sidecar_status`, `_governing_indexes`, `_load_route_index`, `sidecar_body`) so both the `read_ar_files` MCP tool and the new `serving/files.py` dashboard API share one source of truth without the side-effecting controller, and added the reverse-mapping helpers `is_file_sidecar` / `source_path_from_sidecar` for the files API. Behavior-preserving move. Verification metadata pinned until closeout stamps the L1 code commit.
