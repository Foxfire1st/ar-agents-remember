# skills/l-01-agent-lifecycles/criteria/code-seam.md

## Governing Overview

[skills/l-01-agent-lifecycles overview](../overview.md)

## Purpose

The `code-seam` reviewer criterion: verify production wiring end to end, hunt fail-open
shapes, require validate-then-mutate, and prove quiescence (D1-D4) when a change touches a
reusable primitive or a feedback actor. It is the criteria-catalog home of the
escalation-storm catching evidence and the "no event, message, or row outranks system
health" ruled invariant.

## Code Commentary

### Logic

The criterion's D4 quiescence question demands a multi-cycle zero-input simulation for any
feedback actor whose output is a member of its own input class. Its ruled invariant says
notification rows coalesce — a re-firing condition updates its ONE existing row (date, tries,
attempt) and never appends a sibling. The catching evidence records the 2026-07-09
escalation-storm meltdown (every ladder rung transition minted a new pending row) as the D4
seed and the HFX2-L7 O(n^2) re-fold as the scaling seed.

### Conventions

Criterion files are reviewer-facing doctrine: candidate criteria get promoted with a second
catching engagement, and catching evidence must name the exact leaf/commit that caught the
defect class.

### Invariants And Boundaries

- The coalescing invariant is doctrine: one row per root cause, purgeable stores, and the
  durable artifact on disk never being the queue row.
- Since 260713-TES-L5 the wording says "date, tries, attempt" — "rung" is gone with the
  retired escalation ladder; the escalation-storm history stays as catching evidence, not a
  live mechanism.

### Todos

None.


## CCR-R12@v5 Review Scope

This criteria catalog supplies evidence only when the corresponding review is explicitly requested. It does not create a closeout or integration prerequisite; routine handoff uses the worker and curator targeted/scoped check records and preserves any failed or not-run state.

## Evidence

### Docs References

No relevant external documentation found after checking the resolved source registry; the
reviewer criteria catalog and the cited catching leaves are the authority.

- No external/domain document defines this criterion; catching evidence is leaf-cited. [1]

### Repo-Internal References

- The canonical criterion file's standing/candidate structure, mirrored into the packaged runtime copies. [2]

### Cross-Repo References

No meaningful cross-repo references found.

Same-repository reviewer doctrine only.

## Inherited Source-Epoch Commentary

The following account preserves the former distribution-copy card and its useful explanations, history and warnings. It is inherited scope, not a second current contract or a fresh certification of its dated/currentness, tool, provider, registry, execution or permission claims. The canonical account above retains its existing attribution and qualifications; the authored source below is the authority for the file. Historical reference labels in this quotation are provenance labels, not reference identities of this card.

> # l-01-agent-lifecycles/criteria/code-seam.md
>
> ## Governing Overview
>
> [MCP package overview](../../../../../../../overview.md)
>
> ## Purpose
>
> The code-seam review criteria catalog — one of the five seed catalogs in the new `criteria/`
> folder (leaf 260703-L12), the reviewer-as-test-bench doctrine made durable: criteria are never
> made up on the spot; the standing list is the regression floor for an explicitly requested
> code-touching review.
>
> ## Code Commentary
>
> ### Logic
>
> Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
> `skills/l-01-agent-lifecycles/criteria/code-seam.md`. Three standing criteria, each with cited
> catching evidence from the 260703-L8 adversarial loop: **CS-1 production-wiring walk** (trace the
> real call path, never a hand-aligned harness — AR3-1, the inert integrate consumer behind a
> passing hand-aligned test), **CS-2 fail-open hunt** (absent/mistyped addresses must fail closed —
> AR4-1, the exact-string enclosure contract + enclosure-less raise refusal), **CS-3
> validate-then-mutate** (refusal checks before any durable effect — the cycle-6 `wait=false`
> rework). A **Candidate Criteria** tier carries **CS-4 reused-primitive affordance parity**
> (seeded at 260703-L17's review — single catch L17R-2, the DualPane markdown path silently
> dropping the truncation banner) and **CS-5 cross-repo side-effect safety** (seeded at
> 260703-L18 from finding 7's CLEAN exemplar — the mid-`worktree_start` official-memory-repo
> ledger write passing validate-then-mutate, partial-failure, dirty-target, and format-round-trip
> analysis; 0 catches). **CS-6 scaling & reclamation** is now promoted into the standing regression
> floor after two catches. It requires D1 stability, D2 bounded work/storage, D3 same-change
> reclamation proven at two sizes, and D4 zero-input quiescence/fixed-point proof for feedback
> actors. Its health-first invariant rejects immortal queue rows: notifications coalesce, pending
> rows expire, hard caps evict, and durable truth lives in artifacts. CS-6 also records the mechanization seam:
> HFX2-L7 owns the first executable counterparts, and CS-6 graduates into a gate once a reusable
> repo-wide scaling-test helper exists. Plus the exploratory mandate (N novel lenses owed, default
> 2) and the promotion ratchet (candidate → standing at ≥2 catches; standing → spot-check after N
> dry engagements, default 5; mechanizable criteria graduate into gates — the closeout body gate is
> the working example).
>
> ### Conventions
>
> Catalog files live beside the templates under `criteria/` and are bound per review type by
> `roles/reviewer.md` (the binding table). Verdicts pair a per-criterion findings row with the
> catalog and carry promotion proposals.
>
> ### Invariants And Boundaries
>
> When a code review is explicitly requested, the bound standing list, including promoted CS-6, runs
> and reports each criterion even when it found nothing. The catalog is evidence for that review and
> does not create a closeout or integration prerequisite; amendments land only through the promotion
> ratchet on the loop owner's acceptance, never ad hoc.
>
> ### Todos
>
> CS-6 records a future mechanization seam: once a reusable repo-wide scaling-test helper exists, it
> graduates into a gate. No separate immediate TODO is recorded for this catalog.
>
>
> ## CCR-R12@v5 Review Scope
>
> This criteria catalog supplies evidence only when the corresponding review is explicitly requested. It does not create a closeout or integration prerequisite; routine handoff uses the worker's targeted-check record together with the curator's complete memory-quality result and preserves any failed or not-run state.
>
> ### Docs References
>
> No external domain documentation applies to this repository-local catalog.
>
> No relevant external documentation found.
>
> ## Evidence
>
> ### Repo-Internal References
>
> - This package-data catalog copy carries promoted CS-6 scaling and reclamation with D1-D4, the health-first queue invariant, two catching engagements, and the future gate mechanization seam. (historical reference 1)
> - Root `skills/` is the canonical source tree and `scripts/sync-skills.py` propagates it into the MCP package-data copy and all eight harness package copies. (historical reference 2)
> - The reviewer role binds `code-seam` at master-exit, super-exit, and applicable leaf full-loop reviews, and keeps the promotion ratchet as the catalog amendment path. (historical reference 3)
>
> ### Cross-Repo References
>
> No sibling repository evidence is needed for this catalog.
>
> No meaningful cross-repo references found.
>
> ## 260713-TES-L5 Current Delta — Coalescing Invariant Wording (synced copy)
>
> This synced runtime copy of the `code-seam` criterion now says a re-firing condition updates
> its ONE existing row "(date, tries, attempt)" — the "rung" wording is gone with the retired
> escalation ladder. The escalation-storm catching evidence remains as historical D4 seed, not
> a live mechanism.

Inherited reference 1 commentary (not a revalidated target):

> This package-data catalog copy carries promoted CS-6 scaling and reclamation with D1-D4, the health-first queue invariant, two catching engagements, and the future gate mechanization seam.
>
> Anchor: `### CS-6 — Scaling & reclamation *(promoted — 2 catches)*`

Inherited reference 2 commentary (not a revalidated target):

> Root `skills/` is the canonical source tree and `scripts/sync-skills.py` propagates it into the MCP package-data copy and all eight harness package copies.

Inherited reference 3 commentary (not a revalidated target):

> The reviewer role binds `code-seam` at master-exit, super-exit, and applicable leaf full-loop reviews, and keeps the promotion ratchet as the catalog amendment path.
>
> Anchor: "The catalogs your review type binds"; `code-seam`; `## Promotion Ratchet`

## Canonical Source Ownership

The authored file is the canonical contract; its measured byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. The following whole-file reference locates that authored contract; it does not convert inherited statements into executed or whole-card acceptance.

- The authored source owns this contract; the distribution copy is not a separate authority. [3]
