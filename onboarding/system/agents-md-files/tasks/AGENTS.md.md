# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `system/agents-md-files/tasks/AGENTS.md`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-15T00:38+02:00                     |
| lastVerifiedCommitHash | `3a5e72d961b489a7ebb2071e73d0af2247d0ca34` |
| lastVerifiedCommitDate | 2026-05-15T00:52:32+02:00|

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
implementation sequencing rather than only a checklist.

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
| The template covers meta-questioning, task reframing, top-down/bottom-up design philosophy, assumptions, and truth gaps. | L1-L103 | [system/agents-md-files/tasks/AGENTS.md](agents-remember-md/system/agents-md-files/tasks/AGENTS.md) |
| Evidence-first reasoning and representative examples are required when correctness depends on interpretation or risky structure. | L105-L133 | [system/agents-md-files/tasks/AGENTS.md](agents-remember-md/system/agents-md-files/tasks/AGENTS.md) |
| The visible planning standard lists the context agents should surface before non-trivial implementation.             | L136-L153 | [system/agents-md-files/tasks/AGENTS.md](agents-remember-md/system/agents-md-files/tasks/AGENTS.md) |

## Cross-Repo References

No sibling repository evidence is needed for this task doctrine template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-15T00:38+02:00: Created onboarding after the former skills-folder task collaboration doctrine moved to the installable tasks template path. Verification metadata remains pinned to the last committed source until closeout.
