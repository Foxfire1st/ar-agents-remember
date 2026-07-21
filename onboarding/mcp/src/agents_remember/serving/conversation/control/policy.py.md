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

`ConversationPolicyProjection` (L45) carries two `PolicyPart` (L35) DTOs — the AR `repoPolicy`
posture and the effective `harnessMode` — each with state/origin/evidence/freshness/reasons.
`conversation_policy` (L57) resolves the caller and epoch, reads the live snapshot, and builds both
parts plus the `policyRead` capability. `_harness_mode` (L104) reports Claude's `permissionMode` from
the live snapshot carrying the control-contract capability's own `capability.reason` — since
260718-CHATS-L5F R4 that reason is contract-verification language ("unverified until the control seam
is probed"), NEVER a locked-version-mismatch string; codex approval/sandbox values are adapter-private
at thread/turn start and never cross (honestly unverified); pi has no built-in permission-popup
surface. `_freshness` (L133) stamps the observed-time window. `_POLICY_ORIGIN` (L33) is the AR
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The policy DTOs and capability evidence live in the contract; the AR posture comes from the L0
authorization ruling; the harness mode reads the live snapshot.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The `CapabilityEvidence`/`FeatureCapability` DTOs and wire model base. | L406-L678 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The AR local-operator ruling and canonical scope the `repoPolicy` part reports. | L48-L105 | [authorization.py](agents-remember/mcp/src/agents_remember/serving/conversation/authorization.py) |
| The `policyRead` capability gate. | L301-L316 | [capabilities.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/capabilities.py) |
| The live snapshot `harnessMode` reads Claude `permissionMode` from. | L1-L120 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R4 version-gate removal — corrected the now-false
  "locked-version-mismatch reason" prose for Claude's `permissionMode`. `_harness_mode` carries the
  control-contract capability's `capability.reason`, which is contract-verification language
  ("unverified until the control seam is probed") and never a version-string comparison. Change
  uncommitted; closeout re-stamps verification.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the read-only policy
  projection — repoPolicy-vs-harnessMode separation with origin/evidence/freshness/reasons, Claude
  permissionMode with the locked-gate reason, and zero mutation surface. Verification is blank because
  the new source file is uncommitted; closeout owns its first source stamp.
