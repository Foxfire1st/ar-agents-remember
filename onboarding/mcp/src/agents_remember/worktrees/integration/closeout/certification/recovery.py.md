# mcp/src/agents_remember/worktrees/integration/closeout/certification/recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/certification/recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:58:25+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Selected closeout certification overview](overview.md)

## Purpose

Derives recovery input changes from retained owner records and validates the exact prior-red admission context before execution.

## Code Commentary

### Logic

`derive_certificate_input_changes` recompiles each supplied frozen run/candidate observation and requires the same task, contract, repository and source ref. It compares actual candidate code trees and each admitted gate's semantic-input identities. Runtime/toolchain/executor changes carry their exact consuming gates; other per-gate input changes retain the gate-specific class.

When both memory observations are supplied, the comparison separates memory tree/closure/checker/pair changes from changed coherence subrecords. One-sided memory absence refuses. Topology or normative-intent changes are separate from journal, approval, commit-intent and provenance changes; the latter do not invent a code-gate input change. No relevant change yields an `unchanged-interruption` classification, whose reuse still depends on selected certificates and current memory authority.

`build_prior_red_context` requires the exact preceding certificate prefix, a complete certifying red catalog and unique caller-supplied dispositions. It reconstructs the catalog in the original run and invokes lifecycle admission for the current run. Missing, diagnostic, mismatched or incomplete authority refuses with zero gate starts.

### Conventions

This helper classifies supplied owner records; it neither scans for predecessors nor writes publications, journal selections or repair rationales. Change ordering is canonical by content digest.

### Invariants And Boundaries

- Construction of a claimed change class cannot replace actual before/after owner inputs.
- Both memory inputs may be absent before the memory port runs; that absence does not certify reuse of an existing Gate 5.
- Prior failed/blocked rails need the real catalog and explicit corrective dispositions; diagnostics cannot clear them.
- Gate results are rebuilt against the original registry, plan and candidate, preserving full catalog completeness.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry has no entries. The source below establishes this repository-owned boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolved registry supplies no applicable external Domain Documentation source for this card. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Recovery snapshots carry the actual frozen run, candidate and optional memory observation. | `RecoveryInputSnapshot` | mcp/src/agents_remember/worktrees/integration/closeout/certification/recovery.py:42-47 |
| Change classification first validates both admissions and the exact task address. | `derive_certificate_input_changes`; `_require_snapshot`; `_require_same_task` | mcp/src/agents_remember/worktrees/integration/closeout/certification/recovery.py:50-79; mcp/src/agents_remember/worktrees/integration/closeout/certification/recovery.py:138-147; mcp/src/agents_remember/worktrees/integration/closeout/certification/recovery.py:150-155 |
| Gate/runtime and memory/coherence changes derive from actual admitted inputs. | `_gate_changes`; `_memory_changes` | mcp/src/agents_remember/worktrees/integration/closeout/certification/recovery.py:158-192; mcp/src/agents_remember/worktrees/integration/closeout/certification/recovery.py:195-230 |
| Topology/intent and journal/approval/provenance changes remain distinct. | `_candidate_changes` | mcp/src/agents_remember/worktrees/integration/closeout/certification/recovery.py:233-261 |
| Prior-red context requires a complete original catalog, prefix and corrective admission. | `build_prior_red_context`; `_require_complete_red_catalog` | mcp/src/agents_remember/worktrees/integration/closeout/certification/recovery.py:82-124; mcp/src/agents_remember/worktrees/integration/closeout/certification/recovery.py:264-284 |

## Cross-Repo References

No cross-repository implementation or external protocol is owned here.


| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |
## Update History

- 2026-09-06T14:58:25+00:00 — Created after full source review at `c69d5171187fa1957025e393270db9f5a864ab14`. Records current implementation and remaining composition boundaries; source verification is not gate execution, delivery or acceptance.
