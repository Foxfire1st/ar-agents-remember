# mcp/src/agents_remember/serving/conversation/control/policy.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/policy.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate |  2026-07-21T11:31:07+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

R5: policy is read-only evidence. The projection separates the AR-side policy posture (the local
single-operator authorization ruling and the canonical project scope) from the effective harness
mode, each with origin/evidence, observed time, freshness, runtime/helper versions, and
unavailable/unverified reasons. There is no `PATCH`, `policyWrite`, preview, or mutation surface
anywhere in this leaf — capability gating alone cannot authorize one.

## Code Commentary

### Logic

cit:([`ConversationPolicyProjection`], mcp/src/agents_remember/serving/conversation/control/policy.py:46-55) carries two cit:([`PolicyPart`], mcp/src/agents_remember/serving/conversation/control/policy.py:36-43) DTOs — the AR `repoPolicy`
posture and the effective `harnessMode` — each with state/origin/evidence/freshness/reasons.
cit:([`conversation_policy`], mcp/src/agents_remember/serving/conversation/control/policy.py:58-101) uses the already-resolved authorization binding as route proof, resolves the session entry, verifies the bridge epoch, reads the live snapshot, and builds both
parts plus the `policyRead` capability. cit:([`_harness_mode`], mcp/src/agents_remember/serving/conversation/control/policy.py:104-130) reports Claude's `permissionMode` from
the live snapshot carrying the control-contract capability's own `capability.reason` — since
260718-CHATS-L5F R4 that reason is contract-verification language ("unverified until the control seam
is probed"), NEVER a locked-version-mismatch string; codex approval/sandbox values are adapter-private
at thread/turn start and never cross (honestly unverified); pi has no built-in permission-popup
surface. cit:([`_freshness`], mcp/src/agents_remember/serving/conversation/control/policy.py:133-134) stamps the observed-time window. cit:([`_POLICY_ORIGIN`], mcp/src/agents_remember/serving/conversation/control/policy.py:33-33) is the AR
composition origin string.

### Conventions

Every field is evidence with an origin; missing or adapter-private data is stated as
unverified/unavailable, never invented. The route is GET-only.

### Invariants And Boundaries

- No mutation surface exists: `PATCH`/`PUT`/`DELETE`/`policyWrite` are absent (the wire proves 405,
  and the foundation pin is GET-only).
- `repoPolicy` is the local single-operator loopback authority + canonical scope; `harnessMode` is
  the effective harness posture — the two are never conflated.
- Claude's `permissionMode` crosses with its control-contract capability reason — unverified until
  the control seam is probed, never a version gate (the L5F R4 removal); codex/pi carry honest
  unavailable/unverified reasons rather than a fabricated mode.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the policy contract is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The policy DTOs and capability evidence live in the contract; the AR posture comes from the L0
authorization ruling; the harness mode reads the live snapshot.

| Finding | Anchor | Source |
| --- | --- | --- |
| The `CapabilityEvidence`/`FeatureCapability` DTOs and wire model base. | `WireModel`; `CapabilityEvidence`; `FeatureCapability` | mcp/src/agents_remember/serving/conversation/models.py:55-63; mcp/src/agents_remember/serving/conversation/models.py:655-659; mcp/src/agents_remember/serving/conversation/models.py:662-690 |
| The AR local-operator ruling and canonical scope the `repoPolicy` part reports. | `LocalOperatorAuthorizationResolver`; `for_workspace`; `resolve`; `require` | mcp/src/agents_remember/serving/conversation/authorization.py:69-105 |
| The `policyRead` capability gate. | `policyRead` | dashboard/src/data/conversation/types.ts:274-274 |
| The live snapshot `harnessMode` reads Claude `permissionMode` from. | `_harness_mode` | mcp/src/agents_remember/serving/conversation/control/policy.py:104-130 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-04T11:39:21+02:00 — 260731-EFA-L6 S18-B09 curator: reconciled the frozen-source ledger and repaired scoped citations; unsupported source claims were narrowed or removed, and the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 3 stale self-citations, all read back.
  The three single-line anchors each pointed at the blank line ABOVE their construct (a one-line
  shift, from the module docstring's re-wrap) and are now full spans: `PolicyPart` L35 → L36-L43,
  `ConversationPolicyProjection` L45 → L46-L55, `conversation_policy` L57 → L58-L101. cit:([`_harness_mode`], mcp/src/agents_remember/serving/conversation/control/policy.py:104-130),
  cit:([`_freshness`], mcp/src/agents_remember/serving/conversation/control/policy.py:133-134) and cit:([`_POLICY_ORIGIN`], mcp/src/agents_remember/serving/conversation/control/policy.py:33-33) were re-checked and still land on their own
  `def`/assignment. No claim text changed; every claim still holds.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The single
  `L406-L678` span into `conversation/models.py` no longer holds the material — the file grew to
  1282 lines and the two subjects are now far apart. Split it into the `WireModel` strict/frozen/
  camel-case base at L55-L63 and the `CapabilityEvidence` + `FeatureCapability` DTOs at L640-L675
  (including the `require_honest_state_evidence` validator and the R4 no-version-demotion note this
  card's 2026-07-21 entry describes). Read both ranges back.
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R4 version-gate removal — corrected the now-false
  "locked-version-mismatch reason" prose for Claude's `permissionMode`. `_harness_mode` carries the
  control-contract capability's `capability.reason`, which is contract-verification language
  ("unverified until the control seam is probed") and never a version-string comparison. Change
  uncommitted; closeout re-stamps verification.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the read-only policy
  projection — repoPolicy-vs-harnessMode separation with origin/evidence/freshness/reasons, Claude
  permissionMode with the locked-gate reason, and zero mutation surface. Verification is blank because
  the new source file is uncommitted; closeout owns its first source stamp.
