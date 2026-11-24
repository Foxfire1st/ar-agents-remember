# mcp/src/agents_remember/kernel/sidecar_pairing.py

## Governing Overview

[../../../overview.md](../../../overview.md)

## Purpose

`sidecar_pairing.py` is the shared, side-effect-free home for the 1:1
code↔onboarding sidecar resolution, the governing-route-index walk, and the
repo-relative path-confinement guard. The MCP tool and the dashboard `serving/files.py` HTTP API share these helpers without importing each other.

## Code Commentary

### Logic

These helpers confine paths and resolve source/card pairing. Confinement reads filesystem
metadata through path resolution and, for the stricter artifact helper, `lstat`.
Route-sidecar lookup reads the relevant governing indexes or paired-sidecar path.
The module writes no files and raises no domain events.

`confine_rel(code_root, requested)` is the path-confinement guard (formerly
`read_files._confined_rel`). It rejects an absolute path, then resolves the candidate
under `code_root`, following `..` and symlinks. It rejects the result only when the
resolved path escapes the root; an in-root `a/../b` spelling and an in-root symlink
are admitted and returned in resolved posix-relative form. The separate
`confine_non_symlink_rel` has the stricter component and symlink policy.

`route_sidecar_status(onboarding_root, rel)` walks the governing route-index chain
nearest-first via `_governing_indexes` / `_load_route_index`, asking
`route_index.sidecar_status` per index; the first index whose scope covers the path
decides (`present` / `absent`). When no governing index covers the path, it
probes both the mirror Markdown and JSON halves; either existing file is `present`. Its optional `observe` callback receives every path
whose identity decides that status — each candidate route index, an absent one
included — and, on the fallback, both card halves, **before** either is checked, so a
caller that reuses the answer observes exactly the inputs it was derived from instead
of re-deciding them on the next read. `sidecar_body(onboarding_root, rel)` reads the
mirror sidecar and projects it through `meaningful_body`, returning `None` when the
file is absent or non-decodable.

`is_file_sidecar(onboarding_rel)` and `source_path_from_sidecar(onboarding_rel)`
are the reverse-mapping helpers for `serving/files.py`. On a posix-relative
**string**, the route/entity overviews (`overview.md` / `entities.md`), the route
index, and `bootstrap/` docs are NOT per-source sidecars (they are
overview-without-code nodes); any other `.md` is a 1:1 sidecar whose source path is
the rel with the trailing `.md` stripped. These string helpers remain Markdown-only; the separate `route_index` Path helpers also recognize JSON card halves.


## No-Symlink Confinement

`confine_non_symlink_rel(root, requested)` provides stricter confinement
for artifact roots with immutable canonical addresses (the task-local
`requirements/` surface). Unlike `confine_rel` — which deliberately
follows in-root symlinks because code/onboarding pairing addresses the resolved
repository file — the guard requires every requested component to already exist
beneath `root` and refuses ANY symlink, even one pointing back inside the root.
It rejects empty/absolute/backslash/NUL paths and `.`/`..` segments, proves
the root exists and is not a symlink, walks each part with `lstat` (missing
components surface as `FileNotFoundError` for the caller), and finishes with a
containment proof against the resolved root. Invalid paths and symlinks raise `AuthorityError`;
missing components retain `FileNotFoundError`.

### Invariants And Boundaries

- **Purity is the contract.** No events, no ledger writes, no ambient state — this
  is why the module is safe for the dashboard's read-only files API to import.
- **A missing sidecar is never an error.** `route_sidecar_status` returns `absent`
  and `sidecar_body` returns `None`; callers decide how to present "this source has
  no onboarding yet". Confinement is a separate boundary: `confine_rel` rejects
  absolute or escaping paths with `AuthorityError`; `confine_non_symlink_rel` also
  rejects symlink aliases and leaves missing components as `FileNotFoundError`.
- **The first governing index whose scope covers the path decides.** The nearest-first governing
  walk decides; the mirror-file probe is only the fallback when no governing index
  covers the path. The `route_index` public surface (`sidecar_status` + the name constants)
  is consumed read-only; the small private prefix walk does not extend it.


## Evidence

### Repo-Internal References




- The read_ar_files naming entry point imports confine_rel and route_sidecar_status under their private aliases. [1]



- The dashboard files API that reuses this module (forward + reverse pairing, the path guard). [2]


- The `meaningful_body` extractor applied to a sidecar body here. [4]
- The mirror sidecar-path helper (`onboarding_root/<rel>.md`) is used for the body read; when no index covers the source, the fallback also probes the JSON half. [5]
- The `path_is_relative_to` confinement predicate used by `confine_rel`. [6]







- `sidecar_status` + `INDEX_FILE_NAME` / `ROUTE_OVERVIEW_NAME` / `ENTITY_CATALOG_NAME` consumed read-only. Anchor: `sidecar_status` [3]

- The `AuthorityError` raised on an out-of-root / absolute path. [7]
