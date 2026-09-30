# mcp/src/agents_remember/memory_quality/ — Memory Quality Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| lastUpdated | 2026-09-30T04:44:12+02:00 |
| lastVerifiedCommitHash | `31d761a241055d67b85ef3908033856b78a86a57` |
| lastVerifiedCommitDate | 2026-09-30T05:10:40+02:00|
| sourceRoute            | `mcp/src/agents_remember/memory_quality/`  |
| doc_type               | `route-local-overview`                     |
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## 260915-CAPS-L20 The Dead Governing Declaration Becomes Visible

This route gained the check that closes `D3`/`D16`'s product gap, and gained it in the same shape as
the route's other integrity checks: a read-only module that reports, plus a wiring that makes the
report reach the loop a curator completes against.

`integrity/governing_overview_resolution.py` resolves every card's declared governing overview and
reports the ones that do not. Until this leaf the product validated that a source **has** a card and
never that the card's declared route **resolves**, so a card whose `governingOverview` field — or
whose `## Governing Overview` body link — pointed at a file that does not exist passed every check the
product runs. Two declarations are graded per card, and they are graded **independently**, because a
card can be broken in both and reporting only the first one found would understate the family. The
field is tried under three bases (the card's own directory, the onboarding root, and the root's
parent) because two authoring conventions ship; the body link is held to the card-relative resolution
a reader clicking it actually gets.

A card that declares the field but carries no body link to resolve — no `## Governing Overview`
section at all, or a section with no markdown link in it — is **observed, not failed**, and `ok` is
derived from the findings tuple alone. That boundary is doctrine rather than convenience: making those
cards gated would create 96 new obligations layer-wide, so this leaf reports the shape and declines to
decide it.

The check's own discrimination is pinned by
`tests/test_governing_overview_resolution.py`, whose single case seeds both dead declaration forms
beside a clean card and both observation forms **in the same tree**, so a checker that flagged
everything could not pass. The wiring is pinned separately, in `test_memory_quality_runs.py`, because
the silence was the defect: a correct checker whose findings never reach `repair_findings` still
reports clean.

**What the route's own curator reads.** `application/memory_quality/controller.py` publishes
`governingOverviewResolution` on the operation response and extends its findings into the gated
curator repair set, so the count a curator iterates now moves when a declaration is dead. The
closeout-admission consumer is behind `D32` — the readiness comparison is only reached once the raw
status is `ready-for-closeout`, which no leaf on this master has reached — and that condition belongs
in any statement of the fix's reach.

## Purpose

`memory_quality/` owns memory-layer quality control for the MCP package. It
groups integrity checks that compare onboarding to source state and style
checks that enforce repository memory conventions.

## Hot Path Summary

`worktrees/modules/memory_candidate_pair.py` — moved out of this route by commit `806649b9` — binds repository/worktree identity, branches, bases, onboarding and contract facts without requiring a cached ledger file or hashing its path into authority. Citation provenance snapshots read substantive memory content while excluding only root `memory.md`; actual source/candidate drift remains detectable. `knowledge_validator/` (MIK-R22) is the mandatory validator for converted text knowledge: one rule registry, run before any converted memory commit.

## Detailed Route Context

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
`memory_census_scope.py` is this route's remaining memory-candidate root. `future_code_candidate.py`
and `memory_candidate_pair.py` were this route's as well until commit `806649b9` moved both to
`worktrees/modules/`, and their cards moved with them; the closeout-facing preparation adapter left in
the same commit, on to the application rank. This route therefore keeps no inbound
dependency on the closeout plane.

## Route Model

- `knowledge_validator/` (MIK-R22, added by 260928-MIK-L22) is the mandatory knowledge
  validator for the converted text layout (Doc14). `trees.py` reads a memory tree's `knowledge/`
  and `onboarding/` bytes (directory or Git) and the paired code tree's paths; `parsed.py` reads each
  file once through the MIK-R21/R07 models and attributes every problem to one rule; `markers.py` is the
  `[n]` marker grammar; `registry.py` is the single rule registry (rule 9) and the validation context;
  `rules_structure.py` and `rules_references.py` register MIK-R22's 16 rules (3 report-only);
  `family_routes.py` and `rules_routes.py` (MIK-R04, added by 260928-MIK-L04) hold the family route
  state and mechanical suggestion and register six route rules (3 report-only, 3 writer-reported);
  `rules_census.py` (MIK-R20, added by 260928-MIK-L20) registers the nine refusing census rules;
  `rules_admission.py` (MIK-R27, added by 260928-MIK-L27) registers the admission rule (one refusing,
  two report-only);
  `validator.py` exposes `validate_tree`, `validation_applies` and `require_valid_commit`;
  `report.py` holds the violations and the refusal; `commit_route.py` is the Git adapter the
  worktree layer's `KnowledgeValidationPort` binds to. It is separate from the onboarding checks
  above: it validates only trees that carry `knowledge/layout.json`, and before MIK-R37 no production
  tree does.
- `knowledge_census/` (MIK-R20, added by 260928-MIK-L20) is the migration census over text files:
  `files.py` reads `knowledge/census/`, `checks.py` holds the integrity and append-only checks the
  validator registers, `measures.py` the Doc12 measures and `report.py` the per-census report. It reads
  bytes only; the Git-reading inventory and the writer are in `memory/knowledge_census/`.
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
- `style/update_history/` checks that onboarding `## 260915-KS-L15 The Factual Knowledge-Review Section

This route gains a new module and one new section in its existing artifact, and the route's governing
boundary is stated once here because it is the property a later reader is most likely to get wrong:
**the `knowledgeReview` section is report-only.** `memory_quality/knowledge_review.py` renders it;
`curator_checklist.py` gained one defaulted input field and appends the rendered lines after the
report-only findings; and none of it reaches `actionable_count`, which is still
`len(repair) + len(missing) + len(stale)`. An unresolved, stale or partial-scope assessment changes the
section's counted limitations and changes nothing about the gate, the status line, or the arithmetic
the attestation binds.

The section renders into the **same** `curator-memory-quality.md` artifact the shipped renderer already
atomically replaces, so this route still has one checklist, one attestation and one count. Its three
limitation codes are facts about the collection — `unresolved` counts authors who could not conclude,
`stale` counts bindings that moved, `partial-scope` counts records with no comparison or scope
reference — and a subject with no assessment is not rendered as a disposition at all.

The route also carries a capacity fact recorded rather than worked around:
`mcp/tests/test_final_full_memory_coherence_certification.py` stands at 1199 of its 1200-line limit
after this leaf's re-scope, so the next leaf that must edit it has to split it first.

- `style/update_history/` checks that onboarding `## Update History` bullets
  are newest-first and timestamped, and contains the dedicated history-order
  fix script.


## Invariants And Boundaries

- **No converted memory commit is made without a passing run of `knowledge_validator`.** Every
  commit route calls one registry through `require_valid_commit` (or the worktree port that wraps it);
  there is no skip parameter, no CLI flag that skips a rule, and a report-only rule never refuses.
  The validator judges shape, identity, references, ownership, families, anchor paths and history
  freezing, never meaning or currentness.

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
- **A preview that plans an operation does not enforce it, and the two surfaces must be maintained
  as one (260831-LOCR-L34).** Every diagnostic on this route has a non-mutating preview and a
  mutating apply — `citation_fix`'s dry run and apply, `memory_quality_check`'s report vs the
  closeout-owned refresh, the citation document transaction's prospective digest vs its write. A plan
  is read as a promise by a human deciding what to do next and by an agent composing the next call, so
  a preview that answers "this would succeed" while its apply refuses is a defect in the plan, not
  merely in the apply. The inventory of known instances (and the deliberate exceptions) is maintained
  on the `worktrees/overview.md` route; this route's own previews are subject to the same rule.

## Historical milestone context: The Preview/Apply Parity Invariant (260831-LOCR-L34)

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

The invariant was established while repairing the worktree checkpoint route, and it is recorded here as
well as on the `worktrees/overview.md` route because **the memory-quality surfaces are the ones a bulk
mechanical migration will touch next**. `citation_fix`, the citation document transaction, and the
onboarding refresh plan each present a preview and an apply that must agree about eligibility; the
route-observed instances below are the evidence that this agreement is not self-maintaining:

- five instances where a preview promised what its apply refused were **fixed** in the leaf that found
  them (series closeout's `would-closeout` on a partial master — the original, and the one that misled
  a human into writing a false note; the checkpoint route's eligibility; the `integration-ref-race`
  payload's hardcoded `nextTool`; the checkpoint's ledger projection; and the ordinary integration dry
  run's unevaluated projection);
- two were **reported and deliberately not fixed** (`worktree_start`, whose dry run skips two binding
  checks because that is a reservation compare-and-swap and not safely separable; and the
  `memory_carryover_plan` / `memory_carryover_apply` pair, where the apply additionally enforces
  `require_ordinary_repository_checkout` and `ensure_clean`);
- one **adjacent shape** is recorded: `worktree_abandon` / `worktree_cleanup` evaluate their preflight
  on the dry run and report blockers, but return `ok=true, state="would-abandon"` / `"would-cleanup"`
  where the apply returns `ok=false, state="abandon-blocked"` / `"blocked"`, and `worktree_cleanup`'s
  summary does not name the blockers at all. That is a verdict/state-string divergence, not a missing
  evaluation, and turning it into a refusal would be a public state-vocabulary change.

Every one of the six was found by **exercising an operation rather than by reading it**. That is the
practical rule for this route: when a preview and an apply are two implementations of one decision,
exercise the pair, and prefer a single shared eligibility evaluation over two agreeing copies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The MCP application entry point builds drift context, including temporary leaf-base provenance, and calls the package runner. | `run_memory_quality_request`; `_execute_memory_quality` | mcp/src/agents_remember/application/memory_quality/controller.py:259-265; mcp/src/agents_remember/application/memory_quality/controller.py:393-467 |
| Tool metadata and server registration expose `memory_quality_check` to agents. | `memory_quality_check_payload`, `create_server` | mcp/src/agents_remember/mcp/server.py:58-70; mcp/src/agents_remember/mcp/tools/memory.py:59-66 |
| The update-history fixer is a dedicated mutating module rather than a `memory_quality_check` option. | `memory_quality_check` | mcp/src/agents_remember/mcp/registration/memory.py:67-98 |
| The missing-onboarding checker catches newly added worktree files before code commit. | `check_missing_onboarding` | mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py:50-77 |
| The shared drift model declares the vocabulary used by drift-check wire responses. | "class DriftSummary(StrictResponseModel):" | mcp/src/agents_remember/models/drift.py:13-23; mcp/src/agents_remember/models/memory.py:13-27 |
| The context-packet application entry point that returns `DriftSummaryPacket` from its drift seam. | `build_context_packet` | mcp/src/agents_remember/application/context_packet.py:64-110 |
| The curator checklist renderer owns deterministic grouping, closeout-provenance separation, and atomic publication. | `write_curator_checklist` | mcp/src/agents_remember/memory_quality/curator_checklist.py:132-212 |

Current working-candidate evidence for this route:

| Finding | Anchor | Source |
| --- | --- | --- |
| Memory candidate identity excludes consumer cache availability. | `MemoryCandidatePairIdentity` | mcp/src/agents_remember/models/lifecycles/memory_candidate.py:10-33 |

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
Current per-citation routing is owned by `classify_citation` (mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:254-273).
The former new-file regression suites were retired; this source contract is not a claim
of present test coverage.

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

## Deterministic Citation Document Publication

Exact unique anchor repair still uses the shared source-index oracle. In prepared private C `b34f4a59562b76a3e2413027468e0f699117b36f`, the fixer accepts or declines a projection before staging its edit. `citations/documents/transaction.py` owns full-document rendering, grouped generated history, last-read original-byte comparison, source-cell/projection bindings and the identity of the held source-index lease. A conflict refuses the complete affected document batch; independent documents may still publish. Scoped passing normalization uses the same document boundary without inventing a unique-move projection.

Since 260831-LOCR-L33 a tree-wide retarget is admitted only when **continuity is proved**: no cited
file may still exist, the tree-wide sighting must be unique, and the anchor must have existed in a
cited file at the document's `lastVerifiedCommitHash` carrying the same extent KIND there. The fixer
resolves that per document through `repair.continuity_for` and `Walk.continuity`;
`migration.place` consults the same authority through `Pass.continuity`, so both relocation routes
answer from one owner. A cited file that survives is the claim's own evidence, so an anchor that left
it is a stale range rather than a move. Three new decline codes name the refusals
(`anchor_left_live_file`, `anchor_continuity_unproven`, `anchor_kind_changed`).

**Why the first design was wrong, recorded here because the same mistake is available elsewhere:** an
earlier guard refused only while a cited file *survived*, so **deleting** the cited file fell through
to the same tree-wide lookup and reproduced the identical wrong binding while reporting success. File
deletion does not establish that the replacement evidence supports the claim. The lesson is the rule:
"provenance-based matching fails open when provenance is unavailable" is an argument for *refusing*,
not for a cheaper guard.

The review surface for a changed-but-current claim was corrected too. A range written by the
mechanical projection passes the currency test by construction — the projection picked the
declaration it wrote — so when the document's generated `Update History` bullet names the claim's
anchors, `claim_reopen` now says the citation is **not shown to be current** and asks whether the
construct at the new location supports the claim's own words. That item is **enforced**, not
report-only: its severity is `"error" if bullets else "warning"`. A projected range is unverified
evidence — nothing in the tree records whether anyone reviewed the projection, and the check cannot
prove a review happened — so it must force an explicit disposition rather than sit in the
`surfacedFindings` bucket a curator can read past. The cost is deliberate and total: every
mechanically projected range now blocks until somebody disposes of it. The ordinary evidence-change
item keeps its `warning`, and nothing demotes this item (`_demote_preexisting_provenance_debt` moves
only `code == INVALID`); with no git view every finding stays enforced.

LF and CRLF bytes remain lossless. A preview returns a validated prospective final digest while reporting zero completed writes. If an admitted scoped document disappears after a detected conflict, `findingsRemaining` is null and the existing refusal keeps the result red; the checker does not claim an empty successful scan. Initially missing input still refuses before source acquisition.

The application retains write-scope authorization and the source index retains frozen source authority. Neither supplies a memory-file mutex. Atomic replacement avoids partial files but cannot exclude an uncooperative writer between the final read and replacement. Gate 5 and private-candidate delivery remain pending.

[Document publication route](style/citations/documents/overview.md) owns the local file map and transaction invariants.

| Finding | Anchor | Source |
| --- | --- | --- |
| Projection admission precedes staging; declined claims retain their original bytes. | `_decide` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:354-399 |
| A relocation proves continuity through the established provenance path before a tree-wide match is admitted. | `Continuity`; `continuity_for`; `_retarget` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:159-240; mcp/src/agents_remember/memory_quality/style/citations/repair.py:243-253; mcp/src/agents_remember/memory_quality/style/citations/repair.py:356-387 |
| The walk resolves one document's continuity and feeds it to the planner. | `Walk`; `fix_onboarding_root` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:201-220; mcp/src/agents_remember/memory_quality/style/citations/fixer.py:269-325 |
| The migration pass consults the same continuity authority before a cross-file relocation, although its continuity branches are unreachable from that entry point by construction. | `Pass`; `place` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:63-86; mcp/src/agents_remember/memory_quality/style/citations/migration.py:415-460 |
| A mechanically projected range is ENFORCED at `error` severity with the support question instead of asserting currency; the ordinary evidence-change item stays `warning`. | `_projected_review_message`; `surfaced_finding` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:338-361; mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:364-408 |
| Accepted batches check complete document bytes and held source/cell bindings before atomic publication. | `DocumentTransaction` | mcp/src/agents_remember/memory_quality/style/citations/documents/transaction.py:30-99 |

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
| The application surface projects readiness with no affected-closure plan. | "def _attach_final_full_catalog(" | mcp/src/agents_remember/application/memory_quality/controller.py:597-597; mcp/src/agents_remember/application/memory_quality/controller.py:786-822 |
| Full certification requires explicit evidence and predecessor authority supplied by its caller. | "def certify_final_full_memory_coherence(" | mcp/src/agents_remember/memory_quality/final_certification/certify.py:44-134 |

## The Shared Exclusion Register, And The Ruled Caps (260915-CAPS-L14)

One register, **three sources**, all reduced to one answer — *is this path outside the candidate
population, and which rule said so*. The register is a **record** as much as a filter: it is
serialized onto the manifest of every published generation, so a later reader sees which rule set
produced an index instead of reconstructing it from the checkout.

| Source | Where it comes from | How it is matched |
| --- | --- | --- |
| `pathRules.exclude` | `onboarding.pathRules.exclude.paths` in the memory layer's `system/settings.json` — the register the exclusion review agrees with the user **before** closeout | the same `matches_any` the storage resolver and the drift check already use |
| `gitignore` | the code repository's own `.gitignore` | inside a Git work tree **Git is the authority** (`ls-files --exclude-standard` already removed them) and the register records the patterns; outside a work tree `FallbackIgnoreMatcher` applies them |
| `caller` | `exclude=` on the `citation_fix` MCP tool and `--exclude` on the CLI, scoped to that one call | exactly like `pathRules.exclude` |

`exclusion_register.py` owns the register; `citation_index_settings.py` owns the two settings keys
(`onboarding.pathRules.exclude` and the optional `onboarding.citationIndex`) and accepts both at the
`onboarding` level **or** the document root. The register, the caps and the settings key are
**mode-independent**: nothing on this route branches on the memory storage mode.

**The register's `.gitignore` rule deliberately diverges from Git, and the divergence is pinned.**
Git does not re-include a file whose parent directory is excluded; the register does, because its
contract answers *"did the exclusion review's rules admit this file?"* rather than *"what would
`git add` do?"*. The direction is the safe one — the register admits a file, it never silently drops
one Git would have kept — and
`test_the_register_admits_a_negated_file_under_an_excluded_directory_where_git_does_not` measures
both sides so a future reader cannot mistake it for an accident.

**Exceeding a cap is a reported skip naming the file and its size — never a silent omission and
never a whole-tree refusal.** The developer's 2026-08-20 ruling sets the numbers, all verifiable as
module constants in `source_index_state.py`: `MAX_SOURCE_FILE_BYTES` 4 MiB (per-file skip),
`MAX_SOURCE_BYTES` 512 MiB (aggregate, applied to the **post-exclusion, post-skip** set),
`MAX_SOURCE_HARD_STOP_BYTES` 2 GiB (the bound past which no index is built at all — a reported,
actionable error naming offenders), `MAX_SOURCE_FILES` 100 000, and `MAX_DATABASE_BYTES` 256 MiB. A
malformed `onboarding.citationIndex` value is refused **by name** rather than falling back to a
default, because a cap that silently ignores its configuration is the failure mode the ruling exists
to prevent.

**The quality surface cannot be bricked by either.** A capped index is `checked` with its skip list;
an unreadable source is named with its path; an unbuildable index is a reported state
(`citation-source-index-unavailable`) carrying offenders and a `nextStep`. The closeout gate's own
admission refuses by name too: `_admitted_source_index` in
`application/prepared_certification.py` raises a typed `CertificationContractError`
(`citation-source-index-unavailable`) instead of letting a bare `ValueError` out.

**The manifest schema moved 9 → 10** for the register. An old v9 manifest is **refused and rebuilt**
rather than being read as "no register" — a rebuilt index must not silently lose the rules that
produced its population.

| Finding | Anchor | Source |
| --- | --- | --- |
| The one construction point folding settings, ignore file and call into one register. | `resolve_exclusion_register` | mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py:196-226 |
| The two settings keys, and the refusal-by-name discipline for a malformed value. | `read_citation_index_settings` | mcp/src/agents_remember/memory_quality/style/citations/citation_index_settings.py:56-85 |
| The bounded non-Git matcher and its pinned divergence from Git. | `FallbackIgnoreMatcher` | mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py:252-297 |
| A caller exclude that cannot mean anything is refused by name. | `validate_caller_excludes` | mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py:171-193 |
| The ruled numbers, the skip vocabulary and the status vocabulary. | `MAX_SOURCE_BYTES`; `MAX_SOURCE_FILE_BYTES`; `MAX_SOURCE_HARD_STOP_BYTES`; `SKIP_REASONS`; `STATUS_CAPPED`; `STATUS_WITHIN_CAPS` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:22-23; mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:27-27; mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:36-36; mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:38-39 |
| The register's three sources and recorded authority values. | `EXCLUSION_SOURCES`; `GITIGNORE_AUTHORITIES` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:48-52; mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:57-61 |
| The closeout gate refuses by name rather than letting a bare error out. | `_admitted_source_index` | mcp/src/agents_remember/application/prepared_certification.py:424-446 |
| The caller-exclude surface on the registered tool and the CLI. | `citation_fix` | mcp/src/agents_remember/mcp/registration/memory.py:100-128 |
| One root gives one authority on both acquisition routes. | `test_one_root_gives_one_gitignore_authority_on_both_acquisition_routes` | mcp/tests/test_citation_index_resilience.py:376-406 |

## Exact Git Candidate Source-Index Composition

Citation `Trees` selects an explicit Git candidate tree when R06/R07 require immutable candidate
membership. The source index binds that selection separately from the content snapshot: the manifest
schema (now v10, carrying the exclusion register; a v9 manifest is refused and rebuilt, not read as
"no register") and SQLite metadata distinguish a Git candidate from ordinary filesystem selection.
Candidate census includes eligible tracked build/ignored paths, excludes Git metadata and refuses
unavailable, unsafe or byte-mismatched candidate members. Ordinary filesystem use continues to
observe eligible dirty and untracked files under its existing traversal policy.

**One root gives one `gitignoreAuthority` on both acquisition routes.** The default walk records the
authority it actually had, and the explicit candidate route reports the same value for the same root
and settings (`"git"` where Git's membership applied the rules, `"register"` where the fallback
matcher did, `"absent"` where the root has no ignore file), so the record never says "these patterns
exist but nothing applied them" while Git was applying them.

R06 checks the candidate-bound lease, ready record, manifest, census and member content. R07
validates the lease against its exact unit tree before running the selected-document range checker
with the same explicit tree. These owners are usable by the recovery verifier; their library
composition does not close the production execution gap recorded above or replace full Gate 5.

| Finding | Anchor | Source |
| --- | --- | --- |
| The index opens either the explicit candidate selection or the ordinary filesystem policy. | `open_repository_index` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:360-431 |
| R06 checks candidate selection and exact indexed membership. | `observe_source_index`; `_require_index_matches_candidate` | mcp/src/agents_remember/memory_quality/incremental_scope/owners.py:100-152; mcp/src/agents_remember/memory_quality/incremental_scope/owners.py:353-404 |
| R07 validates and forwards the unit candidate tree to its selected-document checker. | `RangeResolutionAffectedExecutor` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_execution.py:67-134 |

## L34 Preparation Ownership — the closeout adapter moved out

The closeout-facing certification adapter that composed the actual affected closure, full memory
checks, missing-onboarding/index observations and curator coherence against a proved private code
view no longer lives here: commit `deb032fb` moved it out of this route because a pre-closeout
quality service must not depend on the closeout plane. It went to
`worktrees/integration/closeout/` and then **on to the application rank** in commit `806649b9`, so
its card now sits at
[application/prepared_certification.py](../application/prepared_certification.py.md). The closeout
plane may depend on this route; not the reverse. Red results remain evidence and cannot authorize
memory-content output preparation.

## Memory-Candidate Roots Relocated In, And Two Of Them Out Again

The de-entanglement cut moved this route's candidate-identity roots in from
`worktrees/integration/closeout/`: `future_code_candidate.py` and `memory_candidate_pair.py` by commit
`0b63d6fc`, and `memory_census_scope.py` by commit `be517eec`. **Commit `806649b9` then moved the
first two out again to `worktrees/modules/`** as pure renames — both blobs are byte-identical before
and after — so this route no longer owns them and no longer carries their cards; those cards were
moved to the moved modules' own route. `memory_census_scope.py` stayed and is still this route's own
memory-candidate owner. None of the three carries a closeout dependency.

| Source File | Onboarding | Status |
| --- | --- | --- |
| `future_code_candidate.py` | [../worktrees/modules/future_code_candidate.py.md](../worktrees/modules/future_code_candidate.py.md) | **relocated out** by `806649b9`; card moved with it |
| `memory_candidate_pair.py` | [../worktrees/modules/memory_candidate_pair.py.md](../worktrees/modules/memory_candidate_pair.py.md) | **relocated out** by `806649b9`; card moved with it |
| `memory_census_scope.py` | [memory_census_scope.py.md](memory_census_scope.py.md) | covered |

## 260915-KS-L16 The Family-Review Pipeline, And The Actionability Formula Given A Name

`KS-R16@v1` owns the pipeline *between* the record leaves, and this route owns the half that carries a fact
from one to the next without becoming a second source of any of them: `memory_quality/family_review.py`
composes, and `curator_checklist.py` gained the one named function that composition calls.

**Four acts, each with one failure it exists to prevent.** `group_detection_facts` deduplicates matches by
their recorded subject and declared input set and retains **every** matched condition with its supporting
paths and edges — grouping merges and never drops, and the fact group's own `retains()` is the review that
measures it. `compose_status_report` reports the five status owners separately, each with its own closed
vocabulary and its own statement of what it does *not* establish, and no field in the result could hold a
merged verdict; `detector_status` and `curator_review_status` derive two of the five from what was recorded
rather than accepting a caller's word for them. `compose_currentness` compares one authored record's
recorded binding against the caller's measurement of the current world through `KS-R15@v1`'s own comparison:
it decides no equivalence, a moved input is stale, the record stays readable and reuse is refused, and
`curator_currentness_status` reduces a sequence of those findings to the one state the route publishes.
`route_family_review` counts the shipped formula's three terms **once**, beside the family-review row count,
and reports that family rows moved nothing; `family_review_summaries` and `reported_subject_status` are the
read-only reductions over the same records.

**The arithmetic has one definition, and it is now a function with one name.**
`curator_checklist.py`'s shipped `repair + missing + stale` expression — the one `write_curator_checklist`
already computed inline — was extracted into `curator_actionable_count(repair, missing, stale)`, and the
checklist writer's one call site calls it. The **value and the behaviour are unchanged**: this leaf's
`KS-R16@v1` §5.3 requires that the formula gain no fourth term, and naming it is what makes that property a
property of one definition rather than a convention each consumer restates. The pipeline calls it instead of
re-implementing the sum, so the routing report cannot drift from the checklist it reports into. The
`knowledgeReview` section this pipeline renders into is `KS-R15@v1`'s own: there is no second worklist, no
second reports directory and no second counter on this route.

**The one thing the pipeline refuses to do is invent a conclusion.** Nothing in the module reads a
rationale, a path's bytes, a label or a count to decide whether a change matters. A caller that finds a stage
here attaching a verdict has found the defect, and the fix is to remove it rather than to author it in code.

## 260918-TSIP-L6 `citation_migrate`'s Preview Stops Reporting A Plan As A Failure

`T64`: `memory_quality/style/citations/migration.py::payload` (`:767-833`) folded three facts
into `ok` — declined, remaining, and `dry_run` — so a **preview** that had produced its complete
plan reported `ok: false`, while its sibling `citation_fix` answers `ok: true` on the equivalent
preview of the same family. A caller could not tell "nothing to migrate" from "the operation did
not happen".

`ok` now answers *did this call do what it set out to do*: `not blocked`, where
`blocked = bool(result.declined) or (not dry_run and bool(result.remaining))`. The two facts that
were folded in are declared separately — `state` (`"refused"` / `"planned"` / `"converted"`) and
`outcome` — and `remaining` is never read on a dry run, because it is a post-write measurement
(`migrate_onboarding_root` fills it only on the non-dry branch). Reading it while previewing
would answer `ok: false, state: "planned"`, which is `T64`'s symptom returning through the other
fact the old expression folded in. The truth table, including that row, is pinned by
`mcp/tests/test_response_address_binding.py:225-291`; the entry-point sweep's third pin
(`UNMARKED_NOT_OK`) was emptied in the same change.

## 260918-TSIP-L7 The Definition-Outside-Range Report, And The Escape That Made A Construct Invisible

Two changes land in this route's citation machinery, both report-only in effect and both proven by a
case in `mcp/tests/test_memory_citation_agreement.py` rather than by a report:

- **`T52` — a construct that moved INSIDE its cited range is now counted.** `range_resolution` asks
  whether an anchor OCCURS in a cited range, and a construct's name occurs at every call site, so a
  range the definition has left stays green for as long as anything inside it still spells the name.
  `definition_outside_range_findings`
  (`memory_quality/style/citations/range_resolution.py:466-513`) fires only when the anchor is a
  **symbol**, exactly **one** of its definitions exists across the cited files, that definition is
  inside **no** cited range, and the name still occurs in one; `check_onboarding_root` (`:650-685`)
  emits it, and the payload carries it in the new key `definitionsOutsideCitedRanges` (`:718`).
  `ok` and `findingCount` are unchanged: this is a report, not a gate, and the siblings it belongs
  with are already report-only.
- **`T57` — GFM's `\|` escape is resolved where cell text becomes anchor text.** `cells.unescaped`
  (`memory_quality/style/citations/cells.py:40-53`) is applied to **both** cells, so
  `` `useEffect(cb, [a \| b])` `` reaches the anchor grammar as the anchor its unescaped spelling
  yields instead of being silently counted as an *unchecked span* — reading as checked and not being
  checked. The bound is one literal `\|` → `|` replacement, which is GFM's own reading: with two
  backslashes the second is the one consumed and the source's `a | b` stays unmatched.

The populations both changes measure on the leaf memory worktree (base `fd1a024e`) are pinned in the
new module rather than restated here: **120** definition-outside-range rows and an enforced population
of **283**, with the `T58` wrapped-`cit:` population at **3** constructs in **2** documents. The
module's own header cites `application/memory_tools.py:100` for `_refuse_official_memory`; in the tree
it pins, that definition is at **`:105`** (`:100` is `"onboardingRoot": scope.onboarding_root.as_posix(),`)
— recorded as the leaf's `R2-3`.

## 260921-ICR-L15 Measured assessment currentness

`ICR-R15@v1` splits one fact this route's section used to fold together — *a record's binding moved* — from
two it never stated: *nothing measured this record*, and *a measurement found it still current*. The route
owns both halves of that split: the vocabulary in `family_review.py` (452 → 457 lines) and the reader that
publishes it in `knowledge_review.py` (210 → 230).

**The vocabulary is the whole six.** `reported_subject_status`'s docstring now names every member the
projection can answer — `none-recorded`, `stale`, `unavailable`, `unresolved`, `not-measured`, `current` —
in the projection's own precedence order, where it previously listed four. `not-measured` is what a caller
whose measurement covered **none** of a record's declared inputs gets, and `unavailable` is what a failed
measurement gets; neither is a clearance and neither is a movement. There is still no "compatible" member
and no default, so a subject nobody reviewed answers `none-recorded` rather than the absence being rendered
as a clearance.

**The count travels the whole pipeline.** `family_review_summaries` passes `state.notMeasuredCount` into
`AssessmentSummaryInput` beside `unresolvedCount` and `staleCount`, and
`application/memory_quality/controller.py` (847 → 848 lines) passes the same field through its own
composition, so the number the checklist renders is the projection's own rather than a second measurement
taken beside it.

**The persisted checklist gains a `not-measured` limitation row and count, and `stale` narrows to a
measured movement.** `memory_quality/knowledge_review.py` declares `NOT_MEASURED_BINDING = "not-measured"`,
adds `notMeasuredCount` to `AssessmentSummary` and `AssessmentSummaryInput`, and renders a dedicated
limitation row beside the re-worded `stale` row, whose limit now reads *a measurement of the current inputs
found this record's binding moved*. The reason is the reading a bare `| stale | 0 |` line invites: with an
unmeasured collection counted nowhere, a zero could be read as "nothing moved" when nothing had been
measured at all. `summarise_assessment_state` keeps the counts exact — the negative check now includes
`notMeasuredCount` and the bound is that `staleCount + notMeasuredCount` cannot exceed `assessmentCount` —
and `_limitations` lists `not-measured` beside the other counted codes, so the section's vocabulary and the
counts it renders cannot disagree.

## 260928-MIK-L22 The Mandatory Knowledge Validator Joins This Route

**This route gained `knowledge_validator/`, the integrity check that replaces database constraints once
knowledge is text in Git (D18).** It is governed here rather than by its own overview, following the
sibling subpackages (`final_certification/`, `integrity/`, `style/`), which have none. Its
file-level cards carry the per-module detail; the route-level facts are these:

- **One registry, run everywhere.** MIK-R22 registers 16 rules (rules 1–7), and later packets (MIK-R04,
  R20, R27, R13) add theirs with `register_rule`. Every caller (the managed sync's memory merge today,
  the `agents-remember knowledge-validate` command, later the writer and MIK-R09's routes) runs all of
  them. Three rules are report-only by registry flag: a file sidecar without Markdown, an unresolved
  reference target, and a carried anchor at an absent path.
- **Where it sits in the layering.** The package ranks with `memory_quality`, so the worktree layer
  reaches it only through `worktrees.services.KnowledgeValidationPort`, which
  `application/worktree_services.py` binds to `commit_route.GitKnowledgeValidation`. The CLI imports it
  directly, and `cli/knowledge_format.py` shares its `trees.is_excluded_from_knowledge` predicate.
- **Production is unchanged before MIK-R37.** Applicability is the layout marker on the candidate or any
  base; the live memory repository has none, so every route returns before the validator runs.
- **What it does not judge.** Meaning (Doc13), and whether an anchor's content still matches the code
  (currentness, MIK-R03). Only path existence is checked, and only for anchors no base carries.

| Finding | Anchor | Source |
| --- | --- | --- |
| The package's module map and public API. | `__all__` | mcp/src/agents_remember/memory_quality/knowledge_validator/__init__.py:56-76 |
| The single registry. | `register_rule`; `registered_rules` | mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:68-74; mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:77-80 |
| The commit route's call, with no skip parameter. | `require_valid_commit`; `validation_applies` | mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:88-91; mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:94-109 |
| The Git adapter the worktree port binds to. | `GitKnowledgeValidation` | mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py:31-80 |
| The registered rule sets, with their report-only flags. | `STRUCTURE_RULES`; `REFERENCE_RULES` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_structure.py:134-163; mcp/src/agents_remember/memory_quality/knowledge_validator/rules_references.py:229-269 |

## 260928-MIK-L04 Family Route Rules Join The Knowledge Validator

**MIK-R04@v2 adds six rules to `knowledge_validator/`'s one registry, and the route logic they share.**
[`family_routes.py`](knowledge_validator/family_routes.py.md) computes one family's route state over the
realization entries of the same tree (proof entries never count): Coverage, Non-empty, the reported states
`unrealized_family` and `route_unassigned`, the retired exemption, and the mechanical route suggestion,
labelled `mechanical` and never written. [`rules_routes.py`](knowledge_validator/rules_routes.py.md)
registers the rules, and `validator.py` imports it, so every place the validator runs runs them:

- **Refused:** an added route that is not a directory of the paired code tree (`R04.1-route-directory`),
  a realization under no route or a family with `routes: []` that is not an unassessed export
  (`R04.2-coverage`), and a route with no realization (`R04.2-non-empty`).
- **Reported, never refused:** a route carried from a base whose directory is gone
  (`R04.1-carried-route-absent`, `route_path_absent` for MIK-R06), `R04.4-unrealized-family` and
  `R04.4-route-unassigned`.
- **Reported inside the writer.** The three refusing rules carry the new registry flag `writer_reports`;
  `writer_reported_rule_ids()` names them. Every commit route still refuses them; only the writer (MIK-R12)
  downgrades them to reports, so a leaf may break a route rule mid-way and repair it before closeout.
- **Directory existence.** [`trees.py`](knowledge_validator/trees.py.md)'s `CodeTree` gains `has_directory`;
  the root route `.` always exists.

The validator cannot tell a broad route from a deep one; route depth stays curator judgment, helped by the
suggestion and the `agents-remember knowledge-routes` command.

| Finding | Anchor | Source |
| --- | --- | --- |
| One family's route state over its members' realizations. | `FamilyRouteState` | mcp/src/agents_remember/memory_quality/knowledge_validator/family_routes.py:72-132 |
| The six registered rules, three report-only and three writer-reported. | `ROUTE_RULES` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_routes.py:174-217 |
| The registry flag a writer reads. | `writer_reported_rule_ids` | mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:83-88 |

## 260928-MIK-L20 The Migration Census Joins This Route

**MIK-R20@v2 adds `knowledge_census/`, the census over text files, and nine census rules to the validator's
one registry.** The package reads a memory tree's bytes only and depends on nothing above `models`:

- [`files.py`](knowledge_census/files.py.md) reads every file under `knowledge/census/` into parsed census
  directories and problems (location, schema, census and route-slug agreement, canonical formatting, and a
  census missing its baseline or inventory).
- [`checks.py`](knowledge_census/checks.py.md) holds the nine refusing rules: shape, canonical, pinned
  (exactly `baseline.json` and `inventory.json` never change once committed), claim rows, stable claim fields
  (`id`, `text`, `location`, `kind` and `applicability` never change), claim records, known routes, and the
  append-only status and assessment rules (prefix at one base, subsequence at a merge).
- [`measures.py`](knowledge_census/measures.py.md) computes `N = T + F + U + P` over the assessable cohort and
  the Doc12 measures; a zero denominator is "not applicable", and every percentage carries its counts.
- [`report.py`](knowledge_census/report.py.md) builds one report per census, sliced by route and claim kind,
  with each route's governing status (the latest entry across every census).
- [`__init__.py`](knowledge_census/__init__.py.md) re-exports them.
- [`knowledge_validator/rules_census.py`](knowledge_validator/rules_census.py.md) registers the nine rules,
  running the checks once per validation; `validator.py` imports it. `parsed.py` still skips
  `knowledge/census/`, so the validator is not forked.

No separate `knowledge_census/overview.md` was created, following the sibling subpackages. The census writer
(`memory/knowledge_census/writer.py`) runs the same checks before every write.

| Finding | Anchor | Source |
| --- | --- | --- |
| The nine census rules. | `CENSUS_RULES` | mcp/src/agents_remember/memory_quality/knowledge_census/checks.py:52-65 |
| The measures in Doc12's order. | `compute_measures` | mcp/src/agents_remember/memory_quality/knowledge_census/measures.py:137-160 |
| The registration with the validator. | `CENSUS_VALIDATION_RULES` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_census.py:54-57 |


## 260928-MIK-L24 The Converted Format Joins This Route

**MIK-R24@v1 rule 5: on a converted memory tree this route's checks read the text format.** Two new modules
and four touched ones carry it. Nothing changes on an unconverted tree, and no production tree is converted
before MIK-R37.

- [`reference_state.py`](reference_state.py.md) is reference currentness over sidecars: `current`, `stale`,
  `stale:unresolved` or `stale:path-absent` in the code working tree. A stale reference is **report-only,
  never a gate finding**; the onboarding gate (MIK-R30) is its refresh route. The fixer re-records only
  mechanically moved anchors. `application/memory_tools` routes `citation_check` and `citation_fix` here
  on a converted tree.
- [`converted_check.py`](converted_check.py.md) is the converted run. The legacy-format checks (Update
  History order, `range_resolution`, `claim_reopen`) report `not-applicable-converted`. The drift slot
  becomes `knowledge.converted`: the validator's refusals are findings, and its reports and stale references
  are report-only.
- [`check.py`](check.py.md) dispatches every selected check by format (`_converted_check`).
- [`knowledge_validator/commit_route.py`](knowledge_validator/commit_route.py.md) takes an optional
  `base_converter` (rule 7). The composition binds `memory/conversion/base.GitBaseConverter`, so a
  converted merge whose base is unconverted is validated against that base's conversion.
- [`knowledge_validator/markers.py`](knowledge_validator/markers.py.md) gains `escape_markers`, the
  conversion's one escaping rule on the validator's own grammar.
- [`style/citations/extents.py`](style/citations/extents.py.md) gains `qualified_spans`, the one
  symbol-binding rule the curator writer, the conversion and the reference check share. The
  conversion-format version pins it.
- The rule 9 refusal runs in the memory-quality controller (`application/memory_quality/controller.py`,
  the `application` route). It is inert until the official line is converted (architect ruling).

| Finding | Anchor | Source |
| --- | --- | --- |
| Stale references are report-only. | `check_references` | mcp/src/agents_remember/memory_quality/reference_state.py:125-157 |
| The converted run's legacy-format checks and its validator slot. | `LEGACY_FORMAT_CHECKS`; `converted_knowledge_check` | mcp/src/agents_remember/memory_quality/converted_check.py:31-37; mcp/src/agents_remember/memory_quality/converted_check.py:66-93 |
| The runner's dispatch by format. | `_converted_check` | mcp/src/agents_remember/memory_quality/check.py:163-177 |
| The commit route's optional base converter. | `GitKnowledgeValidation` | mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py:31-80 |
| The escaping rule on the validator's grammar. | `escape_markers` | mcp/src/agents_remember/memory_quality/knowledge_validator/markers.py:142-162 |
| The one symbol-binding rule. | `qualified_spans` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:159-178 |

## 260928-MIK-L28 The Checklist Lists The Invariants Without Proof, As Information

**Route meaning extended (MIK-R28@v1 rule 5).** [`curator_checklist.py`](curator_checklist.py.md) gains a
defaulted `without_proof` input and renders an "Invariants without proof" section after the
`knowledgeReview` section: one row per live invariant no proof entry names, with the tests its recorded
evidence mentions, so a curator pass knows where to start turning migrated evidence into proofs. **The list
is checklist-only and informational (architect ruling, 2026-09-29):** it is not an input to
`curator_actionable_count`, the attestation or the wire summary, and no count field is added to the strict
summary model. The controller passes `None` for every unconverted tree, so the checklist bytes are
unchanged before MIK-R37.

| Finding | Anchor | Source |
| --- | --- | --- |
| The defaulted input and its section. | `WithoutProof`; `_append_without_proof` | mcp/src/agents_remember/memory_quality/curator_checklist.py:66-71; mcp/src/agents_remember/memory_quality/curator_checklist.py:73-78; mcp/src/agents_remember/memory_quality/curator_checklist.py:354-386 |

## 260928-MIK-L08 The Checklist Shows The Leaf's Worklist, As Information

**Route meaning extended (MIK-R08@v2 rule 7).** The new
[`knowledge_worklist_section.py`](knowledge_worklist_section.py.md) renders the leaf's persisted
`knowledge-worklist/v1` document as the checklist section "Knowledge worklist (MIK-R08)": state, file,
digest, pairing, and one row per item (or the unreadable inputs of an `incomplete` run). Its
`worklist_summary` is the compact summary the memory-quality response, the managed-sync response and
`knowledge_integrity_check` carry. [`curator_checklist.py`](curator_checklist.py.md) gains the defaulted
`knowledge_worklist` and `knowledge_worklist_path` inputs and renders the section after the "without proof"
section.

- **Information, never a count.** The worklist never enters `curatorActionableCount`, the attestation or the
  wire counts; what an open item blocks is MIK-R09's closeout gate, live at the cutover.
- **Unchanged for unconverted leaves.** With no worklist the section is not rendered, so today's checklist
  bytes are unchanged.

| Finding | Anchor | Source |
| --- | --- | --- |
| The section and the summary. | `knowledge_worklist_lines`; `worklist_summary` | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:27-38; mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:194-242 |
| The checklist's defaulted inputs. | `knowledge_worklist`; `knowledge_worklist_path` | mcp/src/agents_remember/memory_quality/curator_checklist.py:69-70 |

## 260928-MIK-L30 The Update History Fixer Steps Aside On A Converted Tree

MIK-R30 rule 5 retires the Update History ordering checks and their fixers at the cutover.
`style/update_history/history_order_fix.fix_onboarding_root` now returns `not-applicable-converted` without
reading or writing anything when the onboarding root's parent holds `knowledge/layout.json`; the diagnostic
check was already not applicable there (MIK-R24). On an unconverted tree both are unchanged. Deleting
`style/update_history/` is left to MIK-R37 (architect ruling 2026-09-29T18:49:50 (5)), because deleting it
now would change today's gate on unconverted trees. The gate that replaces Update History on converted trees
is `worktrees/modules/onboarding_trace.py`; this route gains no new module.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixer's converted-tree early return. | `fix_onboarding_root`; "not-applicable-converted" | mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py:33-66 |

## 260928-MIK-L11 The Worklist Section Shows The Planned Effects

**Route meaning extended (MIK-R11 rule 7, visibility).** The worklist section rendered by
[`knowledge_worklist_section.py`](knowledge_worklist_section.py.md) gains three things, all inside the
section and so only on converted leaves:

- a **"Planned effects (MIK-R11)"** block before the item table: one line when the leaf's task document
  declares nothing ("every item is `unplanned`"), otherwise one line per declaration with its planned key,
  its `requirementRef`, and either the row or invariant that matched it or **unmatched** with the reason and
  whether a planned row answers it;
- a **Plan** column in the item table, showing each invariant and family item's `planning` mark (`-` for a
  kind with none);
- the facts of a `planned_untouched` item: the declaring requirement, the unmatched reason, each row about
  the declared record marked "(does not deliver it)", and "answered by" or "needs a planned row".

The section stays information, never a count: MIK-R09's gate (L09) is what enforces an open
`planned_untouched` item, through `models/knowledge_files/planned.planned_item_open`. Because the `planning`
mark sits inside every item, every converted worklist's digest and checklist change against a worklist
persisted before MIK-R11; that is carried to L09 (ruling F4, 2026-09-29T22:35:34+02:00). The reviewer-UI
half of rule 7 is carried to L31 (ruling Q1, 2026-09-29T21:56:18+02:00). Unconverted leaves render no
section, so today's checklist bytes are unchanged; this curation's own `memory_quality_check` runs produced
no worklist.

| Finding | Anchor | Source |
| --- | --- | --- |
| The planned-effects block and the `planned_untouched` facts. | `_planned_lines`; `_planned_facts` | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:71-81; mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:115-141 |
| The item table's **Plan** column. | `knowledge_worklist_lines`; "Plan" | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:194-242 |

## 260928-MIK-L27 The Admission Rule Joins The Knowledge Validator

**MIK-R27@v1 adds three rules to `knowledge_validator/`'s one registry (MIK-R22 rule 9).**
[`rules_admission.py`](knowledge_validator/rules_admission.py.md) registers them and `validator.py` imports
it, so the writer and every commit route run them. Every invariant, family and decision record states
the admission criterion it meets with a one-sentence justification; admission governs **creation, not
maintenance**:

- **Refused on a new record** (`R27.2-new-record`). A record is new when no comparison base holds its ID
  and it is not an export; an export is a record whose `origin.legacyId` derives its ID through the
  conversion's own `derived_record_id`, so a hand-written legacy ID does not exempt a record (ruling
  2026-09-29T23:04:57 F2). It is refused for `legacy-unassessed`, for a justification made only of
  references (task, leaf, requirement, step and section IDs, developer-ruling IDs and commit hashes by
  ruling 22:11:24 Q2, ISO dates, and provenance filler words by ruling 23:04:57 F1), or for a
  `spans_locations` or `guarded_by_test` claim the tree does not support. No criterion at all is refused
  earlier, by the shape rule.
- **"Supported by the index"** is read from the sidecar `realizes` and `proves` entries the derived index
  is built from, in the tree the validator already parsed, because this route ranks below
  `memory/knowledge_index` (ruling 22:11:24 Q1). `spans_locations` needs realizations in two or more
  files; `guarded_by_test` needs a proof entry naming the invariant.
- **Reported, never refused:** the same unsupported claim on an existing or exported record
  (`R27.2-existing-record`), and one tree-level count of the live `legacy-unassessed` records
  (`R27.4-legacy-unassessed`). Retired records are exempt from both admission rules.
- **Writer.** None of the rules is writer-reported, so the writer refuses a new record exactly as a commit
  route does.

Only presence, shape, the reference-only form and the two checkable criteria are mechanical; plausibility
is the reviewer's (OM-4). The rules refuse nothing until records are authored on a converted line: the
validator runs only over converted trees, the conversion commit holds only exports and a crossing sync
only records a parent holds. Unconverted memory is unchanged, and this curation's own
`memory_quality_check` runs produced no worklist. Carried: closeout and landing validating admission
against the parent line (L09, ruling Q6); demotion's realization entries and the census outcome (the R19
follow-up, ruling Q5).

| Finding | Anchor | Source |
| --- | --- | --- |
| A new record is refused for an unsupported claim, legacy-unassessed or a reference-only justification. | `check_new_record_admission` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_admission.py:247-273 |
| An export is a record whose legacy ID derives its ID. | `_exported` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_admission.py:180-192 |
| The three rules, one refusing and two report-only. | `ADMISSION_RULES` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_admission.py:307-328 |

## 260928-MIK-L06 The Worklist Section Renders The Family Route Conditions

**Route meaning extended (MIK-R06@v2, visibility).** The worklist section rendered by
[`knowledge_worklist_section.py`](knowledge_worklist_section.py.md) now describes the new
`family_route_condition` items (computed on the application route by
`application/knowledge_worklist/route_conditions.py`): the condition and the affected routes or entry paths
(the base view's when it shows the condition), where the renamed files went, the MIK-R04 mechanical
suggestion or "no suggestion" when the rename target is ambiguous or a file is absent at C without a rename
(ruling Q5, with `unmappedLocations` named), and "answered by <row>" or "needs a family row (rerouted,
assigned, changed or retired; never no_impact) and routes that satisfy MIK-R04".

`_item_facts` now dispatches through a kind-to-renderer table (`_FACT_RENDERERS`, review R3-N1) instead of an
`if`/`elif` ladder; every earlier kind renders the same text. The section stays information, never a count:
enforcing an open route item is MIK-R09's gate (L09), through
`application/knowledge_worklist.family_route_item_open`. Unconverted leaves render no section, so today's
checklist bytes are unchanged; this curation's own `memory_quality_check` runs produced no worklist.

| Finding | Anchor | Source |
| --- | --- | --- |
| The route item's facts, its affected set and its suggestion text. | `_route_facts`; `_route_affected`; `_route_suggestion` | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:144-160; mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:163-168; mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:171-174 |
| The kind-to-renderer table (since MIK-R10 it also maps the two unexplained kinds). | "_FACT_RENDERERS: Final[" | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:177-187 |

## 260928-MIK-L13 The Decision Content Rules Join The Knowledge Validator

**MIK-R13@v2 adds five rules to `knowledge_validator/`'s one registry (MIK-R22 rule 9).**
[`rules_decisions.py`](knowledge_validator/rules_decisions.py.md) registers them and `validator.py` imports it, so
the writer and every commit route run them over every decision record; the checks are the pure functions of
`models/knowledge_files/decisions.py`.

- **Refused:** fewer than two alternatives, or not exactly one `chosen` (`R13.1-alternatives`); a `rejected` or
  `deferred` alternative without `reconsider_when` (`R13.1-reconsider-when`); a stored `superseded`, as the status
  or an alternative's, named from the raw JSON because it never parses (`R13.2-superseded-derived`, next to the
  shape rule); a `reconsider_on` link whose `alternative` is out of range or `chosen` (`R13.3-reconsider-on`,
  ruling 2026-09-30T01:45:56 Q2).
- **Reported:** a decision with no `explains`, `constrains` or `motivated_change_to` link (`R13.3-governs`,
  report-only by ruling Q2).
- **Every decision, new or carried** (ruling Q3). None of the rules is writer-reported.
- **Not here:** `origin` naming the task is MIK-R21's shape, and the ruling travels in the attached entry's
  evidence (ruling Q1); unresolved requirement endpoints are reported by the writer, because this route has no task
  plane (Q5/Q6, carried to L14).
- **Admission (review F6, ruling 02:05:07):** [`rules_admission.py`](knowledge_validator/rules_admission.py.md)'s
  `_exported` is `False` for every `DecisionRecord`, since the conversion exports no decisions; a `legacyId` on a
  decision exempts it from nothing.

The rules refuse nothing until decisions are authored on a converted line: the conversion writes no
`knowledge/decisions/` directory, and base and leaf builds gave byte-identical `knowledge-validate` reports on a
freshly converted scratch copy. Unconverted memory is unchanged, and this curation's own `memory_quality_check`
runs produced no worklist.

| Finding | Anchor | Source |
| --- | --- | --- |
| The five rules, four refusing and one report-only. | `DECISION_RULES` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_decisions.py:112-144 |
| A stored superseded is named from the raw document. | `check_superseded_not_stored` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_decisions.py:80-97 |
| A decision is never an export for admission. | "if isinstance(record, DecisionRecord):" | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_admission.py:189-190 |

## 260928-MIK-L10 The Worklist Section Renders The Unexplained Changes

**Route meaning extended (MIK-R10@v2, visibility).** The worklist section rendered by
[`knowledge_worklist_section.py`](knowledge_worklist_section.py.md) now describes MIK-R10's `unexplained_hunk` and
`unexplained_file` items (computed on the application route by `application/knowledge_worklist/unexplained.py`):
the path and each hunk as `-<start>,<count> +<start>,<count>` (or a file change's content and status), the
coverage (covered or uncovered, the realization-entry count, the governing route and its migration status),
"delete-only: only no_invariant" for a delete-only hunk, and "answered by <row or counted-change>", or for an open
item "needs attach/author or a no_invariant row `hunk:…`" (covered) or "needs the onboarding trace
`onboarding:<path>`" (uncovered). `_unexplained_facts` is two entries of the `_FACT_RENDERERS` table; no branch was
added (the L06 sync).

The section stays information, never a count: an open unexplained item is enforced by MIK-R09's gate (L09) through
`models/knowledge_files/unexplained.unexplained_item_open`. On the application route the memory-quality controller
also keeps an `onboarding:<path>` row that answers an uncovered item out of MIK-R30's unnecessary-row report
(ruling 2026-09-30T01:56:39 Q3). Unconverted leaves render no section, so today's checklist bytes are unchanged;
this curation's own `memory_quality_check` runs produced no worklist. Grouping the (by design numerous) unexplained
items for the curator is carried to L31/L32.

| Finding | Anchor | Source |
| --- | --- | --- |
| An unexplained item's facts: where, coverage, delete-only, and what answers it. | `_unexplained_facts` | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:84-112 |
| The two unexplained kinds in the renderer table. | "\"unexplained_file\": _unexplained_facts," | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:185-186 |

## Update History
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): **route body updated for MIK-R10.** Added the section "260928-MIK-L10 The Worklist Section Renders The Unexplained Changes" after L13's (`_unexplained_facts` as two `_FACT_RENDERERS` entries; the Q3 onboarding-row rule; the L31/L32 carry), two rows. **Reopened claim reworded:** L06's `_FACT_RENDERERS` row (the table gained two entries) is re-anchored on the line-exact quote "_FACT_RENDERERS: Final["; this pass's fixer bullet for it was removed. The entry is in the real list after the last section, not the inline `## Update History` mention. No verification stamp was advanced.
- 2026-09-30T03:13:03+02:00 — 260928-MIK-L13 curator (uncommitted change set on `ar/260928-mik-l13`, code base `3772cdcd008fcacdc5a86e264a3ef63e879ea544` plus the staged delta): **route body updated.** Added the section "260928-MIK-L13 The Decision Content Rules Join The Knowledge Validator" after L06's: the five `rules_decisions.py` rules, rulings 01:45:56 Q1–Q3 and Q5/Q6, and the review F6 admission guard in `rules_admission.py`. Three rows. The entry is in the real list after the last section, not the inline `## Update History` mention. No verification stamp was advanced.
- 2026-09-30T01:22:26+02:00 — 260928-MIK-L06 curator (uncommitted change set on `ar/260928-mik-l06`, code base `c493b55731545a090d6b81f504bf02e1e427ec74` plus the staged delta): **route body updated for MIK-R06.** Added the section "260928-MIK-L06 The Worklist Section Renders The Family Route Conditions" (`_route_facts` and its helpers, the `_FACT_RENDERERS` dispatch table from review R3-N1), with two rows; L11's two rows into `knowledge_worklist_section.py` were re-measured by hand (`72-82`/`85-111` → `71-81`/`84-110`, `118-166` → `161-209`). The entry went into the real list after the last section, not into the inline `## Update History` mention. No verification stamp was advanced.
- 2026-09-30T00:17:15+02:00 — 260928-MIK-L27 curator (uncommitted change set on `ar/260928-mik-l27`, code base `46ca74302e76cf40fb6370ea9ece16d8fa719f00` plus the staged delta): **route body updated for MIK-R27.** Added the section "260928-MIK-L27 The Admission Rule Joins The Knowledge Validator" (the new, carded `rules_admission.py`, governed by this overview), recording architect rulings 2026-09-29T22:11:24 (Q1, Q2, Q5, Q6) and 23:04:57 (F1, F2), with three rows; the Route Model bullet names the module. The entry went into the real list after the last section, not into the inline `## Update History` mention. No verification stamp was advanced.
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): **route body updated for MIK-R11.** Added the section "260928-MIK-L11 The Worklist Section Shows The Planned Effects" (the planned-effects block, the **Plan** column and the `planned_untouched` facts), recording architect rulings 2026-09-29T21:56:18 (Q1) and 22:35:34 (F4). L08's section-and-summary row was re-measured (`knowledge_worklist_lines` now `118-166`). The entry went into the real list after the last section, not into the inline `## Update History` mention. No verification stamp was advanced.
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): **route body updated for MIK-R30.** Added the section "260928-MIK-L30 The Update History Fixer Steps Aside On A Converted Tree" (the `not-applicable-converted` return, architect ruling 2026-09-29T18:49:50 (5)). One row. The entry went into the real list after the last section, not into the inline `## Update History` mention in the `style/update_history/` bullet. No verification stamp was advanced.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): **route body updated for MIK-R08.** Added the section "260928-MIK-L08 The Checklist Shows The Leaf's Worklist, As Information": the new `knowledge_worklist_section.py` (carded, governed by this overview) and the checklist's defaulted worklist inputs, never counted. The entry went into the real list after the last section, not into the inline `## Update History` mention in the `style/update_history/` bullet.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): **Route body update (MIK-R28).** New section: the checklist's informational "Invariants without proof" section, with the architect ruling that the list is checklist-only and never counts toward `curatorActionableCount`. One row. The entry went into the real list after the last section, not into the inline `## Update History` mention. The `_attach_final_full_catalog` row was re-pointed by the exact line map, and five further rows were re-pointed or normalised by the installed `memory-citations --fix`, with no wording change.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): **Route body update (MIK-R24 rule 5).** New section "260928-MIK-L24 The Converted Format Joins This Route", covering the two new modules (`reference_state`, `converted_check`), the four touched ones (`check`, `commit_route`, `markers`, `extents`) and the rule 9 ruling, with six rows. The entry sits in the real Update History list after the last section, not in the inline mention inside "Deterministic Citation Document Publication".
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): **route body updated — new section "260928-MIK-L20 The Migration Census Joins This Route"** for the five new `knowledge_census/` cards and the new `knowledge_validator/rules_census.py` card, plus the `validator.py` and `parsed.py` changes; the Route Model gains a `knowledge_census/` bullet and names `rules_census.py`. No separate `knowledge_census/overview.md` was created. No stamp advanced.
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): **route body updated — new section "260928-MIK-L04 Family Route Rules Join The Knowledge Validator"** for the two new cards (`family_routes.py`, `rules_routes.py`) and the `registry.py`/`trees.py`/`validator.py`/`__init__.py` changes. The L22 section's `__init__`, registry and validator rows were re-pointed by the exact line shift (the validator row's two ranges put back in anchor order), and the installed fixer re-normalised older passing ranges in this document; no claim wording changed there. No stamp advanced.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): **route body updated — the mandatory knowledge validator joins this route.** Added `knowledge_validator/` to the Route Model and the Hot Path Summary, a new first invariant (no converted memory commit without a passing validator run; no skip), and the section "260928-MIK-L22 The Mandatory Knowledge Validator Joins This Route". The package's eleven modules got new file cards governed by this overview; no separate `knowledge_validator/overview.md` was created, following the sibling subpackages. No verification stamp was advanced.
- 2026-09-23T12:00:00+02:00 — 260921-ICR-L15 curator (uncommitted change set; leaf base commit `3103e1142a3ded8a843c3e5bbefca14861ba4a58` plus the working-tree delta): **added the `260921-ICR-L15 Measured assessment currentness` section above.** It records the two governed sources this leaf changed under this route: the six-member status vocabulary `reported_subject_status` now enumerates in the projection's own precedence order and the `notMeasuredCount` the pipeline carries end to end (`family_review.py`, 452 → 457 lines, with `application/memory_quality/controller.py` 847 → 848), and the persisted checklist's new `not-measured` limitation row and count beside the narrowed meaning of `stale` (`knowledge_review.py`, 210 → 230). This is a body change and not a metadata-only refresh, which is why it is recorded here. This document carried **no** repairable citation finding, so no citation range on it was touched. No verification stamp was advanced: the candidate is uncommitted — the honest basis is the leaf base commit `3103e1142a3ded8a843c3e5bbefca14861ba4a58` plus the working-tree delta — so no commit contains the content a stamp would claim to have verified, and the governed closeout owns the real code and memory commits.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-19T22:58+02:00 — 260918-TSIP-L7 curator (uncommitted change set on `ar/260918-tsip-l7-ar`, memory worktree base `fd1a024e`): **added the L7 section** — the two citation changes this leaf lands under this route (`definition_outside_range_findings` and the `definitionsOutsideCitedRanges` payload key at `range_resolution.py:466-513`/`:650-685`/`:718-718`; `cells.unescaped` at `cells.py:40-53`), each named with the shape it fires on and the bound it does not exceed, and the population the agreement module pins on the leaf memory worktree (120 / 283 / 3 / 2) recorded as a pin held elsewhere rather than restated. It also records the module header's wrong-tree-adjacent line number for `_refuse_official_memory` (`R2-3`: the header says `:100`, the definition is at `:105`). The body changed substantively and this entry is the history record; `lastVerifiedCommitHash` is not advanced because the candidate is uncommitted and the governed closeout owns the real code commit. No other claim in this document was re-read.
- 2026-09-19T19:54+02:00 — 260918-TSIP-L6 (uncommitted change set on `ar/260918-tsip-l6-ar`, base `a1351504`): recorded `T64` — `citation_migrate`'s preview answers `ok: true` with `state: planned`, and `remaining` is never read on a dry run; the two facts the old `ok` folded in are now declared separately. Citation range re-derived against the repaired file. Verification metadata stays closeout-owned.
- 2026-09-18T19:56:44+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the three enforced `citation_anchor_absent_from_range` rows in this document** (two table rows). (a) The readiness row cited `controller.py:583-600` for `"def _attach_final_full_catalog("`, whose definition this leaf's changes left at `671-707`; that cell cites it now. (b) and (c) The entry-point row cited `110-125` and `318-360` for `run_memory_quality_request` and `_execute_memory_quality`; the two definitions now span `249-255` and `383-435`, which is what the cell cites. Claims, anchors and the other ranges are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T18:40+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **repointed this route at the two candidate-identity modules commit `806649b9` moved out to `worktrees/modules/`.** The route's source is unchanged by this pass — the change is that two cards used to be reached from here and now are not, so the `Memory-Candidate Roots Relocated In` section and the two prose mentions of `future_code_candidate.py` / `memory_candidate_pair.py` now say where those modules actually live and link to their cards' new paths. Leaving the old links would have made this overview the last dead reference to the retired `memory_quality/` sidecars. No verification stamp is advanced: this route's own source did not change, and the entry records a documentation move, not a re-read of this route. `memory_census_scope.py` is unaffected and still this route's.
- 2026-09-18T14:05+02:00 — 260915-KS-L16 curator (uncommitted change set on `ar/260915-ks-l16`, base `7b1db4e0`): **added the L16 section** — the route's new `family_review.py` with its four acts and the failure each exists to prevent, and the one change this leaf made to a shipped module: the three-term actionability formula extracted into the named `curator_actionable_count`, whose value and behaviour are unchanged and whose one call site is the checklist writer. The section states the two boundaries a reader must not flatten — the pipeline calls the shipped function rather than restating the sum, and it renders into `KS-R15@v1`'s existing `knowledgeReview` section rather than creating a second worklist. The metadata block above now names this leaf's candidate as what was read; the body was changed substantively and this entry is the history record, not a metadata-only refresh.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read this route against its changed sources and wrote the section above. The route gained `knowledge_review.py` and one defaulted input plus one rendered section in `curator_checklist.py`; the section is **report-only** and the arithmetic is unchanged, which the body now states where the module's own comparison sentence lives rather than leaving it to a reader to infer. The reference rows were re-derived from the current files: `_append_drift` is `:319-350`, `_render` `:204-266`, `write_curator_checklist` `:100-180`, `_tracked_onboarding_paths` `:183-189`, and the controller rows moved to `:317-337`. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "def _attach_final_full_catalog(" repointed to mcp/src/agents_remember/application/memory_quality/controller.py:583-583. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: added the section above and recorded this route's share of the leaf — the new `integrity/governing_overview_resolution.py` check, its two-base resolution rule, its observation boundary, the wiring that carries its findings into the gated curator repair set, and the `D32` condition on the closeout-admission consumer. Verification metadata advanced to this leaf's frozen code base.
- 2026-09-17T11:20+02:00 — 260915-CAPS-L14 curator: added **The Shared Exclusion Register, And The Ruled Caps** as a current-intent section, because this leaf makes the register a contract on this route rather than a detail. Records the three sources feeding one register and where each lives, the `matches_any` semantics shared with the storage resolver and the drift check, the register's **deliberate and pinned divergence from Git** on a negated file under an excluded directory, the developer's 2026-08-20 cap numbers with the skip-and-report rule (never a silent omission, never a whole-tree refusal), the refusal-by-name discipline for a malformed `onboarding.citationIndex`, and the closeout gate's own typed refusal through `_admitted_source_index`. Corrects the **stale `schema-9` claim** in *Exact Git Candidate Source-Index Composition* to the v10 manifest that now carries the register and states that a v9 manifest is refused and rebuilt, and adds the one-authority-per-root parity between the two acquisition routes. Repointed the *L34 Preparation Ownership* link to the card's real home after the adapter's second move (`806649b9`) to the application rank. Records that the register, the caps and the settings key are **mode-independent**. Verification metadata is left at this leaf's synced base `0346da9c`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code commit.
- 2026-09-17T08:15:00+00:00 — 260915-KS-L9 curator (memory-quality closure): migrated this route's reference tables from the superseded `| Finding | Citations | Source Path |` shape — unbackticked `L..` ranges beside markdown-library links — to the canonical `| Finding | Anchor | Source |` shape, replacing every range-and-link pair with a real anchor naming the construct the claim is about and a `path:start-end` source that holds it. No claim wording changed; the underlying assertions were re-read against the code worktree and still hold. Recorded here because a reference-table migration is a body update and needs its history entry.
- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Documented cache-independent candidate pair identity and citation content snapshots. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T09:05+00:00 — 260831-LOCR-L34: recorded the preview/apply parity invariant on this route
  as both an invariant bullet and a section, naming the five fixed instances, the two
  reported-not-fixed ones (`worktree_start`'s non-separable reservation CAS; the memory-carryover
  plan/apply pair) and the `worktree_abandon`/`worktree_cleanup` verdict/state-string adjacent shape,
  with the observation that every instance was found by exercising an operation rather than by reading
  it. Recorded why this route carries it: its own `citation_fix` / citation-transaction /
  onboarding-refresh previews are the surfaces a planned bulk mechanical migration will touch next.
  The full inventory remains owned by the `worktrees/overview.md` route. Content change, not a range
  repoint; verification metadata remains closeout-owned and no acceptance claim is made.
- 2026-09-13T02:05+02:00 — 260831-LOCR-L33 route curation (delta after publish): the projected-range
  review item is now **enforced** (`severity="error" if bullets else "warning"`) rather than
  report-only, so a mechanically projected range blocks until it is disposed of; recorded the
  rationale (unverified evidence must force a disposition), the cost (every projected range blocks),
  that the ordinary evidence-change item keeps its `warning`, that only `code == INVALID` is ever
  demoted to pre-existing debt, and that with no git view every finding stays enforced. Also recorded
  that the migration pass's continuity branches are unreachable from its own entry point by
  construction. **Supersedes the severity "still warning / undecided policy call" statement in the
  entry below.** Source-evidence rows updated.
- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 route curation: recorded the continuity-based relocation
  rule (no live cited file, a unique tree-wide sighting, and a proved same-kind origin at the
  document's verification stamp), that the fixer and the migration pass consult one authority
  (`Walk.continuity` / `Pass.continuity` behind `repair.continuity_for`), the three new refusal codes,
  why the first design failed open on a *deleted* cited file, and the corrected review surface for a
  mechanically projected range (the support question instead of a currency assertion, severity still
  `warning` as an undecided policy call). Source-evidence rows added. Route ownership and publication
  semantics are otherwise unchanged.
- 2026-09-11T10:26:37+02:00 — De-entanglement cut cleanup at code commit `2fa5e81f`: moved the `prepared_certification.py` sidecar out to `worktrees/integration/closeout/` (commit `deb032fb`) and moved the `future_code_candidate.py`, `memory_candidate_pair.py` and `memory_census_scope.py` sidecars in from the closeout route (commits `0b63d6fc`, `be517eec`), repairing the dead `prepared_certification.py.md` link and recording the new candidate-root ownership. This records source documentation only; it makes no acceptance or certification claim.
- 2026-09-10T04:35+02:00 — CCR-L42 final citation curation: re-anchored the readiness projection
  row to the current `_attach_final_full_catalog` declaration; certification ownership and route
  semantics remain unchanged.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "def _attach_final_full_catalog(" repointed to mcp/src/agents_remember/application/memory_quality/controller.py:503-503. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T14:39:58+00:00: Generated citation repair: "def _attach_final_full_catalog(" repointed to mcp/src/agents_remember/application/memory_quality/controller.py:499-499. No content impact: mechanical anchor-range projection bound to citation source snapshot 5911742cfcc7a53db92b36b80bac02ee49a67204b190c0311a81bcc2e388ad59; claim bytes unchanged; generated by ccr-r10@v1.
### 2026-09-06T17:13:06+00:00 — L34 implementation memory
- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation: Documented the accepted-edit transaction route, exact observed-conflict boundary, CRLF, dry-run counts and nullable scoped recheck at source-reviewed private C b34f4a59; retained all separate Gate-5 readiness/execution limits.
- 2026-09-06T00:23:26+00:00 — L30 recovery: Added the exact Git-candidate index and R06/R07 composition boundary at 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; retained the unresolved production-caller and deterministic-repair limits.
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
Recorded the current private preparation/publication ownership from source. Existing verification identity is retained; this entry does not claim tests, certification or acceptance.
