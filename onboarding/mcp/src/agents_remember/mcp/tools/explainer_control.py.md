# mcp/src/agents_remember/mcp/tools/explainer_control.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The payload builder behind `explainer_control`: the architect's Update and Retire over one leaf's explainer, and the claim by which any hosted architect seat takes a master over.

## Code Commentary

- The caller is the tool server's own agent binding — an environment, never an argument — so a seat can no more name another agent than name itself another role; `update` and `retire` are accepted only from the seat the master-to-architect record names.
- When no record names a seat, both leaf actions are refused `not-this-masters-architect`, and the refusal says to take the master over with `claim`; `claim` itself is refused `not-an-architect` unless the caller's canonical role is architect.
- A claim writes the record with act `claim` before transferring this master's held reports. Each admitted row is withdrawn before a delivery attempt and its terminal or held state is logged. If the new destination cannot take it, the report file is returned to the tray as `*.undelivered.md` where possible; when no backing file exists, it attempts to restore the old held row so custody can be retried. A failed restoration is logged as `not reported`, rather than claimed as held.
- Named bridge timeout and unknown-send codes, and a bare `TimeoutError`, become `sent, outcome unknown`; other named bridge failures hold unless explicitly refused. An unclassified exception is `not reported`. A logged uncertain outcome is not a held candidate for a later claim, so the claim does not resend it.
- Delivery is pre-checked for the recipient's provider limit, an unopened or unfinished seat, a pending permission, other messages already waiting and a recipient inside a turn.
- Every refusal is an answer with `ok: False`, a `reason` and the same word in `code`; an unresolvable selection becomes `selection-unavailable` rather than a server error, and a Retire needs its receipt id reduced to a single path segment.

## Evidence

- An unknown action is refused before any lookup or mutation [1]
- Update and Retire are accepted only from the seat the record names, and a missing record accepts none [2]
- A claim writes the record first and then moves the master's held reports [3]
- A timeout or unknown outcome is classified as uncertainty rather than a failure to report

- A withdrawn report follows delivery, held, unknown or fallback handling; if no backing file exists, fallback attempts to restore the previous held custody [4]

- Provider-limit, unopened, unfinished, permission, waiting-message and active-turn conditions are checked before a send attempt [6]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/mcp/tools/explainer_control.py:508-518 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b. Retired means the anchor no longer stands, not that the cited subject was deleted.
