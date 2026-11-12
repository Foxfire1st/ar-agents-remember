# mcp/src/agents_remember/worktrees/modules/quality/certification_run.py

## Governing Overview

[Governing route overview](../overview.md)

## Purpose

Connects strict quality execution to original typed terminal recording, caller-owned selection callbacks and complete code-prefix evidence readback.

## Code Commentary

### Logic

`SelectedCodeCertification` transports the validated execution input together with three owner callbacks: select returned terminals, resolve protected report generations, and authorize a gate start. The dataclass does not invoke those callbacks or confer lifecycle authority.

`record_terminal_generation` opens the decoder artifact through the supplied immutable publication, parses an object payload and delegates to `record_published_generation`. Unreadable bytes or a non-object payload produce typed catalog refusal. This seam can retain complete red or interrupted catalogs before the caller propagates failure. `require_recorded_generation` separately raises if recording returned any refusal.

`verify_selected_code_terminals` requires exactly Gates 1–4, with a certificate and exact reference at every gate. It reopens certificate/result references from the existing store, compares original objects, reparses publication shape, verifies publication authority and physical nested evidence, then validates the whole certificate chain against the frozen admission. It returns the fourth terminal’s original publication.

### Conventions

Typed terminal objects are inputs to journal selection; dictionary rendering and report pointers are presentation. Callers retain responsibility for live ownership, CAS and failure propagation.

### Invariants And Boundaries

- A passed process without complete original references is insufficient for code certification.
- Red recording and rejection are separate steps so failed evidence is not erased by an early exception.
- These helpers do not run Dagger, mint lifecycle authority, perform Gate 5 or finalize the worktree.

### Todos

None recorded for this file's bounded responsibility.

## Evidence

### Docs References

The resolved registry supplies no applicable external Domain Documentation source for this card.

### Repo-Internal References

- The caller supplies selection, retention and last-moment start authority. [1]
- Decoder readback records actual terminal catalogs before failure propagation. [2]
- Returned recording refusals remain fatal to their caller. [3]
- Complete code-prefix verification reopens originals and validates the frozen chain. [4]

### Cross-Repo References

No separately configured cross-repository source is used for this card.
