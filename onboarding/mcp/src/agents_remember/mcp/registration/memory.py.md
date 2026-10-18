# mcp/src/agents_remember/mcp/registration/memory.py

## Current operative account — MIK-R112

The current source facts below replace the former operative inventory. The separately labelled superseded claims describe only the pre-repair card. Original paragraphs, dated closures, evidence and citation identities remain intact in the explicitly historical section; they grant no current call, restored route or fresh execution acceptance.

- drift_check is no longer a registered memory tool.
- citation_migrate registration was deleted while citation_fix remains. Citation fix advertises
  finite `documents` selection beside singleton `document`; scope validation owns exclusive,
  empty and shared-bound refusals. Quality, citation and route descriptions advertise status and
  corpus locations, not a new authority to change their scopes or checks.
- Typed MQC sync/start/poll and baseline boundaries survive. Carryover keeps flat selection inputs: plan advertises equal-version converted pairs/records, official-code anchor observation and curator-authored history with no commit/report; apply requires `intent_note`, reanchors/indexes/validates the recovery worktree, restores bytes on refusal, skips edited targets and imports no history or commit. `memory_commit_message` and `CarryoverCommitMessages` are removed. `citation_fix` retains finite `documents`/singleton `document`, optional `contract_path` and `dry_run`; `expected_snapshot` and caller `exclude` are absent from its signature and scope construction.
- `citation_fix` exposes optional `contract_path`; the short description names the ordinary leaf call and points to shipped tool-details for the full ordinary/pre-baseline admissions. The application guard still permits the configured converted root before its attributed baseline with no linked worktree. Route-index apply uses the same measured exception; other unscoped index calls remain read-only previews. Transport declarations do not bypass the application guard.

- The public fixer signature makes `contract_path` optional; its short description gives leaf-call cues and points to `docs/tool-details.md`, but does not state the ordinary/pre-baseline admissions. [17]
- The index description retains pre-baseline apply and qualifies other unscoped calls as read-only previews. [18]

### Source and authority bounds

- Source comparison: `mcp/src/agents_remember/mcp/registration/memory.py:19-35,38-132`.
- Source comparison: `git diff HEAD -- mcp/src/agents_remember/mcp/registration/memory.py (drift_check/citation_migrate removed)`.

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

## Historical original card — preserved, not the current operative account

<details>
<summary>Retained original source accounts and producer history</summary>

## Governing Overview

[registration route overview](overview.md)

## 260731-EFA-L8 Change

The tool-registration functions gained bare-`*` keyword-only signatures (the 19
PLR0917 fixes across `mcp/registration/*.py`); the rule stays enabled and call sites
already pass keywords. Registered tools are unchanged.

## Purpose

`register_memory_tools(server, config)` declares the eight memory-root tools: `memory_quality_check`,
`citation_fix`, `route_index_refresh`, `memory_init`, `memory_baseline_status`,
`memory_baseline_adopt`, `memory_carryover_plan`, `memory_carryover_apply`.

## Code Commentary

### Logic

`memory_carryover_apply` takes only approval intent and explicit review selections; the retired
`memory_commit_message` and `CarryoverCommitMessages` are absent from its signature. Its description names attributed
memory content and a ledger cache refresh; there is no ledger commit argument or ledger branch
publication for callers to provide.

The reference-anchor check and its repair are named for what they measure: `citation_fix` reports the anchors
of onboarding cards and the validity of the tree — on converted memory how many anchors are current
and how many are stale against the code, plus the knowledge validator's refusing findings. Whether an
invariant is still current is answered by `knowledge_read` and `knowledge_integrity_check`, not here; a
stale reference is reported and never blocks by itself, and nothing is repaired by this check. A contract-scoped `memory_quality_check` is the
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
  `replace_existing` become one `CarryoverSelection`. The `intent_note` stays a separate argument: it is the approval, not
  part of the selection, and apply takes no commit-message object.

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
- `memory_quality_check` identifies the repair work; contract-scoped `memory_quality_check` must be repaired and
  rerun by the curator before handoff, then repeated by closeout after real-commit metadata refresh.
- Registration documents the checklist as the only write of a full scoped quality call: code and
  memory remain unchanged, and dirty-source/full-quality `ok` is not the curator's zeroable gate.
- Memory-quality request modes are mutually exclusive and extra-forbid; no legacy `wait`/`run_id`
  overload or silent branch inference remains.
- Quality execution lives in `application/memory_quality/controller.py`; other memory tools remain
  in `application/memory_tools.py`. Registration chooses only the validated request variant.

### Todos

No additional file-local TODO is established by this candidate review.

## Evidence

### Docs References

No Domain Documentation source is configured in the resolved memory repository. The current
contract is supported by the implementation and the authorized cache-retirement requirement.

No configured external domain source applies.

### Repo-Internal References

- The payload builders for the carryover plan and report-filing apply pair. [2]
- The typed sync/start/poll payload builders. [3]

- Carryover registration declares one memory subject and describes the computed cache refresh. [1]
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

**Retired, not current.** The caller `exclude` parameter described below is gone: `citation_fix`'s
signature carries no `excludes`, `CitationOperationScope` no longer packs caller globs, and the
`_citation_trees` construction point it fed was removed with the legacy citation router. What
remains is the register every call still honours — the memory layer's
`settings.json → onboarding.pathRules.exclude` and the code repository's `.gitignore`. The paragraphs
below are the historical account of the retired parameter, kept as intent.

Retired account: the registered `citation_fix` tool gained one optional parameter:

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

- The drift description states the anchor measurement, the non-blocking stale rule, and the no-repair boundary. [15]
- The adoption description states that accept_drift clears stale anchors only and the first baseline is validated. [16]

</details>

- Registration exposes converted worktree-only carryover and finite citation selectors without retired commit-message, caller-exclude or expected-snapshot arguments. [19]
