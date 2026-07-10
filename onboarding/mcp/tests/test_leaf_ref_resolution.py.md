# mcp/tests/test_leaf_ref_resolution.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_leaf_ref_resolution.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-08T23:59+02:00                     |
| lastVerifiedCommitHash | `79b2fd6c4da73c7845406f6c68b947b8bd0e1009` |
| lastVerifiedCommitDate | 2026-07-10T22:22:16+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[tests overview](overview.md)

## Purpose

`test_leaf_ref_resolution.py` pins the shared task-tree leaf-ref resolver introduced by HFX-L4. It is
focused coverage for accepted canonical forms, legacy aliases, no-match reporting, ambiguity reporting,
start-scope task-root consistency, sibling JSON artifact handling, read-path contract tolerance,
light-task candidate indexing, loud marker-bearing malformed-doc handling, and HFX2-L8's boot-safety
skip for malformed non-task JSON artifacts.

## Code Commentary

The temp fixtures write real `TaskDocument` master and subtask JSON/Markdown pairs through
`write_task_doc`, then call `resolve_leaf_ref` directly. The tests prove:

- qualified refs, doc ids, and legacy slug/file stems normalize to one `repo/master/doc-id` identity;
- no-match errors use `leaf-ref-not-found`, include `<repo>/<master-folder>/<doc-id>`, and list a nearby
  candidate;
- ambiguous legacy slugs use `leaf-ref-ambiguous` and list both candidate qualified ids;
- a fully qualified ref outside the caller's requested `task_name` is rejected instead of being attached
  to the wrong start contract;
- a missing optional master `task.json` is skipped, malformed non-task sibling JSON is ignored for boot
  safety, while a malformed schema-marked leaf JSON file raises;
- sibling JSON artifacts without the task-document schema marker are ignored by resolver and
  `load_contract` normalization;
- `load_contract` keeps a legacy leaf id unchanged when active-task resolution cannot prove the mapping;
- standalone/light `task.json` docs resolve from their doc id, slug/folder, and enclosure aliases.

## Invariants And Boundaries

- The tests cover resolver policy, not terminal catalog mutation or worktree start side effects.
- Fixtures use real task-doc writes so candidate aliases match production task-tree shape.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Resolver under test. | [../src/agents_remember/worktrees/leaf_refs.py](../src/agents_remember/worktrees/leaf_refs.py.md) |
| Task document writer used to create representative task trees. | [../src/agents_remember/tasks/overview.md](../src/agents_remember/tasks/overview.md) |

## Update History

- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (minimal projection robustness): added a regression for
  malformed sibling JSON without the task-document schema marker being ignored, while schema-marked
  malformed task docs still fail loud. Verification metadata pinned until closeout stamps the
  260707-HFX2-L8 commit.
- 2026-07-07T23:45+02:00 — 260707-HFX-L4R2: added regressions for schema-marked malformed task docs,
  non-task sibling JSON artifacts, live-style contract loading with sibling artifact JSON, unproven
  read-path contract mapping, and standalone/light task-doc candidate aliases. Verification metadata
  pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: created focused resolver coverage for canonical leaf-ref
  validation, normalization, candidate errors, task-scope mismatch refusal, missing optional master docs,
  and malformed-doc loud failures. Verification metadata pinned until closeout stamps the 260707-HFX-L4
  commit.
