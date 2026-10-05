# operations/review.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Independently inspect the exact requested candidate or sealed fix-verification scope and return a verdict for the owner.

## Current Contract

The assignment supplies requirement revision, candidate/base, review mode, criteria and report path. A baseline covers every changed file, including unattributed changes; invariant mapping adds an inspection dimension and never filters the population. Evidence must match each requirement’s class.

Fix-verification checks only the sealed outstanding findings against the same requirement/candidate lineage. It cannot reset the baseline or introduce new findings into that round; a separate new contradiction returns to the owner.

The report records pass/block recommendation, changed-file coverage, stable findings with location/evidence/impact/repair, checks and limitations. The owner reads and records the review state.

## Conventions

Canonical skills/l-01-agent-lifecycles/operations/review.md owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy and the eight harness copies; no generated file defines a separate obligation.

## Invariants And Boundaries

Reviewer never edits, accepts AR task truth or publishes Git. Developer decisions stay in the own chat; peer clarification uses `role_message` to the actual parent/task role.

## Evidence

### Repo-Internal References

| Finding | Anchor | References |
| --- | --- | --- |
| Requested complete baseline, monotonic fix-verification and owner-recorded independent result. | lines 3-9 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/operations/review.md:3-9 |
