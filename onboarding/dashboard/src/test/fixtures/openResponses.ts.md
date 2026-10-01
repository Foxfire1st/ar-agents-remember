# dashboard/src/test/fixtures/openResponses.ts

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
- 400s: cit:(["def _open_terminal_response(", "\"status\": \"launch-selection-invalid\""], mcp/src/agents_remember/serving/_app_terminal_routes.py:239-257) and cit:([`INVALID_NON_NATIVE`], dashboard/src/test/fixtures/openResponses.ts:52-55) model the pair/kind refusal payloads; the server's paired/native selection guard is cit:([`resolve_terminal_open_selection`], mcp/src/agents_remember/serving/harness_control_api.py:156-179), and the route reports its control error as cit:(["def _open_terminal_response(", "\"status\": \"launch-selection-invalid\""], mcp/src/agents_remember/serving/_app_terminal_routes.py:239-239; mcp/src/agents_remember/serving/_app_terminal_routes.py:257-257).
- 400s: cit:([`INVALID_PARTIAL_PAIR`], dashboard/src/test/fixtures/openResponses.ts:46-49) and cit:([`INVALID_NON_NATIVE`], dashboard/src/test/fixtures/openResponses.ts:52-55) model the pair/kind refusal payloads, and the route reports its control error as cit:(["def _open_terminal_response("], mcp/src/agents_remember/serving/_app_terminal_routes.py:239-257).
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

## Evidence

### Repo-Internal References

- Every response-path fixture + the failed/pending rows. [1]
- The response-body mirrors these instantiate. [2]
- The shared row builder the failed/pending rows extend. [3]
- The route decorator exposes the terminal-open API. [4]
- The terminal response body is assembled by `_terminal_entry_payload`. [5]
- The shared opener returns the resolved terminal-open response. [6]
- The `launchFlow` classifier is declared for the response-path cases. [7]
- Tier uniformity ×3 harnesses over `FAILED_LAUNCH_ROWS`. [8]
- Verbatim bridgeError rendering over the failed rows. [9]
