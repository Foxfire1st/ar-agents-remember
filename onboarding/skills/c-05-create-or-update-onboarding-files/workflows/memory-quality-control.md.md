# skills/c-05-create-or-update-onboarding-files/workflows/memory-quality-control.md

## Governing Overview

[Repository overview](../../../overview.md)

## Purpose

The pre-code-commit and pre-curation memory-quality procedure this skill now owns: resolve context, run task-start drift control, classify drift, hand off maintenance, check missing onboarding before the code commit, run the complete curation check, judge validator findings, publish curator coherence and use targeted style fixers only after findings.

## Code Commentary

The file is kept from the retired memory-quality-control skill and its opening comment states the two facts that changed with the product. The task-start drift report path is retired (`docs/reference/drift-c02.md`): `context_packet(include_drift=true)` answers the drift summary in its own response and files no report, and the durable result of a quality check is the single contract-scoped checklist `memory_quality_check` atomically replaces at the `reportPath` it returns — the enclosure's `reports/curator-memory-quality.md`, with its `attestationPath` beside it, outside both Git worktrees and removed with the enclosure on cleanup or abandon.

Its boundaries now route authoring to the sibling procedures of the same skill rather than to a separate skill: this diagnostic reports and routes memory-quality work and does not rewrite onboarding prose itself, while `../SKILL.md` and `converted-card-workflow.md` author it. Curation stays complete — a named scoped check never stands in for the full operation — and a scoped diagnostic never becomes a whole-repository adoption scan. Closeout commits remain owned by the `w-02-light-task-workflow` transaction and authority controls, and a code-quality, test or independent-review result is not made a closeout prerequisite. The curators' permitted-action rules keep their stated ownership of the two quality tools.

## Evidence

- Drift classification answers in `context_packet`'s own response and files no temporary report; the durable result is the contract-scoped checklist at the `reportPath` `memory_quality_check` returns, with its attestation beside it. [1]
- The procedure reports and routes; authoring belongs to this same skill's `SKILL.md` and `converted-card-workflow.md`, and closeout commits stay with the `w-02-light-task-workflow` transaction. [2]
- Curation is always the complete operation, and a scoped diagnostic never replaces it or turns into a repository-wide adoption scan. [3]
