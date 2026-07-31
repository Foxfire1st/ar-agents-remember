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

`ConversationPolicyProjection` (L46-L55) carries two `PolicyPart` (L36-L43) DTOs — the AR `repoPolicy`
posture and the effective `harnessMode` — each with state/origin/evidence/freshness/reasons.
`conversation_policy` (L58-L101) resolves the caller and epoch, reads the live snapshot, and builds both
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
| The `CapabilityEvidence`/`FeatureCapability` DTOs and wire model base. | L55-L63; L640-L675 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The AR local-operator ruling and canonical scope the `repoPolicy` part reports. | L48-L105 | [authorization.py](agents-remember/mcp/src/agents_remember/serving/conversation/authorization.py) |
| The `policyRead` capability gate. | L305-L321 | [capabilities.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/capabilities.py) |
| The live snapshot `harnessMode` reads Claude `permissionMode` from. | L1-L120 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 3 stale self-citations, all read back.
  The three single-line anchors each pointed at the blank line ABOVE their construct (a one-line
  shift, from the module docstring's re-wrap) and are now full spans: `PolicyPart` L35 → L36-L43,
  `ConversationPolicyProjection` L45 → L46-L55, `conversation_policy` L57 → L58-L101. `_harness_mode`
  (L104), `_freshness` (L133) and `_POLICY_ORIGIN` (L33) were re-checked and still land on their own
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
