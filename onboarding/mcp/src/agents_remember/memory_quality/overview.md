# mcp/src/agents_remember/memory_quality/ — Memory Quality Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| lastUpdated | 2026-09-19T23:02+02:00 |
| lastVerifiedCommitHash | `1bcf73e772b640fea56c2788fe9a52d98099bd41` |
| lastVerifiedCommitDate | 2026-09-20T05:00:13+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l16` uncommitted staged source; base `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| reviewedWorkingCandidate | `ar/260913-lca-l9` uncommitted source; base `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
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

`worktrees/modules/memory_candidate_pair.py` — moved out of this route by commit `806649b9` — binds repository/worktree identity, branches, bases, onboarding and contract facts without requiring a cached ledger file or hashing its path into authority. Citation provenance snapshots read substantive memory content while excluding only root `memory.md`; actual source/candidate drift remains detectable.

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
| The MCP application entry point builds drift context, including temporary leaf-base provenance, and calls the package runner. | `run_memory_quality_request`; `_execute_memory_quality` | mcp/src/agents_remember/application/memory_quality/controller.py:249-255; mcp/src/agents_remember/application/memory_quality/controller.py:383-435 |
| Tool metadata and server registration expose `memory_quality_check` to agents. | `memory_quality_check_payload`, `create_server` | mcp/src/agents_remember/mcp/server.py:58-70; mcp/src/agents_remember/mcp/tools/memory.py:58-65 |
| The update-history fixer is a dedicated mutating module rather than a `memory_quality_check` option. | `memory_quality_check` | mcp/src/agents_remember/mcp/registration/memory.py:57-75 |
| The missing-onboarding checker catches newly added worktree files before code commit. | `check_missing_onboarding` | mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py:46-73 |
| The shared drift model declares the vocabulary used by drift-check wire responses. | "class DriftSummary(StrictResponseModel):" | mcp/src/agents_remember/models/drift.py:13-23; mcp/src/agents_remember/models/memory.py:13-27 |
| The context-packet application entry point that returns `DriftSummaryPacket` from its drift seam. | `build_context_packet` | mcp/src/agents_remember/application/context_packet.py:59-102 |
| The curator checklist renderer owns deterministic grouping, closeout-provenance separation, and atomic publication. | `write_curator_checklist` | mcp/src/agents_remember/memory_quality/curator_checklist.py:79-126 |

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
| The migration pass consults the same continuity authority before a cross-file relocation, although its continuity branches are unreachable from that entry point by construction. | `Pass`; `place` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:63-87; mcp/src/agents_remember/memory_quality/style/citations/migration.py:415-461 |
| A mechanically projected range is ENFORCED at `error` severity with the support question instead of asserting currency; the ordinary evidence-change item stays `warning`. | `_projected_review_message`; `surfaced_finding` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:315-339; mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:341-386 |
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
| The application surface projects readiness with no affected-closure plan. | "def _attach_final_full_catalog(" | mcp/src/agents_remember/application/memory_quality/controller.py:565-565; mcp/src/agents_remember/application/memory_quality/controller.py:671-707 |
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
| The bounded non-Git matcher and its pinned divergence from Git. | `FallbackIgnoreMatcher` | mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py:253-297 |
| A caller exclude that cannot mean anything is refused by name. | `validate_caller_excludes` | mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py:171-193 |
| The ruled numbers, the skip vocabulary and the status vocabulary. | `MAX_SOURCE_BYTES`; `MAX_SOURCE_FILE_BYTES`; `MAX_SOURCE_HARD_STOP_BYTES`; `SKIP_REASONS`; `STATUS_CAPPED`; `STATUS_WITHIN_CAPS` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:18-43 |
| The register's three sources and recorded authority values. | `EXCLUSION_SOURCES`; `GITIGNORE_AUTHORITIES` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:45-61 |
| The closeout gate refuses by name rather than letting a bare error out. | `_admitted_source_index` | mcp/src/agents_remember/application/prepared_certification.py:415-437 |
| The caller-exclude surface on the registered tool and the CLI. | `citation_fix` | mcp/src/agents_remember/mcp/registration/memory.py:100-124 |
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
| The index opens either the explicit candidate selection or the ordinary filesystem policy. | `open_repository_index` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:323-390 |
| R06 checks candidate selection and exact indexed membership. | `observe_source_index`; `_require_index_matches_candidate` | mcp/src/agents_remember/memory_quality/incremental_scope/owners.py:100-152; mcp/src/agents_remember/memory_quality/incremental_scope/owners.py:347-397 |
| R07 validates and forwards the unit candidate tree to its selected-document checker. | `RangeResolutionAffectedExecutor` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_execution.py:67-130 |

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

## Update History
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
