# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/agents-md-files/tasks/AGENTS.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-01T11:18+02:00                     |
| lastVerifiedCommitHash | `3113f8b877d670e15df17349de186b1bcbc6b629` |
| lastVerifiedCommitDate | 2026-06-01T13:10:08+02:00|

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
`C-04-retrieval-strategy-router`.

### Conventions

This is a doctrine file rather than a task instance. It uses broad behavioral
rules that apply to task planning and review, while the concrete W-02/W-01 task
formats still own the artifact structure for individual tasks.

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

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

This onboarding is backed by the source template itself.

| Finding                                                                                                              | Citations | Source Path |
| -------------------------------------------------------------------------------------------------------------------- | --------- | ----------- |
| The template covers meta-questioning, task reframing, top-down/bottom-up design philosophy, assumptions, and truth gaps. | L1-L103 | [mcp/src/agents_remember/package_data/runtime/agents-md-files/tasks/AGENTS.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/agents-md-files/tasks/AGENTS.md) |
| Evidence-first reasoning and representative examples are required when correctness depends on interpretation or risky structure. | L105-L133 | [mcp/src/agents_remember/package_data/runtime/agents-md-files/tasks/AGENTS.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/agents-md-files/tasks/AGENTS.md) |
| The visible planning standard lists the context agents should surface before non-trivial implementation.             | L136-L153 | [mcp/src/agents_remember/package_data/runtime/agents-md-files/tasks/AGENTS.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/agents-md-files/tasks/AGENTS.md) |

## Cross-Repo References

No sibling repository evidence is needed for this task doctrine template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-06-01T11:18+02:00: Documented the new title preamble (the task collaboration doctrine applies up front, before a task format is chosen or task file exists) and the `C-04-retrieval-strategy-router` route added to Evidence-First Reasoning. Verification metadata stays pinned; Repo-Internal Reference line ranges and the `Runtime AGENTS Template Package` entity fingerprint will be re-verified/recomputed at closeout.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-15T00:38+02:00: Created onboarding after the former skills-folder task collaboration doctrine moved to the installable tasks template path. Verification metadata remains pinned to the last committed source until closeout.
