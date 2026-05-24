# C-02-memory-quality-control/SKILL.md

| Field                  | Value                                                              |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember-md                                                 |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-02-memory-quality-control/SKILL.md` |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `31846c1136f0fe75503a63fb557303a79fa022e8` |
| lastVerifiedCommitDate | 2026-05-24T23:07:31+02:00|

## Purpose

This skill defines C-02 as the memory quality control workflow. It keeps the
task-start drift gate for onboarding trust, adds the pre-code-commit
missing-onboarding pass for newly added source files, and describes the
closeout memory quality gate that runs before the memory content commit.

## Code Commentary

### Logic

The skill instructs agents to use C-08/MCP context resolution, run `drift_check`
as the task-start trust baseline, classify drift into clean-source update
candidates versus dirty-source active work-in-progress, run
`agents_remember.memory_quality.integrity.check_missing_onboarding` before a
code commit when the task added source files, and run `memory_quality_check`
after onboarding refresh and before the memory content commit. It keeps the
drift classifier rules for file-level sidecars, route overviews, inline blocks,
and repo entity catalog fingerprints.

### Conventions

C-02 reports and routes memory quality work; it does not rewrite onboarding
prose. Task-start drift reports remain local coordination artifacts under
C-08's resolved `temp_root`. Closeout style checks do not run at task start.
Mechanical style repair is done by targeted fixers only after
`memory_quality_check` reports a finding.

### Invariants And Boundaries

C-02 must stay read-only with respect to onboarding prose. Any content update
belongs to C-05. Drift reports are temporary evidence, not durable onboarding,
and explicit report paths inside a durable memory repo should be redirected
back to the resolved coordination temp area. Implementation approval is not
commit approval; C-02 can report quality state, but C-09 owns commit approval
gates.

### Todos

Add tests for C-02 against a migrated external memory repo once such a fixture exists.

### Docs References

No external domain documentation applies to this repository-local maintenance skill.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

C-02 is the memory quality control gate used before implementation, before code
commit when new files exist, and before the memory content commit during
closeout.

| Finding                                                                                                                                                                                                                                    | Citations | Source Path                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- | ---------------------------------------------------------------------------------------------------- |
| The skill names task-start drift, pre-code-commit missing-onboarding checks, closeout `memory_quality_check`, and targeted style repair as one C-02 quality control workflow. | L27-L40 | [C-02 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-02-memory-quality-control/SKILL.md) |
| Task-start quality control runs MCP `drift_check`, preserves the gradual-adoption boundary for historical files without onboarding, and separates clean-source update candidates from dirty-source active work-in-progress before C-05 handoff. | L67-L91 | [C-02 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-02-memory-quality-control/SKILL.md) |
| Pre-code-commit quality control runs `check_missing_onboarding` only against current worktree additions so newly added files cannot escape onboarding. | L147-L164 | [C-02 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-02-memory-quality-control/SKILL.md) |
| Closeout quality control runs MCP `memory_quality_check` and uses focused fixers such as `history_order_fix.py` only after reported findings. | L166-L191 | [C-02 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-02-memory-quality-control/SKILL.md) |

## Cross-Repo References

No cross-repo evidence is needed for the current skill contract.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` added clean-source versus dirty-source drift classification to C-02.
- 2026-05-24T04:34+02:00: Refreshed verification metadata after C-02 memory quality control source landed.
- 2026-05-24T04:05+02:00: Renamed C-02 to memory quality control and expanded the skill around drift, missing-onboarding, closeout quality, and style fixer procedures.
- 2026-05-15T12:57+02:00: Documented entity catalog inventory-to-fingerprint reconciliation, including missing fingerprint rows and orphaned fingerprint rows. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-15T11:46+02:00: Refreshed after C-02 added route-overview checks and deterministic repo-entity fingerprints. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-12T18:51+02:00: Refreshed after the skill frontmatter moved to the lowercase `c-02-onboarding-drift-detection` name.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-11T18:34: Updated after the C-02 helper command examples adopted `--code-repository-root`.
- 2026-05-10T03:11: Updated after C-02 documented that explicit report paths inside `memory_root` are redirected to coordination temp.
- 2026-05-10T00:36: Refreshed verification metadata after the temp-root drift report behavior landed on main.
- 2026-05-09T23:22: Updated after C-02 moved default drift reports under C-08's temporary artifact root.
- 2026-05-09T22:57: Refreshed verification metadata and clarified that reports are coordination artifacts.
- 2026-05-09T21:59: Updated after C-08 split memory roots from coordination roots.
- 2026-05-09T21:15: Created first file-level onboarding baseline for C-02 skill documentation.
