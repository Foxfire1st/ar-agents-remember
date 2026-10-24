# mcp/src/agents_remember/canvas/explainer_planned.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The planned-mode page a leaf's intent review shows before any work exists: declared effects, packet scopes, prepared context and reference files, with no change set to explain.

## Code Commentary

- `planned_page` is pure: its caller supplies the task document, the planned comparison, the statements, the packet texts, the reference names and the code tip's paths, and it answers the payload without opening a file or starting anything.
- The payload states `modelTurns: 0` and `agentStarts: 0` because the module has no path that could take a turn, so zero model work is a property rather than a promise.
- `TOP_LINE` and `INTENDED_NOTICE` fix the page's standing reading: a planned page shows intent, never a fact about the code, and never a change set.
- `PLANNED_SORTS` offers exactly three deterministic orders — as declared, by subject, by effect — and deliberately no judgment sort, because a planning leaf has no change set to grade.
- `scope_paths` reads a packet's `## Scope` section as prose and keeps each backticked span that looks like a repository path once, in the order it is written.
- `_resolve` answers a code-tip path only when one reading is unambiguous; a path that two files or two directories answer is listed as text rather than guessed at.

## Evidence

- The one top line a planned page carries says there are no changes [1]
- Every planned diagram or claim carries the notice that it is intended and not a fact about the code [2]
- Only three deterministic sorts are offered, each a function of the declarations themselves [3]
- A packet's scope is read from its own prose as the backticked paths it names, each once [4]
- A scope path that two readings answer is listed as text, never resolved by preference [5]
- The whole payload is answered from the caller's reads, with no model turn and no agent start [6]
