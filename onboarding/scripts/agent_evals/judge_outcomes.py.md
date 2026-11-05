# scripts/agent_evals/judge_outcomes.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Turns validated deterministic and rubric results into trial labels.

## Code Commentary

### Invariants And Boundaries

Capture failure remains distinct from a valid semantic unknown. Failure has precedence; a semantic-unknown label requires the admitted opposite-family judge.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
