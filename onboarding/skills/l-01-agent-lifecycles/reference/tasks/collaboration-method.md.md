# skills/l-01-agent-lifecycles/reference/tasks/collaboration-method.md

## Governing Overview

[overview](../../overview.md)

## Purpose

The method by which the agent and developer work out scope and risk before choosing a task format or creating a task file; it applies as soon as the developer considers building something, including in plain chat.

## Code Commentary

The shared understanding of scope and risk decides whether a task file is warranted and which format to use. The agent may help improve the question itself (meta-questioning) when a request is poorly framed, aimed at the wrong layer or asks for implementation before the operating model is clear, but not on simple tasks. Non-trivial, ambiguous, risky, architectural, documentation-heavy or taxonomy-heavy requests get a reviewable reframing (surface request, deeper objective, best framing, assumptions, boundaries); a reframing that materially changes scope, intent or sequencing waits for the developer's confirmation, while a clarifying one may proceed.

The design is reasoned top-down (objective, conceptual model, assumptions, non-goals, what must be true) and bottom-up (files, validations, edits, sequencing, checked against the model). Before implementation on non-trivial work the agent surfaces assumptions, truth gaps only the developer can answer, invariants and non-goals, makes its evidence model visible by type (gathering evidence through `knowledge/use.md`) and says what will prove the plan correct, and gives reviewable examples before risky change. The visible planning standard lists eight items, ending with an implementation plan derived from the earlier ones. `core/invariants.md` points here before scoping work and asks that the method be applied as written; `document-authoring.md` points here before writing a design.

## Evidence

- The method applies before choosing a task format, including in plain chat, and meta-questioning is for leverage, not delay. [1]
- Non-trivial requests get a reviewable reframing, and a scope-changing reframing waits for confirmation. [2]
- Design reasoning runs in both directions, with assumptions, truth gaps, invariants and non-goals surfaced. [3]
- Evidence and examples are visible before risky change, and the planning standard lists eight items. [4]
- The shared invariants point here before scoping work. [5]
