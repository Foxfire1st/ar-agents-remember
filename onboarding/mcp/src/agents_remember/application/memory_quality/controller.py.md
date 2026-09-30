# mcp/src/agents_remember/application/memory_quality/controller.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/memory_quality/controller.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T04:44:12+02:00 |
| lastVerifiedCommitHash | `31d761a241055d67b85ef3908033856b78a86a57` |
| lastVerifiedCommitDate | 2026-09-30T05:10:40+02:00|
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
while quality was running cit:([`_curator_candidate_inputs`, `_require_same_curator_candidate`], mcp/src/agents_remember/application/memory_quality/controller.py:852-871; mcp/src/agents_remember/application/memory_quality/controller.py:880-910).
The checklist writer receives `code_candidate_tree` and `memory_candidate_tree` so the attestation
can declare its exact pair/tree inputs cit:([`_execute_memory_quality`, "candidate_inputs=candidate_inputs", `_attach_curator_checklist`], mcp/src/agents_remember/application/memory_quality/controller.py:393-467; mcp/src/agents_remember/application/memory_quality/controller.py:517-681).

Interactive quality execution resolves the exact scope before scanning and revalidates it after
the scan and before publication. A full leaf run joins its checklist with the same
`require_current_curator_coherence` validator used by closeout: unfinished memory repairs retain
`closeoutReady=false`; missing or stale coherence cannot become combined-ready. The deterministic
full catalog is a readiness projection, not final certification: this interactive route has no
Gate 1–4 certificate prefix or affected-closure plan and explicitly reports those missing
authorities. This permits preparatory memory work without claiming final acceptance.

cit:([`_resolve_execution`], mcp/src/agents_remember/application/memory_quality/controller.py:370-390)
cit:([`_execute_memory_quality`, "revalidate_memory_candidate_scope"], mcp/src/agents_remember/application/memory_quality/controller.py:388-459)
cit:([`_attach_coherence_readiness`], mcp/src/agents_remember/application/memory_quality/controller.py:956-983)
cit:([`_attach_coherence_readiness`], mcp/src/agents_remember/application/memory_quality/controller.py:956-983)
cit:([`_attach_final_full_catalog`], mcp/src/agents_remember/application/memory_quality/controller.py:806-842)

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

## 260928-MIK-L24 The Unconverted-Line Refusal (MIK-R24 Rule 9)

`_execute_memory_quality` now asks `worktrees/knowledge_crossing.unconverted_line_refusal` first, for
every contract-scoped run whose contract names a memory worktree. When the leaf's memory tree has no
`knowledge/layout.json` but the tip of its official memory branch has one, the run returns
`{ok: false, state: "refused", code: "unconverted-memory", detail}` without scanning. The detail names
the crossing sync (`worktree_sync`) as the only way such a leaf converts.

- **Inert until the official line is converted (architect ruling, 2026-09-29).** The refusal fires only
  when the official line holds the layout marker, and no line does until MIK-R37 converts this master's
  line. Until then every run behaves exactly as before.
- **Conversion and crossing are separate routes.** The crossing sync is only for lines that descend
  from a converted official line. An unconverted official line, or a repository without one, converts by
  running `agents-remember knowledge-convert` on that line and committing it through its normal route.
- Repository-only runs (no contract) are not affected.

| Finding | Anchor | Source |
| --- | --- | --- |
| The refusal runs before any scan and returns a refused result naming the crossing sync. | `_execute_memory_quality`; `unconverted_line_refusal` | mcp/src/agents_remember/application/memory_quality/controller.py:393-467; mcp/src/agents_remember/worktrees/knowledge_crossing.py:163-195 |

## 260928-MIK-L28 The "Invariants Without Proof" Input (MIK-R28 Rule 5)

`_attach_curator_checklist` now passes `without_proof=_without_proof(<memory root>, config.coordination_root)`
to the checklist. `_without_proof` asks `application/knowledge_proofs.invariants_without_proof` for the
memory tree and turns its rows into `WithoutProof`. For every unconverted tree, which is every tree before
MIK-R37, it returns `None`, and the checklist renders nothing new.

- **Information, not a gate (architect ruling, 2026-09-29).** The list stays in the rendered checklist
  only. It never enters `curatorActionableCount`, the attestation or the strict wire summary; no count
  field is added.
- The tree's index comes from the coordination index cache when a coordination root is configured. A tree,
  index or cache that cannot be read becomes a `problem` line in the section, never an exception, so the
  run that shows the list cannot fail because of it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The checklist receives the list; `None` for an unconverted tree. | `_attach_curator_checklist`; `_without_proof` | mcp/src/agents_remember/application/memory_quality/controller.py:517-681; mcp/src/agents_remember/application/memory_quality/controller.py:762-773; mcp/src/agents_remember/application/memory_quality/controller.py:736-747; mcp/src/agents_remember/application/memory_quality/controller.py:695-706 |

## 260928-MIK-L08 The Leaf's Change-To-Knowledge Worklist (MIK-R08 Rules 7 And 8)

`_execute_memory_quality` now recomputes the leaf's worklist right after preparing the census:
`_knowledge_worklist(scope)` calls `application/knowledge_worklist.recompute_leaf_worklist(scope.contract)`
for a contract-scoped run and returns `None` for every other scope. `recompute_leaf_worklist` computes,
persists `knowledge-worklist.json` beside the series contract and never raises; it returns `None` where no
worklist applies (both memory sides unconverted, which is every production leaf before MIK-R37).

- When a worklist exists, the response gains `knowledgeWorklist` (`worklist_summary`: state, path, digest,
  item count, counts by kind, unreadable inputs), and the checklist receives `knowledge_worklist` and
  `knowledge_worklist_path`, rendered as the "Knowledge worklist (MIK-R08)" section.
- The census and the worklist travel to `_attach_curator_checklist` together as `_PreparedInputs(census,
  worklist)`, keeping the function within the argument and statement limits; the old `census=` keyword is
  now `prepared=`.
- **Information, not a gate.** The section never counts toward `curatorActionableCount`, the attestation or
  the wire counts; what an open item blocks is MIK-R09's closeout gate.
- **Trigger split (architect ruling 1).** This run is one of the two triggers L08 wires; the other is
  managed-sync completion. Closeout validation and landing pre-commit evaluation are L09's, through the same
  `recompute_leaf_worklist`.
- **Unconverted runs are unchanged:** with no worklist, neither the response field nor the section appears.

| Finding | Anchor | Source |
| --- | --- | --- |
| The worklist is recomputed after the census and summarized in the response. | `_knowledge_worklist`; `worklist_summary` | mcp/src/agents_remember/application/memory_quality/controller.py:457-457; mcp/src/agents_remember/application/memory_quality/controller.py:478-487 |
| The prepared inputs handed to the checklist. | `_PreparedInputs` | mcp/src/agents_remember/application/memory_quality/controller.py:470-475 |
| Only a contract-scoped run gets a worklist, through the one recompute entry point. | `_knowledge_worklist`; `recompute_leaf_worklist` | mcp/src/agents_remember/application/memory_quality/controller.py:478-487 |
| The checklist receives the worklist and its path. | `_attach_curator_checklist`; `knowledge_worklist_path` | mcp/src/agents_remember/application/memory_quality/controller.py:517-681 |
| The controller-level run persists, reports and renders the worklist; the count stays 0. | `test_the_memory_quality_controller_persists_the_worklist_and_renders_it_in_the_checklist` | mcp/tests/test_knowledge_worklist_leaf.py:577-669 |

## 260928-MIK-L30 The Onboarding Gate Dispatch (MIK-R30 Rule 6)

The leaf block of `_attach_curator_checklist` now calls `_onboarding_refresh_gate(scope, changed_paths,
working_paths, (accepted_no_impact, accepted_route_no_impact), response)`, which returns the repair and
report-only findings of the leaf's onboarding gate:

- **Converted tree** (`leaf_onboarding_trace_sides(contract, memory_tree=<memory root>)` returns sides): it
  runs `onboarding_trace_gate_for_context`. Each missing trace is **one repair finding** that counts toward
  `curatorActionableCount`, unreadable inputs are repair findings too, a row naming a subject the leaf raised
  no item for is report-only, and the response gains `onboardingTrace` (the result's `brief()`: owner, item
  and open counts, the first open subjects, unnecessary-row and problem counts). The curator-coherence
  no-impact identities are not consulted there (architect ruling 2026-09-29T18:49:50 (1)).
- **Unconverted tree** (`None`): it runs today's `validate_memory_refresh_attestations` with the same
  arguments, and a refusal is the same single `memory-refresh-attestation-failed` finding with the same
  text. This is every production leaf before MIK-R37, including this master's own leaves.

| Finding | Anchor | Source |
| --- | --- | --- |
| The checklist's leaf block hands the gate the changed paths and the accepted identities. | "gate_findings, gate_report_only = _onboarding_refresh_gate(" | mcp/src/agents_remember/application/memory_quality/controller.py:628-634 |
| The dispatch: the history-file gate on a converted tree, today's gate otherwise. | `_onboarding_refresh_gate`; `leaf_onboarding_trace_sides` | mcp/src/agents_remember/application/memory_quality/controller.py:709-759 |
| Each missing trace counts once; rows make the count 0; today's function is not called. | `test_the_memory_quality_run_counts_each_missing_trace_toward_the_actionable_count` | mcp/tests/test_onboarding_trace_gate.py:706-723 |

## 260928-MIK-L10 A Needed Onboarding Row Is Not Reported Unnecessary (MIK-R10 Rule 5)

On a converted leaf, the report-only findings of MIK-R30's gate now pass through `_needed_rows_dropped` before
they join the checklist (ruling 2026-09-30T01:56:39 Q3):

- It takes `answering_trace_subjects` of the leaf's worklist items: the `onboarding:<path>` subjects that answer
  an uncovered unexplained item. MIK-R30 raises no card item for a card-less path, so its report would call
  the leaf's row about that path unnecessary, although MIK-R10 rule 5 needs it as the item's trace. Those
  findings are dropped; rows about files the leaf did not change are still reported.
- MIK-R30's report-only findings are exactly its unnecessary rows, so it sets the response's
  `onboardingTrace.unnecessaryRowCount` to the number kept, and the count and the list agree (the L06-sync
  consistency fix). Doing this inside the helper keeps `_attach_curator_checklist` within PLR0915.
- The findings now carry each row's `subject` (`worktrees/modules/onboarding_trace.report_only_findings`,
  additive), which is what the filter reads. `repair_findings`, which drive the gate decision, are untouched.
- **Unconverted leaves are unchanged:** with no worklist the answering set is empty, nothing is dropped, and
  today's gate runs as before; this leaf's own memory-quality runs returned no worklist and no
  `onboardingTrace`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The report-only findings pass through the filter. | "report_only.extend(_needed_rows_dropped(" | mcp/src/agents_remember/application/memory_quality/controller.py:637-637 |
| The filter and the adjusted count. | `_needed_rows_dropped`; `answering_trace_subjects` | mcp/src/agents_remember/application/memory_quality/controller.py:684-706 |
| The raw count is 2 and the response count 1; only the stray row remains. | `test_an_onboarding_row_that_answers_an_uncovered_item_is_not_reported_unnecessary` | mcp/tests/test_unexplained_change_disposition.py:540-579 |

## Docs References

No configured Domain Documentation source applies; the controller contract is repository-internal.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The execution identity contains normalized checks, detail limit, publication semantics, and frozen scope. | `MemoryQualityExecution` | mcp/src/agents_remember/application/memory_quality/controller.py:107-125 |
| Sync, start, and poll are separate typed request entry points with capacity and nondisclosing poll translations. | `run_memory_quality_request`; `start_memory_quality_request`; `poll_memory_quality_request` | mcp/src/agents_remember/application/memory_quality/controller.py:259-265; mcp/src/agents_remember/application/memory_quality/controller.py:268-274; mcp/src/agents_remember/application/memory_quality/controller.py:277-283 |
| Full leaf checks compose and atomically publish the curator checklist: the tail of `_execute_memory_quality` returns early for a run that publishes no checklist, and otherwise hands the payload to the checklist writer. | "if not execution.publish_curator_report"; "_attach_curator_checklist("; `_attach_curator_checklist` | mcp/src/agents_remember/application/memory_quality/controller.py:458-458; mcp/src/agents_remember/application/memory_quality/controller.py:460-460; mcp/src/agents_remember/application/memory_quality/controller.py:517-681 |
| R03 candidate-tree freezing and change refusal around curator publication. | `_curator_candidate_inputs`; `_require_same_curator_candidate` | mcp/src/agents_remember/application/memory_quality/controller.py:852-871; mcp/src/agents_remember/application/memory_quality/controller.py:880-910 |

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

## KS-R15@v1 Knowledge-Review Summary Read

`curator_knowledge_review_summaries` reads the **already-published** curator-coherence authority and
summarises its stored assessment collection into the `AssessmentSummary` rows the checklist's factual
`knowledgeReview` section renders. It decides nothing about what it reads: it is deliberately not an
input to `curatorActionableCount`, and a subject with no stored assessment produces no row at all
rather than a favourable one.

The read is the controller's second read of the same authority on a full scoped run, and it is
deliberately the same already-resolved authority rather than a new resolution: the checklist write path
passes the summaries into `CuratorChecklist.knowledge_review`, whose default keeps every existing
caller unchanged.

## KS-R23@v1 The Ruler Stamp, And The Checks' Own Closeout-Owned Bucket

Two changes reach this controller.

**Every public entry point names the build that measured (item 26, D-33).** The three public functions
are now thin wrappers rather than the bodies themselves: `_run_memory_quality_request` (`:124-134`),
`_start_memory_quality_request` (`:137-169`) and `_poll_memory_quality_request` (`:172-234`) hold what
the public names used to hold, and `run_memory_quality_request` (`:249-255`),
`start_memory_quality_request` (`:258-264`) and `poll_memory_quality_request` (`:267-273`) return
`_stamped(...)` over them. `_stamped` (`:237-246`) merges `measuring_build_stamp()` into the payload, so
a sync run, an async admission, a poll **and the refusal envelopes around them** all carry `servingBuild`.
That placement is the requirement rather than a detail: the controller answers more than one shape, and a
stamp added at one return site is a stamp missing from the others. A reader can then tell a count
produced by the candidate's own code from one produced by the build the MCP surface happens to serve.

**The closeout-owned rows a check publishes itself are collected (item 17 half (b), D-24/D-29).**
`_checklist_finding_sets` (`:641-668`) replaces the direct `split_commit_owned_findings` call at the
checklist composition site (`:489-493`). It keeps that split's repairable/commit-owned division and
additionally collects every `closeoutOwnedFindings` row the executed checks declared in
`payload["checks"]`, in sorted check order. Those rows — the citation check's anchor-multiplicity class,
which no range a curator may write can discharge — therefore land in the checklist's
*"Closeout-owned real-commit provenance"* section (folded into the summary's `Real-commit provenance
findings` row) instead of sitting in the repairable set whose count has to reach zero, or being dropped
from both.

## Update History
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): **body updated for MIK-R10.** Added the section "260928-MIK-L10 A Needed Onboarding Row Is Not Reported Unnecessary (MIK-R10 Rule 5)" (`_needed_rows_dropped`, the adjusted `unnecessaryRowCount`, ruling 01:56:39 Q3), three rows. Other rows were normalised by the installed fixer or re-pointed by exact line shift. No verification stamp was advanced.
- 2026-09-29T18:58:47+00:00: Generated citation repair: `_attach_coherence_readiness` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:930-957. No content impact: mechanical anchor-range projection bound to citation source snapshot f243d6cd7f6b1214330608a0b5e372fb521b8035680e9d41a0f33ceb9d8057ab; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T18:58:47+00:00: Generated citation repair: `_attach_coherence_readiness` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:930-957. No content impact: mechanical anchor-range projection bound to citation source snapshot f243d6cd7f6b1214330608a0b5e372fb521b8035680e9d41a0f33ceb9d8057ab; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T18:58:47+00:00: Generated citation repair: `_attach_final_full_catalog` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:780-816. No content impact: mechanical anchor-range projection bound to citation source snapshot f243d6cd7f6b1214330608a0b5e372fb521b8035680e9d41a0f33ceb9d8057ab; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): **body updated for MIK-R30.** Added the section "260928-MIK-L30 The Onboarding Gate Dispatch (MIK-R30 Rule 6)": `_onboarding_refresh_gate` and its converted/unconverted dispatch, the `onboardingTrace` response field, and architect ruling 2026-09-29T18:49:50 (1). Rows below the inserted function were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T15:42:37+00:00: Generated citation repair: `_attach_coherence_readiness` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:889-916. No content impact: mechanical anchor-range projection bound to citation source snapshot e0edc40115a57d64eee749407e3bb64382ff6c5a6884c16ce3f8938fb89031a7; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T15:42:37+00:00: Generated citation repair: `_attach_coherence_readiness` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:889-916. No content impact: mechanical anchor-range projection bound to citation source snapshot e0edc40115a57d64eee749407e3bb64382ff6c5a6884c16ce3f8938fb89031a7; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): Added the section "260928-MIK-L08 The Leaf's Change-To-Knowledge Worklist (MIK-R08 Rules 7 And 8)": `_knowledge_worklist` and `recompute_leaf_worklist` after the census, the `knowledgeWorklist` response summary, the checklist's worklist inputs, and `_PreparedInputs` replacing the `census=` keyword. It records architect ruling 1 (L08 wires the memory-quality run and managed-sync completion; closeout and landing are L09's) and that the section is information, never counted. Unconverted runs are unchanged.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): Added the section "260928-MIK-L28 The "Invariants Without Proof" Input": `_without_proof` and the new `without_proof=` argument of `_attach_curator_checklist`, with the architect ruling that the list is checklist-only information and adds no count to the wire summary. One cited row. The other ranges moved by the two added lines and the new function were re-pointed by the installed `memory-citations --fix`; no claim wording changed there. No verification stamp was advanced.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): Added the section "260928-MIK-L24 The Unconverted-Line Refusal": the MIK-R24 rule 9 refusal that `_execute_memory_quality` now makes first. The section records the architect rulings: the refusal is inert until the official line is converted, and conversion and crossing are separate routes. It has one cited row. The three claims citing `_execute_memory_quality` were reopened: the function changed, and a committed 2026-09-18 projection bullet names it. I re-read each one against the working tree, and each still holds: the scope is revalidated, the candidate inputs are passed to the checklist writer, and a run that publishes no checklist returns early. Following the L23 precedent, the two prose claims now also quote the line they are about (`revalidate_memory_candidate_scope`, `candidate_inputs=candidate_inputs`) within the function's real extent (`384-455`). The Repo-Internal row is re-cited to the call site it is about (`446-454`: the early return and the `_attach_curator_checklist(` call), and names `_execute_memory_quality` in its finding text rather than as an anchor. No committed history bullet was altered.
- 2026-09-29T12:03:35+00:00: Generated citation repair: `_attach_final_full_catalog` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:691-727. No content impact: mechanical anchor-range projection bound to citation source snapshot 75677f16e5ed8ed01a37a3496ecf058f05e2f85f804720849cd36afc05309a98; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-18T18:04:10+00:00: 260915-KS-L23 residue clearance (seat A, follow-up): the two claims that name `_execute_memory_quality` and `_attach_curator_checklist` (the prose `cit:` claim and the Repo-Internal row) were re-cited from `controller.py:318-360; controller.py:363-441` to `controller.py:383-435; controller.py:465-638`, the two functions' current extents -- the full leaf checks compose in `_execute_memory_quality` and `_attach_curator_checklist` is the checklist publication. The reopen item's currency test reads the changed construct's **declaration** line, and neither retired range contained `_attach_curator_checklist`'s at 465, which is why the item was enforced; with the declaration inside a cited range the pointer lands on the construct the claim is about. Claim wording retained (it still holds), and no anchor, row, citation or range was deleted. Verification stamp not advanced: the code is uncommitted and closeout owns the stamp.
- 2026-09-18T17:53:23+00:00: 260915-KS-L23 residue clearance (seat A): `run_memory_quality_request`, `start_memory_quality_request` and `poll_memory_quality_request` repointed from `mcp/src/agents_remember/application/memory_quality/controller.py:110-120`, `:111-143` and `:146-208` to `mcp/src/agents_remember/application/memory_quality/controller.py:249-255`, `:258-264` and `:267-273` — the new ranges hold the three public entry-point definitions (the KS-R23@v1 `_stamped(...)` wrappers), while the retired ranges held `MemoryQualityExecution.identity` and the three private `_run`/`_start`/`_poll` bodies; claim re-read against the construct, wording unchanged. Also repointed in the same card: `_curator_candidate_inputs` and `_require_same_curator_candidate` from `:545-564`, `:596-648` and `:657-687` to `mcp/src/agents_remember/application/memory_quality/controller.py:717-736` and `:745-775` (the two definitions the R03 candidate-tree freeze/refusal claim is about) in the reference table and in the CCR-R03 prose citation, which shared those same three retired ranges. Verification stamp not advanced: the code is uncommitted and closeout owns the stamp.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_resolve_execution` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:360-380. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_execute_memory_quality` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:383-435. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_attach_coherence_readiness` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:820-847. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_attach_coherence_readiness` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:820-847. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:23+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **recorded the two changes this leaf made to the controller, neither of which this card stated.** Item 26 (D-33) split each public entry point into an unstamped body plus a `_stamped(...)` wrapper — `_run`/`_start`/`_poll_memory_quality_request` now hold the bodies, and `run`/`start`/`poll_memory_quality_request` return `_stamped(...)` over them — so `servingBuild` rides every mode *and* the refusal envelopes around them; the section above states that placement is the point. Item 17 half (b) added `_checklist_finding_sets`, which keeps `split_commit_owned_findings`' division and additionally collects each check's own `closeoutOwnedFindings` bucket into the checklist's closeout-owned section, so the anchor-multiplicity rows are reported where the stamp decision is made rather than counted as curator work. Both were read against the delivered but **uncommitted** working tree, so the verification stamp is not advanced: no commit carries these bytes and closeout owns the real stamp. The reference-table rows (whose ranges this leaf's line moves shifted) were left to the citation-range repair pass that owns them.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `_attach_coherence_readiness` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:749-776. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `_attach_coherence_readiness` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:749-776. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `_attach_final_full_catalog` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:600-636. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/src/agents_remember/application/memory_quality/controller.py:72-89` -> `mcp/src/agents_remember/application/memory_quality/controller.py:93-111`; `mcp/src/agents_remember/application/memory_quality/controller.py:295-315` -> `mcp/src/agents_remember/application/memory_quality/controller.py:317-337`; `mcp/src/agents_remember/application/memory_quality/controller.py:651-678` -> `mcp/src/agents_remember/application/memory_quality/controller.py:714-741`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
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

## 260921-ICR-L15 The Unmeasured Count Reaches The Checklist

`260921-ICR-L15` (`ICR-R15@v1`) adds one field to this controller's knowledge-review read: the
projection's own `notMeasuredCount` is now passed through `AssessmentSummaryInput` beside the counts
already carried, so a subject whose records **no measurement covered** is reported as unmeasured
instead of being folded into `stale` or into a silent zero.

Nothing else about the read changed, and the boundary this card's own sections describe is untouched.
`curator_knowledge_review_summaries` still reads the **already published** curator-coherence authority
and decides nothing about it; the count comes from `curator_coherence_subject_assessment_state`, which
this leaf re-pointed at the shipped per-record measurement. The read remains structurally outside
`curatorActionableCount` — it is a factual projection feeding the checklist's report-only
`knowledgeReview` section, and this leaf gives it no gate consequence. The one visible effect is one
more counted limitation downstream: the section that consumes these summaries can now say
`not-measured` rather than letting `| stale | 0 |` be read as "nothing moved" when nothing was
measured at all.

## Update History
- 2026-09-23T13:10:00+02:00 — 260921-ICR-L15 curator (candidate `ar/260921-icr-l15`, uncommitted; leaf base commit `3103e1142a3ded8a843c3e5bbefca14861ba4a58`, so the honest basis for every claim here is that commit plus the working-tree delta): **the unmeasured count enters the summary input.** This leaf changed this source by one line — `curator_knowledge_review_summaries` passes `state.notMeasuredCount` through — which the memory-refresh check correctly refused to accept as a history-only update, so the read is recorded in the body as a body change and not as a metadata refresh. No claim, anchor or citation range was changed here, and **no verification stamp was advanced**: the candidate is uncommitted, the header's stamp values are untouched, and the governed closeout owns the real stamp.
