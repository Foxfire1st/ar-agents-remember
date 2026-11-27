# skills/l-01-agent-lifecycles/capsule-budgets-current.json

## Governing Overview

[overview](overview.md)

## Purpose

The current size record keeps authored capsule, detail and digest ceilings separate from generated measurements of the instruction corpus; budget tests compare freshly compiled texts with those measurements and ceilings.

## Code Commentary

The generated curation entries record 412 words for the Curator and 724 for the Manager, and the Consolidator capsules measure 689 (`orientation`), 466 (`consolidation`), and 442 (`recovery`) words. The coherence-judgments detail measures 355 words and `reference/consolidation-pass.md` measures 740 words. These measurements sit below the authored ceilings.

The generated measurement for the Curator handoff ingestion template is 6,889 words and carries the current source digest. The measurement leaves the authored ceilings unchanged.

The record has schema `ar-role-capsule-budget-current/v1`. Its `derived.current_measurements` records 37 capsule sizes, 45 declared step-detail sizes, the every-role digest (342 words) and eight ordinary linked templates. Authored capsule word ceilings remain recorded in the file (Architect 5,500 words, Manager 4,600, Curator 4,537, Reviewer 4,200, Bootstrap 4,000, Orchestrator 3,800 and every other role 3,742; detail 2,500 and digest 2,327), while active enforcement moved to `COMPILED_CAPSULE_TOKEN_CEILINGS` and `WIRE_TOKEN_CEILINGS` in `wire_budget.py`. Current measurements are facts, not individual item limits.

`derived.current_detail_population` matches the composed manifest's step-detail sources, and the linked-template population matches its ordinary template references. `derived.approved_source_sizes` records measured sizes and source hashes despite its historical key name; `derived.compiler_input_revisions` records current compiler inputs. These generated facts detect same-size source changes without granting approval. The `decision` block retains historical authorities and frozen predecessor hashes. Its active `measuredCurrentRenewalBug08` contains authority only; renewal computes current facts with `mcp/.venv/bin/python scripts/renew-instructions.py`.

The retained `measuredCurrentRenewalWaitsAndCodingGuidelines` sub-record carries
`measuredCurrentRenewalAlwaysOnToolNames` as `supersededUncommittedRecord`. Its recorded
basis says that sub-record was current only in the uncommitted candidate, never on a
committed tree, and therefore has no `historicalTree`. This is retained renewal custody,
not the active renewal or a new source measurement.

## Evidence



- Generated measurements cover current capsules, declared details and the shared digest without individual item limits. [2]


- Generated approved source sizes record the Manager brief at 1,463 words and its exact source SHA-256; current generated measurements include ordinary linked templates. [3]

- Authored role, detail and digest ceilings are separate from generated measurements. [4]

- Detail and ordinary-template populations agree with their composed manifest classifications. [5]

- The retained predecessor, historical registry and their retained helpers are authenticated by hash. [6]

- Budget checks read current measurements and authored ceilings. [7]


- The generated template measurement records 6,625 words and the current source digest. [11]

- The decision block retains authority and frozen historical registry and predecessor identities. [1]


- The generated size record holds the current curation capsule (412 Curator, 727 Manager) and judgment detail (353) measurements. [8]
