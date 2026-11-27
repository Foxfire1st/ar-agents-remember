# mcp/src/agents_remember/application/read_files.py

## Governing Overview

[overview.md](overview.md)

## Current operative account — MIK-R109

`read_ar_files_reply` names governing knowledge for one to `READ_AR_FILES_MAX_PATHS` (20) repository-relative path strings. It resolves admitted context once, measures record states at the code tree observed for this read, and can return per-path existence, a readable governing card location or none, state counts, card state and action-asking record names and headings in the fuller reply. Each full row can also carry two counts taken from one reader selection over the same memory tree: `openWeaknesses`, the open weaknesses anchored to the file, and `dependentDocuments`, the documents that stand on it. Either count is absent at zero; a count that could not be taken is said in the row's `statesProblem` rather than answered as zero, without replacing a problem sentence the row already had, and an unconverted tree carries neither count. An eligible fuller row can carry local rule and weakness text assembled from current memory. A later eligible row can carry counts and a brief pointer when fuller detail does not fit. A compact reply can omit counts, full card detail and overview locations. The reader measures the saved brief's freshness and leaves the memory folder untouched. The full row keeps its brief pointer when rule text is shortened, with moved rules first. If the minimum expanded response exceeds the answer bound, every path gets a compact row. The row reports existence when known. A refused row names its refusal code. Other rows give card status and any brief path relative to `memoryRoot`, with saved freshness when needed. The caller opens source, card, sidecar and overview bodies with native tools. The caller can open the current saved brief when present. A pointer can name a missing saved file. The next write covering the file or its folder renews a missing or older saved brief when the writer can refresh it. A card with no Markdown half can carry `cardStatus: sidecar-only`. A fuller row can name its JSON half, the missing Markdown half and available record states and counts. Missing/unconverted memory names no card; an unavailable code observation leaves states unmeasured. A confined outside path is refused in its row without losing valid siblings. The sidecar and route index govern the card lookup. Fuller replies can list overview locations once per call in deterministic, deeper-first order. There is no published_intent payload, source-range parser, refresh/reset-marker consumer, served ledger or continuation. There is no ambient read.packet emission or per-file event-facts accumulator; completed-call observation belongs to the separate response boundary. Removed refresh is refused by the payload boundary, while object/non-string entries are refused here with argument-removed.

## Current source contract evidence


- The addressed read names governing knowledge. Fuller eligible rows can include bounded rule text. It emits no ambient `read.packet`.




## Purpose

`read_files.py` is the application entry point behind the `read_ar_files` MCP tool (slice 07).
It names a batch of up to twenty repository-relative paths inside an AR-managed repo. The mounted adapter takes the reply and its fitter. A mapping-only wrapper returns the payload dict.
Resolution lives here rather than in the payload module.

Dataset selection uses `select_knowledge_dataset` from `application/published_intent.py`; the naming response carries no `published_intent` block.

## Code Commentary

### Logic

The path-confinement guard and route-sidecar-status helper live in `kernel/sidecar_pairing.py`, shared with the dashboard `serving/files.py`; they are imported here under the private names `_confined_rel` and `_route_sidecar_status`.

`read_ar_files_reply(config, *, repo_id, files, working_folder, worktree_scope, _context)` is the mounted entry point. It resolves the repo through `require_repo` (authority check), validates the string-path batch and resolves the coordination context once via `resolve_coordination_context`, using `CoordinationHints`, `EnclosureSelector` and the contract reader. The `_context` keyword is still the test seam that injects a pre-built `CoordinationContext` to isolate one storage mode. It observes the code tree and assembles the naming payload. `BatchBriefs` composes the short answers against that same observation and supplies the fitter used with the delivered response metadata. The route has no ambient lifecycle read, served ledger or `read.packet` emission.



The format is `text/v2` exactly when the memory root (the onboarding root's parent) holds `knowledge/layout.json`.

`PublishedIntentDirectTests` exercises `published_intent_block` directly; the mounted naming route answers an unconverted tree with no card.





`_confined_rel` is the path-confinement guard. It rejects an absolute
path, then `resolve()`s the candidate under the code root (following `..` and
symlinks) and rejects it unless `path_is_relative_to` the code root — so a
traversal token, a symlinked file/dir escaping the repo, or a mid-path `..` that
climbs out is rejected, not just a literal `..`. It returns the posix-relative
form.



`_governing_card` resolves the storage mode for the path via `resolve_storage_for_source`; `repo-sidecar`, `memory-repo` and `external` use the sidecar route, while a path outside that scope has no card. `_route_sidecar_status` walks the governing route-index chain nearest-first via `_governing_indexes` / `_load_route_index`, asking `sidecar_status` per index; the first index whose scope covers the path decides. When no governing index covers the path, it probes both the mirror Markdown half and JSON half. The application also probes the card's own path when the index did not list it: either existing half is named, and the answer identifies stale index coverage. A readable JSON half with no Markdown is `sidecar-only`; an indexed card with neither half present at its own path names no card or record states.

Every requested path is confined again when `_overview_locations` derives its overview chain, independently of the per-file naming call.



### Invariants And Boundaries

- **Path confinement is the security boundary.** Every requested path — and every
  path used to derive the overview locations — runs through `_confined_rel`, which
  resolves real paths before the check, so symlink/traversal escapes are rejected,
  not just literal `..` tokens. Paths must be repo-relative, never absolute.

- **The route index decides coverage; an existing in-scope card remains readable when the index omits it.** The application probes the card's own Markdown and JSON paths, names an existing half and identifies stale index coverage.

- The route-index public surface is consumed read-only here; the small private
  nearest-route prefix walk does not extend it.




## Evidence

### Repo-Internal References













- The import of `TEXT_FORMAT` and `memory_format` for memory selection. [4]








| Repo-resolution authority guard. | `require_repo` | mcp/src/agents_remember/kernel/authority.py:16-24 |
| The authority-violation error raised by path confinement. | `AuthorityError` | mcp/src/agents_remember/kernel/sidecar_pairing.py:38-50 |
| Coordination-context resolution and per-path storage-mode resolution. | "_resolver.resolve_coordination_context" | mcp/src/agents_remember/kernel/coordination_context_resolver.py:131-146 |
| The shared confinement helper resolves the requested path and refuses a repository escape; read_files imports it as _confined_rel. | "def confine_rel(" | mcp/src/agents_remember/kernel/sidecar_pairing.py:37-49 |
| The shared sidecar status helper consults governing indexes and falls back to a mirrored file probe; read_files imports it as _route_sidecar_status. | "def route_sidecar_status(" | mcp/src/agents_remember/kernel/sidecar_pairing.py:91-106 |

| `ROUTE_OVERVIEW_NAME` consumed read-only for governing overview locations. | `ROUTE_OVERVIEW_NAME` | mcp/src/agents_remember/kernel/route_index.py:17-17 |

### Runtime Source References




- The batch's overview locations: each named path contributes its ancestor chain, every overview is listed once for the call, and deeper chains sort before their ancestors. [7]



- The mounted payload delegates to the reply wrapper and passes its fitter to the shared completion boundary. [1]

- The memory-format switch selects the converted index when available and names no card for other memory states. [3]


- A fuller naming row can carry its governing card and action records. A compact row keeps its path and any recorded existence. A refusal has its code. Other compact rows give card status and any brief pointer with saved freshness. [6]
