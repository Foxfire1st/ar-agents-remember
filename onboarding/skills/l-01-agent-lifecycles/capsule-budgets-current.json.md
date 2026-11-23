# skills/l-01-agent-lifecycles/capsule-budgets-current.json

## Governing Overview

[overview](overview.md)

## Purpose

The current size record keeps authored capsule, detail and digest ceilings separate from generated measurements of the instruction corpus; budget tests compare freshly compiled texts with those measurements and ceilings.

## Code Commentary

The record has schema `ar-role-capsule-budget-current/v1`. Its `derived.current_measurements` records 34 capsule sizes, 38 declared step-detail sizes, the every-role digest and eight ordinary linked templates. Authored capsule ceilings are Architect 5,500 words, Manager 4,600, Curator 4,537, Reviewer 4,200, Bootstrap 4,000, Orchestrator 3,800 and every other role 3,742; the detail ceiling is 2,500 and the digest ceiling 2,327. Current measurements are facts, not individual item limits.

`derived.current_detail_population` matches the composed manifest's step-detail sources, and the linked-template population matches its ordinary template references. `derived.approved_source_sizes` records measured sizes and source hashes despite its historical key name; `derived.compiler_input_revisions` records current compiler inputs. These generated facts detect same-size source changes without granting approval. The `decision` block retains historical authorities and frozen predecessor hashes. Its active `measuredCurrentRenewalBug08` contains authority only; renewal computes current facts with `mcp/.venv/bin/python scripts/renew-instructions.py`. Growth within an authored ceiling needs no per-item limit increase.

The retained `measuredCurrentRenewalWaitsAndCodingGuidelines` sub-record carries
`measuredCurrentRenewalAlwaysOnToolNames` as `supersededUncommittedRecord`. Its recorded
basis says that sub-record was current only in the uncommitted candidate, never on a
committed tree, and therefore has no `historicalTree`. This is retained renewal custody,
not the active renewal or a new source measurement.

## Evidence





- Generated measurements cover current capsules, declared details and the shared digest without individual item limits. [2]


The generated ordinary-template measurement records the Manager brief at 1,465 words and retains its exact source SHA-256.


- Authored role, detail and digest ceilings are separate from generated measurements. [4]

- Detail and ordinary-template populations agree with their composed manifest classifications. [5]

- The retained predecessor, historical registry and their retained helpers are authenticated by hash. [6]

- Budget checks read current measurements and authored ceilings. [7]

- The decision block retains authority and frozen historical registry and predecessor identities. [1]
- Current generated measurements include ordinary linked templates. [3]
