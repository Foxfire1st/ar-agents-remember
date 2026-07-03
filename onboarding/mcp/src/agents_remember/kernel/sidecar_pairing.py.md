# mcp/src/agents_remember/kernel/sidecar_pairing.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/kernel/sidecar_pairing.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-28T22:41+02:00                     |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a` |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[../../../overview.md](../../../overview.md)

## Purpose

`sidecar_pairing.py` is the shared, side-effect-free home for the 1:1
code↔onboarding sidecar resolution, the governing-route-index walk, and the
repo-relative path-confinement guard. It was extracted from
`controllers/read_files.py` (the `read_ar_files` tool) so the **same** logic backs
both the MCP tool and the dashboard `serving/files.py` HTTP API (L1 of the
operations-integration series) without either consumer importing the other — and,
critically, without the dashboard pulling in the side-effecting `read_ar_files`
controller, which emits a `read.packet` event and mutates the served ledger.

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

| Finding | Source Path |
| --- | --- |
| The `read_ar_files` controller that these helpers were extracted from; it imports them under their former private names. | [controllers/read_files.py](agents-remember/mcp/src/agents_remember/controllers/read_files.py) |
| The dashboard files API that reuses this module (forward + reverse pairing, the path guard). | [serving/files.py](agents-remember/mcp/src/agents_remember/serving/files.py) |
| `sidecar_status` + `INDEX_FILE_NAME` / `ROUTE_OVERVIEW_NAME` / `ENTITY_CATALOG_NAME` consumed read-only. | [kernel/route_index.py](agents-remember/mcp/src/agents_remember/kernel/route_index.py) |
| The `meaningful_body` extractor applied to a sidecar body. | [kernel/onboarding_doc.py](agents-remember/mcp/src/agents_remember/kernel/onboarding_doc.py) |
| The mirror sidecar-path helper (`onboarding_root/<rel>.md`) used for the body read and the no-index probe. | [onboarding_drift_check/discovery.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py) |
| The `path_is_relative_to` confinement predicate used by `confine_rel`. | [mcp/config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| The `AuthorityError` raised on an out-of-root / absolute path. | [errors.py](agents-remember/mcp/src/agents_remember/errors.py) |

## Update History

- 2026-06-28T22:41+02:00 — Created for operations-integration L1: extracted the pure sidecar-pairing + path-confinement helpers from `controllers/read_files.py` (`confine_rel`, `route_sidecar_status`, `_governing_indexes`, `_load_route_index`, `sidecar_body`) so both the `read_ar_files` MCP tool and the new `serving/files.py` dashboard API share one source of truth without the side-effecting controller, and added the reverse-mapping helpers `is_file_sidecar` / `source_path_from_sidecar` for the files API. Behavior-preserving move. Verification metadata pinned until closeout stamps the L1 code commit.
