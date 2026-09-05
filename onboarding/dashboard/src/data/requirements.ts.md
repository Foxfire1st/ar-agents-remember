# dashboard/src/data/requirements.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/requirements.ts`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-09-04T01:06+02:00 |
| lastVerifiedCommitHash | `1993dd25bdf8331a2c1e28171dff2bf92ea090e2` |
| lastVerifiedCommitDate | 2026-09-04T00:57:29+02:00 |
| governingOverview      | `overview.md`                                    |

## Governing Overview

[data overview](overview.md)

## Purpose

Browser client for the read-only task-local requirement-packet API introduced by
260831-CCR-L23, plus the pure requirement-address resolvers that let task prose and
References cells name `requirements/<path>.md` packets. It exposes typed helpers over
the two GET endpoints (`/api/requirements/list`, `/api/requirements/read`) and reuses
`data/files.ts`'s shared transport (`getJson`/`qs`) so the serving error idiom (a
thrown error on non-ok / a `bad-path`-style body) surfaces the same way every other
dashboard data client does. The client is read-only and stateless; all confinement,
symlink refusal, and inventory-bound enforcement stays server-side
(`mcp/src/agents_remember/serving/requirements.py`).

## Code Commentary

### Logic

`listRequirements(repo, master, document, base)` GETs
`/api/requirements/list?repo=...&master=...&document=...` and returns a
`RequirementsListing` (`registered` + `requirements: RequirementEntry[]`). The master
must be a single-segment master name and `document` the canonical task-document
reference (`<master>/<file>.json`) that selects the one `requirements/` root the
server walks; the client never invents a filesystem root.

`readRequirement(repo, master, document, path, base)` GETs
`/api/requirements/read?...&path=...` and returns a `RequirementContent` — one packet's
`RequirementEntry` metadata plus the decoded UTF-8 `content`.

The address vocabulary is deliberately small and reserved:

- `isRequirementAddress(value)` — true iff the value starts with the reserved
  `requirements/` prefix (an exact-prefix check, not a substring scan).
- `resolveRequirementAddress(address, requirements)` — maps an exact registered
  `requirements/...` address to its `path` (the listing is the authority; an address
  absent from the fetched listing resolves to undefined).
- `requirementAddressFromReference(reference)` — extracts the first
  `requirements/...<token>.md`-shaped address from freeform References prose
  (`PATH_TOKEN = /[\w./%-]+\.md/g` then `find(isRequirementAddress)`), so a reference
  like `requirements/CCR-R23-v1.md (approved packet)` yields the address and prose
  that merely mentions a bare filename is not guessed at.
- `resolveRequirementReference(reference, requirements)` — composes the two: extract,
  then resolve against the listing.

### Conventions

Same-origin typed client over `data/files.ts` (`getJson`/`qs`), mirroring `notes.ts`
for the sibling notes surface. Address helpers are pure and total over their inputs.

### Invariants And Boundaries

- The reserved root prefix is `requirements/` only: `notes/requirements/...` and full
  URLs are NOT requirement addresses (they stay notes/external links).
- Resolution never invents a packet: an address or reference that is not in the
  server's own listing resolves to undefined — the UI renders refusal, never a
  fabricated target.
- Read-only GET surface; no mutation endpoints exist.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared JSON transport and query-string helper the client is built on. | `getJson`; `qs` | dashboard/src/data/files.ts:90-100 |
| The listing and content shapes this client returns. | `RequirementsListing`; `RequirementContent` | dashboard/src/data/requirements.ts:11-17; dashboard/src/data/requirements.ts:19-24 |
| The server surface behind the two endpoints (task-context root selection + packet walk). | `register_requirements_routes` | mcp/src/agents_remember/serving/requirements.py:181-208 |
| The grammar provider that supplies the registered-packet listing to Markdown/TaskNotes. | `TaskRequirementLinksProvider` | dashboard/src/grammar/TaskRequirementLinks.tsx:13-61 |
| The client test suite. | "data/requirements client" | dashboard/src/data/requirements.test.ts:33-49 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| A same-origin view over the local serving API; nothing crosses repositories. | — | — |

## Update History

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 memory pass: created for the new
  task-local requirement-packet client and the reserved `requirements/` address
  resolution helpers (list/read + `isRequirementAddress` /
  `resolveRequirementAddress` / `requirementAddressFromReference` /
  `resolveRequirementReference`). Verified at code commit 1993dd25.
