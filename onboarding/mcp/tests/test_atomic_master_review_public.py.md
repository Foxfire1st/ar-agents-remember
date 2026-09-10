# mcp/tests/test_atomic_master_review_public.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_atomic_master_review_public.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-09T14:10+02:00 |
| lastVerifiedCommitHash | `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`|
| lastVerifiedCommitDate | 2026-09-10T07:24:09+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Exercises the registered public task and integration routes for the CCR-R26 master-review boundary.
It checks public refusal and publication behavior while preserving the distinction between atomic
child closeout and master-to-parent integration. The current card tracks the composed CQ07
external-memory ledger-identity fixture plus the R27 review-state callers; earlier V6 composition
evidence remains historical.

## Code Commentary

### Logic

The module uses the public MCP registration helpers to construct leaf, direct-series, and master
scenarios. It proves that atomic child closeout remains deferred through the real leaf-to-master
landing path, while a direct organizational candidate retains missing, blocked, current, and stale
leaf-review behavior. The master cases exercise missing-review refusal, candidate stamping, exact
protected landing, and the lock-time evidence-staleness recheck.

The CQ06 successor narrows the optional `closeout_door` values in the blocked and stale direct-door
branches with explicit `is not None` assertions and reformats three existing response-text
comprehensions. These are Pyright/Ruff repairs only; no fixture, route, operation, or refusal
assertion changes.

The CQ07 successor adds an external-memory atomic-door fixture. It exercises full and abbreviated
ledger commit identities, then malformed, missing, non-commit, and ambiguous identities through
the registered public door. The fixture asserts that valid abbreviated identities are returned as
their resolved full commit, while invalid identities return `closeout-door-ledger-incompatible`
and preserve the contract, ledger bytes, and protected source ref. The composed source contains
these assertions. V6 extends the same fixture with a 10,000-character invalid identity and asserts
a bounded response carrying the stable refusal cause and explicit truncation marker. These are
source assertions; this card does not promote a focused run to certification.

The R27 API composition also exercises the shared `begin_review` transition before direct and
canonical-master route-review publication and checks the returned `reviewState` payload. The
current source is preparation evidence for the public API and preserves the R26 altitude rule:
atomic children remain deferred while the aggregate master review is consumed at integration.

The L41 public state payload also records the two default exception fields explicitly:
`developerApproval` is `None` and `additionalRounds` is `0` before any exhaustion-only direct
permission. This keeps the public contract aligned with the bounded R28 state without claiming
developer authentication.

### Conventions

Public route tests compare the readable and structured response payloads, task-document state,
contract generation, and protected ref movement inside isolated fixtures. They observe the review
boundary; they do not authorize a verdict or substitute for the combined master integration run.
The CQ06 edits retain the same runtime assertions and add no casts or ignores.
The CQ07 fixture is isolated under disposable repositories and does not authorize a verdict or
substitute for the combined master integration run.

### Invariants And Boundaries

- A public atomic child operation defers independent review and can still complete its exact
  leaf-to-master landing while the child and master documents remain review-free.
- A direct organizational door refuses missing, blocked, and candidate-stale reviews without
  moving the protected source ref or replacing the prior generation; a current review publishes.
- Master integration refuses before publication when its current review is absent or its evidence
  becomes stale after admission.
- Optional door narrowing is explicit and local to the blocked/stale assertions; it does not alter
  the public operation contract.
- External-memory ledger identities are resolved through Git before door publication: a full or
  abbreviated commit identity is normalized to the full commit, while missing, ambiguous, and
  non-commit identities refuse without changing prior contract, ledger, or protected-ref state.
- An oversized invalid identity keeps the public refusal bounded, retains the resolution cause and
  `...[truncated]...` marker, and leaves the contract, ledger, and protected source ref unchanged.
- Public route-review publication begins the bounded review round and exposes its pending/finding
  state without allowing callers to supply plane-owned candidate identities.
- A fresh public review state exposes `developerApproval: None` and `additionalRounds: 0`; those
  fields remain recorded evidence and do not authorize extra rounds by themselves.
- The test owns no mutation outside its isolated fixtures.

### Todos

The final combined public integration exercise remains parent-owned.

## Docs References

No relevant external documentation was configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation source was configured for this test module. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public helper and route registration coverage. | `_call`; `_assert_wire_payload` | mcp/tests/test_atomic_master_review_public.py:81-99 |
| CQ07 external-memory identity fixture, long-identity bound, and public door assertions. | `_ambiguous_memory_commit_prefix`; `_external_atomic_ledger_door_case`; `_assert_external_ledger_identity_cases` | mcp/tests/test_atomic_master_review_public.py:336-505 |
| Atomic child deferral, real leaf landing, organizational leaf review gate, and CQ07 fixture invocation. | `test_atomic_leaf_public_closeout_defers_review_and_organizational_leaf_keeps_gate` | mcp/tests/test_atomic_master_review_public.py:669-777 |
| Direct organizational missing, current, blocked, and stale review behavior. | `test_registered_direct_organizational_door_keeps_leaf_review_gate`; `_exercise_blocked_direct_review` | mcp/tests/test_atomic_master_review_public.py:258-334; mcp/tests/test_atomic_master_review_public.py:778-859 |
| CQ06 static narrowing and formatter-only successor edits. | "closeout-door-route-review-blocked"; "closeout-door-ledger-incompatible\" in missing_text[0]"; "closeout-door-route-review-stale" | mcp/tests/test_atomic_master_review_public.py:296-301; mcp/tests/test_atomic_master_review_public.py:460-465; mcp/tests/test_atomic_master_review_public.py:851-856 |
| Missing master review refuses before protected ref movement. | `test_atomic_master_public_integration_refuses_without_review_before_ref_move` | mcp/tests/test_atomic_master_review_public.py:860-946 |
| Master review stamps the branch candidate and allows exact landing. | `test_public_master_review_stamps_branch_candidate_and_allows_exact_protected_landing` | mcp/tests/test_atomic_master_review_public.py:947-1023 |
| Evidence mutation after admission makes the master review stale. | `test_public_master_integration_refuses_after_admission_evidence_changes` | mcp/tests/test_atomic_master_review_public.py:1024-1129 |
| Production refusal projection. | `master_route_review_refusal` | mcp/src/agents_remember/worktrees/integration/master_review_gate.py:53-95 |
| R27 direct and canonical-master review-state publication paths. | `test_registered_direct_organizational_door_keeps_leaf_review_gate`; `test_public_master_review_stamps_branch_candidate_and_allows_exact_protected_landing`; `test_public_master_integration_refuses_after_admission_evidence_changes` | mcp/tests/test_atomic_master_review_public.py:778-859; mcp/tests/test_atomic_master_review_public.py:947-1023; mcp/tests/test_atomic_master_review_public.py:1024-1129 |
| L41 public default exception fields remain explicit before any exhaustion-only permission. | `test_registered_direct_organizational_door_keeps_leaf_review_gate` | mcp/tests/test_atomic_master_review_public.py:778-818 |

## Cross-Repo References

No meaningful cross-repo implementation reference is required for this preparation test card. The
coordination requirement is tracked in the task report.

## Historical V3 Binding

The predecessor v3 public-test source was cumulative tree
`1ace1845d61c29f47ece5b4f2b93c86f7203021d` with file SHA-256
`fcd8c9e8797ff5d9de994d0b18b71932ba950c028160edea57e1cc9703a7e59c`. That identity is retained
as historical composition evidence and is not the active successor binding below.

## Historical V6 Candidate Binding

This card is bound to the frozen V6 candidate tree `637152923330a4f7ac67a819dc124211497a7998`;
the current CQ07 successor file is 41,407 bytes and 1,047 lines with SHA-256
`bf4de116fbbfd4cb58b2cc83b31d948cc67d8b2e6879ac2c367dfe14721647a3`. The immediate V5 bytes
`06295ed0ea74686eec95b55c10e3ec495fcc656d002e4f52215c253b1030ceab` (1,032 lines) and CQ06
predecessor bytes `7415b51de6e181276fe21e02108399a29f6aa8ad72a4d03fdbda94220f28fa7a` (871 lines)
remain historical evidence. V6 composition is recorded in the V6 candidate manifest; no final
test pass or landed commit identity is asserted here. Verification metadata remains blank until
governed closeout stamps a landed code commit.

## Current R27 API Candidate Binding

The source checkout is based at code commit `8133b6a9de2f787cb6c4527621a70123357aff31`; the
frozen R27 API composition of this file is 44,107 bytes and 1,129 lines with SHA-256
`8b5da44fc27b3fdc6af3f8d8f6071687f4ca4d2f51a6f6439374d2195d2ae4f3`. It includes the R26 public
route tests plus the bounded `begin_review`/`record_route_review` state assertions. No focused test
pass, landed commit identity, independent review, or acceptance is asserted here; verification
metadata remains blank until governed closeout stamps a genuine code commit.

## Current R28 L41 Candidate Binding

The frozen L41 source tree is `2d2e1ae39b2046b5663aca2cf82f27779dafe0c2`. This public-test source is
44,173 bytes and 1,131 lines with SHA-256
`00ebadf8ddd33be0ecba0fefb64d6d5a415bc64a8ecde50a5361e3682d7fab9f`. Relative to the preserved
R27 binding, the public direct-organizational review-state assertion includes the two default
exception fields (`developerApproval: None`, `additionalRounds: 0`); all R26/R27 route, ledger,
atomic-child, and master-integration proofs remain in the same source. No focused pass, landed
commit identity, independent review, or acceptance is asserted.

## Update History

- 2026-09-09T14:10+02:00 — CCR-L42 curator intake created/reconfirmed this one-to-one card against the current uncommitted source bytes (SHA-256 `00ebadf8ddd33be0ecba0fefb64d6d5a415bc64a8ecde50a5361e3682d7fab9f`, `44173` bytes, `1131` lines). Verification remains closeout-owned; no test, review, acceptance, or future commit is asserted.

- 2026-09-08T23:09:11+02:00 — CCR-R27/R28 bounded memory citation correction: repaired current report-listed table-safe anchors, source ranges, and implementation-only provenance against the paired frozen source; verification metadata and historical bindings remain unchanged.
- 2026-09-08T22:56:00+02:00 — CCR-R27/R28 bounded memory curation: corrected 2 report-listed citation anchor/range entries against the paired frozen source; existing verification metadata and historical bindings remain unchanged.
- 2026-09-08T22:32:00+02:00 — CCR-R28 L41 memory curation: preserved the historical V3/V6/R27
  bindings and recorded the exact frozen L41 public default-state fields without changing the
  route-boundary, ledger, or integration claims; no test, review, or acceptance claim was added.
- 2026-09-08T22:13:45+02:00 — CCR-R27 L40 API memory preparation: rebound the public atomic-master card to the 1,129-line source, recorded the review-state caller assertions, and retained V6 as historical composition evidence; no code commit, review, or acceptance claim.
- 2026-09-08T20:37:13+02:00 — CCR-CQ07 V6 successor curation: rebased the public-test fixture
  citations to the 1,047-line source, recorded the 10,000-character identity bound and truncation
  assertion, and replaced the active V5 binding with the exact V6 file bytes; no test, source,
  shared-overview, or landed-commit claim was added.
- 2026-09-08T20:26:49+02:00 — CCR-CQ07 V5 successor curation: rebased public-test citations to the
  composed 1,032-line source, recorded the full/abbreviated/missing/non-commit/ambiguous ledger
  identity fixture and its protected-state assertions, and bound the card to the exact V5 file
  bytes; no test pass, source edit, shared overview edit, or verification pin was claimed.
- 2026-09-08T20:12:08+02:00 — CCR-L24 v4 citation repair: re-read the direct-door and CQ06 claims against the current 871-line successor, expanded every pooled source segment to a full path, and anchored formatter/narrowing evidence to unique literals; CQ07 successor preparation remains pending and no verification pin or code/shared overview was changed.
- 2026-09-08T19:14:44+02:00 — CCR-CQ06 successor-preparation curation: rebased public-test anchors to the 871-line corrected file, recorded the two explicit optional-door assertions and formatter-only shifts, replaced the active v3 whole-tree binding with the exact successor file SHA, and preserved v3 as historical evidence; no code or shared overview was edited.
- 2026-09-08T19:06:02+02:00 — CCR-CQ03/R25 source-ground memory repair: expanded the card to the five current public operation proofs, corrected all source ranges to frozen v3, and updated the candidate binding; no code or shared overview was edited.
- 2026-09-08T18:14:20+02:00 — CCR-L24 bounded memory-quality repair: re-read the renamed admission-evidence test, corrected its source range, and updated the active candidate tree to frozen v2; no verification pin was fabricated.
- 2026-09-08T17:31:25+02:00 — CCR-L24 final-v2 source binding: rebased active R25/R26 citation ranges against the frozen cumulative source; verification remains closeout-owned.

- 2026-09-08T16:42+02:00 — CCR-R26 source-grounded preparation: created the card for public
  route-boundary checks from the frozen source. Commit-owned verification metadata remains blank.
