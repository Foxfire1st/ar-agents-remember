# skills/c-09-git-worktree-manager/SKILL.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/c-09-git-worktree-manager/SKILL.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T13:20+02:00 |
| lastVerifiedCommitHash |  `e0820b04a499cbfb2079c78485346c50917a238a`|
| lastVerifiedCommitDate |  2026-09-13T18:02:04+02:00|
| governingOverview | `skills/c-09-git-worktree-manager/overview.md` |

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

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical contract-scoped admission and task/queue separation. | "Atomic-series implementation admission is a separate, contract-scoped authority." | skills/c-09-git-worktree-manager/SKILL.md:237-249 |
| Resumable retained-conflict transaction and explicit cancellation doctrine. | `## Mid-Task Sync` | skills/c-09-git-worktree-manager/SKILL.md:256-300 |
| Exact cleanup/finalization boundary. | `## Lifecycle Finalization And Cleanup` | skills/c-09-git-worktree-manager/SKILL.md:430-508 |
| Public implementation facade preserves the same contract-addressed API. | `sync_result` | mcp/src/agents_remember/worktrees/modules/sync.py:28-67 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned lifecycle doctrine.

| Finding | Anchor | Source |
| --- | --- | --- |

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

## Update History
- 2026-09-14T13:20+02:00 — Corrected the sync doctrine this card states: the transaction no longer
  re-judges a memory resolution against either parent's row list, because the ledger is derived state
  and its rebuild is its authority, so a row the rebuild cannot resolve is reported as an exclusion
  rather than refused. The shared source text at `SKILL.md:293-299` was corrected in the same change,
  together with its eight generated copies, so the skill no longer carries the removed parent-row
  validation; the matching invariant was reworded.
  Verification remains closeout-owned.
- 2026-09-13T15:01:46+02:00 — Gate-required ungoverned-mirror curation: removed the dead
  `source-pair-scoped` admission claim and reworded the logic to the shipped contract-scoped
  authority; rebound the citation to `"Atomic-series implementation admission is a separate,
  contract-scoped authority."` at SKILL.md:237-249, and rebound `## Mid-Task Sync` to :256-300 and
  `## Lifecycle Finalization And Cleanup` to :430-508 after grepping the frozen source. Body now
  records per-contract activation (selection publishes `reconciling` for that contract and suspends
  nothing; one master's selection never pauses or excludes another; multiple nonterminal contracts
  remain valid) and the queue's active/reconciling/vacant projection. Added the Ungoverned Mirror
  Status defect statement. Verification metadata remains closeout-owned.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `sync_result` repointed to mcp/src/agents_remember/worktrees/modules/sync.py:28-67. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "Atomic-series implementation admission is a separate, source-pair-scoped authority." repointed to skills/c-09-git-worktree-manager/SKILL.md:237-237. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-08-26T14:32+02:00 — Corrected sync doctrine to preserve every exact parent ledger row while
  accepting repeated code commits as newest-first memory history. Verification remains
  closeout-owned.

- 2026-08-26T10:44:52+02:00 — Completed governed provenance review for the canonical c-09 selector, resumable sync, cancellation, and terminal-release doctrine.

- 2026-08-26T08:45+02:00 — Restored canonical Docs/Cross-Repo reference sections for the changed
  c-09 doctrine card.

- 2026-08-26T08:20+02:00 — Reconciled canonical c-09 selection, resumable-sync, cancellation,
  terminal-release, and no-fallback doctrine to the frozen source.

- 2026-08-26T05:20+02:00 — Created strict canonical onboarding for the source-pair selector,
  reconciliation-before-exposure, retained conflicts, continue/cancel, stable journal, exact
  terminal release, and no-fallback boundary. Final citations remain post-Dagger-owned.
