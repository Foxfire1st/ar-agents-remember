# mcp/src/agents_remember/certification/repository_profiles/adapters.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/repository_profiles/adapters.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification overview](../overview.md)

## Purpose

Repository-neutral executor and terminal-result decoder interfaces. This module defines the two
generic contracts the framework calls with: a `RepositoryExecutorAdapter` that turns one
declared `DaggerModuleExecutorDefinition` plus an execution request into an exact command line,
and a `RepositoryResultDecoder` that turns one declared `JsonExitStatusDecoderDefinition`
plus the exported artifacts into a typed terminal result. There is no repository-specific import,
test-runner name, or report inventory anywhere in this file: the framework executes only the
exact admitted profile bytes through these adapters, implementing CCR-R22's rule that raw
commands may be repository-owned configuration but the MCP executes only the exact admitted
bytes through the declared sandbox adapter.

Before this commit the equivalent logic was the fixed Agents Remember wrapper path
(`mcp/test_support/agents_remember_test_support/code_quality/check.py`) and a repository-name policy in `gate.py`, and
`result_artifacts.py` hardcoded `clean-quality-results.json` field names
(`completedSteps`, `ambientRoleChatEvidence`). `adapters.py` replaces both: the decoder is a
declared, profile-owned configuration and the artifact-reference rules are generic.

## Code Commentary

`RepositoryExecutionRequest` carries the exact candidate source checkout, the git ancestry
bundle, the execution (admission) manifest, mode, diff base, export root, and an optional memory
cap. `DecodedExecutorResult` is the typed terminal (status, exit code, artifact path).

`DaggerModuleExecutorAdapter.command` builds `<executable> --progress=plain call
<function> --source=... --bundle=... --manifest=... [--diff-base=...] [--memory-cap-bytes=...]
<reports-field> export --path=<export-root>`. It appends the diff base and memory cap only when
present, refuses a negative cap, and never substitutes a host command for the declared Dagger
graph.

`JsonExitStatusDecoder.decode` reads the declared decoder artifact confined to the export root
(`_confined_regular_artifact` refuses exports outside the root and symlink/non-regular paths),
parses JSON, validates artifact references and reference activations, and requires the status
field to equal `passedValue` on exit code 0 or `failedValue` otherwise. A contradictory or
invalid result raises `RuntimeError`; a boolean or negative exit code refuses.

`_validate_artifact_references` / `_reference_values` enforce that every artifact referenced
by declared `artifactReferences` rules is present in the exported inventory and is a safe
relative repository file path. `_validate_reference_activation` binds `referenceActivations`
rules: when the selector list contains `containsValue`, every referenced field must be present;
when inactive, none may be claimed. `_json_field` does confined nested field traversal with
`null_parent_as_missing` support for `ignore-reference`/`ignore-activation` policies.

## Invariants And Boundaries

- The framework never names a repository command or report: every string in the command comes
  from the admitted profile definitions; the export inventory bounds what may be consumed.
- Only the declared executor adapter executes; host execution is not planned here
  (`run_local_quality_diagnostic` refuses in `gate.py`).
- The decoder reads exactly one declared artifact, confined to the export root, with reference
  and activation validation; no legacy `clean-quality-results.json` field convention survives.
- A missing/irregular artifact, invalid reference, or contradictory terminal result is a hard
  `RuntimeError`; there is no fallback result and no silent skip.

## Docs References

CCR-R22@v1 states raw commands may be repository-owned configuration because the repository
already owns executable code, but the MCP must execute only the exact admitted bytes through the
declared sandbox adapter; configuration cannot inject host execution outside the admitted
executor boundary. The expected implementation evidence requires generic executor-adapter and
artifact/result-decoder interfaces with no repository-specific imports or report names in the
framework layer.

| Finding | Anchor | Source |
| --- | --- | --- |
| Raw commands may be repository-owned configuration, but the MCP executes only the exact admitted bytes through the declared sandbox adapter. | `## Required Profile Contract` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md |
| Expected implementation evidence: generic executor-adapter and artifact/result-decoder interfaces with no repository-specific imports or report names in the framework layer. | `## Expected Implementation Evidence` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md |
| The MCP owns fixed gate meanings, order, and typed schemas; each repository owns commands or adapters and result decoders. | `## Framework and repository boundary` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/task.md |

## Repo-Internal References

`gate.py` uses `DaggerModuleExecutorAdapter` to render the reported preview command and the
strict-succeed payload, and uses `JsonExitStatusDecoder` during recovery. `clean_executor.py`
runs the admitted adapter against the exact staged candidate and decodes the exported terminal
artifact. The old hardcoded result inventory it replaces was deleted in
`worktrees/modules/quality/result_artifacts.py` (removed in this same commit).

| Finding | Anchor | Source |
| --- | --- | --- |
| The generic executor/decoder protocol and the concrete Dagger + JSON implementations. | `RepositoryExecutorAdapter`; `RepositoryResultDecoder`; `DaggerModuleExecutorAdapter`; `JsonExitStatusDecoder` | mcp/src/agents_remember/certification/repository_profiles/adapters.py:43-58; mcp/src/agents_remember/certification/repository_profiles/adapters.py:60-97; mcp/src/agents_remember/certification/repository_profiles/adapters.py:99-133 |
| The preview and success payload render the profile-declared command through the same adapter. | `_profile_report_command`; `_strict_quality_success_payload` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:539-557; mcp/src/agents_remember/worktrees/modules/quality/gate.py:396-442 |
| The clean executor runs the admitted adapter against the exact candidate and decodes the exported result; recovery decodes through the same decoder. | `run_clean_quality`; `_executor_command`; `recover_strict_code_quality_gate` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:90-144; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:178-196; mcp/src/agents_remember/worktrees/modules/quality/gate.py:279-343 |
| The generic decoder replaces the deleted hardcoded result-inventory validations. | (deleted) `validate_result_artifact_references` | mcp/src/agents_remember/worktrees/modules/quality/result_artifacts.py (removed at this commit) |

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new repository-neutral executor/decoder interface module of the repository-owned certification profile package.
