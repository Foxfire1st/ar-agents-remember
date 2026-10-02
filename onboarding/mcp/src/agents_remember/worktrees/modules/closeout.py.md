# mcp/src/agents_remember/worktrees/modules/closeout.py

## Purpose

Owns worktree closeout preview/apply behavior.

## CCR-R12@v5 Current Transaction Boundary

The normal closeout path is a recoverable transaction: preview describes candidate/source and
metadata work, apply checks explicit approval and Git/ref safety, commits the accepted code, then
delegates raw external-memory refresh and an attributed memory-content commit, then refreshes the disposable ledger cache. It does
not automatically run strict code quality, memory quality, selected certification, curator
coherence, or independent review. The explicit closeout approval/Git guard remains a transaction
control. The code commit and external-memory commit helpers use an already staged index without
invoking configured repository hooks; full suites remain an explicit developer request. Historical
quality-gate sections below describe pre-R12 behavior and are not prerequisites for this route.

## Code Commentary

### Logic

Closeout records code and memory-content commits, then publishes the exact contract state. External cache refresh is informational: it supplies no approval message, source-head expectation, recovery completeness cell, or integration output. Source-head validation uses `integrated_memory_content_commit`, and no-op finalization proves the existing two outputs without inventing a cache-maintenance commit.

A non-dry-run leaf entry refuses with `selected-closeout-operation-required` and zero gate starts unless it enters through the journal-selected certification operation. Preview and recording-only series behavior remain here. The selected lifecycle composition owns private code preparation, final memory certification and exact publication.

The existing publication helper receives already checked input, worklist, quality, route review and approval facts. It revalidates contract and candidate before claiming approval. Targeted code checks remain leaf-scoped; full-suite acceptance belongs to master integration. Coverage is diagnostic and production CRAP20 is a review trigger, not a mandatory changed-code floor.

Closeout admission now combines the immediate source-head check with the full task-derived
transitive lineage projection, and that projection self-heals a settleable stale break instead of
refusing it. `_validate_closeout_source_state(contract, *, dry_run)` runs
`heal_current_source_lineage` first — carrying a `behind > 0` break through the existing
`worktree_sync` transaction — and then re-proves the exact immediate source heads with
`_validate_closeout_source_heads` against the reloaded contract the sync left on disk. It returns
that healed contract, so lineage-first ordering means a source branch that moved while only its
ancestry is stale is settled by the sync rather than refused as a moved source. That source state is
checked at preflight and again on the last reversible line before approval claim. An unprovable break
escalates to the human developer, and a parent branch that moves during the long gate still refuses
before the approval is spent or any code or memory commit is created or the contract is published. The
transaction itself runs no code-quality gate and no memory preflight: it claims the gate approval and
then commits code and external memory and refreshes the disposable ledger cache, and leaf closeout then additionally re-resolves
the exact route-review record while series/master closeout deliberately bypasses only that leaf-owned
evidence, never the all-altitude candidate identity check. `_revalidate_candidate` threads the healed
contract on to the candidate comparison, so candidate identity is compared against the same identity
the lineage check proved; `_CloseoutResultFacts` and `_closed_result_payload` isolate the completed
result shape without moving mutation intent, Git, or contract-publication ordering. See "Closeout
Auto-Carry Of A Stale Source Break" below.

### Conventions

Accepted input, exact Git facts, and typed owner results stay distinct from disposable projections.

### Invariants And Boundaries

The ledger is a computed consumer cache; it cannot supply an additional Git output or lifecycle prerequisite.

### Todos

None recorded for the ledger-retirement boundary.

## Closeout Auto-Carry Of A Stale Source Break

`_validate_closeout_source_state` no longer refuses every stale transitive break. It calls
`modules/closeout_lineage.heal_current_source_lineage(contract, operation="closeout",
dry_run=dry_run)` and re-proves the immediate source heads on the returned identity:

- A stale edge with `behind > 0` — including every `diverged` edge, because `ahead` is the work
  branch's own normal work — is carried by the existing journaled `worktree_sync` transaction for the
  contract that owns each stale edge. It fast-forwards where the descendant has no own commits and
  merges where it does, then the reloaded contract is re-projected. A leaf that owns its own commit
  is the normal case, not a refusal.
- An `unavailable` projection (absent/unreadable contract, absent branch, organizational source that
  is not the sprint `integrationBranch`, or a comparison Git could not make) escalates to the human
  developer — a carried merge is mechanical, but an unprovable break is not settleable by an agent.
- A `dry_run` call refuses with the preview duty and mutates nothing; the applying call is what
  carries the break.
- A retained sync conflict (`sync-resolution-required`) surfaces as
  `source-lineage-sync-conflict`: the closeout completes for neither code nor memory, and the agent
  resolves in the exact reported sync worktree. A sync refused for any other reason surfaces as
  `source-lineage-sync-refused`; a sync that completed but left the lineage stale tells the caller to
  sync the remaining ordered parent edges.

The heal runs before the immediate-head check, so a source branch that moved while only its ancestry
is stale is settled rather than reported as a moved source. `_revalidate_candidate` now returns the
reloaded contract and both of its call sites thread it — `closeout_result` and the locked publication
callback in `_publish_closeout_candidate` — while `_closeout_entry` threads the same healed identity
from `_validate_closeout_source_state`. `dry_run` never mutates.

## At The Last Reversible Boundary

`_revalidate_candidate` recomputes the full Git candidate and compares it with the durable
operation's accepted `candidate_tree` for every altitude. A mismatch refuses before approval claim or
commit. The source state it re-proves is the healed identity above, never the stale pre-carry object.

R42 narrows this module back to coordination: `MemoryCloseoutOutcome` and
`prove_closeout_recovery_commits` now come from `worktrees/queue/closeout_recovery.py`. Normal closeout
and already-committed finalization still use the same typed result, but the proof of clean heads,
exact memory output identity, and memory ancestry now lives beside the other recovery primitives instead of
inside the coordinator.

The worklist is no longer dirty-tree-only (issue #83). `closeout_changed_paths`
unions the working tree with `committed_changed_paths(code_worktree,
code_base_commit, code_commit)` — the unverified committed range, excluding
synced-in parallel work and previous closeouts in the same worktree — and both
preview and apply consume that worklist. The onboarding plan receives the
working tier through `working_paths`, so missing sidecars block only for
working-tree paths while committed-range paths without onboarding surface as
the non-blocking `unonboarded` list. Both body gates receive
`contract_memory_verified_commit(contract)` (`memory_content_commit` → `memory_base_commit`) so sidecar work already
committed in the memory worktree still classifies honestly. When everything is
pre-committed and the tree is clean, `commit_if_dirty` returns the existing
HEAD and metadata stamps to that tip without creating an empty commit.

Payload lists that scale with transported history are bounded (issue #83):
`_bounded_paths` exposes count + sample capped at `PATH_SAMPLE_LIMIT`, applied
to `changed_code_paths`, `changed_code_paths_committed`, the
`onboarding_metadata_refresh` view (`required`/`unonboarded`; the blocking
`missing`/`unsupported` lists stay full), `sidecar_body_gate`,
`sidecars_attested_no_impact`, `refreshed_onboarding`, and
`unonboarded_changed_paths` in the apply payload.

The preview payload exposes the body gates' classifications
(`sidecar_body_gate` from `classify_sidecar_updates` and
`route_overview_body_gate` from `classify_route_overview_updates`), and the
apply path surfaces `sidecars_attested_no_impact`,
`route_overviews_attested_no_impact`, and
`route_overviews_stamped_without_body_review`. The current structured curator-coherence record's
exact no-content/no-route decisions are applied to those classifications before preview and
admission; a decision can clear only unchanged `stale` content, never an `untraced` body edit.
Still-recognized historical in-body markers and happenstance header stamps remain visible as
classification facts rather than becoming a second curator-report authority.

The entry points (`closeout_preview_payload`, `closeout_result`) and approval helper take the typed
`WorktreeArgs` dataclass. Closeout execution requires `args.closeout_input` to be the already
normalized `EffectiveCloseoutInput`; raw message fields no longer exist on this transport.
`closeout_result` asserts `args.contract_path is not None` before loading the contract, since
`WorktreeArgs.contract_path` is optional.

`closeout_result` obtains the required `EffectiveCloseoutInput` once at entry and explicitly threads
that same value through the commit phase, code recovery, external-memory refresh, memory commit,
and resume consumers. It constructs one `VerifiedChange` from the accepted code
commit and passes it to `closeout_external.external_closeout_commits`. That sole external-phase owner
threads the same change through onboarding, route-overview, entity-fingerprint, route-index, and
raw metadata refresh before using the accepted memory-content message and its code-attribution trailer for the memory commit. The subsequent cache refresh needs no commit message. No private consumer re-reads an optional transport field or invents shadow intent.

Server-side gate enforcement (slice 6b, generalized by 260703-L4): when the contract carries a
`lifecycle_id`, closeout reads the lifecycle's gate log via
`GateStore(observer_logs_root(contract.coordination_root))` — the same log the
dashboard writes — and `controlplane.evaluate_closeout_gate(..., policy=args.gate_policy)` refuses the closeout
unless a `closeout-approval` gate is `approved` by the developer or by a
policy-valid delegated orchestration decision (a model self-approval, owner
self-approval, missing required reviewer verdict evidence, or an
`open`/`rejected`/`applied` gate blocks; a gateless lifecycle consumes the approval and nonblank
note already persisted by the canonical journaled closeout operation). Both preview and apply payloads carry a `closeout_gate` block
(`enforced` / `permitted` / `gateId` / `reason`) for the commit-approval relay.

**Since 260731-EFA-L5 that enforcement is two functions, not one, and this is the section to read
before changing either — see "The Claim" below.** The old shape —
`_enforce_closeout_gate` checking near the top, `_mark_closeout_gate_applied` appending `applied`
after `write_contract` at the very end — is gone. `_mark_closeout_gate_applied` was **deleted, not
deprecated**.

Task 30 adds the re-closeout reset path for already-integrated leaves. When a
completed integration is legitimately re-closed, source-head validation accepts
the recorded integrated tips in addition to the original base tips. Preview
reports `integration_reopen.would_reopen` when the closeout would create or
transport new unlanded code or memory content. The exact prospective and produced-commit policy
now lives in `integration/closeout/integration_reopen.py`; this coordinator consumes that decision
and owns publication. The policy compares resulting code and memory-content commits against the
contract and recorded source branches; if either new content commit is not yet on its source
branch, closeout reopens the contract by clearing the integrated commit fields, setting
`integration_status` back to `not-started`, and leaving cleanup pending so
`worktree_integrate` can land the new tip normally. A clean no-op re-closeout
does not reopen integration and creates no cache-maintenance commit,
so a completed leaf stays completed when no new code or memory content exists.

## 260731-EFA-L17: The Leaf Contract And The Memory-Quality Carve-Out

Both closeout entry points now pass the leaf's targeted plan: `closeout_preview_payload`
(lines 362-434) and `closeout_result` (lines 941-1037) hand
`QualityGatePlan(mode="targeted")` to the preview/run, and `_gate_staged_code`
runs `run_strict_code_quality_gate(QualityGateTarget(code_worktree, worktree_group),
diff_base=..., plan=QualityGatePlan(mode="targeted"))` after the reset+stage. The enclosure
argument routes the complete test/quality transcript to the leaf's stable
`reports/test-results.md`; the successful closeout payload retains its `reportPath`. The preview summary and
the apply flow state the ladder explicitly: the leaf contract is `--targeted` (changed
files + reverse-import closure + derived test subset), the full wrapper is NOT a leaf
gate (once per master at the master integration gate with host-managed memory
by default), and
`memory_quality_check` stays a per-leaf closeout gate (`run_memory_quality_phase` in
`closeout_memory_quality.py`). A leaf closeout cannot skip its required checks: an uncovered changed
production module, a failed targeted run, or a missing wrapper refuses loudly.

## 260731-EFA-L4: The Gate Stages Before It Gates

`_gate_staged_code` now lives behind `_quality_gate_target(contract, args)`, which builds
`QualityGateTarget(code_worktree=contract.code_worktree, worktree_group=contract.worktree_group,
repository_id=contract.repo_name, profile_reference=args.certification_profile)`. Since
CCR-R22@v1 (L22, commit `685f83c44055`) every code-committing leaf requires one explicit
configured profile: the old `_quality_gate_executor(contract)` settings loader and the
`requires_integrated_acceptance(repo_name)` self-policy were removed, and the target now carries
the profile reference instead of an executor string. `_gate_staged_code` (target-based)
replaces the bare `run_strict_code_quality_gate(...)` call in `closeout_result`. It is four steps, and **the order is
the contract**:

1. `_refuse_outside_a_linked_worktree(code_worktree)`
2. `_refuse_conflicted_worktree(code_worktree)`
3. `require_git(code_worktree, ["reset", "--mixed", "--quiet", "HEAD"])`
4. `require_git(code_worktree, ["add", "-A"])`
5. `run_pre_commit_hook_if_configured(code_worktree)` → restage hook edits when configured
6. `run_strict_code_quality_gate(_quality_gate_target(contract, args), diff_base=diff_base)`

The commit side of the same contract is `commit_verified_staged`: it performs no `add -A` and
uses `git commit --no-verify`, so the configured hook is not restarted after the wrapper's final
pytest subprocess. This is intentionally different from ordinary `commit_if_dirty`, which still
stages and honors hooks for memory and other non-certified commits.

**Why stage at all.** Every rail of the wrapper reads the index: `derive_scope` lists what ruff and
pyright are given with `git ls-files`, and `diff_coverage` diffs the base against the tracked tree.
Closeout commits with `git add -A`, so until it staged first, any file the task **created** — as
opposed to edited — went into the commit without a single rail reading a line of it, and the gate
reported green having never seen it. Leaf 3's `abc7cbcc` shipped four files that way. The index cut
both ways: a path the task deleted stayed in `ls-files` until the deletion was staged, so ruff was
handed a file that no longer existed and took an `E902`. Staging first makes the gate's scope and
the commit's content one set by construction, rather than by a second enumeration that has to be
kept in step. Widening `derive_scope` to `--cached --others --exclude-standard` was the rejected
alternative: it would redefine the pre-commit tier, where staged content is the point, and could not
reach the coverage floor at all, since an untracked file has no diff against any base.

**Why the mixed reset.** `add -A` alone does not make a retry mean the same thing as a first run:
git applies ignore rules only to files it does not already track or have staged, so a path staged by
a refused attempt survives even after the retry adds it to `.gitignore`, and the commit carries it.
That is this leaf's own history — a `.dmypy.json` a type checker dropped in the worktree was staged
by a refused attempt, ignored on the retry, and committed anyway. `--mixed` is index-only, so the
tree the gate certifies is byte-for-byte what the task left on disk; each run recomputes the index
from the working tree under the ignore rules in force *now*.

**Why the reset goes after both refusals.** Ahead of the first it would inflict the exact damage
that refusal prevents — a mixed reset in a checkout somebody works in discards their `git add -p`
selection, and that refusal promises nothing in the checkout was touched. Ahead of the second it
would disarm it silently: `git reset` drops the unmerged index entries and removes `MERGE_HEAD`, so
`diff --diff-filter=U` would report nothing, the conflict refusal would never fire again, and
`add -A` would stage the `<<<<<<<` markers it exists to keep out of a commit. Reset-then-add is one
step wholly downstream of both checks.

**`_refuse_outside_a_linked_worktree`** tests git's own definition of a linked worktree —
`rev-parse --path-format=absolute --git-dir --git-common-dir` returning two different values — and
raises when they are equal. Not the contract's `kind`: `kind` is a label sitting next to the path,
while this constrains the path about to be written. A leaf contract whose `code_worktree` had been
pointed at the primary checkout would pass a `kind` check and still stage in somebody's working
repository, and a series contract genuinely pointing at a disposable worktree would be refused for
no reason. This is not hypothetical — `default_series_contract` sets
`code_worktree=code.repo_path` for a `kind: "series"` contract, i.e. the primary checkout itself,
and nothing else stops such a contract reaching `worktree_closeout_apply`.

**`_refuse_conflicted_worktree`** runs `diff --name-only --diff-filter=U` and refuses on any
unmerged path, reporting the count and up to `PATH_SAMPLE_LIMIT` names. This is a **behaviour
change, not a guard against the impossible**: `git add -A` over an unmerged index does not fail, it
*resolves* every conflict by taking whatever the working tree holds — the file with the markers
still in it — and closeout then committed that.

**No snapshot, no restore.** A refused gate leaves the worktree staged and commits nothing. The
staging is not undone because this is the task's own disposable checkout (which
`_refuse_outside_a_linked_worktree` makes true rather than assumed), nobody holds a partial staging
in it, and the reset means the next attempt does not inherit it anyway. The previous attempt at this
saved the index file aside and copied it back; that machinery is **gone rather than fixed** — it
could not survive `core.splitIndex` (the saved pointer outlives the `sharedindex.<sha>` that
`add -A` expires, leaving `status` exiting 128), it could not survive `SIGTERM`, which is how an MCP
server actually dies, and every guarantee it offered was about a person who is never in this
checkout.

**The preview says all of this.** `closeout_order` replaced its single
`"run-strict-code-quality-if-code-commit"` entry with four:

```
refuse-if-gate-would-run-and-code-checkout-is-not-the-tasks-own-worktree
refuse-if-gate-would-run-and-code-worktree-has-unresolved-merge-conflicts
reset-and-stage-whole-task-worktree-if-gate-would-run
run-configured-pre-commit-hook-once-and-restage-hook-edits
run-strict-code-quality-over-that-staged-content
commit-exactly-certified-code-index-without-rerunning-hooks
```

and the preview `summary` was rewritten to state that the staging step and its two refusals belong
to the gate — so they apply exactly when the preview reports `code_quality_gate.status ==
enforced`. A checkout carrying no wrapper runs no gate, stages nothing early, and commits as it
always has.

### Two smaller contract-integrity changes in the same leaf

- The preview's commit-approval block now calls **`recovery_guidance("request_commit_approval",
  tool="worktree_closeout_apply", ...)`** instead of `next_guidance` (the import changed with it).
  The emitted keys are identical; `request_commit_approval` is a `RecoveryOperation` because this
  payload is a gate rendered as a `FlexibleToolResponse`, not a lifecycle phase reaching
  `WorktreeSummary`.
- The end-of-closeout contract write splits in two: `amend_contract(replace(contract, <free-text
  commits, notes and strategies>), ContractCells(human_review_status="approved",
  closeout_status="completed", integration_status=..., cleanup=...))`. The four vocabulary cells go
  through the typed record so pyright checks them; `replace` carries only the fields that have no
  vocabulary to be checked against. The reopen logic itself is unchanged.

## Evidence

### Approval Claim And Mutation Evidence

Closeout keeps the early read-only gate check so an unsatisfied dashboard gate can refuse before
quality work. The actual approval claim remains under the gate-store lock after reversible quality,
lineage, route-review, and accepted-candidate checks and before the first journaled mutation intent
or Git action. A contract without a lifecycle gate still requires the approval claim and nonblank
note persisted by the canonical closeout operation; the retired synchronous chat/CLI apply path is
not a fallback.

Approval consumption and mutation recovery are deliberately separate facts. The gate claim proves
that this accepted operation may proceed; it does not prove that Git changed, retain a generation,
or make recovery cells authoritative. Per-leg mutation evidence or the exact canonical finalized-
contract hash decides closeout generation retention. A restart therefore reconciles the same
accepted effective input and repository evidence instead of inferring safety from the approval or
phase alone.
### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `closeout_preview_payload` asks approval for the actual code/memory transaction and reports cache refresh separately; a converted leaf the gate refuses gets the refused preview instead, which asks for no approval. [1]
- `_validate_closeout_source_heads` proves code and memory source tips against their recorded base or landed output. [2]

- `_amended_closeout_contract` records actual code/memory output and clears integration fields only when reopening. [3]

- `_recover_closeout_finalization` asks the recovery gate and re-proves existing output commits before exact contract publication. [4]

- Closeout refresh helpers provide sidecar metadata, route overview metadata, route index, and entity fingerprint updates before the memory commit. (`refresh_onboarding_metadata`; `refresh_route_overview_metadata_for_context`; `refresh_route_indexes_for_context`; `refresh_entity_fingerprints_for_context`) [5]
- Defines the `WorktreeArgs` dataclass that types every closeout entry point and helper. [6]
- The pure closeout-gate policy this module enforces (slice 6b). (`GateGuard`; `evaluate_gate`; `evaluate_closeout_gate`) [7]
- The gate policy threaded through `WorktreeArgs`. [8]
- `GateStore.claim_approval` — the compare-and-swap this module now spends an approval through: fold, policy verdict and the `applied` append inside one held `exclusive_access`. It is the only way to spend one; `_mark_closeout_gate_applied` was deleted. (`claim_approval`) [9]
- `CONSUMED_APPROVAL_GATE_KINDS` — why the `applied` snapshot this module writes is no longer reclaimed at any age, which is the other half of the replay fix. [10]
- The strict source-quality adapter decides applicability, executes the current worktree wrapper under the selected mode/executor, and fails before mutation. (`code_quality_gate_preview`; `requires_strict_code_quality`; `run_strict_code_quality_gate`) [11]
- `require_git` is the fail-closed facade over the shared Git runner; it preserves raw runner decoding and makes only raised diagnostics transport-safe. [12]
- Closeout imports the self-healing lineage guard that carries a settleable stale break through the existing sync. (`heal_current_source_lineage,`) [13]
- Closeout's import block takes the queue preview and recovery owners and imports no code-quality gate; the staged-quality owner `gate_staged_code` lives only in its own module. [14]

- Closeout revalidates the accepted candidate tree and refuses a candidate that moved after admission before publishing; the reversible code-quality preflight no longer exists in the transaction. (`_revalidate_candidate`; `closeout_result`) [15]

- The extracted owner binds and certifies the exact staged candidate. (`gate_staged_code`) [16]
- The closeout transaction runs no code-quality gate and no memory pre-refresh; the memory-quality phase owners remain standalone in their own module. (`run_memory_quality_phase`; `combine_memory_quality`) [17]
- `recovery_guidance` and the `RecoveryOperation` vocabulary the commit-approval gate belongs to, plus `status_payload`. [18]
- `ContractCells` and `amend_contract` define the contract-cell amendment API. [19]
- Closeout uses that amendment API for its contract write and avoids the forbidden `replace` keyword. (`_amended_closeout_contract`) [20]

### 260815-DAG-L3 Claim/Certification History, Replaced By Journal Evidence

The commit worker no longer claims or certifies a queue candidate. The lifecycle owner atomically
transfers the exact first-ready waiting door into the enclosure-external journal before launching
the worker. Code, memory-content, and contract results are journaled against that immutable operation
generation; recovery re-proves retained journal and Git evidence rather than patching a queue row.

### Cross-Repo References

No separately configured cross-repository implementation governs this file; any external-memory repository is addressed by the task contract.

No additional cross-repository evidence applies.

## The Closeout Preview Reads The Same Completion Gate As The Apply (260831-LOCR-L34)

`closeout_preview_payload` cit:([`closeout_preview_payload`], mcp/src/agents_remember/worktrees/modules/closeout.py:235-292) now calls
`require_closeout_publication_authority(contract)`
cit:([`require_closeout_publication_authority`], mcp/src/agents_remember/worktrees/series_closeout.py:33-57) immediately after `refuse_series_workbench_commit`, so **the preview refuses
exactly what the apply refuses**.

**Why this was a real defect, not a tidy-up.** The atomic-completion gate (master `Completed`, every
canonical leaf landed) existed only behind the apply, in `publish_closeout_under_authority`. A partial
master's preview therefore answered `state: "would-closeout"` with a plan, and the apply then refused
on every completion blocker — 19 of them on LOCR. That misleading plan is what led a human to write a
false note about the series being closable. The gate is now one definition with two callers (the
preview and the apply), and its first statement is `if contract.kind == "leaf": return`, so **no leaf
closeout preview changes** — a leaf owes nothing there, exactly as it owed nothing to the old
publication wrapper.

This is instance 1 of the preview/apply parity invariant recorded on the `worktrees/overview.md`
route; the full instance inventory lives there and in `memory_quality/overview.md`. The reason it
belongs in memory at all is that a preview is a *plan* and plans are read by humans and by agents:
when the two surfaces are two implementations, the plan is a promise nobody enforces.

## A Checkpointed Series Passes Its Own Landed Source Head (260831-LOCR-L30)

`_validate_closeout_source_heads` asserts that the live source-branch head is one *this contract's
own landing legitimately produced*: the recorded base, plus the commit the contract records as
landed. That set is computed by `_landed_source_heads(contract, base, integrated)`
cit:([`_landed_source_heads`], mcp/src/agents_remember/worktrees/modules/closeout.py:167-181) — the
former `_completed_integration_source_heads`, renamed because its condition is no longer about
"completed" integration.

The condition widened from `contract.integration_status == "completed"` to
`contract.integration_status in {"completed", "checkpointed"}`
cit:(["contract.integration_status in {\"completed\", \"checkpointed\"} and integrated"], mcp/src/agents_remember/worktrees/modules/closeout.py:179-179).

**Why the old form was wrong.** A checkpoint also moves the source branch forward, and it records the
commit it moved the branch to. Keying the expected set on `completed` alone therefore made the
checkpoint's *own* recorded landing look like foreign movement, and the next closeout refused with
`RuntimeError: code source branch moved since task start` — AR's own landing reported as an outside
move. A source that genuinely moved anywhere else still matches neither head and is still refused;
the widening admits exactly one additional head, the one the checkpoint recorded.

**Why the refused party is exactly the checkpointed master.** `closeout_result`
cit:([`closeout_result`], mcp/src/agents_remember/worktrees/modules/closeout.py:715-749) is the single closeout entry point and dispatches on nothing; `_closeout_entry`
cit:([`_closeout_entry`], mcp/src/agents_remember/worktrees/modules/closeout.py:855-878) reaches the
validator for **series** contracts too — its only `kind` branch (the leaf-only binding refusal) is
`if contract.kind == "leaf":` at line 831 and returns early for leaves rather than excluding series.
And a checkpointed contract is always `kind == "series"`: `integrate.py:456` refuses anything else
with "checkpoint landing is defined only for an atomic series contract". So the path that used to
refuse is the checkpointed series' own next closeout.

### The Remaining `== "completed"` Sites Are Deliberate

`_landed_source_heads` and `guidance.py::_post_integration_phase` were the only two sites that
needed widening, because they are the two that ask *"did a landing this contract performed move the
ref?"*. Every other `integration_status == "completed"` in the tree asks *"is this contract
complete?"*, and for that question a checkpoint must read as **not complete** — that is the whole
point of the state. They are reviewed and deliberately unchanged; do not "fix" them:

- `application/next_step.py` holds two adjacent dry-run gates that bracket the checkpoint correctly.
  The `worktree_integrate` gate keys on `integration_status != "completed"`
  cit:(["and contract.integration_status != \"completed\""], mcp/src/agents_remember/application/next_step.py:217-217), so a checkpointed
  series still gets "Integration dry-run verified — ready to integrate", which is right because it
  integrates again when it completes. The `lifecycle_finalize_task` gate keys on
  `integration_status == "completed"`
  cit:(["and contract.integration_status == \"completed\""], mcp/src/agents_remember/application/next_step.py:229-229), so a checkpointed series does **not** get the "stop
  before reclaiming the worktrees" hint, which is also right because it is not terminal.
- `worktrees/integration/organizational_completion.py:447` and
  `memory_quality/memory_candidate_pair.py:95` / `:112` read completion as the predicate for their
  own facts; a checkpoint is not that fact.
- `worktrees/integration/atomic_series_landing.py:111` and
  `worktrees/activation/atomic_series_activation.py:517` treat `completed` or a terminal `cleanup`
  as the terminal-series signal, which a checkpointed series is not.
- `worktrees/integration/lifecycle/lifecycle_completed_disposition.py:138` and
  `application/task_docs/task_unstarted_evidence.py:545` likewise assert completion; a checkpoint
  must not satisfy them.
- `worktrees/modules/guidance.py:267` is the `completed` branch of `_post_integration_phase`; its
  sibling `checkpointed` branch at `:307` is what the checkpoint uses instead.

## 260731-EFA-L1 Current Commit-Gate Delta

The three quality-gate call sites — `code_quality_gate_preview` in `closeout_preview_payload`, and
`code_quality_gate_preview` plus `requires_strict_code_quality` in `closeout_result` — now pass
`contract.code_worktree` instead of `contract.repo_name`. The gate is no longer hard-coded to this
repository: applicability is decided by whether the target checkout carries
`mcp/test_support/agents_remember_test_support/code_quality/check.py`.

**This call site is type-unsafe by construction.** `contract` is unannotated here, so Pyright does
not object if a `str` repository name is passed where a checkout `Path` is expected — and the
failure is silent, because a relative path built from a name is not a file, so
`requires_strict_code_quality` returns `False` and the mandatory gate never runs.
`test_worktree_closeout_quality_gate.py::test_closeout_hands_the_gate_the_code_worktree_not_the_repository_name`
spies on the actual argument at both entry points for exactly this reason.

The payload's `code_quality_gate.status` now distinguishes `enforced`, `no-code-commit`, and
`wrapper-unavailable`; the last means the commit still happens and the payload states it was not
quality-checked.

## 260718-CHATS-L5I Incremental Commit-Gate Delta

Preview exposes the strict quality requirement and places it first in `closeout_order`. Apply
recomputes whether code would commit, runs the gate before `commit_if_dirty`, and returns the gate
result in the closeout payload. **Since 260731-EFA-L4 the apply path calls `_gate_staged_code`
rather than `run_strict_code_quality_gate` directly, and the single `closeout_order` gate entry
became four** — see the L4 section above. `run_strict_code_quality_gate` remains imported and is
still what actually runs the wrapper, one step inside `_gate_staged_code`.

## R39 Closeout Altitude And Candidate Policy

Leaf closeout alone stages and runs targeted acceptance. Series/master closeout refuses dirty code
and records already-landed HEAD without acceptance. Every altitude binds an accepted candidate
tree into durable operation input and rechecks it after long quality work before approval claim;
non-leaf route review is intentionally not required. Agents Remember requires its self-owned
wrapper, so deleting it refuses instead of becoming a consumer no-adapter result.

## R43 Candidate Identity Typing

`closeout_result` still admits only a non-empty accepted candidate tree before quality, mutation
intent, or Git. After that existing admission, the coordinator narrows the optional
typed field with `cast(str, args.candidate_tree)` instead of carrying a redundant second runtime
refusal. Revalidation and commit ordering are unchanged.

## 260815-DAG-L4 Integration-Authority Impact

Task-derived integration refs remain mechanically non-ordinary: repository defaults, sprint supers,
and active atomic-series refs are censused across code and external memory. Closeout admission is the
exact door plus journaled operation generation; protected-ref landing and terminal capabilities stay
with their own owners. Stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## 260815-DAG Master Full-Gate Repair

Imports updated to the moved queue/integration packages (`worktrees/queue/*`, `worktrees/integration/integration_branch_authority`); the closeout quality-facts composition was extracted into `_closeout_quality_facts` — the attestations, code-quality gate, memory-quality preflight, and strict-quality requirement for both the resuming and fresh paths.

## 260821-CLIVE-L1 Closeout Coordinator

Closeout execution now requires journaled mutation authority and one validated `EffectiveCloseoutInput`. Entry validates the accepted plan before recovery or mutation and returns the typed value to the coordinator; preview renders that plan, code commit and external consumers receive that value explicitly, and external-memory content and cache refresh are owned by `closeout_external.py`. Immediately before publication, the locked callback reloads the contract and rechecks contract identity, authority, workbench state, and the accepted candidate so validation cannot be separated from mutation by a stale object. The old generated ledger subject, raw message fallbacks, optional private guards, and shadow intent are removed. Contract finalization publishes the exact canonical hash, allowing verified-existing/no-op completion without fabricated Git evidence. The operation journal records lifecycle evidence; any later queue refresh is a disposable scheduling effect, never certification.

## 260821-CLIVE-L2 Current Contract

The current source seams include `closeout_changed_paths`, `closeout_preview_payload`, `closeout_result`. Closeout uses closed admission, immutable generation input, root-journal mutation evidence, and same-generation recovery. Missing commit-message or other input errors are refused before authority; retries cannot amend accepted intent or strand work behind queue state.

### Reconciled Source Evidence

- The current module exposes `closeout_changed_paths`, `closeout_preview_payload`, `closeout_result` at this ownership boundary. [21]

- The source-state boundary self-heals a settleable stale break and re-proves the immediate heads on the healed contract; candidate revalidation returns that healed contract. (`_validate_closeout_source_state`; `_validate_closeout_source_heads`; `_revalidate_candidate`) [22]
- The expected source heads a contract's own landing may have produced, now covering a checkpoint's recorded move. (`_landed_source_heads`; `contract.integration_status in {"completed", "checkpointed"} and integrated`) [23]

- The current module exposes `closeout_changed_paths`, `closeout_preview_payload`, `closeout_result` at this ownership boundary. [24]

- The source-state boundary self-heals a settleable stale break and re-proves the immediate heads on the healed contract; candidate revalidation returns that healed contract. (`_validate_closeout_source_state`; `_validate_closeout_source_heads`; `_revalidate_candidate`) [25]
- The expected source heads a contract's own landing may have produced, now covering a checkpoint's recorded move. (`_landed_source_heads`; `contract.integration_status in {"completed", "checkpointed"} and integrated`) [26]

- The single closeout entry and the entry helper that reaches the validator for series contracts too. (`closeout_result`; `_closeout_entry`) [27]
- The closeout entry threads the healed contract through preflight, the gate's preflight and the locked publication callback. (`closeout_result`; `_publish_closeout_candidate`; `_closeout_entry`) [28]

## 260821-CLIVE Journal-Owned Claim Boundary

This commit worker no longer claims or certifies a mutable queue candidate before/after its Git and
contract work. The lifecycle-operation owner transfers the exact first-ready waiting door into the
root journal and launches this worker with immutable accepted input. The worker continues to
revalidate contract, review, tree, quality, and repository authority and publishes exact commits
and contract finalization; recovery/certification is inferred from the retained journal and Git
evidence, never repaired through a stale row.

## MCAR-L02 Shared Coherence Preflight

`_memory_quality_before_refresh` now requires the current structured curator-coherence authority
before citation checks or expensive code validation and records its exact record digest and
delivery attempt. This is the same validator public memory readiness and door evidence call, so a
hardcoded legacy report cannot pass one boundary and fail another. The validated no-impact
projection is threaded through preview, body-gate admission, and `ExternalCloseoutEvidence`, so
the post-code-commit memory refresh consumes the same decisions instead of re-deriving them.

## MCAR-L03 Preview, Apply, And Recovery Pairing

Preview obtains the pair from the current coherence authority and reports it. Normal completed
apply carries that same accepted pair. Post-commit finalization recovery re-proves the exact
contract-addressed pair directly, because pre-commit candidate-tree evidence is expected to become
stale after commits; it never re-resolves from repository id. The pair policy lives in the focused
closeout pairing module rather than adding another resolver to this orchestration module.

## Governing Overview

[Governing route overview](overview.md)

## 260918-TSIP-L6 The Refreshed-Onboarding Census, And The Closed Payload's Own Address

**`T71` — a list that counted entries it could not name.** A refresh entry is either a *source*
file (`source_path`) or a regenerated **document** whose own path is the only identity it has:
`worktrees/modules/onboarding.py::_refresh_regenerated_documents` appends those with
`source_path: ""`. Reading `source_path` alone turned every document entry into a blank string, so
the payload reported a `count` with most entries unnamed. `_refreshed_onboarding_paths`
(`:127-141`) now names each entry by `source_path` **or** `onboarding_file`, and `_bounded_paths`
(`:115-126`) refuses to count a blank: a `count` an operator cannot audit is not a report.

**`T54`'s producer half — the closed payload declares its own address.**
`_closed_result_payload` (`:595-627`) now emits `contractPath` alongside `status_payload`'s
snake_case `contract_path`. Without it a closed closeout declared **no** address in the spelling
the guidance guard reads (`application/tool_response.py::bound_next_step` reads
`contractPath`/`enclosurePath`), so the guard had nothing to compare against and guidance derived
from whatever enclosure the *process* happened to hold was emitted verbatim — which is how a
closeout for one leaf shipped a `nextStep` naming another master's contract. The producer is
driven end to end by `mcp/tests/test_transaction_only_worktree_delivery.py:275-284`; the guard's
own four cases are in `mcp/tests/test_response_address_binding.py`.

## 260928-MIK-L37 The Closeout Asks The Mandatory Gate Before It Claims Anything, And The Preview Says What The Apply Will Do

On converted memory three places of this module ask the mandatory invariant gate (MIK-R09), through
`closeout_external` (decision record DEC-TJ0CX7; invariants INV-HWAWFT and INV-WV1YQE):

- **The apply's preflight.** `closeout_result` calls `refuse_ungated_candidate(contract, accepted_candidate_tree)`
  after `_revalidate_candidate` and before `_publish_closeout_candidate`. A closeout refused here claims no approval
  and commits neither side. The exact memory tree is judged again at the memory commit, after the code commit
  (`_closeout_commit_phase` commits the code first): a refusal there leaves the code commit made and no memory
  committed, and a rerun takes that commit as it is and completes once the gate passes.
- **The preview.** `closeout_preview_payload` calls `candidate_gate_verdict` after the publication checks. When the
  gate refuses, it returns `_gate_refused_preview` instead of the plan:
  - `state: "knowledge-gate-refused"` (`GATE_REFUSED_PREVIEW`), never `would-closeout`;
  - `knowledge_gate: {state: "refused", findingCount, findings, truncated}` with at most `MAX_PREVIEW_FINDINGS` (50)
    findings;
  - `commit_approval_required: false`, `nextOperation: "continue_work"`, no `nextTool`, and a `nextStep` that says to
    answer the findings, rerun `memory_quality_check` and preview again.

  `_closeout_entry` returns that preview with return code 2. A passing preview of a converted leaf carries
  `knowledge_gate: {"state": "pass"}`; an unconverted leaf's preview carries no such block. The preview writes
  nothing, and the gate's memo lets the apply that follows reuse its verdict. The preview evaluates the gate itself
  whenever the memo holds no verdict for the same inputs; that is sound while the preview is called only on explicit
  request and nothing polls it (assumption ASM-NJ9P83, which the decision record DEC-TJ0CX7 links as a reason to
  reconsider).
- **A recovered closeout.** `_recover_closeout_finalization` calls `require_gated_recovery` before it proves the
  recovered commits, so the contract is finalized only for a memory commit the gate passes.

- The apply asks the gate before it publishes the closeout. [29]
- The preview asks the same verdict and answers the refused preview. [30]
- The refused preview: the findings, no approval, no next tool. [31]
- A refused preview returns code 2. [32]
- A recovered closeout is finalized only for a gated memory commit. [33]
- The preview answers what the apply will do. [34]
- An unconverted leaf's preview carries no gate verdict. [35]
