# dashboard/src/panels/session-cockpit/InteractionBar.test.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The jsdom InteractionBar suite: kind-awareness, the single exact-session answer path,
the full round-trip — answering… → verbatim error + retry | answered-waiting — and (review R6)
the multiplexed sub-agent approval chrome: one bar per pending
payload, agent badge, cross-slot channel routing, and sibling round-trip isolation. The bar has no
terminal dependency by construction, so xterm never appears here.

## Code Commentary

### Logic

- **Kind-awareness (F8)**: choices render one button per choice + kind chip + the
  honesty hint; non-choice kinds mark the composer (`data-answer-mode`) with the exact-session
  label; unrepresentable payloads say so with ZERO dead buttons; no pending interaction ⇒
  renders nothing.
- **Round-trip (F7)**: a deferred-promise fetch pins the in-flight `answering…` + disabled buttons
  before release → "answered — waiting" with the poll-bounded copy. A direct-route failure keeps
  the server's words verbatim and retry re-sends the SAME `response` body. A lifecycle-less choice
  and composer text both assert the exact `/api/terminal/{session}/interaction-response` URL —
  never `/submit` or `/api/actions/approve`.
- **Stale round-trip state (review finding 5)**: a pre-seeded "answered" record on
  the seat + a FOLLOWING unrepresentable payload ⇒ the store record clears and no answered line
  renders (fails on the old guard that skipped `interactionId === undefined`).
- **Focus + announce**: appearance never steals focus (outside button keeps it) and
  the `role="alert"` region carries the prompt; unmount while holding focus returns it to the
  invoker.
- **Multiplexed sub-agent approvals (review R6)**: over the
  `L7_MULTIPLEXED_INTERACTIONS` fixture — two bars render (parent first, UNBADGED; the agent bar
  badged `agent agent-t` from the adapter-bound `raw.agentLabel`), answering the AGENT bar POSTs
  `{interactionId: "ix_l7_agent", expectedBridgeEpoch: "ep-1", response: "allow"}` through the
  existing session-direct channel, and the parent's bar never shows the agent's
  inflight/answered state.

  cit:(["choice kinds render one button per choice + the kind chip + the honesty hint", "non-choice kinds mark the composer as the direct answer input", "unrepresentable kinds say so honestly — no dead buttons", "renders nothing when no interaction is pending"], dashboard/src/panels/session-cockpit/InteractionBar.test.tsx:56-93)
  cit:(["answering… disables the buttons in flight, then lands on answered — waiting", "POST failure renders the verbatim error and retry re-sends the SAME answer", "a lifecycle-less choice still POSTs to its exact session", "composer answer-mode routes text to the exact session, NOT /submit"], dashboard/src/panels/session-cockpit/InteractionBar.test.tsx:95-204)
  cit:(["clears a previous 'answered — waiting' before a FOLLOWING unrepresentable interaction renders"], dashboard/src/panels/session-cockpit/InteractionBar.test.tsx:245-265)
  cit:(["never steals focus on appearance and announces via an assertive region", "returns focus to the invoker when the bar clears while holding focus"], dashboard/src/panels/session-cockpit/InteractionBar.test.tsx:269-278; dashboard/src/panels/session-cockpit/InteractionBar.test.tsx:280-289)
  cit:(["renders one bar per pending interaction — parent first, agent badged", "answers the AGENT approval through the existing interaction-response channel"], dashboard/src/panels/session-cockpit/InteractionBar.test.tsx:483-498; dashboard/src/panels/session-cockpit/InteractionBar.test.tsx:500-518)

### Invariants And Boundaries

Fetch is stubbed per case (`vi.unstubAllGlobals` in afterEach); stores reset in beforeEach; the
URL/body assertions are the regression net against any drift toward a terminal/queue write.
Test-only.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- The component under test (multiplexing fan-out + per-payload bar). [1]
- The answer path + cross-slot exact-session routing the suite exercises end-to-end. [2]
- The `L6_INTERACTION_*` fixtures (choices / freetext / unrepresentable). [3]
- The `L7_MULTIPLEXED_INTERACTIONS` fixture (parent in both slots + the `agent agent-t` approval). [4]
- The copy constants asserted verbatim (honesty hint). [5]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

## Reliable Submit Delta

The suite drives the shared composer handle across the interaction kind matrix and proves exact
session-owned round trips, lifecycle-free choice delivery, retained failed-answer text/revision,
newer-draft preservation, focus changes, and stale-interaction rejection. It asserts that neither
`/submit` nor a lifecycle gate is an answer fallback.

## Current Structured-Interaction Maintenance

The interaction tests cover separate question option groups, multi-select confirmation, progress and
recorded-answer copy, all-or-nothing direct submission, and the retained honest fallback forms.
