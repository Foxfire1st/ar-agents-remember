# l-01-agent-lifecycles/criteria/code-seam.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/code-seam.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T02:39+02:00 |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce` |
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

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
rework). A **Candidate Criteria** tier carries **CS-4 reused-primitive affordance parity**
(seeded at 260703-L17's review — single catch L17R-2, the DualPane markdown path silently
dropping the truncation banner) and **CS-5 cross-repo side-effect safety** (seeded at
260703-L18 from finding 7's CLEAN exemplar — the mid-`worktree_start` official-memory-repo
ledger write passing validate-then-mutate, partial-failure, dirty-target, and format-round-trip
analysis; 0 catches). **CS-6 scaling & reclamation** is now promoted into the standing regression
floor after two catches. It requires D1 stability, D2 bounded work/storage, D3 same-change
reclamation proven at two sizes, and D4 zero-input quiescence/fixed-point proof for feedback
actors. Its health-first invariant rejects immortal queue rows: notifications coalesce, pending
rows expire, hard caps evict, and durable truth lives in artifacts. CS-6 also records the mechanization seam:
HFX2-L7 owns the first executable counterparts, and CS-6 graduates into a gate once a reusable
repo-wide scaling-test helper exists. Plus the exploratory mandate (N novel lenses owed, default
2) and the promotion ratchet (candidate → standing at ≥2 catches; standing → spot-check after N
dry engagements, default 5; mechanizable criteria graduate into gates — the closeout body gate is
the working example).

### Conventions

Catalog files live beside the templates under `criteria/` and are bound per review type by
`roles/reviewer.md` (the binding table). Verdicts pair a per-criterion findings row with the
catalog and carry promotion proposals.

### Invariants And Boundaries

The standing list, including promoted CS-6, MUST run every time the catalog binds — reporting a criterion even when it
found nothing. Amendments land only through the promotion ratchet on the loop owner's acceptance,
never ad hoc.

### Todos

CS-6 records a future mechanization seam: once a reusable repo-wide scaling-test helper exists, it
graduates into a gate. No separate immediate TODO is recorded for this catalog.

### Docs References

No external domain documentation applies to this repository-local catalog.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| This package-data catalog copy carries promoted CS-6 scaling and reclamation with D1-D4, the health-first queue invariant, two catching engagements, and the future gate mechanization seam. | L63-L84 | [code-seam.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/code-seam.md) |
| Root `skills/` is the canonical source tree and `scripts/sync-skills.py` propagates it into the MCP package-data copy and all eight harness package copies. | L14-L15; L43-L55 | [scripts/sync-skills.py](agents-remember/scripts/sync-skills.py) |
| The reviewer role binds `code-seam` at master-exit, super-exit, and applicable leaf full-loop reviews, and keeps the promotion ratchet as the catalog amendment path. | L56-L74 | [reviewer.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md) |

## Cross-Repo References

No sibling repository evidence is needed for this catalog.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-10T02:39+02:00 — HFX3 retro curation: refreshed CS-6 from candidate/D1-D3 wording to
  its promoted standing form, including D4 zero-input quiescence and the developer-ruled
  health-first notification contract. Added the governing-overview backlink. Verification metadata
  remains pinned until closeout stamps the eventual two-parent code commit.

- 2026-07-09T10:40+02:00 — 260707-HFX2-L8: refreshed after synced CS-6 scaling &
  reclamation entered the code-seam candidate catalog with HFX2-L7 catching evidence and a
  mechanization seam for future gate promotion. Verification metadata pinned until closeout stamps
  the HFX2-L8 commit.

- 2026-07-07T20:55+02:00 — agent-orchestration L18: body de-staled to the current catalog — the Candidate tier now carries CS-4 (reused-primitive affordance parity, seeded at L17's review, one catch) and CS-5 (cross-repo side-effect safety, seeded at L18 from finding 7's clean exemplar). Covers both the 984a303 direct commit (CS-4, previously unreflected in this sidecar) and this leaf's sync. Verification metadata pinned until closeout stamps the L18 commit.
- 2026-07-06T15:35+02:00 — Created file-level onboarding for the new `criteria/code-seam.md` seed catalog (leaf 260703-L12): CS-1 production-wiring walk (AR3-1), CS-2 fail-open hunt (AR4-1), CS-3 validate-then-mutate, with the exploratory mandate and the promotion ratchet. Verification metadata pinned until closeout stamps the L12 commit.
