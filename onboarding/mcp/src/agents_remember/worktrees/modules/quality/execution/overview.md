# Selected Code Execution And Retained Reports

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/modules/quality/execution/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-06T15:15:01+00:00 |
| lastVerifiedCommitHash | `602143bd1d48226f4d53b83ff7c5002a695dcdff` |
| lastVerifiedCommitDate | 2026-09-09T00:26:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[Worktree modules overview](../../overview.md)

## What This Area Is

The code-executor boundary for an explicit selected certification suffix and its original report bytes. It validates the frozen R21 decision, prepares fresh or selected profile admission, and writes the candidate sandbox manifest. The surrounding lifecycle journal supplies selected authority; the clean executor owns the sandbox, Dagger runtime and cleanup.

## Hot Path Summary

Start with `models.py` for the code-only launch contract, `retained_reports.py` for original byte transport, and `sandbox.py` for candidate/profile/source-selection composition. The package marker has no initialization behavior.

## Operating Model

1. Validate canonical frozen objects and recompute the selected R21 reuse plan. Only a first gate of 1–4 enters code execution; Gate-5-only and finalization-only decisions stay outside this transport.
2. Match retained original certificates to the exact reused prefix, then bind each result to its publication authority.
3. Resolve fresh profile authority or retain the selected frozen profile/plan. Observe the actual comparison source selection in the prepared Git sandbox and require the frozen decision to match.
4. Derive retained report membership and byte limits from the frozen producer declarations and original result members. Resolve every original path, then copy bounded verified bytes into the fresh transport directory.
5. Atomically write the admission manifest with source, profile, execution and runtime bindings. Starting commands and selecting returned terminals remain explicit neighboring owner responsibilities.

## Local Invariants And Traps

- A transport DTO or manifest does not confer lifecycle journal authority or prove that a gate ran.
- No current-pointer or history search supplies a missing predecessor.
- Original publication provenance remains distinct from semantic certificate/reuse identity.
- Physical retained reports are bounded by their actual frozen declarations, with a 4,096-file population ceiling.
- Source-selection movement refuses before the manifest can represent a different candidate.
- This route does not implement Gate 5 or the production finalization continuation.

## File-Level Onboarding Map

| Source File | Onboarding | Role |
| --- | --- | --- |
| `__init__.py` | [__init__.py.md](__init__.py.md) | Documentation-only package marker |
| `models.py` | [models.py.md](models.py.md) | Exact selected code suffix and original prefix validation |
| `retained_reports.py` | [retained_reports.py.md](retained_reports.py.md) | Frozen producer bounds and confined original byte copies |
| `sandbox.py` | [sandbox.py.md](sandbox.py.md) | Fresh/selected profile and candidate admission manifest |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The code boundary recomputes reuse and rejects zero-code-start decisions. | `CodeCertificationExecution` | mcp/src/agents_remember/worktrees/modules/quality/execution/models.py:42-100 |
| Original result membership and frozen declarations jointly bound retained files. | `retained_report_inventory` | mcp/src/agents_remember/worktrees/modules/quality/execution/retained_reports.py:37-77 |
| Snapshotting reopens the original publication before exclusive copies. | `snapshot_retained_reports` | mcp/src/agents_remember/worktrees/modules/quality/execution/retained_reports.py:80-109 |
| Selected admission preserves frozen semantic profile authority. | `_selected_profile` | mcp/src/agents_remember/worktrees/modules/quality/execution/sandbox.py:69-118 |
| Manifest composition reobserves actual source selection. | `_write_sandbox_manifest` | mcp/src/agents_remember/worktrees/modules/quality/execution/sandbox.py:121-169 |
| The surrounding gate receives explicit owner selection/start/retention callbacks. | `SelectedCodeCertification` | mcp/src/agents_remember/worktrees/modules/quality/certification_run.py:38-44 |

## Docs And Cross-Repo References

The configured Domain Documentation registry supplies no applicable source. The adjacent quality, certification-domain and lifecycle journal owners provide the same-repository boundaries; no external protocol is defined here.

## Update History

- 2026-09-09T02:35:47+02:00 — CCR-L38 inherited route reconciliation: re-read this route's purpose, member inventory, route summary, and invariants against frozen candidate code tree `4c6b7bc2362bc03d50fc7a0643f34b591b805d45`; the candidate's changed paths are outside source route `mcp/src/agents_remember/worktrees/modules/quality/execution`, so no route/member/prose/invariant change is required. route-member-count=4; source inspection only; verification metadata remains unchanged pending producer-owned realization. No acceptance or certification claim.

- 2026-09-06T15:15:01+00:00 — Created the nearest execution route from all four source files at `c69d5171187fa1957025e393270db9f5a864ab14`. Linked the exact suffix, original report transport and sandbox admission owners. Source verification is not execution or acceptance evidence.
