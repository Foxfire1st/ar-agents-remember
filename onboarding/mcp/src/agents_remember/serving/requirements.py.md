# mcp/src/agents_remember/serving/requirements.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/requirements.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T08:27+02:00 |
| lastVerifiedCommitHash | `ea35964985f30080488270e71ac81657ac40682b` |
| lastVerifiedCommitDate | 2026-09-05T06:48:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[serving overview](overview.md)

## Purpose

The read-only task-local requirement-packet API (260831-CCR-L23): the server half of
`/api/requirements/{list,read}`. The client selects exactly one canonical
`tasks/<repo>/<master>/requirements/` root by repository, single-segment master,
and canonical task-document reference and walks it for Markdown packets with stable
`requirements/<path>.md` addresses. Every filesystem component is confined and
must be a real non-symlink node; the surface is GET-only.

## Code Commentary

### Logic

`_selected_root(config, repo_id, master, document)` validates the selector:
master must be a single segment, the document must be a canonical POSIX task-document
reference (`TaskDocumentRef` round-trip), and `TaskDocumentTopology.resolve`
must return the exact document under `tasks/<repo>/<master>` — otherwise the
selector is not one canonical context (`RequirementContextError`).

`_registered_root(root)` returns the exact `requirements/` directory or
`None` when absent, refusing symlinked or escaping roots. `_walk_packets`
walks the root depth-first (bounded to `_MAX_INVENTORY_DEPTH = 8` and
`_MAX_INVENTORY_FILES = 2_000`), skipping non-Markdown and non-regular files and
failing closed on any symlink, and emits one metadata packet per file
(`name/path/address/size/sha256`). `_packet` decodes UTF-8 (a decode error
propagates to the error mapper) and hashes the exact bytes.

`list_requirements` returns the listing envelope (`registered` +
packets); `read_requirement` confines the client-supplied rel against the root
with `confine_non_symlink_rel`, requires a `.md` suffix and a regular file,
and returns metadata + decoded content.

`_requirements_json` is the shared error mapper: unknown repo `404`
(`unknown-repo`), bad selector `400 bad-context`, missing root/packet
`404 not-found`, and confinement/decode/value/os errors `400 bad-path`.
`register_requirements_routes` mounts the two GET endpoints with the declared
response models and shared refusal table from `response_contract.py`.

### Conventions

All reads are GET and confined server-side; addresses stay stable
`requirements/<path>.md` values; the module never lets the client name a
filesystem root.

### Invariants And Boundaries

- Selector and inventory both fail closed: a non-canonical context, a symlink root or
  child, a depth/file-count overflow, or an escaping path is a typed refusal, never a
  silent read.
- Registered-root confinement is stricter than code/onboarding pairing
  (`confine_non_symlink_rel` refuses in-root symlink aliases too).
- The packet address is derived from the walk, never from client text.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Route registration + the two handlers. | `register_requirements_routes` | mcp/src/agents_remember/serving/requirements.py:181-208 |
| Task-context root selection and the registered-root guard. | `_selected_root`; `_registered_root` | mcp/src/agents_remember/serving/requirements.py:45-72; mcp/src/agents_remember/serving/requirements.py:75-87 |
| The stricter no-symlink confinement reused by read. | `confine_non_symlink_rel` | mcp/src/agents_remember/kernel/sidecar_pairing.py:52-92 |
| The declared models + shared scoped-read refusal table. | `RequirementRow`; `RequirementsListing`; `RequirementContents`; `SCOPED_READ_RESPONSES` | mcp/src/agents_remember/serving/response_contract.py:767-798; mcp/src/agents_remember/serving/response_contract.py:1103-1109 |
| Composition: the app registers this surface. | `register_requirements_routes` | mcp/src/agents_remember/serving/app.py:283-284 |
| The HTTP proofs. | `RequirementRouteTests` | mcp/tests/test_serving_requirements.py:30-276 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-05T08:27+02:00 — L31 native curator: Removed the leaked diff-marker bullet after checking root selection; retained the GET-only requirement-packet contract and refreshed the scoped-read refusal-table evidence. Reviewed against frozen code `ea35964985f30080488270e71ac81657ac40682b`; this records source verification, not gate acceptance.

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 memory pass: created for the new
  task-local requirement-packet serving module (confined GET-only list/read over the
  `tasks/<repo>/<master>/requirements/` root). Verified at code commit 1993dd25.
