# mcp/src/agents_remember/worktrees/queue/closeout_projection_activation.py

## Governing Overview

[queue overview](overview.md)

## Purpose

This file is the read-only adapter from per-contract atomic-series activation authority into
disposable closeout projection source facts. It gives the queue waiting reasons without granting it
selector mutation or lifecycle ownership.

## Code Commentary

### Logic

`project_series_activation(contract)` strictly observes that one series contract's own activation
record — never a shared per-source-pair slot. A valid observation returns its source fact plus zero
or one waiting reason, and the only surviving reason is `atomic-series-reconciling`: vacant and
active are never waiting states, and another master's state is never this contract's reason to wait.
A derivation/read failure becomes a bounded `ProjectionSourceProblem` with the contract or activation
address and an explicit repair through a selecting manager/start/attach operation. It never chooses a
winner, because there is no winner to choose.

### Conventions

`SeriesActivationProjection` is a frozen local carrier for source fact, waiting tuple, and optional
problem. The record it reflects is addressed by `contract_fingerprint`, the digest of the resolved
contract path, so two sprint-commanded masters that share one protected source pair hold independent
records. That holds for a graph-less sprint too: the sprint declares no dependencies, so nothing
serializes its masters and each contract's own observation reaches `active` with an empty `waiting`
tuple — the `atomic-sequential` default is the sprint's shape, not a serialization mechanism. Repair
guidance names the selecting transaction rather than an internal store edit.

### Invariants And Boundaries

- The queue observes activation; it cannot publish, release, or archive it.
- Multiple live series are valid, including several for one protected source pair; vacant and active
  are normal, not another contract's waiting reason.
- A record that is not this exact contract is refused as unreadable
  (`atomic-series-activation-contract-mismatch`), so a foreign master can never be adopted here.
- Malformed authority fails loud as a source problem; no stale row or census-order fallback exists.
- No claim, commit, certification, integration, or terminal evidence is projected here.

### Todos

Repair wording and claims are reconciled to the per-contract selector observer; verification metadata
awaits the real code commit.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- Selector observation and waiting-reason derivation are owned outside the queue; the reader takes the contract and the reason is derived from the observation alone. [1]
- The queue route is a disposable rebuild projection with task truth and lifecycle state outside it. [2]
- Focused tests prove two masters sharing one protected source pair both project with no waiting reason, including the graph-less sprint where nothing serializes the masters. [3]

### Cross-Repo References

No cross-repository source is configured for this memory root.
