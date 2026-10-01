# AGENTS.md

## Purpose

This file is the package-owned template for installed
`ar-coordination/tasks/AGENTS.md`. It defines task collaboration doctrine for
work planned or recorded under the coordinator task tree.

## Code Commentary

### Logic

The template tells agents to improve the framing of under-specified or risky
tasks, surface assumptions and truth gaps, reason top-down and bottom-up, make
the evidence model visible, and show representative examples before risky code
or structural documentation changes. It also defines a visible planning standard
for non-trivial work so task artifacts carry intent, invariants, examples, and
implementation sequencing rather than only a checklist. A preamble now states
the doctrine applies up front — the moment a developer is thinking about building
something, in plain chat, before any task format is chosen or task file exists —
and the Evidence-First Reasoning section routes evidence gathering through
`c-04-retrieval-strategy-router`.

### Conventions

This is a doctrine file rather than a task instance. It uses broad behavioral
rules that apply to task planning and review, while the concrete `w-02-light-task-workflow` skill task
format still owns the artifact structure for individual tasks.

### Invariants And Boundaries

The task doctrine should increase clarity without delaying simple work. It must
not replace the concrete workflow skills, task templates, or approval gates; it
only describes the framing standard agents should bring to non-trivial tasks.

### Todos

Refresh verification metadata after the current `AGENTS.md` source reshuffle is
committed.

### Docs References

No external domain documentation is needed for this repository-local task
doctrine template.

No relevant external documentation found.

## Evidence

### Repo-Internal References

This onboarding is backed by the source template itself.

- The template covers meta-questioning, task reframing, top-down/bottom-up design philosophy, assumptions, and truth gaps. [1]
- Evidence-first reasoning and representative examples are required when correctness depends on interpretation or risky structure. [2]
- The visible planning standard lists the context agents should surface before non-trivial implementation. [3]

### Cross-Repo References

No sibling repository evidence is needed for this task doctrine template.

No meaningful cross-repo references found.

## 260821-CLIVE Task Authoring Doctrine

The installed doctrine now states that every intrinsically valid task mutation publishes during
every door, projection, and operation phase. Its validity comes from typed task arguments,
caller/task authority, exact source CAS, task invariants, and structural integrity—not scheduling
convenience. The response's `projectionEffects` reports the before/after affected sprint union:
canonical task truth is already accepted, projections become invalid-empty, and independent
rebuild failures carry exact next actions. No queue row is patched or retained as fallback.
`discard-unstarted` is separately defined as a reasoned, centralized no-execution proof plus typed
parent audit; present or ambiguous evidence routes to real abandon/archive/recovery/completion.
