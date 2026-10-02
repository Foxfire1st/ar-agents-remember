# c-12-closeout/SKILL.md

## Governing Overview

[mcp overview](../../../../../../overview.md)

## Purpose
This skill documents c-12-closeout as the shared closeout contract for approved Agents
Remember edits in repositories that use external memory. Applicable authority remains separate from
implementation approval: standalone, final, or unclear work uses the explicit developer route, while
accepted-series work can use its recorded delegated authority.

## Code Commentary

### Logic

The generated closeout guidance names the existing comparison producer and carries its written/reused generation or refusal. Comparison recording remains review evidence; closeout remains report-only for that result and gains no semantic gate.

c-12-closeout owns worktree-only closeout sequencing. It previews and applies the exact
authorized code, memory-content, and ledger Git transaction through the task contract, preserving
the existing authority, conflict, ref-movement, and unfinished-leg recovery safeguards. Closeout
does not author onboarding or rerun worker/curator checks; it consumes their prepared content and
reports any failed or not-run evidence without relabeling it.

The transaction preview reports concrete commit inputs and conflicts without launching quality,
test, memory-quality, certification, curator-certification, or independent-review tools. Apply
stages and commits only the enabled transaction legs through the existing transaction owner.
Full code quality, full test suites, and requested reviews remain explicit
developer operations through their owning workflows.

The transaction-owned commit legs suppress automatic quality and test hooks. Ordinary explicit Git
hook policy outside closeout/integration remains unchanged. Closeout still refuses malformed
transaction inputs, unresolved conflicts, unauthorized authority, or unsafe ref movement, and it
never pushes automatically. A requested review keeps the lifecycle sealed complete finding list
and monotonic three-round rule.

After the code and memory are landed, including any required PR/carryover tail, the agent
must preview and apply `worktree_cleanup` for each finished enclosure before handoff. This
also applies after an authorized manual Git landing. A refusal leaves cleanup explicitly pending
with its concrete reason; `lifecycle_finalize_task` then verifies cleanup and completes the
current task and its immediate parent row.

On converted memory (the memory tree holds `knowledge/layout.json`) the skill says that both closeout tools ask the
mandatory invariant gate (MIK-R09) about the leaf's exact code and memory candidate (L37):

- `worktree_closeout_preview` answers `state: "knowledge-gate-refused"` instead of `"would-closeout"` while a
  worklist item is open, the worklist run is incomplete or the validator fails. `knowledge_gate.findingCount` and
  `knowledge_gate.findings` name what is open (at most 50 are listed, and `truncated` says so). It asks for no
  commit approval. A passing preview carries `knowledge_gate: {"state": "pass"}`.
- `worktree_closeout_apply` refuses the same leaf with the same findings before it claims the approval or commits
  either side, and judges the exact memory tree once more at the memory commit.
- The memory commit records exactly the tree the gate judged. A file written to the memory worktree while the
  closeout runs is either refused ("changed while the gate ran") or left as an uncommitted change.

### Conventions

- Preview before mutation and keep the preview/apply input immutable across retries.
- Keep code, memory-content, and ledger legs explicit and record each resulting commit.
- Preserve failed and not-run targeted/scoped evidence in the handoff and task report.
- Route onboarding authorship to c-05-create-or-update-onboarding-files; closeout verifies
  the prepared memory leg rather than patching onboarding inline.

### Invariants And Boundaries

- Closeout is a Git transaction, not a quality, test, memory-quality, certification, or review gate.
- The transaction does not create compatibility paths for missing certificates, reports, or suites.
- Authority, task contract, conflict, and ref safeguards remain mandatory.
- The closeout tool does not integrate or clean up; the agent must continue through the
  worktree-manager workflow and clean up each finished enclosure before handoff.
- Verification metadata and generated indexes remain coordinated follow-up work after the source and
  memory bodies are prepared; this card does not fabricate a stamp.

## CCR-R12@v5 Transaction Boundary

Current contract: closeout previews and applies the authorized code, memory-content, and ledger Git
transaction, preserves existing authority/conflict/ref safeguards, and leaves quality, test,
memory-quality, certification, and review operations explicit. Transaction-owned commit legs suppress
automatic quality and test hooks; ordinary explicit Git hook policy outside closeout/integration
remains unchanged. Workers and curators hand off targeted/scoped evidence with failed and not-run
states visible.

## Evidence

### Repo-Internal References

- Cleanup is an explicit agent follow-up after landing and before handoff, including manual Git landing. [1]

- `c-12-closeout` skill defines worktree closeout tool usage and centralizes the closeout sequence. [2]

- `c-12-closeout` keeps commit approval separate from implementation approval, states the quality altitude ladder, and binds completed strict runs to one atomically replaced enclosure test-results report. [3]
- Approval authority requires preview-first notify-and-stop for developer-gated closeout; an explicitly raised `closeout-approval` is the sole human commit gate. [4]
- `c-12-closeout` skill uses the missing-onboarding gate before code commit and routes missing sidecars to `c-05-create-or-update-onboarding-files` skill. [5]
- `c-09-git-worktree-manager` skill routes worktree closeout to `c-12-closeout` skill and retains worktree lifecycle, integration, and cleanup ownership. [6]
- Closeout delegates task completion to `lifecycle_finalize_task` after closeout, integration, PR merge/pull, and carryover. [7]
- The L4 staging contract in Approval Authority: when code would commit **and the checkout carries the wrapper**, closeout resets the index, stages the whole task worktree, and gates exactly that staged content before any commit; a refusal leaves it staged, and `wrapper-unavailable` is the reported state for a checkout with no wrapper. [8]
- The two staging refusals run before staging or ref movement: the code checkout must be the declared task worktree unless the declared route is a sanctioned branch-direct landing, and a worktree with unresolved merge conflicts (a merge, rebase, cherry-pick, or revert with unmerged entries) is refused so a blind stage cannot commit conflict markers. [9]
- The one external-memory closeout order restates step 4 as commit the code changes, then the prepared memory-content changes with their code attribution, keeping the transaction owner, pair identity and recoverable publication journal for each leg. [10]
- The caller-side implementation of that contract: `prepare_staged_code` runs both refusals before the mixed reset, then `git reset --mixed --quiet HEAD` and `git add -A`, and `gate_staged_code` then runs the strict targeted gate over the staged candidate. [11]
- The closeout order is now one external-memory six-step list: confirm the worker's targeted-check report and the curator's handoff, preview the enabled code and memory legs, call `worktree_closeout_apply`, commit code then the prepared memory content with its code attribution, refuse before mutation on a moved ref or an unresolved conflict, then update the task contract closeout state. [12]
- The skill's own statement of the staging contract: a refused gate leaves the worktree fully staged and uncommitted, and because a retry must not inherit that index, each gate run begins with a reset and restages from the working tree, so resetting first recomputes the staged set under the ignore rules in force. [13]
- `DEFAULT_CRAP_THRESHOLD = 20.0` — the actual value behind every "the configured threshold" sentence in this skill, which names no number itself. [14]

- On converted memory both closeout tools ask the mandatory gate; the preview never answers would-closeout for a refused leaf, and the commit records exactly the judged tree. [15]

### Cross-Repo References

No sibling repository evidence is needed for the skill itself.

No meaningful cross-repo references found.

## Series-Contract Notes

Closeout instructions now target the leaf enclosure `series-contract.md`; the root series contract is integration-branch state and is not the path used for leaf code/memory closeout.

## R39 Repository-Resolved Acceptance Doctrine

The packaged closeout skill is generic again and, since CCR-R22@v1 (L22, commit `685f83c44055`),
repository-owned: the exact configured repository certification profile
(`repositories.<repo-id>.certificationProfile`) declares the concrete executor, environment,
arguments, resource policy, retry semantics, evidence, and Gates 1-4 applicability; repository
memory such as `system/git-workflow.md` explains intent but is not alternate execution authority.
The cadence is one change-set acceptance at leaf closeout, no leaf-integration rerun, and one full
check at master integration. Every code-committing repository requires one explicit profile;
missing, ambiguous, invalid, or incomplete authority refuses as `certification-profile-invalid`
before repository execution. No seat may discover a fixed wrapper, infer a runner, or add a
default/compatibility/host fallback.
## 260821-CLIVE Closeout Admission And Recovery Doctrine

Every enabled code, memory, and ledger leg requires its own explicit nonblank immutable commit
message before claim, journal, worker, or Git authority. Blank required input is a typed no-effect
refusal, never a half-created generation or synthesized default. Apply starts or observes the
task-bound generation and returns; later status/control uses the exact journal generation and only
advertised retry/recover/cancel/revise/retire/supersede actions. A closeout gate, when explicitly
present, gates only admission and never task authoring or another sprint. Direct landing has the
same journal-first recovery discipline. Raw Git, repeat-from-scratch, reports, stale queue rows, and
permanent compatibility readers are prohibited; legacy repair is an explicit bounded tool.

## MCAR-L02 Coherence Admission

The packaged closeout doctrine requires `curator_coherence validate` for external-memory leaves
before closeout. Public memory readiness, door evidence, and closeout citation preflight use the
same structured validator; none may parse or search historical Markdown. A stale authority returns
to explicit prepare/publish rather than a compatibility path.

## Direct-Execution Boundary

Direct landing is the explicit policy-gated delivery path for a leaf intentionally implemented
without its own worktree enclosure. It is not a substitute for ordinary master/series closeout or
master-to-parent integration. Those lifecycle operations remain worktree/series operations and do
not require `directExecutionEnabled`; the existence of a root series contract alone does not select
the direct route.
