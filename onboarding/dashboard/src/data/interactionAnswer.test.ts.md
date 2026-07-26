# dashboard/src/data/interactionAnswer.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/interactionAnswer.test.ts`   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-26T15:40+0200 |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f`       |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
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

- **`lifecycleWithGate(overrides)`** (L26-L62) — builds a `LifecycleProjection` carrying one gate
  with the synchronizer-stamped `packet.adapterInteraction` identity; defaults = an open
  `agent-question` gate for `seat-1`/`ix-1`.
- **Kind-awareness (F8)** (L64-L112): choices → `choices` mode with the validated view; no choices
  → `composer` mode; missing `interactionId` → `unrepresentable` whose reason names "cannot be
  answered" + "inspector" (never dead buttons); missing prompt stays answerable with the honest
  empty string; absent payload → null.
- **Gate matching** (L114-L132): matches the open `agent-question` gate by (sessionId,
  interactionId) across lifecycles; decided gates and non-question kinds are ignored.
- **Delivery-failure honesty (M6)** (L134-L166): `readAdapterDecisionFailure` parses the reopened
  gate's failure record defensively — no record / no `delivery` word → null.
- **Legacy round-trip (F7)** (L168-L252): the answer rides as the decision note on the approve
  verb — asserted against the EXACT URL and body (`/api/actions/approve`, `{target, gateId,
  note}`); a 409 failure keeps the server's words verbatim (`stale-gate` + detail); a missing gate
  with a lifecycle states the poll-bounded truth AND the fetch spy is never called — no blind
  POST; a lifecycle-less seat gets CANNOT (not "retry in a moment"), fetch never called (review
  finding 2 regression, fails on pre-fix code).
- **`stubDirectRoute(options)`** (L254-L292) — the fetch stub for the session-direct route and the
  submission-authority read, with scriptable epoch-mismatch and authority-failure modes.
- **Structured questions** (L294-L451): per-question pages from the additive top-level list
  AND the pre-fix runner's `raw.input.questions` fallback; an option-less question falls the whole
  payload back to `unrepresentable` (the all-or-nothing submit could never fire).
- **Session-direct route (no lifecycle required)** (L453-L602): structured answers map and
  permission `response` POST to `/api/terminal/{session}/interaction-response` with the expected
  bridge epoch; epoch mismatch → cache cleared, one retry on the fresh epoch; an unavailable
  submission authority blocks the answer honestly — no blind POST.
- **`pendingInteractionAgentLabel` pins** (L604-L620): the label is read from
  `raw.agentLabel` only — `undefined` for a missing `raw`, an empty `raw`, an absent payload, and
  a blank label; never fabricated.

### 2026-07-24 Curator Delta

The interaction suite now covers structured multi-question maps, direct permission responses,
lifecycle-free seats, epoch mismatch refresh-and-retry, and retained exact retry payloads.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module under test (representation + multiplex helpers, gate fallback, locked submit). | L136-L246; L449-L481; L504-L618 | [interactionAnswer.ts](interactionAnswer.ts) |
| The exact-URL/body and in-flight/retry cases at the component level (incl. the multiplex suite on the shared fixture). | — | [../panels/session-cockpit/InteractionBar.test.tsx](../panels/session-cockpit/InteractionBar.test.tsx) |
| The projection types the gate fixture instantiates. | — | [../types/projection.ts](../types/projection.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

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
