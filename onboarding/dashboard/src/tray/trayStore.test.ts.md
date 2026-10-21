# dashboard/src/tray/trayStore.test.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Checks collection identity, bounded admission, first-target policy, persistence and compensation.

## Code Commentary

### Logic

Exact repeated object deduplicates; whole files from different leaves/trees survive reload separately; refused/racing image writes remove only unowned bytes; notes/removal work; count/image/message limits name refusals; first default applies once, resets only for unchosen last removal, and pending default honors choice/leaving; valid picks reload while untimed legacy chat row is discarded; storage errors retain live picks with warning.

In-memory Storage, image maps and gated image writes make quota/race cases deterministic; stores have fixed clocks and shown-chat callbacks.

### Invariants And Boundaries

This verifies store policy with injected storage, not the browser IndexedDB engine; no test execution was performed by helper.

## Evidence

- Checks collection identity, bounded admission, first-target policy, persistence and compensation. [1]
- Checks collection identity, bounded admission, first-target policy, persistence and compensation. [2]
- Checks collection identity, bounded admission, first-target policy, persistence and compensation. [3]
- Checks collection identity, bounded admission, first-target policy, persistence and compensation. [4]
- Checks collection identity, bounded admission, first-target policy, persistence and compensation. [5]
- Checks collection identity, bounded admission, first-target policy, persistence and compensation. [6]
- Checks collection identity, bounded admission, first-target policy, persistence and compensation. [7]
- Checks collection identity, bounded admission, first-target policy, persistence and compensation. [8]
- Checks collection identity, bounded admission, first-target policy, persistence and compensation. [9]
- Checks collection identity, bounded admission, first-target policy, persistence and compensation. [10]
- Checks collection identity, bounded admission, first-target policy, persistence and compensation. [11]
