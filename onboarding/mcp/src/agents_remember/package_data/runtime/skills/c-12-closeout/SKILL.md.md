# c-12-closeout/SKILL.md

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated | 2026-09-10T06:03:57+00:00|
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview      | `../../../../../../overview.md` |

## Governing Overview

[mcp overview](../../../../../../overview.md)

## Purpose
This skill documents c-12-closeout as the shared closeout contract for approved Agents
Remember edits in repositories that use external memory. Applicable authority remains separate from
implementation approval: standalone, final, or unclear work uses the explicit developer route, while
accepted-series work can use its recorded delegated authority.

## Code Commentary

### Logic

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Cleanup is an explicit agent follow-up after landing and before handoff, including manual Git landing. | "Closeout does not mark the task" | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:211-219 |
| `c-12-closeout` skill defines worktree closeout tool usage and centralizes the closeout sequence. | `# c-12-closeout Closeout` | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:6-307 |
| `c-12-closeout` keeps commit approval separate from implementation approval, states the quality altitude ladder, and binds completed strict runs to one atomically replaced enclosure test-results report. | `## Approval Authority` | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:44-130 |
| Approval authority requires preview-first notify-and-stop for developer-gated closeout; an explicitly raised `closeout-approval` is the sole human commit gate. | `## Approval Authority`; `## Explicit Durable Closeout Gates` | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:46-130; mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:131-143 |
| `c-12-closeout` skill uses the missing-onboarding gate before code commit and routes missing sidecars to `c-05-create-or-update-onboarding-files` skill. | `## Preconditions` | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:144-166 |
| `c-09-git-worktree-manager` skill routes worktree closeout to `c-12-closeout` skill and retains worktree lifecycle, integration, and cleanup ownership. | `# c-09-git-worktree-manager Git Worktree Manager` | mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md:6-329 |
| Closeout delegates task completion to `lifecycle_finalize_task` after closeout, integration, PR merge/pull, and carryover. | "Closeout does not mark the task `Completed`" | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:212-212 |
| The L4 staging contract in Approval Authority: when code would commit **and the checkout carries the wrapper**, closeout resets the index, stages the whole task worktree, and gates exactly that staged content before any commit; a refusal leaves it staged, and `wrapper-unavailable` is the reported state for a checkout with no wrapper. | `## Approval Authority` | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:44-122 |
| The two staging refusals run before staging or ref movement: the code checkout must be the declared task worktree unless the declared route is a sanctioned branch-direct landing, and a worktree with unresolved merge conflicts (a merge, rebase, cherry-pick, or revert with unmerged entries) is refused so a blind stage cannot commit conflict markers. | "unresolved merge conflicts"; "unmerged entries" | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:104-106; mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:261-266; mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:110-110; mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:269-269 |
| The closeout order is now one external-memory six-step list: confirm the worker's targeted-check report and the curator's handoff, preview the enabled code and memory legs, call `worktree_closeout_apply`, commit code then the prepared memory content with its code attribution, refuse before mutation on a moved ref or an unresolved conflict, then update the task contract closeout state. | `## Closeout Order` | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:182-221 |
| The skill's own statement of the staging contract: a refused gate leaves the worktree fully staged and uncommitted, and because a retry must not inherit that index, each gate run begins with a reset and restages from the working tree, so resetting first recomputes the staged set under the ignore rules in force. | "Staging is **not** undone if the gate refuses." | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:97-106 |
| `DEFAULT_CRAP_THRESHOLD = 20.0` — the actual value behind every "the configured threshold" sentence in this skill, which names no number itself. | `DEFAULT_CRAP_THRESHOLD` | mcp/test_support/agents_remember_test_support/code_quality/crap_calculator.py:37-37 |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

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

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `Completed`; "Closeout does not mark the task" repointed to mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:212-212; mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:212-212. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: **complete curation inverts the doctrine this card recorded.** CAPS-R18@v1 removes the optional/narrow-curation sentences from the shipped instruction corpus and states the rule normatively — the full `memory_quality_check` operation runs as part of every leaf's curation at its contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every curator-actionable finding is repaired or escalated as blocked with its exact returned code, and closeout and integration **carry** the completed curation as a prerequisite while invoking nothing. Updated the transaction-boundary sentence: curation is carried, never invoked, so the full memory-quality result is complete before the transaction starts.
- 2026-09-10T09:50+02:00 — CCR-R12@v5 transaction-only curation against code commit `4bbe2c37b0fa70b07af4ddbc247aeee1f58343b0`: re-read the staging-refusal row against the rewritten skill: the `MERGE_HEAD` rationale is gone and the refusals are now stated as not-the-declared-task-worktree plus unresolved merge conflicts. Verification metadata remains closeout-owned.

- 2026-09-10T07:41:10+00:00: Generated citation repair: `# c-12-closeout Closeout` repointed to mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:6-307. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `## Preconditions` repointed to mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:144-166. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `Completed`; "Closeout does not mark the task" repointed to mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:211-211; mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:211-211. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `## External-Memory Order` repointed to mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:167-189. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `## Internal-Memory Order` repointed to mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:190-220. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-10T06:03:15+00:00 — Require the agent to preview and apply worktree cleanup after landing each enclosure, then finalize; cleanup refusals must remain visible in the handoff.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `Completed`; "Closeout does not mark the task" repointed to mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:332-332; mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:332-332. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `MERGE_HEAD` repointed to mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:412-412. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): updated the packaged closeout doctrine to the repository-profile authority model -- certificationProfile requirement, certification-profile-invalid refusal, and removal of the integrated-adapter/required-when-missing wording.


- 2026-08-31T20:30+02:00 — 260831-DER: synchronized the narrow direct-execution boundary and
  explicitly excluded ordinary master/series closeout and integration from the policy flag.

- 2026-08-29T08:52+02:00 — Added structured coherence validation to external-memory closeout
  admission. Verification remains closeout-owned.

- 2026-08-28T10:03:40+02:00 — Reconciled the current closeout explanation with Candidate A
  retirement; Dagger acceptance has no host Python wrapper or compatibility substitute.

- 2026-08-26T14:32+02:00 — No closeout behavior impact: refreshed the c-09 relationship citation
  after its ledger-history doctrine correction. Verification remains closeout-owned.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: merged input-total admission, journal controls, gate scope, direct landing, and explicit legacy-repair doctrine. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-14T11:25+02:00 — R39 curator: replaced embedded Agents Remember commands and thresholds
  with repository-resolved policy while preserving exact cadence and required-adapter refusal.
  Verification remains closeout-owned.
- 2026-08-14T06:32+02:00 — L23 synchronized runtime doctrine: closeout requires exact candidate
  route review, current lineage, Dagger-only quality, and task-addressed durable observation before
  irreversible commits. Verification remains closeout-owned.

- 2026-08-13T14:32+02:00 — L23 final curator pass: synchronized the Dagger-only acceptance rule,
  targeted leaf/focused versus once-per-master full altitude, mandatory explicit diff base,
  generated help, and diagnostic-only host execution. Verification remains closeout-owned.
- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: synchronized the
  host-managed full-gate default and explicit constrained-CI cap into the
  packaged closeout skill. Verification metadata remains pinned until closeout
  stamps L24.

- 2026-08-11T17:50+02:00 — 260731-EFA-L19 curator: recorded the single
  enclosure-owned `reports/test-results.md`, pass/fail full-output publication, interrupted-run
  preservation, and cleanup lifetime. Verification metadata remains pinned until governed
  closeout stamps the L19 code commit.

- 2026-08-10T07:30+02:00 — 260805-ARG-L1 developer expansion: documented wrapper-owned
  cheap-first execution and fail-closed exact/test-only proof reuse, full fallback, CI-fresh
  behavior, and the fresh-run diagnostic override. Verification metadata remains blank until
  closeout stamps the code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the quality altitude
  ladder (leaf `--targeted`; full wrapper once per master at the master
  integration gate, memory-capped; `memory_quality_check` per-leaf carve-out;
  loud skip-refusal shapes) and refreshed the section anchors to the post-L17
  ranges. Verification metadata stays pinned until closeout stamps the
  260731-EFA-L17 commit.

- 2026-08-05T21:40+02:00 — 260731-EFA-L16 curator: recorded the coding-guidelines read added to
  Preconditions and Boundaries rule 10 (developer ruling after task identifiers shipped in source
  comments through green rails on three leaves) — the change set's added lines are read against
  `system/coding-guidelines.md` before the preview, in-scope violations are repaired, and the rest
  are named findings at the commit-approval relay. Preconditions citation range extended to
  176-236. Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: replaced the `n/a` rows with exact
  heading anchors, converted the history `(L…)` citations, and rebound the lifecycle_finalize
  row; exact non-fixing check returns zero findings.

- 2026-08-01T09:45+02:00 — 260731-EFA-L4 curator: recorded the staging contract and **corrected the
  CRAP threshold, which this card had wrong**. The body asserted "at or above the configured
  threshold (30 by default)"; the real constant is `DEFAULT_CRAP_THRESHOLD = 20.0`
  (`code_quality/crap_calculator.py:83`), and the skill body itself names no number at all — it says
  "the configured threshold" at all six mentions. Added "The Gate Stages What It Certifies": when
  code would commit *and the checkout carries the wrapper*, closeout resets the index, stages the
  whole task worktree, and runs the wrapper over exactly that staged content, because every rail of
  the wrapper reads the index while closeout commits with `git add -A` — so created files were
  committed unread and deleted ones surfaced as `E902`. Recorded that the reset (not just `add -A`)
  is what makes a retry equal a first run, since git applies ignore rules only to paths it does not
  already track or hold staged; that a refusal deliberately leaves the worktree staged; and that the
  linked-worktree and conflicted-worktree refusals run **before** the reset because `git reset` drops
  unmerged entries and `MERGE_HEAD` and would otherwise disarm the conflict check silently. Reworded
  the guarantee from "without mutation" to "without any **commit**" in both the Logic paragraph and
  Invariants, since the index write is now the one mutation preceding the gate, and noted that a
  no-wrapper consuming repository runs no gate and reports `wrapper-unavailable`.
  **Verified the packaged copy against the canonical skill: `cmp` reports byte-identical, and all ten
  copies (canonical + packaged + eight harness mirrors) share sha256 `b6e9d764…4be7` — no
  sync drift.** Re-anchored five stale citations against the now-372-line source (L11-L31;L70-L96 →
  L11-L16;L30-L43, L31-L47 → L64-L69, L43-L87 → L111-L175, L50-L59 → L187-L198, L180-L184 →
  L288-L292) and added five rows for the new behaviour; the `c-09` row was re-checked and is
  unchanged. Verification metadata pinned until closeout stamps the commit.

- 2026-07-24T14:31Z — 260718-CHATS-L5I CRAP/commit-gate curation: documented the
  strict repository-wrapper gate that runs after preview/approval and before every
  closeout mutation. CRAP at or above the configured threshold (30 by default) is
  a mandatory failure, and missing interpreters/wrappers or nonzero wrapper exits
  fail closed without mutating code, memory, ledger, contract, or applied-gate
  state. This is the pathRules-eligible packaged copy synchronized from the
  canonical `skills/c-12-closeout/SKILL.md`; verification metadata remains pinned
  until the code commit.

- 2026-07-08T15:27+02:00 — 260707-HFX2-L6 (delegated closeout authority):
  frontmatter and Approval Authority guidance now distinguish explicit developer commit approval
  for standalone/final/unclear work from delegated accepted-series authority for subordinate
  orchestrated work. Subordinate managers/orchestrators may apply closeout after clean previews
  while recording the series authority in `intent_note`; final super/PR-carryover, raised
  `closeout-approval`, out-of-scope changes, red checks outside scope, unrepaired memory-quality
  blockers, and quo-vadis decisions remain developer stops. Sync-propagated bundle copy of the
  canonical `skills/c-12-closeout/SKILL.md`; no Python closeout enforcement changed. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L6 commit.

- 2026-07-08T00:00+02:00 — 260707-HFX-L11 curator activation (c-12 rewiring, R2): added the Seat
  note (manager -> builder -> reviewer -> curator chain: builder = code + report only, curator
  authors onboarding, this seat verifies). Reworded the Preconditions block, the External-Memory
  Order steps 1-2 and 5, and the Failure Conditions section so `check_missing_onboarding` and the
  changed-sidecar-body check are framed as verifying the curator's already-landed onboarding, not
  triggering inline authoring by the closing seat; a still-failing check now names "escalate to
  run/rerun the curator's pass" explicitly, never "write it here." Solo flat sessions with no
  separate curator seat are called out as unchanged. Doctrinal only —
  `check_missing_onboarding`/the changed-sidecar gate remain role-agnostic on-disk checks (see
  doctrine-review Note C: mechanized authorship attribution is a promotion-ratchet candidate, not
  landed here). Doctrine-only change set (60 files: 6 canonical `skills/` edits + 1 new template,
  each synced to 9 mirrors, 0 Python); sync-propagated (`scripts/sync-skills.py`) bundle copy of the
  canonical `skills/c-12-closeout/SKILL.md`. Verification metadata pinned — the branch
  `ar/260707-hfx-l11-curator-activation` has no commits yet (working-tree change); this pass is the
  memory side of the leaf, code commit is the closing seat's job.
- 2026-07-05T01:32+02:00 - L9 lifecycle convergence: the relay reference now names the l-01-agent-lifecycles orchestrator hand-off protocol. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-27T22:00+02:00 — Order fix (notify-then-report): corrected the Task 28
  notify-and-continue hand-off ORDER for the closeout commit and push hand-offs to
  **dry-run → notify (`lifecycle_turn_end_notification`, the last tool call) →
  report (the last prose) → stop**. The earlier notify-and-continue pass (entry
  below) had described report-before-notify; the corrected order ends the turn on
  the prose report (the notification returns immediately and does not render a
  prompt over the prose, so the report stays last). Parked block-and-wait
  `closeout-approval` / `push-approval` `lifecycle_gate` fallback unchanged (report
  still precedes the durable gate raise there). Sync-propagated
  (`scripts/sync-skills.py`) bundle copy of the canonical
  `skills/c-12-closeout/SKILL.md`. Verification metadata pinned.
- 2026-06-27T22:00+02:00 — Task 28 (notify-and-continue reframe): the closeout
  commit hand-off (and the push hand-off) now notify-and-continue through the new
  `lifecycle_turn_end_notification` tool — preview/dry-run, chat report, then
  `lifecycle_turn_end_notification(summary=…)` + STOP, which sets the new
  `awaiting-developer` state, surfaces a dashboard attention item, and returns
  immediately; the developer approves and the next turn's first AR tool call
  auto-resumes (`running`) and auto-dismisses the item before
  `worktree_closeout_apply` (no `lifecycle_resume`). Block-and-wait
  `closeout-approval` / `push-approval` `lifecycle_gate` and the operator inbox
  parked as the fallback. Sync-propagated (`scripts/sync-skills.py`) bundle copy
  of the canonical `skills/c-12-closeout/SKILL.md`; the Task 25 Server-Side Gate
  Enforcement block above is superseded historical context. Verification metadata
  pinned until closeout stamps the task-28 code commit.
- 2026-06-26T18:58+02:00 — No content impact: reviewed the source commit's
  generated skill-copy sync; the existing body already documents closeout as
  preview/dry-run first, chat report second, then `lifecycle_gate`, with apply
  only after developer resolution plus `lifecycle_resume`.
- 2026-06-26T17:21+02:00 — Task 25 regression fix: current closeout guidance now
  follows preview/dry-run first, chat report second, and `lifecycle_gate` third;
  apply remains after developer resolution plus `lifecycle_resume`.
- 2026-06-26T17:12+02:00 — Regression fix: current closeout and push gate
  guidance now describes `lifecycle_gate` as the single call that creates the
  durable gate, blocks the lifecycle, and waits for the developer decision or
  matching inbox response.
- 2026-06-26T14:27+02:00 — Task 25: updated current closeout and push gate guidance to use `lifecycle_gate` as the single lifecycle-gate junction call that creates the durable gate, blocks the lifecycle with the ask, and waits for the developer response. Older split-call history entries below are superseded historical context. Verification metadata pinned until closeout stamps the task-25 code commit.
- 2026-06-25T13:20+02:00 — Task 23/24: closeout gate instructions now rely on one normal five-minute `gate_response_wait` call instead of caller-managed timeout loops.
- 2026-06-25T07:17+02:00 — Task 19: closeout gate enforcement docs now use `gate_response_wait` and require consuming returned operator-inbox entries after reading them, so dashboard Chat responses do not disappear while dashboard approvals/rejections remain developer-attributed gate decisions. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: packaged closeout guidance now names leaf enclosure `series-contract.md` paths and says the closeout worklist is anchored by the leaf contract-recorded range. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00 — Dashboard task 14: clarified that closeout is commit-only; `lifecycle_finalize_task` later proves the landed edge, runs or verifies cleanup, and marks the current task plus immediate parent row complete. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-23T07:39+02:00 — Slice 09: extended the Server-Side Gate Enforcement onboarding to the full **raise → wait → clear** choreography — the raise now opens the ambient `lifecycle_block(kind="decision")` **and** the durable `gate_create(kind="closeout-approval")`, and the agent **always clears** with `lifecycle_resume` (the new step) before `worktree_closeout_apply`, since a chat "approved" does not propagate itself. Stated that **`closeout-approval` IS the commit gate** (the single commit-of-record for code/memory/ledger; no separate `commit-approval`), and that the push junction uses the `push-approval` gate kind. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: documented the new Server-Side Gate Enforcement section — opt-in `gate_create`/`gate_wait` choreography for dashboard-connected lifecycles, the developer-approved-gate-binds / never-self-approve rule, and the gateless-unchanged fallback. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-12T19:47+02:00 — Approval Gate adopted the `l-01-agent-lifecycles` skill gate protocol: the relay is its own turn ending with a prose approval question, and the apply tool is never invoked in the same turn as the relay.
- 2026-06-12T19:06+02:00 — Issue #83: the skill documents the committed-range worklist (last verified commit → HEAD, base-scoped), the gate-regardless-of-author rule for existing artifacts, the non-blocking `unonboarded` report, and the commit-gate relay of its count + sample.
- 2026-06-11T06:47+02:00 — Issue #62 worktree-only closeout: the skill no longer offers `direct_closeout_preview`/`apply` or the "small approved edits" direct-closeout guidance; the MCP Tools block lists only the worktree closeout pair and the intro states the worktree-only rule.
- 2026-05-29T07:36+02:00: Updated after `c-12-closeout` skill added a changed-file content gate — a changed source whose existing sidecar body was not updated this task fails closeout — plus the matching failure condition and boundary against metadata-only verification refreshes.
- 2026-05-28T15:24+02:00: Updated after `c-12-closeout` skill explicitly required route overview metadata, generated route index refresh, and clean `memory_quality_check` before memory commits. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-26T16:25+02:00: Created after closeout guidance was promoted from `c-09-git-worktree-manager` skill into a shared direct/worktree closeout skill.
