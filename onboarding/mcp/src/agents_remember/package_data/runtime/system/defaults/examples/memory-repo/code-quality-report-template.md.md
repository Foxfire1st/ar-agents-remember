# code-quality-report-template.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/code-quality-report-template.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T12:32+02:00                     |
| lastVerifiedCommitHash | `3f09b75461760479b443f1b04b180772724e7a24` |
| lastVerifiedCommitDate | 2026-05-28T15:10:01+02:00|
| governingOverview      | `../../../../../../../../overview.md`      |

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

### Conventions

- Report what tools actually found, not merely that tests were executed.
- Separate findings in touched files from inherited repository pressure.
- Adapt the template to the target repository before treating it as policy.

### Invariants And Boundaries

The packaged example is scaffold material. The authoritative quality-reporting
instructions for a real project belong in that project's selected memory layer,
usually beside `system/tools.md`.

### Todos

None.

## Docs References

No external documentation is needed for this template example.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The template says it is a memory-repo example to copy or adapt, then asks agents to report actual tool findings rather than only execution. | L1-L9 | [code-quality-report-template.md](agents-remember/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/code-quality-report-template.md) |
| The tool-results table is explicit but adaptable; the prose gives a TypeScript stack as a replacement example. | L18-L31 | [code-quality-report-template.md](agents-remember/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/code-quality-report-template.md) |
| The findings sections separate touched-file findings from existing or out-of-scope pressure. | L33-L51 | [code-quality-report-template.md](agents-remember/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/code-quality-report-template.md) |

## Cross-Repo References

The live memory layer carries a project-specific copy beside `system/tools.md`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The local memory-layer template is the project-specific copy used by `agents-remember` agents. | n/a | [system/code-quality-report-template.md](ar-coordination/memory-repos/ar-agents-remember/system/code-quality-report-template.md) |

## Update History

- 2026-05-28T12:32+02:00: Created after adding the packaged memory-repo example for quality-report transparency.
