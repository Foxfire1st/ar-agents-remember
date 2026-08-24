# c-12-closeout/SKILL.md

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-24T15:04+02:00 |
| lastVerifiedCommitHash |  `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate |  2026-08-24T15:28:18+02:00|
| governingOverview      | `../../../../../../overview.md` |

## Governing Overview

[mcp overview](../../../../../../overview.md)

## Purpose

This skill documents `c-12-closeout` skill, the shared closeout contract for approved Agents
Remember edits in repositories that use external memory. As of HFX2-L6, "approved" means the
applicable authority for the context: explicit developer approval for standalone/final/unclear
work, or recorded delegated series authority for subordinate accepted-series work.

## Code Commentary

### Coding-Guidelines Read (260731-EFA-L16)

The Preconditions section now also requires reading the change set's added lines against the
memory layer's `system/coding-guidelines.md` before the closeout preview, and Boundaries rule 10
forbids closing out a guideline contradiction that was neither repaired in scope nor named at the
commit-approval relay. Rationale: the wrapper certifies lint, types, tests, coverage, and CRAP —
it does not read for guideline adherence. Three leaves had already shipped source comments
carrying task/leaf identifiers (forbidden by the guidelines' Source Comment Scope) through fully
green rails; the violation surfaced only when the developer spotted it in review. The named
failure modes the new read targets are exactly that class: task identifiers in shipped comments,
new positional boolean flags, `object`-typed boundary parameters, and oversize files growing
again. In the reviewer chain this read belongs to the reviewer seat's evidence.

### Seat Note (260707-HFX-L11)

In the manager -> builder -> reviewer -> curator chain, onboarding authorship happens in the
curator's prior pass (`l-01-agent-lifecycles` `roles/curator.md`), not in this closeout seat. A
new "Seat note" at the top of the skill body states this explicitly. Every place the body used to
read as "create"/"update onboarding here" was reworded to **verify** the curator's already-landed
output: `check_missing_onboarding` and the changed-sidecar-body check confirm the curator's pass,
they are not the trigger for the closing seat to author onboarding inline. A check that still
fails after the curator pass is a closeout failure — escalate to run/rerun the curator's pass,
never patch onboarding from the closing seat. A solo flat session with no separate curator seat is
called out as unchanged: it still runs `c-05-create-or-update-onboarding-files` itself before
closing out. This is a doctrinal binding only — `check_missing_onboarding` and the changed-sidecar
gate remain role-agnostic on-disk checks (they do not verify who authored a sidecar); see the
doctrine-review Note C on this leaf for the promotion-ratchet candidate ("mechanize when
authorship can be attributed").

### Logic

`c-12-closeout` skill owns closeout sequencing for worktree-backed tasks. It
uses the worktree closeout preview/apply tools against the task contract,
requires a non-mutating preview before real commits, requires applicable closeout
authority with an intent note, runs the package-local missing-onboarding gate,
and runs the leaf change-set-scoped Dagger quality contract before any code, memory, ledger,
contract, or applied-gate **commit**. The full Dagger graph is NOT a leaf gate: it runs once per
master at the master integration gate. Every Agents Remember acceptance run requires the explicit
task-derived diff base; generated Dagger help is the public argument contract. Host pytest and
direct wrapper runs are refused and cannot replace or receive fallback from Dagger acceptance.
`memory_quality_check` stays a per-leaf closeout gate. The wrapper's CRAP threshold is
mandatory by default: a function scoring at or above the
configured threshold fails closeout.
Every completed strict wrapper run also atomically replaces the owning enclosure's
`reports/test-results.md`: success returns `reportPath`, failure writes the complete transcript
before refusing, and an interrupted retry leaves the preceding completed result intact. The file
is operational enclosure state, not content for either Git worktree, and cleanup/abandon removes
it with the shared reports directory.
That threshold is **`DEFAULT_CRAP_THRESHOLD = 20.0`**
(`mcp/src/agents_remember/code_quality/crap_calculator.py`), not 30 — the skill body
itself never names a number, it says "the configured threshold" throughout, and this
card previously asserted 30. After that gate passes, closeout commits code, refreshes affected
onboarding metadata, entity fingerprints, route
overview metadata, and generated route indexes, runs the full memory quality
check, commits memory content only after the quality gate is clean, prepends the
`C2 | M2` mapping to `memory.md`, and commits the ledger update.

Closeout is worktree-only: every change affecting the code repo runs through a
`c-09-git-worktree-manager` dual worktree (code + memory), and the former
direct-closeout usage block was removed (issue #62). Worktree closeout is used
when `c-09-git-worktree-manager` skill created or attached a task contract;
`c-09-git-worktree-manager` skill then owns later integration, lifecycle
finalization, cleanup, and task-document completion. Closeout does not mark the
task `Completed`; `lifecycle_finalize_task` does that after landing and
carryover are complete.

### The Gate Stages What It Certifies (260731-EFA-L4)

L4 changed *when* the wrapper runs relative to the index, and the skill body now says so in four
places: Approval Authority cit:([`## Approval Authority`], mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:44-122), both memory-order lists cit:([`## External-Memory Order`, `## Internal-Memory Order`], mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:268-348), and Failure
Conditions cit:([`## Failure Conditions`], mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:324-390).

Every rail of the wrapper reads the **index** — `derive_scope` lists ruff's and pyright's files with
`git ls-files`, and `diff_coverage` diffs the base against the tracked tree — while closeout commits
with `git add -A`. Those two facts disagreed. A file the task **created** was committed without a
single rail reading a line of it, and a file it **deleted** stayed in `ls-files` until the deletion
was staged, so ruff was handed a path that no longer existed and took an `E902` for it.

So when code would commit **and this checkout carries the wrapper**, closeout now resets the index,
stages the whole task worktree, and runs the wrapper over exactly that staged content. That index
write is the **one mutation that precedes the gate** — which is why the failure guarantee is now
worded "fails without any *commit*" rather than "without mutation".

- **The reset is not cosmetic.** `git add -A` alone does not make a retry mean the same thing as a
  first run: git applies ignore rules only to paths it does not already track or hold staged, so a
  file staged by a refused attempt stays staged even after the retry adds it to `.gitignore`, and
  the commit carries it. `git reset --mixed` recomputes the index from the working tree under the
  ignore rules in force at that moment. `--mixed` is index-only, so no file content is touched.
- **A refusal leaves the worktree staged, and nothing undoes it.** That is the intended end state,
  not a gap: the checkout is the task's own disposable worktree (created by `worktree_start`,
  destroyed by `lifecycle_finalize_task`), so nobody is holding a partial staging in it, and the
  next run's reset restages from the working tree regardless.
- **Ordering is load-bearing.** Two refusals guard the staging step, so they run where the gate runs
  and, critically, **before the reset**. Closeout refuses when the code checkout is **not** a task
  worktree (git's own test: `--git-dir` and `--git-common-dir` differ in a linked worktree and are
  the same path in a repository's own checkout, which is what `default_series_contract` records),
  and when the worktree has unresolved merge conflicts. Running the reset first would disarm the
  second **silently**: `git reset` drops the unmerged index entries and removes `MERGE_HEAD`, so the
  conflict probe would find nothing and `add -A` would go on to stage the `<<<<<<<` markers.
- **A consuming repository carrying no wrapper is unaffected.** It runs no gate, is not staged early,
  and reaches the ordinary commit step's own `git add -A` exactly as before. The preview reports that
  state as `wrapper-unavailable` rather than passing it off as checked. Neither refusal applies to it.

### Quality Altitude Ladder (260731-EFA-L17/L23)

The skill body states one accepting boundary per altitude: leaf closeout runs targeted Dagger
acceptance exactly once before committing; leaf integration reuses that certified commit without
rerunning acceptance; clean series/master closeout never creates a code commit or reruns
acceptance; master integration runs full Dagger acceptance exactly once. Ordinary push hooks and
pull-request checks remain deterministic non-test rails. Host pytest and direct-wrapper execution
are refused. `memory_quality_check` stays a per-leaf closeout gate. A leaf closeout
that tries to skip its required checks (an uncovered changed production module, a failed
targeted run, or a missing wrapper) is refused loudly, never passed silently.

The same section binds the test-evidence lifetime: one complete transcript per enclosure at
`reports/test-results.md`, atomically replaced only by a completed run, with no timestamped copies
and no promotion into code or memory history.

### Cheap-First And Delta Retry Contract (260805-ARG-L1)

The packaged closeout skill now records wrapper-owned retry behavior. Cheap deterministic rails
precede pytest. Only a fresh pytest pass followed by a coverage-derived refusal can seed a local
content-addressed proof; exact retries skip pytest, and concrete selected-test-only deltas remove
their prior Coverage.py contexts before rerunning just those modules. Source/config/suite/runtime/
environment/artifact drift runs the ordinary derived suite, an inconclusive delta falls back to
one full pytest selection, and `AR_QUALITY_NO_RETRY=1` forces fresh Dagger-owned diagnosis.

### Conventions

Closeout approval is separate from implementation approval. Agents must not
treat a previous "looks good", implementation approval, or their own judgment
as authority. 260707-HFX2-L6 changes the current approval model from unconditional per-closeout
developer hand-off to contextual authority: standalone work, final super-branch landing, unclear
series authority, deliberately raised `closeout-approval`, out-of-scope changes, unresolved red
checks, unrepaired memory-quality blockers, and quo-vadis decisions still stop for explicit
developer commit approval; subordinate work inside an accepted orchestrated series may apply
closeout after a clean preview/checks under delegated series authority, with the `intent_note`
recording the accepted planner/series source and owning-seat review. For a developer-gated
closeout, the matching preview tool is the approval prompt surface: it reports the proposed code,
memory, and ledger commit messages before the apply tool mutates Git. The relay follows the
`l-01-agent-lifecycles` skill hand-off protocol in the corrected order — run the preview/dry-run
first, call `lifecycle_turn_end_notification` as the **last tool call**, then report the preview
facts and proposed messages as the **final prose** ending with the approval question.
`worktree_closeout_apply` is never invoked in the same turn as the developer-gated relay; the next
turn auto-resumes to run it (the parked dashboard `lifecycle_gate` path instead raises the durable
gate after the report and is then cleared with `lifecycle_resume`), because harnesses can hide
approval-prompted reports.

The missing-onboarding check is scoped to current additions so newly added
eligible source files cannot escape the gradual onboarding adoption boundary. A
parallel content gate covers changed (already-onboarded) files: a changed source
whose existing sidecar body was not updated this task fails closeout, so
verification metadata is never advanced over stale onboarding content. As of
260707-HFX-L11, in the manager -> builder -> reviewer -> curator chain both checks are expected to
already be satisfied by the curator's prior memory pass when the closing seat runs them here —
they verify that pass, they do not cue the closing seat to author sidecars inline. A solo flat
session with no separate curator seat is unaffected and still authors onboarding itself before
closing out.

The closeout worklist covers the working tree plus the contract-recorded
committed range (issue #83): paths changed between the last verified commit and
the work branch HEAD, scoped by the recorded base so synced-in parallel work
and previously closed-out slices never re-gate. Already-onboarded artifacts
gate on every transported change regardless of author; committed-range paths
without onboarding are reported as `unonboarded` (count plus capped sample) and
never block, and the skill instructs relaying that list at the commit-approval
gate so important transported files are onboarded deliberately.
Entity fingerprints are refreshed after the code commit because
`git-blob-set-v1` resolves `HEAD:<path>` Git blobs. Route overview metadata and
generated route indexes are refreshed before `memory_quality_check` so the
quality gate sees the same memory tree that will be committed.

Task 25 consolidates the **Server-Side Gate Enforcement** section onto
`lifecycle_gate`: when the lifecycle is dashboard-connected, the agent runs the
preview/dry-run first, reports the preview facts in chat, then raises one
`closeout-approval` lifecycle gate carrying the durable junction kind,
developer-facing ask, and preview packet. That call also blocks the active
lifecycle and waits for the developer decision or matching inbox response.
`worktree_closeout_apply` refuses
unless that gate is `approved` **by the developer** — an agent self-approval
(`decidedBy="model"`) never satisfies it. The section remains explicit that
opening a gate is opt-in (a pure-chat session with no cockpit must not open one,
or it self-blocks on its own `open` gate) and that gateless lifecycles keep the
chat `intent_note` commit gate unchanged; the preview/apply `closeout_gate`
block is relayed at the commit-approval gate.

After the developer's resolution reaches the agent it **always clears** with
`lifecycle_resume()` before `worktree_closeout_apply` — the clear remains
agent-owned because a chat "approved" does not propagate itself.
The section also states plainly that **`closeout-approval` is the commit gate**:
closeout is the single commit-of-record for code, memory, and ledger, so every
commit (even a singular one) routes through this one gate and there is no separate
`commit-approval` kind. The push junction in External-Memory Order is likewise the
`push-approval` gate kind through `lifecycle_gate`, followed by `lifecycle_resume`
before any push once the developer response is handled.

Task 28 reframes the closeout commit hand-off (and the push hand-off) from the
block-and-wait `lifecycle_gate` to **notify-and-continue**, in the order **dry-run
→ notify (last tool call) → report (last prose) → stop**: after the preview/dry-run
the agent calls
`lifecycle_turn_end_notification(summary={…the preview facts + the commit ask…})`
as the **last tool call of the turn**, then delivers the preview facts, quality
results, and proposed commit messages as its **final prose** (ending on the commit
ask) and **STOPs / ends the turn**. That tool sets the new `awaiting-developer`
lifecycle state, surfaces a dashboard attention item, and returns immediately —
no wait, no operator inbox, and because it does not render a prompt over the prose
the report stays the last thing the developer reads; the developer approves and the **first AR tool call
of the next turn** auto-resumes (`running`) and auto-dismisses the item, after
which the agent runs `worktree_closeout_apply` (then any push) with no explicit
`lifecycle_resume`. The server-enforced block-and-wait
`closeout-approval` / `push-approval` `lifecycle_gate` and the operator inbox are
parked as the fallback for a deliberate durable, developer-attributed,
mutation-blocking record (on that parked path the report still precedes the gate
raise, since the durable gate renders a prompt over the prose); the Task 25 Server-Side Gate Enforcement /
`lifecycle_resume` descriptions above are superseded historical context. This
packaged file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the
canonical `skills/c-12-closeout/SKILL.md`.

### Invariants And Boundaries

`c-12-closeout` skill must not commit without explicit approval after a preview, must not create
a memory content commit whose affected onboarding metadata still points at
pre-closeout code, must not commit memory before route overview metadata,
generated route indexes, and `memory_quality_check` are clean for the new code
commit, must not **commit** code, memory, ledger, contract, or applied-gate state
when the leaf change-set-scoped quality contract cannot run or reports any failure,
including CRAP at or above the configured threshold (`DEFAULT_CRAP_THRESHOLD = 20.0`) over the
changed production modules, and must not defer or skip `memory_quality_check` — it stays a
per-leaf closeout gate even though the full wrapper moved to the master integration gate.
The index is the one exception and the only mutation permitted ahead of the gate: closeout
resets and stages the task worktree so the gate reads exactly what would be committed, and
it does **not** roll that staging back on refusal. It must not advance
verification metadata for a changed source file whose
sidecar content was not updated in the task, and must not push automatically. It does not create worktrees, integrate
worktrees, finalize lifecycles, clean up worktrees, or initialize memory roots. In the curator
chain it must not author onboarding inline to satisfy a still-failing missing-onboarding or
changed-sidecar check — that failure escalates to a respawned curator pass.

The linked-worktree and conflicted-worktree refusals must keep running **before** the
`git reset`, never after: a `git reset` drops unmerged index entries and `MERGE_HEAD`, so
reordering them would silently disable the conflict check and let `git add -A` stage conflict
markers into a commit. They are preconditions of the staging step, not closeout-wide
preconditions — a checkout carrying no wrapper runs no gate and neither refusal applies to it.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `c-12-closeout` skill defines worktree closeout tool usage and centralizes the closeout sequence. | `# c-12-closeout Closeout` | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:6-409 |
| `c-12-closeout` keeps commit approval separate from implementation approval, states the quality altitude ladder, and binds completed strict runs to one atomically replaced enclosure test-results report. | `## Approval Authority` | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:44-130 |
| Server-Side Gate Enforcement, now explicitly headed **"(parked fallback)"**: run preview/dry-run first, report in chat, raise one `lifecycle_gate(kind="closeout-approval", ask=..., packet=...)`, then `lifecycle_resume` before apply once the developer response is handled; the developer-attributed gate is the security boundary and `closeout-approval` IS the commit gate. The active hand-off is the notify-and-continue `lifecycle_turn_end_notification` above it. | `## Server-Side Gate Enforcement (parked fallback)` | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:123-187 |
| `c-12-closeout` skill uses the missing-onboarding gate before code commit and routes missing sidecars to `c-05-create-or-update-onboarding-files` skill. | `## Preconditions` | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:188-248 |
| `c-09-git-worktree-manager` skill routes worktree closeout to `c-12-closeout` skill and retains worktree lifecycle, integration, and cleanup ownership. | `# c-09-git-worktree-manager Git Worktree Manager` | mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md:6-328 |
| Closeout delegates task completion to `lifecycle_finalize_task` after closeout, integration, PR merge/pull, and carryover. | "Closeout does not mark the task `Completed`" | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:343-343 |
| The L4 staging contract in Approval Authority: when code would commit **and the checkout carries the wrapper**, closeout resets the index, stages the whole task worktree, and gates exactly that staged content before any commit; a refusal leaves it staged, and `wrapper-unavailable` is the reported state for a checkout with no wrapper. | `## Approval Authority` | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:44-122 |
| The two staging refusals and why their order is load-bearing: not-a-task-worktree (`--git-dir` vs `--git-common-dir`) and unresolved merge conflicts both run **before** the reset, because `git reset` drops unmerged entries and `MERGE_HEAD` and would silently disarm the conflict check. | `MERGE_HEAD` | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:390-390 |
| Both memory-order lists restate step 4 as reset + stage + the leaf targeted contract over staged content before any commit, with the no-wrapper checkout committing as it always has. | `## External-Memory Order` | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:249-284; mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:285-323 |
| The caller-side implementation of that contract: `_gate_staged_code` runs both refusals, then `git reset --mixed --quiet HEAD`, then `git add -A`, then the wrapper — and `requires_strict_code_quality` is what makes the whole step conditional on the wrapper being present. | `## Internal-Memory Order` | mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md:308-348 |
| `DEFAULT_CRAP_THRESHOLD = 20.0` — the actual value behind every "the configured threshold" sentence in this skill, which names no number itself. | `DEFAULT_CRAP_THRESHOLD` | mcp/src/agents_remember/code_quality/crap_calculator.py:37-37 |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Series-Contract Notes

Closeout instructions now target the leaf enclosure `series-contract.md`; the root series contract is integration-branch state and is not the path used for leaf code/memory closeout.

## R39 Repository-Resolved Acceptance Doctrine

The packaged closeout skill is generic again: repository memory resolves the concrete executor,
environment, arguments, resource policy, retry semantics, and evidence. The cadence is one
change-set acceptance at leaf closeout, no leaf-integration rerun, and one full check at master
integration. A repository whose policy requires its adapter fails closed when the candidate
removes it. No seat may infer a runner or add a compatibility fallback.

## 260821-CLIVE Closeout Admission And Recovery Doctrine

Every enabled code, memory, and ledger leg requires its own explicit nonblank immutable commit
message before claim, journal, worker, or Git authority. Blank required input is a typed no-effect
refusal, never a half-created generation or synthesized default. Apply starts or observes the
task-bound generation and returns; later status/control uses the exact journal generation and only
advertised retry/recover/cancel/revise/retire/supersede actions. A closeout gate, when explicitly
present, gates only admission and never task authoring or another sprint. Direct landing has the
same journal-first recovery discipline. Raw Git, repeat-from-scratch, reports, stale queue rows, and
permanent compatibility readers are prohibited; legacy repair is an explicit bounded tool.

## Update History

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
