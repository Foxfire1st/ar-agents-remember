# dashboard/src/panels/session-cockpit/FailedLaunchBanner.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/FailedLaunchBanner.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The failed-launch banner jsdom suite (260715-FEUI-L3 R6/S4): the refusal renders VERBATIM for ALL
THREE harnesses, the retained pair renders as refused (never validated), and the only actions are
an honest Retire confirm and 'Launch corrected…' — no auto-retry path exists.

## Code Commentary

### Logic

- **Verbatim ×3** (L31-L39) — loops `FAILED_LAUNCH_ROWS` (Claude, Codex, Pi) asserting the
  rendered text `toBe` the fixture's `controlRaw.bridgeError` byte-for-byte (uniform async
  fail-loud: no harness gets special framing).
- **Refused, never validated** (L41-L49) — the Codex row's retained pair renders with "never
  validated" and the badge's `data-evidence-tier`/`aria-label` are `refused`.
- **Prefill** (L51-L59) — 'Launch corrected…' calls back with the Pi row's exact
  `{harness, modelKey, effort}` (provider-qualified key intact).
- **Honest confirm** (L61-L89) — ZERO fetches before the explicit confirm (asserted twice: on
  render and after arming); the confirm names the session label ("scout-claude") AND the leaf id;
  confirming sends exactly ONE `POST /api/terminal/<id>/terminate`; the confirm closes after
  success.
- **Decline** (L91-L99) — `keep` disarms and NOTHING is sent.
- **Stated absence** (L101-L105) — a failed row without a retained bridgeError renders "no
  bridgeError retained", never an invented message.

### Conventions

Rows come from the shared `openResponses` failed fixtures + the `catalogRow` builder (leafed/bare
variants built inline); fetch stubbed per-case via `vi.stubGlobal`. Test-only.

### Invariants And Boundaries

The verbatim ×3 loop is the R6 uniformity net (a harness-specific rewording fails it); the
zero-fetch-before-confirm assertions are the no-auto-retry net.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The banner under test. | L70-L182 | [FailedLaunchBanner.tsx](FailedLaunchBanner.tsx) |
| The failed-row fixtures ×3 harnesses with verbatim bridgeErrors. | L93-L178 | [../../test/fixtures/openResponses.ts](../../test/fixtures/openResponses.ts) |
| The shared row builder for the leafed/bare variants. | L10-L27 | [../../test/fixtures/catalogRows.ts](../../test/fixtures/catalogRows.ts) |

## Update History

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 S4 (R6): verbatim bridgeError ×3 harnesses,
  refused-not-validated pair + badge tier, refused-pair prefill, the honest armed confirm with a
  single terminate POST, the decline path sending nothing, and stated bridgeError absence.
  Verification metadata pinned to the leaf base until closeout stamps the L3 code commit.
