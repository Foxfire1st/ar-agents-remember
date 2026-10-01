# mcp/src/agents_remember/kernel/sidecar_pairing.py

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


## 260831-CCR-L23 No-Symlink Confinement

L23 added `confine_non_symlink_rel(root, requested)`, the stricter confinement
for artifact roots with immutable canonical addresses (the task-local
`requirements/` surface). Unlike `confine_rel` — which deliberately
follows in-root symlinks because code/onboarding pairing addresses the resolved
repository file — the new guard requires every requested component to already exist
beneath `root` and refuses ANY symlink, even one pointing back inside the root.
It rejects empty/absolute/backslash/NUL paths and `.`/`..` segments, proves
the root is a real non-symlink directory, walks each part with `lstat` (missing
components surface as `FileNotFoundError` for the caller), and finishes with a
containment proof against the resolved root. All refusals are `AuthorityError`.

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

## Evidence

### Repo-Internal References

- The `read_ar_files` application entry point that these helpers were extracted from; it imports them under their former private names. [1]
- The dashboard files API that reuses this module (forward + reverse pairing, the path guard). [2]
- `sidecar_status` + `INDEX_FILE_NAME` / `ROUTE_OVERVIEW_NAME` / `ENTITY_CATALOG_NAME` consumed read-only. [3]
- The `meaningful_body` extractor applied to a sidecar body here. [4]
- The mirror sidecar-path helper (`onboarding_root/<rel>.md`) used for the body read and the no-index probe. [5]
- The `path_is_relative_to` confinement predicate used by `confine_rel`. [6]
- The `AuthorityError` raised on an out-of-root / absolute path. [7]
