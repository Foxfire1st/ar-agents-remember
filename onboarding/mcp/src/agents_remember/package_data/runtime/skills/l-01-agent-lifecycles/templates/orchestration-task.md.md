# l-01-agent-lifecycles/templates/orchestration-task.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/orchestration-task.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T02:39+02:00 |
| lastVerifiedCommitHash | `79b2fd6c4da73c7845406f6c68b947b8bd0e1009` |
| lastVerifiedCommitDate | 2026-07-10T22:22:16+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The tenth template: the **orchestration task** — the sprint plan and scope. After an approved
strategist pass, the orchestrator adopts the strategist's accepted draft into durable task form.
After a developer-sanctioned strategist skip, the orchestrator authors and adopts it from the
developer-ruled plan and records that source in the decision log. The template's defining property is that it **REQUIRES the
shown work per section** — the plan is refutable evidence, not narrative.

## Code Commentary

### Logic

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/templates/orchestration-task.md`. Six rules bind the shape: (1)
shown work per section — every dependency edge carries evidence (tool query, file, decision-log
entry, design-section citation, or a **declaration cross-reference** for new surfaces); every
blast-radius entry names its derivation (caller-set / doctrine-propagation / migration /
user-visible); every leaf move carries from→to + rationale; (2) surfaces are **two-sided** —
existing (route-map-mapped) vs new (declared: parent route/location + intended shape); new-surface
edges come from declaration cross-reference (a pure ORDER edge when leaf B names what leaf A
creates; a CONFLICT-risk edge at a shared parent route); (3) honest failures — "unplannable as
scoped" fires only when a leaf can name neither existing surfaces nor a parent anchor, and
quo-vadis contradictions sit at the top of the coherence findings; (4) draft-for-adoption; (5)
adversarial plan review (`criteria/plan-review.md`) before the drawing board, revisions appending
round sections; (6) the adopted artifact is the sprint's standing scope with the re-evaluation
rules. Shape sections: header table (strategist · masters in scope · status · round) · Sprint
Scope (IN/OUT + why) · Touch Surfaces (two-sided per leaf) · Dependency Graph (edge table with
kind + evidence) · Blast-Radius Register (feeds loop-tier scoring) · Leaf Moves · Coherence
Findings (quo-vadis first; unplannable-as-scoped) · Sprint Order/Waves (landing-reconciliation
cost noted) · Open Risks · Re-Evaluation Triggers · Evidence Inventory.

### Conventions

Same template idiom as the other nine: a `# <Name> Template` header, an intro naming author
(strategist) and consumer (orchestrator), a Rules list, and a fenced `md` Shape block with
placeholder slots. Lives beside the other templates; drafted under the series/coordination
`notes/` path the brief names.

### Invariants And Boundaries

An uncited edge is refutable by default — the plan-review catalog's first standing criterion
attacks exactly this. A strategist-produced artifact is a **notes draft until adopted**; the
orchestrator also owns the alternate author-and-adopt path after a sanctioned skip. Either path
requires an adoption decision-log entry before Job O. Wiring it as a first-class dashboard/task-doc
kind is deferred to the L14 hierarchy work.

### Todos

No TODO is recorded for this template beyond the deferred L14 first-class wiring.

### Docs References

No external domain documentation applies to this repository-local template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | n/a | [orchestration-task.md](agents-remember/skills/l-01-agent-lifecycles/templates/orchestration-task.md) |
| The strategist role that fills this template as method phase 8. | n/a | [strategist.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/strategist.md) |
| The plan-review criteria catalog the reviewer runs against a filled orchestration task. | n/a | [plan-review.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/plan-review.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-10T02:39+02:00 — HFX3/L14 combined curation: replaced the mandatory-strategist premise
  with the two valid authorship paths—approved strategist draft or orchestrator-authored task after
  a sanctioned skip—and preserved adoption plus shown-work requirements. Added the governing
  overview backlink. Verification metadata remains pinned until closeout stamps the eventual
  two-parent code commit.

- 2026-07-06T15:35+02:00 — Created file-level onboarding for the new `templates/orchestration-task.md` (leaf 260703-L12): the tenth template — the strategist's sprint plan with mandatory shown work (evidence-cited edges incl. declaration cross-references, derivation-named blast radii, from→to leaf moves, honest unplannable-as-scoped findings). Verification metadata pinned until closeout stamps the L12 commit.
