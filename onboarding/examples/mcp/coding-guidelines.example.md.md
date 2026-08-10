# coding-guidelines.example.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `examples/mcp/coding-guidelines.example.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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
**Responsibility Rules** per module archetype (CLI adapter, application entry point, service,
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found after checking the resolved sources registry (no Domain Documentation entries configured). | n/a | n/a |

## Repo-Internal References

This example is a generalized sibling of the coding-discipline ruleset Agents
Remember applies to its own memory layer (the repo's authority is its memory
`system/coding-guidelines.md`). The example carries the same structure —
file-size budgets, function/class budgets, split triggers, responsibility rules,
and anti-patterns — written language-general for teams to adapt.

| Finding | Anchor | Source |
| --- | --- | --- |
| The full guidelines body (design philosophy, budget tables, split triggers, responsibility rules, anti-patterns, naming, boolean-flag rule) lives in the source example. | `# Code Shape and Refactor Discipline` | examples/mcp/coding-guidelines.example.md:1-253 |
| The example sits in the `examples/mcp` route governed by the route overview, alongside `settings.example.json`. | `# examples/mcp Overview` | onboarding/examples/mcp/overview.md:1-90 |

## Cross-Repo References

No meaningful cross-repo references: this is standalone example content.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: No content impact: re-read the current staged example; its documented coding guidance remains accurate. Citation repair is recorded in the durable L9 curator report.
- 2026-08-02T16:46+02:00 — 260731-EFA-L6 curator W1-B03: repaired 2 citation rows with exact headings and source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation that ran past the end of the target. `examples/mcp/coding-guidelines.example.md` is 254 lines (ends mid-fence at the Boolean Flag Rule example), so the whole-body citation is now L1-L254 instead of L1-L255.
- 2026-05-30T21:30+02:00: Created the file-level onboarding sidecar for the previously-undocumented `examples/mcp/coding-guidelines.example.md`, closing the route's coverage gap surfaced during the S1 onboarding-drift refresh. Verified against `3f006e9`.
