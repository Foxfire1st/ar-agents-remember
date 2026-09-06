# mcp/src/agents_remember/worktrees/integration/integration_quality.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_quality.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:55:31+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Runs altitude-aware acceptance for integration. An ordinary leaf lands its exact closeout-certified commit without another acceptance run; a branch-owning master or final organizational leaf selects the repository profile in full mode. The integration journal owns the original frozen run, terminal references, and completed organizational proof. Resumption reuses the selected certified prefix and executes only its uncertified code-gate suffix.

## Code Commentary

### Logic

`quality_gate_mode` returns full mode for branch-owning master integration and refuses a leaf. Preview and execution preserve the configured `profile_reference`, comparison base, memory-cap policy, and detached checkout of the exact integration commit. A leaf without an organizational completion plan returns the existing leaf-closeout certification description.

Execution builds an `IntegrationCertificationRequest` with the explicit operation owner, prepares or reopens its selected original run, and refuses an unchanged red catalog. `SelectedCodeCertification` carries terminal-selection, generation-retention and immediate start-authorization callbacks. Only the first uncertified G1–4 suffix runs; afterward the owner reopens selected terminals and renders the result from those original publications.

For organizational completion, a prior completed proof is revalidated against the current fingerprint, commit, tree and attestation. Otherwise `_certification` binds the selected frozen-run reference and terminal prefix, and `select_completed_integration` persists that exact proof through the operation owner. There is no report-directory search or caller-supplied certification sink. Execution errors retain the stable integration-quality failure vocabulary and cancel/repair handoff.

### Conventions

Repository profile authority chooses execution details. The framework-facing full-gate attestation keeps the `dagger` label; the lifecycle owner supplies journal authority explicitly.

### Invariants And Boundaries

- A final organizational leaf and an atomic series both use the detached exact-commit checkout.
- Organizational certification and publication evidence is persisted for crash-safe reuse in the
  integration journal; queue projection may schedule the door candidate but does not own repair.
- A reused certification must match the current completion fingerprint, code commit, candidate tree, Dagger plan, and exact journal-selected original references.
- A red original catalog requires a corrected candidate and successor operation; missing certificates do not become success.
- Original terminal publications and interrupted history remain protected while selected; selection and start callbacks recheck the live operation owner.
- Every code-committing master integration resolves one valid repository profile through the forwarded `profile_reference`; missing/invalid authority or an unavailable executor prerequisite fails closed before any commit.

### Todos

This card records source behavior only. Leaf acceptance and later production memory/finalization composition require their own evidence.

## Repo-Internal References

The orchestration module delegates selection and readback to the integration certification owner. These references distinguish retained original authority from a reconstructed result payload.

| Finding | Anchor | Source |
| --- | --- | --- |
| Branch-owning integration uses full mode; ordinary leaf integration reuses closeout. | `quality_gate_mode`; `_leaf_closeout_certification` | mcp/src/agents_remember/worktrees/integration/integration_quality.py:98-103; mcp/src/agents_remember/worktrees/integration/integration_quality.py:230-240 |
| Preview preserves exact checkout, profile, comparison base and completion identity. | `quality_gate_preview` | mcp/src/agents_remember/worktrees/integration/integration_quality.py:106-135 |
| The public gate requires an explicit owner and preserves stable failure classification. | `run_integration_quality_gate` | mcp/src/agents_remember/worktrees/integration/integration_quality.py:138-163 |
| Selected originals control suffix execution, publication retention and result rendering. | `_execute_integration_gate` | mcp/src/agents_remember/worktrees/integration/integration_quality.py:166-227 |
| The exact final-leaf failure retains its cancel/repair handoff. | `organizational_quality_failure_payload` | mcp/src/agents_remember/worktrees/integration/integration_quality.py:251-306 |
| Completed proof binds selected references and current attestation. | `_certification`; `_quality_attestation`; `_require_matching_certification` | mcp/src/agents_remember/worktrees/integration/integration_quality.py:309-326; mcp/src/agents_remember/worktrees/integration/integration_quality.py:329-343; mcp/src/agents_remember/worktrees/integration/integration_quality.py:346-378 |
| The integration owner selects once, verifies original publications and refuses unchanged red evidence. | `prepare_integration_certification`; `_load`; `require_resumable_integration` | mcp/src/agents_remember/worktrees/integration/certification.py:192-216; mcp/src/agents_remember/worktrees/integration/certification.py:235-296; mcp/src/agents_remember/worktrees/integration/certification.py:343-349 |
| Terminal and completion writes use the selected journal owner. | `select_integration_terminals`; `select_completed_integration` | mcp/src/agents_remember/worktrees/integration/certification.py:352-364; mcp/src/agents_remember/worktrees/integration/certification.py:367-441 |

## Docs References

No external Domain Documentation source is configured for this repository-owned integration boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source governs these integration-local claims. | N/A | N/A |

## Cross-Repo References

Code and external-memory integration authority is passed through the canonical worktree contract. This module establishes no independent cross-repository protocol.

| Finding | Anchor | Source |
| --- | --- | --- |
| The implementation evidence is owned by the same repository and cited above. | N/A | N/A |

## 260821-CLIVE-L2 Current Contract

The current source seams include `IntegrationQualityFailure`, `integration_quality_failure`, `IntegrationQualityOutcome`. Organizational quality and completion evidence is persisted in the canonical integration journal and repaired through journal-owned transitions. The earlier description of a queue-owned quality transaction is obsolete.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes failure, projection, and outcome types at this ownership boundary. | `IntegrationQualityFailure`; `integration_quality_failure`; `IntegrationQualityOutcome` | mcp/src/agents_remember/worktrees/integration/integration_quality.py:55-74; mcp/src/agents_remember/worktrees/integration/integration_quality.py:77-89; mcp/src/agents_remember/worktrees/integration/integration_quality.py:93-95 |

## 260821-CLIVE No Local Behavior Delta

The CLIVE diff updates documentation terminology from a queue-owned organizational transaction to
the journal-owned transaction. Quality execution behavior is unchanged in this file; no new gate,
fallback, or authority seam was introduced.

## 260824-PDLS — Integration Accepts Certifying Evidence Only

Organizational integration quality requires the Dagger result's typed certifying evidence for the
integration consumer. Diagnostic evidence has no path into reusable organizational certification
or protected-ref integration.


## PDLS Reconciliation

Certification matching now reports the exact observed-versus-expected identity mismatch while preserving Dagger as the sole integration-quality authority.

This change preserves the file's existing authority boundary. No threshold exception, silent
fallback, or compatibility reader was added.
## Update History

- 2026-09-06T14:55:31+00:00 — Completed source verification against actual commit c69d5171187fa1957025e393270db9f5a864ab14 after rechecking equality with the independently reviewed candidate source. Preserved the curated body, all citations and earlier history; certification remains pending.

- 2026-09-06T13:51:59+00:00 — L33 candidate curation: Replaced obsolete report-recovery/sink descriptions with operation-selected original readback and suffix execution; retained exact-commit full-profile policy and repair handoff. Reviewed uncommitted source; prior verification commit/date remain unchanged. This is source documentation, not gate or acceptance evidence.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the profile-bound full gate -- `profile_reference` forwarding through preview/run/integrate, `QualityGateTarget` construction, removal of the settings executor field and `requires_integrated_acceptance`, and `CertificationContractError` surfacing as integration-quality failure.


- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T21:23+02:00 — 260824-PDLS applied the evidence-altitude firewall at integration.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: verified the local diff as documentation-only and corrected the transaction owner. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/integration_quality.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for altitude-aware integration acceptance.
