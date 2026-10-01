# turn.jsonl

## Governing Overview

[mcp/tests overview](../../../overview.md)

## Purpose

Provides the Claude 2.1.210 replay-acceptance, assistant activity, retry, and terminal-result frames
used by the adapter's correlated turn regression.

## Code Commentary

### Logic

The sequence starts with the replayed correlated user message that proves acceptance, then emits
assistant activity, a structured API retry, and a successful terminal result. The test applies the
frames one at a time to prove that acceptance, settling activity, and completion are distinct state
transitions.

### Conventions

Stable UUIDs, session id, vendor request id, and timestamp keep the fake transport deterministic.
The user frame carries the same correlation envelope the adapter writes on submission.

### Invariants And Boundaries

- A replayed user frame proves acceptance but not terminal completion.
- Retry evidence maps activity without authorizing resend.
- The successful result remains explicit structured evidence; no pane, log, or timing fallback is
  implied.
- The fixture contains bounded synthetic content and no credentials.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation entries are configured in the resolved source registry.

No configured live documentation source was available for this pass.

### Repo-Internal References

The Claude bridge regression feeds these frames incrementally and asserts the resulting receipt,
activity, transcript, and terminal outcome.

- The fixture loader selects the 2.1.210 directory and parses each JSONL frame. [1]
- The correlated-turn test proves replay acceptance, retry settling, and terminal completion remain distinct. [2]

### Cross-Repo References

No meaningful cross-repo references were needed for this fixture.

No meaningful cross-repo references found.
