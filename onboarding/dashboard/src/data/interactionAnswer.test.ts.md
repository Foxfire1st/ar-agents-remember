# dashboard/src/data/interactionAnswer.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/interactionAnswer.test.ts`   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-01T09:38+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

The unit suite for the **interaction answer path**: kind classification, gate matching, the legacy gate answer POST, the structured
and permission direct-route round-trips, and the multiplexed sub-agent label pins. It pins that no
blind POST ever fires — the legacy path needs a matched open gate, the direct route needs a current
bridge epoch — and that no terminal code exists in the module at all. Fetch is stubbed per case
(`vi.stubGlobal`), unstubbed in `afterEach`.

## Code Commentary

### Logic

- **`lifecycleWithGate(overrides)`** cit:([`lifecycleWithGate`], dashboard/src/data/interactionAnswer.test.ts:30-56)
  `test/fixtures/wire.ts::lifecycleWithGate`: it names the gate `id`/`kind`/`state`/`ts` and the
  synchronizer-stamped `packet.adapterInteraction` identity, and takes the rest of the lifecycle and
  the rest of the gate as served default. Defaults = an open `agent-question` gate for
  `seat-1`/`ix-1`. It no longer closes with `as unknown as LifecycleProjection`, so the override
  object is checked against the mirror at this call site.
- **Kind-awareness (F8):** choices → `choices` mode with the validated view; no choices
  → `composer` mode; missing `interactionId` → `unrepresentable` whose reason names "cannot be
  answered" + "inspector" (never dead buttons); missing prompt stays answerable with the honest
  empty string; absent payload → null.
- **Gate matching:** matches the open `agent-question` gate by (sessionId,
  interactionId) across lifecycles; decided gates and non-question kinds are ignored. "Decided" is
  read from `gate.state`, never from `gate.decisions` — the fixture now inherits the served
  `["approve", "revise"]` decision vocabulary rather than the empty list it used to state, and the
  matcher does not look at it.
- **Delivery-failure honesty (M6):** `readAdapterDecisionFailure` parses the reopened
  gate's failure record defensively — no record / no `delivery` word → null.
- **Legacy round-trip (F7)** cit:(["POSTs the answer as the gate decision note on the approve verb", "keeps the server's words VERBATIM on failure", "states the poll-bounded truth when the gate has not been projected YET (seat has a lifecycle)", "says CANNOT (not 'retry in a moment') for a lifecycle-less seat — its gate never projects (review finding 2)"], dashboard/src/data/interactionAnswer.test.ts:172-195; dashboard/src/data/interactionAnswer.test.ts:197-217; dashboard/src/data/interactionAnswer.test.ts:219-232; dashboard/src/data/interactionAnswer.test.ts:234-250): the answer rides as the decision note on the approve
  verb — asserted against the EXACT URL and body (`/api/actions/approve`, `{target, gateId,
  note}`); a 409 failure keeps the server's words verbatim (`stale-gate` + detail); a missing gate
  with a lifecycle states the poll-bounded truth AND the fetch spy is never called — no blind
  POST; a lifecycle-less seat gets CANNOT (not "retry in a moment"), fetch never called (review
  finding 2 regression, fails on pre-fix code).
- **`stubDirectRoute(options)`** cit:([`stubDirectRoute`], dashboard/src/data/interactionAnswer.test.ts:257-295)
  submission-authority read, with scriptable epoch-mismatch and authority-failure modes.
- **Structured questions:** per-question pages from the additive top-level list
  AND the pre-fix runner's `raw.input.questions` fallback; an option-less question falls the whole
  payload back to `unrepresentable` (the all-or-nothing submit could never fire).
- **Session-direct route (no lifecycle required):** structured answers map and
  permission `response` POST to `/api/terminal/{session}/interaction-response` with the expected
  bridge epoch; epoch mismatch → cache cleared, one retry on the fresh epoch; an unavailable
  submission authority blocks the answer honestly — no blind POST.
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
| The module under test (representation + multiplex helpers, gate fallback, locked submit). | `representPendingInteraction`; `pendingInteractionPayloads`; `findInteractionGate`; `answerPendingInteraction`; `interactionAnswerIsLocked`; `submitInteractionAnswer` | dashboard/src/data/interactionAnswer.ts:136-184; dashboard/src/data/interactionAnswer.ts:208-223; dashboard/src/data/interactionAnswer.ts:258-274; dashboard/src/data/interactionAnswer.ts:449-481; dashboard/src/data/interactionAnswer.ts:484-490; dashboard/src/data/interactionAnswer.ts:504-618 |
| The matcher that decides "open agent-question gate" from `kind` and `state` alone. | `findInteractionGate` | dashboard/src/data/interactionAnswer.ts:258-274 |
| The local fixture reads the sampled projection into `SERVED`, selects a gate-bearing lifecycle as `SERVED_GATE`, and `BASE_GATE` copies that row's gate fields. | `SERVED`; `SERVED_GATE`; `BASE_GATE` | dashboard/src/test/fixtures/wire.ts:66-66; dashboard/src/test/fixtures/wire.ts:88-91; dashboard/src/test/fixtures/wire.ts:109-117 |
| The component suite covers exact URL/body handling, in-flight/retry states, structured questions, and multiplexed sub-agent approvals. | `stubDirectRoute`; "round-trip states (F7)"; "structured questions (260718-CHATS-L5I)"; "multiplexed sub-agent approvals" | dashboard/src/panels/session-cockpit/InteractionBar.test.tsx:114-244; dashboard/src/panels/session-cockpit/InteractionBar.test.tsx:298-323; dashboard/src/panels/session-cockpit/InteractionBar.test.tsx:325-480; dashboard/src/panels/session-cockpit/InteractionBar.test.tsx:482-521 |
| The projection types the gate fixture instantiates. | `LifecycleProjection`; `GateNode` | dashboard/src/types/projection.ts:217-227; dashboard/src/types/projection.ts:258-276 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

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
