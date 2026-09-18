# mcp/src/agents_remember/application/memory_quality/controller.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/memory_quality/controller.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-09-17T19:30+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l20-ar` uncommitted source; base `621db8981aba09a6f17880d2138cf76a37332c6c` |
| governingOverview | `../overview.md` |

## Governing Overview

[application/overview.md](../overview.md)

## Purpose

Owns the single typed sync/start/poll API for memory quality. It resolves canonical scope once,
forms complete run identity, executes the check, publishes leaf curator checklists when required,
and translates registry outcomes into stable public results.

## Code Commentary

### Logic

`run_memory_quality_request` executes an explicit sync request. `start_memory_quality_request`
resolves the same execution contract and admits it to the bounded registry; equivalent live work
returns its existing run, while full live capacity returns `capacity-reached` plus retry guidance.
`poll_memory_quality_request` accepts only configured `repo_id` and `run_id`, so a wrong repository
observes the same `run-not-found` result as an absent or evicted run.

`MemoryQualityExecution.identity` freezes repository, resolved scope, normalized checks,
`detail_limit`, and the report-publication decision. A full leaf check composes missing-onboarding,
route-index preview, drift rows, and commit-owned versus curator-owned findings into the one
enclosure-local checklist. Sync and async paths therefore share one execution implementation.

CCR-R08 (260831-CCR-L08) adds the final full catalog seam: after the curator checklist is
attached, `_attach_final_full_catalog` (444-480) projects the deterministic complete Gate-5
catalog onto the full run result through `final_catalog_readiness` (the package-owned
`ReadinessProjectionInput`), naming every item's typed status and the still-missing
certification authorities without ever claiming certification eligibility; `_catalog_checks`
(483-487) narrows the executed check payload for the projection. The projection requires the
exact pair identity and refuses otherwise.

Under CCR-R03@v1 curator-report publication is bound to the exact working-tree candidate: before
and after the primary scan, and again immediately before the checklist write, the controller
captures both candidate trees with `worktree_candidate_tree` (through scratch indexes outside the
repositories) and refuses `memory-quality-candidate-changed` if the code or memory candidate moved
while quality was running cit:([`_curator_candidate_inputs`, `_require_same_curator_candidate`], mcp/src/agents_remember/application/memory_quality/controller.py:545-564; mcp/src/agents_remember/application/memory_quality/controller.py:596-648).
The checklist writer receives `code_candidate_tree` and `memory_candidate_tree` so the attestation
can declare its exact pair/tree inputs cit:([`_execute_memory_quality`, `_attach_curator_checklist`], mcp/src/agents_remember/application/memory_quality/controller.py:318-360; mcp/src/agents_remember/application/memory_quality/controller.py:363-441).

Interactive quality execution resolves the exact scope before scanning and revalidates it after
the scan and before publication. A full leaf run joins its checklist with the same
`require_current_curator_coherence` validator used by closeout: unfinished memory repairs retain
`closeoutReady=false`; missing or stale coherence cannot become combined-ready. The deterministic
full catalog is a readiness projection, not final certification: this interactive route has no
Gate 1–4 certificate prefix or affected-closure plan and explicitly reports those missing
authorities. This permits preparatory memory work without claiming final acceptance.

cit:([`_resolve_execution`], mcp/src/agents_remember/application/memory_quality/controller.py:295-315)
cit:([`_execute_memory_quality`], mcp/src/agents_remember/application/memory_quality/controller.py:318-360)
cit:([`_attach_coherence_readiness`], mcp/src/agents_remember/application/memory_quality/controller.py:690-717)
cit:([`_attach_final_full_catalog`], mcp/src/agents_remember/application/memory_quality/controller.py:550-586)

### Invariants And Boundaries

- Public callers choose exactly one request mode; no flat legacy overload or inferred wait mode is
  accepted.
- Every result-affecting input is part of `QualityRunIdentity`; distinct work cannot alias.
- Capacity is a typed refusal with guidance, not an exception or an unbounded extra thread.
- Polling never discloses whether another configured repository owns the supplied run id.
- Curator-report publication is derived from resolved leaf scope and a full check, never from a
  caller-provided path.
- Curator publication requires the exact code/memory candidate trees frozen at start and unchanged
  through publication; a moved candidate refuses instead of publishing evidence under a new tree.

### Todos

None recorded.

## 260915-CAPS-L20 The Dead Governing Overview Becomes A Gated Finding

This leaf closed `D3`/`D16`'s **product** half and the consumer it feeds. Until it, the product
validated that a source *has* a card and never that the card's declared route *resolves*, so a card
whose `governingOverview` field — or whose `## Governing Overview` body link — pointed at a file that
does not exist passed every check the product runs and reported clean.

`_attach_curator_checklist` now calls `check_governing_overview_resolution(scope.onboarding_root)` and
publishes its summary on the **response** under `governingOverviewResolution`: the five counters
(`cardsWalked`, `cardsFlagged`, `unresolvedFieldCount`, `unresolvedLinkCount`, `sectionAbsentCount`),
the findings, and the observations. Two placements are deliberate rather than incidental. The summary
is attached to `response`, not to `payload`, because `response` is composed from `**payload` *before*
this function runs — a key added to `payload` here would never be published. And it stays **out of**
`response["checks"]`, because that mapping is the closed `AVAILABLE_CHECKS` population the
certification catalog is validated against, and a key outside that population would be a catalog item
with no planned identity.

The findings then join the gated set:

```python
repair_findings.extend(row.to_dict() for row in governing_overviews.findings)
```

`.findings`, never `.observations`, and that distinction carries the whole doctrine boundary. The 96
cards that declare a live field but carry no body link to resolve are **observations**: `ok` is
`not findings`, so a pure-observation tree is green and the 96 cannot reach
`curatorActionableCount`. Making them gated would create 96 new obligations layer-wide and change
shipped doctrine, so this leaf observes them and declines to decide whether each *should* carry a
link — that is the developer's call, recorded rather than taken.

**What the gating reaches, stated with its condition.** The findings reach the **curator's completion
loop** today: the full contract-scoped operation (no `checks` subset, which is what
`publish_curator_report` requires) publishes the count the curator iterates against. The
closeout-admission consumer is the *designed* one and is behind `D32`: the readiness comparison lives
inside `require_current_curator_coherence`, which the checklist only consults once the raw status is
`ready-for-closeout`, and no leaf on this master has ever reached it. Both statements are true, and
stating only the first would understate the fix while stating only the second would overstate today's
reach.

The standalone runner is the half an operator can drive without pytest:
`python -m agents_remember.memory_quality.integrity.governing_overview_resolution --onboarding-root
<root>` prints the five counters and one row per finding, and exits **non-zero** while any declaration
is dead. Before this leaf no command in the product could fail on a dead governing overview.

## Docs References

No configured Domain Documentation source applies; the controller contract is repository-internal.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The execution identity contains normalized checks, detail limit, publication semantics, and frozen scope. | `MemoryQualityExecution` | mcp/src/agents_remember/application/memory_quality/controller.py:72-89 |
| Sync, start, and poll are separate typed request entry points with capacity and nondisclosing poll translations. | `run_memory_quality_request`; `start_memory_quality_request`; `poll_memory_quality_request` | mcp/src/agents_remember/application/memory_quality/controller.py:110-120; mcp/src/agents_remember/application/memory_quality/controller.py:111-143; mcp/src/agents_remember/application/memory_quality/controller.py:146-208 |
| Full leaf checks compose and atomically publish the curator checklist. | `_execute_memory_quality`; `_attach_curator_checklist` | mcp/src/agents_remember/application/memory_quality/controller.py:318-360; mcp/src/agents_remember/application/memory_quality/controller.py:363-441 |
| R03 candidate-tree freezing and change refusal around curator publication. | `_curator_candidate_inputs`; `_require_same_curator_candidate` | mcp/src/agents_remember/application/memory_quality/controller.py:545-564; mcp/src/agents_remember/application/memory_quality/controller.py:596-648; mcp/src/agents_remember/application/memory_quality/controller.py:657-687 |

## Cross-Repo References

No meaningful cross-repository implementation reference applies.

## MCAR-L02 Combined Readiness

After a full leaf checklist is written, `_attach_coherence_readiness` preserves its raw
`qualityChecklistStatus` and invokes the same `require_current_curator_coherence` validator used by
closeout. A ready quality worklist with missing/stale coherence becomes
`checklistStatus=coherence-required`, `closeoutReady=false`; only a current record exposes its
digest and combined readiness. This prevents the public quality result and closeout admission from
selecting different artifacts.

## MCAR-L03 Exact Candidate Scope

Repository-only checks are now explicitly `official-diagnostic` and cannot produce candidate
acceptance. A candidate sync/start resolves the full pair before scanning, freezes it into async
run identity, and revalidates it before and after the primary scan. Full checklist publication
revalidates once more after missing-onboarding and route-index derivation, immediately before the
report/attestation write. Candidate polls must repeat the exact contract path and re-prove the
stored pair; a changed pair remains `scope-refused` rather than being relabelled as completed.

## 260831-CCR-R03 Exact-Candidate Checklist Publication

Curator publication now freezes both working-tree candidate trees in scratch indexes and refuses a
moved candidate before and after the scan and at the final write, so the attestation's declared
code/memory tree inputs always match the bytes it reports (worker handover:
notes/reports/260902-CCR-L03-worker-delivery.md).

## CCR-R08 Final Full Catalog Projection

After a full leaf checklist is written, `_attach_final_full_catalog` (controller.py:444-480)
projects the deterministic complete Gate-5 catalog onto the full run result: every standard
checker, the missing-onboarding and stale-route-index counts, the affected-closure item
(blocked until the plan digest is supplied), the coherence-record item (blocked without a
current record), and the candidate-pair item, each with a content-addressed subresult digest,
plus `finalizationEligible=false` and `fullFinalRequired=true`. The projection requires the
exact code/memory pair identity and never claims certification eligibility; the certification
executor compares it with the attested final catalog.

## CCR-L42 current candidate

Prepared candidate quality execution now uses the scope's quality code root and quality context, and withholds the unstamped fallback when a prepared code view is present; checklist missing-onboarding and route-index projections use the same quality input. This keeps quality evidence tied to the frozen candidate while preserving the controller's typed sync/start/poll and final-catalog boundaries.

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_attach_coherence_readiness` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:690-717. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: recorded this leaf's controller change — the governing-overview resolution summary is published on the response (not `payload`, not `checks`) and its findings are extended into the gated curator repair set, so a dead declaration now reaches the loop the curator completes against instead of reporting clean. The consumer boundary is stated with it: the curator loop binds today, while the closeout-admission consumer sits behind `D32` because the raw status has never reached `ready-for-closeout` on this master. Verification metadata advanced to this leaf's frozen code base.
- 2026-09-10T00:20:36+02:00 — CCR-L42 current candidate reconciliation: Prepared candidate quality execution now uses the scope's quality code root and quality context, and withholds the unstamped fallback when a prepared code view is present; checklist missing-onboarding and route-index projections use the same quality input. This keeps quality evidence tied to the frozen candidate while preserving the controller's typed sync/start/poll and final-catalog boundaries.
- 2026-09-08T14:45:44+00:00: CCR-L24 preparation reviewed `_attach_final_full_catalog`, `_curator_candidate_inputs`, and `_require_same_curator_candidate` against the current L38-composed code candidate; wording retained and ranges regenerated. Verification metadata remains pinned pending final pair composition.
- 2026-09-08T14:39:58+00:00: Generated citation repair: `_attach_coherence_readiness` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:600-627. No content impact: mechanical anchor-range projection bound to citation source snapshot 5911742cfcc7a53db92b36b80bac02ee49a67204b190c0311a81bcc2e388ad59; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T14:39:58+00:00: Generated citation repair: `_attach_final_full_catalog` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:499-535. No content impact: mechanical anchor-range projection bound to citation source snapshot 5911742cfcc7a53db92b36b80bac02ee49a67204b190c0311a81bcc2e388ad59; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: recorded the CCR-R08
  final full catalog projection seam (`_attach_final_full_catalog`/`_catalog_checks`, package-owned
  `final_catalog_readiness` on the full run result, pair-identity requirement) and re-anchored
  every controller citation the +57-line change shifted (identity 72-89, request surface 98-208,
  execute/attach 318-360/363-441, candidate guards 490-509/512-542). Verification metadata
  pinned to the owning commit 16d1a4d6.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the exact candidate-tree freeze/change guard for curator publication and the tree inputs passed to the checklist writer; prior mode, identity, and pair-scope prose preserved.

- 2026-08-29T21:46+02:00 — MCAR-L03: bound sync/start/poll and curator publication to one exact
  contract pair with pre-scan, post-scan, and final pre-publication refusal. Verification remains
  closeout-owned.

- 2026-08-29T08:52+02:00 — MCAR-L02 A005: joined raw memory quality with the sole structured
  coherence validator. Verification remains closeout-owned.

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: created for the canonical typed memory-quality controller and complete run identity. Verification remains blank until architect-owned closeout stamps the code commit.
