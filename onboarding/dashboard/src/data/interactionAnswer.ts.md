# dashboard/src/data/interactionAnswer.ts

## Governing Overview

[data overview](overview.md)

## Purpose

The **InteractionBar's sole adapter-answer path** (design §7.3): kind classification and
exact-session delivery for pending vendor interactions. Every representable interaction uses
`/api/terminal/{session}/interaction-response` with the current bridge epoch. Structured question
pages send an `answers` map; permission, arbitrary-choice, and composer interactions send one
`response` string. Lifecycle gates may mirror an interaction for coordination but are never its
answer transport. **NEVER a PTY write**: terminal text remains an ordinary queued user message.

For multiplexed seats the module also derives the FULL pending set —
the parent thread's singular `controlPendingInteraction` slot plus the additive plural
`controlPendingInteractions` (harness sub-agent pendings), de-duplicated by interactionId — exposes
the adapter-bound sub-agent label (evidence only, never fabricated), and routes every answer against
the ONE interaction looked up across BOTH slots.

## Code Commentary

### Logic

- **`representPendingInteraction(raw)`** cit:([`representPendingInteraction`], dashboard/src/data/interactionAnswer.ts:146-183) — kind-aware classification of ONE
  `controlPendingInteraction` payload into the `InteractionRepresentation` union cit:([`InteractionRepresentation`], dashboard/src/data/interactionAnswer.ts:42-50):
  structured questions → `questions`; choices exactly allow/deny → `permission`; other choices →
  `choices`; none → `composer`. Every scalar mode sends a direct-route `response`. No usable
  `interactionId`, or a structured question with no options, → `unrepresentable`
  with an honest reason pointing at the inspector's raw payload — never dead buttons, never
  silently dropped. A missing prompt stays answerable: `prompt` is the empty string, reported not
  invented. Absent payload → `null` (no bar).
- **`pendingInteractionAgentLabel(raw)`** cit:([`pendingInteractionAgentLabel`], dashboard/src/data/interactionAnswer.ts:191-198) — the adapter-bound sub-agent label on a
  multiplexed pending interaction, read from `raw.raw.agentLabel` ONLY (the codex adapter binds it
  when a sub-agent thread raises the request). Absent on the parent thread's singular slot;
  missing/blank → `undefined` — the bar badges WHO is asking only from this evidence, never a
  fabricated name.
- **`pendingInteractionPayloads(session)`** cit:([`pendingInteractionPayloads`], dashboard/src/data/interactionAnswer.ts:207-222) — every pending interaction payload on the
  row: the parent-thread singular slot first, then the multiplexed sub-agent entries from the
  additive plural `controlPendingInteractions`, de-duplicated by interactionId (multiplexed bridges carry
  the parent in BOTH slots). Entries without an interactionId still render (the bar says why they
  cannot be answered) but never dedupe against each other.
- **`representSessionPendingInteraction(session, interactionId)`** cit:([`representSessionPendingInteraction`], dashboard/src/data/interactionAnswer.ts:230-245) — the
  representation of ONE pending interaction by id, looked up across the singular slot AND the
  multiplexed sub-agent entries (`unrepresentable` payloads skipped). Answer-channel routing must
  see an agent-owned payload exactly like the parent's — routing against only the singular slot
  would miss sub-agent answers.
- **`submitInteractionAnswer(args)`** cit:([`submitInteractionAnswer`], dashboard/src/data/interactionAnswer.ts:570-615) — acquires the per-interaction store lock,
  retains the exact retry payload, then derives channel routing from the session's CURRENT pending
  interaction via `representSessionPendingInteraction(args.session, args.interactionId)`
  cit:([`representSessionPendingInteraction`], dashboard/src/data/interactionAnswer.ts:230-245) — across the singular slot AND the multiplexed agent entries, never the caller's
  say-so and never the parent's singular slot alone. Structured maps must cover EVERY question (the
  backend's all-or-nothing contract — a partial map is refused client-side first); every scalar
  representation uses `response`. A stale bridge epoch is re-read and retried ONCE, then the
  server's own `not-pending` words land instead of a loop.

### Invariants And Boundaries

- Every representable adapter interaction is session-owned and answers through the exact-session
  route, regardless of lifecycle presence. No answer path writes to a PTY or lifecycle gate.
- Structured question answers must cover every exact wire question text; a stale epoch gets one fresh
  epoch read rather than a blind retry loop.
- Payload routing is derived from the interaction looked up across BOTH pending slots.
- The plural list is de-duplicated by interactionId (multiplexed bridges carry the parent in both slots);
  id-less entries render but never dedupe. The sub-agent label comes from `raw.agentLabel` only —
  absent evidence renders no badge rather than an invented name.
- An unavailable submission authority blocks before POST; response failures keep the server's words
  verbatim.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- Kind classification, the agent label, the multiplexed payload set, and the per-interaction lookup. [1]
- Exact-session POST + epoch retry and the locked submit. [2]
- The `OpenSession` mirror of both pending slots + the catalog mapping that carries them. [3]
- The exact-session backend response endpoint used by all modes. [4]
- The bar that renders one bar per pending payload and badges the agent label. [5]
- The rail preview naming WHO asks via the same label helper. [6]
- The waiting-seat triage titles deriving asker + preview from the helpers. [7]
- The round-trip state slice this path's outcomes land in. [8]
- The suite: kind matrix, lifecycle-free structured/scalar round-trips, epoch retry, and agent-label pins. [9]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

## Reliable Submit Delta

Answer delivery preserves the exact pending interaction plus answer text and draft revision across a
retry. The shared lock admits only the matching current interaction, and successful clearing is
revision-CAS so a concurrent operator edit survives. Lifecycle membership is irrelevant: a normal
message, PTY write, or lifecycle gate can never substitute for the exact-session response.
