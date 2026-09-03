# dashboard/src/data/requirements.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/requirements.test.ts`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-04T01:06+02:00 |
| lastVerifiedCommitHash | `1993dd25bdf8331a2c1e28171dff2bf92ea090e2` |
| lastVerifiedCommitDate | 2026-09-04T00:57:29+02:00 |
| governingOverview      | `overview.md`                              |

## Governing Overview

[data overview](overview.md)

## Purpose

Vitest unit coverage for `dashboard/src/data/requirements.ts`, the task-local
requirement-packet client introduced by 260831-CCR-L23. It pins the two request
bindings (list + read against the canonical repository/master/task-document
selector), the reserved `requirements/` prefix classification, and the pure
address/reference resolution rules — an exact registered address resolves, an
unregistered one does not, a `notes/...`-shaped or bare-filename mention is
never treated as a requirement address.

## Code Commentary

### Logic

`stubFetch` stubs global `fetch` to answer any URL with a 200 JSON payload,
and `afterEach(() => vi.unstubAllGlobals())` restores it. The fixture
`requirements` is one canonical packet entry (`requirements/CCR-R23-v1.md`)
the resolvers run against.

- **client binding** — the first case calls `listRequirements` and
  `readRequirement` for the same repo/master/document and asserts the exact
  encoded URLs, so the task-context selector is pinned to the wire and the path
  parameter is percent-encoded (`260831_master%2F23_leaf.json`).
- **address resolution** — an exact registered address maps to its path; a missing
  packet and a `notes/`-prefixed address both resolve to undefined.
- **reference extraction** — `requirements/CCR-R23-v1.md (approved packet)`
  yields the address and its resolved path; a bare filename without the reserved
  prefix yields nothing.
- **classification** — only the exact root prefix classifies: `notes/requirements/...`
  and full URLs return false.

### Conventions

Fetch is stubbed per test (never a live server); assertions target return values and
URLs, not implementation internals. The suite is deliberately small because the
resolution logic is total and side-effect free.

### Invariants And Boundaries

The suite pins the same no-guessing boundary as the client: only the server's own
listing authorizes a requirement address, and the reserved prefix is
`requirements/` alone.

## Docs References

No Domain Documentation source is configured for this repository-local client test.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The client under test. | `listRequirements`; `resolveRequirementReference` | dashboard/src/data/requirements.ts:26-32; dashboard/src/data/requirements.ts:64-69 |
| The component-level suite that exercises the same resolution through the detail reader. | "task requirement navigation" | dashboard/src/panels/detail-panel/taskRequirements.test.tsx:48-105 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 memory pass: created for the new
  requirement-packet client test module (wire bindings + address/reference
  resolution). Verified at code commit 1993dd25.
