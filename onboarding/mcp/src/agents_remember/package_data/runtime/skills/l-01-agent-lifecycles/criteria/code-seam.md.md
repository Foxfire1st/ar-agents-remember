# l-01-agent-lifecycles/criteria/code-seam.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/code-seam.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T15:35+02:00 |
| lastVerifiedCommitHash | `bcaa78070f77c76f1c4db0af93786bb193b92523` |
| lastVerifiedCommitDate | 2026-07-06T07:51:05+02:00|

## Purpose

The code-seam review criteria catalog — one of the five seed catalogs in the new `criteria/`
folder (leaf 260703-L12), the reviewer-as-test-bench doctrine made durable: criteria are never
made up on the spot; the standing list is the regression floor every code-touching review runs.

## Code Commentary

### Logic

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/criteria/code-seam.md`. Three standing criteria, each with cited
catching evidence from the 260703-L8 adversarial loop: **CS-1 production-wiring walk** (trace the
real call path, never a hand-aligned harness — AR3-1, the inert integrate consumer behind a
passing hand-aligned test), **CS-2 fail-open hunt** (absent/mistyped addresses must fail closed —
AR4-1, the exact-string enclosure contract + enclosure-less raise refusal), **CS-3
validate-then-mutate** (refusal checks before any durable effect — the cycle-6 `wait=false`
rework). Plus the exploratory mandate (N novel lenses owed, default 2) and the promotion ratchet
(candidate → standing at ≥2 catches; standing → spot-check after N dry engagements, default 5;
mechanizable criteria graduate into gates — the closeout body gate is the working example).

### Conventions

Catalog files live beside the templates under `criteria/` and are bound per review type by
`roles/reviewer.md` (the binding table). Verdicts pair a per-criterion findings row with the
catalog and carry promotion proposals.

### Invariants And Boundaries

The standing list MUST run every time the catalog binds — reporting a criterion even when it
found nothing. Amendments land only through the promotion ratchet on the loop owner's acceptance,
never ad hoc.

### Todos

No TODO is recorded for this catalog.

### Docs References

No external domain documentation applies to this repository-local catalog.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | n/a | [code-seam.md](agents-remember/skills/l-01-agent-lifecycles/criteria/code-seam.md) |
| The reviewer role that binds this catalog per review type. | n/a | [reviewer.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md) |

## Cross-Repo References

No sibling repository evidence is needed for this catalog.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-06T15:35+02:00 — Created file-level onboarding for the new `criteria/code-seam.md` seed catalog (leaf 260703-L12): CS-1 production-wiring walk (AR3-1), CS-2 fail-open hunt (AR4-1), CS-3 validate-then-mutate, with the exploratory mandate and the promotion ratchet. Verification metadata pinned until closeout stamps the L12 commit.
