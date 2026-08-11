# mcp/src/agents_remember/kernel/primitives/gate_vocab.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/kernel/primitives/gate_vocab.py`     |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-08T14:38+02:00                                       |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                   |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

`kernel/primitives/gate_vocab.py` is the gate vocabulary for policy and records (kernel-owned,
260731-EFA-L9). Kernel is below models: the wire layer re-exports these names from here rather
than defining them, and the control-plane records import them through models.

## Code Commentary

### Logic

The module defines the `GateKind` literal vocabulary and `coerce_gate_kind`
(cit:([`coerce_gate_kind`], mcp/src/agents_remember/kernel/primitives/gate_vocab.py:45-45)), which validates raw gate-kind strings with a typed
error for unknown values.

### Invariants And Boundaries

- One declaration per gate-kind member: models re-export, records import through models, and
  nobody re-types the literal.

### Todos

No known follow-up.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Structural gate models import the producer-owned vocabulary from kernel. | "from agents_remember.kernel.primitives.gate_vocab import (" | mcp/src/agents_remember/models/structural/gates.py:15-20 |
| Vocabulary edge coverage rides the structural-coverage suite. | `test_gate_vocabulary_errors` | mcp/tests/test_leaf_structural_coverage.py:199-199 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the kernel gate-vocabulary
  extraction. Verification metadata pinned until closeout stamps the L9 code commit.
