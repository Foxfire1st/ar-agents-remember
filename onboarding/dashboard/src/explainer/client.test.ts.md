# dashboard/src/explainer/client.test.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Specifies the explainer's client: the four routes, the several spellings the host may answer in, the refusals that keep the page usable, and the receipt and delivery shapes.

## Code Commentary

- The route cases assert one path per press with every part escaped.
- The parse cases feed the column's own shape and the host's alternate spellings and expect the same view from both.
- A refusal keeps the server's reason and detail, an unreachable host is a sentence rather than a thrown error, and an answer that is not an attempt answer is no answer.
- The body cases assert a bounded single-segment request id and receipt id, as the real route accepts.

## Evidence

- An archived or retired seat is no seat, and an unknown seat word is unavailable [1]
- A refusal returns its reason and the server's detail instead of throwing [2]
- An unreachable host is a sentence, not a failed page [3]
- Posted bodies carry a bounded single-segment request id and receipt id [4]
