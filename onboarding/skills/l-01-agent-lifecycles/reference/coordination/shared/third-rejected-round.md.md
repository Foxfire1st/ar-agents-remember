# skills/l-01-agent-lifecycles/reference/coordination/shared/third-rejected-round.md

## Governing Overview

[overview](../../../overview.md)

## Purpose

How Managers and, under developer-chosen direct coordination, Architects judge progress at a coder's third rejected round, consider an earlier coder switch or Reviewer replacement, and tell coder rounds from the product's automatic step-up count.

## Code Commentary

Work starts on the Worker role's default. At the same coder's third rejected round the judge reads the sealed finding trail and judges observed progress; a third rejection does not by itself require a stronger model. Clear progress may justify one more bounded repair with a recorded reason and a separately authorized further round. If fixes stay too large or barely move, the configured stronger model in `role.stepUp` is used; with none configured the Manager asks the Architect, and the Architect under direct coordination uses its developer-decision route. A stronger model grants no extra review round, an earlier coder switch needs the developer's agreement, and a Reviewer is replaced only on clear observed signs. The three-round rule counts the current coder's rounds, while the product's `afterTries` step-up counts the task's failed rounds of the matching lane and does not reset on a coder change.

## Evidence

- The third rejected round is judged from the sealed finding trail and does not automatically require a stronger model. [1]
- Progress allows one bounded repair; otherwise the configured step-up model is used, or the decision goes up. [2]
- A stronger model grants no extra round; coder switches and Reviewer replacements have their own conditions. [3]
- Coder rounds and the product's automatic step-up count are distinct. [4]
