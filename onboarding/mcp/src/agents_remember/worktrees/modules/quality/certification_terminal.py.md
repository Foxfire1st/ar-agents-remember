# mcp/src/agents_remember/worktrees/modules/quality/certification_terminal.py

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

## Evidence

### Docs References

The resolved registry supplies no applicable external Domain Documentation source for this card.

### Repo-Internal References

- A terminal binds exact original references; generation rendering stays separate. [1]
- Typed selection inputs and presentation grouping have distinct fields. [2]
- Gate catalog parsing bounds rows and rejects malformed or duplicate integer identities. [3]
- Rail observations must equal the exact planned identity population. [4]
- Codes preserve supplied failures or derive a deterministic status label. [5]
- Blockers resolve only against the planned same-gate rails. [6]
- Refused records carry no certificate or result-manifest authority. [7]

### Cross-Repo References

No separately configured cross-repository source is used for this card.
