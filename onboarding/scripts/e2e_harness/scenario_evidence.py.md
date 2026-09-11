# scenario_evidence.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `scripts/e2e_harness/scenario_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T10:33+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `scripts/e2e_harness/overview.md` |

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

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical address and one-tool discovery are explicit evidence contracts. | `DiscoveryEvidence` | scripts/e2e_harness/scenario_evidence.py:23-78; scripts/e2e_harness/scenario_evidence.py:103-146 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Tmux evidence is bounded and redacts the credential value. | `tmux_evidence` | scripts/e2e_harness/scenario_evidence.py:197-235 |
| Failure evidence joins response, catalog, inbox, hosted control, and Codex observations. | `failure_evidence` | scripts/e2e_harness/scenario_evidence.py:238-284 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| Evidence is produced from the run-owned fixture and current candidate only. | `failure_evidence` | scripts/e2e_harness/scenario_evidence.py:238-284 |

## Update History

- 2026-08-31T10:33+02:00 — 260821-ARSPAWN-L5 closeout repair: generation 6 proved every
  dispatch succeeded but C09 could not decode Codex's current `Wall time`/`Output` result envelope.
  The evidence boundary now recognizes that exact shape and still rejects malformed wrappers;
  verification remains closeout-owned.

- 2026-08-30T22:20:19+02:00 — 260821-ARSPAWN-L5 converted source references to the
  canonical anchored citation format. Verification metadata remains closeout-owned.

- 2026-08-30T22:11:35+02:00 — 260821-ARSPAWN-L5: factored live tool-discovery
  observations into an immutable evidence value with small extraction predicates. Verification
  metadata remains closeout-owned.

- 2026-08-30T21:59:40+02:00 — 260821-ARSPAWN-L5: strengthened L5-C09 with the shared
  schema digest, controlled negative-sentinel results, and positive public response evidence for
  every dispatch route. Verification metadata remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 created onboarding for bounded checkpoint and failure evidence. Verification metadata remains closeout-owned.
