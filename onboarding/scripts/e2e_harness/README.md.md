# README.md

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

The committed Codex production registration forwards `AR_HOSTED_SESSION_ID` and `AR_SPAWN_ROLE`
into its MCP subprocess while launching `uvx --refresh-package agents-remember-mcp
agents-remember-mcp@latest` (`.codex/config.toml:1-10`). This released-package launch does not
identify a source candidate. The separate candidate runtime exposes its actual source digest,
interpreter and package root through `serving/build_info.py`; a package version alone cannot
establish that candidate identity. This distinction does not assert that the deleted public-surface
conformance suite still runs or supplies coverage.

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

## Evidence

### Docs References

No Domain Documentation source is configured; the executed CLI records current runtime evidence.

- The document distinguishes the real consumer from deterministic provider scripting. [1]

### Repo-Internal References

- Security containment and false-positive prevention are explicit fixture contracts. [2]
- Idempotency, negative sentinels, and cleanup evidence are distinguished from retries. [3]
- One forwarded tmux namespace binds role creation to liveness and cleanup. [4]
- Targeted/full applicability, replication count, and retry count are explicit. [5]

### Cross-Repo References

No meaningful cross-repository reference applies.

- The document names no sibling repository as implementation authority. [6]
