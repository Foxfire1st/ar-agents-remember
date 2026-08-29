# c-02-memory-quality-control/SKILL.md

| Field                  | Value                                                              |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                 |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md` |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-08-29T08:52+02:00                     |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a` |
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|

## Purpose

This skill defines `c-02-memory-quality-control` skill as the memory quality control workflow. It keeps the
task-start drift gate for onboarding trust, adds the pre-code-commit
missing-onboarding pass for newly added source files, and describes the
closeout memory quality gate that runs before the memory content commit.

## Code Commentary

### Logic

The skill instructs agents to use `c-08-ar-coordination-context-resolver` skill/MCP context resolution, run `drift_check`
as the task-start trust baseline, classify drift into clean-source update
candidates versus dirty-source active work-in-progress, run
`agents_remember.memory_quality.integrity.check_missing_onboarding` before a
code commit when the task added source files, and run `memory_quality_check`
after onboarding refresh and before the memory content commit. It keeps the
drift classifier rules for file-level sidecars, route overviews, inline blocks,
and repo entity catalog fingerprints. During a curator leaf pass, the full scoped quality call
also replaces one enclosure-local checklist combining the repairable work, current-addition
coverage, stale indexes, source-change candidates, and noteworthy evidence; the curator reruns it
until the zeroable count clears.

### Conventions

`c-02-memory-quality-control` skill reports and routes memory quality work; it does not rewrite onboarding
prose. Task-start drift reports remain local coordination artifacts under
`c-08-ar-coordination-context-resolver` skill's resolved `temp_root`. Closeout style checks do not run at task start.
Mechanical style repair is done by targeted fixers only after
`memory_quality_check` reports a finding.
The curator checklist is the explicit temp-location exception: it lives under the leaf worktree
enclosure's reserved `reports/` directory, outside both Git worktrees, and replaces its predecessor.

### Invariants And Boundaries

`c-02-memory-quality-control` skill must stay read-only with respect to onboarding prose. Any content update
belongs to `c-05-create-or-update-onboarding-files` skill. Drift reports are temporary evidence, not durable onboarding,
and explicit report paths inside a durable memory repo should be redirected
back to the resolved coordination temp area. The enclosure checklist is temporary operational
evidence and is garbage-collected with the worktrees. Implementation approval is not
commit approval; `c-02-memory-quality-control` skill can report quality state, but `c-09-git-worktree-manager` skill owns commit approval
gates.

### Todos

Add tests for `c-02-memory-quality-control` skill against a migrated external memory repo once such a fixture exists.

### Docs References

No external domain documentation applies to this repository-local maintenance skill.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | — | — |

## Repo-Internal References

`c-02-memory-quality-control` skill is the memory quality control gate used before implementation, before code
commit when new files exist, and before the memory content commit during
closeout.

| Finding | Anchor | Source |
| --- | --- | --- |
| The quality-control phase table distinguishes task-start drift, curator intake, pre-commit coverage, closeout validation, and targeted style repair. | "## Quality Control Phases" | mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md:30-38 |
| Task-start quality control preserves the gradual-adoption boundary for historical files without onboarding and separates clean-source update candidates from dirty-source active work-in-progress before `c-05-create-or-update-onboarding-files` skill handoff. | "Run Task-Start Drift Control" | mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md:71-107 |
| Pre-code-commit quality control checks only current worktree additions so newly added files cannot escape onboarding. | "Run Pre-Code-Commit Missing-Onboarding Control" | mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md:164-180 |
| Closeout quality control runs the full memory gate and uses focused style fixers only after reported findings. | "Run Closeout Memory Quality Control"; "Use Targeted Style Fixers Only After Findings" | mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md:234-234; mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md:261-261 |

## Cross-Repo References

No cross-repo evidence is needed for the current skill contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260821-DAGQC-L2 Canonical Quality Calls

The packaged skill now uses the same strict `request={mode: ...}` grammar as the public tool. Sync,
start, and poll examples keep their field sets separate; capacity refusal directs the caller to
poll/wait and retry rather than bypassing the controller. This packaged copy remains synchronized
from canonical doctrine and introduces no compatibility path.

## MCAR-L02 Structured Coherence Workflow

The packaged memory-quality doctrine now treats the deterministic structured checklist as the
candidate census, then requires `curator_coherence prepare` → agent-owned exact judgments → atomic
`publish` → shared `validate`. It separates raw quality readiness from combined closeout readiness,
uses explicit evidence namespaces, keeps requirement/attempt/digest identities distinct, and
forbids hand-versioned reports or filename fallback. Same-input quality reruns preserve bytes;
changed inputs intentionally stale the authority.

## Update History

- 2026-08-29T08:52+02:00 — MCAR-L02 A005: synchronized the structured coherence publication and
  combined-readiness workflow. Verification remains closeout-owned.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: synchronized the memory-quality workflow to the canonical discriminated request and capacity retry guidance. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-11T16:54+02:00 — Documented the full scoped curator checklist, its stable enclosure
  path, overwrite/cleanup lifetime, and repeat-until-zero repair loop.
- 2026-08-03T04:32:19+02:00 — W3-B08 curator: curated 4 citations (citation_anchor_missing=2, citation_prose_not_in_cit_form=0, citation_source_malformed=2); final scoped citation check clean.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` added clean-source versus dirty-source drift classification to `c-02-memory-quality-control` skill.
- 2026-05-24T04:34+02:00: Refreshed verification metadata after `c-02-memory-quality-control` skill memory quality control source landed.
- 2026-05-24T04:05+02:00: Renamed `c-02-memory-quality-control` skill to memory quality control and expanded the skill around drift, missing-onboarding, closeout quality, and style fixer procedures.
- 2026-05-15T12:57+02:00: Documented entity catalog inventory-to-fingerprint reconciliation, including missing fingerprint rows and orphaned fingerprint rows. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-15T11:46+02:00: Refreshed after `c-02-memory-quality-control` skill added route-overview checks and deterministic repo-entity fingerprints. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-12T18:51+02:00: Refreshed after the skill frontmatter moved to the lowercase `c-02-onboarding-drift-detection` name.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-11T18:34: Updated after the `c-02-memory-quality-control` skill helper command examples adopted `--code-repository-root`.
- 2026-05-10T03:11: Updated after `c-02-memory-quality-control` skill documented that explicit report paths inside `memory_root` are redirected to coordination temp.
- 2026-05-10T00:36: Refreshed verification metadata after the temp-root drift report behavior landed on main.
- 2026-05-09T23:22: Updated after `c-02-memory-quality-control` skill moved default drift reports under `c-08-ar-coordination-context-resolver` skill's temporary artifact root.
- 2026-05-09T22:57: Refreshed verification metadata and clarified that reports are coordination artifacts.
- 2026-05-09T21:59: Updated after `c-08-ar-coordination-context-resolver` skill split memory roots from coordination roots.
- 2026-05-09T21:15: Created first file-level onboarding baseline for `c-02-memory-quality-control` skill documentation.
