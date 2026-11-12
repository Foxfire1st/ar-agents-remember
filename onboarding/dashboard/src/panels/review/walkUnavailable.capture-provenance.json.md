# dashboard/src/panels/review/walkUnavailable.capture-provenance.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The receipt of the one refused body `walkUnavailable.refused.captured.json`, captured for the mounted status-reveal cases of MIK-R39 (OR-R042). It records when and how the body was captured, over which route and world, and what the body is.

## Code Commentary

### The capture

- `captured_at` is 2026-10-06T19:02:38+02:00. The producer is the leaf's worker with `capture_refusal.py` over the public reviewer HTTP route.
- `route` and `url`: `GET /api/review/intent?repo=agents-remember&master=260928_maintained-invariant-knowledge&leaf=260928-MIK-L33&selectorKind=invariant&selectorId=00000000-0000-0000-0000-000000000000` (the fields are the `params` object).
- `status` is 400; the body is 927 bytes with `sha256` `a07bc47b4dd357992dae6580e4d3a1a70755554567118a3ae920c88cea38677b`.
- `source_commit` is `beb9473e21f3e173094da4f1437798660c3abb52`; the served world was the scratch one under `/tmp/mik-run3/l39/r42-restartB/real`.
- `condition` states the honesty rule: the route was asked for an invariant identity absent from the comparison, so the refusal is genuine; the body is preserved verbatim and replayed as the refused answer of an in-tree read; no refusal body was authored by hand.

### Use

`ReviewSurface.walkUnavailable.test.tsx` replays this body for every refused-read case; each click and key activation of the target row receives it unchanged.

### Boundaries

The refusal is a fact about the captured comparison, not a statement that the requested obligation does not exist. The body is not current project knowledge.

## Evidence

- The receipt row: when, by what producer, over which route, status, hash, size, source commit, world and honesty condition. [1]
- The refused body it names, whole. [2]
