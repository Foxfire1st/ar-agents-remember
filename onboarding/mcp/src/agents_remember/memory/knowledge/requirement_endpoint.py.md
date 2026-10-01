# mcp/src/agents_remember/memory/knowledge/requirement_endpoint.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Resolving a requirement endpoint of the text knowledge format (MIK-R13 rule 4, MIK-R21 rule 6).** A record's
link may name a requirement packet as `{ task: { repository, path }, packet, id, version }`
(`shapes.RequirementReference`). This module locates the owning task's root, `<coordination
root>/tasks/<repository>/<path>`, and hands `{ packet, id, version }` to the requirement owner
(`requirement_owner.consume_owner_resolution`). **The requirement owner remains the resolver** (packet
Preservation Boundaries): every packet answer is the owner's, verbatim. **Since MIK-R14 (rule 2)** it also answers
whether the owning task has a newer approved version: `latest_approved_requirement_version(task_root, stable_id)`
reads the task's `requirements/manifest.json`.

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
- **The manifest lookup (MIK-R14 rule 2).** `_manifest` reads `<task root>/requirements/manifest.json`
  (`MANIFEST_PATH`) and requires `format: approved-requirement-corpus` (`MANIFEST_FORMAT`) and a `packets` list;
  otherwise it returns why (no manifest, unreadable, wrong format, no `packets`). `_approved_entries` keeps each
  entry with the stable ID, `state: approved` and a version `v<n>` (`version_number`, the integer after `v`, no
  leading zero). `requirement_approval` answers a `RequirementApproval`: `approved` with the highest such version as
  `latest` and its `packet` (`requirements/<file>`, `None` when the entry names no `file`); `not_approved` when the
  manifest lists no approved entry for the ID; `unknown` with the reason as `detail` when there is no manifest this
  lookup can read. `newer_than(version)` compares the integers. `latest_approved_requirement_version` is the packet's
  named function: the same lookup's `latest`, or `None`.
- Only the manifest's `packets` list is read (ruling 2026-09-30T04:37:56 Q6: `not_approved` is accepted as a third
  state; this master's own `v1_packets` are not read).
- **Recording what was read (MIK-R09, L09 ruling 2026-09-30T15:09:25).** The approval state lives outside every Git
  tree, so the module records each file it reads for it through `kernel.recorded_reads.record_read` (a no-op outside
  a recording block):
  - `_manifest` now reads the bytes once and records the SHA-256 of exactly those bytes (`bytes_identity`), or
    `absent` for a missing manifest, or the identity now for an unreadable one; it then parses those bytes, so its
    answers are unchanged;
  - `resolve_requirement_endpoint` records the linked packet it hands the owner **before** the owner reads it, so a
    race can only cause a miss.

  The mandatory gate evaluates inside `recorded_reads()` and keeps its verdict with that read set; before reusing a
  kept verdict it hashes each file again, so a newly approved version, or a manifest that appears, forces a
  recompute that raises the reconsideration item (the approval-state test). The recorder itself moved to
  `kernel/recorded_reads.py` in the review R1 fix round.

### Conventions

- The module's own answers are only the two root codes; it never judges a packet.

### Invariants And Boundaries

- **An unresolved requirement endpoint is reported, never refused.** The function never raises for an unresolved
  endpoint and returns a value the caller reports; the record keeps the link exactly as written. Proved by
  `test_requirement_endpoints_resolve_through_the_owner_and_never_refuse` (resolved, version mismatch, missing
  packet, outside `tasks/`, no root) and, on real data, by the worker's and reviewer's runs (MIK-R21@v2 and MIK-R99
  reported `unresolved` with the owner's codes while the run was still written or planned).
- The root is used only to read task packets, never to write (review F8).
- **A task without a readable manifest never triggers a reconsideration** (MIK-R14 rule 2): its approval state is
  `unknown`, `newer_than` is false. Proved by `test_the_manifest_lookup_returns_the_highest_approved_version` (v10 is
  newer than v2; a draft and a superseded entry do not count; another ID is `not_approved`; a missing or
  wrong-format manifest is `unknown`) and `test_a_requirement_endpoint_triggers_only_on_a_newer_approved_version`.

### Todos

- **L26 (ruling 01:45:56 Q8):** if MIK-R26 retires the `memory/knowledge` database package, this resolver moves with
  `requirement_owner.py`.
- **L14 and L29 (ruling 01:45:56 Q5; review F2): L14's half is resolved.** MIK-R14's worklist step 8 reuses
  `resolve_requirement_endpoint` and then `requirement_approval` for every `reconsider_on` requirement endpoint, and
  reports each endpoint's state in the run's `reconsideration.links` summary. The reads remain L29's. A task that is
  later archived or moved makes its endpoints unresolved, which is reported, never refused, and never triggers.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R13@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`13_decision-records-with-rejected-alternatives.json`), MIK-R21 rules 4 and 6 for the record and requirement-reference
shapes, and the coordination-root note Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`,
section 4.5); they live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The locator, the resolver and its proof.

- The docstring's recording paragraph (MIK-R09). [1]
- The linked packet is recorded before the owner reads it. [2]
- The two answers that are this module's own, both about the root. [3]
- One endpoint, its state, its task root and the owner's answer; its index key. [4]
- The owning task's root, or none when the repository is not one directory. [5]
- No root, a root outside tasks, or the owner's answer verbatim. [6]
- The manifest path, format and version pattern; the approval states. [7]
- The integer after `v`. [8]
- What the manifest says about one ID, and the newer-than comparison. [9]
- The manifest read with its reasons, since MIK-R09 recording the exact bytes read; the approved entries of one ID. [10]
- The highest approved version and its packet, `not_approved`, or `unknown`; the packet's named function. [11]
- The lookup's cases. [12]
- The owner the packet question is handed to. [13]
- Resolved, version mismatch, missing, outside tasks and no root; the validator never resolves. [14]

### Cross-Repo References

No cross-repo boundary is crossed: the task plane read is the coordination root's `tasks/` tree of the same workspace, not another repository.

No cross-repo boundary is crossed by this file.
