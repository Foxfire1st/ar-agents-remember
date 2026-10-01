# mcp/src/agents_remember/mcp/tools/hosted_readiness.py

## Governing Overview

[overview.md](overview.md)
## Purpose

One payload builder, `hosted_session_readiness_payload` — the read-only, bounded, exact-session
readiness check a dispatcher must pass before delivering a durable brief.

## Code Commentary

### Logic

`hosted_session_readiness_payload(config, *, session_id, wait_seconds=0.0, catalog=None, host=None)`:

1. Validates `wait_seconds` **before** touching anything: it must be finite and within
   `0.0 .. MAX_HOSTED_READINESS_WAIT_SECONDS`, otherwise `ValueError`. The wait is always finite.
2. Resolves the catalog (`TerminalCatalog(terminal_catalog_path(config.coordination_root))`) and the
   host (`TerminalHost()`) unless a caller injected one — the two optional parameters exist for tests.
3. Calls `hosted_session_readiness(catalog, host, session_id=session_id,
   wait=ReadinessWait(seconds=wait_seconds))` — since 260731-EFA-L2 the wait travels as a
   `ReadinessWait` value from `serving/hosted_readiness.py` rather than a bare float keyword.
4. Projects the result onto the public response: `ok` (true only when `status == "ready"`),
   `status`, `session`, and — from the catalog entry when present — `harness`, `tmuxName`,
   `controlState`, `activity`, `acceptance`, `vendorSessionId`, `pendingInteraction`, plus `detail`.
   Every entry-derived field is `None` when there is no entry.

Readiness is exact adapter evidence: catalog identity plus the negotiated protocol snapshot,
including acceptance capability. Pane text, copy mode and log timing are diagnostics, not authority.
The builder never sends input.

### Invariants And Boundaries

- Read-only and bounded. Do not add an unbounded or infinite wait, and do not make the tool write.
- The readiness predicate itself lives in `serving/hosted_readiness.py`; this file only validates the
  wait, resolves collaborators, and shapes the response.
- `catalog`/`host` stay optional injection points for tests; production passes neither.

## Evidence

### Docs References

No relevant documentation was configured in the resolved source registry; repository source is the
direct evidence.

### Repo-Internal References

- The readiness predicate, `ReadinessWait`, and `MAX_HOSTED_READINESS_WAIT_SECONDS`. [1]
- The tool declaration that exposes `session_id` / `wait_seconds`. [2]
- The dispatch path that requires `status=ready` before creating a durable brief row. [3]

### Cross-Repo References

No meaningful cross-repo references.

#### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.
