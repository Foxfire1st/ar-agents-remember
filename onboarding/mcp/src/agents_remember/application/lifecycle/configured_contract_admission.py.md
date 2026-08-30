# mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T05:55+02:00 |
| lastVerifiedCommitHash | `346507af24396ab7b491e02511c4af006ccd3dc5` |
| lastVerifiedCommitDate | 2026-08-30T07:51:57+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing route overview](../overview.md)

## Purpose

Closed admission for every public current-contract mutation route.

## Code Commentary

### Logic

The public surface is `ConfiguredContractAccepted`, `ConfiguredContractRefused`, `admit_configured_contract`, `configured_authority_refusal`, `configured_contract_reread_refusal`, `execute_configured_contract_operation`. This application boundary exposes a closed public result and delegates durable mutation to its owning domain seam. Expected configured-contract, location, or legacy failures are translated through typed decisions; callers do not enumerate lower-level exception families or invent alternate authority. Admission is strict by default, including current candidate-worktree identity. An exact-pair consumer may explicitly set `require_candidate_identity=False` only because the shared code-memory pair validator owns that same live-candidate check; configured repository roots, separation, task identity, and enclosure confinement remain admitted here.

### Conventions

The file exposes typed values or one narrow operation boundary. Callers consume those values directly rather than reconstructing lower-level state from strings, mutable task documents, or queue projection.

### Invariants And Boundaries

- Preserve the module's single ownership seam; do not add a fallback reader or duplicate authority.
- Disabling the admission layer's candidate-identity check is valid only for an exact-pair consumer
  that immediately delegates the same obligation to the canonical pair validator.
- Expected refusal states remain typed and bounded, while unexpected programming faults remain loud.
- Durable lifecycle facts live in the canonical root journal; scheduling projections may only consume them.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file itself is the current evidence for this file-specific contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `ConfiguredContractAccepted`; `ConfiguredContractRefused`; `admit_configured_contract` as its public seam. | `ConfiguredContractAccepted`; `ConfiguredContractRefused`; `admit_configured_contract` | mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py:58-64; mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py:77-87; mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py:96-169 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Final Terminal Admission Route

`admit_configured_terminal_contract` keeps live mutation admission strict, but recognizes one
state-disjoint terminal route when the exact locator is `terminal-archived`. That route requires
readable surviving contract truth, the exact external archive and receipt, and configured
repository identity for the archived contract without requiring worktrees cleanup already removed.
Present-invalid archive or authority evidence becomes a bounded refusal. Terminal admission is
only for status and exact cleanup retry; it is never a generic fallback for live mutations.

## Update History

- 2026-08-30T05:55+02:00 — MCAR-L03 A005: exposed the strict-by-default candidate-identity
  choice to exact-pair consumers. Relaxed callers still pass the same closed configured admission
  and retain repository, task, and enclosure authority; only the shared pair API owns candidate
  liveness and field-specific refusal.

- 2026-08-29T17:23+02:00 — No content impact: reviewed the Python 3.13 local type-parameter migration for the configured-operation result and confirmed that the documented admission, refusal, and reread boundary is unchanged. Verification remains closeout-owned.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: merged the final live-versus-terminal admission contract into the current DAGQC card. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
