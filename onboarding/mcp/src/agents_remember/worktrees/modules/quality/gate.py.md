# mcp/src/agents_remember/worktrees/modules/quality/gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees/modules overview](../overview.md)

## Purpose

This module is the narrow policy and process adapter that makes the repository-owned
certification profile a mandatory, fail-closed lifecycle gate. Since CCR-R22@v1 (L22, commit
`685f83c44055`) leaf closeout requires one explicit configured profile whenever code would be
committed, admits it against the exact task worktree, and runs the profile-declared
change-set-scoped adapter exactly once before creating its commit; leaf integration reuses that
certified commit without invoking this runner again. Master integration runs the full
profile-declared adapter once with container-runtime-managed RAM and swap by default inside
`worktree_integrate` itself. An explicit settings cap (memoryCapBytes) remains available for
full runs; the executor identity now belongs to the profile, not to agentic settings.

It also owns the latest completed gate transcript. The caller supplies a `QualityGateTarget`
containing the checkout, its worktree enclosure, the repository id, and the profile reference;
every completed run atomically replaces `<worktree_group>/reports/test-results.md`, and success
returns that path plus profile-bound evidence while failure publishes the same full output before
raising.

Applicability is now all-or-nothing for code commits: there is no consumer
`wrapper-unavailable` state. A repository with no valid configured profile has no legal
code-commit route; preview and apply refuse with `certification-profile-invalid` instead of
skipping the gate. Older tasks without code changes remain valid and do not need a profile merely
to be read or recovered. The former self-policy `requires_integrated_acceptance` (removed in
this commit) is replaced by the universal requirement that every code-committing repository admit
its own profile.

## Code Commentary

### Logic

`QualityGateTarget` binds the exact repository context: `code_worktree`, `worktree_group`,
`repository_id`, and `profile_reference` (the configured repository-relative
`certificationProfile` path or `None`). `QualityGatePlan` carries only `mode` (targeted/full)
and the optional `memory_cap_bytes`; there is no executor field anymore because the executor
identity comes from the profile.

`requires_strict_code_quality(target, *, code_would_commit)` returns False when nothing would
commit, otherwise it admits the profile via `load_repository_profile` (fail-closed on missing or
invalid authority) and returns True: code commits always need one valid configured profile.

`code_quality_gate_preview(target, *, code_would_commit, diff_base, plan)` reports one of three
states. In the enforced state it admits the profile/selection (`_admitted_selection`),
renders the profile-declared symbolic command (`_gate_command` / `_profile_report_command` via
`DaggerModuleExecutorAdapter`), and returns mode, `executor: "dagger"` (the framework-facing
label), `executorAdapterId`, `profileDigest`, `profileSelectionId`, and (full mode) the memory
policy block. `GATE_NO_CODE_COMMIT` reports no-code-commit; the old
`GATE_WRAPPER_UNAVAILABLE` state no longer exists.

`run_strict_code_quality_gate(target, *, diff_base, plan, invocation, attestation)` requires a
valid profile (else `certification-profile-invalid` before anything runs), hands the exact
candidate to `run_clean_quality` with the profile reference, writes the complete exported
transcript through `_write_test_results_report`, refuses a pass without a published manifest,
re-verifies the candidate write-tree before and after publication, and raises with both the stable
report path and a bounded output tail on any non-zero result. Success returns a payload validated
through `QualityGateResult` with `profileDigest`, `profilePlanDigest`,
`profileSelectionId`, `resultArtifact`, `reportPath`, `publishedResultPath`, and
certifying-test evidence. `_memory_policy_payload` reports `processPolicy:
profile-adapter-owned` and `swap: container-host-managed` with an explicit cap option for full
runs.

`recover_strict_code_quality_gate` loads the strict v3 published manifest once, checks the
caller-bound attestation and the declared result from that same immutable snapshot, recompiles the
expected profile plan digest for the current candidate, requires the manifest's profile identity
(profile/plan digest, selection, executor adapter, result decoder) to match the admitted
selection, decodes the terminal artifact through the declared decoder, and recovers one exact
passed generation after a caller crash. Its public `reportPath` remains the stable
`reports/test-results.md`; recovery additionally exposes `publishedResultPath`.

`run_local_quality_diagnostic` refuses immediately; there is no host command planner or
fallback executor. `test_results_report_path` fixes the report location at
`reports/test-results.md` under the supplied worktree group. `_write_test_results_report`
renders status, invocation, mode, executor adapter, profile digest, plan digest, selection, diff
base, exit code, timing, exact shell command, cap facts, and the full output, then publishes with
the shared `atomic_write_text` primitive. The command reported in the payload is the
profile-declared adapter command a reader can rerun exactly.

### The Index Is The Scope, And This Function Does Not Own It

The profile-declared adapter derives its scope from the index/working tree of the staged task
worktree — so **what is staged when this runs is what gets certified**. Since the staging commit
wave closeout stages the whole task worktree first (`closeout._gate_staged_code`), the gate's
scope and the commit's content are one set; before that, a file the task *created* went into the
commit with no rail of the gate having read it.

This module deliberately does not do the staging and does not describe it. The failure message
states only what is true of every caller — "code" — and **does not say the staging was undone,
because closeout does not undo it**. This function certifies the index it is handed and says
nothing about how it came to look that way. The refusals, the reset and the `add -A` all live in
`closeout.py`, where the disposable-worktree precondition that makes staging safe is actually
established.

### `diff_base` Is What Makes The Coverage Floor Passable

`diff_base` must be the task's recorded base commit. Leaf closeout passes
`contract.code_base_commit`; master integration passes the recorded super base. The lifecycle
executor materializes a separate ancestry bundle and the exact staged candidate, then the
profile-declared Dagger function refuses an empty or unprovable base.

Using the wrong base is the wrong measurement for a leaf: the profile's per-diff floor demands
full coverage of the changed statements and branch arcs, so measuring against `main` charges a
leaf for every change on the whole integration branch rather than for its own diff — a gate no
leaf can pass, which is exactly as useless as a gate that cannot fail. GitHub PR validation does
not invoke this acceptance path; the lifecycle always supplies the task-derived base.

`_gate_command` renders the profile-declared symbolic Dagger call into the payload's
`command` key, including exact-candidate and ancestry-bundle placeholders, mode, base, and
optional cap. `diffBase` reports the base on its own key.

### Host Execution Refuses

`run_local_quality_diagnostic` is an explicit refusal surface: the only executable path is
`run_clean_quality`, which reconstructs the accepted candidate inside the pinned Dagger graph
through the profile-declared adapter. This refusal is scoped to the Python quality/acceptance
wrapper; it does not overclaim that every direct diagnostic in the repository is forbidden.
Direct targeted Vitest unit/component diagnostics are governed by the dashboard configuration and
never enter this adapter.

### Conventions

`status` is the machine-readable field; `reason` is prose for a human reading the closeout
payload. Callers branch on `status`, not on `required` alone.

### Invariants And Boundaries

- The target carries the repository id and profile reference independently of the checkout path;
  authority is a configured repository settings value, never a discovered path.
- No-code closeout is skipped. Every code commit requires one valid configured profile; a missing,
  invalid, incomplete, or candidate-incoherent profile refuses as
  `certification-profile-invalid` before memory quality, approval claim, or commit.
- `requires_integrated_acceptance` and the consumer `wrapper-unavailable` state were removed at
  this commit; there is no no-adapter code-commit route and no repository-name special case.
- A required missing/invalid profile, an unavailable executor prerequisite, or a non-zero adapter
  result refuses before irreversible closeout or integration mutation.
- The leaf contract is the only sanctioned narrowing: targeted mode is explicit in the
  profile-declared command; full mode is explicit at master integration.
- **A closeout must pass the leaf's own base commit.** Dropping `diff_base` at a call site does
  not weaken the gate, it makes it unpassable.
- Failure output is bounded to the last 40 lines while preserving the actionable exit status.
- `reports/test-results.md` retains the complete stdout/stderr transcript for both pass and fail
  and is replaced atomically only after a run completes.
- **This module never stages, resets or restores.** The index it is handed is the scope it
  certifies; producing that index is the caller's job.
- This module never builds or launches a host wrapper command. `run_clean_quality` owns exact
  candidate reconstruction and profile-declared Dagger execution.
- `reportPath` always names the stable enclosure report. `publishedResultPath` is optional,
  recovery-only evidence and must never replace the stable path.
- Recovery loads one strict v3 manifest snapshot and uses it for attestation, profile identity,
  digest/size verification, and artifact-path resolution; no second pointer read or compatibility
  reader is permitted.

### Todos

None recorded.

## Docs References

The gate semantics are governed by CCR-R22@v1 and the master task.md framework/repository boundary:
the profile is configurable, the gate semantics are not; Gate 1-4 meanings and order are fixed
while the repository owns the concrete rails; Gate 5 remains memory-domain authority outside the
profile.

| Finding | Anchor | Source |
| --- | --- | --- |
| The profile is configurable; the gate semantics are not; repositories may not redefine the ordering contract. | `## Framework-Owned Classification Rules` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md |
| Missing, ambiguous, invalid, or incomplete profile authority fails during admission; no fallback or compatibility route. | `## Normative Requirement` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md |
| The MCP owns trusted host runtime-launch; every code-committing repository requires one explicit profile. | `## Framework and repository boundary` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/task.md |

## Repo-Internal References

Closeout owns sequencing, while the profile-declared adapter performs the actual repository-quality
checks; this module routes between them.

| Finding | Anchor | Source |
| --- | --- | --- |
| Target/plan shape and the strict-required decision that always admits one valid profile when code would commit. | `QualityGateTarget`; `QualityGatePlan`; `requires_strict_code_quality` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:48-65; mcp/src/agents_remember/worktrees/modules/quality/gate.py:66-69; mcp/src/agents_remember/worktrees/modules/quality/gate.py:126-134 |
| Preview reports the profile-admitted enforced state or no-code-commit; success payload carries profile identity and evidence. | `code_quality_gate_preview`; `_strict_quality_success_payload`; `_admitted_selection` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:136-191; mcp/src/agents_remember/worktrees/modules/quality/gate.py:396-442; mcp/src/agents_remember/worktrees/modules/quality/gate.py:520-537 |
| The strict run certifies the index it is handed, publishes the report, and refuses failures before any commit. | `run_strict_code_quality_gate`; `_write_test_results_report`; `_gate_failure_message` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:235-278; mcp/src/agents_remember/worktrees/modules/quality/gate.py:445-518; mcp/src/agents_remember/worktrees/modules/quality/gate.py:590-606 |
| Recovery reuses one exact passed generation only when profile identity and plan digest match the current candidate. | `recover_strict_code_quality_gate` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:279-343 |
| The named local entry point refuses before resolving or executing a host command. | `run_local_quality_diagnostic` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:443-444 |
| Closeout builds the target from the configured profile reference and runs targeted mode; integration forwards the reference for the full gate. | `_quality_gate_target`; `_closeout_quality_gate_preview`; `run_integration_quality_gate` | mcp/src/agents_remember/worktrees/modules/closeout.py:147-155; mcp/src/agents_remember/worktrees/modules/closeout.py:836-852; mcp/src/agents_remember/worktrees/integration/integration_quality.py:140-196 |
| The profile package provides admission/adapters/planning consumed here. | `load_repository_profile`; `DaggerModuleExecutorAdapter`; `compile_repository_profile_plan` | mcp/src/agents_remember/certification/repository_profiles/authority.py:42-92; mcp/src/agents_remember/certification/repository_profiles/adapters.py:60-97; mcp/src/agents_remember/certification/repository_profiles/planning.py:71-118 |
| Regressions cover enforced/no-code states, profile admission refusals, targeted/full modes, cap-kill naming, immediate host refusal, exact leaf base forwarding, bounded failures, and mutation ordering. | `CodeQualityGateTests`; `CloseoutCodeQualityGateTests` | mcp/tests/test_worktree_closeout_quality_gate.py:140-1088; mcp/tests/test_worktree_quality_gate_runner.py:183-536 |

## Cross-Repo References

This gate acts on whatever code worktree closeout hands it; for a consuming repository that
checkout carries that repository's own configured profile, and the profile-declared adapter is
that repository's own executable contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| Applicability is decided by the configured profile reference plus the admitted profile in the target checkout — no wrapper discovery, no repository-name special case. | `load_repository_profile`; `_admitted_selection` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:126-134; mcp/src/agents_remember/worktrees/modules/quality/gate.py:520-537 |

## L23 Acceptance Interpretation (Preserved)

This module owns only the pinned Dagger acceptance adapter. Leaf closeout runs targeted mode once;
leaf integration reuses that certified commit; master integration runs full mode once. Both
acceptance runs require the exact task-derived diff base. Host pytest and direct wrapper execution
are refused. The wording has evolved from the L23/R43 self-owned-wrapper era to the CCR-R22
profile-admission era captured above.

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): rewrote the card for the repository-profile cutover. `QualityGateTarget` gained `repository_id`/`profile_reference`, the plan lost its executor field, `requires_strict_code_quality` now always admits one valid profile for code commits, the `wrapper-unavailable` state and `requires_integrated_acceptance` were removed, preview/success payloads carry profile digest/plan digest/selection/executor adapter id/result artifact, and recovery re-derives the expected plan digest and profile identity before reuse.

- 2026-08-25T08:16+02:00 -- 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T21:23+02:00 -- 260824-PDLS made lifecycle quality consume only verified Dagger evidence.

- 2026-08-24T14:19+02:00 -- 260821-DAGQC-L2: made recovery single-snapshot and strict-manifest-owned, retained stable `reportPath`, and added optional immutable `publishedResultPath` without disturbing the concurrent L4 diagnostic-wording contract.

- 2026-08-24T13:51:26+02:00 -- 260821-DAGQC-L4: recorded the narrowed Python quality refusal wording. Direct targeted Vitest remains a separate diagnostic-only route; the adapter still has no host executor or acceptance fallback.

- 2026-08-22T10:39+02:00 -- 260821-CLIVE-L1 candidate-11 curation rebind: refreshed formatter-moved source coordinates against accepted tree `4241908c`; where applicable, replaced a deleted coordinator anchor with the sole current owner.

- 2026-08-17T12:30+02:00 -- 260815-DAG-L5: added `recover_strict_code_quality_gate` and attestation-bound Dagger report recovery for crash-safe full-gate reuse.

- 2026-08-14T12:13:26+02:00 -- R43 curator: reconciled self-owned-wrapper refusal wording and the new direct non-Dagger builder proof.

- 2026-08-14T11:24+02:00 -- R39 curator: replaced the obsolete checkout-only/name-forbidden applicability claim with the two-layer policy: consumer adapter opt-in plus mandatory Agents Remember self-wrapper presence. (The self-policy layer was subsequently removed by CCR-R22 at this commit.)

- 2026-08-14T09:37+02:00 -- Reopened L23 cadence: clarified this runner's two accepting owners -- targeted leaf closeout and full master integration -- and the leaf-integration no-rerun boundary.

- 2026-08-13T14:32+02:00 -- L23 final curator pass: re-read the reopened CONTRIBUTING claim and recorded that this host runner remains diagnostic/generic plumbing while Agents Remember acceptance is Dagger-only with explicit diff-base and no fallback.

- 2026-08-13T08:40+02:00 -- L23 integration-gate repair: documented the extracted strict plan validator and preserved the fail-closed no-fallback executor boundary.

- 2026-08-12T20:10+02:00 -- L23 curator: documented durable-report versus short-scratch ownership.

- 2026-08-12T15:19+02:00 -- L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges.

- 2026-08-12T07:10+02:00 -- 260731-EFA-L24 curator: recorded the host-managed full-gate default, explicit-cap-only wrapping, host swap, unchanged pytest `-n=auto`, and the `memoryPolicy` preview/result/report evidence.

- 2026-08-12T01:38+02:00 -- 260731-EFA-L22 citation maintenance: moved runner-policy proofs to `test_worktree_quality_gate_runner.py` and refreshed retained closeout ranges.

- 2026-08-11T22:28+02:00 -- 260731-EFA-L19 final curator pass: recorded deterministic UTF-8 replacement for captured quality output and non-Windows `/tmp` normalization for ephemeral quality scratch.

- 2026-08-11T17:50+02:00 -- 260731-EFA-L19 curator: recorded the enclosure-owned, atomically replaced `reports/test-results.md` contract, full pass/fail transcript retention, stable `reportPath`, explicit checkout+enclosure target, and interrupted-run preservation.

- 2026-08-08T17:18+02:00 -- 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired.

- 2026-08-08T02:00+02:00 -- 260731-EFA-L17 curator: recorded the altitude-routed plan (`QualityGatePlan` mode `targeted`/`full`, mandatory cap for full runs, `memoryCap` payload, cap-kill naming, invocation labels) and refreshed reference rows to post-L17 ranges.

- 2026-08-04T15:32:44+02:00 -- 260731-EFA-L6 S18-B08 curator: split wrapper applicability from preview reporting and regenerated both operative code-quality function extents.

- 2026-08-02T16:45:41+02:00 -- 260731-EFA-L6 curator W1-B10: repaired 20 manifest citation findings plus the residual cross-repo row; scoped recheck clean.

- 2026-08-01T09:44+02:00 -- 260731-EFA-L4 curator: recorded the staging-step reason wording and the index-as-scope docstring contract; repaired citations.

- 2026-07-31T21:20+02:00 -- 260731-EFA-L3 curator (second pass): recorded the `quality_environment` dependency on `git_environment()` and the no-selector handover.

- 2026-07-31T20:48+02:00 -- 260731-EFA-L3 curator: documented `diff_base` across deciders/payloads, the one git runner, and re-anchored citations.

- 2026-07-31T16:40+02:00 -- 260731-EFA-L2: corrected citation ranges after the whole-tree `ruff format` pass.

- 2026-07-31T16:10+02:00 -- 260731-EFA-L2 attestation: file touched only by the whole-tree `ruff format` pass (commit `00e8379`); sidecar re-read and deliberately not rewritten.

- 2026-07-31T04:28+02:00 -- 260731-EFA-L1 removed the repository-name hard-code (L1-R10); added the three status constants and the path-not-name boundary.

- 2026-07-24T14:31Z -- 260718-CHATS-L5I incremental curator: created the sidecar for mandatory pre-code-commit quality enforcement, linked-worktree interpreter selection, current-worktree import precedence, and fail-closed bounded error reporting.
