# C-03-repo-bootstrap/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T22:57                           |
| lastVerifiedCommitHash | `bb95b9956d55c70555bbbbcd236ca9ab62cd7261` |
| lastVerifiedCommitDate | 2026-05-09T22:15                           |

## Purpose

This skill describes repository onboarding bootstrap.

## Code Commentary

### Logic

C-03 resolves context with C-08, uses the resolved onboarding root as the write target, and builds repo overview coverage through scout, deep-dive, synthesis, and optional deepening phases.

### Conventions

Internal bootstrap uses `ar-memory/`; shared bootstrap uses the selected per-repo memory repo under `ar-management/memory-repos/ar-<repo-name>/`.

### Invariants And Boundaries

C-03 writes durable onboarding, not task coordination state. Task artifacts stay in the coordinator, and area findings merge back into the single repo overview rather than permanent nested overview layers.

### Todos

If bootstrap gains executable helpers, use C-08's `memory_root`, `coordination_root`, `sources_path`, and `tools_path` fields directly rather than deriving paths from prose.

### Docs References

No external documentation is needed for this repository-local skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| C-03 bootstraps repo overview coverage, uses bounded phases, and writes durable artifacts rather than loading an entire repo into one context. | L8-L22 | [C-03 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |
| The skill relies on C-08 for topology-aware internal/shared roots and path-rule eligibility. | L28-L30; L51-L58 | [C-03 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |
| Later passes merge component findings back into the repo overview and invoke C-05 for file-level onboarding. | L616-L641 | [C-03 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |
| The routing table distinguishes full bootstrap from smaller direct overview/file-level updates. | L725-L741 | [C-03 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-09T21:59: Created onboarding after C-03 was aligned to the resolved memory root model.
- 2026-05-09T22:57: Refreshed verification metadata and expanded source-backed references.
