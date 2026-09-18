# c-02-memory-quality-control/SKILL.md

| Field                  | Value                                                              |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                 |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md` |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-08-29T08:52+02:00                     |
| lastVerifiedCommitHash | `a29a20c6eefea424a7e0321a54fcda2ed1b35098` |
| lastVerifiedCommitDate | 2026-09-17T14:23:47+02:00|

## Purpose

This skill defines `c-02-memory-quality-control` skill as on-demand memory-quality diagnostics and scoped
onboarding checks. It keeps task-start drift evidence and routes missing-onboarding or targeted quality
work to the owning curator; the curator runs the complete memory-quality operation as part of curation,
and closeout and integration carry that completed result as a prerequisite instead of invoking it.

## Code Commentary

### Logic

The skill instructs agents to resolve context through `c-08-ar-coordination-context-resolver` skill/MCP,
use `drift_check` as task-start evidence, classify clean-source candidates versus dirty active work, and
run `check_missing_onboarding` or named memory-quality checks only for an approved scoped diagnostic.
Curators own affected onboarding content and report each check as passed, failed, blocked, or not-run.
Subset calls remain diagnostic, and a subset never stands in for the whole operation: the curator runs the
complete memory-quality operation at the leaf's contract scope and publishes the coherence authority
whenever the checklist requires it. Closeout and integration consume the prepared memory
leg and carry that completed curation as a prerequisite rather than invoking it.

### Conventions

`c-02-memory-quality-control` skill reports and routes memory-quality work; it does not rewrite onboarding
prose. Task-start drift reports remain local coordination artifacts under
`c-08-ar-coordination-context-resolver` skill's resolved `temp_root`. Closeout style checks do not run at task start.
Mechanical style repair is done by targeted fixers only after
an explicit diagnostic reports a finding and the owning workflow accepts the repair.
The curator checklist is the explicit temp-location exception: it lives under the leaf worktree
enclosure's reserved `reports/` directory, outside both Git worktrees, and replaces its predecessor.

### Invariants And Boundaries

`c-02-memory-quality-control` skill must stay read-only with respect to onboarding prose. Any content update
belongs to `c-05-create-or-update-onboarding-files` skill. Drift reports are temporary evidence, not durable onboarding,
and explicit report paths inside a durable memory repo should be redirected
back to the resolved coordination temp area. The enclosure checklist is temporary operational
evidence and is garbage-collected with the worktrees. Implementation approval is not
commit approval; `c-02-memory-quality-control` skill can report quality state, but `c-09-git-worktree-manager` skill owns commit approval
gates.

### Todos

Add tests for `c-02-memory-quality-control` skill against a migrated external memory repo once such a fixture exists.


## CCR-R12@v5 Transaction Boundary

Current contract: the curator's complete memory-quality operation is part of curation — run at intake and after every repair until `curatorActionableCount=0` and the **raw** `qualityChecklistStatus=ready-for-closeout`. The **combined** `checklistStatus` is rewritten to `coherence-required` **only when the coherence record is then missing or stale** — that is the coherence gate, cleared by publishing the `curator_coherence` authority with `prepare` → `publish` → `validate`. On the success path, where the record is already current, the combined field is **not rewritten** and keeps its incoming `ready-for-closeout` value, with `closeoutReady=true`; the value `ready-for-closeout` is therefore observable in the combined field once the whole pipeline is already complete. A named scoped check or a `checks=[...]` subset never stands in for the full operation. **Field-name correction (`D35`, made by 260915-CAPS-L10):** this sentence previously named `checklistStatus=ready-for-closeout` as the loop's condition; read the raw field to end the loop and the combined field to decide the coherence gate (`application/memory_quality/controller.py:664`, `:671`, `:678`, `:685-687`). **Warrant corrected by `CAPS-R19` (leaf `260915-CAPS-L19`):** the absolute claim that `ready-for-closeout` is *never* a value of the combined field is **literally false** and is superseded by `CAPS-R19`'s revision note; the field-name correction it supported still holds, and attribution is complementary — `260915-CAPS-L10` corrected the **onboarding cards**, while `CAPS-R19` corrected the **shipped sources** (the five loop-gate carriers, their nine generated copies, the guard registry's docstring) and brought `docs/reference/mcp-tools.md` into the loop-gate census and the guard's `LOOP_GATE_DOCUMENTS`. Task-start drift remains diagnostic evidence, and the `curator_coherence` authority is published whenever the checklist reports `coherence-required`. Closeout and integration consume the prepared Git inputs and carry the completed curation as a prerequisite without invoking or requiring memory-quality, census, or review operations.

### Docs References

No external domain documentation applies to this repository-local maintenance skill.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | — | — |

## Repo-Internal References

`c-02-memory-quality-control` skill owns the memory-quality operation a curator runs as part of curation,
together with task-start drift and the missing-onboarding report scoped to the curator's change set. Its
completed result travels with the curation handoff as a closeout and integration prerequisite.

| Finding | Anchor | Source |
| --- | --- | --- |
| The quality-control phase table distinguishes task-start drift, curator intake, pre-commit coverage, closeout validation, and targeted style repair. | "## Quality Control Phases" | mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md:30-38 |
| Task-start quality control preserves the gradual-adoption boundary for historical files without onboarding and separates clean-source update candidates from dirty-source active work-in-progress before `c-05-create-or-update-onboarding-files` skill handoff. | "Run Task-Start Drift Control" | mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md:71-107 |
| Pre-code-commit quality control checks only current worktree additions so newly added files cannot escape onboarding. | "Run Pre-Code-Commit Missing-Onboarding Control" | mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md:164-180 |
| Curation publishes the coherence authority the checklist requires and uses focused style fixers only after reported findings. | "### 7. Publish the Curator Coherence Authority When the Checklist Requires It"; "### 8. Use Targeted Style Fixers Only After Findings" | mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md:209-228; mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md:229-263 |

| The curator handoff runs the complete curation check and repairs or escalates every curator-actionable finding with its exact returned code. | "### 6. Run the Complete Curation Check"; "### 7. Publish the Curator Coherence Authority When the Checklist Requires It" | mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md:189-208; mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md:209-228 |

## Cross-Repo References

No cross-repo evidence is needed for the current skill contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260821-DAGQC-L2 Canonical Quality Calls

The packaged skill now uses the same strict `request={mode: ...}` grammar as the public tool. Sync,
start, and poll examples keep their field sets separate; capacity refusal directs the caller to
poll/wait and retry rather than bypassing the controller. This packaged copy remains synchronized
from canonical doctrine and introduces no compatibility path.

## MCAR-L02 Structured Coherence Workflow

The packaged memory-quality doctrine now treats the deterministic structured checklist as the
candidate census, then requires `curator_coherence prepare` → agent-owned exact judgments → atomic
`publish` → shared `validate`. It separates raw quality readiness from combined closeout readiness,
uses explicit evidence namespaces, keeps requirement/attempt/digest identities distinct, and
forbids hand-versioned reports or filename fallback. Same-input quality reruns preserve bytes;
changed inputs intentionally stale the authority.

## Update History
- 2026-09-17T14:15+02:00 — 260915-CAPS-L19 curator: **Field-name warrant corrected — `ready-for-closeout` read as *never* a value of the combined `checklistStatus`.** That absolute sentence was written by 260915-CAPS-L10's curator as the warrant for this card's `D35` correction, and `CAPS-R19` (`260915-CAPS-L19`) measures it **literally false** (`application/memory_quality/controller.py:685-687` leaves the combined field at its incoming `ready-for-closeout` value on the success path, with `closeoutReady=true`). The card now states the three-path model instead: the raw `qualityChecklistStatus` is the repair loop's gate; the combined `checklistStatus` is rewritten to `coherence-required` **only when the coherence record is then missing or stale**; and `closeoutReady` becomes true only once that validation passes. Corrected under `CAPS-R19`'s revision note (2026-09-17T13:55), which is the authority for this change. The field-name correction itself stands and attribution is complementary — `260915-CAPS-L10` corrected the onboarding cards, `CAPS-R19` corrected the shipped sources (the five loop-gate carriers, their nine generated copies, the guard registry's docstring) and brought `docs/reference/mcp-tools.md` into the loop-gate census and the guard's `LOOP_GATE_DOCUMENTS`. The earlier entries below are left exactly as written: they record what L10 did, and this entry is the correction of their warrant. No verification stamp advanced — the candidate is uncommitted and the governed closeout owns the real commits.
- 2026-09-17T13:45+02:00 — 260915-CAPS-L10 curator: **corrected a landed defect (`D35`) in the CCR-R12@v5 boundary block.** The complete-curation contract it states named `checklistStatus=ready-for-closeout` as the repair loop's termination condition; `ready-for-closeout` is never a value of the combined field. The block now names the **raw** `qualityChecklistStatus` as the loop's gate and the **combined** `checklistStatus=coherence-required` as the coherence gate, matching the controller (`application/memory_quality/controller.py:664,671,678,687`). No doctrine changed — only the field names, which were the defect. This leaf's code delta is zero, so no citation range moved and no verification stamp was advanced.
- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: **complete curation inverts the doctrine this card recorded.** CAPS-R18@v1 removes the optional/narrow-curation sentences from the shipped instruction corpus and states the rule normatively — the full `memory_quality_check` operation runs as part of every leaf's curation at its contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every curator-actionable finding is repaired or escalated as blocked with its exact returned code, and closeout and integration **carry** the completed curation as a prerequisite while invoking nothing. Updated the Purpose, Logic, the CCR-R12@v5 boundary block and the Repo-Internal prose accordingly, and re-pointed the two citation rows whose anchors this leaf renamed (`### 7` is now the coherence-authority step, `### 6` the complete curation check) to their current headings and ranges.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.

- 2026-09-10T00:00+02:00 — CCR-L42 current-candidate curation: recorded that curator intake must run the complete validation path and treats subset calls as diagnostics, not green evidence; verification metadata remains closeout-owned.

- 2026-08-29T08:52+02:00 — MCAR-L02 A005: synchronized the structured coherence publication and
  combined-readiness workflow. Verification remains closeout-owned.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: synchronized the memory-quality workflow to the canonical discriminated request and capacity retry guidance. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-11T16:54+02:00 — Documented the full scoped curator checklist, its stable enclosure
  path, overwrite/cleanup lifetime, and repeat-until-zero repair loop.
- 2026-08-03T04:32:19+02:00 — W3-B08 curator: curated 4 citations (citation_anchor_missing=2, citation_prose_not_in_cit_form=0, citation_source_malformed=2); final scoped citation check clean.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` added clean-source versus dirty-source drift classification to `c-02-memory-quality-control` skill.
- 2026-05-24T04:34+02:00: Refreshed verification metadata after `c-02-memory-quality-control` skill memory quality control source landed.
- 2026-05-24T04:05+02:00: Renamed `c-02-memory-quality-control` skill to memory quality control and expanded the skill around drift, missing-onboarding, closeout quality, and style fixer procedures.
- 2026-05-15T12:57+02:00: Documented entity catalog inventory-to-fingerprint reconciliation, including missing fingerprint rows and orphaned fingerprint rows. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-15T11:46+02:00: Refreshed after `c-02-memory-quality-control` skill added route-overview checks and deterministic repo-entity fingerprints. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-12T18:51+02:00: Refreshed after the skill frontmatter moved to the lowercase `c-02-onboarding-drift-detection` name.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-11T18:34: Updated after the `c-02-memory-quality-control` skill helper command examples adopted `--code-repository-root`.
- 2026-05-10T03:11: Updated after `c-02-memory-quality-control` skill documented that explicit report paths inside `memory_root` are redirected to coordination temp.
- 2026-05-10T00:36: Refreshed verification metadata after the temp-root drift report behavior landed on main.
- 2026-05-09T23:22: Updated after `c-02-memory-quality-control` skill moved default drift reports under `c-08-ar-coordination-context-resolver` skill's temporary artifact root.
- 2026-05-09T22:57: Refreshed verification metadata and clarified that reports are coordination artifacts.
- 2026-05-09T21:59: Updated after `c-08-ar-coordination-context-resolver` skill split memory roots from coordination roots.
- 2026-05-09T21:15: Created first file-level onboarding baseline for `c-02-memory-quality-control` skill documentation.
