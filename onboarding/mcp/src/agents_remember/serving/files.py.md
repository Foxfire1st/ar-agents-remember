# mcp/src/agents_remember/serving/files.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`files.py` is the read-only **files API** (L1 of the operations-integration
series): the serving-layer bridge from the dashboard to the kernel
`CoordinationContext`. It lets the File Viewer (L2) and the Change-Set Viewer
(L3/L4) enumerate repositories and their `{mainline + active worktree
enclosures}`, list a scoped directory level (code + paired onboarding), read one
file's content + onboarding metadata, and resolve the 1:1 code↔onboarding sidecar
pairing in both directions. The shared serving/scope.py resolver supplies CoordinationContext-backed roots to this API and the change-set routes.

## Code Commentary

### JSON declarations and media routes

The catalog, listing, text read, path resolution and onboarding routes declare `response_model`; the bytes route returns media responses. cit:([`register_files_routes`], mcp/src/agents_remember/serving/files.py:362-412) Each JSON handler returns a `JSONResponse` it built itself, and FastAPI applies `response_model`
only to values it serializes for you — so these declarations contribute an OpenAPI
schema and validate nothing at runtime. The former broad conformance suite was removed in IAS testing cleanup. Its historical execution is not current enforcement; the declarations remain the response contract.

The declarations, in `serving/response_contract.py`:

- `GET /api/files/repos` → `RepoCatalog`, and it is the **one route in this family with no
  `responses=` table at all**: the catalog is assembled from the allow-list itself, so it has no
  refusal branch to declare.
- `GET /api/files/list` → `DirectoryListing`
- `GET /api/files/read` → `FileContents`
- `GET /api/files/onboarding` → `OnboardingResolution`

The listing, text read, path resolution, bytes and onboarding routes share `SCOPED_READ_RESPONSES` (400 / 404), which declares the shared scope error map: `StatusRefusal` on 400, and `UnknownRepoRefusal | UnknownScopeRefusal |
MissingPathRefusal` on 404. The bytes route also maps the separate typed media refusals.

`OnboardingResolution` is a **five-shape union**, and declaring it that way is the honest
contract rather than a convenience: `direction` picks the forward/reverse pair
(`OnboardingForwardFound | OnboardingForwardMissing` vs. `OnboardingPartnerSidecar |
OnboardingPartnerOverview | OnboardingPartnerNone`), and within each pair `status`/`kind`
discriminates further. Declaring only the forward shape would have been a lie about half the
route's traffic. `DirectoryListing.code` carries the discriminated `CodeNode` union for the same
reason — only a `kind: "file"` row may carry `language`/`hasSidecar`, and only it must.



### Logic

The shared scope layer (`FileScope`, `resolve_scope`, `run_scoped`, `language_for`, `_iter_repo_contracts`/`_find_enclosure_contract`, `_resolve_within`, `_LANG_BY_EXT`) lives in sibling `serving/scope.py`, so `serving/changeset.py` reuses it. `files.py` imports `FileScope`, `_resolve_within`, `language_for` and `run_scoped` from `.scope`,
along with its catalog, decoding and response helpers, and **re-exports** `FileScope` +
`_resolve_within` for existing callers/tests. The scope resolver and error map are shared with `serving/changeset.py`.

`register_files_routes(app, config)` registers six GET routes and **must** be
called before the greedy static `/` mount in `serving/app.py` (its registration precedes the later APIs and static delivery). Routes: `GET /api/files/repos` (catalog), `/api/files/list`,
`/api/files/read`, `/api/files/onboarding?direction=forward|reverse`, `/api/files/bytes` and `/api/files/resolve`. The scoped JSON routes are
thin closures over `run_scoped` (in `serving/scope.py`), which resolves the scope and maps domain
errors to the serving status-string `JSONResponse` idiom: an unknown repo →
`404 unknown-repo`, an unknown enclosure → `404 unknown-scope`, an out-of-root /
absolute path → `400 bad-path`, an absent file → `404 not-found`. The bytes route shares run_scoped_response; the catalog has no scoped operation. JSON operations return camelCase dictionaries at 200; the bytes operation returns the media response or its typed refusal.

`resolve_scope(config, repo_id, scope_id)` maps `{repo, mainline|enclosure}` to a
frozen `FileScope` (`code_root`, `onboarding_root | None`, `memory_root | None`,
branch, contract). The repo is gated through `require_repo` (the allow-list
authority — `AuthorityError` on an unknown id). For an enclosure scope it finds the
on-disk leaf contract whose `worktree_group` basename matches and resolves against
the contract; otherwise it resolves the mainline. It then calls
`resolve_coordination_context`, taking `code_worktree or code_repository_root` as
the code root. **If the repo has no AR memory** (`MissingMemoryError`), it degrades
to a code-only scope (`onboarding_root=None`) rather than failing — code stays
browsable and onboarding resolves uniformly "missing".

`list_repos(config)` is the catalog: every `config.allowed_repo_ids` entry with its
mainline (always) and its active enclosures, enumerated on a catalog TTL miss in one walk from
`iter_leaf_enclosure_contracts(coordination_root/"tasks")` via `_assemble_repo_catalog` and `_iter_active_contracts`
— filtered to the allow-listed `repo_name`, skipping `cleanup=="abandoned"` and any
enclosure whose `code_worktree` no longer exists, and tolerating a malformed
contract (`ContractError`/`OSError` → skip, never abort).

`list_dir(scope, rel_dir)` lazily lists one level: code children from `code_root`
(each file annotated with `language` and `hasSidecar` via `route_sidecar_status`)
plus the parallel onboarding children from `onboarding_root` when present.
`read_file(scope, rel)` returns fixed-media metadata without reading payload bytes; otherwise it serves a file's content (capped at `_MAX_FILE_BYTES` = 2
MiB with a `truncated` flag; an initial-NUL or non-UTF-8 file degrades to `language:"binary"`,
empty content) — the cap goes through the shared
`scope.decode_capped`, cutting at a UTF-8 codepoint boundary so a multi-byte char
straddling the cap returns the first ~2 MiB + `truncated:true` instead of empty
`binary` — and `_onboarding_meta` (the drift-bearing
`lastVerifiedCommitHash`/`Date` when a sidecar is present, else `status:"missing"`).
`resolve_onboarding` (forward) returns a code path's sidecar status + body;
`resolve_partner` (reverse) maps a sidecar to its partner code path (with an
`exists` flag for orphans) or classifies an overview-without-code node. An
overview/entities/index doc has **no code partner**, so the reverse node now also
carries its own `"body"` (via `_onboarding_doc_body`) — the File Viewer renders that
markdown directly instead of showing an empty "no code partner" placeholder, so a
route overview is readable, not just an unopenable tree leaf.
`_onboarding_doc_body(scope, rel)` reads that raw text from the onboarding root with the
same guards as `read_file` — confined through `_resolve_within`, capped at `_MAX_FILE_BYTES`
via the same `scope.decode_capped` codepoint-boundary cut, and binary-tolerant — returning
`None` for a missing / unreadable / non-UTF-8 file (the reader then falls back to the
placeholder) and `None` when the scope has no onboarding root.
`_resolve_within(root, rel)` is the per-call confinement: `""`/`"."` is the root,
everything else goes through `confine_rel` (so an absolute or escaping path is
rejected, never silently re-rooted).

### Invariants And Boundaries

- **Security posture (Task-6):** GET-only, read-only, 127.0.0.1-bound, no
  auth/CORS added. The repo allow-list is `config.allowed_repo_ids` via
  `require_repo`; a `repo_name` off a contract that is not allow-listed is never
  trusted. Every served path is confined to a resolved root via `confine_rel` —
  realpath-checked, symlink-safe — so no traversal escapes a code/onboarding root.
- **Missing onboarding is never an error.** A code file with no sidecar →
  `status:"missing"` (the placeholder the File Viewer renders); a repo with no AR
  memory degrades to code-only browsing rather than a 409 that would blank the
  scope. `MissingMemoryError` is a repo-level condition (no durable memory exists),
  never raised per-file.
- **Routes register before the static mount.** The `/` `StaticFiles` mount is
  greedy; `/api/files/*` must be registered first or the SPA index swallows them.
- **The pairing logic is shared, not re-derived.** All sidecar resolution +
  confinement comes from `kernel/sidecar_pairing.py`; this module owns only the
  scope/catalog resolution, the HTTP shape, and the read cap.
- **Enclosure catalog construction reads on-disk active contracts and uses the short catalog TTL**, not projection-derived enclosure rows, so a newly started or closed worktree appears after catalog refresh without a projector tick. Scope resolution still resolves its requested contract.
- **The declared response models are the contract.** These handlers return `Response` objects, so the model declaration alone does not validate their bodies. The removed conformance suite is not current protection. A new key emitted by `list_dir`,
  `read_file`, `resolve_onboarding` or `resolve_partner` must land in the matching model in
  `serving/response_contract.py` in the same change — `extra="forbid"` makes an undeclared key a
  failure, which is the point.

## Evidence

### Repo-Internal References

- The shared scope layer in `serving/scope.py` owns `FileScope`, `resolve_scope`, `run_scoped`, `language_for` and `_resolve_within`. [1]
- The app factory calls register_files_routes before the later API registrations and mount_static. [2]
- The shared, side-effect-free sidecar pairing + path-confinement helpers this module reuses. [3]
- The scope resolver + `CoordinationContext`/`MissingMemoryError` bridged here. [4]
- The repo allow-list authority guard (`require_repo` → `RepositoryScope`). [5]
- `McpRuntimeConfig` (`allowed_repo_ids`, `repositories`) + the `path_is_relative_to` guard. [6]

- The leaf-enclosure contract enumerator the catalog walks. [7]

- The `WorktreeContract` (`code_worktree`, `worktree_group`, `cleanup`) + `load_contract`/`ContractError`.



| The JSON routes declare `RepoCatalog`, `DirectoryListing`, `FileContents`, `FileResolution` and `OnboardingResolution`; the bytes route returns media responses under the shared scoped-read declarations. | `register_files_routes` | mcp/src/agents_remember/serving/files.py:362-412 |
| Current production declaration; the removed broad suite supplies no current execution proof. | `register_files_routes` | mcp/src/agents_remember/serving/files.py:362-412 |

## Repository catalog reuse

`list_repos` now walks the task surface once, buckets entries by repository, and applies a short TTL memo. The repository-files API no longer repeats the same whole-task-tree traversal for each repository in one request.



- The `WorktreeContract` (`code_worktree`, `worktree_group`, `cleanup`) + `load_contract`/`ContractError`.

- The files reader uses table_metadata for Markdown-table metadata and mirror_onboarding_path to derive the source-to-sidecar .md path. [9]
