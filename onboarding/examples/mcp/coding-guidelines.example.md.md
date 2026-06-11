# coding-guidelines.example.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `examples/mcp/coding-guidelines.example.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-30T21:30+02:00                     |
| lastVerifiedCommitHash | `3f006e9b25d62d689c5a60906ef508d12c5db699` |
| lastVerifiedCommitDate | 2026-05-27T14:20:42+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`coding-guidelines.example.md` is a ready-to-adapt example body for a memory
layer's `system/coding-guidelines.md`. It is the second public example shipped
under `examples/mcp/` (alongside `settings.example.json`) and exists so teams
can copy a concrete, opinionated "Code Shape and Refactor Discipline" ruleset
into their own memory repo instead of starting from a blank guidelines file.

It is documentation-shaped example content, not a runtime input: nothing in the
MCP server, providers, or skills reads this file. Its value is as a starting
template a human curates per repository.

## Code Commentary

### Logic

The document is a structured guidelines body, not code. It defines: a design
philosophy (every concept gets a clear home; files stay small enough to
understand without re-reading half the project); a **File Size Budget** table
(0-300 healthy … 4000+ emergency cleanup) keyed to required agent behavior; a
**Function and Class Budget** table (function <= 40 lines, class <= 250, <= 10
public methods, <= 5 args, cyclomatic complexity <= 10); **Split Triggers** (new
noun / new lifecycle phase / new external boundary / two concerns / >600 lines);
**Responsibility Rules** per module archetype (CLI adapter, controller, service,
policy, adapter/provider, parser, reporter, model); an **Anti-Patterns** list of
ten drift rationalizations; a **Refactor-First Rule** sequence for large files;
**Naming Rules** (boring ownership names; `utils.py` only for tiny shared
primitives); and a **Boolean Flag Rule** against mode-flag accretion.

It is deliberately language-general (it says "source code files" and labels the
naming section "Python example") so it can seed guidelines for any stack, while
this repo's own committed `system/coding-guidelines.md` is the Python-specific
descendant of the same ruleset.

### Conventions

- Keep it example/template-shaped: opinionated and concrete, but framed as a
  starting point a repo curates, not as binding rules for this source tree.
- Keep it language-general where practical; mark language-specific guidance as
  an example (as the naming section already does).

### Invariants And Boundaries

- This file is example content under `examples/mcp/`; it must not be treated as
  the authoritative guidelines for `agents-remember` itself. The authority for
  this repo is its memory layer's `system/coding-guidelines.md`.
- No runtime component reads this file. Changing it does not change MCP, provider,
  or skill behavior.
- Keep it aligned in spirit with the repo's real `system/coding-guidelines.md`
  so the public example does not contradict the discipline the project actually
  applies to its own code.

### Todos

None.

## Docs References

No external domain documentation proves this file; it is a same-repository
example of an Agents Remember memory-layer guidelines body.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found after checking the resolved sources registry (no Domain Documentation entries configured). | n/a | n/a |

## Repo-Internal References

This example is a generalized sibling of the coding-discipline ruleset Agents
Remember applies to its own memory layer (the repo's authority is its memory
`system/coding-guidelines.md`). The example carries the same structure —
file-size budgets, function/class budgets, split triggers, responsibility rules,
and anti-patterns — written language-general for teams to adapt.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The full guidelines body (design philosophy, budget tables, split triggers, responsibility rules, anti-patterns, naming, boolean-flag rule) lives in the source example. | L1-L255 | [coding-guidelines.example.md](agents-remember/examples/mcp/coding-guidelines.example.md) |
| The example sits in the `examples/mcp` route governed by the route overview, alongside `settings.example.json`. | n/a | [overview.md](overview.md) |

## Cross-Repo References

No meaningful cross-repo references: this is standalone example content.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-30T21:30+02:00: Created the file-level onboarding sidecar for the previously-undocumented `examples/mcp/coding-guidelines.example.md`, closing the route's coverage gap surfaced during the S1 onboarding-drift refresh. Verified against `3f006e9`.
