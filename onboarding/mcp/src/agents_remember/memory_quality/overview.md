# mcp/src/agents_remember/memory_quality/ — Memory Quality Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/memory_quality/`  |
| doc_type               | `route-local-overview`                     |
| lastUpdated | 2026-09-05T07:14+00:00 |
| lastVerifiedCommitHash | `ea35964985f30080488270e71ac81657ac40682b` |
| lastVerifiedCommitDate | 2026-09-05T06:48:29+02:00 |
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`memory_quality/` owns memory-layer quality control for the MCP package. It
groups integrity checks that compare onboarding to source state and style
checks that enforce repository memory conventions.

## Hot Path Summary

`check.py` is the public package-level runner. It can execute style-only checks
without repository context, or combine drift integrity and style checks when an
MCP application entry point supplies `DriftCheckContext`. Drift logic lives under
`integrity/onboarding_drift_check/`; the pre-code-commit missing-onboarding
check lives at `integrity/check_missing_onboarding.py`; update-history ordering lives under
`style/update_history/`. The history-order checker is diagnostic; the matching
`history_order_fix.py` module is the explicit mutating script for timestamped
history-order fixes. `style/document_shape/entity_catalog_alignment.py` owns the cheap,
tree-only one-to-one check between root entity inventory entries and fingerprint rows.
Contract-scoped application calls supply the leaf base as temporary provenance for unstamped
dirty-tree claims; this is comparison input only and never a verification stamp.
`curator_checklist.py` renders the full scoped result plus missing-onboarding, route-index, drift,
and report-only detail into the enclosure's one atomically replaced curator worklist.

## Route Model

- `check.py` normalizes check names, dispatches quality runners, and returns one
  combined payload.
- `integrity/onboarding_drift_check/` contains the moved `c-02-memory-quality-control` skill drift classifier
  and bounded summary helper; the summary run also persists a durable
  `ar-drift-snapshot/v1` JSON (best-effort) under `logs/observer/drift/` for the
  observer dashboard to read without re-classifying (slice 3b). Task 29 S7 writes the snapshot's
  `sourceRoot`, `memoryRoot`, optional `reportPath`, and `checkedAt` provenance so actionable-drift
  attention can say which repo/memory pair raised the notice and when it was measured. Task 32 routes
  that writer through the shared observer drift-snapshot path helper so producer
  writes, projection pruning, and cleanup deletion share one filename contract.
  The packet owner remains `integrity/onboarding_drift_check/models.py`; it imports the
  single `DriftStatus` declaration from `models/drift.py`. The packet includes required
  `status` and optional counts, paths, rows, samples and error. Wire consumers share that
  lower-layer vocabulary rather than importing a status declaration upward.
- `integrity/check_missing_onboarding.py` checks only current worktree
  additions so newly added eligible files get sidecars before the code commit.
- `curator_checklist.py` deterministically separates zeroable curator repairs from truthful
  closeout-only provenance, renders every worklist class, and publishes one operational report
  outside both Git worktrees.
- `final_certification/` (CCR-R08, added by 260831-CCR-L08) owns the final full
  memory-coherence certification (Gate 5): the deterministic complete final catalog
  (`catalog.py`), the closed typed models (`models.py`), the R21 Gate-5 semantic-input
  assembly and coherence subrecord derivation (`certificate.py`), the executable
  certification protocol (`certify.py`), and the exact green Gate 1-4 prerequisite adapter
  (`gate_prefix.py`). The interactive full contract-scoped quality run publishes the
  non-certifying `finalFullCatalog` readiness projection through the application controller;
  the certification API requires the R21 certificates and R07 affected-closure plan for green.
  No production closeout caller currently supplies those inputs or invokes that API.
- `style/update_history/` checks that onboarding `## Update History` bullets
  are newest-first and timestamped, and contains the dedicated history-order
  fix script.

## Invariants And Boundaries

- Task-start work should use `drift_check` to build the onboarding worklist.
- Curator starts with the full contract-scoped `memory_quality_check`, uses its single enclosure
  report as the combined missing-onboarding/quality/index/drift worklist, and reruns until
  `curatorActionableCount` is zero before handoff.
- Closeout creates the real code commit, refreshes commit-derived metadata once, and repeats the
  full quality gate before the memory content commit.
- Closeout should run `check_missing_onboarding` before the code commit when
  the task added source files; this is local worktree responsibility, not a
  whole-repository adoption scan.
- Style checks should not block the beginning of normal implementation work.
- `memory_quality_check` must not mutate code or memory. Its full leaf-scoped operational report
  is an atomic overwrite outside both Git worktrees; mechanical style rewrites still belong in
  focused fix scripts.
- New memory-quality checks should be placed under `style/` or `integrity/`
  according to what they validate.
- `models/drift.py` owns the shared drift-status vocabulary. Packet and response consumers
  import it; the older EFA-L4 declaring-owner narrative below is historical and was
  superseded by the L9 layering move.
- **A `NotRequired` key on `DriftSummaryPacket` must be read with `.get`, including by
  consumers on this route.** `check.py`'s `run_drift_quality_check` reads `count`,
  `reportPath` and `actionableCount` with `.get(...)`, not `[...]`: those keys accompany a
  `checked` status only, which the guard above the return has established but the type cannot
  carry across.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The MCP application entry point builds drift context, including temporary leaf-base provenance, and calls the package runner. | `run_memory_quality_request`; `_execute_memory_quality` | mcp/src/agents_remember/application/memory_quality/controller.py:98-108; mcp/src/agents_remember/application/memory_quality/controller.py:318-360 |
| Tool metadata and server registration expose `memory_quality_check` to agents. | `memory_quality_check_payload`, `create_server` | mcp/src/agents_remember/mcp/server.py:58-70; mcp/src/agents_remember/mcp/tools/memory.py:58-65 |
| The update-history fixer is a dedicated mutating module rather than a `memory_quality_check` option. | `memory_quality_check` | mcp/src/agents_remember/mcp/registration/memory.py:57-75 |
| The missing-onboarding checker catches newly added worktree files before code commit. | `check_missing_onboarding` | mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py:46-73 |
| The shared drift model declares the vocabulary used by drift-check wire responses. | "class DriftSummary(StrictResponseModel):" | mcp/src/agents_remember/models/drift.py:13-23; mcp/src/agents_remember/models/memory.py:13-27 |
| The context-packet application entry point that returns `DriftSummaryPacket` from its drift seam. | `build_context_packet` | mcp/src/agents_remember/application/context_packet.py:59-102 |
| The curator checklist renderer owns deterministic grouping, closeout-provenance separation, and atomic publication. | `write_curator_checklist` | mcp/src/agents_remember/memory_quality/curator_checklist.py:79-126 |

## Historical 260731-EFA-L2 — Every Verdict Is Now Emitted From One Place

The check catalogue, the dispatch contract and the diagnostic-only rule are unchanged. What changed
is that each classifier now emits its verdicts through a single constructor, which is what makes the
verdict *set* auditable — previously the same nine-field `DriftRow` or `MissingOnboarding` was
rebuilt at every branch, and a field could silently disagree between two of them.

- **`check_missing_onboarding.py`** dispatches on storage mode to `_missing_sidecar_onboarding`
  (the mirrored path this source expects, reported when the file does not exist) and
  `_missing_inline_onboarding` (the in-source block, reported when absent *or unreadable*). The
  three states remain `missing`, `unsupported` (non-UTF-8 source, or a storage mode this checker
  does not implement) and "no finding"; the unsupported-storage-mode fallthrough is now the
  function's visible last statement rather than a branch buried after the inline path.
- **`sidecar.py`** builds one local `row(...)` closure that fixes the sidecar's identity and
  verification stamp, so a classifier only supplies `classification` / `trust` /
  `affected_sections` / `note`. `_early_classification` groups the three pre-diff verdicts —
  `missing verification`, `orphaned`, and the recorded commit not being in git history — and
  returning `None` from it is what means "go on and diff". The classification vocabulary and trust
  levels are byte-identical.
- **`entities.py`** takes `EntityCatalog` (frozen: `onboarding_file`, `onboarding_root`,
  `repository`, `settings`, `last_updated`). All five are read out of one document before any row
  is emitted and every row builder needs all five, so the catalog travels as the document it is.
- **`drift.py`** and `check_missing_onboarding.py` resolve coordination context through
  `hints=CoordinationHints(topology=, coordination_root=, settings_path=, onboarding_root=)` — the
  resolver's new keyword-bundle API (see
  [kernel/coordination_context](../kernel/coordination_context/overview.md)). Resolved contexts are
  identical.

## Historical 260731-EFA-L3 — Every Verdict Is Now Read Through One Git Runner

Every check this route emits is ultimately a statement about *a repository*: which files
the worktree added, which blobs a source has, whether a recorded commit is in history.
Two files in this route each carried their own private `run_git`, and both were the
kernel's runner with `env=git_environment()` dropped — the guard that strips the eight
`GIT_DIR`-family repository selectors. `cwd=` does not defeat those variables, so with
`GIT_DIR` exported these checks would read a *different repository* and emit verdicts
about it in the current one's name. Both copies are gone; both files now import
`run_git` from `agents_remember.kernel.git_command`.

- **`integrity/check_missing_onboarding.py`** is the pre-code-commit gate, so a
  misdirected read is not a wrong report but a wrongly-passed gate — this is the check
  whose stated boundary above is that it is "local worktree responsibility, not a
  whole-repository adoption scan", and until this leaf an exported `GIT_DIR` was enough
  to make it enumerate someone else's worktree. Its private runner always raised on a
  nonzero return, so `run_git` was the wrong name for it; it is now **`require_git`**
  (line 176), delegating to the owner and keeping the fail-fast contract. It still
  returns the `CompletedProcess` rather than stripped text — unlike the same-named
  helper in `worktrees/modules/git.py` — because every caller reads NUL-delimited
  output that a `.strip()` would corrupt. Both call sites moved:
  `worktree_added_sources` (lines 82-83, the three `-z` enumerations) and
  `code_repository_name_from_git` (line 192, the `--git-common-dir` probe that decides
  which repository name the finding is filed under).
- **`integrity/onboarding_drift_check/git_ops.py`** is the drift classifier's entire git
  surface — `current_branch_name` (line 15), `local_change_note` (line 22),
  `list_repo_sources` (line 41), `git_stdout` (line 54), `git_blob_hash` (line 61) and
  the entity fingerprints built on it. Its `run_git` was the route's other copy and is
  deleted; `drift.py`, `report.py` and `sidecar.py` correspondingly import `run_git`
  from the kernel rather than re-exporting it through `git_ops`.

The checks, their names, their classification vocabulary and their emitted rows are
unchanged. What changed is that a verdict can no longer be computed against a repository
the caller did not name. `mcp/tests/test_git_command.py` holds the proof against a decoy
repository named by the selectors.

## Historical 260731-EFA-L4 — The Drift Summary Is A Typed Packet With A Named Vocabulary

The drift summary crossed three module boundaries as `dict[str, Any]`, which meant its shape
was agreed by convention at each of them. It is now `DriftSummaryPacket`, a `TypedDict` declared
in `integrity/onboarding_drift_check/models.py` beside the classifier that fills it, with
`DriftStatus` declared in the same place.

- **`models.py`** declares `DriftStatus = Literal["notChecked", "checked", "error"]` and
  `DriftSummaryPacket` (`status` required; `count`, `actionableCount`, `reportPath`,
  `actionableSample`, `error` `NotRequired`). The `NotRequired` markers are the honest part:
  which keys are present genuinely depends on the status, and the type now says so instead of
  every consumer guessing.
- **`summary.py`**'s three producers — `not_checked`, `run_drift_summary`, `summarize_rows` —
  return `DriftSummaryPacket` rather than `dict[str, Any]`. Nothing they emit changed.
- **`check.py`**'s `run_drift_quality_check` reads the optional keys with `.get(...)` where it
  had used `[...]`. On the `checked` path those keys are in fact always present, so this is not
  a behaviour change on any reachable input; it is what makes the checked-status narrowing
  expressible, since a `TypedDict` cannot carry the `status != "checked"` guard's conclusion
  into the branch below it.

The reason this route now has an inbound dependency from `models/` and `application/`: the
vocabulary had been copied twice on the wire side, and one copy was SHORT. `models.drift`
declared `Literal["notChecked", "checked"]` and no `error` field, while `run_drift_summary`
returns `{"status": "error", "error": ...}` for a missing onboarding root — the diagnostic
crashed on precisely the call meant to explain the missing onboarding. Both wire models now
import `DriftStatus` from here, and `application/context_packet.py`'s `_drift_packet` is
annotated `-> DriftSummaryPacket`. The route's checks, their names, their classification
vocabulary and their emitted rows are all unchanged.

## 260731-EFA-L16 — The Citation Gate Moves Before The Suite

Closeout's citation gate (`range_resolution` + `claim_reopen`) now runs before the code commit
and the strict wrapper: both checks are working-tree semantics — the fixer regenerates ranges
and a changed construct with a current citation is only the review surface — so they clear
without a commit and reject in seconds. The L6 placement made clearing require the commit
itself, deadlocking every structural change (115 unresolvable findings at this leaf's closeout).
The curator runs the same `memory_quality_check` during the leaf; the gate is its fallback.
The post-commit phase keeps drift, shape, and history order as the refresh sanity pass.

## 260731-EFA-L8 — The Whole-New-File Absent-At-Stamp Rule

claim_reopen's absent-at-stamp rule (a construct added after the stamp) now extends to whole
source files added after the stamp. A new file's anchor that resolves exactly once in the
working tree inside a cited range surfaces report-only — the same current-citation review
surface, clearing with no commit; an anchor that is absent, ambiguous, or lands outside the
cited range stays hard (`citation_provenance_invalid` / `citation_claim_reopened`). This is
what lets a leaf's new-file rows resolve pre-commit instead of failing provenance: regenerated
ranges point at the new content and the curator's review is the report-only relay.
Coverage lives in `mcp/tests/test_l6_diff_coverage_claim_reopen.py`
(`TestLocalChangesNewFile`, lines 143-186) and
`mcp/tests/test_memory_citation_change_detection.py` (the `test_a_new_source_*` arms in
`CodeProvenanceTests`, plus the `ChangeRoutingTests` untracked/ignored-local-path assertion).

## L9 Closeout Repair — Entity Structure Fails Before Code Rails

`style.document_shape.entity_catalog_alignment` separates a pure tree-shape invariant from the
full post-refresh drift comparison. It rejects missing catalog sections, inventory entries without
a fingerprint, fingerprint rows without an inventory entry, and duplicate fingerprint rows. The
check is first in `BEFORE_METADATA_REFRESH_CHECKS`, before citation scans, staging, hooks, Pyright,
or pytest. Source evidence and hash freshness remain in the post-refresh drift check because those
need the real code commit and refreshed metadata to clear.

## 260731-EFA-L9 Route Impact — Caller Re-Points

The memory-quality callers were rewritten by the L9 caller wave: `DriftStatus`/`DriftSummaryPacket` import from `models/drift.py` (declaration moved by L9), and runtime config from `kernel/primitives/runtime_config.py`. Check behavior is unchanged.

## 260815-DAG-L3 Structured Curator Attestation

The curator checklist now emits a machine-readable `ar-curator-memory-quality/v1` attestation beside
the rendered report. It binds checklist status and zero/actionable counts, the exact onboarding
root, the report path and digest, and the complete source-change candidate set. Queue declaration
requires this structured zero gate; when candidates exist it also requires the canonical leaf
curator authority to match the set exactly. The former five-column Markdown review
is historical; current consumers use the structured coherence manifest and record. A free-text ready sentence or
path mention is not readiness evidence.

## 2026-08-26 Application Controller Boundary

The asynchronous sync/start/poll controller now lives at `application.memory_quality.controller`. This route continues to own the integrity/style checks and their package runner; the application controller composes those checks and finalizes transport responses without duplicating check logic or adding a fallback path.

## MCAR-L02 Deterministic Checklist And Coherence Join

The enclosure-local curator checklist and its `ar-curator-memory-quality/v1` attestation are now
byte-deterministic for identical inputs; the prior generated timestamp could invalidate a current
coherence record without a semantic change. The structured attestation remains the exact candidate
census. Public memory readiness retains raw `qualityChecklistStatus` but reports combined
`checklistStatus=coherence-required` and `closeoutReady=false` until the same structured authority
validator used by closeout succeeds.

## MCAR-L03 Pair-Bound Quality Evidence

Full leaf quality receives only a contract-resolved code/onboarding pair and writes that complete
identity into the structured curator attestation. Repository-only quality remains a diagnostic and
cannot publish candidate acceptance. Pre/post-scan revalidation makes wrong or raced scope a
typed refusal before evidence can be accepted.

## 260831-CCR-L08 — Final Full Memory-Coherence Certification (Gate 5)

This route now owns the final full memory-coherence certification package
(`final_certification/`). The complete Gate-5 catalog is the exhaustion surface: every
applicable memory checker, the missing-onboarding and route-index alignment owners, the R07
affected-closure plan, the canonical curator-coherence record, and the exact code/memory
candidate pair return pass/fail/blocked/not-applicable, and the attestation checks the caller-supplied executed-check population against the plan.
The `certify_final_full_memory_coherence` function itself consumes those results; it does
not launch the checkers or independently establish that they ran. The interactive full run projects the deterministic, non-certifying
`finalFullCatalog` readiness surface onto its result (controller `_attach_final_full_catalog`); the
executable certification API (green/red/blocked, finalization-eligible only when green) remains
separate. The current closeout path does not invoke it; a readiness result is not a Gate-5 certificate.

## Current Deterministic Citation Repair Limit

R10 adds uniquely resolved range/move repair and deterministic projection planning. The
current fixer stages an edit before the projection decision; a later projection decline
does not remove that edit, so apply can still write it. Document reads are cached and the
publication loop does not call `verify_unchanged`. The existing caller scope guard and
atomic replacement do not provide fresh-document compare-and-swap. These confirmed defects
remain pending repair; a dry-run proposal is not safe-apply certification.

## Gate-5 Registry And Execution Boundary

`gate_five_rails.py` derives one enforcing memory-domain R11 rail per item in the complete
final catalog. Its configuration identity includes the final catalog version, checker registry
version and exact population. This is the Gate-5 registry contribution consumed by the R11/R22
bridge; declaring that contribution does not execute the checkers.

The interactive application controller calls `final_catalog_readiness` with the exact memory tree
and candidate-pair authority but explicitly passes `affected_closure_plan_digest=None`. The R07
`compile_affected_closure_plan` / `execute_affected_closure` and R08
`certify_final_full_memory_coherence` APIs have no production callers outside their own packages
in the inspected source. Existing closeout memory checks and curator-coherence publication remain
real behavior, but must not be equated with the new affected-closure/full-certification protocol.

| Finding | Anchor | Source |
| --- | --- | --- |
| Complete catalog items become deterministic memory-domain rails and a population-bound configuration digest. | "def gate_five_memory_rails("; "def _catalog_configuration_digest() -> str:" | mcp/src/agents_remember/memory_quality/gate_five_rails.py:36-102 |
| The application surface projects readiness with no affected-closure plan. | "def _attach_final_full_catalog(" | mcp/src/agents_remember/application/memory_quality/controller.py:444-480 |
| Full certification requires explicit evidence and predecessor authority supplied by its caller. | "def certify_final_full_memory_coherence(" | mcp/src/agents_remember/memory_quality/final_certification/certify.py:44-134 |

## Update History

- 2026-09-05T07:14+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Corrected drift vocabulary ownership, historical Markdown coherence authority, final certification producer claims, and explicit R10 write defects. Verification records source review, not execution or acceptance.


- 2026-09-05T06:12+00:00 — Recovered final-catalog knowledge and corrected readiness versus certification ownership; added the Gate-5 rail derivation and the still-unwired R07/R08 execution boundary.

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: added the
  `final_certification/` route-model bullet and the CCR-R08 leaf section (final full
  memory-coherence certification: complete catalog, readiness projection on the full run,
  executable certification) and re-anchored the controller row shifted by the +57-line change.
  Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-29T21:46+02:00 — MCAR-L03: bound leaf quality and curator attestations to the exact
  code/memory pair. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — MCAR-L02 A005: removed timestamp entropy from the curator checklist and
  joined raw quality with the sole coherence validator. Verification remains closeout-owned.

- 2026-08-26T10:44:52+02:00 — Reconciled the route with the extracted application controller while preserving memory-quality check ownership inside this package.

- 2026-08-15T09:10+02:00 — 260815-DAG-L3 route impact: recorded the structured curator
  attestation and exact source-change disposition contract consumed before queue declaration.
  Verification remains closeout-owned.

- 2026-08-11T16:54+02:00 — Added the enclosure-local curator checklist owner, combined the
  pre-closeout worklist behind one full scoped quality call, and preserved code/memory mutation and
  real-commit stamping outside the report writer.
- 2026-08-11T14:58+02:00 — Re-read the new temporary-provenance claim against the current
  application entry point and regenerated its evidence to the exact declaration and assignment.
- 2026-08-11T14:40+02:00 — Assigned missing-onboarding and full dirty-tree quality repair to the
  curator before handoff, recorded temporary comparison provenance, and kept real-commit refresh
  and the repeated hard gate in closeout.

- 2026-08-10T12:46+02:00 — L9 closeout repair: added the entity-catalog alignment owner and its
  pre-code fail-fast boundary; verification metadata stays pinned until closeout stamps the repair.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 route impact: L9 caller/import re-points recorded and body updated.

- 2026-08-07T14:30+02:00 — 260731-EFA-L8 curator (bounded delta): recorded the round-9
  claim_reopen mechanism — the absent-at-stamp rule extended to whole source files added after
  the stamp (unique working-tree anchor inside a cited range surfaces report-only; absent,
  ambiguous, or stale evidence stays hard) — and the test coverage that pins it. Verification
  metadata stays pinned until closeout stamps the code commit.
- 2026-08-05T22:55+02:00 — 260731-EFA-L16 curator: recorded the closeout memory-quality phase-order repair (`check.py` phase constants + `worktrees/modules/closeout.py`): the before-commit phase list is now empty and every check, claim-reopen included, runs in the single phase after the code commit and the metadata refresh to it — claim evidence is only comparable once the commit it must be compared against exists; L16's closeout produced the first live deadlock under the L6 placement (115 unresolvable findings). Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B20 curator: rebound the
  `memory_quality_check` row to the actual `memory_quality_check_tool` definition; exact
  non-fixing check returns zero findings.

- 2026-08-02T20:33:53+02:00 — 260731-EFA-L6 curator W1-B10 final-index reconciliation after S31: repaired 1 citation range for `memory_quality_check` using the warm source-index snapshot; scoped recheck clean.

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 10 citation findings (4 rows); scoped recheck clean.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No route impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:26+02:00 — 260731-EFA-L4 curator: **body corrected.** This route acquired
  something the card did not describe — it is now the declaring owner of a wire vocabulary, not
  only its producer. Recorded `DriftStatus` and the `DriftSummaryPacket` TypedDict in
  `integrity/onboarding_drift_check/models.py`, `summary.py`'s three producers moving off
  `dict[str, Any]` onto it, and the resulting INBOUND import edge from `models/drift.py`,
  `models/memory.py` and `controllers/context_packet.py` (checked by grep against the current
  source: those three plus the six in-subpackage consumers). Recorded WHY the edge exists rather
  than just that it does: `models.drift.DriftStatus` was `["notChecked", "checked"]` with no
  `error` field, so `context_packet(include_drift=true)` against a repo with no onboarding root
  raised on both the status and the key — the diagnostic failed on the call meant to explain the
  problem. Added two invariants (one declaration of an emittable status, imported by every wire
  model; and `NotRequired` keys are read with `.get`, with `check.py`'s guard-then-`.get` pattern
  named as the reason) and two reference rows to the 2-column table. **Re-verified all eight
  line-number citations in the L3 section and its history entry against the current files** — none
  moved: `require_git` is still at `check_missing_onboarding.py:176`, `worktree_added_sources`'
  call sites at 82-83, `code_repository_name_from_git`'s probe at 192, and `git_ops.py`'s
  `current_branch_name`/`local_change_note`/`list_repo_sources`/`git_stdout`/`git_blob_hash` at
  15/22/41/54/61. Neither of those two files was touched by this leaf. Verification metadata
  pinned until closeout stamps the L4 commit.
- 2026-07-31T20:58+02:00 — 260731-EFA-L3 curator: recorded that this route no longer contains a
  git runner. `integrity/onboarding_drift_check/git_ops.py` and
  `integrity/check_missing_onboarding.py` each held a private `run_git` that was the kernel's
  runner minus `env=git_environment()`, so an exported `GIT_DIR` could make these checks read a
  different repository — including the pre-code-commit gate whose stated boundary is that it is
  local-worktree-scoped. Both now call `kernel/git_command.run_git`; the misnamed always-raising
  copy in `check_missing_onboarding.py` became `require_git` (line 176), with
  `worktree_added_sources` and `code_repository_name_from_git` moved onto it. No statement in the
  body was false — the route model, check catalogue and emitted rows are unchanged — this adds the
  correctness fact behind them. Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2: verdict construction was centralized per classifier
  (`_missing_sidecar_onboarding`/`_missing_inline_onboarding`, `sidecar.py`'s `row(...)` closure
  and `_early_classification`, `EntityCatalog` in `entities.py`), and both CLI entry points now
  pass `hints=CoordinationHints(...)` to the resolver. No check was added, removed or reclassified;
  emitted rows are unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-06-28T07:43+02:00 — Task 29 S7 route impact: drift snapshot summaries now carry source-root,
  memory-root, optional report-path, and checked-at provenance for actionable-drift attention detail.
  Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-27T23:09+02:00 — Task 32 route impact: the drift summary writer now uses the shared observer drift-snapshot path helper, keeping producer writes aligned with projection pruning and cleanup deletion. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-13T20:48+02:00 — Slice 3b (browser-dashboard): the drift summary run now also persists a durable `ar-drift-snapshot/v1` JSON under `logs/observer/drift/` (`_write_drift_snapshot`, best-effort) for the observer dashboard to read without re-classifying; recorded this new output in the `integrity/onboarding_drift_check/` Route Model bullet. The route's check responsibilities are otherwise unchanged. Verification metadata pinned until closeout stamps the 3b code commit.
- 2026-06-11T15:20+02:00 — No route impact: onboarding_drift_check/git_ops.py fingerprint helpers gained a keyword-only ref parameter for carryover entity-catalog validation; route structure and check responsibilities are unchanged.
- 2026-06-06T12:15: Re-verified against the current memory-quality package; corrected controller and MCP payload-builder references after memory tools moved out of the former `skill_tools.py`/`mcp/tools.py` surfaces.
- 2026-05-31T12:40+02:00: Removed the `integrity/ledger_consistency.py` reserved-stub bullet after the empty stub source and its sidecar were deleted in the 1.0.0 remediation.
- 2026-05-24T03:24+02:00: Updated after adding `check_missing_onboarding` as the pre-code-commit integrity pass for newly added files.
- 2026-05-24T03:09+02:00: Updated after adding the dedicated `history_order_fix.py` script and keeping `memory_quality_check` report-only.
- 2026-05-24T02:47+02:00: Created after memory quality became a first-class package route with integrity and style subdomains.
