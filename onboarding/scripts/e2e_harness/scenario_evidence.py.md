# scenario_evidence.py

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Builds bounded canonical-routing, tool-discovery, tmux, control, catalog, inbox, and Codex evidence
for success checkpoints and failure diagnosis.

## Code Commentary

### Logic

Canonical-message helpers project only address/delivery fields. `DiscoveryEvidence` reduces observed
tool calls to routes, one discovered dispatch identity, one canonical schema digest, two passed
negative sentinels, and a positively decoded `ok: true` result for every required ambient/hosted
dispatch. String results accept direct JSON or the exact current Codex execution envelope
(`Wall time: <number> seconds`, then `Output:`); arbitrary prefixes and malformed payloads remain
non-evidence instead of being searched heuristically for a favorable `ok` value.
Failure evidence snapshots every hosted seat with bounded pane/log/control data so a failed process
boundary names what diverged without requiring a rerun.

### Conventions

Acceptance evidence and diagnostics are distinct: only `recorder.check` can close a checkpoint.
Environment evidence records presence for the API key rather than its value.

### Invariants And Boundaries

- A canonical manager message contains task document plus role and no private ids.
- The ambient and hosted chain must converge on one normally advertised `dispatch_agent` identity.
- Every required dispatch route must return a recursively decoded positive public result; a merely
  completed model turn is insufficient.
- The current Codex execution envelope is normalized at one strict boundary; malformed or unknown
  wrappers fail the checkpoint rather than becoming a compatibility search path.
- Pane/log tails are bounded and secrets are not copied.
- Failure evidence remains diagnostic and cannot turn a failed checkpoint green.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

- Canonical address and one-tool discovery are explicit evidence contracts. [1]

### Repo-Internal References

- Tmux evidence is bounded and redacts the credential value. [2]
- Failure evidence joins response, catalog, inbox, hosted control, and Codex observations. [3]

### Cross-Repo References

No meaningful cross-repository reference applies.

- Evidence is produced from the run-owned fixture and current candidate only. [4]
