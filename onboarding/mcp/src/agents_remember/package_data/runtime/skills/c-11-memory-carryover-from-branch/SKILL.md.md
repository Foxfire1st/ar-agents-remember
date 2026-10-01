# c-11-memory-carryover-from-branch/SKILL.md

## Purpose

This skill documents `c-11-memory-carryover-from-branch` skill, the selective memory carryover workflow for protected-branch environments where a developer has richer memory on another source branch but official code receives delayed batched merges.

## Code Commentary

### Logic

The skill defines `c-11-memory-carryover-from-branch` skill as a memory reconciliation step rather than a normal Git merge. It tells agents to use the `memory_carryover_plan` MCP tool first, review the candidate report, and use `memory_carryover_apply` only with explicit intent. The contract names the five relevant branch roles: official code, source branch code, official memory, source branch memory, and old base. It defines evidence tiers from strongest to weakest, with only exact landed commits, patch-id matches, and final content matches becoming auto-carry candidates by default.

Since GitHub #54 the Output States section also documents `ledger-mapped-head`
(an unmapped official code HEAD — e.g. a PR merge commit — mapped to the
current memory content commit) and the `memory_main_advance` block every apply
reports: memory `main` is fast-forwarded to the official checkout tip after
the carryover commits (states `fast-forwarded` / `already-current` /
`diverged` / `failed` / `skipped`), with a note to push memory `main` per the
repo's git workflow on developer approval.

The Candidate Kinds section (carryover artifact coverage, 2.9.0) names the
four kinds and their `include_review_required` selection keys: `file-sidecar`
(source path), `route-overview` (normalized route), `memory-only-doc` (source
path or route, for docs changed only in branch memory), and `entity-catalog`
(the literal `entity-catalog`; always review-required when differing, with
fingerprints recomputed against the official ref on apply and reported as
`entity_fingerprint_validation`). The `exact-landed-commit` tier wording now
matches the implementation: EVERY source-branch commit touching the path must
have landed.

### Conventions

`c-11-memory-carryover-from-branch` skill output is state-oriented and JSON-friendly. Same-path overlap is intentionally review-required because the official branch may contain another developer's independent change. The skill keeps `--replace-existing` and explicit review-required inclusion as opt-in choices for overwriting different official onboarding content.

### Invariants And Boundaries

`c-11-memory-carryover-from-branch` skill must not copy source branch memory for code that did not land, must not copy source branch ledger rows wholesale, and must refresh carried onboarding verification metadata to the official code commit. `c-02-memory-quality-control` skill remains the accuracy check for the current branch; `c-11-memory-carryover-from-branch` skill only imports richer memory whose source-code validity is proven or explicitly reviewed.

### Todos

Future versions can add structural onboarding merges after the first whole-file carryover path has enough real-world usage.

### Docs References

No external documentation is needed for this repository-local workflow skill.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The skill defines the source-branch-to-official memory carryover use case, command shape, evidence tiers, output states, and boundaries. [1]
- The package service implements the public plan and the configured, leaf-contract-bound internal apply owner described by this skill. [2]

### Cross-Repo References

No sibling repository evidence is needed for the skill itself.

No meaningful cross-repo references found.

## 260815-DAG-L4 Carryover Boundary

L4 narrows carryover to an explicitly task-owned recovery leaf. Official default, sprint-super, and atomic-memory refs are not writable workbenches, so planning and apply guidance must lead through ordinary leaf closeout and integration rather than a direct protected-ref fallback.
