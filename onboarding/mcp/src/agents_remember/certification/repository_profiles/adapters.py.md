# mcp/src/agents_remember/certification/repository_profiles/adapters.py

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
bundle, the execution (admission) manifest, mode, export root, optional retained reports and an optional memory
cap. `DecodedExecutorResult` is the typed terminal (status, exit code, artifact path).

`DaggerModuleExecutorAdapter.command` builds `<executable> --progress=plain call
<function> --source=... --bundle=... --manifest=... [--retained-reports=...] [--memory-cap-bytes=...]
<reports-field> export --path=<export-root>`. It appends declared retained-report transport and memory cap only when
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

### Current source-selection contract

The execution request carries optional retained_reports instead of a diff-base transport. The Dagger adapter forwards that directory only when the admitted definition declares retainedReportsArgument; otherwise it refuses. Candidate source, ancestry bundle, manifest, memory cap and export remain explicit inputs.

- `RepositoryExecutionRequest` carries the current contract described above. [1]
- `DaggerModuleExecutorAdapter` carries the current contract described above. [2]

## Evidence

### Docs References

CCR-R22@v1 states raw commands may be repository-owned configuration because the repository
already owns executable code, but the MCP must execute only the exact admitted bytes through the
declared sandbox adapter; configuration cannot inject host execution outside the admitted
executor boundary. The expected implementation evidence requires generic executor-adapter and
artifact/result-decoder interfaces with no repository-specific imports or report names in the
framework layer.

CCR-R22@v1 (requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md,
"## Required Profile Contract") states raw commands may be repository-owned configuration,
but the MCP executes only the exact admitted bytes through the declared sandbox adapter; the
expected implementation evidence ("## Expected Implementation Evidence") requires generic
executor-adapter and artifact/result-decoder interfaces with no repository-specific imports
or report names in the framework layer. The master task boundary (task.md,
"## Framework and repository boundary") assigns fixed gate meanings, order, and typed
schemas to the MCP while each repository owns commands or adapters and result decoders.


### Repo-Internal References

`gate.py` uses `DaggerModuleExecutorAdapter` to render the reported preview command and the
strict-succeed payload, and uses `JsonExitStatusDecoder` during recovery. `clean_executor.py`
runs the admitted adapter against the exact staged candidate and decodes the exported terminal
artifact. The old hardcoded result inventory it replaces was deleted in
`worktrees/modules/quality/result_artifacts.py` (removed in this same commit).

- The generic executor/decoder protocol and the concrete Dagger + JSON implementations. [3]
- The profile report command selects the admitted executor and renders it through DaggerModuleExecutorAdapter. [4]
- The success payload uses the shared gate-command renderer and reports the admitted profile identity. [5]
- The clean executor runs the admitted adapter against the exact candidate. [6]
- The clean executor publishes the exported execution outcome. [7]
- The configured result decoder determines the exported pipeline exit status. [8]
- Render an exact journal selection after full original-object and artifact readback. [9]
