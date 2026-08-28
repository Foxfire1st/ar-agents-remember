# `w-02-light-task-workflow` template.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/template.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-28T11:32+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |

## Purpose

This template defines the required shape of `w-02-light-task-workflow` skill `task.md` artifacts inside task wrapper folders. Slice 3c makes it the **render spec** for the JSON-primary task document: the `task_doc` MCP tool renders an `ar-task-document/v1` JSON into exactly this shape (series master files stay hand-authored markdown).

## Code Commentary

### Logic

The synchronized task template separates protocol events from review-handoff attempts and makes
each attempt a lightweight content-addressed view rather than a duplicate master evidence body.

The template includes status, repo, type, objective, requirements, a `## Design` section, implementation steps, examples, decision log, open questions, and references. The `## Design` section sits above implementation steps and holds the settled design sized to the request per the Task Collaboration Doctrine (`tasks/AGENTS.md`), or a note that no design reasoning is needed. Usage rules include resolved `c-08-ar-coordination-context-resolver` skill paths and the wrapper location `<task-root>/<task-slug>/task.md`; when worktrees are created, `c-09-git-worktree-manager` skill places `contract.md` beside that file.

### Conventions

Task files use checkboxes for progress and a table for decisions. The template preserves sections even when a docs-only task does not need code examples; a planning slice that instead defers its examples to the plan gate sets `codeExamplesNote` so the section reads as deferred rather than none-needed. A leaf doc may also carry a `statusNote` suffix, `headerNotes` (extra `**Key:** value` header lines), and freeform `sections` appended after References for bespoke prose — the escape hatch; the standard sections stay the backbone (R4).

### Invariants And Boundaries

The template is a task artifact schema, not an onboarding schema. Its contents can cite onboarding but should not replace it.

### Todos

No current template TODO beyond adding examples from a real task wrapped by the `c-09-git-worktree-manager` skill.

### Docs References

No external domain documentation applies to this repository-local template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The template is the stable artifact shape for `w-02-light-task-workflow` skill.

| Finding | Anchor | Source |
| --- | --- | --- |
| The template requires status metadata, objective, requirements, a `## Design` section (sized per `tasks/AGENTS.md`), implementation steps, examples, decision log, open questions, and references. | `# Light Task Template` | mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/template.md:1-116 |
| Usage rules require `c-08-ar-coordination-context-resolver` skill resolved paths, wrapper-folder task placement, checklist progress, status changes, append-only decisions, and sizing the `## Design` section to the request. | "# Task: <Title>" | mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/template.md:10-10 |

## Cross-Repo References

No sibling repository evidence is needed for the current template file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Series-Contract Notes

The light-task template's artifact guidance points worktree-backed tasks at the leaf enclosure contract path under `enclosures/<leaf-id>/series-contract.md`.

## M38 Stable-Requirement Template Projection

The task scaffold now gives every requirement a stable ID and references the per-ID builder
acceptance envelope and reviewer verdict. Usage rules require complete delivery/verification
evidence and no overall pass with a rejected ID, while durable-evidence promotion remains separate.
The installed file is a synchronized render/template projection and owns no independent schema.
Each projection links the immutable version-addressed packet and its durable corpus ruling; the
task document remains non-normative summary rather than a compatibility copy of the contract.

## M40-M43 Leaf-Template Projection

The installed leaf template separates semantic versions from immutable exact-candidate attempts,
requires separate reviewer records and closed failure classes, and preserves the two authorized
invalidation paths.

## 2026-08-27 Attempt Boundary Clarification

This packaged projection preserves the canonical phase boundary: validate before append; a
malformed never-handed-off row receives a non-attempt correction/void without consuming an ID;
a malformed handed-off attempt requires independent rejection before successor handoff.

## Update History

- 2026-08-28T11:32+02:00 — No content impact: synchronized projection payload changed with the
  canonical one-primary requirement doctrine; projection ownership and byte-identity rules remain
  unchanged.

- 2026-08-27T22:15+02:00 — Synchronized the pre-handoff correction versus post-handoff rejection
  contract from canonical lifecycle/task doctrine.

- 2026-08-27T21:53+02:00 — Synchronized M40@v2 task-record semantics.

- 2026-08-27T18:06+02:00 — M40-M43: synchronized the leaf attempt-journal task contract.

- 2026-08-27T14:04+02:00 — Added immutable packet addressing and packet-local durable corpus
  approval to the installed task projection description.
- 2026-08-27T13:32+02:00 — M39@v1: the task scaffold now carries only stable ID + version +
  canonical-packet projections, records corpus approval, and enforces one primary revision per leaf
  with dependency/preservation rows unable to claim closure. Verification remains closeout-owned.

- 2026-08-27T12:43+02:00 — M38: recorded stable requirement IDs and the per-ID acceptance artifact
  contract. Verification metadata stays pinned until governed closeout stamps the PDLS commit.


- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: replaced the `n/a` rows with exact
  template heading anchors; exact non-fixing check returns zero findings.

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: packaged light-task template now points worktree-backed tasks at `enclosures/<leaf-id>/series-contract.md` instead of sibling `contract.md`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T06:03+02:00: Slice 3c reopened (R4, leaf-doc fidelity) — extended the status Usage Rule to cover the leaf extensions: a `statusNote` suffix, `headerNotes`, and freeform `sections` after References (the escape hatch; standard sections stay the backbone). Synced from canonical `skills/`. Verification metadata pinned until closeout stamps the R4 code commit.
- 2026-06-19T05:15+02:00: Slice 3c reopened (R3, deferred-examples honesty) — added the Usage Rule for `codeExamplesNote` (a deferred planning slice sets it so the rendered Proposed Code Examples section says so instead of "none needed"). Synced from canonical `skills/`. Verification metadata pinned until closeout stamps the R3 code commit.
- 2026-06-13T22:34: Slice 3c commit 2 — documented that this template is the render spec for the JSON-primary `task_doc` tool (renders `ar-task-document/v1` JSON into this `task.md` shape). Verification metadata pinned until closeout stamps the 3c commit-2 code commit.
- 2026-05-31T01:06+02:00: Added a `## Design` section above implementation steps (settled design sized per the Task Collaboration Doctrine) plus a usage rule for it; corrected the earlier "design philosophy" description that did not match the actual template.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-10T00:47: Updated after the `w-02-light-task-workflow` skill template became the `task.md` file inside task wrapper folders.
- 2026-05-09T22:57: Refreshed verification metadata and tightened template citations.
- 2026-05-09T21:59: Updated after worktree task contracts became part of the light-task artifact placement rules.
- 2026-05-09T21:15: Created first file-level onboarding baseline for `w-02-light-task-workflow` skill task template.
