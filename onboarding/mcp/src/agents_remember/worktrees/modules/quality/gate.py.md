# mcp/src/agents_remember/worktrees/modules/quality/gate.py

## Governing Overview

[Governing route overview](../overview.md)

## Purpose

Owns repository-profile admission and the lifecycle-facing quality gate boundary. It runs or recovers the exact candidate's Dagger generation, publishes the durable test report, and invokes the certification-record adapter around the run.

## Code Commentary

### Logic

`QualityGateTarget` binds checkout, enclosure, repository id and configured profile reference; `QualityGatePlan` carries targeted/full mode, an optional memory cap and optional exact selected certification. A code commit requires one admitted profile. Missing profile authority refuses instead of providing the former wrapper-unavailable opt-out.

`run_strict_code_quality_gate` captures the staged tree, freezes certification admission before `run_clean_quality`, writes the completed test report, rejects failed or uncertified output, then rechecks both the evidence tree and current staged tree. The index is supplied by the caller: this module neither stages nor undoes staging. The recorded task diff base determines the measured change set.

`render_selected_code_certification` reopens the selected frozen run, requires its candidate tree and repository to match the current target, validates the selected original terminal publications, and requires certifying evidence before rendering success. It does not synthesize a replacement execution. The public report and immutable published evidence retain separate paths.

The record helper reopens the published decoder artifact and delegates its gate catalog. A nonempty returned refusal list now raises before the caller returns quality success, including exact-generation recovery. Every available published manifest is recorded, and selected callbacks retain its actual terminals before nonzero execution failure is raised. A zero exit without a manifest refuses. The recorded generation must satisfy its complete evidence contract before success.

### Conventions

Only the pinned Dagger path supplies acceptance evidence. A symbolic command in a preview is not execution evidence. Preserve the profile and shared runtime-authority digests in reports and recovered payloads.

### Invariants And Boundaries

- Freeze admission before Gate 1; never manufacture authority after execution from unbound inputs.
- Candidate, profile, selection, decoder and attestation must match during recovery.
- A green quality result and a complete certificate chain are separate facts at this boundary.
- Host diagnostic execution refuses; a failed gate leaves caller-owned staging intact.
- An explicit memory cap changes resource policy, not the test population or evidence requirements.

### Todos

No red/interrupted-record integration remains pending at this seam. Gate-5 memory execution remains owned by the separate lifecycle continuation; this code runner does not manufacture it.

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

External domain documentation is not configured.

### Repo-Internal References

- Required profile authority governs execution and preview. [1]
- Admission precedes Dagger and the exact staged tree is rechecked. [2]
- Recovery reads the selected frozen run and original terminal publications, checks exact current candidate identity, and requires certifying evidence. [3]
- Successful certification renders the exact evidence and manifest into the typed quality result. [4]
- Host diagnostic entry refuses certification execution through this owner. [5]
- Persist complete actual terminal catalogs, including red and interrupted gates. [6]

### Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

No cross-repository evidence is required for these file-local claims.
