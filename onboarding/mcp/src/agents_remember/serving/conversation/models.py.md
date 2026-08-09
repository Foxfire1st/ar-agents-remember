# mcp/src/agents_remember/serving/conversation/models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash |  `7af76249ff1aa728d34a6e81c5f09c8bcb797484`|
| lastVerifiedCommitDate | 2026-08-09T02:17:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation contract overview](overview.md)

## Purpose

Owns the stable, strict, native-authoritative wire grammar shared by active conversation reads,
dormant native history, operation/control projection, browser consumers, and orchestration. The
module represents truth and rejects contradictory authority products; it is not a projector,
history store, or control service.

## Code Commentary

### 260731-EFA-L4 Current Delta — Six Fields That Could Not Validate Their Own Output

Four models declared six fields as **required and nullable** while the serializers that emit
them dump with `exclude_none=True` — so a `None` was DROPPED from the wire and the model could
not validate its own emitted body. The response conformance suite found it the moment those
routes started declaring these models. All six gained `= None` defaults:

| Model | Fields | Line |
| --- | --- | --- |
| `StatusFreshness` | `last_evidence_at`, `age_ms` | L473-L474 |
| `ConversationTurnStatus` | `turn_id`, `state_since` | L505-L506 |
| `ConversationEventEnvelope` | `previous_cursor` | L641 |
| `ConversationPageWindow` | `older_cursor` | L760 |

**No bytes moved.** The absent key already meant exactly this `None`; the fix is that the model
now says so. `age_ms` keeps its `ge=0` bound (`Field(default=None, ge=0)`), so the default is
additive to the constraint, not a replacement for it.

**Why only these six, and not every nullable field in the module:** the two serializers differ
on purpose. `active/api._dump` and `control/api._dump` both use
`model_dump(mode="json", by_alias=True, exclude_none=True)`, while `library/api._dump`
deliberately does **not** exclude nulls — "null is meaningful on this wire (nextCursor /
olderCursor / identity absence is contract-significant)". Fields reached only by the library
serializer, such as `ConversationLibraryPage.next_cursor` and
`HistoricalConversationPage.older_cursor` cit:(["class HistoricalConversationPage"], mcp/src/agents_remember/serving/conversation/_models_status.py:422-422), are therefore correct as required-and-nullable
and were deliberately left alone. The six above are the ones the exclude-none serializers reach.

This entry supersedes any earlier description in this sidecar that conflicts with the current
source behavior above; verification metadata stays pinned to the pre-commit source history until
closeout.

### Logic

- `WireModel` makes public DTOs immutable, camel-case on the wire, and closed to unknown fields.
- Purpose-prefixed opaque types keep active-page, active-event, library-list, library-read,
  library-key, private native-resume, and SHA-256 operation identities non-interchangeable.
- Conversation items carry stable ids, monotonic revisions/global ordinals, typed content blocks,
  explicit lane/source/producer provenance, and unknown-vendor/input evidence.
- Harness sub-agent grammar: cit:(["class ConversationAgentRef(WireModel):"], mcp/src/agents_remember/serving/conversation/_models_blocks.py:137-137) labels
  the sub-agent one timeline item belongs to via the additive optional `ConversationItem.agent`
  field (L371); absent means the parent conversation. Identity is evidence-bound — codex
  `agentThreadId` (plus `agentPath`/`nickname`/`role` once collab evidence binds them), claude
  `agentId`/`subagent_type` joined through the spawning tool call (`join_key` =
  `parent_tool_use_id`) — and `status` cit:(["export function isTerminalAgentStatus(status: ConversationAgentStatus): boolean {"], dashboard/src/data/conversation/agents.ts:41-41) tracks the agent's
  own lifecycle, not the item's phase.
- Library sub-agent grouping: cit:(["class ConversationLibraryAgentRow(WireModel):"], mcp/src/agents_remember/serving/conversation/_models_status.py:375-375) is one
  sub-agent conversation grouped under its parent row's `agents` tuple (L804); it opens through
  its own `conversation_key` exactly like a top-level row. `ConversationLibraryPage.agents_note`
  cit:(["agents_note:"], mcp/src/agents_remember/serving/conversation/_models_status.py:419-419) carries capability honesty: the exact native reason sub-agent conversations are
  (partially) unavailable on a page, never silently absent.
- Status models fix the evidence-to-turn-state vocabulary and validate waiting and terminal
  cross-products; unknown evidence cannot establish ready.
- Capability models require exact evidence products. `FeatureCapability` carries a documenting NOTE
  cit:(["class FeatureCapability"], mcp/src/agents_remember/serving/conversation/_models_status.py:262-262) that there is deliberately
  NO `for_observed_runtime` version-demotion: the contract is the only gate, a capability is never
  demoted because an installed runtime/helper version drifts from a fixture's captured version, and
  the runtime/helper version survives on `CapabilityEvidence` as informational metadata only.
- Page/event models carry cursor continuity and explicit gap/repage semantics.
- Open, interrupt, queue, withdrawal, attachment, telemetry, and runtime-fixture DTOs validate the
  full semantic product rather than relying on callers to combine individually valid fields.
- `operation_fingerprint` hashes canonical immutable request identity plus authorization without
  retaining raw request content.

### Conventions

This is intentionally a declaration-heavy single contract owner. Use literal discriminators and
Pydantic validators for intrinsic cross-field authority. Add production behavior in focused service
modules behind these types, not in this file.

### Invariants And Boundaries

- Cursor/token brands, authorization, identity/scope, generations, revisions, and ordinals are
  authority boundaries, not decorative typing.
- Exact producer/lane/strength products are required for cockpit, durable bus, controlled-terminal,
  interaction, and control sources. Unknown input stays native-only/unknown and producer-free.
- Supported or partial capability states require runtime-fixture evidence and a fixture id;
  fixture evidence itself has `enablesCapabilities=false`.
- Open identity and catalog proof must agree exactly. No-launch results cannot carry identities;
  identity-bearing failures require phase-matching explicit rollback.
- Only queued cockpit work exposes withdrawal identity. Raw draft and attachment recovery exist
  only in the authoritative successful withdrawal response.
- Metrics always retain scope, freshness, precision, runtime, and evidence origin.
- Sub-agent identity is never fabricated: unresolved identity renders as
  `agent <short-id>`, both on item refs and library rows, and agent/library identity fields are
  populated only from native evidence. When sub-agent conversations are unavailable on a library
  page, `agents_note` must carry the exact native reason — absence stays explicit, never silent.
- **A model must be able to validate its own emitted body.** Required-and-nullable is only
  correct for fields reached by the library serializer, which keeps nulls on the wire. Anything a
  route dumps with `exclude_none=True` must be nullable AND defaulted, or the model rejects the
  very payload it produced — the failure mode `260731-EFA-L4` found in six fields across four
  models.

### Todos

If this declaration module grows with behavior, split that behavior behind a stable models facade;
do not fragment the accepted wire vocabulary prematurely.

## Docs References

No Domain Documentation source is configured. The repository-owned hostile contract matrix is the
authoritative behavioral evidence for this internal grammar.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Hostile tests cover cursor purpose, provenance, status, capability, identity/rollback, recovery, attachment, metrics, and fixture products. | `test_cursor_bindings_preserve_authorization_identity_scope_and_purpose` | mcp/tests/test_conversation_contracts.py:196-220 |
| Foundation tests prove the types participate in exactly two ports and that installed runtime fixtures are allowlisted evidence, never enablement. | `test_installed_runtime_fixtures_are_allowlisted_evidence_not_enablement` | mcp/tests/test_conversation_foundation.py:163-188 |
| The two read protocols consume these normalized models without owning control behavior. | "class ConversationLibraryPort" | mcp/src/agents_remember/serving/conversation/ports.py:59-59 |
| The `active/api` serializer emits `exclude_none=True`, which drops the six required-and-nullable fields' nulls. | "page.model_dump" | mcp/src/agents_remember/serving/conversation/active/api.py:155-155 |
| The `control/api` serializer emits `exclude_none=True`, which drops the six required-and-nullable fields' nulls. | "model.model_dump" | mcp/src/agents_remember/serving/conversation/control/api.py:147-147 |
| The `library/api` serializer deliberately keeps nulls (`model_dump(mode="json", by_alias=True)` without `exclude_none`). | "value.model_dump" | mcp/src/agents_remember/serving/conversation/library/api.py:316-316 |
| The declarations that made these models the routes' stated contract. | "class WireResponse" | mcp/src/agents_remember/serving/response_contract.py:88-88 |
| The suite that drove the real bodies through them. | "class ServingRouteInventoryTests" | mcp/tests/test_serving_response_conformance.py:500-500 |

## Cross-Repo References

No cross-repository implementation governs these contracts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: now a facade over the `_models_{blocks,operations,status,telemetry,wire}.py` modules; full surface re-exported and pinned. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B22 curator: replaced the superseded
  `(L…)` prose citations (Logic + retained history entries) and the `n/a` table rows with
  exact anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-08-01T09:02+02:00 — 260731-EFA-L4 curator: recorded the six fields that gained `= None`
  defaults across four models — `StatusFreshness.last_evidence_at`/cit:(["age_ms: int | None = Field(default=None, ge=0)"], mcp/src/agents_remember/serving/conversation/_models_status.py:71-71),
  `ConversationTurnStatus.turn_id`/cit:([`state_since`], mcp/src/agents_remember/serving/conversation/_models_status.py:103-103),
  `ConversationEventEnvelope.previous_cursor` cit:(["previous_cursor:"], mcp/src/agents_remember/serving/conversation/_models_status.py:240-240), `ConversationPageWindow.older_cursor`
  cit:(["class ConversationPageWindow"], mcp/src/agents_remember/serving/conversation/_models_status.py:354-354) — and why: declared required-and-nullable while `active/api._dump` and
  `control/api._dump` emit with `exclude_none=True`, so the null was dropped and the model could
  not validate its own body. Recorded the deliberate asymmetry that scopes the fix —
  `library/api._dump` keeps nulls, so `HistoricalConversationPage.older_cursor` cit:(["class HistoricalConversationPage"], mcp/src/agents_remember/serving/conversation/_models_status.py:422-422) and
  `ConversationLibraryPage.next_cursor` are correct as-is — and added it as an invariant. No wire
  bytes moved; the absent key already meant this `None`. Re-derived the 4 in-file citations the
  leaf's 20 added comment lines shifted: the `FeatureCapability` NOTE L670-L675 → L685-L690,
  `ConversationLibraryAgentRow` L755-L774 → L775-L794, `ConversationLibraryRow.agents` L784 →
  L804, and `ConversationLibraryPage.agents_note` L797-L799 → L817-L819. The three sub-agent
  grammar citations (L311-L313, L316-L334, L371) sit above every edit and were re-verified
  unchanged. Verification metadata pinned until closeout stamps the L4 commit.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: re-anchored this card's in-file citations, which
  the same leaf's `ruff format` pass invalidated. Collapsing a dozen wrapped `Literal`/`Mapping`/
  `ClassVar` declarations back onto single lines (and deleting the dead `# noqa` comments recorded
  in the entry below) shortened the module by 23 lines, moving every declaration the sub-agent and
  capability bullets point at: `ConversationAgentStatus` L315-L317 → L311-L313,
  `ConversationAgentRef` L320-L338 → L316-L334, `ConversationItem.agent` L375 → L371, the
  `FeatureCapability` NOTE L680-L685 → L670-L675, `ConversationLibraryAgentRow` L765-L784 →
  L755-L774, `ConversationLibraryRow.agents` L794 → L784, and `ConversationLibraryPage.agents_note`
  L807-L809 → L797-L799. Each declaration is otherwise byte-identical, so no claim about the wire
  grammar itself changed — only where to find it.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: the only non-format change here is a lint-suppression cleanup — the `# noqa: UP040` suppressions on the `ConversationContentBlock` / `ConversationMutation` / `WithdrawQueueResponse` / `ComposerSubmitBlock` type aliases and the `# noqa: UP046` on `MetricEvidence` were deleted, because `[tool.ruff] target-version` is now pinned to the supported floor `py311` and those PEP 695 upgrade rules no longer fire. The declarations themselves are byte-identical. Nothing else in the file changed, so no other claim in this sidecar can have been invalidated by this leaf. Attested, deliberately not rewritten.
- 2026-07-26T15:34 — 260718-CHATS-L7: harness sub-agents became first-class wire participants.
  Code added `ConversationAgentStatus` cit:(["ConversationAgentStatus = Literal["], mcp/src/agents_remember/serving/conversation/_models_blocks.py:132-132) and `ConversationAgentRef` cit:(["class ConversationAgentRef(WireModel):"], mcp/src/agents_remember/serving/conversation/_models_blocks.py:137-137) with
  the additive `ConversationItem.agent` field (L375), cit:(["class ConversationLibraryAgentRow(WireModel):"], mcp/src/agents_remember/serving/conversation/_models_status.py:375-375)
  with `ConversationLibraryRow.agents` cit:(["class ConversationLibraryRow"], mcp/src/agents_remember/serving/conversation/_models_status.py:397-397), and `ConversationLibraryPage.agents_note`
  cit:(["agents_note:"], mcp/src/agents_remember/serving/conversation/_models_status.py:419-419). Sidecar: documented the evidence-bound, never-fabricated sub-agent identity
  grammar and the capability-honesty `agents_note`; fixed the stale L5F NOTE citation
  (L653-L658 → L680-L685); corrected the foundation-test citation (L102-L137 pointed at the
  registration/lock tests, not fixture non-promotion → L162-L176) and the contracts range end
  (L1185 → L1182). Uncommitted; closeout re-stamps verification.
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: version-gate REMOVAL (developer ruling
  2026-07-21, R4). Corrected the now-false "demote mismatched runtime/helper versions" claim:
  `FeatureCapability.for_observed_runtime` is removed; a documenting NOTE cit:(["class FeatureCapability"], mcp/src/agents_remember/serving/conversation/_models_status.py:262-262) records the
  deliberate absence and the contract-only gate; the runtime/helper version is informational
  `CapabilityEvidence` metadata only. Uncommitted; closeout re-stamps verification.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the contract sidecar after same-reviewer
  PASS closed six authority findings. Verification is blank until closeout commits and stamps the
  new source.
