# dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx

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
  the confirmation names the session label and, when bound, the canonical task-document path
  cit:(["retire session “{session.label}”", "session.taskDocumentRef ?"], dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:193-196).
  Confirming sends ONE `terminateTerminalSession(session.id)` POST
  (retire = the operator terminate route: `/api/terminal/{id}/retire` requires the retiring
  seat's OWN `actor_session`, which the dashboard operator does not have — worker decision 6,
  reviewer-verified as genuinely unusable from this surface; the resulting `terminated` status
  renders as the grammar's "retired". Provenance-recording retires need an upstream operator
  actor-identity decision — logged as an upstream ask). A failed terminate states "the server did
  not confirm; the row is unchanged" cit:(["retire failed — the server did not confirm; the row is unchanged"], dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:89-89); success re-hydrates the catalog. `keep` disarms
  and sends nothing.
- **Launch corrected…** cit:(["launch corrected…"], dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:128-128): hands `{harness, modelKey, effort}` from the refused pair to
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

## Evidence

### Repo-Internal References

- The banner: verbatim error, refused pair, armed retire confirm, corrected-launch prefill. [1]
- `verbatimBridgeError` (serialize-never-reword) + the tier machine behind 'refused'. [2]
- The refused-tier badge with the word in the accessible name. [3]
- The operator terminate route this retire uses. [4]
- The owner mounting it for a focused FAILED seat and opening the pre-filled flow. [5]
- The flow consuming the refused-pair prefill. [6]
- The failed-row fixtures ×3 harnesses (verbatim bridgeErrors, retained refused pairs). [7]
- The suite: verbatim ×3, never-validated, prefill, honest confirm, decline, stated absence. [8]
