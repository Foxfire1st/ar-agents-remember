# dashboard/src/panels/session-cockpit/FailedLaunchBanner.test.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The failed-launch banner jsdom suite (260715-FEUI-L3 R6/S4): the refusal renders VERBATIM for ALL
THREE harnesses, the retained pair renders as refused (never validated), and the only actions are
an honest Retire confirm and 'Launch corrected…' — no auto-retry path exists.

## Code Commentary

### Logic

- **Verbatim ×3** cit:(["renders the bridgeError VERBATIM for every harness's failed row"], dashboard/src/panels/session-cockpit/FailedLaunchBanner.test.tsx:31-39) — loops `FAILED_LAUNCH_ROWS` (Claude, Codex, Pi) asserting the
  rendered text `toBe` the fixture's `controlRaw.bridgeError` byte-for-byte (uniform async
  fail-loud: no harness gets special framing).
- **Refused, never validated** cit:(["renders the retained pair as the REFUSED pair"], dashboard/src/panels/session-cockpit/FailedLaunchBanner.test.tsx:41-49) — the Codex row's retained pair renders with "never
  validated" and the badge's `data-evidence-tier`/`aria-label` are `refused`.
- **Prefill** cit:(["'Launch corrected…' pre-fills the flow from the refused pair"], dashboard/src/panels/session-cockpit/FailedLaunchBanner.test.tsx:51-59) — 'Launch corrected…' calls back with the Pi row's exact
  `{harness, modelKey, effort}` (provider-qualified key intact).
- **Honest confirm** cit:(["Retire arms an HONEST confirm naming the session and leaf; confirming retires once"], dashboard/src/panels/session-cockpit/FailedLaunchBanner.test.tsx:61-89) — ZERO fetches before the explicit confirm (asserted twice: on
  render and after arming); the confirm names the session label ("scout-claude") AND the leaf id;
  confirming sends exactly ONE `POST /api/terminal/<id>/terminate`; the confirm closes after
  success.
- **Decline** cit:(["declining the confirm keeps the row untouched"], dashboard/src/panels/session-cockpit/FailedLaunchBanner.test.tsx:91-99) — `keep` disarms and NOTHING is sent.
- **Stated absence** cit:(["a failed row WITHOUT a retained bridgeError states the absence rather than inventing one"], dashboard/src/panels/session-cockpit/FailedLaunchBanner.test.tsx:101-105) — a failed row without a retained bridgeError renders "no
  bridgeError retained", never an invented message.

### Conventions

Rows come from the shared `openResponses` failed fixtures + the `catalogRow` builder (leafed/bare
variants built inline); fetch stubbed per-case via `vi.stubGlobal`. Test-only.

### Invariants And Boundaries

The verbatim ×3 loop is the R6 uniformity net (a harness-specific rewording fails it); the
zero-fetch-before-confirm assertions are the no-auto-retry net.

## Evidence

### Repo-Internal References

- The banner under test. [1]
- The failed-row fixtures ×3 harnesses with verbatim bridgeErrors. [2]
- The shared row builder for the leafed/bare variants. [3]
