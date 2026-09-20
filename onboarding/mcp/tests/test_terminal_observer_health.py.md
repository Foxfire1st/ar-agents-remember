# mcp/tests/test_terminal_observer_health.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| lastUpdated | 2026-09-15T20:42+02:00 |
| lastVerifiedCommitHash | `3888cd8600e39a52c540d6038820759e3d4ffa7a` |
| lastVerifiedCommitDate | 2026-09-20T20:02:13+02:00|
| path | `mcp/tests/test_terminal_observer_health.py` |
| doc_type | `file-level-onboarding` |
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pins `LOCR-R17@v1`'s executable contract for the observer's own health: one exact atomic v1 record,
one exact serve-time payload, one additive omissive tail key, and publication on the observer CALL
for both outcomes. Sixteen cases in three classes: nine drive the record/store/accumulator
directly, two drive the real `_serving_lifespan` where publication ordering and the write-failure
recovery path are the subject, and five drive the served surface. It is deliberately separate from
[test_serving_observation_loop.py](test_serving_observation_loop.py.md), which owns the lifespan's
observation cadence and `LOCR-R11@v1`'s failure boundary, and from
[test_serving_startup_prime.py](test_serving_startup_prime.py.md), which owns the prime's ordering.

## Code Commentary

### Logic

`TerminalObserverHealthRecordTests` (`mcp/tests/test_terminal_observer_health.py:220-617`) pins the
durable row and the writer: the destination observed at the instant of replacement is still the
previous COMPLETE record and an interrupted replacement leaves it readable with no stray temp file
(25 further publications leave exactly one constant-size row); the persisted bytes are the exact v1
field set; both counters saturate at `2**32 - 1` and a persisted above-ceiling row is omitted; a
success → failures → success sequence advances exactly the documented fields, retains
`lastSuccessAt` across failures and resets the consecutive count on success; a failed write keeps
serving the LAST persisted row rather than the newer accumulator; the status ladder is
`initializing` → `degraded` → `healthy` → `stale` with `stale` outranking everything at the exact
cutoff boundary; the cutoff is exactly six configured sweeps; every unusable source (missing,
unreadable, non-object, wrong marker, extra key, missing key, wrong type, unparseable stamp, naive
stamp, prior-lifetime stamp, above-ceiling counter) omits the key and is left byte-identical rather
than repaired; and classification is bounded, ordered and secret-safe.

`TerminalObserverHealthLifespanTests` (`:619-732`) drives the real lifespan: the prime's own outcome
is the serving lifetime's first published transition (call 1), every steady pass publishes success
and failure distinctly with the phase-selected category, and a health-write failure logs only the
fixed line and lets the next observation retry the complete record.

`TerminalObserverHealthServedTailTests` (`:734-931`) drives the served surface through the real
`_state_response` handler and the real `stream_events` generator against stub projectors: the tail is
additive and leaves every existing served field byte-identical; `/api/state` serves the key without
touching revision, ETag or the 304 path; the SSE `snapshot` carries health while a `delta` carries no
tail; a fresh notifier cannot mask a stale or failed observer (cross-read rows 2, 3 and 5); and a
current success beside a fresh notifier reads `healthy` from its OWN row (row 4), with the health
half's provenance proved by equating every health fact to the persisted record and by showing the
notifier's later tick advanced no health counter (`ageSeconds` 1.0, not the notifier's 0.0).

Module-local harness: `_Clock` (`:101`), `_RouteProjector` (`:115`), `_StreamProjector` (`:128`) and
`_SecretTokenError` (`:216`), the last a `RuntimeError` subclass used to prove a custom class name
cannot reach the wire.

### Conventions

`unittest` / `unittest.IsolatedAsyncioTestCase` with module-local private harness classes and
temporary roots. Every case is a unit-lane case: no HTTP transport, no server, no real second. The
route half calls the production handler and generator directly rather than starting an ASGI app —
the integration population had only three cases of headroom, and the brief forbids raising it — so
the ETag/304 branch, the assembled body and the snapshot/delta asymmetry exercised are the
production ones.

### Invariants And Boundaries

The cases assert the contract, not a convenience reading of it: omission is asserted together with
byte-identity of the source file (so "no repair" is proved, not assumed), the failed-write case
asserts the persisted row rather than the newer accumulator, and the cross-read case asserts the
health half's provenance rather than only its status word. The module claims nothing about the
notifier's own internals, about the observer's cadence (the sibling module owns it), or about the
pre-serve prime's ordering. Written exceptions are asserted by their base category, never by message
or class text.

### Todos

None.

## Docs References

No Domain Documentation entries are configured in the resolved memory root; the module tests a
repository-owned serving contract, so no external domain claim is needed.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The record, writer and accumulator contract: exact v1 bytes, one atomic replacement, saturating counters, the failed-write source of truth, and the status ladder at the exact cutoff. | `TerminalObserverHealthRecordTests` | mcp/tests/test_terminal_observer_health.py:220-617 |
| Every unusable source omits the wire key and is never repaired, including a prior-lifetime row and an above-ceiling counter. | `test_every_unusable_source_omits_health_and_is_never_repaired` | mcp/tests/test_terminal_observer_health.py:503-567 |
| Classification is bounded, ordered and secret-safe; a custom subclass publishes its base category. | `test_failure_classification_is_bounded_ordered_and_secret_safe` | mcp/tests/test_terminal_observer_health.py:569-617 |
| Publication rides the observer call: the prime's own outcome is the first transition and both outcomes publish distinctly. | `TerminalObserverHealthLifespanTests`; `test_the_prime_and_every_steady_pass_publish_success_and_failure_distinctly` | mcp/tests/test_terminal_observer_health.py:619-732; mcp/tests/test_terminal_observer_health.py:629-682 |
| A health-write failure emits only the fixed log line and retries the complete record next observation. | `test_a_health_write_failure_logs_only_the_fixed_line_and_retries_publication` | mcp/tests/test_terminal_observer_health.py:684-732 |
| The served tail is additive and omissive, and the read routes never mutate the row. | `TerminalObserverHealthServedTailTests` | mcp/tests/test_terminal_observer_health.py:734-931 |
| The cross-read table: a fresh notifier cannot mask a stale or failed observer, and a current success beside a fresh notifier reads healthy from its own row. | `test_a_fresh_notifier_cannot_mask_a_stale_or_failed_observer`; `test_a_current_success_beside_a_fresh_notifier_reads_healthy_from_its_own_row` | mcp/tests/test_terminal_observer_health.py:858-896; mcp/tests/test_terminal_observer_health.py:898-931 |
| The served surface the cases drive: the fourth tail key and the payload model it carries. | `ServedWorkspaceProjection`; `served_state_tail` | mcp/src/agents_remember/serving/served_state.py:50-66; mcp/src/agents_remember/serving/served_state.py:78-109 |
| The publication seam and the served payload the cases enter through the real lifespan and the real route handler. | `_observe_terminal_catalog`; `_terminal_observer_health_payload`; `_state_response` | mcp/src/agents_remember/serving/_app_lifespan.py:80-107; mcp/src/agents_remember/serving/_app_lifespan.py:376-394; mcp/src/agents_remember/serving/_app_routes.py:77-108 |
| The module is registered exactly once, in the explicit unit-regression lane. | "mcp/tests/test_terminal_observer_health.py" | mcp/tests/test-evidence-lanes.toml:186-186 |

## Cross-Repo References

No meaningful cross-repository implementation boundary is established by this repository-owned
unit-regression module.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-20T17:17:10+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:186-186. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:183-183. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:182-182. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:181-181. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:179-179. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:157-157. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 6 generated projection bullet(s) by hand while resolving the memory sync** — `mcp/tests/test_terminal_observer_health.py`, `ServedWorkspaceProjection`, `served_state_tail`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.
- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 4 generated projection bullet(s) by hand** — `mcp/tests/test_terminal_observer_health.py`, `ServedWorkspaceProjection`, `served_state_tail`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.
- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"mcp/tests/test_terminal_observer_health.py"` → `mcp/tests/test-evidence-lanes.toml:152-152`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:151-151. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/src/agents_remember/serving/served_state.py:50-51 in the row 106 of this card; the repetition added no pooled evidence
- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `ServedWorkspaceProjection` in the row 106 of this card from mcp/src/agents_remember/serving/served_state.py:78-83 to mcp/src/agents_remember/serving/served_state.py:50-51, the extent of the construct the claim is about (the checker named line(s) [11, 33, 50] as its live location)
- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `served_state_tail` in the row 106 of this card from mcp/src/agents_remember/serving/served_state.py:50-51 to mcp/src/agents_remember/serving/served_state.py:78-83, the extent of the construct the claim is about (the checker named line(s) [32, 74, 78] as its live location)
- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): added mcp/src/agents_remember/serving/served_state.py:32 to the row 106 of this card as the citation for `served_state_tail`: no cited file carried the construct, and the checker named line(s) [32, 74, 78] in this file as its live location
- 2026-09-15T18:42:00+00:00 — 260831-LOCR-L17 curator (uncommitted change set on `ar/260831-locr-l17`,
  base `99534dc5`, 13 paths, `git diff | sha256sum` = `b75a785d…`): created this file card for the new
  focused test module (16 cases / 27 subtests, 931 lines) and its `unit-regression` row at
  `mcp/tests/test-evidence-lanes.toml:122`. Recorded the current contract each class protects — the
  exact v1 row and its atomic writer, the omission-and-no-repair rule for every unusable source, the
  bounded ordered secret-safe classification, publication on the observer CALL for both outcomes, the
  fixed write-failure log line with retry, the additive omissive served tail, and the packet's
  cross-read rows (including row 4, added by this leaf's fix-verification round). Also recorded why
  the route half drives the production handler and generator directly instead of an ASGI app: the
  integration population has three cases of headroom and the brief forbids raising it, so the
  ETag/304 branch and the snapshot/delta asymmetry proven here are the production ones. Verification
  metadata remains closeout-owned; no stamp advanced.
