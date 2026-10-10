# skills/l-01-agent-lifecycles/operations/review.md

## Governing Overview

[lifecycle overview](../overview.md)

## Purpose

Independent review that runs only when requested: one pass/block recommendation per requirement with coverage, findings and checks, handed directly to the Worker — and code PASS directly to the Curator — with the memory check kept as a separate sealed lane.

## Code Commentary

A baseline covers the complete candidate diff; fix-verification checks only the sealed outstanding IDs. Rounds are bounded with a D107 one-further-look exception the Manager records. The Reviewer opens each ordinary leaf round itself, records its own verdict, and never edits, accepts, starts a role or publishes. After code and memory PASS it tells the Manager once that the leaf is ready for closeout. Curator code findings are answered directly even after code PASS, by taking the point into the findings or stating why it does not hold.

## Evidence

- The verdict goes directly to the Worker and code PASS directly to the Curator. [1]
- Fix-verification checks only the sealed outstanding IDs; rounds are bounded with a recorded D107 exception. [2]
- The Reviewer never edits, accepts, starts a role or publishes. [3]
