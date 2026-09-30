# mcp/src/agents_remember/memory/knowledge/requirement_endpoint.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/requirement_endpoint.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T03:13:03+02:00 |
| lastVerifiedCommitHash | `3eb034a6ab0493a51da5dcd6d013aa6f27f39496`|
| lastVerifiedCommitDate | 2026-09-30T03:31:21+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Resolving a requirement endpoint of the text knowledge format (MIK-R13 rule 4, MIK-R21 rule 6).** A record's
link may name a requirement packet as `{ task: { repository, path }, packet, id, version }`
(`shapes.RequirementReference`). This module locates the owning task's root, `<coordination
root>/tasks/<repository>/<path>`, and hands `{ packet, id, version }` to the requirement owner
(`requirement_owner.consume_owner_resolution`). **The requirement owner remains the resolver** (packet
Preservation Boundaries): every packet answer is the owner's, verbatim.

## Code Commentary

### Logic

- `requirement_task_root(coordination_root, reference)` returns `None` when `repository` is not one plain directory
  name (it contains a slash or a backslash, or is `.` or `..`); otherwise the task root. `RequirementReference`'s path type
  already refuses `..` and absolute task paths, and the owner contains the packet path.
- `resolve_requirement_endpoint(coordination_root, reference)` answers a `RequirementEndpoint`:
  - no coordination root: `unresolved`, `requirement-task-plane-unavailable` (`TASK_PLANE_UNAVAILABLE`);
  - repository not one directory: `unresolved`, `requirement-task-outside-tasks` (`TASK_OUTSIDE_TASKS`);
  - otherwise the owner's resolution: `resolved`, or `unresolved` with the owner's `refusal_code` and
    `refusal_detail` (for example `task-intent-requirement-packet-version-mismatch` or `…-packet-missing`).
- `RequirementEndpoint.task_root` is set whenever the root could be located, resolved or not, so a later reader
  (MIK-R14's lookup of a newer approved version in that task's `requirements/manifest.json`) starts from the same
  place. `key` is the index's spelling, `<repository>/<task path>#<id>@<version>`.

### Conventions

- The module's own answers are only the two root codes; it never judges a packet.

### Invariants And Boundaries

- **An unresolved requirement endpoint is reported, never refused.** The function never raises for an unresolved
  endpoint and returns a value the caller reports; the record keeps the link exactly as written. Proved by
  `test_requirement_endpoints_resolve_through_the_owner_and_never_refuse` (resolved, version mismatch, missing
  packet, outside `tasks/`, no root) and, on real data, by the worker's and reviewer's runs (MIK-R21@v2 and MIK-R99
  reported `unresolved` with the owner's codes while the run was still written or planned).
- The root is used only to read task packets, never to write (review F8).

### Todos

- **L26 (ruling 01:45:56 Q8):** if MIK-R26 retires the `memory/knowledge` database package, this resolver moves with
  `requirement_owner.py`.
- **L14 and L29 (ruling 01:45:56 Q5; review F2):** reuse `resolve_requirement_endpoint` for surfacing and reads.
  Today only a writer run reports endpoints, and only for the records that run touched; a task that is later
  archived or moved makes its endpoints unresolved, which is reported, never refused.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R13@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`13_decision-records-with-rejected-alternatives.json`), MIK-R21 rules 4 and 6 for the record and requirement-reference
shapes, and the coordination-root note Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`,
section 4.5); they live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The locator, the resolver and its proof.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two answers that are this module's own, both about the root. | `TASK_PLANE_UNAVAILABLE`; `TASK_OUTSIDE_TASKS` | mcp/src/agents_remember/memory/knowledge/requirement_endpoint.py:33-34 |
| One endpoint, its state, its task root and the owner's answer; its index key. | `RequirementEndpoint`; `key` | mcp/src/agents_remember/memory/knowledge/requirement_endpoint.py:39-59 |
| The owning task's root, or none when the repository is not one directory. | `requirement_task_root` | mcp/src/agents_remember/memory/knowledge/requirement_endpoint.py:62-68 |
| No root, a root outside tasks, or the owner's answer verbatim. | `resolve_requirement_endpoint` | mcp/src/agents_remember/memory/knowledge/requirement_endpoint.py:71-107 |
| The owner the packet question is handed to. | `consume_owner_resolution` | mcp/src/agents_remember/memory/knowledge/requirement_endpoint.py:29-29; mcp/src/agents_remember/memory/knowledge/requirement_endpoint.py:93-98 |
| Resolved, version mismatch, missing, outside tasks and no root; the validator never resolves. | `test_requirement_endpoints_resolve_through_the_owner_and_never_refuse` | mcp/tests/test_knowledge_decisions.py:280-311 |

## Cross-Repo References

No cross-repo boundary is crossed: the task plane read is the coordination root's `tasks/` tree of the same workspace, not another repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:13:03+02:00 — 260928-MIK-L13 curator (uncommitted change set on `ar/260928-mik-l13`, code base `3772cdcd008fcacdc5a86e264a3ef63e879ea544` plus the staged delta): created this card for the new file MIK-R13 adds, recording rulings 01:45:56 Q5 and Q8. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
