# C-02-onboarding-drift-detection/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-02-onboarding-drift-detection/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T22:57                           |
| lastVerifiedCommitHash | `bb95b9956d55c70555bbbbcd236ca9ab62cd7261` |
| lastVerifiedCommitDate | 2026-05-09T22:15                           |

## Purpose

This skill defines C-02, the drift-detection gate for onboarding. It checks whether onboarding metadata still matches source files and routes actionable maintenance to C-05.

## Code Commentary

### Logic

The skill instructs agents to use C-08 for memory/coordination context resolution, run the drift helper, inspect classifications, and treat drifted, missing-verification, orphaned, unsupported, or missing units as trust problems before relying on onboarding.

### Conventions

C-02 reports trust state; it does not rewrite onboarding. It supports sidecar and inline storage models under the resolved onboarding root and writes Markdown reports as local coordination artifacts under the resolved coordination root.

### Invariants And Boundaries

C-02 must stay read-only with respect to onboarding content. Any content update belongs to C-05. Drift reports are temporary evidence, not durable onboarding.

### Todos

Add tests for C-02 against a migrated shared memory repo once such a fixture exists.

### Docs References

No external domain documentation applies to this repository-local maintenance skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

C-02 is the trust gate used before implementation and after onboarding maintenance.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The skill outputs classifications and a C-05 handoff worklist. | L16-L21 | [C-02 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-02-onboarding-drift-detection/SKILL.md) |
| The helper writes a report and supports JSON, CSV, and text output. | L34-L54 | [C-02 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-02-onboarding-drift-detection/SKILL.md) |
| Resolution must use C-08 and handle sidecar or inline storage. | L58-L64 | [C-02 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-02-onboarding-drift-detection/SKILL.md) |
| Metadata comparison and classification rules establish which onboarding can be trusted. | L66-L93 | [C-02 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-02-onboarding-drift-detection/SKILL.md) |
| C-02 hands content maintenance to C-05 rather than editing onboarding directly. | L132-L154 | [C-02 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-02-onboarding-drift-detection/SKILL.md) |

## Cross-Repo References

No cross-repo evidence is needed for the current skill contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-09T21:15: Created first file-level onboarding baseline for C-02 skill documentation.
- 2026-05-09T21:59: Updated after C-08 split memory roots from coordination roots.
- 2026-05-09T22:57: Refreshed verification metadata and clarified that reports are coordination artifacts.
