# mcp/src/agents_remember/canvas/explainer_grades.py

## Governing Overview

[Route overview](overview.md)

## Purpose

One leaf's judgment store: the categories a grade means, the grades keyed by block identity and fingerprint, and the prune that drops the blocks a comparison no longer holds.

## Code Commentary

- `grades_path` keeps the store beside the task's other durable records, so a grade survives Retire and leaves only with the master's retirement or the sprint's archive.
- `read_grades` answers an empty store when no grade was ever made, and refuses `grades-unreadable` rather than inventing grades from a file it cannot read.
- `define` refuses a scale outside two to five named grades, a grade name repeated in one scale, a meaning that is not one line, a redefinition of a category under another scale or meaning (`category-exists`), and a category beyond the admitted count (`category-limit`).
- `grade` refuses a leaf that never defined the category, a grade outside that category's scale, a reason that is empty, multiline or too long, and more references than one call admits.
- A reference the product could not fingerprint is returned in the refused tuple and nothing is written, because a grade made without a fingerprint could never be marked stale.
- `prune` drops only the grades of blocks named as gone, and answers the store and the count it removed.

## Evidence

- The store lies with the task's durable records, so it outlives the environment [1]
- An absent store reads as empty; an unreadable one is a named refusal, never invented grades [2]
- A category is two to five named grades defined once; another scale or meaning for the same name is refused [3]
- A grade needs a defined category, a grade of its scale, a one-line reason and a fingerprint for every block it names [4]
- Only the grades of blocks that no longer exist are pruned [5]
