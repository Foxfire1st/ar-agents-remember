# README.md

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `scripts/e2e_harness/README.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T09:45+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `scripts/e2e_harness/overview.md` |

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Explains the clean-room E2E's real-versus-scripted boundary, exact Codex version, model-provider
choice, security containment, production-starter preservation, applicability, replication count,
retry count, same-seat idempotency call, negative sentinels, and cleanup-evidence contract.
It also documents the single fixture-owned tmux namespace shared across Codex, candidate MCP,
liveness, and teardown.

## Code Commentary

### Logic

The document is the operator entry point rather than executable code. It directs readers to
`run.py` and `selection.py`, states that real Codex and candidate MCP behavior remain live, and
limits scripting to deterministic model-side function choices.
It names the dynamic `TMUX_TMPDIR` forwarding contract and server-scoped `exit-empty` setting that
make the clean-room process boundary truthful.

### Conventions

Version pins and security choices are stated together with their scope. Fixture-only authority is
never presented as a production runtime setting.

### Invariants And Boundaries

- Production starters retain their release-updating `uvx ... @latest` behavior.
- Codex 0.151.0 is the acceptance pin, not a production starter pin.
- The clean room is credential-free and network-bounded despite the inner client's permissive MCP
  approval settings.
- Both modes use the same entry point, two fresh replications, and zero retries.
- One repeated ambient dispatch is an idempotency assertion, not a failure retry; controlled live-
  schema mutations must fail through the canonical validator.
- Cleanup errors remain secondary evidence and still fail the teardown checkpoint.
- Candidate MCP processes, role sessions, probes, and cleanup must share the exact fixture
  `TMUX_TMPDIR`; the temporary anchor may disappear only after server-scoped `exit-empty` is off.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the executed CLI records current runtime evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| The document distinguishes the real consumer from deterministic provider scripting. | `# Clean-room E2E harnesses` | scripts/e2e_harness/README.md:1-9 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Security containment and false-positive prevention are explicit fixture contracts. | "danger-full-access" | scripts/e2e_harness/README.md:11-15 |
| Idempotency, negative sentinels, and cleanup evidence are distinguished from retries. | "same canonical occupant" | scripts/e2e_harness/README.md:17-23 |
| One forwarded tmux namespace binds role creation to liveness and cleanup. | `TMUX_TMPDIR` | scripts/e2e_harness/README.md:25-29 |
| Targeted/full applicability, replication count, and retry count are explicit. | "Every invocation executes two planned fresh replications and zero retries" | scripts/e2e_harness/README.md:31-34 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The document names no sibling repository as implementation authority. | `# Clean-room E2E harnesses` | scripts/e2e_harness/README.md:1-34 |

## Update History

- 2026-08-31T09:45+02:00 — 260821-ARSPAWN-L5 closeout repair: documented the single tmux
  namespace contract across Codex MCP forwarding, role creation, probes, and cleanup. Verification
  remains closeout-owned.

- 2026-08-30T22:20:19+02:00 — 260821-ARSPAWN-L5 converted source references to the
  canonical anchored citation format. Verification metadata remains closeout-owned.

- 2026-08-30T21:59:40+02:00 — 260821-ARSPAWN-L5: documented the same-seat repeat,
  controlled dispatch-advertisement sentinels, and separately preserved cleanup failures.
  Verification metadata remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 created onboarding for the harness operator contract. Verification metadata remains closeout-owned.
