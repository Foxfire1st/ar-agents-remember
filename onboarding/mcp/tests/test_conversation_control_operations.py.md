# mcp/tests/test_conversation_control_operations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_control_operations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Interrupt ledger contract tests (R1/R7). Every test drives the real composition up to the harness
edge — a real bridge + IPC server on a real socket, the real submission authority, and the landed L2E
client reads — with the structural fake adapter as the only double. Covers acknowledgement vs
settlement, idempotence, per-session serialization, lost-response reconcile, the guard battery, and
both pi settlement classes (content-less, content-ful, and oversized/clipped).

## Code Commentary

### Logic

Since 260731-EFA-L2 every call into the ledger carries a `ControlRequest` parameter object:
`operations.interrupt(ControlRequest(service=…, authorization=…, ar_session_id=…,
expected_bridge_epoch=…), turn_id=…, request_id=…)`, and the same for `interrupt_status` with its
`reconcile=` flag. The four scope values that were loose leading arguments now travel bound
together — nothing in the package may act on a session without all four, and `ControlRequest`
narrows to a `ControlScope` only once the service has verified the epoch.

cit:([`CodexInterruptTests`], mcp/tests/test_conversation_control_operations.py:40-192): accepted → `interrupted`/`already-settled`/`failed` settlement over the
completion surface; identical-tuple replay returns the stored projection with one native write;
reused id + different tuple → `request-conflict`; concurrent same-tuple gathers serialize to one
write; lost `may_have_sent` → `unknown` (202) → reconcile recovers the first ack with one write;
pre-write failure → 503 with no phantom record. cit:([`PiInterruptTests`], mcp/tests/test_conversation_control_operations.py:195-410): the pi settlement battery
including the Finding 1 regression pair (content-ful `stop` → `already-settled`, content-ful
`aborted` → `interrupted`) driven through the real bridge evidence path, plus the Finding 2 facet
regressions over the closed L3E envelope preservation (an oversized `x*40_000` content-ful frame
settles not-`pending`; a small `toolUse` then an oversized final `aborted` settles `interrupted`,
never `already-settled`) — both proven non-vacuous by neutralizing the L3E preservation.
cit:([`ClaudeInterruptTests`], mcp/tests/test_conversation_control_operations.py:413-509): claude is no longer gated off — the suite asserts the capability
reports `supported` at evidence tier `runtime-fixture` (fixture
`claude-2.1.217-installed-20260722`, runtime version `2.1.217`), that the interrupt accessor shares
the control gate's verdict, and then drives the same settlement battery as the other harnesses:
accepted/`pending` on acknowledgement with the operation id reaching the adapter, `interrupted`
(200) after the abort lands, `already-settled` (200) on natural completion, `failed` (503) on an
unprovoked error result, and a stale expected identity refused before any native call.

### Conventions

Every path crosses the real socket; only the lost-response classes patch the client boundary inside
the ledger (documented). The service is read from `harness.service` (the `NOW`-anchored instance), so
lease arithmetic is time-consistent regardless of wall clock.

### Invariants And Boundaries

- Acknowledgement ≠ settlement is asserted for every terminal class, per harness.
- Idempotence proofs count native writes (exactly one for identical replay / concurrent same-tuple).
- The pi content-ful and oversized/clipped regressions fail on the exact Finding 1 / Finding 2
  symptoms without the fix and pass with it — non-vacuity is proven, not assumed.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the interrupt contract is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The suite exercises the interrupt ledger over the shared topology and the L3E-preserved evidence
fields.

| Finding | Anchor | Source |
| --- | --- | --- |
| The interrupt ledger under test, incl. the Finding 1 payload-type settlement match. Both entry points now take a `ControlRequest`, the per-attempt values travel as `InterruptTicket` (L205-L216), and the claude branch's settlement match was extracted into `_claude_result_settlement` (L417-L450). | `interrupt` | mcp/src/agents_remember/serving/conversation/control/operations.py:95-156; mcp/src/agents_remember/serving/conversation/control/operations.py:159-160; mcp/src/agents_remember/serving/conversation/control/operations.py:205-216; mcp/src/agents_remember/serving/conversation/control/operations.py:417-450; mcp/src/agents_remember/serving/conversation/control/operations.py:452-482 |
| The `ControlRequest` scope object these calls build, and its `resolved()` narrowing to a verified-epoch `ControlScope`. | `ControlRequest` | mcp/src/agents_remember/serving/conversation/control/service.py:156-197 |
| The shared fake-topology harness (real bridge/IPC/authority, `NOW`-anchored service, pi emit helpers). | `NOW` | mcp/tests/_control_plane.py:82-82 |
| The L3E truncation-envelope identity preservation the Finding 2 regressions depend on. | `_preserved_evidence_identity` | mcp/src/agents_remember/models/conversations/evidence.py:242-269 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260718-CHATS-L5I Current Delta

Control-operation regressions now cover structured interaction answers and native interrupt acknowledgement-versus-settlement behavior through the authorized operation boundary.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: normalized the 3 citation rows
  (operations.py ledger extents, service.py `ControlRequest`/`ControlScope`, harness_control_models
  L3E preservation) and corrected the `InterruptTicket` prose range to L205-L216. Zero findings
  remain.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: the `PLR0913` pass moved the ledger's scope
  arguments into a parameter object, so the card now states the current call shape and its anchors
  were re-derived. `operations.interrupt` and `operations.interrupt_status` take a frozen
  `ControlRequest(service, authorization, ar_session_id, expected_bridge_epoch)` positionally,
  keeping `turn_id`, `request_id` and `reconcile` keyword-only; the complexity extraction in the
  same leaf also added `InterruptTicket` and split the claude settlement match out as
  `_claude_result_settlement`, both now cited. Nineteen call sites grew, moving the class anchors,
  so `CodexInterruptTests` L34 became L40 and `PiInterruptTests` L178 became L195, verified by
  reading the file at those lines. While re-anchoring, found the third paragraph describing a class
  that does not exist: there is no `ClaudeInterruptGateTests`, and cit:([`ClaudeInterruptTests`], mcp/tests/test_conversation_control_operations.py:413-509) has
  not proved a pre-native capability refusal for some time — it asserts claude is `supported` at
  evidence tier `runtime-fixture` and then drives the full settlement battery. That paragraph was
  already wrong at the L2 base commit, not by this leaf's doing, and has been rewritten against the
  current source. Also shifted the `_control_plane.py` harness range to L88-L518; the
  `harness_control_models.py` L3E range was re-checked and is still accurate. No settlement class,
  write count, epoch check or non-vacuity claim changed. Verification metadata stays pinned until
  closeout stamps the code commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the R4 contract-reason refinement in
  `ClaudeInterruptGateTests` — the pre-native capability refusal now asserts a contract-driven reason
  (`"contract"` in the message), not a version-string comparison, matching the version-gate removal.
  Verification metadata stays pinned (uncommitted); closeout re-stamps the candidate commit.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the interrupt ledger
  suite — codex/pi/claude coverage over the real seam, idempotence write-counting, lost-response
  reconcile, and the Finding 1 content-ful + Finding 2 oversized/clipped settlement regressions
  (non-vacuous). Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
