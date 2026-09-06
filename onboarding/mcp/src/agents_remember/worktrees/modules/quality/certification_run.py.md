# mcp/src/agents_remember/worktrees/modules/quality/certification_run.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/certification_run.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:15:01+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `../overview.md` |

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

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolved registry supplies no applicable external Domain Documentation source for this card. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The caller supplies selection, retention and last-moment start authority. | `SelectedCodeCertification` | mcp/src/agents_remember/worktrees/modules/quality/certification_run.py:38-44 |
| Decoder readback records actual terminal catalogs before failure propagation. | `record_terminal_generation` | mcp/src/agents_remember/worktrees/modules/quality/certification_run.py:47-70 |
| Returned recording refusals remain fatal to their caller. | `require_recorded_generation` | mcp/src/agents_remember/worktrees/modules/quality/certification_run.py:73-76 |
| Complete code-prefix verification reopens originals and validates the frozen chain. | `verify_selected_code_terminals` | mcp/src/agents_remember/worktrees/modules/quality/certification_run.py:79-107 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |

## Update History

- 2026-09-06T15:15:01+00:00 — Created from the complete source at `c69d5171187fa1957025e393270db9f5a864ab14`. Documented the selected-original, terminal or transport responsibility and its actual neighboring owners. Source verification is not execution or acceptance evidence.
