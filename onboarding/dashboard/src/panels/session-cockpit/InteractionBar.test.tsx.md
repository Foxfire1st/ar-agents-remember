# dashboard/src/panels/session-cockpit/InteractionBar.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/InteractionBar.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-01T10:40+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The jsdom InteractionBar suite: kind-awareness, the gate-only answer path,
the full round-trip — answering… → verbatim error + retry | answered-waiting — and (review R6)
the multiplexed sub-agent approval chrome: one bar per pending
payload, agent badge, cross-slot channel routing, and sibling round-trip isolation. The bar has no
terminal dependency by construction, so xterm never appears here.

## Code Commentary

### Logic

- **`projectGate` helper** (L27-L44): seeds `dashboardStore.lifecycles` with an open
  `agent-question` gate carrying the REAL packet shape
  (`packet.adapterInteraction.{sessionId,interactionId}`) — the exact stamp
  `hosted_interactions.py` writes. Since 260731-EFA-L4 it builds that through
  `lifecycleWithGate(…)` (`test/fixtures/wire.ts`) instead of an
  `{ id, gate } as unknown as LifecycleProjection` cast, so the seeded lifecycle is a shape the
  mirror can produce and a packet field the mirror does not declare fails `tsc -b` here. The gate
  still sets `decisions: []` explicitly.
- **Kind-awareness (F8)** (L75-L112): choices render one button per choice + kind chip + the
  honesty hint; non-choice kinds mark the composer (`data-answer-mode`) with the gate-channel
  label; unrepresentable payloads say so with ZERO dead buttons; no pending interaction ⇒
  renders nothing.
- **Round-trip (F7)** (L114-L244): a deferred-promise fetch pins the in-flight `answering…` +
  disabled buttons before release → "answered — waiting" with the poll-bounded copy; the
  500-with-body case asserts the VERBATIM server words and that retry re-sends the SAME body
  (captured fetch bodies compared — `note: "deny"` twice); the missing-gate case proves NO blind
  POST (fetch spy never called) and poll-bounded copy; composer answer-mode asserts the EXACT
  URL + body (`/api/actions/approve`, `{target, gateId, note}`) — never /submit.
- **Stale round-trip state (review finding 5)** (L246-L268): a pre-seeded "answered" record on
  the seat + a FOLLOWING unrepresentable payload ⇒ the store record clears and no answered line
  renders (fails on the old guard that skipped `interactionId === undefined`).
- **Focus + announce** (L270-L292): appearance never steals focus (outside button keeps it) and
  the `role="alert"` region carries the prompt; unmount while holding focus returns it to the
  invoker.
- **Multiplexed sub-agent approvals (review R6)** (L482-L521): over the
  `L7_MULTIPLEXED_INTERACTIONS` fixture — two bars render (parent first, UNBADGED; the agent bar
  badged `agent agent-t` from the adapter-bound `raw.agentLabel`), answering the AGENT bar POSTs
  `{interactionId: "ix_l7_agent", expectedBridgeEpoch: "ep-1", response: "allow"}` through the
  existing session-direct channel, and the parent's bar never shows the agent's
  inflight/answered state.

### Invariants And Boundaries

Fetch is stubbed per case (`vi.unstubAllGlobals` in afterEach); stores reset in beforeEach; the
URL/body assertions are the regression net against any drift toward a terminal/queue write.
Test-only.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test (multiplexing fan-out + per-payload bar). | L242-L281, L283-L525 | [InteractionBar.tsx](InteractionBar.tsx) |
| The answer path + cross-slot channel routing the suite exercises end-to-end. | L449-L640, L533 | [../../data/interactionAnswer.ts](../../data/interactionAnswer.ts) |
| The `L6_INTERACTION_*` fixtures (choices / freetext / unrepresentable). | L205-L256 | [../../test/fixtures/catalogRows.ts](../../test/fixtures/catalogRows.ts) |
| The `L7_MULTIPLEXED_INTERACTIONS` fixture (parent in both slots + the `agent agent-t` approval). | L411-L446 | [../../test/fixtures/catalogRows.ts](../../test/fixtures/catalogRows.ts) |
| The copy constants asserted verbatim (honesty hint). | L54-L71 | [lifecycleCopy.ts](lifecycleCopy.ts) |
| `lifecycleWithGate` — the typed builder `projectGate` now seeds through, and the `BASE_LIFECYCLE`/`BASE_GATE` bases it spreads. | L98-L120; L252-L262 | [../../test/fixtures/wire.ts](../../test/fixtures/wire.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## Reliable Submit Delta

The suite now drives the shared composer handle across the interaction kind matrix and proves one
exact gate round trip, retained failed-answer text/revision, newer-draft preservation, focus changes,
and stale-interaction rejection. It asserts that `/submit` is not an answer fallback.

## Current Structured-Interaction Maintenance

The interaction tests cover separate question option groups, multi-select confirmation, progress and
recorded-answer copy, all-or-nothing direct submission, and the retained honest fallback forms.

## Update History

- 2026-08-01T10:40+02:00 — 260731-EFA-L4 curator: the only source change is `projectGate` swapping an
  `{ id, gate } as unknown as LifecycleProjection` cast for `lifecycleWithGate(…)`, so the helper
  bullet now says where the seed comes from and the `L20-L45` range was repaired to `L27-L44`, which is
  where the function actually opens and closes. I verified the swap is behaviour-neutral before saying
  so: the seeded lifecycle now inherits `BASE_LIFECYCLE` (`state: "blocked"`, `phase`, `tokens: 1200`,
  timestamps), but every case in this suite routes through the GATE — `packet.adapterInteraction` and
  `gate.state === "open"` — and no assertion reads a lifecycle field other than the gate; the gate
  itself still sets `decisions: []` explicitly, so `BASE_GATE`'s served `["approve","revise"]` never
  applies, which is the one residual that could have changed an answer body. `git diff -U2` shows no
  field value inside the literal changed. Suite re-run: all cases pass. Also repaired
  `Focus + announce` `L270-L296` → `L270-L292` (the describe closes at 292; 293+ is other content) and
  added one reference row for the builder.

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: recorded the "multiplexed sub-agent approvals"
  suite (review R6) over the new `L7_MULTIPLEXED_INTERACTIONS` fixture — two bars (parent
  unbadged, agent badged `agent agent-t`), the AGENT bar's answer POSTing
  `{interactionId: "ix_l7_agent", expectedBridgeEpoch: "ep-1", response: "allow"}` through the
  existing session-direct channel, and the parent bar never inheriting the agent's round-trip
  state. Refreshed stale suite-citation ranges shifted by earlier leaves. Source uncommitted;
  closeout re-stamps verification.

- 2026-07-24T13:17:17Z — Curator: recorded structured-interaction rendering and answer-routing
  regression coverage; verification fields remain pre-commit.

- 2026-07-17T21:39+02:00 — FEUI-L5: added shared answer-mode, exact retry, revision, and sole-
  channel regression coverage.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R4/R9 (13 cases): kind-awareness incl. the
  honest unrepresentable fallback, the exact-URL/body gate-channel assertions, the deferred
  in-flight disable, verbatim-error + same-answer retry, the no-blind-POST missing-gate case,
  the finding-5 stale-answered clear before a following unrepresentable payload, and the
  no-steal/return focus + assertive announce cases. Verification metadata pinned to the leaf
  base until closeout stamps the L6 code commit.
