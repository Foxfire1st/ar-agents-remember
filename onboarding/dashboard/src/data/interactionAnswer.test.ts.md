# dashboard/src/data/interactionAnswer.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

The unit suite for the **single exact-session interaction answer path**: kind classification,
structured and scalar response bodies, lifecycle-free Codex MCP approvals, free-text delivery,
epoch refresh, retry, and multiplexed sub-agent label pins. It proves every representable vendor
interaction uses `/api/terminal/{session}/interaction-response`; no lifecycle gate or terminal
write exists in the answer module. Fetch is stubbed per case and unstubbed in `afterEach`.

## Code Commentary

### Logic

- **Kind-awareness (F8):** choices → `choices` mode with the validated view; no choices
  → `composer` mode; missing `interactionId` → `unrepresentable` whose reason names "cannot be
  answered" + "inspector" (never dead buttons); missing prompt stays answerable with the honest
  empty string; absent payload → null.
- **Delivery-failure honesty (M6):** `readAdapterDecisionFailure` parses the reopened
  gate's failure record defensively — no record / no `delivery` word → null.
- **`stubDirectRoute(options)`** cit:([`stubDirectRoute`], dashboard/src/data/interactionAnswer.test.ts:118-156)
  submission-authority read, with scriptable epoch-mismatch and authority-failure modes.
- **Structured questions:** per-question pages from the additive top-level list
  AND the pre-fix runner's `raw.input.questions` fallback; an option-less question falls the whole
  payload back to `unrepresentable` (the all-or-nothing submit could never fire).
- **Session-direct route (no lifecycle required):** structured `answers` maps and every scalar
  `response` POST to `/api/terminal/{session}/interaction-response` with the expected bridge epoch.
  The regression cases include the exact Codex MCP `accept`/`decline`/`cancel` choice shape and a
  free-text interaction on lifecycle-less seats. Epoch mismatch refreshes and retries once; an
  unavailable submission authority blocks honestly before a POST.
- **`pendingInteractionAgentLabel` pins:** the label is read from
  `raw.agentLabel` only — `undefined` for a missing `raw`, an empty `raw`, an absent payload, and
  a blank label; never fabricated.

### 2026-07-24 Curator Delta

The interaction suite now covers structured multi-question maps, direct permission responses,
lifecycle-free seats, epoch mismatch refresh-and-retry, and retained exact retry payloads.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The module under test (representation, multiplex helpers, direct route, and locked submit). [1]
- The component suite covers exact URL/body handling, in-flight/retry states, structured questions, and multiplexed sub-agent approvals. [2]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
