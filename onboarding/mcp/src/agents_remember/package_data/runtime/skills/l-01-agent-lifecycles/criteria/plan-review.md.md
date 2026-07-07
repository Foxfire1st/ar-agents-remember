# l-01-agent-lifecycles/criteria/plan-review.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/plan-review.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T15:35+02:00 |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063` |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|

## Purpose

The plan-review criteria catalog — the fifth catalog in the new `criteria/` folder (leaf
260703-L12): what the adversarial reviewer runs against an **orchestration task** (the
strategist's sprint plan) in the portfolio three-party loop, before the developer's drawing
board. Its criteria are seeded by ruling (the developer's method challenge, 2026-07-06) rather
than by prior catches — the strategist loop had not run yet when the catalog was seeded.

## Code Commentary

### Logic

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/criteria/plan-review.md`. Five standing criteria: **PR-1 refute
uncited edges** (every dependency edge needs evidence — a tool query, file, decision-log, design
citation, or a declaration cross-reference for new surfaces; uncited = refutable by default),
**PR-2 missed-shared-surface hunt** (class-completeness applied to surface intersections:
re-intersect the per-leaf surface lists — existing AND declared-new, including CONFLICT-risk at a
shared parent route — and hunt omitted pairs), **PR-3 blast-radius re-derivation** (re-derive at
least the HIGH entries with `cgc_dependencies`/`cgc_callers`/`cgc_callees`; spot-check the rest),
**PR-4 order-respects-edges** (no ORDER edge runs backwards; CONFLICT pairs serialized or moved;
waves contain only INDEPENDENT pairs — the catalog's mechanization candidate), **PR-5 honesty of
the findings section** (unplannable-as-scoped must be genuine both ways — a not-yet-existing
surface is NOT unplannable; silently-guessed thin scopes are findings; quo-vadis flagged at the
top). Plus the exploratory mandate (default 2) and the promotion ratchet. The reviewer holds the
same read-only analysis tools the strategist used, so mechanical claims are re-derivable.

### Conventions

Catalog files live beside the templates under `criteria/` and are bound per review type by
`roles/reviewer.md`: the plan review runs this catalog + report-verification.

### Invariants And Boundaries

The standing list MUST run every time the catalog binds; amendments land only through the
promotion ratchet on the loop owner's (the orchestrator's) acceptance.

### Todos

PR-4 is named as the mechanization candidate (a topological check over a structured edge list);
no other TODO is recorded.

### Docs References

No external domain documentation applies to this repository-local catalog.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | n/a | [plan-review.md](agents-remember/skills/l-01-agent-lifecycles/criteria/plan-review.md) |
| The reviewer role that binds this catalog for the portfolio plan review. | n/a | [reviewer.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md) |
| The orchestration-task template whose shown-work sections these criteria attack. | n/a | [orchestration-task.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/orchestration-task.md) |
| The strategist whose eight-phase method produces the plan under review. | n/a | [strategist.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/strategist.md) |

## Cross-Repo References

No sibling repository evidence is needed for this catalog.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-06T15:35+02:00 — Created file-level onboarding for the new `criteria/plan-review.md` catalog (leaf 260703-L12): PR-1 refute uncited edges, PR-2 missed-shared-surface hunt (incl. declared-new surfaces and parent-route CONFLICT risk), PR-3 blast-radius re-derivation via cgc, PR-4 order-respects-edges, PR-5 findings honesty — the fifth catalog, seeded by ruling for the strategist loop. Verification metadata pinned until closeout stamps the L12 commit.
