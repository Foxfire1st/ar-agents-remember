# Closeout Integration Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/closeout` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Integration overview](../overview.md)

## What This Area Is

Closeout-door publication, structured curator-coherence authority, source reconstruction, ledger
recovery, organizational repair, and recovery projection. It separates disposable scheduling
evidence, candidate acceptance evidence, and the durable operation journal.

## Hot Path Summary

`prepared_certification.py` (relocated here from `memory_quality/` by commit `deb032fb`) composes the
actual affected closure and full memory checks against a proved private code view;
`curator_coherence.py` captures and validates the exact code/memory/task/attestation candidate;
`curator_coherence_publication.py` publishes the sole live content-addressed authority;
`curator_coherence_judgments.py` binds agent-owned decisions to evidence bytes; and
`curator_coherence_render.py` produces a one-way human projection. `door_source.py` reconstructs
the exact waiting source; `ledger_recovery.py` advances code and memory proof after partial
closeout without making the disposable queue own commit evidence. `integration_reopen.py` decides
whether exact newly produced code or memory output needs another plane-owned integration.
For graph-backed candidates, both door reconstruction and curator-coherence observation pass the
already resolved authored graph to the shared queue/task-domain context and use its bound immutable
sprint snapshot. The door, coherence record, and projection therefore cannot mix graph generations.

CCR now binds canonical semantic `taskIntent` and declared direct dependency digests through
curator coherence, waiting/claimed doors, and lifecycle admission. A stale or missing intent
refuses current use and names republishing, rather than accepting topology alone.
`task_intent_identity.py` resolves the exact contract-owned leaf;
`task_intent_legacy_census.py` separately counts current legacy containers before decoder
removal. Historical generations remain audit evidence. These existing door/journal owners
are distinct from the selected certification graph: admission and code-suffix execution are now
composed under `certification/`; prepared-memory and finalization execution are separate registered continuation responsibilities.

## De-Entanglement Cut Relocations

Three member cards left this route and one arrived, all by explicit relocation commits:

- `future_code_candidate.py`, `memory_candidate_pair.py` (commit `0b63d6fc`) and
  `memory_census_scope.py` (commit `be517eec`) moved to `memory_quality/`, because a pre-closeout
  quality service must be able to mint and prove its own memory-candidate identity without the
  closeout plane. This route may depend on `memory_quality/`; not the reverse.
- `prepared_certification.py` moved in from `memory_quality/` (commit `deb032fb`) as the
  closeout-facing certification adapter.

The public closeout-door *tool entry point* was deleted by the same cut (commit `6982c6a7`, which
removed `application/closeout_door.py`, `mcp/tools/closeout_door.py`, the `models/lifecycles/door_response.py`
response model and the tool registration). The closeout-internal door modules on this route
(`door.py`, `door_control.py`, `door_evidence.py`, `door_source.py`, `initial_door_recovery.py`)
were not removed by that commit.

## Selected Certification Route

[The selected certification overview](certification/overview.md) follows actual frozen admission, explicit predecessor/publication readback, journal CAS and suffix execution. It also explains retained red evidence, current Gate-5 observations and the narrowly proven code-output recovery comparison. These responsibilities extend the existing door/coherence/journal separation; they do not make queue state own certification or themselves establish memory/finalization execution.

## Local Invariants And Traps

- Door publication authorizes entry; the operation journal owns running and terminal evidence.
- Recovery is idempotent and candidate-bound; missing or conflicting proof refuses loudly.
- Queue invalidation never erases an already-claimed lifecycle operation.
- One stable structured coherence manifest selects one immutable generation per leaf. Historical
  Markdown is neither parsed nor searched.
- Memory readiness, door evidence, and closeout admission share one currentness validator.
- The validated record projects exact content/route no-impact identities to onboarding body gates;
  only unchanged stale content is eligible, while untraced edits remain closed.
- Malformed live authority bytes remain replaceable only through exact prepared CAS.
- Graph-backed closeout consumers share one admitted immutable graph generation per observation.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `door_source.py` | [door_source.py.md](door_source.py.md) | covered |
| `ledger_recovery.py` | [ledger_recovery.py.md](ledger_recovery.py.md) | covered |
| `prepared_certification.py` | [prepared_certification.py.md](prepared_certification.py.md) | covered |
| `curator_coherence.py` | [curator_coherence.py.md](curator_coherence.py.md) | covered |
| `curator_coherence_judgments.py` | [curator_coherence_judgments.py.md](curator_coherence_judgments.py.md) | covered |
| `curator_coherence_publication.py` | [curator_coherence_publication.py.md](curator_coherence_publication.py.md) | covered |
| `curator_coherence_render.py` | [curator_coherence_render.py.md](curator_coherence_render.py.md) | covered |
| `integration_reopen.py` | [integration_reopen.py.md](integration_reopen.py.md) | covered |

## Docs And Boundary References

No configured external source applies. The lifecycle and queue overviews describe adjacent owners.

## MCAR-L03 Pair-Bound Closeout

The coherence authority, its source attestation, immutable record, publication fingerprint,
generated report, closeout preview, completed apply, and post-commit recovery now share the exact
pair model. Preview/normal closeout obtain it from current coherence; initial apply and recovery
re-prove it from the same exact contract so stale pre-commit evidence is never treated as a repo-id
fallback.

## L34 Preparation Ownership

[Preparation](preparation/overview.md) now owns selected private C/M/L creation, genuine existing-output reuse, physical code views and prepared-memory result currentness. [preparation_selection.py](preparation_selection.py.md) retains original objects and command outcomes through canonical journal CAS. Final memory evidence comes from the registered prepared-memory producer; private output selection alone is not ref publication or approval.


## Integrated IAS Recovery Contract

Preparation selection requires the exact four original code certificates and, for memory legs, the selected fifth certificate. Prepared finalization recovery is attempted before fresh original-head admission so the original generation can finish C/M/L publication after its owned refs advance. This is recovery of retained outputs, not permission to rerun commands or certify a changed candidate.

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.


## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the
  `mcp/src/agents_remember/worktrees/integration/closeout/` route changed since the recorded
  verification commit. Re-read the card against the frozen on-disk source and re-checked its claims
  and cited ranges: nothing this card asserts is falsified by the change, so no wording changed.
  Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the route moved since the
  recorded verification commit — door storage left the worktree contract for the contract's own door
  journal. Re-read the route card: its deletion and retention claims still match the tree, its
  journal invariant is now literally true, and it carries no line ranges. No wording changed;
  verification metadata remains closeout-owned.
- 2026-09-11T10:26:37+02:00 — De-entanglement cut cleanup at code commit `2fa5e81f`: moved the `future_code_candidate.py`, `memory_candidate_pair.py` and `memory_census_scope.py` sidecars out to `memory_quality/` and moved the `prepared_certification.py` sidecar in, repaired the dead `future_code_candidate.py.md` map link, and recorded that the public closeout-door tool entry point was deleted while the closeout-internal door modules remain. This records source documentation only; it makes no acceptance or certification claim.
- 2026-09-10T02:27:58+02:00 — CCR-L42 parity curation: No route impact: curator preparation and closeout now run the shared sidecar and route body/history validators independently; this route's ownership and source semantics remain unchanged. No acceptance claim is made.

- 2026-09-09T02:35:47+02:00 — CCR-L38 inherited route reconciliation: re-read this route's purpose, member inventory, route summary, and invariants against frozen candidate code tree `4c6b7bc2362bc03d50fc7a0643f34b591b805d45`; the candidate's changed paths are outside source route `mcp/src/agents_remember/worktrees/integration/closeout`, so no route/member/prose/invariant change is required. route-member-count=42; source inspection only; verification metadata remains unchanged pending producer-owned realization. No acceptance or certification claim.

- 2026-09-06T21:58:28+00:00 — Reconciled this route against the source delta from `245057ab16e19afdaabd5c188c9576b22e0c0870` to `d36109038b3f2b500c138f9dc1ea9c9f9a247489`. Updated current ownership and policy claims; prior verification commit/date and history remain unchanged. Source inspection only; no test, review or acceptance claim.


### 2026-09-06T17:13:06+00:00 — L34 implementation memory

Recorded the current private preparation/publication ownership from source. Existing verification identity is retained; this entry does not claim tests, certification or acceptance.

- 2026-09-06T14:58:25+00:00 — Added the selected certification child route from source at `c69d5171187fa1957025e393270db9f5a864ab14` and corrected the obsolete all-unwired claim. Preserved all earlier history and the broader route verification stamps; other closeout owners are outside this bounded update.


- 2026-09-05T07:12+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Added current task-intent and direct evidence dependencies across coherence, door and operation admission, with bounded legacy census. Verification records source review, not execution or acceptance.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: door and curator-coherence task contexts now
  bind the authored graph once and consume the same immutable sprint graph generation as projection
  currentness. Verification remains closeout-owned.

- 2026-08-30T06:08+02:00 — MCAR-L03 A005: added the extracted completed-integration reopen policy
  owner and its exact code/memory leg boundary. Verification remains closeout-owned.

- 2026-08-29T21:46+02:00 — MCAR-L03: bound coherence and all closeout report/recovery surfaces to
  one exact contract pair. Verification remains closeout-owned.

- 2026-08-29T18:29+02:00 — Added disposition-exact no-impact projection for the shared onboarding
  body gates without weakening untraced-content refusal.

- 2026-08-29T10:40+02:00 — Adopted the exact future-code candidate identity owner from the
  worktrees root so candidate identity and curator-coherence consumption share the closeout route.

- 2026-08-29T08:52+02:00 — Added the single structured curator-coherence authority, exact CAS,
  generated projection, and shared consumer validator. Verification remains closeout-owned.

- 2026-08-25T15:44+02:00 — Created for the recoverable closeout-door/journal boundary.
  Verification remains closeout-owned.
