# dashboard/src/data/interactionAnswer.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/interactionAnswer.test.ts`   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-09T19:36+02:00 |
| lastVerifiedCommitHash | `fb0296562ceb29929a3675a1b0195700d23bc56a`       |
| lastVerifiedCommitDate | 2026-08-09T20:35:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

The unit suite for the **single exact-session interaction answer path**: kind classification,
structured and scalar response bodies, lifecycle-free Codex MCP approvals, free-text delivery,
epoch refresh, retry, and multiplexed sub-agent label pins. It proves every representable vendor
interaction uses `/api/terminal/{session}/interaction-response`; no lifecycle gate or terminal
write exists in the answer module. Fetch is stubbed per case and unstubbed in `afterEach`.

## Code Commentary

### Logic

- **Kind-awareness (F8):** choices → `choices` mode with the validated view; no choices
  → `composer` mode; missing `interactionId` → `unrepresentable` whose reason names "cannot be
  answered" + "inspector" (never dead buttons); missing prompt stays answerable with the honest
  empty string; absent payload → null.
- **Delivery-failure honesty (M6):** `readAdapterDecisionFailure` parses the reopened
  gate's failure record defensively — no record / no `delivery` word → null.
- **`stubDirectRoute(options)`** cit:([`stubDirectRoute`], dashboard/src/data/interactionAnswer.test.ts:118-156)
  submission-authority read, with scriptable epoch-mismatch and authority-failure modes.
- **Structured questions:** per-question pages from the additive top-level list
  AND the pre-fix runner's `raw.input.questions` fallback; an option-less question falls the whole
  payload back to `unrepresentable` (the all-or-nothing submit could never fire).
- **Session-direct route (no lifecycle required):** structured `answers` maps and every scalar
  `response` POST to `/api/terminal/{session}/interaction-response` with the expected bridge epoch.
  The regression cases include the exact Codex MCP `accept`/`decline`/`cancel` choice shape and a
  free-text interaction on lifecycle-less seats. Epoch mismatch refreshes and retries once; an
  unavailable submission authority blocks honestly before a POST.
- **`pendingInteractionAgentLabel` pins:** the label is read from
  `raw.agentLabel` only — `undefined` for a missing `raw`, an empty `raw`, an absent payload, and
  a blank label; never fabricated.

### 2026-07-24 Curator Delta

The interaction suite now covers structured multi-question maps, direct permission responses,
lifecycle-free seats, epoch mismatch refresh-and-retry, and retained exact retry payloads.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module under test (representation, multiplex helpers, direct route, and locked submit). | `representPendingInteraction`; `pendingInteractionPayloads`; `interactionAnswerIsLocked`; `submitInteractionAnswer` | dashboard/src/data/interactionAnswer.ts:146-183; dashboard/src/data/interactionAnswer.ts:207-222; dashboard/src/data/interactionAnswer.ts:432-438; dashboard/src/data/interactionAnswer.ts:570-615 |
| The component suite covers exact URL/body handling, in-flight/retry states, structured questions, and multiplexed sub-agent approvals. | `stubDirectRoute`; "round-trip states (F7)"; "structured questions (260718-CHATS-L5I)"; "multiplexed sub-agent approvals" | dashboard/src/panels/session-cockpit/InteractionBar.test.tsx:95-242; dashboard/src/panels/session-cockpit/InteractionBar.test.tsx:296-321; dashboard/src/panels/session-cockpit/InteractionBar.test.tsx:323-478; dashboard/src/panels/session-cockpit/InteractionBar.test.tsx:480-519 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-09T19:36+02:00 — 260713-TES-L5F2: deleted the legacy gate fixtures and assertions;
  added lifecycle-free Codex MCP approval and free-text exact-session response regressions.

- 2026-08-04T15:58:25+02:00 — 260731-EFA-L6 S18-B12 curator: expanded the legacy F7 citation across its approve, stale-gate, no-blind-POST, and lifecycle-less refusal evidence while retaining the interaction source split.
- 2026-08-01T09:38+02:00 — 260731-EFA-L4 curator: every line range in the Logic section was stale by
  three lines — the diff against `abc7cbc` added a four-line import+comment block above
  `lifecycleWithGate` and removed one line from its body — so each bullet's range had slid off the
  block it names. Re-anchored all nine against the current 623-line source (`lifecycleWithGate`
  L27-L56, kind-awareness L67-L115, gate matching L117-L135, M6 L137-L169, legacy round-trip
  L171-L251, `stubDirectRoute` L257-L295, structured questions L297-L454, session-direct route
  L456-L605, `pendingInteractionAgentLabel` L607-L623). Rewrote the `lifecycleWithGate` bullet: it
  is now a wrapper over `test/fixtures/wire.ts::lifecycleWithGate` and no longer ends in
  `as unknown as LifecycleProjection`. Two residual data deltas checked rather than assumed — the
  gate fixture dropped its explicit `decisions: []` and inherits the served `["approve", "revise"]`,
  and the lifecycle is now a full served node (`state: "blocked"`, phase, tokens, `startedAt`)
  instead of a bare `{ id, gate }` — but `findInteractionGate` skips on
  `gate.kind !== "agent-question" || gate.state !== "open"` and then reads only
  `gate.packet.adapterInteraction`, and `answerPendingInteraction` POSTs `{target, gateId, note}`,
  so neither the "ignores decided gates" case (which drives `state: "approved"`) nor the exact-body
  assertion can see either delta. Recorded the `decisions` point in the gate-matching bullet because
  a reader would otherwise expect an empty list there.

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: documented the `pendingInteractionAgentLabel`
  pins (label from `raw.agentLabel` only; `undefined` for missing/blank/absent) and corrected the
  stale Purpose claim that the gate channel is the SOLE answer path — the L5I direct route has been
  pinned here since the 2026-07-24 delta. Refreshed every stale line citation to the current
  source. The L7 code is uncommitted in the code worktree; closeout re-stamps verification.

- 2026-07-24T13:17:50Z — Added direct interaction-route and structured-answer regression coverage.
  Verification hash/date remain pinned to the pre-commit source stamp.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R4/R9 (incl. fix round 1 finding 2): the
  10-case suite — kind matrix (choices/composer/unrepresentable/empty-prompt/null), open-gate
  matching, exact approve-verb URL+body, verbatim 409 words, no-blind-POST, and the NOT-YET vs
  CANNOT copy split for lifecycle-less seats. Verification metadata pinned to the leaf base until
  closeout stamps the L6 code commit.
