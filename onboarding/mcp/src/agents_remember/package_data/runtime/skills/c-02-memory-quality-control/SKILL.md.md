# c-02-memory-quality-control/SKILL.md

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

**Converted memory (L37 fix round P1b).** Section 3 of the skill now opens with a paragraph for a memory tree that
holds the knowledge layout marker: the checks that read the legacy card format report `not-applicable-converted`;
currentness comes from anchors (the `knowledge.converted` check runs the knowledge validator, and stale sidecar
references are reported, never failed); every changed source file is answered through the onboarding gate
(MIK-R30: a counted change of its card, or an `onboarding_trace` row); and cards and their references are authored
as the c-05 skill's converted-card workflow describes. The rest of the section still describes unconverted memory.

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

No relevant external documentation found.

## Evidence

### Repo-Internal References

`c-02-memory-quality-control` skill owns the memory-quality operation a curator runs as part of curation,
together with task-start drift and the missing-onboarding report scoped to the curator's change set. Its
completed result travels with the curation handoff as a closeout and integration prerequisite.

- The quality-control phase table distinguishes task-start drift, curator intake, pre-commit coverage, closeout validation, and targeted style repair. [1]
- Task-start quality control preserves the gradual-adoption boundary for historical files without onboarding and separates clean-source update candidates from dirty-source active work-in-progress before `c-05-create-or-update-onboarding-files` skill handoff. [2]
- Pre-code-commit quality control checks only current worktree additions so newly added files cannot escape onboarding. [3]
- Curation publishes the coherence authority the checklist requires and uses focused style fixers only after reported findings. [4]

| The curator handoff runs the complete curation check and repairs or escalates every curator-actionable finding with its exact returned code. | "### 6. Run the Complete Curation Check"; "### 7. Publish the Curator Coherence Authority When the Checklist Requires It" | mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md:189-208; mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md:209-228 |

- On converted memory the legacy-format checks are not applicable, and currentness comes from anchors. [5]

### Cross-Repo References

No cross-repo evidence is needed for the current skill contract.

No meaningful cross-repo references found.

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
