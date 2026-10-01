# code-quality-report-template.md

## Governing Overview

[mcp/overview.md](../../../../../../../../overview.md)

## Purpose

This packaged example gives memory layers a starting shape for implementation
quality reports. It is intentionally an adaptable example, not a universal
assertion that every project uses the Agents Remember Python quality stack.

## Code Commentary

### Logic

The example tells agents to copy or adapt the template into a target memory
layer, then revise tools, thresholds, sections, and wording for the project's
real quality stack. The report shape includes summary, tool results,
in-scope findings, existing or out-of-scope findings, verification notes, and
follow-up.

The default table names Ruff, Pytest, Coverage, Radon, and CRAP-Calculator
because that is useful for this source checkout, but the text explicitly tells
agents to replace those rows for other stacks such as TypeScript projects using
ESLint, TypeScript, Vitest, Playwright, or bundle checks.

### A Row May Only Offer Results Its Tool Can Produce (260731-EFA-L2)

The Radon rows lost `passed` and `failed`. They now read
`<reported / not run>`, and the CRAP row lost `reported` and now reads
`<passed / failed / not run>`. New prose beside the table states the rule and the reason:

> `passed` is not one of Radon's: `radon cc` and `radon mi` exit 0 whatever they find, so
> a Radon run reports and never passes or fails. Offering `passed` invites a report to be
> recorded as a verdict, which is how a suite ends up looking greener than it is.

The rule generalises to every row a project adds: **if a tool cannot fail, do not give it
a result that says it did not.** That makes this template a teaching artifact for the
report-versus-enforcement distinction, not just a form.

### Conventions

- Report what tools actually found, not merely that tests were executed.
- Separate findings in touched files from inherited repository pressure.
- Adapt the template to the target repository before treating it as policy.
- Give each row only the verdict vocabulary its tool can actually produce.

### Invariants And Boundaries

The packaged example is scaffold material. The authoritative quality-reporting
instructions for a real project belong in that project's selected memory layer,
usually beside `system/tools.md`.

This file is a **generated copy**. The canonical source is root
`system/defaults/examples/memory-repo/code-quality-report-template.md`; edit that and run
`python3 scripts/sync-runtime.py`. The live `agents-remember` memory layer carries its own
project-specific copy, which received the same correction.

### Todos

None.

## Evidence

### Docs References

No external documentation is needed for this template example.

No relevant external documentation found.

### Repo-Internal References

- The template says it is a memory-repo example to copy or adapt, then asks agents to report actual tool findings rather than only execution. [1]
- The tool-results table is explicit but adaptable; the prose gives a TypeScript stack as a replacement example. [2]
- The findings sections separate touched-file findings from existing or out-of-scope pressure. [3]

### Cross-Repo References

The live memory layer carries a project-specific copy beside `system/tools.md`.

- The local memory-layer template is the project-specific copy used by `agents-remember` agents. [4]
