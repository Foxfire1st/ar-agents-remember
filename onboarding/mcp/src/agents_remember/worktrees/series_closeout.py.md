# mcp/src/agents_remember/worktrees/series_closeout.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/series_closeout.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `756c47b37fa16324a836a44336655413d10fffaa` |
| lastVerifiedCommitDate | 2026-09-20T03:26:53+02:00|
| verificationStatus | working-candidate |
| reviewedWorkingCandidate | candidate `ar/260915-ks-l35-ar`, uncommitted; base `7abacd8e432730cfca177ff0136711f13ea5f34d` |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Prove completed atomic-master candidates and capture exact series refs for final closeout or a non-final checkpoint.

## Code Commentary

### Logic

The final route resolves canonical master/leaf task membership and requires one exact enclosure per leaf. It verifies each leaf's repository, source branch, base-to-integrated edges, and recorded code/memory output identity, then orders the chain by the landings' own ancestry. It does not order from bases that a later sync legitimately advanced.

Without a recorded sync, the oldest leaf starts at the exact series base. With sync history, the origin is proved against the first sync's old bases and each leaf must remain on that line. The series spine must contain every landing and only admitted inter-leaf/source transitions. Memory-side history inspection excludes root memory.md content; the removed special ledger-recording commit exception is not an authority rule.

Every step of that spine is proved by **enumerating** what it adds — `rev-list --no-merges --full-history <later> --not <earlier>`, the memory side additionally excluding `.` with `:(top,exclude)memory.md` — and admitting a commit only when it is an official position one of the chain's own contracts synced with, or when a recorded position that lies **inside that step** reaches it. The second clause is what stops the rule refusing the shape it names: when a step's endpoint is the merge of the previous landing with a synced position, the whole step *is* that position's own line. Measured on the 260915-KS master, the step is L5's landing `7db50f8f` to L6's recorded base `8dfc11b8`; `8dfc11b8` is the merge of `7db50f8f` with the synced super-line position `8dd62345`, every commit the step adds is reachable from `8dd62345`, and only the position itself used to be admitted (register row D-60). *Inside* means strictly after the step's start and at or before its end, so a position that merely descends **from** the step stays outside it and still cannot vacate a commit the step genuinely introduced. The admission stays bounded to the positions the call was given, and the step is never *subtracted* from the revision walk: removing a position's whole ancestry is what once made the check pass vacuously.

Both checkpoint capture and final memory recording use `series_memory_closeout`: re-read the exact code work ref, capture the actual memory work ref, and prove its recorded-base ancestry. They do not select an output from cached rows or require a fixed-point table. A code tip with no corresponding memory trailer can therefore still be captured without inventing attribution.

Final closeout and integration require the master complete. The checkpoint route deliberately does not, and instead refuses an already-completed master, requires an explicit captured `expected` pair, reloads the contract, and revalidates live tips before publication. It records no completed-task claim and reclaims nothing.

### Conventions

Closeout records existing refs rather than committing an ambient series workbench. Substantive dirty checkouts still refuse; memory.md alone is excluded. Checkpoint publication, stop-only pause, and finalization are distinct operations.

### Invariants And Boundaries

- Canonical task membership and exact repository/ref identity remain mandatory.
- Leaf order comes from real code and memory ancestry, including after source reconciliation.
- Cache rows, ordering, and fixed-point projection are never series completion or checkpoint gates.
- No agent-owned ledger-only commit is needed to record a reconciled code tip.
- The checkpoint's expected candidate is required and is re-read before publication.
- A spine step may add only a recorded official position, or a line that a recorded position lying inside that step reaches; a position descending from the step admits nothing.
- Preview and apply consume the same final-completion predicate.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

| Finding | Anchor | Source |
| --- | --- | --- |
| Final closeout and series integration re-prove canonical completion. | `require_closeout_publication_authority` | mcp/src/agents_remember/worktrees/series_closeout.py:33-57 |
| Checkpoint capture and publication revalidate an explicit two-output candidate. | `SeriesCheckpointRefs`; `publish_series_checkpoint_under_authority` | mcp/src/agents_remember/worktrees/series_closeout.py:147-178 |
| Leaf membership, output identity, and ordering remain exact. | `_exact_atomic_landing_chain`; `_ordered_atomic_landing_chain`; `_atomic_leaf_code_matches`; `_atomic_leaf_memory_matches` | mcp/src/agents_remember/worktrees/series_closeout.py:201-223; mcp/src/agents_remember/worktrees/series_closeout.py:251-281; mcp/src/agents_remember/worktrees/series_closeout.py:664-697; mcp/src/agents_remember/worktrees/series_closeout.py:700-714 |
| Recorded origins and admitted substantive history preserve reconciled series proof. | `_require_chain_origin`; `_require_admitted_step` | mcp/src/agents_remember/worktrees/series_closeout.py:309-340; mcp/src/agents_remember/worktrees/series_closeout.py:472-509 |
| Series cleanliness and actual memory-ref capture exclude cache authority. | `refuse_series_workbench_commit`; `publish_series_checkpoint_under_authority` | mcp/src/agents_remember/worktrees/series_closeout.py:763-781; mcp/src/agents_remember/worktrees/series_closeout.py:147-178 |
| Recorded origins and admitted substantive history preserve reconciled series proof. | `_require_chain_origin`; `_require_admitted_step`; `_positions_inside_the_step`; `_reached_by_an_official_position` | mcp/src/agents_remember/worktrees/series_closeout.py:320-351; mcp/src/agents_remember/worktrees/series_closeout.py:483-543; mcp/src/agents_remember/worktrees/series_closeout.py:546-566; mcp/src/agents_remember/worktrees/series_closeout.py:569-576 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-20T03:17+02:00 — 260915-KS-L35 curator (uncommitted change set on `ar/260915-ks-l35-ar`, code base `7abacd8e`): **the spine's step rule now admits the reconciled line a step actually merged with, so the check stopped refusing the shape its own docstring names.** `_require_admitted_step` enumerates what a step adds (`rev-list --no-merges --full-history <later> --not <earlier>`, the memory side excluding `memory.md`) and admits a commit that is a recorded official position **or** that is reachable from a recorded position lying **inside** that step: `_positions_inside_the_step` computes the inside set (strictly after the start via `is_ancestor(earlier, position)`, at or before the end via `is_ancestor(position, later)`, the start itself excluded because the revision walk already removes what it reaches) and `_reached_by_an_official_position` asks whether any of them reaches the commit. The measured shape is this master's own L5→L6 step — `7db50f8f` → `8dfc11b8`, where `8dfc11b8` is the merge of `7db50f8f` with the synced super-line position `8dd62345` and all 22 commits the step adds are reachable from `8dd62345`, so the old rule admitted the position and refused the line it introduced (register row D-60). A position that merely descends **from** the step is not inside it, so the counter-case still refuses and its case still passes unchanged. The three reference rows whose cited ranges this change moved were re-derived against the tree rather than left pointing into the docstring: `_atomic_leaf_code_matches` and `_atomic_leaf_memory_matches` now cite their own extents `:664-697` / `:700-714`, `refuse_series_workbench_commit` cites `:763-781`, and the origin/admitted row carries the two new helpers at `:546-566` and `:569-576`. No verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-20T01:00+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared the 1 enforced citation row this card carried (citation_anchor_absent_from_range): its cited range was hand-read against mcp/src/agents_remember/worktrees/series_closeout.py and already held the anchor its claim names — `refuse_series_workbench_commit` at series_closeout.py:718-736 — so no range was changed; every claim wording, anchor and every other range is unchanged, and no verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 1 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `refuse_series_workbench_commit`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 1 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `series_closeout.py.md:70` (`refuse_series_workbench_commit`, `publish_series_checkpoint_under_authority`).
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Unified series memory capture on the actual memory ref; removed exact-mapping and fixed-point readers, ledger output cells, and the ledger-only history exemption. Preserved canonical completion, leaf-chain origin/spine proof, expected checkpoint capture, and pause/finalization distinctions. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of
  18 claim(s) whose anchor no longer sat in its cited range and normalised 20 further range(s) in
  this card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T11:58+02:00 — 260913-LCA-L11 curator (uncommitted change set on `ar/260913-lca-l11-ar`,
  base `4214d7a1`): recorded the deletion of this route's own ledger-row census.
  `atomic_series_ledger_prefix`, `_reconciled_ledger_prefix` and `_is_reconciliation_row` are gone
  with their only consumer, `LandingAdmission.expected_series_ledger_prefix`, because the
  integration-side check that a landing preserves the complete source ledger history was removed by
  the developer's 2026-09-14T08:15+02:00 ruling: it protected the tracked `memory.md`, which is
  derived state. Corrected the two body claims the deletion falsifies — the paragraph that said
  `_exact_atomic_landing_chain` feeds `atomic_series_ledger_prefix`, and the "The master's own rows"
  section that described all three functions as live — and corrected the invariant that said a
  reconciliation row is proved from the landed table. Stated the boundary a future reader needs:
  `_require_series_ledger_projection` (was cited at `914-930`, now **841-857**) still requires `is_fixed_point` and still
  refuses a dropped, reordered or replaced source row **on the reconciled-pair recording path**,
  which is not the landing check that was removed; it must not be "finished off" on the strength of
  the landing change, and the landing rule must not be back-ported here. Repointed every reference
  range in this card after the module shrank by 73 lines. Verification metadata remains
  closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: corrected this card's L36 sentence that "no worktree tool
  performs it". The stop now exists as its own public verb (`worktree_pause`, registered by the
  working-half registrar), so the card states the L36 state as history and names the two separate
  registered descriptions that now point at each other. The checkpoint's own publication account is
  unchanged. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T17:38+02:00 -- 260831-LOCR-L36 curator reconciliation against the changed code
  candidate. Recorded that the atomic completion proof no longer anchors the leaf chain at
  `series.code_base_commit`/`series.memory_base_commit` (which `worktree_sync` advances): the order
  now comes from the leaves' own landed ancestry (`_ordered_atomic_landing_chain`,
  `_leaf_landing_precedes`), the origin is the recorded base exactly only without a sync and one
  line with the first sync's pre-state once a sync exists (`_require_chain_origin`,
  `_series_pre_sync_base`, `_require_same_line`, `_require_leaf_starts_on_the_chain`), and one
  series ref is proved to be the leaf landings joined only by the official positions this contract
  synced with (`_require_landing_spine_side`, `_require_admitted_step`, `_is_ledger_recording`,
  `_landing_source_positions`). Recorded the new reconciled-pair path: `atomic_series_ledger_prefix`
  now includes the master's own proved reconciliation merges, and the series closeout accepts the
  reconciled tip through `series_memory_closeout` only after proving the master's own chain tip is
  still mapped and the landed table is the exact projection of its source plus this line's own true
  rows (`_require_series_ledger_projection`). Corrected the earlier claim that the checkpoint and
  the final series closeout share one reader: the checkpoint reads the exact mapping through
  `exact_series_memory_closeout`, the final route may accept the reconciled pair through
  `series_memory_closeout`. Stated that recording the reconciled pair remains an agent-owned
  `memory.md` write (the test helper `_record_reconciled_pair`) with **no public tool**, because the
  developer cancelled the follow-up pass that would have made it public. Recorded that a checkpoint
  is a partial PUBLICATION, not a pause: it moves both refs onto the super branch under explicit
  developer approval, while a pause publishes nothing and moves no ref. Re-derived every reference
  range in this card for the rewritten symbol block. Verification metadata remains closeout-owned;
  no acceptance claim.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T08:40+00:00 — 260831-LOCR-L34 reachability repair: recorded that the L30 checkpoint
  route was unreachable in both directions (a partial master could not reach the closeout-gated
  route; a complete one was refused) and never proved its real ref move, and what L34 changed —
  `capture_series_checkpoint_refs`/`SeriesCheckpointRefs` capturing the live code and memory work
  branch tips and proving their mapping through the same `exact_series_memory_closeout` the final
  route uses, the now-required and revalidated `expected` argument with its
  `atomic-series-checkpoint-candidate-moved` refusal, and `require_series_checkpoint_authority` as one
  definition with two callers. Recorded the closeout gate's extraction into
  `require_closeout_publication_authority` (leaf-exempt, read by both the preview and the apply) as
  instance 1 of the preview/apply parity invariant. Re-derived every reference range in this card for
  the new symbol block. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: added `publish_series_checkpoint_under_authority`,
  the missing partial-master verb that keeps every ref-protecting authority while dropping the
  "master is complete" and "every atomic leaf landed" assumptions; recorded the
  `atomic-series-checkpoint-master-complete` refusal that stops a checkpoint from downgrading a
  finished integration, the contract re-read before protected landing, and the invariant that the
  checkpoint route may not grow a completion proof. Re-derived every reference range in this card
  (the new function is inserted at L72, shifting all later symbols by ~37 lines). Verification
  metadata remains closeout-owned; no acceptance claim.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_require_atomic_master_complete` repointed to mcp/src/agents_remember/worktrees/series_closeout.py:309-346. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T12:02+02:00 — Closeout-door cut reconciliation at code commit `fad9808e`: removed the door dimension from the landed-leaf proof claim — `_AtomicLandingFacts` and its `door`/`door_sprint`/`door_candidate` comparisons were deleted with `contract.closeout_door`. Verification metadata remains pinned because only the cut-affected claims were reconciled; source documentation only, no acceptance claim.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.

- 2026-08-29T17:23+02:00 — No content impact: reviewed the Python 3.13 local type-parameter migration for closeout and integration publication callbacks and confirmed that series authority remains as documented. Verification remains closeout-owned.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: replaced initial queue-state publication with exact atomic completion and claimed-door re-proof at landing. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the source only imports the extracted `initial_queue_state` owner and calls the same initializer with the same arguments. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: atomic closeout gates on the effective execution
  nature (nature-less legacy masters close out atomically under the default, L13-R5a), and a
  graph-less sprint's series edge publishes queue-free because the live series contract already
  owns the sequential lane (L13-R1). Verification remains closeout-owned.

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: added `atomic_series_ledger_prefix` and made `_exact_atomic_landing_chain` return the ordered leaf chain. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created atomic series closeout authority onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
