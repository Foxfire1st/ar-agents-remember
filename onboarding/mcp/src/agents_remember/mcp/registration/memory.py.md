# mcp/src/agents_remember/mcp/registration/memory.py

## Governing Overview

[registration route overview](overview.md)

## 260731-EFA-L8 Change

The tool-registration functions gained bare-`*` keyword-only signatures (the 19
PLR0917 fixes across `mcp/registration/*.py`); the rule stays enabled and call sites
already pass keywords. Registered tools are unchanged.

## Purpose

`register_memory_tools(server, config)` declares the eight memory-root tools: `drift_check`,
`memory_quality_check`, `route_index_refresh`, `memory_init`, `memory_baseline_status`,
`memory_baseline_adopt`, `memory_carryover_plan`, `memory_carryover_apply`.

## Code Commentary

### Logic

`memory_carryover_apply` publishes one `memory_commit_message`, packs it into
`CarryoverCommitMessages`, and leaves approval intent separate. Its description names attributed
memory content and a ledger cache refresh; there is no ledger commit argument or ledger branch
publication for callers to provide.

The two read-only checks are named for what they measure: `drift_check` is the **task-start**
worklist
(classifies how far onboarding has drifted since it was last verified — a nonzero actionable count
after code changes is expected, not a failure). A contract-scoped `memory_quality_check` is the
curator's full pre-closeout repair worklist and is repeated as the hard post-refresh closeout gate;
`ok=false` means enforced findings exist, not that the tool failed. A full scoped call also replaces
one operational checklist under the enclosure `reports/` directory and returns the zeroable
curator count/status; subset and unscoped calls write no checklist. The application layer supplies
the leaf base only as temporary comparison provenance for unstamped cards.

For 260821-DAGQC-L2 `memory_quality_check` publishes one `request` parameter whose discriminator is
`mode`. `sync` and `start` accept execution inputs; `poll` accepts only configured repository and
run id. Registration dispatches by the validated DTO type and makes no lower-level failure
decision. Saturated unique start and nondisclosing missing/wrong-repository poll outcomes are
controller-owned public results.

Three declarations pack:

- `memory_baseline_adopt` — `source_branch` + `work_branch` become `MemoryBranches`.
- `memory_carryover_plan` / `memory_carryover_apply` — the five refs the plan compares
  (`repo_id`, `source_memory`, `official_code_ref`, `source_code_ref`, `old_base`) plus
  `replace_existing` become one `CarryoverSelection`, and apply's memory-content commit message becomes
  `CarryoverCommitMessages`. The `intent_note` stays a separate argument: it is the approval, not
  part of the selection.

The mutating/approval-gated ones say so in their docstrings — `memory_baseline_adopt` commits attributed memory and refreshes the
ledger cache and is gated on clean drift unless `accept_drift=true`;
`memory_carryover_apply` may only run after the code has landed officially and after
`memory_carryover_plan` has been reviewed.

- **`citation_fix` on converted memory (L37 fix round P1b).** The registered tool's description now says that on
  converted memory it authors the cards' citation rows into sidecar references and re-records moved anchors,
  and that `document` then needs no `expected_snapshot` and scopes the run to that one card. The response still
  carries the tree-wide `stale` reference list even for one document, so it can be very large; the CLI
  (`memory-citations --fix --document`) returns the same JSON for a caller that needs to bound it.

### Conventions

Flat baseline/carryover arguments are packed into their application parameter objects. The quality request keeps its existing discriminated shape.

### Invariants And Boundaries

- Carryover and baseline signatures stay flat and build their parameter objects in the body;
  memory quality deliberately publishes the one nested discriminated request object.
- `drift_check` identifies update work; contract-scoped `memory_quality_check` must be repaired and
  rerun by the curator before handoff, then repeated by closeout after real-commit metadata refresh.
- Registration documents the checklist as the only write of a full scoped quality call: code and
  memory remain unchanged, and dirty-source/full-quality `ok` is not the curator's zeroable gate.
- Memory-quality request modes are mutually exclusive and extra-forbid; no legacy `wait`/`run_id`
  overload or silent branch inference remains.
- Quality execution lives in `application/memory_quality_controller.py`; other memory tools remain
  in `application/memory_tools.py`. Registration chooses only the validated request variant.

### Todos

No additional file-local TODO is established by this candidate review.

## Evidence

### Docs References

No Domain Documentation source is configured in the resolved memory repository. The current
contract is supported by the implementation and the authorized cache-retirement requirement.

No configured external domain source applies.

### Repo-Internal References

- Carryover registration declares one memory subject and describes the computed cache refresh. [1]
- The payload builders for the carryover plan and report-filing apply pair. [2]
- The typed sync/start/poll payload builders. [3]
- The `MemoryBranches` parameter object. [4]
- The `CarryoverSelection` parameter object. [5]
- The `CarryoverCommitMessages` parameter object. [6]
- The payload builder for the carryover plan. [7]
- The payload builder for the report-filing apply. [8]
- The typed sync payload builder. [9]
- The typed start payload builder. [10]
- The typed poll payload builder. [11]
- The `citation_fix` registration and its caller-exclude parameter. [12]
- The scope object the excludes ride with. [13]
- The one construction point that carries them into every citation operation. [14]

### Cross-Repo References

No separate cross-repository implementation claim is made.

No external implementation source applies.

## 260915-CAPS-L14 The Citation Surface Gains A Caller Exclude

The registered `citation_fix` tool gained one optional parameter:

```
exclude: list[str] | None = None
```

It is **additive and scoped to one call**. Caller-supplied, code-root-relative globs narrow **that
call's** acquisition on top of the register every call already honours — the memory layer's
`settings.json → onboarding.pathRules.exclude` and the code repository's `.gitignore` — so a caller
cannot accidentally change what another document's repair sees. The globs are packed onto
`CitationOperationScope.excludes`, validated at that boundary, and carried into the one construction
point (`_citation_trees`) shared by all four citation operations.

A pattern that cannot mean anything — empty, absolute, or escaping the code root with `..` — is
refused **by name** rather than quietly matching nothing, because "I excluded it and it is still
indexed" is the harder failure to see. The parameter is keyword-only, so no existing positional call
changes meaning. The CLI declares the matching repeatable `--exclude GLOB`.

The register's rule set is reported in the result, so a reader can still see which patterns produced
the population.

## 260815-DAG-L3 Curator Attestation Registration

The `memory_quality_check` registration now states that a full contract-scoped run atomically
replaces both the rendered curator checklist and its structured, report-digest-bound JSON
attestation; subset and unscoped calls write neither artifact.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260821-DAGQC-L2 Canonical Quality Registration

The public tool now accepts exactly `request={mode: ...}`. Pydantic's discriminated union rejects
mixed or extra mode fields before authority or execution. Registration then forwards the already
typed sync, start, or poll object to the matching thin payload adapter; compatibility readers and
local failure-family translations are intentionally absent.

## MCAR-L02 Memory Readiness Contract

The public quality description now distinguishes the raw deterministic checklist status from
combined coherence readiness. Same-input full runs preserve attestation bytes; changed input
invalidates the prior coherence generation. `closeoutReady=true` requires the same structured
validator used by closeout, and a `coherence-required` response directs the caller to the one
`curator_coherence` API.

## MCAR-L03 Public Memory-Quality Contract

The registration advertises repository-only calls as official diagnostics and requires candidate
polls to repeat the original contract path. It does not imply that repository id can select an
acceptance pair.
