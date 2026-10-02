# skills/c-09-git-worktree-manager/SKILL.md

## Governing Overview

[c-09 worktree lifecycle overview](overview.md)

## Purpose

Canonical agent doctrine for the Agents Remember worktree lifecycle. It defines the public,
contract-addressed route from intent/start through source reconciliation, closeout handoff,
integration, terminal cleanup, and reopen recovery while keeping private selector, journal, ref,
and queue mechanics behind their APIs. Closeout and integration are Git transactions; automatic
quality, test, memory-quality, certification, review, and hook execution do not become lifecycle
prerequisites.

## Code Commentary

### Logic

Atomic-series implementation admission is separate from task planning and is a contract-scoped
authority: each canonical series contract owns its own activation record, so masters that share one
exact code/memory source pair never share this state. Manager dispatch, worker dispatch, atomic
`worktree_start`, and `worktree_attach` are selecting operations; reviewer and curator inspection is
not. Selection first publishes `reconciling` for that exact contract, which suspends nothing — not
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

### Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned lifecycle doctrine.

## Ungoverned Mirror Status (known defect)

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
