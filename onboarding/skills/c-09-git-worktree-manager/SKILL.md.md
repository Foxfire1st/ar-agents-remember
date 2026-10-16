# skills/c-09-git-worktree-manager/SKILL.md

## Current A8 carrier and authority boundary

The source still separates archive-ready from completed cleanup, exact retry arguments from defaults and task authoring from projection admission. Its initial start/attach description no longer carries fleeting on_unsaved save/discard promotion; developer-gated start/integration/finalization wait for approval relayed through the parent or parentless chat. Inspection does not select. The corrected compatibility statement excludes cache bytes as authority; historical incoming direct-recovery wording is scoped below, with current c-12 receipt recovery retained.



- Current start/attach records worktree locations and preserves contract-owned landing; parent approval and exact-source authority remain. [8]




## Governing Overview

[c-09 worktree lifecycle overview](overview.md)

## Purpose

Canonical agent doctrine for the Agents Remember worktree lifecycle. It defines the public,
contract-addressed route from intent/start through source reconciliation, closeout handoff,
integration, terminal cleanup, and reopen recovery while keeping private selector, journal, ref,
and queue mechanics behind their APIs. Closeout and integration consume the completed full
Curator memory-quality result, any required current coherence, and mandatory invariant gates.
They do not start an automatic test, independent-review or curation campaign. Publication-route
hook behavior stays explicit rather than becoming a blanket waiver.

## Code Commentary

Every later converted landing is judged again: leaf integration judges the closeout pair, recorded leaf landing judges the supplied landed memory against the recorded memory base, with the recorded closeout code when the landed code equals or descends from it, otherwise the landed code, and master final/checkpoint/recorded routes run validator, net staleness, chain and authentic-history checks. Direct landing may name its leaf. Historical incoming card warning: an intent-less direct generation's public recover was described as refusing while the real executor settled the kept closing receipt. That is not a blanket current refusal: present c-12 instructions state that advertised direct recovery continues its admitted generation and settles the kept closing receipt. This is an instruction-source account, not a fresh runtime verdict.

### Logic

Atomic-series implementation admission is separate from task planning and is a contract-scoped
authority: each canonical series contract owns its own activation record, so masters that share one
exact code/memory source pair never share this state. Historical predecessor: manager and worker dispatch were listed as selecting operations. Current instruction names atomic `worktree_start` and `worktree_attach` as selectors; reviewer and curator inspection is not selection. Selection first publishes `reconciling` for that exact contract, which suspends nothing — not
its chat, process, worktree, contract, or already-claimed lifecycle journal — then reconciles both
protected source tips and publishes `active` only when both are current. One master's selection
never pauses or excludes another, and multiple nonterminal contracts remain valid. A completed sync
pass whose source moved again remains reconciling. Explicit cancellation publishes durable `vacant`.

The task-document plane remains upstream and never reads activation or queue state. The closeout
queue merely projects active, reconciling, or vacant waiting candidates and owns no claim, commit,
certification, integration, or activation transition. Malformed selection bytes invalidate only the
affected runtime projection/admission; an exact selecting operation archives the bytes with evidence
and replaces the record. Contract presence never elects an owner. Contract-presence fallback and
tolerant readers are prohibited.

`worktree_sync` reconciles the exact source pair as a journaled transaction. It pins recorded bases,
pre-sync branch heads, and admitted source tips before merge mutation. A code or memory conflict is
retained in its exact `.sync` worktree and returned as resolution-required. The agent resolves and
stages derivable conflicts, then calls `resolution_action=continue`; the journal supports resuming
across tool calls and process restarts. `resolution_action=cancel` restores pinned heads, removes
temporary worktrees, terminalizes the journal, and releases an exact reconciling selection.
Memory resolution is not re-judged against either parent's row list: the ledger is derived state, its
rebuild is its authority, and a row the rebuild cannot resolve is reported as an exclusion rather
than refused by the sync. Repeated code commits remain valid newest-first memory history; neither the
skill nor the sync transaction collapses them into a globally unique code key. The shared source text
at `SKILL.md:293-299` says the same: it and its generated copies were corrected together with the
code, because they had told agents that continuation validates every exact parent ledger row
survives.

Unconverted-memory guidance is unconditional (MIK-R46@v2), not triggered by a
converted branch elsewhere. A moving sync with unconverted target and source
refuses `legacy-format`; merging three unconverted trees is not a plain Git
fallback. A fast-forward that takes a converted source remains admitted, and a
mixed-format merge takes the crossing route. Fast-forwarding an unconverted
source onto a converted target refuses rather than removing the text format.
The unchanged no-memory-move cases remain outside this new refusal. Convert first
through `c-13-install-and-onboard` and `docs/guides/first-conversion.md`: one new
leaf converts its memory worktree, then closes out and lands; other open lines
cross at their next `worktree_sync` with `merge-memory`. Retained continue/cancel
recovery is not a fresh legacy-write admission.

Cleanup releases an exact selected terminal contract before removing the authority needed to name
it and never clears a newer selection. Integration conflicts use the same evidence boundary:
agents resolve technically derivable conflicts; only genuine semantic ambiguity escalates to the
architect.

**Finalization reaches the master that lists a leaf naming none (MIK-R38, 260928-MIK-L38).** The finalizer
paragraph of `## Lifecycle Finalization And Cleanup` now says the finalizer derives and reconciles the exact row when
the bound leaf declares an existing immediate parent "or names none and its folder's `task.json` master lists it"
(ruling 2026-09-30T12:33:07 Q3), and that "a sub-task naming none whose folder `task.json` is not a master is
refused" (review R1 note 5, ruling 13:11:32; "sub-task" rather than "leaf" by ruling 14:12:52, so a `light` task that
is its own `task.json`, which finalizes standalone, is not covered). `scripts/sync-skills.py` rewrote the package
copy and the eight harness starter copies byte-identically from this source.

The closeout paragraph says since L37 that the preview does ask the mandatory invariant gate on converted memory:
a leaf the apply would refuse is answered `knowledge-gate-refused` with the open findings, never `would-closeout`
(see `c-12-closeout`).
On unconverted memory, preview and apply refuse `legacy-format` before claim or
commit; first conversion precedes closeout regardless of converted memory elsewhere.

**Memory cannot be disabled for a task (260928-MIK-L50).** The skill's recovery list is now `reconciliation` / `custom` — the `disabled-memory` choice is gone — and a start that names the removed mode or choice is refused (`memory-opt-out-refused`). A contract on disk that carries the removed mode is abandoned and started again: save the changes worth keeping, run `worktree_abandon` (the dry run first), then `worktree_start` at the same address without `memory_mode` (skills/c-09-git-worktree-manager/SKILL.md:211-216).

### Conventions

- Preview before mutation and keep dry-run side-effect free.
- Use the canonical enclosure contract as the public recovery address.
- Sync early, before memory work, while preserving exact code/memory ledger admission.
- Never imitate continue/cancel with ambient Git commands.

### Invariants And Boundaries

- Multiple live series may coexist; each canonical series contract owns its own activation record,
  and multiple nonterminal contracts remain valid.
- Selection publishes `reconciling` and suspends nothing — not the contract, its chat, process,
  worktree, or already-claimed lifecycle journal.
- The enclosure-root journal survives a missing or unreadable task contract.
- The queue never owns operation lifecycle or commit evidence.
- No compatibility reader or contract-presence election exists.
- Ledger order selects current memory authority, while retained exact rows preserve audit history.
  The sync proves Git state and the admitted mapping only: merge validation requires no row list and
  imposes no global code-key uniqueness.

### Todos

None. Exact source claims and vocabulary are reconciled to the canonical skill.


## CCR-R12@v5 Transaction Boundary

Current contract: closeout and integration are Git transactions over the authorized code, memory-content, and ledger legs, with preview, conflict, and ref safeguards. Their transaction-owned commit legs suppress automatic quality and test hooks; ordinary explicit Git hook policy outside closeout/integration remains unchanged. Targeted checks, certification, full quality, full tests, full memory quality, and independent review are contextual evidence or explicit operations; they are not automatic c-09 prerequisites.

## Granted direct workspace

A granted canonical leaf works in its master series checkouts without leaf worktree_start or an enclosure. Product role preparation keeps report/scratch artifacts in the separate group and refuses missing authority/roots or another active direct sibling. Ordinary ungranted enclosure start/attach, source-edge sync and transaction recovery retain their owners; directness is not a shell permission or OS sandbox.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- Canonical contract-scoped admission and task/queue separation. [1]


- Resumable retained-conflict transaction and explicit cancellation doctrine. [2]




- Exact cleanup/finalization boundary. [3]




- The finalizer paragraph names the folder master's row and refuses a sub-task naming none whose folder `task.json` is not a master (MIK-R38). [4]



- Public implementation facade preserves the same contract-addressed API. [5]




- The preview asks the mandatory gate on converted memory. [6]


- Bounded no-remains exception: with no locator, folder or branches, cleanup or abandon finishes directly, recording terminal state and reason in the surviving contract.

### Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned lifecycle doctrine.

## Historical mirror-scope observation (known defect at its observed configuration)

This card lives in the `onboarding/skills/**` tree, which mirrors the code repository's `skills/**`
route. `skills/**` is absent from `settings.json`'s `pathRules.include`, so this whole onboarding
tree sits outside normal onboarding census coverage: it is legacy and ungoverned. It is retained here
only because the contract-scoped memory-quality checker still validates these documents whenever
`skills/**` is part of a leaf's changed set, which is exactly why this card was updated by hand
rather than by a governed maintenance pass. The remaining sibling sidecars under
`onboarding/skills/**` — the other role, criteria, and template cards — are knowingly stale and are
deliberately left untouched pending a follow-up decision on whether this mirror should be governed or
removed. That mismatch between the declared path rules and the enforced checking scope is itself the
recorded defect.

## Current handoff boundary

Preview and human-pinned authorization remain separate from mutation. Retired explicit
lifecycle signal calls are not replacement APIs; next-turn/session wording in the instruction
is not evidence of implemented L113 runtime handling.

- Current preview/handoff/STOP and owner-authority instruction; not runtime acceptance. [7]

## Current source qualification

This candidate's finalizer text reconciles the parent's exact child row and validates the independently optional parent assertions; each parent-child edge is finalized separately and the parent itself is not recursively completed. The former explicit standalone/no-parent support sentence was removed. An older card aside saying a task.json finalizes standalone is retained only as historical commentary, not a supported-candidate promise. The current contract-location, parent approval-relay and start/attach selector qualifications above remain governing.

- Finalizer edge reconciliation no longer advertises the removed standalone/no-parent support sentence. [9]


## Inherited Source-Epoch Commentary

The following distribution-copy account preserves useful explanations and source-epoch history, not a second current contract. Its currentness, tool, seat, provider, execution and permission claims are inherited scope unless separately qualified above against the current canonical source. Earlier incompatible claims on the explicitly updated seams are historical, not restored authority. Historical labels in this quotation do not allocate this card's reference numbers.

> # mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md
>
> ## Current A8 carrier and authority boundary
>
> The source still separates archive-ready from completed cleanup, exact retry arguments from defaults and task authoring from projection admission. Its initial start/attach description no longer carries fleeting on_unsaved save/discard promotion; developer-gated start/integration/finalization wait for approval relayed through the parent or parentless chat. Inspection does not select. The corrected compatibility statement excludes cache bytes as authority; historical incoming direct-recovery wording is scoped below, with current c-12 receipt recovery retained.
>
> - Current instruction adopts the new contract lifecycle, uses parent role_message approval relays, limits selectors to atomic start/attach and retains strict source lineage and terminal evidence; old fleeting-save/dispatch/automatic-resume accounts are not current authority. \(historical reference 18) (historical reference 18)
>
>
> ## Governing Overview
>
> [MCP package overview](../../../../../../overview.md)
>
> ## Purpose
>
> This generated runtime skill propagates the canonical root skill's exact-pair landing guidance. It distinguishes leaf rejudgment from the master validator/staleness/chain/history checks and separates public direct recover refusal from the real executor's receipt settlement. Edit the canonical skill and regenerate copies; this file is no second authority.
>
>
> Documents `c-09-git-worktree-manager`, the Git worktree lifecycle manager for Agents Remember tasks: worktree start, attach/status, external-memory compatibility before start, integration, lifecycle finalization, and cleanup, plus reopening (`task_reopen` resets a fully landed leaf to planning under its exact leaf id). Closeout sequencing belongs to `c-12-closeout`; this skill only supplies the worktree-specific configured leaf path and the integration/finalization follow-up rules.
>
> ## Code Commentary
>
> Task identity is settled before worktree creation: a master owns the root `series-contract.md` plus its integration branch, and each ungranted enclosed build leaf owns its enclosure contract. The Worktree Intent Gate must be explicitly approved before start and must name branch policy, source/work branches, memory mode, landing path, and risks. Standalone/new/final work previews first and sends its intent to the parent through `role_message`, or ends with the intent in chat when there is no parent; start, integration or finalization runs only after approval arrives. No awaiting-developer state, automatic resume or gate-tool call is inferred. Subordinate accepted-series work continues under recorded series authority.
>
> External memory incompatibility is interactive and offers `reconciliation` or `custom` handling — there is no `disabled-memory` recovery choice. Memory cannot be disabled for a task: a start naming the removed `disabled` mode or the removed `disabled-memory` answer is refused by name (`memory-opt-out-refused`) before any worktree is created. A contract on disk that carries the removed mode is abandoned and started again: save the changes worth keeping, run `worktree_abandon` (dry run first), then `worktree_start` at the same address without `memory_mode`. Historical earlier-card assumption: a newly merged gated PR commit absent from the ledger was called an incompatibility trigger. That is not the current admission criterion: actual code/memory objects, ancestry and refs govern compatibility; `memory.md` remains an ignored consumer cache whose absence, staleness or malformed bytes never make an otherwise valid pair incompatible.
>
> Integration follows applicable authority (`ff-only` for unmoved sources, `replay` for parallel work); the recorded `source_branch` is the integration target. Lifecycle finalization proves the landed commit reachable from the recorded local source branch, runs or verifies cleanup, and reconciles task documents to `Completed`. The closeout preview runs no quality/test/memory/certification/review tool but does ask the mandatory invariant gate on converted memory. Atomic-series activation is scoped to the exact canonical series contract; terminal cleanup releases only the exact still-selected contract.
>
> Unconverted-memory guidance is unconditional (MIK-R46@v2), not triggered by a
> converted branch elsewhere. A moving sync with unconverted target and source
> refuses `legacy-format`; merging three unconverted trees is not a plain Git
> fallback. A fast-forward that takes a converted source remains admitted, and a
> mixed-format merge takes the crossing route. Fast-forwarding an unconverted
> source onto a converted target refuses rather than removing the text format.
> The unchanged no-memory-move cases remain outside this new refusal. Convert first
> through `c-13-install-and-onboard` and `docs/guides/first-conversion.md`: one new
> leaf converts its memory worktree, then closes out and lands; other open lines
> cross at their next `worktree_sync` with `merge-memory`. Retained continue/cancel
> recovery is not a fresh legacy-write admission.
>
> ## Granted direct workspace
>
> A granted canonical leaf works in its master series checkouts without leaf worktree_start or an enclosure. Product role preparation keeps report/scratch artifacts in the separate group and refuses missing authority/roots or another active direct sibling. Ordinary ungranted enclosure start/attach, source-edge sync and transaction recovery retain their owners; directness is not a shell permission or OS sandbox.
>
> ## Evidence
>
> - No `disabled-memory` choice; abandon-and-restart way out (historical reference 15)
> - Removed answer refused by name, never honored (historical reference 16)
> - Removed member refused by name at the vocabulary (historical reference 17)

Inherited reference 15 commentary (not a revalidated target):

> No `disabled-memory` choice; abandon-and-restart way out
>
> Anchor: `c-09-git-worktree-manager`

Inherited reference 16 commentary (not a revalidated target):

> Removed answer refused by name, never honored

Inherited reference 17 commentary (not a revalidated target):

> Removed member refused by name at the vocabulary

Inherited reference 18 commentary (not a revalidated target):

> Current instruction adopts the new contract lifecycle, uses parent role_message approval relays, limits selectors to atomic start/attach and retains strict source lineage and terminal evidence; old fleeting-save/dispatch/automatic-resume accounts are not current authority. (historical reference 18)

## Canonical Source Ownership

The byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. Whole-file source evidence does not certify inherited statements, execution, grading or the whole card.

- The authored source owns this contract; the distribution copy is not a separate authority. [10]
