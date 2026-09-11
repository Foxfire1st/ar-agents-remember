# mcp/tests/test_inbox_rebinding_mechanics.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_inbox_rebinding_mechanics.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Inbox transition idempotence, supersession and replacement delivery.

## Code Commentary

### Logic

Repeated terminal transitions append once. Ambiguous structural ownership refuses. A stale landing cannot overwrite concurrent supersession, and stale unresolved cannot overwrite landed truth. Superseding during actual in-flight delivery wins; a rebound row is sent to the current replacement in a subsequent sweep.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Folded durable state is the oracle. Task containment resolves structural ownership rather than guessed role mailboxes or stale spawn provenance.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Landed superseded unresolved expired and rebind are idempotent. | `test_landed_superseded_unresolved_expired_and_rebind_are_idempotent` | mcp/tests/test_inbox_rebinding_mechanics.py:76-100 |
| Ambiguous structural owner refuses instead of role mailbox guess. | `test_ambiguous_structural_owner_refuses_instead_of_role_mailbox_guess` | mcp/tests/test_inbox_rebinding_mechanics.py:121-132 |
| Concurrent supersede survives a stale landing append. | `test_concurrent_supersede_survives_a_stale_landing_append` | mcp/tests/test_inbox_rebinding_mechanics.py:174-186 |
| Concurrent landed survives a stale unresolved. | `test_concurrent_landed_survives_a_stale_unresolved` | mcp/tests/test_inbox_rebinding_mechanics.py:188-198 |
| Supersede during in flight delivery wins over landing. | `test_supersede_during_in_flight_delivery_wins_over_landing` | mcp/tests/test_inbox_rebinding_mechanics.py:205-315 |
| Rebound row is delivered to replacement in next sweep. | `test_rebound_row_is_delivered_to_replacement_in_next_sweep` | mcp/tests/test_inbox_rebinding_mechanics.py:322-440 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-31T14:31+02:00 — Addendum-11 review corrected every test-class range shifted by the
  `_Topology.altitude` insertion; the ranges now cover each complete AST class span.

- 2026-08-31T14:26+02:00 — A005 closeout repair completed the focused `_Topology` double with
  the protocol's `altitude` operation after the generation-14 Pyright gate exposed the missing
  member; routing behavior and assertions are unchanged.

- 2026-08-31T14:06+02:00 — A005 closeout size repair relocated reviewer-specific stamped-parent
  and invalid-parent forcing to `test_leaf_structural_refusal_coverage.py`; this module retains the
  generic durable-owner rebinding contract and is again below the 1,200-line hard limit.

- 2026-08-31T13:42+02:00 — A005 closeout repair added stamped reviewer-row rebinding plus explicit
  incomplete and mismatched reviewer-parent refusals.

- 2026-08-31T09:02+02:00 — 260821-ARSPAWN-L5 A005 citation reconciliation refreshed
  the row-owner source range after the reviewed routing module moved; no semantic onboarding
  claim changed. Verification remains closeout-owned.

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T00:08+02:00 — Replaced the obsolete spawn-provenance/role-mailbox description with
  current task-document containment and unique-occupant refusal semantics; the transition subtest's
  integer diagnostic is serialization-only for xdist. Verification metadata remains pinned until
  closeout.

- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_inbox_rebinding_mechanics.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: No content impact: re-read the current staged inbox-rebinding mechanics harness; the existing assertions remain accurate. Verification metadata remains pinned until closeout.
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the nudge-store removal from all
  rebinding-mechanics harness contexts. Verification metadata pinned until closeout stamps
  the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: created this file-level onboarding card for
  the new rebinding-mechanics forcing suite (33 test methods: transition idempotence, owner
  derivation, action/evaluation/retention branches, legacy fold, cap fill, F1 stale-snapshot
  authority, supersede-during-in-flight e2e, rebound delivery-to-B). Verification metadata
  pinned until closeout stamps the 260713-TES-L4 commit.
