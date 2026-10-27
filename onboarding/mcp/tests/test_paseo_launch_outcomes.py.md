# mcp/tests/test_paseo_launch_outcomes.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The launch's outcomes against the fake bridge: what is written to a receipt, which failures stay retryable, and how a repeat or a conflicting request is refused.

## Code Commentary

`LaunchOutcomeTests` requires each answer of the runtime to be written to the receipt, a launch without a usable answer to stay retryable, and a 300,000-byte first message to launch as data. `RepeatAndConflictTests` requires a repeated request to converge on the same agent, a conflicting or second request to refuse with nothing changed, and a new start on a closed leaf execution to refuse while naming the holder. A replacing start retires the holder and starts in one call, refuses a running holder without the word, and a task-bound receipt is created exclusively.

## Invariants And Boundaries

A refusal is asserted together with the world being unchanged, so a refusal that left a seat behind fails. The oversized first message is sent as data, not truncated into the prompt path.

## Fresh catalog reads before outcomes

A new start asks catalog metadata before the retained holder/refusal, archive or create sequence. The refusal cases still preserve receipts and create or archive no agent; the extra catalog question is a read, not a changed launch outcome.

## Evidence

### Repo-Internal References

- Every runtime answer is written to the receipt and an unusable one leaves the launch retryable. [1]


- A repeat converges on one agent; a conflict refuses and changes nothing, naming the holder it found. [2]
