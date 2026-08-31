# responses_sse.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `scripts/e2e_harness/responses_sse.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T22:20:19+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `scripts/e2e_harness/overview.md` |

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Renders the minimal Responses API server-sent-event sequences used by the deterministic provider.

## Code Commentary

### Logic

Dedicated builders create function-call, tool-search, and assistant-message output items, then append
one standard zero-usage completion event and serialize the event stream with compact JSON.

### Conventions

Wire projection is isolated from fixture state and tool-selection policy. Namespace is emitted only
for a namespaced tool definition.

### Invariants And Boundaries

- Every response has one created event and one completed event.
- Function arguments are compact JSON strings, matching the Responses wire contract.
- This module projects already-made decisions; it never chooses a tool or route.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the live Codex consumer validates these fixture frames.

| Finding | Anchor | Source |
| --- | --- | --- |
| Each helper emits a bounded created/output/completed SSE sequence. | `function_sse` | scripts/e2e_harness/responses_sse.py:9-68; scripts/e2e_harness/responses_sse.py:71-91 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Namespace is conditional while function name and JSON arguments are always present. | `function_sse` | scripts/e2e_harness/responses_sse.py:9-30 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The projection has no external repository dependency. | "Minimal Responses API server-sent-event projections for the real Codex fixture." | scripts/e2e_harness/responses_sse.py:1-6 |

## Update History

- 2026-08-30T22:20:19+02:00 — 260821-ARSPAWN-L5 converted source references to the
  canonical anchored citation format. Verification metadata remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 split SSE wire projection from provider state to keep both units maintainable. Verification metadata remains closeout-owned.
