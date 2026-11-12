# mcp/tests/test_agent_eval_text_delivery.py

## Governing Overview

[overview](overview.md)

## Purpose

Received native text markers, frozen details and actual read observations are the subject of this regression module, together with the provenance of the current curator capture: each compiled instruction origin after the shared every-role prefix is kept, and missing, malformed or ambiguous origins are refused rather than guessed.

## Code Commentary

### Invariants And Boundaries

The source declares controlled assertions and retained-data scenarios. Delivered detail files carry their emitted bytes, with relative links rewritten to the shipped corpus, while the captured artifact stays unchanged. The module imports `_compiled` from `test_l84_capsule_delivery_proofs.py`, so that test module must stay importable for this one to load. Reading this card establishes neither a fresh test run nor native host or model acceptance.

## Evidence

- The source defines this file's responsibility and the boundaries described here. 

- The source defines this file's responsibility and the boundaries described here. [1]

- The current curator capture keeps the every-role shared prefix as the first origin and every compiled instruction unit's origin contiguously after it, and binding freezes the shipped detail body without mutating the capture. [2]
- Missing, empty, gapped, overlapping, short, duplicated, non-integer, absolute, escaping or wrongly shaped origins are refused with a detail fault and nothing is written. [3]
- A compiled manifest whose every-role source is missing, duplicated or at another revision makes the capture refuse as ambiguous provenance. [4]
- A rewritten detail is identified by its emitted bytes (size and digest), and same-size or size-changing damage stays a validation unknown. [5]
- The module takes its compiled-capsule helper from the capsule-delivery proof module. [6]
