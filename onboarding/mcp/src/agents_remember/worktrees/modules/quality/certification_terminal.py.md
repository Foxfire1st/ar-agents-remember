# mcp/src/agents_remember/worktrees/modules/quality/certification_terminal.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/certification_terminal.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:15:01+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Governing route overview](../overview.md)

## Purpose

Defines typed terminal publication outputs and translates exact executor rail catalogs into domain-owned rail results without inventing missing outcomes.

## Code Commentary

### Logic

`RecordedGateTerminal` binds a result and exact reference to its original publication, with an optional certificate/reference. `RecordedCertificationGeneration` exposes those typed terminals separately from its presentation records; `as_payload` groups certificate, terminal and refused rows. `GateRecordPublication` is the mutable in-flight certificate/terminal accumulator for one publication.

`catalog_gates` requires a list of one to five object rows with unique integer gate values, rejecting booleans. It preserves their supplied order; legal gate membership, prefix and disposition checks belong to the downstream plan/recording owners.

`terminal_results` requires the exact number and identity set of planned rails. It accepts only pass, fail, blocked or not-applicable outcomes, validates nested artifact/evidence shapes and delegates each observation to `build_rail_result`. Unknown, missing, duplicate or incomplete rail populations refuse. A supplied nonempty failure code is retained; otherwise the code is the deterministic rail-id/status label.

Blocked references resolve only to planned same-gate rails; missing/non-list evidence and artifact fields become empty lists before domain validation. Those conversions do not fabricate required evidence or make an invalid result certifiable.

### Conventions

Keep record rendering distinct from domain validity and selected authority. A `refused_record` has no certificate or manifest; its presentation disposition is not a green certification claim.

### Invariants And Boundaries

- The rail plan, not the decoder’s observed subset, fixes the terminal population.
- Typed dataclass construction alone does not validate physical reports or select a journal state.
- A terminal may retain a red or interrupted result without a reusable certificate.
- This file does not discover original publications, publish store objects or start gates.

### Todos

None recorded for this file's bounded responsibility.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolved registry supplies no applicable external Domain Documentation source for this card. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| A terminal binds exact original references; generation rendering stays separate. | `RecordedGateTerminal` | mcp/src/agents_remember/worktrees/modules/quality/certification_terminal.py:27-34 |
| Typed selection inputs and presentation grouping have distinct fields. | `RecordedCertificationGeneration` | mcp/src/agents_remember/worktrees/modules/quality/certification_terminal.py:38-51 |
| Gate catalog parsing bounds rows and rejects malformed or duplicate integer identities. | `catalog_gates` | mcp/src/agents_remember/worktrees/modules/quality/certification_terminal.py:81-109 |
| Rail observations must equal the exact planned identity population. | `terminal_results` | mcp/src/agents_remember/worktrees/modules/quality/certification_terminal.py:112-167 |
| Codes preserve supplied failures or derive a deterministic status label. | `_terminal_code` | mcp/src/agents_remember/worktrees/modules/quality/certification_terminal.py:170-176 |
| Blockers resolve only against the planned same-gate rails. | `_terminal_blocked_by` | mcp/src/agents_remember/worktrees/modules/quality/certification_terminal.py:179-189 |
| Refused records carry no certificate or result-manifest authority. | `refused_record` | mcp/src/agents_remember/worktrees/modules/quality/certification_terminal.py:67-78 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |

## Update History

- 2026-09-06T15:15:01+00:00 — Created from the complete source at `c69d5171187fa1957025e393270db9f5a864ab14`. Documented the selected-original, terminal or transport responsibility and its actual neighboring owners. Source verification is not execution or acceptance evidence.
