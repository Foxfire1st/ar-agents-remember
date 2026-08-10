# dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`       |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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
  the confirm names the session label and its leaf cit:(["import { useState } from \"react\";", "import { leafIdFromKey } from "], dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:8-8; dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:1-1) — the honest
  naming the leaf demands. Confirming sends ONE `terminateTerminalSession(session.id)` POST
  (retire = the operator terminate route: `/api/terminal/{id}/retire` requires the retiring
  seat's OWN `actor_session`, which the dashboard operator does not have — worker decision 6,
  reviewer-verified as genuinely unusable from this surface; the resulting `terminated` status
  renders as the grammar's "retired". Provenance-recording retires need an upstream operator
  actor-identity decision — logged as an upstream ask). A failed terminate states "the server did
  not confirm; the row is unchanged" cit:(["retire failed — the server did not confirm; the row is unchanged"], dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:90-90); success re-hydrates the catalog. `keep` disarms
  and sends nothing.
- **Launch corrected…** cit:(["launch corrected…"], dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:129-129): hands `{harness, modelKey, effort}` from the refused pair to
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The banner: verbatim error, refused pair, armed retire confirm, corrected-launch prefill. | `FailedLaunchBanner` | dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:70-182 |
| `verbatimBridgeError` (serialize-never-reword) + the tier machine behind 'refused'. | `verbatimBridgeError` | dashboard/src/data/launchEvidence.ts:57-66 |
| The refused-tier badge with the word in the accessible name. | `EvidenceBadge` | dashboard/src/grammar/EvidenceBadge.tsx:46-69 |
| The operator terminate route this retire uses. | `terminateTerminalSession` | dashboard/src/data/terminal.ts:443-452 |
| The owner mounting it for a focused FAILED seat and opening the pre-filled flow. | `onLaunchCorrected` | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:179-179 |
| The flow consuming the refused-pair prefill. | `LaunchPrefill` | dashboard/src/panels/session-cockpit/LaunchFlow.tsx:41-47 |
| The failed-row fixtures ×3 harnesses (verbatim bridgeErrors, retained refused pairs). | `FAILED_LAUNCH_ROWS` | dashboard/src/test/fixtures/openResponses.ts:140-144 |
| The suite: verbatim ×3, never-validated, prefill, honest confirm, decline, stated absence. | "FailedLaunchBanner (R6) — uniform across Claude" | dashboard/src/panels/session-cockpit/FailedLaunchBanner.test.tsx:30-106 |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 9 citation claims and preserved verification metadata.

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R6 (uniform async fail-loud): the
  focused-failed-seat banner rendering the bridgeError verbatim (absence stated), the retained
  pair as refused/never-validated with the EvidenceBadge, and exactly Retire (armed confirm
  naming session + leaf; operator terminate route — the true retire route needs the seat's own
  actor identity, upstream ask recorded) and 'Launch corrected…' (refused-pair prefill); zero
  timers/effects — no auto-retry exists. Verification metadata pinned to the leaf base until
  closeout stamps the L3 code commit.
