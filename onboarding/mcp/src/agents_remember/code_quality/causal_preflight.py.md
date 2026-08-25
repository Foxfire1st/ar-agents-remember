# mcp/src/agents_remember/code_quality/causal_preflight.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/code_quality/causal_preflight.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

Validates high-fanout prerequisites once at their owning boundary and emits the causal input used
to avoid hundreds of misleading downstream symptoms.

## Code Commentary

### Logic

`evaluate_preflights` executes typed `PreflightSpec` validators, records the first stable cause, and
derives blocked test files only from complete import/declared ownership edges. The current owner
preflight constructs and revalidates a canonical lifecycle organizational-repair record, ensuring
terminalization cannot replace its durable handoff. The CLI binds the candidate index tree,
environment digest, and attempt nonce before writing JSON/Markdown.

### Conventions

Cause IDs are versioned strings and corrective owners are repository paths. The preflight report
starts with empty runtime evidence; pytest enriches the same artifact.

### Invariants And Boundaries

- Dagger admission is required before preflight execution.
- Heuristic/safe-full reasons never authorize causal suppression.
- A failed preflight still fails quality and grants no acceptance evidence.
- A valid failed report is distinguished from a broken preflight tool.

### Todos

Add another owner only after a reproduced high-fanout cascade proves the need.

## Docs References

No external documentation owns the internal lifecycle schema preflight.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Preflight results and blocking use only proven graph edges. | `evaluate_preflights` | mcp/src/agents_remember/code_quality/causal_preflight.py:42-143 |
| The lifecycle terminalization owner is validated once. | `_validate_lifecycle_terminalization` | mcp/src/agents_remember/code_quality/causal_preflight.py:146-244 |
| Candidate and attempt identity bind the artifact. | `candidate_identity` | mcp/src/agents_remember/code_quality/causal_preflight.py:247-286 |

## Cross-Repo References

No adjacent repository supplies the prerequisite contract.

## Update History

- 2026-08-25T01:56+02:00 — Created for owner-level lifecycle failure localization.
