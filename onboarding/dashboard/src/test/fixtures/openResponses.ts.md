# dashboard/src/test/fixtures/openResponses.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/fixtures/openResponses.ts`   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`       |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
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

- cit:([`OPENED_STARTING`], dashboard/src/test/fixtures/openResponses.ts:17-33): 200 — controlState `'starting'`, the REQUESTED pair persisted
  before validation (`claude-fable-5[1m]`/`max`). cit:([`OPENED_VENDOR_DEFAULTS`], dashboard/src/test/fixtures/openResponses.ts:36-43): the
  intentionally selectionless open — BOTH knobs omitted ⇒ both retained as null.
- 400s: cit:([`INVALID_PARTIAL_PAIR`], dashboard/src/test/fixtures/openResponses.ts:46-49) and cit:([`INVALID_NON_NATIVE`], dashboard/src/test/fixtures/openResponses.ts:52-55) model the pair/kind refusal payloads; the server's paired/native selection guard is cit:([`resolve_terminal_open_selection`], mcp/src/agents_remember/serving/harness_control_api.py:156-179), and the route reports its control error as cit:(["def _open_terminal_response(", "\"status\": \"launch-selection-invalid\""], mcp/src/agents_remember/serving/_app_terminal_routes.py:225-225; mcp/src/agents_remember/serving/_app_terminal_routes.py:243-243).
- 409s: cit:([`SEAT_TAKEN`], dashboard/src/test/fixtures/openResponses.ts:64-71) NAMES the owning session (`worker-l3-live`); cit:([`LAUNCH_CONFLICT`], dashboard/src/test/fixtures/openResponses.ts:72-86)
  carries the LIVE row's retained pair (process truth) with the attempted pair only in
  `detail` — provenance never rewritten.
- Failed rows: cit:([`FAILED_CLAUDE_ROW`], dashboard/src/test/fixtures/openResponses.ts:93-106) (unknown model), cit:([`FAILED_CODEX_ROW`], dashboard/src/test/fixtures/openResponses.ts:108-122) (effort not
  launch-settable for the model), cit:([`FAILED_PI_ROW`], dashboard/src/test/fixtures/openResponses.ts:124-138) (bare id instead of the provider-qualified
  key) — each `controlState: "failed"` with the refused pair retained verbatim in
  `resolvedModel`/`resolvedEffort` and a `bridgeError` in the server's exact
  `validate_launch_selection` wording NAMING the advertised alternatives;
  cit:([`FAILED_LAUNCH_ROWS`], dashboard/src/test/fixtures/openResponses.ts:140-144) is the ×3 sweep the tier-uniformity tests iterate.
- cit:([`FAILED_CLAUDE_EFFORT_ROW`], dashboard/src/test/fixtures/openResponses.ts:147-160): the second refusal shape — the EFFORT is what the
  catalog refused — plus a `paneDiagnostic` ("runner kept the refusal addressable until
  retired").
- cit:([`PENDING_INTERACTION_ROW`], dashboard/src/test/fixtures/openResponses.ts:164-178): a READY row holding `controlPendingInteraction`
  (`ix_7`, approval, prompt + choices) mirroring L2's FLEET shape — answering it is L6's
  surface.

### Invariants And Boundaries

- Response bodies match `app.py` field-for-field and refusal wordings mirror
  `harness_launch.py`/recorded L5 evidence (reviewer byte-checked) — never reword; extend
  against new recorded evidence only.
- Failed rows must keep the refused pair AND a bridgeError naming alternatives: the
  FailedLaunchBanner verbatim tests and `launchEvidence` tier sweep both lean on that anatomy.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Every response-path fixture + the failed/pending rows. | `OPENED_STARTING`; `OPENED_VENDOR_DEFAULTS`; `INVALID_PARTIAL_PAIR`; `INVALID_NON_NATIVE`; `BAD_KIND`; `SEAT_TAKEN`; `LAUNCH_CONFLICT`; `FAILED_CLAUDE_ROW`; `FAILED_CODEX_ROW`; `FAILED_PI_ROW`; `FAILED_LAUNCH_ROWS`; `FAILED_CLAUDE_EFFORT_ROW`; `PENDING_INTERACTION_ROW` | dashboard/src/test/fixtures/openResponses.ts:17-33; dashboard/src/test/fixtures/openResponses.ts:36-43; dashboard/src/test/fixtures/openResponses.ts:46-49; dashboard/src/test/fixtures/openResponses.ts:52-55; dashboard/src/test/fixtures/openResponses.ts:58-61; dashboard/src/test/fixtures/openResponses.ts:64-71; dashboard/src/test/fixtures/openResponses.ts:72-86; dashboard/src/test/fixtures/openResponses.ts:93-106; dashboard/src/test/fixtures/openResponses.ts:108-122; dashboard/src/test/fixtures/openResponses.ts:124-138; dashboard/src/test/fixtures/openResponses.ts:140-144; dashboard/src/test/fixtures/openResponses.ts:147-160; dashboard/src/test/fixtures/openResponses.ts:164-178 |
| The response-body mirrors these instantiate. | `TerminalOpenSuccessBody`; `TerminalOpenSelectionInvalidBody`; `TerminalOpenBadKindBody` | dashboard/src/types/terminalOpen.ts:10-26; dashboard/src/types/terminalOpen.ts:31-34; dashboard/src/types/terminalOpen.ts:37-40 |
| The shared row builder the failed/pending rows extend. | `catalogRow` | dashboard/src/test/fixtures/catalogRows.ts:10-27 |
| The route decorator exposes the terminal-open API. | `api_terminal_open` | mcp/src/agents_remember/serving/_app_terminal_routes.py:683-698 |
| The terminal response body is assembled by `_terminal_entry_payload`. | "def _terminal_entry_payload(entry: TerminalCatalogEntry) -> dict[str" | mcp/src/agents_remember/serving/_app_terminal_routes.py:207-207 |
| The shared opener returns the resolved terminal-open response. | "def _open_terminal_response(" | mcp/src/agents_remember/serving/_app_terminal_routes.py:225-225 |
| The `launchFlow` classifier is declared for the response-path cases. | `launchFlow` | dashboard/src/data/launchFlow.test.ts:29-29 |
| Tier uniformity ×3 harnesses over `FAILED_LAUNCH_ROWS`. | `FAILED_LAUNCH_ROWS` | dashboard/src/data/launchEvidence.test.ts:90-94 |
| Verbatim bridgeError rendering over the failed rows. | "describe(\"FailedLaunchBanner (R6) — uniform across Claude, Codex, and Pi\"" | dashboard/src/panels/session-cockpit/FailedLaunchBanner.test.tsx:30-39 |

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current dashboard card for `openResponses.ts` with its task-document, seat-state, and lifecycle interaction boundaries.
- 2026-08-04T15:32:44+02:00 — 260731-EFA-L6 S18-B08 curator: rebound the invalid-selection fixture, resolver, and route response to their respective whole implementation extents and removed the unsupported exclusivity wording.

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R3/R6 (open + failed-launch fixtures):
  200-starting and 200-vendor-defaults, both 400 `launch-selection-invalid` shapes + `bad-kind`,
  409 `leaf-taken` and `launch-selection-conflict`, sweep-projected failed rows ×3 harnesses
  (+ the Claude effort-refusal variant) with retained refused pairs and alternatives-naming
  bridgeErrors, and the pending-interaction row for L6. Verification metadata pinned to the
  leaf base until closeout stamps the L3 code commit.
