# mcp/src/agents_remember/mcp/tools/hosted_readiness.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | mcp/src/agents_remember/mcp/tools/hosted_readiness.py |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-31T15:31+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | mcp/src/agents_remember/mcp/tools/overview.md |

## Governing Overview

Governing overview: mcp/src/agents_remember/mcp/tools/overview.md

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

## Docs References

No relevant documentation was configured in the resolved source registry; repository source is the
direct evidence.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The readiness predicate, `ReadinessWait`, and `MAX_HOSTED_READINESS_WAIT_SECONDS`. | `hosted_session_readiness`; `ReadinessWait`; `MAX_HOSTED_READINESS_WAIT_SECONDS` | mcp/src/agents_remember/serving/hosted_readiness.py:21-21; mcp/src/agents_remember/serving/hosted_readiness.py:40-52; mcp/src/agents_remember/serving/hosted_readiness.py:59-90 |
| The tool declaration that exposes `session_id` / `wait_seconds`. | `hosted_session_readiness` | mcp/src/agents_remember/serving/hosted_readiness.py:64-95 |
| The dispatch path that requires `status=ready` before creating a durable brief row. | `require_dispatch_target` | mcp/src/agents_remember/serving/dispatch_brief.py:109-130 |

## Cross-Repo References

No meaningful cross-repo references.

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T18:11+02:00 — 260731-EFA-L6 S18-B14 curator: repaired 3 citation rows with exact anchors (`hosted_session_readiness`/`ReadinessWait`/`MAX_HOSTED_READINESS_WAIT_SECONDS`, the registration declaration, `require_dispatch_target`) and ledger-verified ranges; re-pointed the dispatch-brief citation from the removed `mcp/tools/dispatch_brief.py` to `serving/dispatch_brief.py`. Scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: the wait now travels as `ReadinessWait(seconds=...)`
  into `hosted_session_readiness`. Replaced the placeholder body (Purpose, Logic and References had
  been one repeated sentence) with the builder's actual validation, collaborator resolution and
  response projection, read from the current source. Verification metadata pinned until closeout
  stamps the L2 code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
