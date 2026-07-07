# l-01-agent-lifecycles/criteria/onboarding-memory.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/onboarding-memory.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T17:35+02:00 |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063` |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|

## Purpose

The onboarding/memory review criteria catalog — one of the five seed catalogs in the new
`criteria/` folder (leaf 260703-L12). Binds over the memory side of every change set: sidecars,
route overviews, route indexes, update histories (the onboarding-vs-code lens at both seams).

## Code Commentary

### Logic

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/criteria/onboarding-memory.md`. Two standing criteria with cited
catching evidence: **OM-1 staleness diff vs as-landed code** — as of round 2 (L12R-1) cited to the
verifiable record: two engagements — L8 cycle 6's OWNER follow-up pass (deleted canvas models in
the panels overview's build-job/frame tail; duplicated Layout-table rows in the tools and
controlplane overviews; all durably recorded in those overviews' own 2026-07-05T19:25 Update
History entries) and L10's flowModels-sidecar de-stale (its 2026-07-06T12:05 history entry +
L10R-3) — and **OM-2 history-only-update detection** ("refreshed" must mean a genuine body edit —
the L8 cycle-6 closeout-body-gate catch of overviews claimed refreshed but history-only). A
**Candidate Criteria** section (round 2, L12R-2) carries **OM-3 newest-first with the checker's
own semantics** at candidate tier (single catching engagement: L11's four parallel-wave history
collisions re-sorted with the checker's parse — naive as-is, tz-aware folds to UTC; promotes at
≥2). Plus the exploratory mandate (default 2 novel lenses) and the promotion ratchet, which notes
that the closeout body gate IS this catalog's OM-2 mechanized — the working example of a criterion
graduating into a gate.

### Conventions

Catalog files live beside the templates under `criteria/` and are bound per review type by
`roles/reviewer.md` (the binding table).

### Invariants And Boundaries

The standing list MUST run every time the catalog binds; amendments land only through the
promotion ratchet on the loop owner's acceptance.

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
| Canonical source this bundle copy is sync-propagated from. | n/a | [onboarding-memory.md](agents-remember/skills/l-01-agent-lifecycles/criteria/onboarding-memory.md) |
| The reviewer role that binds this catalog per review type. | n/a | [reviewer.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md) |
| The Update History order checker whose naive/UTC comparison semantics OM-3 pins. | n/a | [history_order.py](agents-remember/mcp/src/agents_remember/memory_quality/style/update_history/history_order.py) |

## Cross-Repo References

No sibling repository evidence is needed for this catalog.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-06T17:35+02:00 — 260703-L12 round 2: OM-1's catching evidence re-cited to the verifiable record (L12R-1: the L8 cycle-6 owner-pass overview de-stales in the 2026-07-05T19:25 history entries + L10's sidecar de-stale — two engagements, standing holds); OM-3 re-tiered STANDING → CANDIDATE (L12R-2: one catch, promotes at ≥2). Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T15:35+02:00 — Created file-level onboarding for the new `criteria/onboarding-memory.md` seed catalog (leaf 260703-L12): OM-1 staleness diff (cycle-6 deleted-models catch), OM-2 history-only detection (closeout-body-gate catch), OM-3 newest-first under the checker's naive/UTC semantics (L11 collision re-sort), with the exploratory mandate and the promotion ratchet. Verification metadata pinned until closeout stamps the L12 commit.
