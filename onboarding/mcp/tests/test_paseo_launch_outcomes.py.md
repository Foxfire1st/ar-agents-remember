# mcp/tests/test_paseo_launch_outcomes.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The launch's outcomes against the fake bridge: what is written to a receipt, which failures stay retryable, and how a repeat or a conflicting request is refused.

## Code Commentary

`LaunchOutcomeTests` checks recorded creation and refusal outcomes, retryable unknown outcomes after an unanswered host call, and a 300,000-byte first message sent as data. `RepeatAndConflictTests` requires a repeated request to converge on the same agent, a conflicting or second request to refuse with nothing changed, and a new start on a closed leaf execution to refuse while naming the holder. A replacing start retires the holder and starts in one call, refuses a running holder without the word, and a task-bound receipt is created exclusively.

## Invariants And Boundaries

The refused conflict cases preserve the existing receipt and agent. Saved native Antigravity Retry reuses the recorded agent if present. An absent recorded agent produces HTTP 409 with ACP guidance and leaves the host agent set unchanged. The ACP regression checks the saved create payload, including its task server, is replayed exactly. The oversized first message is sent as data, not truncated into the prompt path.

## Fresh catalog reads before outcomes

A new start asks catalog metadata before the retained holder/refusal, archive or create sequence. The refusal cases still preserve receipts and create or archive no agent; the extra catalog question is a read, not a changed launch outcome.

## Evidence

### Repo-Internal References


- The bridge outcome is stored in the receipt. Timeout without a usable answer leaves the tested launch retryable. [1]




- A repeat converges on one agent. A conflicting request leaves the saved execution unchanged. A fresh request on a closed execution names its holder. [2]
