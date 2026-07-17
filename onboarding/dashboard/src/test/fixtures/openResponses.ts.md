# dashboard/src/test/fixtures/openResponses.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/fixtures/openResponses.ts`   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[dashboard/src overview](../../overview.md)

## Purpose

**Open-route and failed-launch fixtures** (260715-FEUI-L3 R3/R6): every
`POST /api/terminal/{id}` response path plus the sweep-projected FAILED rows for ALL THREE
harnesses. Details mirror the server's exact wording (`harness_control_api.py`, `app.py`,
`harness_launch.py` `validate_launch_selection`) and the recorded L5 refusals — the pack teaches
the central R6 fact that a catalog-invalid pair opens 200/'starting' on every harness and fails
ASYNC. Failed rows are built with L2's shared `catalogRow` builder (extended, not forked).

## Code Commentary

### Logic

- `OPENED_STARTING` (L17-L33): 200 — controlState `'starting'`, the REQUESTED pair persisted
  before validation (`claude-fable-5[1m]`/`max`). `OPENED_VENDOR_DEFAULTS` (L36-L43): the
  intentionally selectionless open — BOTH knobs omitted ⇒ both retained as null.
- 400s: `INVALID_PARTIAL_PAIR` (L46-L49, "model and effort must be provided together"),
  `INVALID_NON_NATIVE` (L52-L55) — the ONLY synchronous selection refusals — and `BAD_KIND`
  (L58-L61).
- 409s: `LEAF_TAKEN` (L64-L68) NAMES the owning session (`worker-l3-live`); `LAUNCH_CONFLICT`
  (L72-L86) carries the LIVE row's retained pair (process truth) with the attempted pair only in
  `detail` — provenance never rewritten.
- Failed rows (L93-L144): `FAILED_CLAUDE_ROW` (unknown model), `FAILED_CODEX_ROW` (effort not
  launch-settable for the model), `FAILED_PI_ROW` (bare id instead of the provider-qualified
  key) — each `controlState: "failed"` with the refused pair retained verbatim in
  `resolvedModel`/`resolvedEffort` and a `bridgeError` in the server's exact
  `validate_launch_selection` wording NAMING the advertised alternatives;
  `FAILED_LAUNCH_ROWS` (L140-L144) is the ×3 sweep the tier-uniformity tests iterate.
- `FAILED_CLAUDE_EFFORT_ROW` (L147-L160): the second refusal shape — the EFFORT is what the
  catalog refused — plus a `paneDiagnostic` ("runner kept the refusal addressable until
  retired").
- `PENDING_INTERACTION_ROW` (L164-L178): a READY row holding `controlPendingInteraction`
  (`ix_7`, approval, prompt + choices) mirroring L2's FLEET shape — answering it is L6's
  surface.

### Invariants And Boundaries

- Response bodies match `app.py` field-for-field and refusal wordings mirror
  `harness_launch.py`/recorded L5 evidence (reviewer byte-checked) — never reword; extend
  against new recorded evidence only.
- Failed rows must keep the refused pair AND a bridgeError naming alternatives: the
  FailedLaunchBanner verbatim tests and `launchEvidence` tier sweep both lean on that anatomy.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Every response-path fixture + the failed/pending rows. | L17-L178 | [openResponses.ts](openResponses.ts) |
| The response-body mirrors these instantiate. | L10-L63 | [../../types/terminalOpen.ts](../../types/terminalOpen.ts) |
| The shared row builder the failed/pending rows extend. | L10-L27 | [catalogRows.ts](catalogRows.ts) |
| The route whose bodies are mirrored field-for-field. | L956-L1046 | [app.py](../../../../mcp/src/agents_remember/serving/app.py) |
| The classifier table consuming every fixture here. | — | [../../data/launchFlow.test.ts](../../data/launchFlow.test.ts) |
| Tier uniformity ×3 harnesses over `FAILED_LAUNCH_ROWS`. | — | [../../data/launchEvidence.test.ts](../../data/launchEvidence.test.ts) |
| Verbatim bridgeError rendering over the failed rows. | — | [../../panels/session-cockpit/FailedLaunchBanner.test.tsx](../../panels/session-cockpit/FailedLaunchBanner.test.tsx) |

## Update History

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R3/R6 (open + failed-launch fixtures):
  200-starting and 200-vendor-defaults, both 400 `launch-selection-invalid` shapes + `bad-kind`,
  409 `leaf-taken` and `launch-selection-conflict`, sweep-projected failed rows ×3 harnesses
  (+ the Claude effort-refusal variant) with retained refused pairs and alternatives-naming
  bridgeErrors, and the pending-interaction row for L6. Verification metadata pinned to the
  leaf base until closeout stamps the L3 code commit.
