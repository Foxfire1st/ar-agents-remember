# mcp/src/agents_remember/application/memory_quality/controller.py

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
while quality was running cit:([`_curator_candidate_inputs`, `_require_same_curator_candidate`], mcp/src/agents_remember/application/memory_quality/controller.py:947-966; mcp/src/agents_remember/application/memory_quality/controller.py:975-1005).
The checklist writer receives `code_candidate_tree` and `memory_candidate_tree` so the attestation
can declare its exact pair/tree inputs cit:([`_execute_memory_quality`, "candidate_inputs=candidate_inputs", `_attach_curator_checklist`], mcp/src/agents_remember/application/memory_quality/controller.py:395-468; mcp/src/agents_remember/application/memory_quality/controller.py:568-722).

Interactive quality execution resolves the exact scope before scanning and revalidates it after
the scan and before publication. A full leaf run joins its checklist with the same
`require_current_curator_coherence` validator used by closeout: unfinished memory repairs retain
`closeoutReady=false`; missing or stale coherence cannot become combined-ready. The deterministic
full catalog is a readiness projection, not final certification: this interactive route has no
Gate 1–4 certificate prefix or affected-closure plan and explicitly reports those missing
authorities. This permits preparatory memory work without claiming final acceptance.

cit:([`_resolve_execution`], mcp/src/agents_remember/application/memory_quality/controller.py:372-392)
cit:([`_execute_memory_quality`, "revalidate_memory_candidate_scope"], mcp/src/agents_remember/application/memory_quality/controller.py:388-459)
cit:([`_attach_coherence_readiness`], mcp/src/agents_remember/application/memory_quality/controller.py:1051-1078)
cit:([`_attach_coherence_readiness`], mcp/src/agents_remember/application/memory_quality/controller.py:1051-1078)
cit:([`_attach_final_full_catalog`], mcp/src/agents_remember/application/memory_quality/controller.py:901-937)

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
- **Since L37 the refusal is `_unconverted_refusal(scope)` and covers both scopes (MIK-R09 rule 6).** A leaf's
  tree is refused when its official line is converted, or otherwise by the cutover lock (through
  `unconverted_line_refusal`) once its memory repository holds converted memory. A repository-level run (no
  contract) reads the official memory checkout: when that checkout is unconverted it is refused by the cutover
  lock, naming "the official memory checkout"; a converted checkout is never locked. During the cutover window
  this refuses the repository-level run for every master, the converting one included, until it lands.
- **The `knowledge.converted` check uses the converted base (L37 review R3-1).** The drift context carries
  `knowledge_base=converted_check_base(scope, coordination_root)`, so on an unconverted `HEAD` the check validates
  against `HEAD`'s conversion, as the gate, the worklist and the writer do.

- The refusal runs before any scan and returns a refused result naming the crossing sync. [1]

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

- The checklist receives the list (since MIK-R09 beside the mandatory gate's findings, which do count); `None` for an unconverted tree. [2]

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
- **The section counts nothing itself.** Until MIK-R09 the worklist was information only. Since L09 the
  mandatory gate turns every open item into one `knowledge-gate` repair finding that counts toward
  `curatorActionableCount` (see the L09 section below); the section still only renders.
- **Trigger split (architect ruling 1).** This run is one of the two triggers L08 wires; the other is
  managed-sync completion. Closeout validation and landing pre-commit evaluation are L09's; since L09 this run
  also recomputes through the gate over its exact candidate, and `_knowledge_worklist` remains the plain
  recompute for a scope the gate does not apply to.
- **Unconverted runs are unchanged:** with no worklist, neither the response field nor the section appears.

- The worklist is recomputed after the census (since MIK-R09 by the gate where it applies, else by `_knowledge_worklist`) and summarized in the response. [3]
- The prepared inputs handed to the checklist. [4]
- Only a contract-scoped run gets a worklist, through the one recompute entry point. [5]
- The checklist receives the worklist (since MIK-R09 the one the gate recomputed) and its path. [6]
- The controller-level run persists, reports and renders the worklist; since MIK-R09 it captures real candidate trees, and its four open items count (`curatorActionableCount` 4, `knowledgeGate.openItemCount` 4). [7]

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

- The checklist's leaf block hands the gate the changed paths and the accepted identities. [8]
- The dispatch: the history-file gate on a converted tree, today's gate otherwise. [9]
- Each open item counts once: since MIK-R09 the card's and the route's traces and the uncovered file's `unexplained_hunk` (3); rows make the count 0; today's function is not called. [10]

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

- The report-only findings pass through the filter. [11]
- The filter and the adjusted count. [12]
- The raw count is 2 and the response count 1; only the stray row remains. [13]

## 260928-MIK-L09 The Mandatory Gate Counts Every Open Item (MIK-R09 Rules 1, 3 And 7)

The curator publication is one of MIK-R09's leaf routes. `_execute_memory_quality` now calls
`_knowledge_gate_and_worklist(scope, candidate_inputs)` right after the census:

- **`_knowledge_gate`** evaluates `knowledge_gate.evaluate_leaf_gate(contract, CandidateTrees(code_tree,
  memory_tree))` over the exact candidate this publication attests (`_curator_candidate_inputs`, captured before the
  scan). It returns `None` for a scope that publishes no curator report, a non-leaf or non-external scope, and every
  unconverted leaf, whose run is unchanged. The gate recomputes the worklist over those trees and persists it; that
  worklist is the one summarized (`knowledgeWorklist`) and rendered. Where no gate applies, `_knowledge_worklist`
  recomputes as before.
- **`_knowledge_briefs`** adds `knowledgeWorklist` and, when the gate ran, `knowledgeGate` (`GateResult.brief()`:
  state, owner, worklist state/digest/path, and the finding, open-item, incomplete, violation and report-only
  counts).
- **`_with_gate`** (in the checklist's leaf block, `prepared.gate` on `_PreparedInputs`) turns every gate finding
  into one repair finding (check `knowledge-gate`) toward `curatorActionableCount` (rule 1: each open item, each
  unreadable input and each refusing violation; none is report-only). Rule 7: the onboarding gate runs through the
  same registry, so an `onboarding_trace` item MIK-R30 already reports under the same item ID, with its richer
  required action, is not counted again; and when the gate's worklist is itself incomplete, MIK-R30's unreadable-side
  finding is dropped because the gate already names it (`_onboarding_findings_beside`).
- `_prepared_findings` (the census blockers as repair findings) was split out of `_attach_curator_checklist` to keep
  it within the statement limit; its radon score fell from D 24 to D 21.
- **The memo.** The closeout validator evaluates the same key (`evaluate_leaf_gate` resolves the same parent tip), so
  one memory-quality run recomputes the gate once and its two validator reads are served from the memo.
- **Unconverted runs are unchanged:** with no gate and no worklist, neither `knowledgeGate` nor `knowledgeWorklist`
  appears and the count is what it was; this curation's own `memory_quality_check` runs returned neither.

- The run evaluates the gate and briefs it. [14]
- The gate carried to the checklist. [15]
- The gate over the exact curator candidate; `None` where it does not apply. [16]
- Each gate finding is one repair finding, each open item counted once. [17]
- The census blockers, split out. [18]

## Evidence

### Docs References

No configured Domain Documentation source applies; the controller contract is repository-internal.

### Repo-Internal References

- The execution identity contains normalized checks, detail limit, publication semantics, and frozen scope. [19]
- Sync, start, and poll are separate typed request entry points with capacity and nondisclosing poll translations. [20]
- Full leaf checks compose and atomically publish the curator checklist: the tail of `_execute_memory_quality` returns early for a run that publishes no checklist, and otherwise hands the payload to the checklist writer. [21]
- R03 candidate-tree freezing and change refusal around curator publication. [22]

- Why a run refuses its unconverted memory: the leaf's line, or the official checkout of a repository-level run. [23]

### Cross-Repo References

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
