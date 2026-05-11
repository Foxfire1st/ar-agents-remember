# C-11-memory-carryover-from-branch/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-11-memory-carryover-from-branch/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-11T03:00                           |
| lastVerifiedCommitHash | `65e91dc05628e0652647be8d3bed865b195ad6e1`                         |
| lastVerifiedCommitDate | 2026-05-11T03:15:36+02:00|

## Purpose

This skill documents C-11, the selective memory carryover workflow for protected-branch environments where a developer has richer memory on another source branch but official code receives delayed batched merges.

## Code Commentary

### Logic

The skill defines C-11 as a memory reconciliation step rather than a normal Git merge. It tells agents to run `memory_carryover.py plan` first, review the candidate report, and use `apply` only with explicit approval. The contract names the five relevant branch roles: official code, source branch code, official memory, source branch memory, and old base. It defines evidence tiers from strongest to weakest, with only exact landed commits, patch-id matches, and final content matches becoming auto-carry candidates by default.

### Conventions

C-11 output is state-oriented and JSON-friendly. Same-path overlap is intentionally review-required because the official branch may contain another developer's independent change. The skill keeps `--replace-existing` and explicit review-required inclusion as opt-in choices for overwriting different official onboarding content.

### Invariants And Boundaries

C-11 must not copy source branch memory for code that did not land, must not copy source branch ledger rows wholesale, and must refresh carried onboarding verification metadata to the official code commit. C-02 remains the accuracy check for the current branch; C-11 only imports richer memory whose source-code validity is proven or explicitly reviewed.

### Todos

Future versions can add structural onboarding merges after the first whole-file carryover path has enough real-world usage.

### Docs References

No external documentation is needed for this repository-local workflow skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The skill defines the source-branch-to-official memory carryover use case, command shape, evidence tiers, output states, and boundaries. | current | [C-11 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-11-memory-carryover-from-branch/SKILL.md) |
| The carryover helper implements the plan/apply behavior described by this skill. | current | [memory_carryover.py](agents-remember-md/skills/U-01-core-skills/C-11-memory-carryover-from-branch/scripts/memory_carryover.py) |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-11T03:00: Created onboarding for the new C-11 memory carryover skill and generalized it from workbench-only to source-branch carryover.
