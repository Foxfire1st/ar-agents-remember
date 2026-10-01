# mcp/src/agents_remember/serving/conversation/control/policy.py

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
surface. cit:([`_freshness`], mcp/src/agents_remember/serving/conversation/control/policy.py:139-140) stamps the observed-time window. cit:([`_POLICY_ORIGIN`], mcp/src/agents_remember/serving/conversation/control/policy.py:39-39) is the AR
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

## Evidence

### Docs References

No Domain Documentation source is configured; the policy contract is repository-owned.

No configured domain documentation was available.

### Repo-Internal References

The policy DTOs and capability evidence live in the contract; the AR posture comes from the L0
authorization ruling; the harness mode reads the live snapshot.

- The `CapabilityEvidence`/`FeatureCapability` DTOs and wire model base. [1]
- The AR local-operator ruling and canonical scope the `repoPolicy` part reports. [2]
- The `policyRead` capability gate. [3]
- The live snapshot `harnessMode` reads Claude `permissionMode` from. [4]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.
