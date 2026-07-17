# dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **failed-launch banner** (260715-FEUI-L3 R6): the runner INTENTIONALLY keeps a refused launch
addressable — the row is never hidden — so the banner renders the sweep-projected refusal
VERBATIM beside the retained pair at tier 'refused', with exactly two actions: Retire (an honest
armed confirm naming the session and its leaf) and 'Launch corrected…' (the LaunchFlow pre-filled
from the refused pair). NEVER an auto-retry — the component holds ZERO timers and ZERO effects
(reviewer-verified) and sends nothing unprompted. Uniform across ALL THREE native harnesses: the
refusal path is identical for Claude, Codex, and Pi (the async fail-loud invariant). Mounted by
SessionsView for any focused seat with `controlState === "failed"`, above the pty surface.

## Code Commentary

### Logic

- **Verbatim refusal** (L81, L103-L105): `verbatimBridgeError(session.controlRaw)` — a string
  bridgeError renders untouched (the server's wording names the advertised alternatives);
  non-string shapes are serialized, never reworded; ABSENCE is stated ("no bridgeError retained —
  see the session terminal for the runner log"), never invented.
- **Refused pair** (L82, L106-L116): the retained `resolvedModel`/`resolvedEffort` render labeled
  "(requested provenance — never validated)" beside an `EvidenceBadge tier="refused" showWord`
  in the headline (L100); a pairless failed row states "no selection was sent (vendor defaults) —
  the failure is the runner's own refusal".
- **Retire** (L84-L95, L117-L126, L146-L179): the `retire…` button only ARMS the inline confirm;
  the confirm names the session label and its leaf (`leafIdFromKey`, L148-L152) — the honest
  naming the leaf demands. Confirming sends ONE `terminateTerminalSession(session.id)` POST
  (retire = the operator terminate route: `/api/terminal/{id}/retire` requires the retiring
  seat's OWN `actor_session`, which the dashboard operator does not have — worker decision 6,
  reviewer-verified as genuinely unusable from this surface; the resulting `terminated` status
  renders as the grammar's "retired". Provenance-recording retires need an upstream operator
  actor-identity decision — logged as an upstream ask). A failed terminate states "the server did
  not confirm; the row is unchanged" (L89-L92); success re-hydrates the catalog. `keep` disarms
  and sends nothing.
- **Launch corrected…** (L127-L143): hands `{harness, modelKey, effort}` from the refused pair to
  `onLaunchCorrected` — SessionsView opens the LaunchFlow pre-filled (applied only where the live
  catalog still advertises the pair; the re-gating lives in the flow, not here).
- **Stays visible** (L144): the copy states "the failed row stays visible until retired — the
  refusal is addressable evidence".

### Invariants And Boundaries

- The bridgeError is EVIDENCE: verbatim or stated-absent, never summarized, reworded, or hidden.
- The retained pair may only ever render as refused/never-validated here — presenting it as
  effective would be an evidence-honesty violation.
- Exactly two actions; no timer, no effect, no auto-retry path may be added without a design
  ruling (the component is deliberately `useState`-only).
- Nothing fires before the explicit confirm — zero fetches until `retire` is confirmed.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The banner: verbatim error, refused pair, armed retire confirm, corrected-launch prefill. | L70-L182 | [FailedLaunchBanner.tsx](FailedLaunchBanner.tsx) |
| `verbatimBridgeError` (serialize-never-reword) + the tier machine behind 'refused'. | L1-L66 | [../../data/launchEvidence.ts](../../data/launchEvidence.ts) |
| The refused-tier badge with the word in the accessible name. | L13-L69 | [../../grammar/EvidenceBadge.tsx](../../grammar/EvidenceBadge.tsx) |
| The operator terminate route this retire uses. | — | [../../data/terminal.ts](../../data/terminal.ts) |
| The owner mounting it for a focused FAILED seat and opening the pre-filled flow. | L589-L597 | [SessionsView.tsx](SessionsView.tsx) |
| The flow consuming the refused-pair prefill. | L36-L42, L227-L236 | [LaunchFlow.tsx](LaunchFlow.tsx) |
| The failed-row fixtures ×3 harnesses (verbatim bridgeErrors, retained refused pairs). | L93-L178 | [../../test/fixtures/openResponses.ts](../../test/fixtures/openResponses.ts) |
| The suite: verbatim ×3, never-validated, prefill, honest confirm, decline, stated absence. | L30-L106 | [FailedLaunchBanner.test.tsx](FailedLaunchBanner.test.tsx) |

## Update History

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R6 (uniform async fail-loud): the
  focused-failed-seat banner rendering the bridgeError verbatim (absence stated), the retained
  pair as refused/never-validated with the EvidenceBadge, and exactly Retire (armed confirm
  naming session + leaf; operator terminate route — the true retire route needs the seat's own
  actor identity, upstream ask recorded) and 'Launch corrected…' (refused-pair prefill); zero
  timers/effects — no auto-retry exists. Verification metadata pinned to the leaf base until
  closeout stamps the L3 code commit.
