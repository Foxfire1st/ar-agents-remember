# mcp/tests/test_checkpoint_landing_end_to_end.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_checkpoint_landing_end_to_end.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `7cbda30d9a9a4c2944382fbef46ac58b85329935` |
| lastVerifiedCommitDate | 2026-09-15T05:15:42+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Exercise composed checkpoint and ordinary integration behavior against real temporary code/memory repositories.

## Code Commentary

### Logic

The sixteen scenario definitions start from QueueFixture's unfinished atomic master and its exact series/leaf contracts. `_unclosed_contract` asserts empty closeout code/memory outputs rather than fabricating completion. Most checkpoint scenarios use the shared public-tool helper; targeted ordinary-entry and approval tests also call their operation seam directly.

The cases verify live-pair preview/apply publication, a real merged memory source, source divergence refusal, idempotent retry and continued work, ordinary final-route completion requirements, closeout preview/apply parity, unchanged leaf preview admission, and ordinary leaf integration with no cache file. They preserve the distinction between checkpoint publication and a stop-only pause.

A code-only advance with no memory attribution can checkpoint without fabricating a row. Missing, stale, or malformed cache data on an owned source checkout cannot block checkpoint publication. Actual master-complete, approval, and ref-race guards remain, including a race response that names the checkpoint tool. Successful assertions read both destination refs and persisted contract cells; refusals verify the relevant refs did not move.

### Conventions

Each test owns a temporary world registered for cleanup during setup, including setup failure. Cached-table corruption/refusal matrices and their old flake note are superseded by current Git-fact scenarios; their prior history remains historical evidence.

### Invariants And Boundaries

- An unfinished checkpoint does not require closeout outputs or claim completed task state.
- The accepted pair is the live code and actual memory ref, not a cache-selected pair.
- Preview and apply preserve completion/source/approval boundaries.
- Cache damage and absent attribution do not become publication gates.
- Substantive divergence and CAS races remain visible.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

| Finding | Citations | Source Path |
| --- | --- | --- |

## Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Initial live-pair capture, source merge, and source divergence. | L67-L122; L124-L147; L149-L163 | [mcp/tests/test_checkpoint_landing_end_to_end.py](mcp/tests/test_checkpoint_landing_end_to_end.py) |
| Retry, continued work, and final-route completion semantics. | L165-L201; L203-L226; L228-L259 | [mcp/tests/test_checkpoint_landing_end_to_end.py](mcp/tests/test_checkpoint_landing_end_to_end.py) |
| Ordinary leaf cache absence and code-only checkpoint publication. | L278-L302; L396-L410 | [mcp/tests/test_checkpoint_landing_end_to_end.py](mcp/tests/test_checkpoint_landing_end_to_end.py) |
| Source-cache damage does not block; real approval/master/race guards survive. | L412-L431; L383-L394; L433-L459; L461-L479 | [mcp/tests/test_checkpoint_landing_end_to_end.py](mcp/tests/test_checkpoint_landing_end_to_end.py) |
| Checkpoint publication remains distinct from pause. | L304-L329 | [mcp/tests/test_checkpoint_landing_end_to_end.py](mcp/tests/test_checkpoint_landing_end_to_end.py) |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Citations | Source Path |
| --- | --- | --- |

## Update History

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Replaced cache-row/refusal matrices with two-output publication, source-content divergence, cache-damaged checkout, and code-without-attribution scenarios; retained public checkpoint, retry, approval, completion, and ref-race behavior. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the shared-support
  extraction moved the whole class, so every one of the twenty case ranges in the table was
  pre-extraction numbering. Re-derived all twenty against the frozen file (`:104-161` … `:847-865`),
  repointed the checkpoint helper to the support module's `checkpoint` (`:345-353`), corrected the
  lane row to 134 and this module's consumer rows to `:304` / `:384` inside the blocks at `:282-341`
  / `:362-421`. The case prose, the L11 removals and the flakiness note were re-read and stand.
  Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/tests/test_checkpoint_landing_end_to_end.py` carries local unstaged changes not represented
  in HEAD. Re-read the card against the frozen on-disk source and re-checked its claims and cited
  ranges: nothing this card asserts is falsified by the change, so no wording changed. Verification
  metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (frozen-tree re-read): the code worktree is frozen
  and these helpers live in the shared support module now, not in this one. Corrected the paragraphs
  to the constructs that exist: `accumulate_master_line`
  (checkpoint_landing_test_support.py:104-120), `branch_checkout`, and `close_out_leaf`
  (checkpoint_landing_test_support.py:66-101), and named `hand_edit_ledger_in_place` with the name
  it actually carries. The substance of each claim holds — the triple is still authored with the
  repository's own ledger helpers, and the closeout still records real commits from the leaf's two
  worktrees — so only the ownership and the anchors changed. Verification metadata remains
  closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 4 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T11:58+02:00 — 260913-LCA-L11 curator (uncommitted change set on `ar/260913-lca-l11-ar`,
  base `4214d7a1`): this module is the leaf's behavioural boundary proof and six of its cases were
  rewritten, so the card was re-derived against the current source. Corrected the class extent
  (`268-656` → `412-1211`); replaced the twelve-case L34 table with the current twenty-case inventory
  and every case's real range; and marked what the leaf did to each case it touched — two renamed and
  **inverted** (a reversed superseding pair now lands, which is the hazard case; the interleaved
  projection now lands on the leaf route too, asserted by the destination refs really moving), one
  renamed (the rebuilt table still checkpoints and an untrue row still refuses), one narrowed (only
  the untrue row refuses — the `dropped`/`duplicated` corruptions are deleted with a comment saying
  why, and the reorderings are asserted as landing), and one re-pointed at the row-truth refusal text
  (instance 4 keeps its fabricated row so the refusal is attributed to the new rule rather than to an
  earlier gate). Corrected the two helper ranges that had drifted (`_accumulate_master_line`
  `125-141` → `132-148`, `_close_out_leaf` `87-122` → `94-129`), replaced the reference row that still
  cited `_require_preserved_ledger_history` with the four promises a landing now owes, and re-pointed
  the recorded `UNREPRODUCED FLAKE` comment (`1162` → `1181-1191`). Added the invariant that a case
  which now accepts a table must assert the acceptance instead of disappearing, and recorded the
  reversal hazard as a known gap pending a decision rather than as something prevented. Verification
  metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-13T18:02+02:00 — 260831-LOCR-L36 terminology: the checkpoint route partially publishes an
  unfinished master, so `_accumulate_master_line`'s state, instance 4's hand-edit scenario, and the
  `_require_preserved_ledger_history` reference row now say "an unfinished master landed at a
  checkpoint" / "a checkpoint's ledger" where they said "a paused master". Wording only; the cases,
  their ranges and the projection proof are unchanged and no verification stamp advanced.
- 2026-09-13T14:32+02:00 — Curator citation repoint after the contract-scoped atomic-series activation re-keying shifted `modules/integrate.py`: the shared-ledger-proof row was rebound to `integrate.py:498-526` (`_require_ledger_projection`) and `integrate.py:527-539` (`_route_commits`). Claim wording unchanged.
- 2026-09-13T12:29:52+00:00: Generated citation repair: `_checkpoint` repointed to mcp/tests/test_checkpoint_landing_end_to_end.py:373-383. No content impact: mechanical anchor-range projection bound to citation source snapshot 608ec827a174d194b141ff2daa61dd8e3b6b44611d03fb561dc0b7bb0223223f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T12:29:52+00:00: Generated citation repair: "UNREPRODUCED FLAKE, RECORDED 2026-09-13" repointed to mcp/tests/test_checkpoint_landing_end_to_end.py:1162-1162. No content impact: mechanical anchor-range projection bound to citation source snapshot 608ec827a174d194b141ff2daa61dd8e3b6b44611d03fb561dc0b7bb0223223f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T09:10+00:00 — Created by the 260831-LOCR-L34 curator pass. Documents the module as the
  boundary proof for plan/apply parity: the twelve cases and what each pins, the public-operation and
  never-pre-populate prohibitions the module docstring states, the fixture composition
  (`QueueFixture` + `_close_out_leaf` + `_accumulate_master_line` + `_branch_checkout`), the
  integration-lane row and the two evidence-lifecycle consumer edges, and the recorded
  `UNREPRODUCED FLAKE` note with its conditions and its "not on the real tree" scope. Verification
  metadata is pinned to the leaf base commit and remains closeout-owned; no acceptance claim.
