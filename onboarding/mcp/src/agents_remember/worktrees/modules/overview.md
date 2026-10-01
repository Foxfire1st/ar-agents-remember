# mcp/src/agents_remember/worktrees/modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/worktrees/modules` |

## Governing Overview

[worktrees overview](../overview.md)

## 260928-MIK-L37 The Memory Routes Ask The Cutover Lock, And The Onboarding Gate Reads Every History File

`260928-MIK-L37` (MIK-R37). The cutover build was installed on 2026-10-01 (MIK-R37 rule 4), and this leaf's closeout converts the master's
memory line. What earlier sections of this overview call "inert until the cutover" is live from this leaf on. Four modules of this route changed:

- **[`closeout_external.py`](closeout_external.py.md).** `external_closeout_commits` asks
  `leaf_cutover_refusal(contract, "the closeout")` before any stamping or commit of unconverted memory.
- **[`record_landing.py`](record_landing.py.md).** On unconverted memory the gate helper returns the cutover lock's
  answer, with or without a named memory commit.
- **[`integrate.py`](integrate.py.md).** `_knowledge_gate_block` now runs for a leaf's integration too:
  `_leaf_landing_lock` refuses only when neither the landed memory commit nor the line it lands on holds the layout
  marker and the repository holds converted memory, so the converting leaf's own landing is never locked. A series
  contract still goes to the landing gate.
- **[`onboarding_trace.py`](onboarding_trace.py.md).** `_history_rows` reads every history file of the leaf (a
  reopened leaf's closed file and its later attempts) as one history.

In a repository that holds no converted memory, unconverted memory passes all three routes exactly as before.

- The closeout's memory side asks the lock before any stamping or commit. [51]
- A leaf's integration is refused only by the lock. [52]
- Record landing on unconverted memory returns the lock's answer. [53]
- The onboarding gate reads all of a leaf's history files. [54]


## 260928-MIK-L09 Closeout, Record Landing And Integration Ask The Mandatory Invariant Gate

Three modules of this route are MIK-R09 routes (leaf 260928-MIK-L09, D5). Each asks the gate through
`worktrees/knowledge_gate.py` and the bound `KnowledgeGatePort`, only on converted memory:

- **`closeout_external.py` (rule 3, the closeout memory commit).** On a converted leaf, `external_closeout_commits`
  closes the leaf's history file (`close_owner_history`, MIK-R07 rule 7), and `_commit_memory_content(closing=…)`
  validates the exact tree it is about to commit (`_refuse_invalid_memory_commit`: `memory_commit_refusal` as a leaf
  publication, against the parent line's memory tip, the carried L22 and L27 obligations) before `begin_git_mutation`;
  any refusal or failure before the commit restores the file (review R1 F2). The closing is inside the one memory
  commit, which keeps its `Code-Commit` trailer.
- **`record_landing.py` (rule 3, commits no memory).** It probes the memory line and the task's memory base first (F7),
  then checks the landed memory commit: the validator against the task's `memory_base_commit` and, for a leaf, the
  history file `closed` in it; a converted line must name its memory commit; an unconverted line's commit is only
  probed and records exactly as before.
- **`integrate.py` (rule 4, master and checkpoint landing).** `_knowledge_gate_block` runs in preview and apply alike
  after the handover gates: the validator on the master's memory commit and the net-staleness check (every entry at a
  path the master's net code diff changed must be `current` at its code commit; `unverifiable` and a failed Git read
  refuse too, F4), blocking with `knowledge-gate-refused` and naming the maintenance-leaf remedy.

Unconverted memory is not gated at any of them (the unconverted test; `unconverted.sh`: the real memory commit tree
`20ccf39a…`, its message and trailer, and the record-landing payload are identical to base). Refusal tests enter
through each public route entry (`test_knowledge_gate_routes.py`). **Inert until the cutover**, which is leaf
260928-MIK-L37: since then the cutover lock refuses unconverted memory at each of them once the repository holds
converted memory (the L37 section above).

- The closeout closes the history file and validates its exact tree, restoring on refusal. [1]
- Record landing probes first, then asks the gate over the landed commit. [2]
- Master and checkpoint landing wait for valid, current knowledge. [3]

## 260928-MIK-L38 Finalization Completes The Row Of The Master That Lists The Leaf

`modules/finalize.py` resolves a leaf's immediate parent by the task-document master sync's rule (MIK-R38, developer
direction D32). A leaf that names its master is unchanged (`_named_parent`). A leaf that names none used to finalize
as standalone, leaving its row on the listing master at `inProgress`; it now resolves the folder's `task.json`
through `tasks/master_sync.folder_master_json_path` (`_folder_parent`), holds it to every named-master check, and
completes its row under the master demotion rule. Without a folder master, or without a row for the leaf, it stays
standalone as before. Both masters and the leaf must also be in place: a document the store would write to another
file is refused before cleanup and before any write (`tasks/leaf_doc.require_task_document_in_place`; review R1
finding 1, rulings 2026-09-30T13:11:32 and 13:35:32). Reopen (`../reopen.py`) resolves by the same helper (ruling
12:33:07 Q2). Every refusal is `task-document-resolution-blocked` with a named reason; the preflight, the source
snapshots and the projection effects are unchanged.

- Parent resolution dispatches on the leaf's `master`: named, folder, or standalone. [4]
- The folder master through the master sync's helper, with the named-master checks. [5]
- The placement guard on the leaf and on every master read. [6]

## 260928-MIK-L10 The Onboarding Gate's Unnecessary-Row Findings Name Their Subject

`modules/onboarding_trace.py`'s `OnboardingTraceResult.report_only_findings` now carries each unnecessary row's
`subject` (one additive field; the message is unchanged). MIK-R10 needs it: an uncovered file's unexplained change is
answered by the file's onboarding trace, which for a card-less path is the leaf's `onboarding:<path>` row, and this
gate raises no card item there, so it would report that row as unnecessary. The memory-quality controller
(`application/memory_quality/controller._needed_rows_dropped`) drops exactly those findings by subject and sets the
response's `unnecessaryRowCount` to what it keeps (ruling 2026-09-30T01:56:39 Q3). The gate's items, repair findings
and decision are unchanged, and MIK-R10 reads its items without changing them. Unconverted leaves still run today's
gate (`onboarding.py`).

- Each unnecessary-row finding names its subject. [7]

## 260928-MIK-L25 Finalization Carries The Review-Artifact Archive Hook

`modules/finalize.py` gained `_with_review_artifact_cleanup` (MIK-R25 rule 5, D17). Right after
`archive_completed_root_task`, `_finalized_result` passes the archive result through it: for an `archived` (or, on
a dry run, `would-archive`) task it calls the composition-bound `ReviewArtifactCleanupPort` (`../services.py`) with
the task root as it now is, `task_name` = the contract's `task_root.name` (the only name of the review-ref
namespace, ruling 2026-09-30T02:32:42 (a)), the contract's two repositories and `dry_run`, and carries the report as
`taskArchive.reviewArtifacts`. An unbound port reports `not-bound`; an exception becomes `{state: "failed", detail}`,
because the task has already moved (review F2). The hook (`application/review_artifact_cleanup.py`) deletes the
task's review refs, its own legacy retained-code pins and its legacy dataset copies, confined to the task folder.

- The archive result gains the hook's report; unbound or failed is reported, never raised. [8]

## 260928-MIK-L30 The Onboarding Refresh Gate On History Files Joins This Route

This route gained **one module**, `modules/onboarding_trace.py` (carded), and `modules/onboarding.py` gained
its entry points. Together they are MIK-R30@v1's gate for converted memory trees, where Update History and
`lastVerifiedCommit*` no longer exist:

- **The rule (`onboarding_trace.py`).** Each changed sidecar-stored source with a card raises an
  `onboarding:<path>` item, and each nearest governing route an `onboarding:<route>/overview` item
  (`onboarding:overview` at the root). An item is satisfied by a counted change of its Markdown or sidecar
  (not by an anchor's `blob`, line numbers or `content` alone) or by the leaf's `no_impact` history row. An
  unreadable history file, an incomplete side or an unreadable K_B sidecar is a named problem; an unreadable
  K_C sidecar keeps its item open. `onboarding_item_open` applies the same rule to a stored worklist item.
- **The entry points (`onboarding.py`).** `onboarding_trace_gate_for_context` (the curator's run: findings,
  never raises) and `validate_onboarding_traces_for_context` (closeout: refuses naming every missing trace),
  both after today's missing-onboarding refusal, now shared as `_require_onboarded_sources`. On a converted
  tree the two metadata refreshers stamp nothing (`converted_onboarding`).
- **Architect rulings (2026-09-29):** 18:49:50 (only a counted change or a row satisfies a trace on converted
  trees; the root subject; deletion of today's gate left to MIK-R37); 19:23:45 (mixed formats are an
  incomplete side; an unreadable sidecar never satisfies a trace); 19:53:54 (the stored-item predicate agrees
  with the live gate; unreadable K_B is an incomplete input, unreadable K_C keeps the item open, a readable
  repair counts).
- **Unconverted trees keep today's gate**, byte-identical: the dispatch lives in the application layer and
  returns to `validate_memory_refresh_attestations` and the two plan validators whenever neither side is
  converted, which is every production leaf before MIK-R37.

- The route's new gate over two memory sides. [9]
- The stored item's open state, as the live gate decides it. [10]
- The two entry points and the shared missing-onboarding refusal. [11]

## 260921-ICR-L32 The Path-Enumeration Family Reads NUL-Delimited Git Output

`worktrees/modules/git.py`'s four path-enumerating functions — `changed_files_with_counts`,
`changed_worktree_paths`, `_diff_paths` and `committed_changed_paths` — asked Git for line-delimited output
and rewrote `\` to `/`, so a filename holding a tab, a newline or a backslash became an address no file
holds. Measured at the leaf's base: five real changes in, four rows out, two addresses resolving to nothing
and one real untracked change silently absent. `260921-ICR-L32` puts `-z` on all four, pairs
`--name-status -z` and `--numstat -z` fields positionally including the two-field rename form, drops the
escape rewrite entirely, and refuses rather than silently omitting — five in, five out, every name verbatim,
with `committed_changed_paths` keeping its deliberate `is_file` filter so a deleted path is not reported as a
change. This route's closeout worklists are exactly what the family feeds, so the defect was a
closeout-input defect as much as a change-set one; `ACCEPTANCE.md` A24 is the row that measures it.

## 260921-ICR-L11 The Route Gains A Git-Object Retention Owner, And Custody Becomes A Measurement Over Named History

This route gained **one module**, `modules/code_object_retention.py`, and the leaf it belongs to
(`260921-ICR-L11`, primary requirement ICR-R11@v1) needed it because a captured candidate tree is in
**no commit**: it is written through a private index, so nothing points at it, `git gc` may delete it at
any moment, and the only thing between "the comparison can be reopened" and "the tree is gone" is an
object reference that survives reclamation.

Three facts belong at this route's altitude, because each one is a decision rather than mechanics:

- **One commit and one ref keep both bound objects alive.** The retention commit's tree *is* the captured
  tree and its parent *is* the recorded base commit, so the candidate tree and the baseline it is
  compared against stay in one ancestry — reclamation cannot keep one and drop the other. The ref lives
  under `refs/ar/retained-code/`, deliberately outside `refs/heads` and `refs/remotes`, which is what
  makes `worktree remove`, `branch -D`, `worktree prune` and `gc --prune=now` leave it exactly where it
  is, and what lets a reader find every pin with one `git for-each-ref` over that prefix.
- **The retention commit's id is a function of the two objects it keeps.** Author, committer and both
  timestamps are supplied explicitly and dated by the **base commit**, so a pin re-created after an
  explicit release is the identical object. That is what makes an exact re-freeze converge instead of
  producing two generations claiming one index for a comparison nobody changed.
- **Custody is measured over the history the caller names, and the leaf's own work branch is not one of
  the names.** An empty name set means *nothing durable holds the tree*, so the pin stays; the
  measurement never walks ancestry, and a tree surviving only deeper in a named branch's past is still
  reported `retained`, because keeping a redundant pin is the safe direction to be wrong in while
  releasing the only reference is not. A ref that already names a different pin is refused rather than
  re-pointed.

The third observation belongs to the reader, not the record: `code_object_observation` answers `absent`
when the object does not resolve at all, and `absent` is a **separate type** from the two custody values
— an object that is gone is not held by anything, so reporting it as `retained` would claim a pin is
holding bytes that are no longer there. That is exactly the state a released-and-reclaimed history is in.

- One commit, one ref, and the recorded base as the commit's parent. [12]
- **The commit whose id is a function of the retained objects, and the identity that makes it so.** [13]
- **Custody over named history only, and the empty set as a statement.** [14]
- **The third observation, which a record never stores.** [15]
- The explicit release: a moved ref refused, an absent ref converged, and the custody measured before deletion. [16]
- The typed failure every ref outcome raises. [17]
- **The create-side consumer, which measures custody against the contract's names and pins only when they do not hold the tree.** [18]
- **The cases that measure the pin against a real repository, including the control object that proves `git gc --prune=now` really reclaimed.** [19]

**One boundary this route inherits and does not settle.** Whether a *landed* integration or closeout
operation objects to the `refs/ar/retained-code/` namespace was **not measured** by this leaf, which
cannot run those transactions; the pin was measured to survive `worktree remove`/`prune`, `branch -D`,
gc-packing and `git fsck`, and the ref namespace question is recorded as open rather than assumed safe.

## IAS Frozen Public Lifecycle Composition

Start, attach, dispatch, and explicit sync share one atomic-series selecting transaction. The
activation record it writes is keyed **per series contract** (`contract_fingerprint` over the
canonical resolved contract path), so a new selection transitions only that contract's own record:
`reconciling`, reconcile its pinned protected code/memory source pair, then `active` only after
current-base proof. Cross-master exclusivity between atomic masters that share one sprint's code and
memory source branches is gone — every refusal the admission projection describes is corrective
action on the addressed contract, a foreign master is never named as a blocker, and the only
surviving activation waiting reason is `atomic-series-reconciling`. The graph-less default is not a
serialization authority either: `atomic-sequential` describes the sprint's shape — every commanded
master executes atomically — and serializes nothing, because a graph-less sprint declares no
dependencies. Real wave dependencies still gate through the sprint execution graph's own
`predecessor-incomplete:` reasons. `worktree_sync` becomes a
resumable contract-addressed operation: genuine conflicts remain available for agent resolution,
`continue` validates the staged result, and `cancel` restores only pinned operation-owned heads.

Cleanup and abandon remain terminal lifecycle operations, not scheduling mutations. After their
terminal publication and outside lifecycle/store locks, they may vacate only the exact selected
terminal contract before destructive contract cleanup. The terminal release addresses exactly the
contract it was given and never clears another contract's record. Missing or malformed
activation/journal authority is not replaced by a legacy or queue-derived fallback reader.

Master-series bootstrap also treats the transient-journal to durable-contract handoff as one
observation boundary. On apply, `startup/start_contract.py` evaluates
`_bootstrap_preflight_contract` while holding the same per-master `exclusive_access` mutex that
serializes bootstrap publication. A concurrent loser therefore observes either the live winner
journal or its published contract; it cannot read before contract publication, wait behind the
winner, then misclassify the now-retired journal as an orphaned branch. Dry-run remains unlocked
and write-free. This is synchronization around the canonical journal/contract authorities, not a
retry, fallback reader, compatibility path, or second lock namespace.

## Evidence

### CCR-R25 Public Start And Status Evidence

`start.py` adds the read-only series activation fact to status results while leaving selection and
source synchronization in the focused activation transaction. `startup/start_contract.py` now
turns persisted master task/repository/branch edge mismatches into typed expected/observed
admission evidence before protected-branch surface calculation, exposing the exact status address
for recovery. `startup/master_series_admission.py` owns the edge comparison and refusal payload
projection, while `worktrees/activation/atomic_series_admission.py` remains the shared pure
diagnostic boundary. Neither path repairs contracts or selector bytes, and logical selection state
is not presented as proof of a live process.

CQ04 also preserves the concrete parser reason when the authoritative master-contract reread finds
an unreadable contract after upstream refresh; the typed refusal remains read-only and is returned
before protected-surface calculation. The same refusal projector bounds both top-level and nested
observed parser detail when malformed input expands the reason beyond the public response limit.
CQ01 bounds the activation diagnostic detail used by status and admission, and CQ02 records the
registered consumer ownership in the evidence catalog.

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The package is imported through the public worktree manager facade. [20]
- Focused worktree tests exercise the facade and operation payloads. [21]
- Finalizer tests cover a named master's row, its rollback and the misplaced-master refusal, and (MIK-R38) the folder master's row, the dry run, the standalone cases and the refusals before any write. [22]
- Reclamation belongs to finalization (260831-LOCR-L31): it runs the terminal cleanup procedure and shapes a real successful reclamation through the pure report shaper, deliberately not on a dry run or a nonzero return code. [23]
- Integration lands the refs through the shared writer and stops, promising reclamation only at the task edge. [24]
- Closeout onboarding refresh uses resolved storage authority for deterministic route-index preview and apply. [25]
- The lifecycle state carries the optional worktree phase the panels render. [26]
- Master-series startup compares task, repository/memory, and branch edges before protected-branch admission and carries bounded expected/observed refusal facts. [27]
- `GateStore.claim_approval` — the compare-and-swap this route spends approvals through, and `CONSUMED_APPROVAL_GATE_KINDS`, which stops the resulting `applied` snapshot from being reclaimed. [28]

Current working-candidate evidence for this route:

- External closeout chooses substantive memory output and refreshes the cache afterwards. [29]
- Final memory staging removes and excludes the cache. [30]
- Carryover completion is actual memory ancestry. [31]

### Certificate Records And Executor Evidence

The strict quality gate freezes the exact R11/R22/R21 lane before Dagger. `quality/certification_run.py` reopens the verified decoder artifact and delegates actual terminal catalogs to `quality/certification_records.py`, including available red/interrupted results. The gate records returned terminals and invokes the selected owner callback before propagating recording or process failure. The adapter requires the exact candidate, profile digest, full plan and selection, then reopens nested evidence and artifacts before publishing canonical results/certificates. A decoder omission or an uncertified terminal does not become green evidence.

`quality/certification_evidence.py` reads the bounded gate-record journal and cross-binds its certificate/result objects to complete strict manifest snapshots. Lifecycle selection separately retains explicit original references in the operation journal. `quality/certification_reuse.py` validates zero-start rows against those supplied original objects and physical publication bytes. `clean_executor.py` combines the existing gate-record pins with the caller’s verified selected-graph generations before pruning; confined report reads remain in `report_publication_paths.py`. No historical scan selects authority.

The Dagger interpreter captures executed pass, fail and skipped handles while retaining complete same-gate outcomes and zero-start later gates. `rail_emission.py` distinguishes observed empty output from unavailable streams, keeps exact bounded byte captures and producer file handles apart from the execution handle, and refuses a green rail when required observed evidence is unavailable. `rail_bindings.py` uses stable report-relative locators; dashboard coverage keeps its Vitest source and receives a separate stable publication name.

`profile_results.QualityProgress` carries retained bytes/file handles until `profile_publication.prepare_profile_reports` builds the report branch. Captures are written through a base64 transport that preserves arbitrary byte tails. Required publications are checked on that actual output branch before the final decoder payload is serialized/exported. The finite profile declares all capture paths as octet streams; reference metadata is not substituted for bytes.

The three previously missing Gate-4 producers are connected: Playwright writes the configured browser JSON report, provider pytest writes its phase report, and the teardown adapter validates both successful `L5-C10` checkpoints and summary/report identities before writing the proof. The separate dashboard suite-result writer remains its existing Vitest companion. These `.dagger/` contracts belong in this governing overview because `.dagger/` is excluded from file-card path rules.

`quality/dagger_authority.py` now uses neutral `kernel/file_lock.py` exclusion for the host registry. Checkout durable stores still enforce their coordination guard before entering the same lock implementation. No process-role declaration or second lock namespace is introduced.

Selected closeout admission, original-reference readback and code-suffix execution are composed through the lifecycle journal. Current Gate-5 observation is an explicit continuation-port obligation; the default production continuation remains unbound. Finalization and telemetry obligations are not established by the existence of the quality helpers or separate diagnostic/final-Codex controllers.

- Returned terminals are recorded and selected before recording/process refusal propagation. [32]
- Recording requires exact admission and physically verified evidence. [33]
- Gate-record publication bindings retain exact semantic authority and physical generation. [34]
- All runnable sibling rails retain observed terminal facts. [35]
- Executed outcomes distinguish unavailable streams and retain exact bytes/files. [36]
- Bound artifact metadata names actual observed producer bytes. [37]
- The report branch persists retained bytes and exports the authoritative payload. [38]
- Required files are checked on the actual publication branch. [39]
- Execution progress retains per-step outcomes, the gate catalog, publication bytes/file handles and environment reconstruction observations. [40]

## Purpose

Terminal cleanup and abandonment exclude the computed root ledger cache from memory dirtiness and discard only that cache before ordinary Git worktree removal. Actual code/memory edits and branch ancestry remain protected. Abandon preview passes its preview state to result validation. The existing Git and public-terminal tests cover these boundaries.

The `worktrees/modules` package contains the extracted implementation modules
behind the `git_worktree_manager.py` facade. It separates Git adapters, lifecycle
status guidance, start preparation, onboarding refresh, strict code-quality gating, closeout, integration,
cleanup, cleanup report shaping, lifecycle finalization, abandon, the stop-only master pause,
provider teardown, start-contract leaf-ref normalization, the typed cross-layer argument DTO, and CLI
argument wiring while preserving the public facade import path. Reopen is deliberately NOT here:
`task_reopen` enters through the task-doc application route and executes `worktrees/reopen.py`; this route's start path
merely honors its `cleanup: reopened` tombstone (recreate fresh, restamp the leaf doc's lifecycle).
The committed L2 layout groups the start-contract, master-series admission, provider-preflight, leaf-ref, and result helpers
under `startup/`; `start.py` remains the coordinating mutation entrypoint.

## Current Profile, Publication And Lifecycle Ownership

`quality/gate.py` admits one explicitly configured repository certification profile through `QualityGateTarget`; wrapper presence is no longer authority. The real R11/R22/R21 bridge freezes that profile plus the memory-service rail catalog before Dagger. Leaf acceptance is targeted at closeout; series closeout requires clean landed code and master integration owns the full gate. Required unresolved test ownership refuses before Gate 2 rather than expanding to a full population. The Gate-5 memory preflight starts only after the code gate is green or not required.

`quality/clean_executor.py` publishes immutable schema-3.1 report generations and an atomic current pointer. Fresh and recovery callers retain the exact `publishedResultPath`; the strict reader verifies the declared inventory and candidate identity. Selected certificate records bind complete original manifest snapshots and physically reopened rail bytes. The lifecycle-selected path supplies current-owner callbacks for terminal selection, protected generations and last-moment start authorization. Its admission and code-suffix composition use the existing operation journal; the default production memory/finalization continuation remains unbound.

Older EFA/L23 paragraphs below preserve the migration account and its original flat module names. Their wrapper discovery, local interpreter selection, citation-first ordering and schema-1/2 descriptions are historical; current paths are `quality/gate.py`, `quality/clean_executor.py`, `quality/closeout_memory.py`, and `quality/published_manifest.py`. Provider setup/teardown moved to `application/provider_runtime.py`, and `reopen.py` to `worktrees/`.

## Hot Path Summary

`closeout_external.py` writes one attributed memory-content commit or reuses the actual unchanged head. `git.py` excludes root `memory.md` before staging and at the final memory commit boundary; cache-only changes cannot request a commit. `guidance.py` proves carryover from memory commit ancestry, and `integrate.py` publishes only the admitted code/memory pair.

## Detailed Route Context

Public worktree modules consume closed configured-contract admission and preserve their existing mutation locks/rereads. Cleanup and abandon remain fail closed before destructive seams until external terminal archive proof exists.

Quality execution, lifecycle gating, closeout memory checks, and immutable published-manifest reads
now live under `modules/quality/`. The package is a behavior-preserving ownership/size split: the
clean executor remains the sole Dagger report publisher, the gate remains the lifecycle consumer,
closeout memory remains phase composition, and the strict manifest reader admits no fallback or
permissive compatibility path.

`onboarding_acceptance.py` is the single pure application boundary for candidate-bound
no-content/no-route decisions. It can reclassify only matching unchanged `stale` bodies as
accepted; `untraced` authored content remains closed. Closeout preview, reversible admission, and
post-commit external-memory refresh therefore consume the same validated coherence decision set.

L23 makes Dagger the sole acceptance executor. `clean_quality_executor.py` materializes the exact
reviewed candidate and required ancestry into the pinned graph, starts a fresh attempt, bounds live
output, and atomically replaces the enclosure's current reports; there is no local compatibility
runner. `code_quality_gate.py` plans targeted or full Dagger authority with an explicit diff base.
`closeout_staged_quality.py` owns the linked/conflict refusals, accepted-tree rechecks, complete
staging, reviewed hook, and targeted gate. `closeout.py` and `integrate.py` preserve approval and
merge ordering while rechecking lineage after long quality work; the closeout lineage boundary now
self-heals a settleable stale break through the sync transaction, and integration remains
failure-atomic before source refs move. `git.py` owns exact candidate-tree and repository-identity helpers.
`startup/start_result.py` separates result projection from start coordination, and the external
`worktrees/queue/closeout_recovery.py` reconciles post-claim code and memory-content commits without
replaying completed irreversible steps.

- `git.py` owns this route's Git vocabulary — the typed helpers and small repository
  state checks every operation module speaks — but **since 260731-EFA-L3 it no longer
  owns a Git runner**. It imports the one owner (`from agents_remember.kernel.git_command
  import run_git`, line 7), and its own `require_git` is now raise-on-nonzero over
  it. Raw results preserve the runner's surrogateescape contract, while only the
  raised failure diagnostic passes through `_transport_safe_git_diagnostic` so
  invalid Git bytes become literal escapes before MCP JSON serialization. See the
  260731-EFA-L3 section below for why the runner/facade distinction is a correctness
  property and not bookkeeping. Its helpers include
  `committed_changed_paths` (issue #83: the unverified committed
  range — tree-diff `base..HEAD` ∩ `verified..HEAD`) and the
  `commit_text_or_none` baseline reader behind the closeout body gates.
  The certified closeout path also uses `run_pre_commit_hook_if_configured` followed by
  `commit_verified_staged`: the former runs the fast hook before the strict wrapper, while the
  latter commits exactly that verified index with hooks bypassed and never restages later edits.
  **Operations-integration L3** adds `changed_files_with_counts(repo, base, head=None)`
  (+ `_rename_aware_path`) — the change-set primitive behind the serving change-set API
  (`serving/changeset.py`): per-file `{path, insertions, deletions, status}` via
  `git diff --numstat --name-status --find-renames`, KEEPING deletions and reporting
  counts (binary → `None`, untracked → `A`, rename → post-rename path), unlike the
  name-only `changed_*_paths`.
- `code_quality_gate.py` is the fail-closed worktree closeout adapter for the
  project-owned quality wrapper. It previews the exact command, resolves
  interpreters in worktree, shared-clone, then active-Python order, puts the
  candidate worktree's `mcp/src` first on `PYTHONPATH`, and rejects a missing
  wrapper/interpreter or any nonzero result. This preserves linked worktree
  operation without weakening the gate or accidentally testing a sibling checkout.
  Captured output is decoded as UTF-8 with replacement so malformed diagnostics cannot suppress
  the completed report. On non-Windows hosts only ephemeral quality scratch is normalized to the
  short process-safe `/tmp` root; the durable latest transcript remains the enclosure-owned,
  atomically replaced `reports/test-results.md`.

  **Since 260731-EFA-L1 the gate is not scoped to one repository.** The deciders take the code
  worktree `Path` and gate on whether that checkout carries
  `mcp/test_support/agents_remember_test_support/code_quality/check.py`; the old `repo_name == "agents-remember"`
  condition made the gate a no-op for every consuming repository — the product's actual audience —
  while the product documented it as mandatory. The preview now reports one of three statuses:
  `enforced`, `no-code-commit`, or `wrapper-unavailable`. The last is deliberately *reported*
  rather than silent: closeout proceeds, and the payload states that the code commit was not
  quality-checked and why. Since 260731-EFA-L4 the `enforced` reason (line 77) also names the
  staging step that now precedes the run, because the gate derives its scope from the index and
  therefore certifies whatever the caller staged — see the L4 section below.

  One hazard lives at this route's boundary: `closeout.py` calls these functions with an
  unannotated `contract`, so passing `contract.repo_name` where a `Path` is expected type-checks
  clean and silently disables the mandatory gate. Only
  `test_worktree_closeout_quality_gate.py::test_closeout_hands_the_gate_the_code_worktree_not_the_repository_name`
  observes the real argument; do not weaken it into a stub.
- `guidance.py` renders lifecycle phase and typed next-operation payloads, and **since
  260731-EFA-L4 it is where the phase/next-move vocabulary is declared** — `WorktreePhase`
  (line 28), `NextOperation` (line 38) and `NextTool` (line 47) are `Literal`s owned by the
  state machine that produces them, and `models/worktree.py::WorktreeSummary` imports those
  three names instead of retyping them (`models/worktree.py` lines 15-19). Before that the
  wire model held a hand-written copy, and the two sets had drifted: `carryover-pending`,
  `abandoned`, `request_carryover_decision` and `memory_carryover_apply` were all emitted by
  the functions below and all rejected by the packet. `lifecycle_guidance` now returns the
  `LifecycleGuidance` TypedDict (line 85) rather than `dict[str, object]`, and the three
  phase-group helpers return it too, so a phase string this module invents but the wire cannot
  carry is a pyright error here rather than a pydantic `ValidationError` raised inside the
  `context_packet` tool handler, which has no `except` for one. Its
  `lifecycle_guidance` checks the disposal states first: `cleanup == "completed"`
  → the `cleanup-completed` phase, and (slice 05l P1) `cleanup == "abandoned"` →
  a dedicated `abandoned` phase (`nextOperation: "done"`). Before the abandoned
  branch a torn-down worktree fell through to the `worktree-started` default, so
  the dashboard rendered it as fully active; the explicit phase lets the observer
  reducer (`_GUIDANCE_PHASE`) project the teardown for the 05k render. **Slice 09**
  removed the dirty-tree → `commit-approval-pending` branch (a visibility bug):
  `lifecycle_guidance` no longer infers a commit-approval gate from `git status`,
  so a dirty worktree falls through to its honest lifecycle-position phase
  (closeout-completed → `integration-pending`, etc.). `commit-approval-pending` is
  owned by the closeout preview (`closeout.py`) and, once the gate plane is adopted,
  by a raised `closeout-approval` `GateNode` — never the working tree; the unused
  `contract_has_worktree_changes` import was dropped. **Slice 05m**
  adds the public `carryover_done(contract) -> (done, carryoverDoneAt)`: it reads the
  actual landed memory-content commit and the official memory source ancestry to
  prove whether content was carried home, returning that commit's `%cI` as the milestone
  (external-only; internal/disabled → `(True, "")`). Cache rows do not decide cleanup. `lifecycle_guidance` now splits the
  `integration_status == "completed"` branch on it — not carried → phase
  `carryover-pending` routing the existing `memory_carryover_apply` (carryover must run
  while the parked memory branch still exists), carried → `cleanup-pending` carrying
  `carryoverDoneAt`.
  **L4 also splits the next-move builder in two.** `next_guidance` (line 142) is now typed
  `NextOperation`/`NextTool` and belongs to the phase machine; the five payloads that are a
  *gate or a block* rather than a phase — the closeout preview's `request_commit_approval` and
  the four blocked start/sync recoveries — call the sibling `recovery_guidance` (line 159)
  with its own `RecoveryOperation` (line 61) / `RecoveryTool` (line 68) vocabulary. Same keys,
  same order, byte-identical wire; the split exists so that widening the recovery set cannot
  widen `WorktreeSummary.nextOperation`, which would put "requires developer approval" and
  "blocked on a stale base" back into the set the context packet claims to report. Undo the
  split and the packet again advertises values its own state machine can never produce.
  `status_payload` and `projected_status_payload` return the `WorktreeStatusPayload` TypedDict
  (line 138) — `WorktreeStatusFacts` (line 98, the snake_case contract facts) merged with
  `LifecycleGuidance` — instead of `dict[str, object]`, and gain one optional key:
  `unknown_contract_cells`, present only when the contract file carried a cell outside its
  vocabulary that `worktree_contract._vocabulary_cell` substituted for. It is the one place a
  degraded contract read becomes visible to whoever called a worktree tool, and it says that
  the phase beside it was computed from the substituted values.
  **`NextTool."worktree_cleanup"` is deliberately retained (260831-LOCR-L31).** This module's
  `cleanup-pending` branch was its last writer here, but it is not orphaned:
  `application/worktree_status.py::_project_terminal_contract_status` sets
  `"nextTool": archive.cleanupOperation` on a terminal contract, and `cleanupOperation` is
  `TerminalCleanupOperation = Literal["worktree_cleanup", "worktree_abandon"]`. That producer also
  writes the same value into `nextAction`, and the pair is **undeclared and unchecked**: the
  `worktree_status` payload validates through `WorktreeStatusResponse`, which inherits
  `extra="allow"` from `FlexibleResponseModel` and declares none of `nextAction` / `nextTool` /
  `nextArgs`, so the values pass through verbatim with no error. `WorktreeSummary` is never on that
  path — it is built only inside `worktree_status_packet`'s helpers — so its single-value
  `nextAction` literal (`Literal["developer-decision"]`) stays honest where it lives.
  `"worktree_abandon"` has never been a `NextTool` member, so that `nextTool` is out-of-vocabulary.
  The branch is reachable (a failed contract amendment is rolled back while the locator stays
  `terminal-archived` → `terminal-archive-ready`), the emitted guidance is **correct** — retrying the
  named tool resumes — and only the typing is missing. The mechanism, the recommended fix, and the
  fact that `test_wire_vocabulary_exhaustiveness.py` no longer has test bodies to enforce
  produced == declared are recorded on `models/worktree.py.md`. Do not reconcile this by deleting
  `worktree_cleanup`.
- `landing.py` (slice 5h; hardened 5l P2) observes the successful-landing arc
  best-effort — `git ls-remote` branch tips (`origin/<feat>`, `origin/mem-main`) +
  a best-effort `gh pr list`, all timeout-bounded and `stdin=DEVNULL` (the #49
  stdio-pipe guard). Since 260731-EFA-L3 the two `ls-remote` probes get both of those
  properties from the shared runner rather than hand-rolling them —
  `run_git(repo, [...], timeout=_PROBE_TIMEOUT_SECONDS)` at `_remote_branch` (line 56)
  and `_default_branch` (line 79), keeping the deliberately short 8s probe bound
  (`_PROBE_TIMEOUT_SECONDS`, line 31) rather than inheriting a runner default. The
  `gh pr list` in `_pr_for` (line 93) is not git and still builds its own
  `subprocess.run`, but it now takes `env=git_environment()` (line 124) — `gh`
  resolves the repository *through* git, so an inherited `GIT_DIR` would have it list
  another repository's pull requests under this worktree's branch name, and `cwd=repo`
  does not outrank the selectors for `gh` any more than it does for `git`. It is the
  package's only non-git spawn that reads a repository.
  The probes are gated to the landing window (closeout-completed onward) so the
  status poll stays network-free during the build phase; `guidance.py`'s
  `status_payload` emits its result as the `landing` block, and the observer reducer
  composes it onto `EngineProcessNode.landing`. Probe failures degrade to
  `factState: "missing"` — never faked. **Slice 5l P2** hardens the probe so the
  dashboard can follow a REAL remote landing: the protected target `origin/<base>`
  is now probed **directly** via `ls-remote` (`_main_ref` + `_default_branch`,
  resolving origin's default branch from the remote HEAD symref, no `fetch`) —
  visible across the whole landing window before any PR and even when `gh` is
  absent, with its `state` honestly tracking whether THIS work landed
  (`merged`/`planned`/`unknown`) rather than merely whether main exists; and the PR
  ref carries gh's own open/merge timestamp (`at` = `mergedAt` once merged, else
  `createdAt`). It re-fires every projector tick (~1s), so no milestone hook is
needed for cadence.
260712-TRH-L7 changes the landing guidance boundary: `status_payload` remains the explicit
interactive fresh-probe surface, while `projected_status_payload` consumes only a pre-observed
immutable landing snapshot. The recurring projector therefore never invokes `git ls-remote` or
`gh` through guidance; missing and stale observations remain explicit.
- `start.py`, `startup/start_contract.py`, `startup/leaf_ref_start.py`, `closeout.py`, `integrate.py`, `cleanup.py`,
  `finalize.py`, and `abandon.py`
  own the named `c-09-git-worktree-manager` skill lifecycle operations.
  `cleanup_report.py` is deliberately **not** in that list: it owns no operation, only the operator
  report for a reclamation `finalize.py` already performed (260831-LOCR-L31).
  `start.py` calls `startup.start_contract.build_start_contract` to resolve the requested leaf ref through the
  `worktrees/leaf_refs.py` task-tree resolver before any start write; accepted refs persist the canonical
  task doc id in the leaf contract, while no-match/ambiguous refs return a `WorktreeCommandResult`
  refusal naming the expected `<repo>/<master-folder>/<doc-id>` form and candidates. Standalone/light
  task roots resolve through their non-master `task.json` doc id, slug/folder, and enclosure aliases, and
  resolver indexing skips sibling JSON artifacts unless they carry the task-document schema marker. After
  that, `start.py` runs a synchronous
  provider preflight, writes the contract, and
  then launches provider setup in the background (GitHub #53): dry runs stay
  synchronous, real starts return `starting` within seconds, and
  `retry_provider_setup` relaunches a failed/stale setup on an existing
  contract. Before any worktree exists, `start.py` also runs the stale-base
  preflight (GitHub #54): source branches behind/diverged from their upstream
  block the start with `stale_base_choice` recoveries (`fast-forward` /
  `proceed-stale`), and a missing external memory source branch is
  auto-created at the official memory tip using the code branch name as
  template. For master tasks, `startup/start_contract.py` creates or loads the root
  `series-contract.md` integration contract first, creates the integration branch from the protected/source
  branch, and then starts each leaf from that integration branch with its own
  `enclosures/<leaf-id>/series-contract.md`. `cleanup.py`/`abandon.py` refuse to tear down while a live
  (fresh-heartbeat) background setup owns the worktree. **Slice 05m** makes
  `cleanup.py` carryover-guarded and work-branch-retiring: `cleanup_result` now HARD-REFUSES
  (raises) when integration is completed but `guidance.carryover_done` is false (external
  memory) — cleanup deletes the parked memory branch carryover reads from, so the carry
  must run first; the proof is reachability of the real memory output from the official memory source. After the guard
  it retires work branches only after proving they are reachable from the contract's
  recorded source branch (`merge-base --is-ancestor work_branch source_branch`), then
  deletes them with `git branch -D`; this avoids Git's ambient `HEAD`/upstream merge
  target while preserving unmerged work branches as `kept_branches`. Task 14 corrected
  cleanup to operate on the just-finalized child edge only: it removes the task work
  branches (`code`, `memory`, optional `memory_integration`) and keeps parent/source
  branches for their own lifecycle edge. Cleanup
  dry-runs also model scheduled removals: registered worktrees and `provider-runtime/`
  are subtracted before the worktree group directory is classified, so a group that will
  become empty reports `would_remove` rather than `not-empty`; real cleanup still removes
  directories only after they are actually empty. Task 32 also makes cleanup reclaim the
  observer drift snapshot generated by the code worktree it is deleting: dry-runs report
  the exact snapshot under `drift_snapshots["code"]`, and real cleanup removes only that
  contract-owned repository/branch snapshot. `integrate.py` refuses while an undecided or policy-invalid `master-handover-approval` gate addressed to the integrating master exists anywhere in the workspace: the pure `handover_gate_guard` folds every gate log (`GateStore.all_current`) and matches gates by `enclosure` against the contract's `task_name`/`parent_task_name` — never the consuming contract's lifecycle — evaluating the application-threaded configured policy (the master-exit seam consumer, mirroring the closeout gate; gateless stays additive). Since cycle 7 the guard is evaluated on the dry run too — reported (`handover_gate` in the preview, whose summary names `handover-gate-blocked` when the real run would refuse) but enforced only on the real run, with no contract mutation on the dry-run path — and the pure sibling `unmatched_handover_gate_warning` puts a `handover_gate_warning` (unmatched OPEN handover gates + a verify-the-enclosure-spelling note) on gateless dry-run/integrated payloads, so a typo'd exact-string address cannot fail open silently. It then performs the code and
  memory fast-forwards atomically: it pre-validates that both fast-forwards are
  possible before mutating either branch and rolls both heads back on any
  memory-side failure, so integration never lands a half-integrated state.
  **Integration lands and stops; finalization reclaims (260831-LOCR-L31).** A completed integration
  publishes the landed refs through `landing_record.py::record_landed_integration` and returns. It
  runs no cleanup and its payload carries no cleanup report — the `cleanup` key there is the untouched
  contract cell. Terminal reclamation belongs to `finalize.py::_run_or_verify_cleanup`, which runs the
  existing `cleanup_result` procedure with `approved=not dry_run` / `teardown_providers` and shapes a
  real successful reclamation through the pure shaper `cleanup_report.py::cleanup_report`.
  **Why the ownership moved:** while `_integrated_result` reclaimed inline, cleanup had already
  reached `completed` when it returned, so the one guard that routes a landed leaf to
  `lifecycle_finalize_task` (`next_step.py::_gate_after`, keyed on `contract.cleanup != "completed"`)
  could never fire. A real landing therefore reported `nextOperation: "done"` while the leaf document
  stayed `planning` and its master row stayed `inProgress` — silently, on leaves L29 and L30.
  A refused or partial integration cleans up nothing — that is when the enclosure evidence is still
  needed — and a cleanup refusal at finalization now **blocks the task-edge close** instead of being
  reported after a landing that already claimed to be done. A checkpoint landing reclaims nothing
  either, and an unfinished master landed at a checkpoint is never finalized, so it keeps its
  worktrees, branches and enclosure.
  The report shaper is gated by its caller: a dry run or a nonzero cleanup return code is passed
  through in cleanup's own words, because a preview must not assert a reclamation that never happened
  and a refusal must keep its `blockers` and partial inventory.
  `abandon.py` is the discard-without-integration sibling: it reclaims the
  isolated provider stack and removes worktrees/branches without requiring a
  prior integration.
- `finalize.py` owns the terminal `lifecycle_finalize_task` operation. It
  refuses until closeout and integration are complete, the landed code commit is
  an ancestor of the recorded local source branch, and external-memory carryover
  is done; then it runs or verifies cleanup and marks the contract-bound leaf and
  its derived immediate parent row `Completed`: the master the leaf names or, for
  a leaf naming none, the folder's `task.json` master that lists it (MIK-R38). The
  proof is one parent-child branch edge at a time. PR-gated flows are identical
  after the PR merge has been pulled locally, while squash-merge equivalence is
  not inferred by default.
- `sync.py` is the narrow public `worktree_sync` facade. It validates typed input, keeps preview
  mutation-free, refreshes source evidence before locking, rereads the full contract under
  authority, and delegates to the ordinary or atomic-series transaction owner. The transaction
  pins exact refs in the enclosure-root journal, retains code/memory conflicts in `.sync`
  worktrees, and resumes or cancels through `resolution_action=continue|cancel`; it never silently
  aborts a conflict. `guidance.py`'s fetch-free `freshness` block in `worktree_status` is the
  detection surface that recommends it.
- `provider_async.py` owns the background setup launch (daemon thread), the
  durable `setup-progress.json` under the worktree group's provider-runtime
  dir, the `worktree_status` providers projection (running / stale / ok /
  ready-with-failed-phases / failed + retryArgs), and the live-setup guard.
  The progress file format itself lives in `providers/setup_progress.py`.
- `provider_teardown.py` performs full-reclaim teardown of a worktree's
  isolated provider stack (Docker rm -f containers and networks derived from
  persisted settings, then rmtree the provider-runtime tree, reclaiming
  root-owned data via a docker chown when needed). Used by both `cleanup.py`
  and `abandon.py`.
- `onboarding.py` owns closeout-time onboarding metadata and entity fingerprint
  refresh planning, plus the four-case body/history gates
  (`classify_sidecar_updates` / `require_updated_sidecar_content` for file
  sidecars, `classify_route_overview_updates` /
  `require_updated_route_overview_content` for route overviews): a changed
  source's sidecar — and the route overview that is its **nearest governor** —
  must pair a meaningful body change with a new Update History entry, or carry
  an explicit `No content impact:` / `No route impact:` history entry.
  Ancestor-matched overviews are reported as `stamped_without_body_review`
  rather than gating. Previews and apply payloads surface marker-attested
  documents. Shared metadata/route parsing lives in `kernel/onboarding_doc.py`
  and is re-exported here. Closeout preview and apply also pass
  `context.storage` explicitly to route-index generation, preserving the same
  repository/path-rule authority used when the onboarding plan was resolved.
  Route planning also includes overview documents changed since the task's
  verified memory baseline, even when their source drift predates the current
  leaf code range. Those directly edited overviews become domain-evident for the
  existing body/history classifier: the expansion makes them stampable in the
  transaction but never permits metadata-only or untraced refreshes. A narrow
  generated-data exception recognizes a task-edited overview whose only body
  delta is the final reference-cell `path:line[-line]` coordinate; sanctioned
  citation repair can advance those ranges without fabricating history, while
  prose, claim, anchor, path, table-shape, and other body changes still gate.
- The closeout worklist (issue #83) is `closeout.py`'s
  `closeout_changed_paths`: working tree ∪ the unverified committed range, so
  transported history (merges, pre-committed slices) gates and stamps like
  hands-on edits. The onboarding plan's two-tier split (`working_paths`) keeps
  missing-sidecar blocking on working-tree paths only; committed-range paths
  without onboarding surface as the non-blocking `unonboarded` report. Body
  gates baseline against `contract_memory_verified_commit` so memory work
  committed before closeout classifies honestly, and payload lists that scale
  with transported history are exposed as count + sample
  (`PATH_SAMPLE_LIMIT`). Slice 6b adds **server-side gate enforcement** to
  `closeout.py`: when the contract has a `lifecycle_id`, closeout refuses unless
  the lifecycle's `closeout-approval` gate is developer-approved or approved by
  a policy-valid delegated orchestration decision
  (`controlplane.evaluate_closeout_gate(..., policy=args.gate_policy)`) and
  reports a `closeout_gate` block; gateless lifecycles keep the chat commit gate.
  **Since 260731-EFA-L5 the "marks it `applied` on success" half of that is retracted** — see the L5
  section below. The `applied` snapshot is now written by `_claim_closeout_gate` (line 449) through
  `GateStore.claim_approval`, one statement *above* the first commit (line 795), not after
  `write_contract`; `_mark_closeout_gate_applied` was deleted, and the early check is renamed
  `_refuse_unsatisfied_closeout_gate` (line 424) because it can only deny.
  Task 30 adds the already-integrated re-closeout reset: closeout source-head
  validation accepts the recorded integrated tips, preview reports
  `integration_reopen.would_reopen`, and apply reopens `integration_status` only
  when the new code or memory-content commit is not yet on the recorded source
  branch. Clean no-op re-closeout keeps the completed integration state and does
  not create a synthetic memory output or a cache-only commit.
  260718-CHATS-L5I inserts the strict `code_quality_gate.py` adapter after
  preview/approval validation and before every apply **commit**. A quality failure
  therefore creates no code or memory-content commit and leaves contract and
  applied-gate state untouched; only a clean wrapper result permits `commit_if_dirty`
  and the subsequent onboarding and memory-content sequence. **Since 260731-EFA-L4 the gate is not
  reached directly**: `closeout_result` (line 743) calls `_gate_staged_code` (line 684) at line 786,
  which stages the code worktree first, so the *index* is one mutation that now precedes
  the gate and survives a refusal. See the L4 section below for why staging is what makes
  the gate see created files, and why the two refusals must run ahead of the reset.
  (These four line numbers all moved with 260731-EFA-L5's +98 lines in `closeout.py`; the symbols
  and the claims are unchanged.)
- `args.py` defines the frozen `WorktreeArgs` cross-layer DTO that operation
  modules consume in place of `argparse.Namespace`; `from_namespace` builds it
  from partial CLI/application namespaces with per-field defaults. It carries `parent_task` and `leaf_id`
  for nested active task-root and leaf-enclosure resolution.
- `cli.py` keeps command-line parsing and JSON print adapters out of operation
  modules and converts each parsed namespace into `WorktreeArgs` at the boundary.
  Its `heal-leaf-ids` subcommand (260712-PTS-L1) is the deliberate invocation seam for
  `worktree_contract.heal_contract_leaf_ids` (`--coordination-root`, `--dry-run`; prints the heal
  report JSON) and intentionally bypasses `WorktreeArgs` — the heal is a one-shot legacy leaf-id
  migration sweep, never a per-read side effect, now that `load_contract` is walk-free and never
  normalizes.

## Closeout Auto-Carry And Source-Moved Recovery Guidance

`modules/closeout_lineage.heal_current_source_lineage` is the closeout-family guard clause: it
carries a settleable stale transitive break (`behind > 0`, including a `diverged` edge, because a
leaf owning its own commit is normal) through the existing journaled `worktree_sync` transaction,
re-reads the reloaded contract, and re-proves immediate source heads. `dry_run` refuses with the
preview duty without mutating; an unprovable projection escalates to the human developer; a retained
sync conflict hands back both worktrees and their duties. `closeout.py` runs it at both entry points
and threads the healed contract into candidate revalidation.

The operator-facing recovery prompts moved with it: `integrate._blocked_non_ff_result` and
`integration/integration_resolution_handoff.py` now route through `worktree_sync` plus a new
targeted closeout rather than `--strategy replay`. `replay` itself remains supported and is the
memory-carryover vehicle; only the guidance changed.

## Historical 260731-EFA-L2 Lifecycle Parameter Objects

The worktree lifecycle's long argument lists became frozen value objects, most of which are
route-level vocabulary rather than local tidy-ups:

- `models.VerifiedChange` — the landed code change onboarding metadata is stamped against
  (`commit`, `commit_date`, `changed_paths`, `working_paths`). `closeout` builds it once;
  `onboarding`'s three refreshers take it, so a refresher cannot stamp one commit's hash beside
  another's path list.
- `worktree_contract.ContractTask` / `LeafIdentity` / `RepoBranchPlan` — what both contract
  constructors now take. On the series contract the old `protected_branch`/`integration_branch`
  pair is the code plan's `source_branch`/`work_branch`, and `memory=None` expresses the whole
  absent-memory state.
- `start_progress.StartingEnclosure` / `StartBeat` — the pre-contract observability payload, split
  into what the beat is about versus how far the start has got.
- `cleanup.RetiringBranch`, `integrate.IntegrationSources` / `IntegratedCommits`,
  `provider_async.ProviderSetupJob`.

`start_result` is now three stages (`_existing_contract_result`, `_preflighted_contract`,
`_create_start_enclosure`) and `lifecycle_guidance` three phase groups whose order is the
precedence contract. `context.py` builds the kernel resolver's `CoordinationHints` /
`EnclosureSelector`. Every payload, refusal, recovery choice and written contract is unchanged.

## Historical 260731-EFA-L3 This Route No Longer Runs Its Own Git

**`git.py` used to define its own `run_git`, and it was the kernel's function with the
environment guard dropped.** Only `kernel/git_command.py`'s copy passed
`env=git_environment()`, which strips the eight `GIT_DIR`-family repository selectors
(`GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`,
`GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`, `GIT_NAMESPACE`, `GIT_PREFIX`).
`cwd=` does not defeat those variables — git consults them first — so with `GIT_DIR`
exported the *same logical operation* landed in a different repository depending on
which copy ran.

This route is where that mattered most, because this route is where the destructive
verbs live. All of these are reachable from the former unguarded copy and are still
here, now on the owner:

| Operation | Site |
| --- | --- |
| `commit` | `git.py` `commit_if_dirty` (line 85) |
| `merge --ff-only` | `integrate.py` (line 462, and memory at 467) |
| `reset --hard` | `integrate.py` rollback (lines 478-479) |
| `rebase` | `integrate.py` (lines 184, 236) |
| `branch -f` | `start.py` (line 393) |
| `branch -D` | `cleanup.py` (lines 77, 94) |
| `worktree remove [--force]` | `cleanup.py` (line 32) |
| `push origin --delete` | `cleanup.py` `_push_branch_deletion` (line 142) |

L4 moved every one of these except `git.py`'s: `integrate.py` +2, `start.py` +7, `cleanup.py` +5 and
`code_quality_gate.py` +11 lines above the cited sites. The symbols and the claims are unchanged.

All nine git-touching modules in this route now import from
`agents_remember.kernel.git_command`: `git.py`, `abandon.py`, `guidance.py`,
`integrate.py`, `start.py`, `sync.py` and `cleanup.py` take `run_git`, while
`landing.py` and `code_quality_gate.py` take both `run_git` and `git_environment`
(they each also spawn something that is not `git` — see below). Nothing about the
helpers themselves changed.

**The runner had to be made fit to be the only one before it could be the only one.**
Its `timeout` was hard-coded to `5`, which is right for `rev-parse` and absurd for a
rebase, so consolidating onto it unchanged would have turned every integrate into a
five-second timeout. `timeout` is now a per-call parameter with three named classes —
`GIT_LOCAL_TIMEOUT_SECONDS = 300` (the default: rebase/merge/status),
`GIT_REMOTE_TIMEOUT_SECONDS = 120`, `GIT_METADATA_TIMEOUT_SECONDS = 30`. This route's
local work takes the default; `landing.py` keeps its own shorter 8s probe bound.

Three route-visible consequences beyond "same behaviour, one runner":

- **`cleanup.py`'s remote calls are bounded for the first time.** `git ls-remote --heads
  origin` and `git push origin --delete` ran inside an MCP tool call, which the client
  cannot cancel, through a runner that set no timeout at all — an unreachable or wedged
  remote held the tool call open forever. `_remote_git` (line 113) runs them at
  `GIT_REMOTE_TIMEOUT_SECONDS` and returns `None` on `subprocess.TimeoutExpired`, which
  `delete_remote_branch_if_present` (line 127) and `_push_branch_deletion` (line 141)
  fold into the already-handled `{"remote_deleted": False, "reason": "remote-unreachable"}`.
  A stall therefore reads as an unreachable remote in the payload rather than escaping
  as an exception or hanging.
- **`code_quality_gate.py`'s repository probe is guarded.** `_git_common_dir` (line 187)
  hand-rolled `subprocess.run` without `env=`; it now calls
  `run_git(code_worktree, ["rev-parse", "--path-format=absolute", "--git-common-dir"])`
  (line 190). That value decides which repository the mandatory closeout quality gate
  then certifies, and this gate runs from the pre-push hook — where `GIT_DIR` *is* set
  by git itself.
- **`code_quality_gate.py` also stops handing the selectors to its child.**
  `quality_environment` (line 168) used to start from `dict(os.environ)`; it now builds
  from `git_environment()` (line 178), so the eight repository selectors are gone before
  the quality wrapper subprocess starts. That wrapper derives its own scope from
  `git ls-files` and its diff base from `merge-base`, and closeout spawns it from paths
  where `GIT_DIR` can be exported. Every git call inside that child strips the selectors
  itself today, so this is defence in depth — but the gate decides *which repository gets
  certified*, and that must not rest on the continued good behaviour of a process this
  one cannot see.

`mcp/tests/test_git_command.py` is the proof: it points every selector at a decoy
repository and asserts the real one received the commit and the decoy did not
(`test_a_commit_lands_in_the_real_repository_not_the_decoy`), plus
`test_a_stalled_push_reports_unreachable_instead_of_hanging` and
`test_both_remote_calls_carry_the_remote_bound` for the cleanup path. `conftest.py` also
strips the selectors, but the decoy test re-sets them inside its own scope precisely so
it cannot pass on the conftest's account — do not "simplify" that away.

## Historical 260731-EFA-L4 Typed Vocabularies, And A Gate That Sees What It Certifies

Two independent things landed here, and both are about a check that could be defeated with
nothing reporting it.

### The six contract vocabulary cells stopped crossing `dataclasses.replace`

`abandon.py`, `cleanup.py`, `closeout.py`, `integrate.py` and `start.py` all amended the
contract with `dataclasses.replace(contract, cleanup=…, integration_status=…, …)`. Typeshed
declares `def replace(obj, /, **changes: Any)`, so **pyright checked nothing about those
keywords**: `replace(contract, cleanup="reclaimed-ish")` produced zero diagnostics even though
`WorktreeContract.cleanup` is a four-member `Literal` and the wire model that reports it
rejects everything else. Each module now routes the vocabulary cells through
`worktree_contract.ContractCells` + `amend_contract`, a frozen record whose six declared
fields put them back in front of the checker, while `replace` still performs the copy and
still carries the free-text cells beside it (commit hashes, approval notes, strategies —
these have no vocabulary to check against, which is exactly why they stay where they are).

| Call site | Cells it moves |
| --- | --- |
| `abandon.py` line 74 | `cleanup="abandoned"` |
| `cleanup.py` line 395 | `cleanup="completed"` |
| `integration/master_review_gate.py` (the `blocked_integration_payload` owner since the closeout-door cut) | `integration_status="blocked"` |
| `modules/landing_record.py` (the single landing writer since L29; `integrate.py::_integrated_result` and `_checkpoint_result` both call it) | `integration_status="completed"`, `cleanup="pending"` — or `integration_status="checkpointed"` with `cleanup` untouched when `checkpoint=True` (260831-LOCR-L30) |
| `closeout.py` line 831 (`ContractCells` at 848) | `human_review_status`, `closeout_status`, `integration_status`, `cleanup` |
| `start.py` line 141 | `memory_mode="disabled"` (the memory-disabled downgrade) |

Undo one of these back to a bare `replace` keyword and **nothing fails at the call site** —
that is the whole defect. It fails later, at the packet, as a pydantic `ValidationError`
raised inside an MCP tool handler that has no `except` for one. The rule that keeps it shut is
"no `replace` call anywhere may carry one of these six keywords", enforced together with
`mcp/tests/test_wire_vocabulary_exhaustiveness.py`.

`startup.start_contract.build_start_contract` (line 187) gained a second `except` for the same reason.
`worktree_start`'s `workflow_kind` and `memory_mode` reach the MCP signature as free `str`
(the tool declares `workflow_kind: str = "light-task"` and documents `'light-task'` or
`'chat-task'`), and `worktree_contract._task_vocabulary` now *refuses* an unknown one at both
contract factories. Nothing between there and the `@server.tool()` handler catches a
`ContractError`, so line 198 converts it through the new
`startup.leaf_ref_start.invalid_contract_request_result` (line 38) into the same
`WorktreeCommandResult(2, {"state": "invalid-request", …})` shape every other blocked start
already used, naming the legal set instead of producing a traceback. Note that this `except`
is broader than its docstring says: it also catches a `ContractError` raised by the
`write_contract` inside `_parent_series_contract` (line 176), which is a write-validation
failure rather than a bad caller argument — the message still names the field and the file, so
the refusal stays honest, but it is not only about arguments.

### `closeout.py` stages the worktree before the quality gate

`closeout_result` (line 743) no longer calls `run_strict_code_quality_gate` directly; it calls
`_gate_staged_code` (line 684, called at line 786), which does `git reset --mixed --quiet HEAD` then
`git add -A` (lines 738-739) and *then* runs the gate.

**Why:** every rail of the wrapper reads the index. `code_quality/check.py::derive_scope`
(line 199) enumerates what ruff and pyright are given with `git ls-files`, and `diff_coverage`
diffs the base against the tracked tree — both blind to a file git has never been told about.
Closeout commits with `git add -A`. So until it staged first, **every file a task created
rather than edited went into the commit without a single rail reading a line of it**, and the
gate reported green having never seen it. Check it against this route's own history:
`git show --diff-filter=A --name-only abc7cbcc` (L3's tail, the commit this leaf is based on)
lists four added files, two of them `.py` — `mcp/tests/test_cold_start.py` and
`mcp/tests/test_git_command.py` — and neither could have appeared in that closeout's
`git ls-files`, because `ls-files` does not report a path git has never been told about.
The index cut the other way too: a path the task *deleted* stayed in `ls-files` until the
deletion was staged, so ruff was handed a file that no longer existed and took an `E902`.

**Why the reset and not just the add:** git applies ignore rules only to paths it does not
already track or hold staged, so a file staged by a refused attempt stays staged even after
the retry adds it to `.gitignore`, and the commit carries it. `--mixed` is index-only, so the
tree the gate certifies is byte-for-byte what the task left on disk; the reset simply makes
each run recompute the index from the working tree under the ignore rules in force *now*.

**The ordering is load-bearing, and this is the part not to "simplify".** `_gate_staged_code`
runs `_refuse_outside_a_linked_worktree` (line 557) and `_refuse_conflicted_worktree`
(line 599) **before** the reset:

- The first compares `git rev-parse --git-dir` with `--git-common-dir`: they differ in a
  linked worktree and are the same path in a repository's own checkout. It tests the property
  that makes staging safe rather than the contract's `kind` label, because
  `worktree_contract.default_series_contract` records `code_worktree=code.repo_path` — the
  primary checkout itself — and nothing else stops such a contract reaching
  `worktree_closeout_apply`. Move the reset ahead of it and the reset inflicts exactly the
  damage the refusal exists to prevent: a mixed reset in a checkout somebody works in discards
  their `git add -p` selection.
- The second lists `git diff --name-only --diff-filter=U`. `git add -A` over an unmerged index
  does not fail — it *resolves* every conflict to whatever the working tree holds, markers and
  all, and closeout then commits that. Move the reset ahead of it and the check is **silently
  disarmed**: `git reset` drops the unmerged index entries and removes `MERGE_HEAD`, so
  `--diff-filter=U` reports nothing and the refusal never fires again.

**A refused gate leaves the worktree staged, deliberately.** There is no rollback and none is
wanted: this checkout is the task's own disposable worktree (which is what the first refusal
makes true rather than assumed), nothing is committed, and the next attempt resets and
restages from the working tree so it reaches the index a first run would have reached. An
earlier attempt saved the index file aside and copied it back; that machinery is **gone rather
than fixed**, because it could not survive `core.splitIndex` (the saved pointer outlives the
`sharedindex.<sha>` that `add -A` expires, leaving `status` exiting 128) nor `SIGTERM`, which
is how an MCP server actually dies.

Both refusals and the staging are **conditional on the gate running at all** —
`requires_strict_code_quality(contract.code_worktree, code_would_commit=…)` still decides, so a
consuming checkout carrying no `code_quality/check.py` wrapper stages nothing early, runs
neither refusal, and reaches `commit_if_dirty`'s own `git add -A` exactly as before.

Three surfaces were re-worded to match, and they are wire-visible:
`code_quality_gate.code_quality_gate_preview`'s `enforced` reason (line 77) now names the
staging; `closeout_preview_payload`'s `closeout_order` (line 315) lists the two refusals, the
reset-and-stage step and the gate as four entries where it listed one; and the preview
`summary` says a refused gate leaves the worktree staged and commits nothing.
`run_strict_code_quality_gate`'s docstring records the corresponding boundary — it certifies
the index it is handed and says nothing about how it came to look that way, so its failure
message claims only that nothing was committed, **not** that the staging was undone.

Historical staging tests exercised created-file scope, task-worktree refusal, conflict-before-reset ordering, and retry equivalence. Those named tests were removed; the production staged-quality owner remains the source of these boundaries.

## Historical 260731-EFA-L5 Spending An Approval Is One Step Now, And One Consumer Still Does Not Spend It

This route holds two of the three reproduced ways one human approval could be spent twice. The
framing worth carrying at route level: **durability of a record is not atomicity of a decision.**
The gate log's own durability fix (`controlplane/durable_store.py`) made every record survive — and
this route's defects would have existed even if it had never lost a byte.

### `closeout.py`: the claim, and the semantics it changes

The check-then-act pair is gone. `_enforce_closeout_gate` → **`_refuse_unsatisfied_closeout_gate`**
(line 424), which now returns `None` and can only **deny**; `_mark_closeout_gate_applied` is
**deleted, not deprecated**. The spend is **`_claim_closeout_gate`** (line 449), which calls
`GateStore.claim_approval(lifecycle_id, kind=CLOSEOUT_GATE_KIND, now=…, policy=…)` — fold, policy
verdict and `applied` append inside one held lock on the gate log.

**The call site is the design** (line 795): one statement above the first commit, after
`_gate_staged_code` and immediately before `commit_if_dirty`, with a source comment forbidding a
move past the commit. Not earlier, because everything upstream — source-head validation, the
onboarding and route plans, the mixed reset and staging, the strict code-quality gate — only reads
or touches the index of the task's own disposable worktree, and a refused code-quality gate is the
common case, so claiming earlier would burn a developer's approval on a refusal that changed
nothing. Not later, because everything downstream writes a commit somebody would have to undo.

**The route-visible semantic change: an approval authorises ONE ATTEMPT, NOT ONE SUCCESS.** A
closeout that dies after the claim — crashed process, failed memory quality gate, git error, ENOSPC
— leaves the approval consumed and the next closeout needs a fresh gate;
`controlplane/enforcement.py` already words the remedy ("was already applied; open a fresh gate for
a new mutation"). Marking `applied` at the end instead means every way that late write can fail
leaves a live approval sitting on top of an unknown amount of completed, irreversible work — both
shapes were reproduced. A two-phase `claimed` state was considered and rejected: the release is the
same write at the same late position with the same failure modes, so it would need a reaper that
re-opens the window on a timer.

Historical replay-window tests exercised approval consumption before commit and refusal before consumption. That suite was removed; this paragraph records the earlier design history and is not current test evidence.

### `integrate.py`: an open decision, deliberately left open

**`integrate.py` never consumes the `master-handover-approval` gate at all.** `integrate_result`
(line 516) folds `gate_store.all_current()` (line 534), evaluates `handover_gate_guard` (line 535),
refuses when the verdict is not permitted, and integrates — there is no `apply_gate` and no
`claim_approval` anywhere in the module. This is **not** a record this leaf dropped and not a
regression: the consume was never written, on any commit. Today the handover gate is a *guard*, not
a *spend*, and nothing prevents one approved handover gate from permitting two integrations.

It is left open for two reasons a reader needs before closing it:

- **It needs a different key.** That gate is matched **cross-lifecycle by `enclosure`** against the
  contract's `task_name`/`parent_task_name` and lives on a different log than the integrating
  lifecycle's, so `claim_approval`'s `(lifecycle_id, kind)` key cannot address it.
- **`closeout.py`'s `integration_reopen` path means a legitimate re-integration exists.** Consuming
  on the first integration would make a re-integration of newly transported content start demanding
  a fresh handover approval, which nobody has decided is correct.

The retention half is already in place: `master-handover-approval` is in
`interaction_retention.SEAM_CONSUMED_GATE_KINDS`, hence in `CONSUMED_APPROVAL_GATE_KINDS`, so an
`applied` snapshot of that kind would be retained with no TTL the moment something writes one.

## Historical 260731-EFA-L16 — Closeout's Citation Gate Before The Suite

`closeout_result` runs the citation gate (`range_resolution` + `claim_reopen`) before the strict
wrapper and the code commit — working-tree checks that clear without a commit — and keeps drift,
shape, and history order in the post-commit sanity phase. The L6 clearing condition required the
commit it was checking against, deadlocking every structural change; `_combined_memory_quality`
reports the two phases as one gate. The approval claim still precedes the first irreversible
act.

## Historical 260731-EFA-L17 — The Altitude-Routed Quality Gate

This route owns the quality altitude ladder's machinery half. `code_quality_gate.py` gained
`QualityGatePlan` (mode `targeted`/`full` + optional cap), `GATE_TARGETED`/`GATE_FULL`, the
`memoryPolicy`/optional `memoryCap` payloads, cap-kill naming (returncode -9 / shell 137), and altitude invocation labels
(`AR_QUALITY_INVOCATION` = `closeout-staged` / `master-integration`).
`closeout.py` passes the leaf targeted plan at both call sites and through `_gate_staged_code`;
`memory_quality_check` stays a per-leaf closeout gate. Leaf integration lands the exact
closeout-certified commit without rerunning acceptance. `integrate.py` runs a gate only for
series/master contracts: the full wrapper once with host-managed RAM/swap by default;
an optional explicit cap is read from `load_agentic_settings(...).quality_gate.memory_cap_bytes`. A refusal returns
`blocked-quality-gate` and nothing merges.

## 260731-EFA-L9 Route Impact

`provider_teardown.py` moved to `application/provider_runtime.py` (absorbing the former
`provider_async.py` setup launcher) so worktrees stops importing providers; `provider_async.py`
is deleted. The new `worktrees/services.py` declares the `ProviderLifecyclePort`/
`MemoryQualityPort`/`CitationGuardPort`/`TerminalGuard` ports and the `WorktreeServices` bundle,
and `worktrees/modules/contract_reader.py` implements the kernel resolver's `ContractReaderPort`.
The closeout/integrate/guidance machinery is unchanged in behavior.

## L23 Parent-First Lineage Gate

Worktree start, attach, and reopen now consult task-derived ancestry before
resuming context or mutating task/contract state. Status publishes the same
projection and ordered `worktree_sync` contract path. Remote stale-base choice
is a later policy and cannot override super-to-master-to-leaf admission.

## L23 Long-Gate Source-Lineage Enforcement

Closeout and integration prove the complete transitive source-lineage chain at preflight, recheck
it after potentially long quality work, and check again immediately before approval claim or
source merge. Integration also pins exact code and external-memory source tips across the gate;
movement yields a retry without ref movement. Supporting cohesion changes route clean-quality
report promotion through the atomic-replace primitive and isolate strict-plan and closeout-result
construction without changing their enforcement authority.

Closeout separately pins the durable operation's full code candidate across quality at every
altitude. The final reversible check recomputes that tree before approval claim; leaf closeout also
revalidates its independent route-review record, while series/master closeout bypasses the
inapplicable terminal-leaf evidence and targeted acceptance. Series/master closeout also requires
a clean code checkout and records only its already-landed HEAD; it cannot create master code.

Repository linkage within that proof follows Git's resolved absolute common directory. Parent and
leaf contracts may address sibling linked worktrees of the same repository; distinct checkout
paths do not create a false repository mismatch, while missing or unresolvable Git identity still
fails closed.

## R39 Lifecycle Acceptance Route

Closeout and integration now split acceptance without duplication: a leaf is targeted-certified
once during closeout and lands without a rerun; a master runs full once during integration.
Series/master closeout requires clean landed code and runs no gate. The shared adapter refuses
host execution, applies an explicit self-wrapper-required policy to Agents Remember, and
revalidates the accepted candidate after long quality work before approval or merge.

## R42 Recovery Ownership

The route still coordinates closeout, but it no longer defines the typed memory outcome or proves
already-committed recovery cells itself. Both moved to sibling owner
`worktrees/closeout_recovery.py`; the coordinator imports them before amending the contract. The
exact staged-scope regression also moved to its own test module to satisfy the file-size rail.

## R43 Fail-Closed Repair

The closeout coordinator now narrows candidate-tree typing only after mandatory admission, and the
quality adapter consistently says `self-owned wrapper` while refusing non-Dagger executors in both
command and memory-policy builders. Self-repository enforcement and consumer opt-in remain distinct.

## 260815-DAG-L3 Queue-Owned Irreversible Boundaries (Superseded By CLIVE)

This section records the earlier DAG queue design: leaf closeout claimed and certified queue rows,
integration claimed/consumed them, and task-fact writers published through queue governance. CLIVE
moved operation recovery, generation controls, worker termination, direct landing, and durable
mutation evidence to the root journal. L3 then removed the remaining lifecycle-shaped rows and
task-authoring veto: task truth publishes first, affected projections become invalid-empty, and
waiting-only rebuild derives solely from exact-current task and door sources.

## 260815-DAG-L4 L4 Exact Worktree Lifecycle

Start, closeout, integrate, sync, cleanup, abandon, and reopen now share task-derived branch authority. Integration uses exact named-ref CAS and crash recovery; atomic series closeout records a complete leaf landing chain; lowest Git/worktree/terminal writers require capabilities instead of trusting caller-supplied branch names.

## 260815-DAG-L13 Atomic-Sequential Lane (Historical, Superseded)

`startup/start_contract.py` gates master series bootstrap on the effective execution nature (a nature-less
legacy master resolves atomic; organizational semantics exist only under an authored graph) and,
under the atomic-sequential default, returns a blocked `sequential-lane-owned`
`WorktreeCommandResult` naming the lane owner and legal next operations instead of starting a
second in-flight master; the block fails closed when the commanding sprint cannot be resolved.
Terminal series artifacts are ignored and reported through `startup/start_result.py`'s
`staleSeriesArtifact` fact. `integrate.py` surfaces the queue consume's stale-by-evidence siblings
on the result payload (`staleByEvidence`, each naming `worktree_sync`).

IAS supersedes that lane owner. Current start/attach/dispatch reconciles the commanded master in its
own contract-keyed activation record, without pausing any other master and without claiming a shared
source pair, and leaves task authoring upstream. Under the graph-less default nothing serializes the
masters: `atomic-sequential` describes the sprint's shape (every commanded master executes
atomically) and declares no dependency, so independent masters proceed concurrently. Current queue
projection observes the addressed contract's own record and never recreates the old owner from
contract census.

## 260815-DAG Master Full-Gate Repair Route Impact

`closeout_staged_quality.py` moved to the new `worktrees/queue/` sub-route; remaining module import paths updated to the moved `queue`/`integration` packages; `closeout.py` extracted `_closeout_quality_facts`.

## 260821-CLIVE-L1 Execution Modules

`args.py` transports one normalized effective closeout input, while legacy synchronous CLI apply fails closed. `closeout.py` coordinates journal-authorized execution and exact contract finalization and threads that effective value explicitly through every code/external/recovery consumer; external-memory refresh and the memory-content commit belong to `closeout_external.py`. That owner uses accepted messages and Git mutation evidence, excludes the consumer cache from content, and refreshes it only as a post-output observation. Guidance remains contract-pure: it publishes only static `intent_note` and routes exact candidate-derived requirements to preview/apply. Abandon and cleanup call lifecycle compatibility explicitly under the pure serialization lease.

## 260821-CLIVE-L2 Current Architecture

Closeout and integrate start or resume journal generations; sync/cleanup/abandon use the same admission projector but retain their own serialization. No module enumerates lower configured-reader failures or adds a fallback reader. Terminal retirement preserves canonical evidence; deletion is a later archive-proven operation.

`integration_recovery.py` proves exact ref convergence and the external-memory head before finalization recovery. The `startup/` package split keeps start derivation/result collaborators separate from `start.py` without retaining the old flattened import paths.

### Reconciled Source Evidence

- Closeout public execution boundary. [41]
- Fail-closed cleanup result. [42]
- Integration recovery requires exact authority-ref convergence and exact journaled memory-content proof. [43]
- Start helpers now live below the dedicated startup package marker. [44]

## 260821-DAGQC-L4 No Route Impact

`code_quality_gate.py` only narrows its host-refusal docstring to the acceptance claim it owns:
the pinned Dagger graph certifies acceptance. The module inventory and executable topology are
unchanged. Direct targeted Vitest remains a dashboard-owned diagnostic-only loop; this worktree
adapter still exposes no host quality executor, bypass, compatibility reader, or fallback.

## Historical 260821-DAGQC-L2 Immutable Quality Publication

`published_quality_manifest.py` is the sole strict schema-1.0 reader for the atomic quality pointer.
The clean executor writes that contract, and gate recovery consumes one immutable snapshot for
attestation, artifact integrity, and path resolution. Public recovery retains stable `reportPath`
and adds optional `publishedResultPath`; no legacy reader or host fallback was introduced. The
concurrent L4 Vitest diagnostic boundary remains unchanged.

## Historical 260824-PDLS — Dagger Publication Is The Evidence Altitude Boundary

The clean quality executor publishes route-neutral phase timing but mints certifying evidence only
after verifying one immutable schema-2 report generation and exact candidate tree. Code-quality
gate fresh/recovery paths consume that typed evidence for lifecycle acceptance. Schema-1 manifests
remain rejected; diagnostic evidence and timing files cannot substitute for publication.

## 260824-PDLS Final Integration-Evidence Boundary

The integration module consumes the exact Dagger certification and typed publication evidence
without re-running acceptance or accepting diagnostic output. Ref-state, topology collision, and
claim-transfer helpers now expose named facts to the integration owner rather than duplicating Git
and lifecycle policy across call sites.

## MCAR-L02 Closeout Admission Coherence

External-memory leaf closeout now calls the same structured
`require_current_curator_coherence` validator as public memory readiness and closeout-door
evidence before citation preflight or the expensive code gate. The result records the exact
coherence record digest and delivery attempt in preflight facts. No hardcoded Markdown filename or
task-evidence pointer can select a competing authority.

## MCAR-L03 Exact Pair Admission And Recovery

Closeout preview, apply admission, working-tree memory preflight, terminal result publication, and
recovery now consume the same `accepted_closeout_memory_pair` adapter. It resolves and revalidates
the configured leaf's exact code/memory pair, joins it to the current structured coherence record,
and carries the pair identity in public preview/apply/result payloads. Recovery re-reads the
contract pair before accepting prior commit evidence; a moved base, wrong checkout, or changed
contract refuses with typed pair facts instead of resuming against ambient Git. The worktree tool
boundary translates the shared pair/coherence error families once, without duplicating resolver
logic or adding a fallback route.

## 260831-CCR-L12 — Cost-Ordered Five-Gate Execution And Shared Dagger Authority

CCR-R12@v4 (commit `cfd09381`) adds `quality/dagger_authority.py` to this route: one host-level,
repository-external declaration (AR_DAGGER_RUNTIME_AUTHORITY) selects the already-running
connection-only Dagger endpoint and exact reusable layer store; admission inspects the live engine
connection-only, freezes an immutable `dagger-runtime-authority/v1` snapshot, registers the exact
consumer in a locked host-level owner registry (PID-safe process fingerprints, typed
authority-transition barriers, exact-owner release, crash reconciliation), and every refusal is a
typed `DaggerRuntimeAuthorityError` before any Dagger command starts. `clean_executor.py` admits or
reuses the authority for every profile-declared launch and releases the exact owner on
terminalization; `published_manifest.py` advanced the quality manifest to schema 3.1 with
`runtimeAuthorityDigest`; `gate.py` threads the digest through report/preview/payload/transcript;
and `closeout.py` runs its closeout gates in Gate-5 order - the Dagger-backed code-quality gate
first, the memory-quality pre-refresh only after it is green or not required. The checked-in
certification profile was regenerated (profile/runtime digests) with explicit per-rail
`successExitCodes`/`skippedExitCodes` and `consumingGates` declarations.

## 260831-CCR-L13 — Optional Non-Certifying Diagnostic E2E Run Control

CCR-R13@v2 (commit `4ba18bb23ba90e201bb37341d61c0efc64161fcf`, leaf 260831-CCR-L13) adds
`quality/diagnostic_executor.py` to this route: the run controller for the optional one-replication
real-Codex diagnostic lane. It consumes the trusted R12 host authority exactly as closeout and
integration do - admission freezes one existing connection-only runner/store snapshot and registers
the attempt as a live owner; run executes at most one replication and terminalizes pass/fail from a
complete diagnostic-altitude manifest (or a typed infrastructure/parser hard failure); abort
terminalizes with teardown evidence and no pass; and every terminalization releases only the
attempt's own owner, never retiring a runner or deleting the reusable layer store owned by another
operation. Gates 1-3 must be green at certifying altitude for the exact candidate before any
scenario step, and R16 telemetry envelopes are emitted under the diagnostic nonce.

## 260831-CCR-L14 - Final Real-Codex Gate-4 Run Control

CCR-R14@v3 (commit `54ff803a05209e06f732f2de1f90e2a71a069e08`, leaf 260831-CCR-L14) adds
quality/final_codex_executor.py to this route: the run controller for the certifying two-fresh
no-retry real-Codex Gate-4 lane. It consumes the trusted R12 host authority exactly as closeout and
integration do - admission freezes one existing connection-only runner/store snapshot and registers
the attempt as a live owner only after the exact candidate certifying Gate-1..3 manifests are
green against the frozen plan; run executes each fresh certifying repetition exactly once and
terminalizes the run from the complete certifying Gate-4 result manifests (or a typed
infrastructure/parser hard failure); abort terminalizes the unpublished slots with teardown evidence
and no pass; and every terminalization releases only the attempt own runtime owner, never retiring
a runner or deleting the reusable layer store owned by another operation. Retry is disabled for the
exact same plan identity, and fresh client/process identities are minted per repetition.

## Selected Quality Execution Routes

The selected code contract and original report transport have a local [execution overview](quality/execution/overview.md). The journal decides the permitted recovery suffix; these owners validate supplied originals, bind the exact sandbox and return real terminal evidence to that journal.

| Source File | Onboarding | Responsibility |
| --- | --- | --- |
| `quality/certification_run.py` | [certification_run.py.md](quality/certification_run.py.md) | Actual terminal recording, selected callbacks and complete original code-prefix readback |
| `quality/certification_terminal.py` | [certification_terminal.py.md](quality/certification_terminal.py.md) | Typed publication outputs and exact planned rail catalog decoding |
| `quality/certification_reuse.py` | [certification_reuse.py.md](quality/certification_reuse.py.md) | Original-object and physical-publication validation of zero-start rows |
| `quality/execution/` | [Execution overview](quality/execution/overview.md) | Canonical suffix DTO, frozen declaration bounds and prepared sandbox manifest |

- Selected execution recomputes canonical reuse, validates exact green retained prefix publications, and refuses Dagger starts outside code gates 1–4. [45]
- Retained transport membership and byte limits come from frozen producer declarations. [46]
- The prepared sandbox reobserves actual comparison source selection before manifest publication. [47]

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.


## CCR-R12@v5 Current Worktree Transaction Boundary

The closeout/integration module route now treats normal delivery as a transaction boundary. Closeout
preserves explicit approval, candidate/source identity, Git safety, and recovery evidence, commits
code through the staged-index transaction helper, performs raw external-memory metadata/entity/index
refresh, then commits substantive memory content with its `Code-Commit:` attribution when needed.
The ledger is rebuilt as a consumer cache; it creates no extra commit. Integration validates and
publishes a prepared pair with ref/tree compare-and-swap and no merge commit. Normal routes do not
automatically run strict code quality, memory quality, selected certification, curator coherence, or
independent review; full suites are an explicit developer request. The older quality-altitude
sections remain historical context for pre-R12 behavior.

## Historical milestone context: 260831-LOCR-L30/L34 Checkpoint Landing In This Route

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

`integrate.py` gained `checkpoint_landing_result` and `_checkpoint_result`, and
`landing_record.py`'s single writer gained `LandedIntegration` plus a `checkpoint` flag. The checkpoint
path selects `series_closeout.publish_series_checkpoint_under_authority`, records `checkpointed`
through the shared writer, and runs no automatic cleanup, so an unfinished master landed at a
checkpoint keeps its worktrees, branches and enclosure. `record_landing.py` (the PR route) calls the same writer with the bundled
`LandedIntegration` and no checkpoint flag, so the terminal `integration` cell still has exactly one
definition. `git_worktree_manager.py` re-exports `checkpoint_landing_result`.

**Superseded by 260831-LOCR-L34, which repaired the route's reachability.** The keyword-only
`checkpoint: bool` flag is gone; `checkpoint_landing_result` now reads the `CheckpointLanding` value
built by `checkpoint_landing_eligibility` — the route's own capture of the live series code and memory
work-branch tips plus their proved ledger mapping — because the old path read the contract's closeout
cells, which an unfinished master does not have and which made the route unreachable in both
directions. The
checkpoint no longer calls `validate_integrate_contract`. L34 also made the ledger projection a
preview-side proof for **both** routes (`_require_ledger_projection` runs before the dry-run branch),
gave the protected-ref edge a required `operation` name so a checkpoint's `integration-ref-race`
payload routes the operator back to the checkpoint rather than to `worktree_integrate`, and extracted
the closeout completion gate into `series_closeout.require_closeout_publication_authority` so
`closeout_preview_payload` refuses what the closeout apply refuses. The full preview/apply parity
invariant and its instance inventory live on [the worktrees route overview](../overview.md) and in
[`memory_quality/overview.md`](../../memory_quality/overview.md).

**260913-LCA-L11 removed this route's ledger-history dimension.** The developer's ruling of
2026-09-14T08:15+02:00 made the rebuild outrank the tracked ledger file, so the shared landing proof
no longer judges the landed table against the source file's row list or row order. Concretely on this
route: `_landing_admission(*, checkpoint)` lost its `contract` parameter, because the finished
master's ledger prefix it used to derive (`series_closeout.atomic_series_ledger_prefix`) is deleted
with its only consumer; `_require_ledger_projection` no longer receives `expected_series_prefix` or
`checkpoint`; and `LandingAdmission` carries one fact, the checkpoint's captured candidate. The
preview/apply parity instances 4 and 5 are unchanged and now hold by construction rather than by both
surfaces deriving the same ledger shape. What the proof still refuses — the landed pair's mapping,
per-row truth, the memory content's descent from the exact source, and a header that disagrees with
its own first row — is inventoried on the `worktrees/overview.md` route and the
`integration_ref_transaction.py` card; the removal's known cost is recorded there too.

The typed-vocabulary table below therefore names `landing_record.py` as the call site of the landing
cells rather than `integrate.py`, and `integration/master_review_gate.py` as the `blocked` call site.

### The Three Downstream Readers A Checkpoint Had To Teach

Fixing the writer was not enough: three readers keyed on `integration_status == "completed"` and
described a checkpointed series wrongly. All three are now corrected in-tree, and each is documented
where it lives rather than here.

- `guidance.py::_post_integration_phase` gained a `checkpointed` branch returning the existing
  `worktree-started` phase with `continue_work` / `worktree_status`; without it the projection fell
  through to `integration-pending` and pointed an open series at `worktree_integrate`, which refuses
  it. No new `WorktreePhase` member was added — the alias is a closed `Literal` mirrored by the
  dashboard, and the summary carries the checkpoint truth.
- `closeout.py::_landed_source_heads` (renamed from `_completed_integration_source_heads`) now admits
  the commit a checkpoint recorded as an expected source head; base-only heads made the checkpoint's
  own landed move refuse as "source branch moved since task start".
- `record_landing.py`'s `already-recorded` guard covers `checkpointed` too, so the pull-request route
  cannot upgrade an open series into `completed` + `cleanup="pending"`.

The remaining `integration_status == "completed"` sites are deliberate: they ask "is this contract
complete?", and a checkpoint must read as not complete. They are listed and dispositioned on the
`closeout.py` card.

## 260831-LOCR-L36 Contract-Keyed Atomic-Series Activation

The activation record behind start/attach/dispatch/sync moved from one file per **protected source
pair** to one file per **series contract**. Two atomic masters commanded by one sprint derive the
same protected source pair (same code/memory repository and branch; only the work branches differ),
so the older key let the second master's selection replace the first and report the first as
paused-by. Each contract now owns its record at
`controlplane/atomic-series-activation/<contract_fingerprint>.json`, where `contract_fingerprint` is
the sha256 of the canonical resolved contract path. `AtomicSeriesActivationRecord` is
`schemaVersion "2.0"` carrying `contractFingerprint` and no `sourcePair`/`sourcePairFingerprint`;
`AtomicSeriesActivationObservation` carries `contract_path` + `contract_fingerprint`; and
`observe_atomic_series`/`observe_atomic_series_path` take the contract rather than a pair.
`_require_record_identity` refuses to adopt any record that is not this exact contract
(`atomic-series-activation-contract-mismatch`). `atomic_series_admission_projection` emits
`contractFingerprint` and no `classification`, `blocking`, or `sourcePair`, and
`activation_waiting_reason(observation)` takes only the observation and returns only
`atomic-series-reconciling`. The terminal release, the cancellation-owner guard, the
sync-continuation guard, the terminal-contract selection refusal, the corrupt-record archive path,
and the bounded 8192-char diagnostic detail are unchanged in semantics and are now addressed per
contract. Everything under `worktrees/integration/**` and `worktree_integrate` is untouched, and the
graph-less sprint scheduling default is unchanged: `atomic-sequential` describes the sprint's shape
(every commanded master executes atomically) and serializes nothing — nothing serializes a graph-less
sprint — while attaching a master to a graph-less sprint still reports graphNode
`deferred-no-graph-default`.

## 260831-LOCR-L37 The Stop-Only Pause Module

`pause.py` is a new module in this route and the whole of it is one operation:
`pause_result(args, current_contract)` releases one atomic master's selection, publishes nothing and
hands the turn back. It belongs in `modules/` because it is an operation a public tool reaches through
the facade — `git_worktree_manager` imports and re-exports `pause_result` — not a helper inside another
module's seam.

It adds no authority. The release is delegated to the existing
`activation/atomic_series_activation_release.py::release_atomic_series_selection`, the same call sync
cancellation and terminal cleanup already make; the pause contributes the caller-facing shape, not a
second scheduling or vacancy mechanism. The module performs no Git, imports no integration, landing,
closeout or ledger module, and writes exactly one thing — the activation snapshot recording that this
contract is no longer selected.

The refusals come from the release authority and are explained, never suppressed: an addressed record
this contract does not own refuses as `atomic-series-activation-release-unreadable`, and a non-series
contract is refused here as `pause-requires-atomic-master` because a leaf owns no selection of its own.
Every refusal returns `paused: False` and, like the success payload, proposes no next call.

Read the file's own card ([`pause.py.md`](pause.py.md)) for the split against
`worktree_checkpoint_landing`, which remains the separate publication in `integrate.py`, and for the
measured import-closure evidence that the stop cannot reach a publication.

## 260831-LOCR-L38 The Already-Vacant Stop

A master holding no selection is already stopped — that is the ordinary state of a master between
landings — so the pause reports it as the success it is instead of failing an intent it has just
satisfied. `_already_stopped_result` answers the release authority's
`atomic-series-activation-selection-missing` status itself, but only after `observe_atomic_series`
confirms the record is `vacant`; the success is explicit (`atomic-series-already-vacant`, `paused: true`,
`_ALREADY_VACANT_SUMMARY` naming that no selection was held) so a caller can tell it apart from a real
release, and it writes nothing at all. This is the one release outcome the pause answers itself:
`_RELEASE_REFUSAL_DETAIL` no longer carries a `selection-missing` entry. An unreadable record and a
record naming another master stay refusals, because neither proves the master is inactive, and
`release_atomic_series_selection` is unchanged because explicit sync cancellation still requires an
existing exact selection.

The companion change is the removal of the child-admission seal: `worktrees/atomic_series_seal.py` and
its `require_series_accepting_leaves` predicate are deleted, so no closeout/integration/cleanup cell
refuses a leaf and a master that took a checkpoint landing can still admit the next one.
`mcp/tests/test_lifecycle_playthrough_end_to_end.py` plays the whole lifecycle in order and proves it.

## Historical milestone context: 260913-LCA-L1 Memory-Content Commit Attribution

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

A closeout's memory content is now attributed inside the commit object rather than only beside it in
the tracked ledger table. `EffectiveCloseoutInput.memory_content_message(code_commit)`
(`models/closeout/input.py`) returns the closeout's own
message verbatim and appends the trailer as its own final paragraph, so
`git interpret-trailers --parse` and `git log --format='%(trailers:key=Code-Commit)'` both read it as
data and `Code-Commit: <sha>` names the code commit that same closeout landed.

The key itself is declared once, and not here: since 260913-LCA-L2 it lives in
`kernel/memory_attribution.py` — the module that reads the trailer back out of the history — and
`models/closeout/input.py` imports it (`input.py:9`). The direction is fixed by `layers.toml`
(`kernel` ranks below `models`, so a kernel module importing a model would import upward), and
`grep -rn '"Code-Commit"' --include=*.py mcp/` has exactly one hit. The writer and the reader
therefore cannot drift into two literals, which is the failure this section's whole design is about:
a writer whose key the reader does not parse looks like "no attribution exists" rather than like a bug.

That is the closeout-shaped way in to the one definition, and both sanctioned closeout routes render
through it: this route's `_commit_memory_content` (`closeout_external.py`, handed
`code_commit=change.commit` by `external_closeout_commits`) and the branch-addressed direct-landing
route's `_direct_memory_commit` (`integration/direct_landing/direct_landing_execution.py`, handed
`code_commit=operation_input.codeCommit`). Neither rewrites the closeout message; the trailer is
appended, never substituted. Since 260913-LCA-L4 the method delegates to
`kernel.memory_attribution.render_memory_content_message`, which is the one writer for all five
producers — the production/maintenance/direct-landing `worktrees` family included — so the format is not
owned anywhere under `worktrees/` (see the producer-surface section below).

The seam is the message construction rather than a later step because the message is hashed into the
object: `commit_verified_staged` runs `git commit --no-verify -m <message>` on the already-staged tree
(returning HEAD unchanged when nothing is staged) and `commit_if_dirty` is `git add -A` plus
`git commit -m <message>`, so the rendered string *is* the commit's message, and `prove_git_commit`
journals that exact sha on the next statement. Adding the attribution afterwards could only be
`git commit --amend`, which rewrites an object already proved and recorded as `memoryContentCommit`.
`git notes` was rejected for the same reason — notes are not bound by the hash.

The `memory.md`-only ledger commit is deliberately excluded: it has no code counterpart to name, and a
second trailered commit for one code commit would project a duplicate row. Absence is the detection,
not a legacy state to tolerate.

## Historical milestone context: 260913-LCA-L4 The Producer Surface Is Total (5 Producers, 0 Untrailered)

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

A memory commit that names no code commit contributes no ledger row, and the projected ledger cannot tell
that apart from a producer that kept the old shape — the pairing is simply gone. So the transition is
either total or it is a silent hole in the map, and L4 made it total. The census below was measured at
base `5bb124d4` from source and **corrects** the master's 2026-09-13T22:05 decision in two places:
`worktrees/queue/closeout_recovery.py:209` is that route's CODE leg rather than a memory-content producer,
and the producer the first census missed is `worktrees/integration/closeout/preparation/memory_output.py`.

This route's own producer is `_commit_memory_content` (`closeout_external.py`, commit site `:165`): it
commits `effective_input.memory_content_message(code_commit)` (`:167`), which is now a delegation to
`kernel.memory_attribution.render_memory_content_message` — the one writer of the trailer. Nothing about
the route changed apart from that delegation: same message body, same leg, same gates, same refusals. A
resumed closeout that still owes its memory commit reaches this same producer, which is why the recovery
route is attributed without owning a commit site of its own.

The five producers, each reaching the shared renderer, are: `closeout_external.py:165` (this route);
`integration/direct_landing/direct_landing_execution.py:270`; `preparation/memory_output.py:92` (its
memory-content leg only); `memory/carryover.py:846`; and `memory/baseline.py:210`. Every other commit site
is trailerless **by rule with a recorded reason**, not by omission: every ledger leg; the recovery route's
code commit; `sync_transaction_git.py`'s memory merge commits (two memory parents and no single code
commit to name); and carryover's nothing-to-carry path, which creates no commit at all.

Two of the five take their commit message as a **public argument of another tool** — carryover's
`CarryoverCommitMessages.memory` and baseline's hard-coded adopt subject — which is why the renderer
appends the attribution as its own final block after a blank line rather than weaving it into the caller's
body: the body may be several paragraphs and its own last paragraph may itself be `Key: value` lines, and
a producer must never edit the string it was handed. The census is enforced from source by
`mcp/tests/test_memory_attribution_producers.py`, and the recovery route's behavioural half lives in
`mcp/tests/test_transaction_only_worktree_delivery.py::test_closeout_recovery_attributes_the_memory_commit_it_still_owed`.

## The Two Memory-Candidate Roots That Landed Here In `806649b9`

Commit `806649b9` moved two candidate-identity owners into this route, each as a **pure rename** (both
blobs are byte-identical before and after): `future_code_candidate.py` from
`memory_quality/`, and `memory_candidate_pair.py` from the same place, which had itself arrived there
from `worktrees/integration/closeout/` in the de-entanglement cut. They were not new code and this
route did not previously own them; what changed is the rank they sit at and the route a reader
reaches them from.

`future_code_candidate.py` owns the exact pre-commit **future-code** route identity: a frozen,
strict three-field model (`FutureCodeCandidateIdentity` — observed HEAD, configured base, candidate
tree) plus the capture and currentness functions that derive and re-prove it, refusing non-leaf use
and translating expected Git/filesystem failures into the package's central typed error family. It
wraps the canonical isolated-index add-all tree calculation in `git.py` rather than duplicating it, and
every observation gets its own enclosure-local temporary index so concurrent captures cannot unlink
each other's.

`memory_candidate_pair.py` owns the one read-only resolver that admits and re-proves an **exact
external-memory leaf pair**: repository identity, both work branches, both recorded bases, and
ancestry, with the memory source head checked against the recorded integrated landing for a completed
leaf. The ledger location it derives is a consumer detail — it is excluded from the contract digest and
is neither required to exist nor admitted as caller-supplied authority. Every refusal is a typed
`MemoryCandidatePairError` naming one field with bounded expected/observed facts and a
contract-addressed repair action.

Both cards' claims were already correct and their cited anchors were verified unchanged; they moved to
this route's card paths with their `path` metadata and governing-overview links repointed.

- The frozen strict future-code route identity, and the capture that derives it without touching the real index. [48]
- Currentness is exact equality of the whole bound route identity. [49]
- The exact-pair resolver, and the branch/base/ancestry proof it performs without mutation. [50]

## 260918-TSIP-L6 The Closeout Payload Names What It Counts, And The Preview Stops Crashing

Two defects on this route, both repaired in `260918-TSIP-L6`.

**`T71` — a count an operator cannot audit.** A refresh entry is either a *source* file
(`source_path`) or a regenerated **document** whose own path is the only identity it has
(`worktrees/modules/onboarding.py::_refresh_regenerated_documents` appends those with
`source_path: ""`). `closeout.py` read `source_path` alone, so those entries arrived as blanks and
the payload reported a `count` its own sample could not name. `_refreshed_onboarding_paths`
(`:127-141`) now names each entry by `source_path` **or** `onboarding_file`, and `_bounded_paths`
(`:115-126`) refuses to count a blank.

**`T54` — the closed payload's own address.** `_closed_result_payload` (`:595-627`) now emits
`contractPath` beside `status_payload`'s snake_case `contract_path`. Without it a closed closeout
declared no address in the spelling the guidance guard reads, so the guard had nothing to compare
against and guidance derived from whatever enclosure the *process* happened to hold was emitted
verbatim — a closeout for one leaf shipping a `nextStep` naming another master's contract.
`test_transaction_only_worktree_delivery.py:275-284` drives the real producer end to end.

**`T62`/`D49` — a preview that crashed on its own producer's output.**
`terminal_validation.py::terminal_result_blockers` (`:246-297`) built the drift-snapshot
expectation without `preview=result.preview`, which is the flag `_done_blockers` reads the pending
key off; this collection's producer answers a dry run with `would_remove` exactly as the worktree,
directory and provider collections beside it do. Without it the entry was neither reclaimed, nor
pending, nor reasoned, so `_blocker` (`:647-665`) raised and **every preview of a task that has a
drift snapshot crashed**. The repair is one keyword argument (`:285-292`), held by three cases in
`mcp/tests/test_terminal_blocker_reasons.py:382-480`.

## 260915-KS-L47 The Anchor Read Gets One Source Of Truth, And The Write Path Binds What It Stores

This route carries the modules whose citations this leaf's change set moved, and two of them changed
meaning rather than only line numbers.

**`memory/knowledge/anchors.py` gained one small public reader.** `read_anchor(connection,
repository_id, anchor_id)` is the same query, column list and decoder `get_anchor` already used, and
`get_anchor` now delegates to it. The reason is not convenience: the curator intake holds a read-only
connection and no `OpenedKnowledgeStore`, and re-deriving how an anchor row is decoded there would have
created a second source of truth for a stored identity -- exactly the shape that lets one anchor be
answered two ways. `get_anchor`'s own behaviour is unchanged.

**Its caller is the application layer's explicit-anchor-reuse repair.** `knowledge_curator_ingest.py`'s
`_require_stored_anchor` resolves a target-level `anchor_id` through this reader against the datasets
`_Source.anchors` carries, in candidate-then-baseline order, and refuses a supplied path, blob or
locator that disagrees with the stored row before any plan exists. The measured defect was a run that
reported `changed` and published a receipt naming symbol `other` while the stored realization cited the
`resolve_budget` anchor; after the repair the receipt, the stored claim and the public read agree by
construction, and a matching reuse still succeeds without adding an anchor row. The two refusal codes
are `anchor_reuse_mismatch` and `anchor_id_not_stored`.

**`worktrees/reopen.py` and `worktrees/modules/closeout.py` changed only by the citation projection**
this leaf's re-measurement performed: their ranges were rewritten to the extents their constructs
actually occupy, with no change of meaning. **`worktrees/modules/startup/`** likewise: the ranges in
`master_series_admission.py`, `series_attach.py` and `start_contract.py` were re-measured, not shifted.
`memory/knowledge/merge.py` was **not** touched by this leaf -- it is byte-unchanged and its
`_independent_insert_refusal` still refuses two independent insertions of one identity with equal
payloads.
