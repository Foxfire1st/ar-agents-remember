# mcp/src/agents_remember/worktrees/reopen.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/reopen.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `7abacd8e432730cfca177ff0136711f13ea5f34d` |
| lastVerifiedCommitDate | 2026-09-20T03:03:09+02:00|
| verificationStatus | working-candidate |
| reviewedWorkingCandidate | candidate `ar/260915-ks-l34-ar`, uncommitted; base `0da444b3b2b61f6a86fa4076b283c305db025d22` |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Reopen a fully landed leaf — or a terminal atomic series — under its original id by atomically resetting its enclosure and task facts, and re-address a series whose enclosure generation was collected but never re-published.

## Code Commentary

### Logic

`reopen_task` requires a leaf whose closeout, integration, and cleanup are completed and whose code/memory worktrees are gone. It resolves the exact parent series, proves accepted memory ancestry through `require_integrated_memory_ancestry`, and uses the recorded integrated code/memory outputs as the terminal lineage position. It never reads a cache mapping or uses an integrated ledger commit.

The reset clears free-form approval/output/lifecycle provenance with dataclass replacement and changes vocabulary cells through `ContractCells` and `amend_contract`. It preserves the leaf id. Task plans reset the leaf and corresponding master row; `cleanup="reopened"` tells worktree start to recreate the enclosure rather than attach to the old one.

The frozen landing observation clear, leaf/master task updates, and contract reset publish in one task-fact CAS batch. Apply reloads and repeats the terminal/source checks inside that publication. Original artifacts support rollback of a failed canonical write; derived projection refresh happens afterward. Recreating worktrees remains worktree_start's responsibility.

#### The series half, and its three deciding facts

The series spelling of the same operation publishes the contract tombstone, the integration refs, the
master document and the successor enclosure generation under the same guards. Three facts decide it,
and the current candidate changed all three (D-58):

- **In flight, not `cleanup`.** `_series_in_flight` reads `closeout_status` and `integration_status`.
  It deliberately does **not** read `cleanup`, because the reopen rewrites that cell as its own first
  durable step — keying the ref rule on it would make the answer depend on whether the reset had
  already been written, which is exactly the difference between a first attempt and its resume.
- **An advanced branch may be the series' own work.** `_series_ref_recut` takes `in_flight` and, when
  the series has not closed out and the recorded source tip is an **ancestor** of the integration
  branch, reports that branch as action `advance`: it is the line the series is landing on, there is
  nothing to re-cut, and refusing would strand it. It is never moved. A completed series keeps its
  refusal, and a diverged or lagging branch is refused in both cases.
- **A live series at a collected address is re-addressed, not refused.** `_series_is_live_unaddressed`
  accepts `cleanup: pending` with both progress cells untouched when the locator at the contract's own
  address reads `terminal-archived`. The locator is the one fact that tells "the generation was
  collected" apart from "somebody is mid-transition", so the call publishes the successor generation
  alone — `mode: publish`, no reset and no ref move — which is the arrival the hand reopen left behind
  and also what a resume of an interrupted publication needs.
- **The review counter is part of the reset.** `_review_state_carries_history` reports whether the
  counter carries anything, and `_plan_series_document_reset` clears `.reviewState` to its pristine
  value when it does — the rounds a completion spent belong to that completion, so a reopened master
  starts at zero instead of billing its next round against a budget it never spent. A document whose
  counter is absent or already all-zero is left untouched, and the reset no longer returns early on a
  document that has left `Completed`.

The applied result payload therefore carries a structured `mode` (`reset` or `publish`) alongside its
`state`, and the two modes report different summaries because they did different things.

### Conventions

This owner lives in worktrees because the enclosure contract is the primary mutated artifact; the task store remains a collaborator. The parent resolver validates parent identity without restoring the deleted child-admission seal. The series half uses the same tombstone proof, the same guards and the same archive citation as the terminal path — there is no second publication route.

### Invariants And Boundaries

- Leaf identity is stable across reopen.
- In-flight leaves, series contracts, and leaves with live worktrees cannot reopen.
- Terminal code/memory Git facts replace cache mapping proof; unrelated source movement remains a refusal.
- Vocabulary cells use the typed contract writer.
- A task/ref race cannot overwrite newer task facts or leave an old completed landing projection current.
- The reopen **never moves an existing ref**: it re-cuts an absent one, accepts an advanced one as the series' own work, and refuses divergence.
- A successor generation always cites the exact archived predecessor, and the series' own `cleanup` stays `pending` — `reopened` is itself a terminal series state and would leave the series unable to own the lane.

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
| Terminal preflight, accepted memory ancestry, and integrated source-position checks. | `_reopen_preflight_refusal` | mcp/src/agents_remember/worktrees/reopen.py:325-398 |
| Contract reset preserves identity while clearing two-output provenance. | `_reopened_contract` | mcp/src/agents_remember/worktrees/reopen.py:197-224 |
| Frozen observation, task plans, and canonical publication remain coordinated. | `_clear_frozen_landing`; `_ReopenPublication` | mcp/src/agents_remember/worktrees/reopen.py:519-579 |
| Whether a series still owns its integration line, read from the two progress cells a completion writes rather than from `cleanup`. | `_series_in_flight` | mcp/src/agents_remember/worktrees/reopen.py:1003-1012 |
| A series is live but unaddressed only when the locator at its own address is `terminal-archived` and both progress cells are untouched. | `_series_is_live_unaddressed` | mcp/src/agents_remember/worktrees/reopen.py:1015-1039 |
| An advanced integration branch is the in-flight series' own landed work: reported as `advance`, never moved; divergence still refuses. | `_series_ref_recut` | mcp/src/agents_remember/worktrees/reopen.py:784-818 |
| The reopen clears the review counter a completion spent, and only when the counter carries history. | `_review_state_carries_history`; `_plan_series_document_reset` | mcp/src/agents_remember/worktrees/reopen.py:1042-1062; mcp/src/agents_remember/worktrees/reopen.py:1065-1117 |
| The publication `mode` (`reset` or `publish`) is decided by the arrival, not by a caller flag. | `_series_reopen_plan` | mcp/src/agents_remember/worktrees/reopen.py:1120-1189 |
| Parent lineage compares exact prestart output positions to the configured parent source. | `parent_source_lineage` | mcp/src/agents_remember/worktrees/source_lineage.py:79-91 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-20T02:05:20+00:00: Generated citation repair: `_series_in_flight` repointed to mcp/src/agents_remember/worktrees/reopen.py:1003-1012. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T02:05:20+00:00: Generated citation repair: `_series_is_live_unaddressed` repointed to mcp/src/agents_remember/worktrees/reopen.py:1015-1039. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T02:05:20+00:00: Generated citation repair: `_review_state_carries_history`; `_plan_series_document_reset` repointed to mcp/src/agents_remember/worktrees/reopen.py:1042-1062; mcp/src/agents_remember/worktrees/reopen.py:1065-1117. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T02:05:20+00:00: Generated citation repair: `_series_reopen_plan` repointed to mcp/src/agents_remember/worktrees/reopen.py:1120-1189. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-20T02:50+02:00 — 260915-KS-L34 curator (uncommitted change set on `ar/260915-ks-l34-ar`, code base `0da444b3`): **the series half of this route is now described here, and this card's own citation rows were re-derived against the file as it stands.** The body gained the three deciding facts and the counter reset — `_series_in_flight` reading the two progress cells a completion writes rather than `cleanup` (the reopen rewrites `cleanup` as its own first durable step, so keying on it would make the rule's answer depend on whether the reset had been written), `_series_ref_recut` accepting an integration branch strictly ahead of its source on the same line as the series' own landed work and reporting it `advance` without moving it, `_series_is_live_unaddressed` accepting a live series at an address whose generation is `terminal-archived` and publishing only the successor generation, and the current partial reset clearing a review counter that carries history. This card's own four rows had **drifted with the file's growth**: `_reopen_preflight_refusal` cited `:313-385` and is at `:325-398`, `_reopened_contract` cited `:187-214` and is at `:197-224`, and the frozen-observation row cited `:506-565` and is at `:519-579`. Each range was re-derived by reading the construct's own extent in the file rather than shifted by arithmetic, and five rows were added for the series owners. No verification stamp advanced and none was invented: the candidate is uncommitted, the governed closeout owns the real code and memory commits, and the metadata carries a `reviewedWorkingCandidate` row naming this candidate because the body moved under the retained pair.

2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Replaced terminal ledger mapping and integrated ledger base with the accepted memory output and real ancestry; retained exact terminal/parent lineage, typed reset cells, frozen-observation clearing, and rollback-safe task publication. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the parent-series rename
  is the frozen change and this card already records it in three places. Re-checked its ranges: they
  hold. No wording changed. Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees/reopen.py` changed since the recorded verification commit.
  Re-read the card against the frozen on-disk source and re-checked its claims and cited ranges:
  nothing this card asserts is falsified by the change, so no wording changed. Verification metadata
  remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (reopened-claim judgement): the checker reopened
  the restamp-helper claim because `plan_leaf_doc_lifecycle_restamp` and
  `restamp_leaf_doc_lifecycle` changed after verification. Re-read the claim against
  `tasks/leaf_doc.py`: `find_leaf_doc` is at `:89`, the planner at `:237` and the publisher at
  `:263`, and the regenerated ranges cover each. The claim that this module shares those helpers
  with worktree start still holds. Retained; verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 1 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-13T20:42+02:00 — Child-admission seal removal (uncommitted change set on
  `ar/260831_lifecycle-owned-completion-relay`): recorded that the import and call in
  `_reopen_preflight_refusal` now name `require_parent_series` instead of
  `require_parent_series_accepting_leaves`, described what that preflight gate actually does (blocker
  list, parent-series resolution, external-ledger mapping), and recorded that the deleted
  `atomic_series_seal.py` no longer seals reopen — a master that took a checkpoint landing no longer
  locks its own leaves. Verification metadata remains closeout-owned; no acceptance claim and no
  verification stamp advanced.
- 2026-09-13T14:32+02:00 — Curator citation repoint after the contract-scoped atomic-series activation re-keying shifted `models/worktree.py`: the `class ContractCells:` / `def amend_contract(` / `CleanupStatus = Literal[` anchors were re-paired with the files that actually carry them — `worktrees/worktree_contract.py:180-189`, `worktrees/worktree_contract.py:197-225` and `models/worktree.py:39-39`. Claim wording unchanged.
- 2026-09-13T12:29:52+00:00: Generated citation repair: "CleanupStatus = Literal[" repointed to mcp/src/agents_remember/models/worktree.py:39-39. No content impact: mechanical anchor-range projection bound to citation source snapshot 608ec827a174d194b141ff2daa61dd8e3b6b44611d03fb561dc0b7bb0223223f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:53:11+00:00: Generated citation repair: "CleanupStatus = Literal[" repointed to mcp/src/agents_remember/models/worktree.py:40-40. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T01:06:15+00:00: Generated citation repair: "CleanupStatus = Literal[" repointed to mcp/src/agents_remember/models/worktree.py:39-39. No content impact: mechanical anchor-range projection bound to citation source snapshot 1740540b8733028dd833a3538d739271e8925ea5f51911a0f8dcd8c49e7e1c13; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T23:05:00+00:00: The one-task-fact-CAS row anchored the bare symbol `publish_task_fact_mutation`, which resolved twice at the cited verification commit (import and call), so the claim could not be compared with its provenance. The anchor is now the publication function `_publish_reopen_transition` plus the exact call text `published = publish_task_fact_mutation(`, both of which occur once inside `reopen.py:471-492`; the cited extent and the claim's wording are unchanged.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: "CleanupStatus = Literal[", "_validate_reopen_row_path(master_path", "class ContractCells:", "def _plan_master_index_reset(", "def amend_contract(", "updated = demote_completed_master_if_unresolved(TaskDocument.model_validate(data))" repointed to mcp/src/agents_remember/models/worktree.py:34-34, mcp/src/agents_remember/worktrees/reopen.py:579-579, mcp/src/agents_remember/worktrees/reopen.py:615-615, mcp/src/agents_remember/worktrees/reopen.py:617-617, mcp/src/agents_remember/worktrees/worktree_contract.py:180-180, mcp/src/agents_remember/worktrees/worktree_contract.py:197-197. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "existing.cleanup in (\"abandoned\", \"reopened\")" repointed to mcp/src/agents_remember/worktrees/modules/start.py:570-570. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "class ContractCells:" repointed to mcp/src/agents_remember/worktrees/worktree_contract.py:180-180. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "def amend_contract(" repointed to mcp/src/agents_remember/worktrees/worktree_contract.py:197-197. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "existing.cleanup in (\"abandoned\", \"reopened\")" repointed to mcp/src/agents_remember/worktrees/modules/start.py:516-516. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T16:45:00+02:00 — CCR-L38 final preparation repair: repointed frozen-source citations after the final contract diagnostic; no behavioral prose change, no verification or acceptance claim.

- 2026-09-05T08:46+02:00 — L31 scoped MCP curator: reviewed 2 declined citation claims against frozen code `ea35964985f30080488270e71ac81657ac40682b`. Separated cleanup vocabulary from the typed amendment record and helper. Kept the prose claim and repaired its precise definitions and cleanup literal. Existing verification hash/date are retained; this scoped source read and citation repair do not certify the entire card or a gate.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: merged exact terminal-predecessor proof, task-CAS publication, and independent projection refresh into reopen. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: imports updated to the moved packages; contract reset extracted into `_reopened_contract`. Verified at code commit e5cb139f.



- 2026-08-20T10:45+02:00 — 260815-DAG-L12 curator: re-anchored citation range(s) to current source after the L12 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16 curator: re-anchored the `task_reopen_tool` citation to its current re-export line (task_doc_tools.py:87) and advanced the card verification stamp to the L16 tree; card source (worktrees/reopen.py) itself is unchanged by L16.

- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 moved the `task_reopen_tool` facade re-export within `task_doc_tools.py`; re-pointed the citation to `task_doc_tools.py:83-85`. Verification metadata unchanged.

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: reopen now passes `memory_source_commit` to the external-ledger mapping proof. Verification remains closeout-owned.

- 2026-08-16T07:15+02:00 — L4 review repair: moved leaf/master reset planning into the locked publication so concurrent task-doc edits cannot be overwritten by stale preflight models.
- 2026-08-16T07:05+02:00 — L4 review repair: moved the exact terminal contract, source-tip, and external-ledger proof into the locked reopen publication boundary before any evidence is erased.

- 2026-08-16T06:15+02:00 — Dagger repair: terminal reopen now validates the current source pair against the leaf's exact landed commits, preserving own-atomic reopen without admitting source drift.

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: replaced the retired direct restamp/publication
  claim with the queue-governed reopen transaction and preserved rollback semantics; verification
  remains closeout-owned.
- 2026-08-14T05:26Z — L23 final curator: replaced the deleted `_reset_leaf_doc` account with the
  atomic `_plan_leaf_doc_reset` planning boundary. Verification remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented parent-lineage admission before reopen mutation and thematic-master recovery; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T12:41:53+00:00 — 260731-EFA-L6 S18-B09 curator: split recreate-fresh admission, contract write, and lifecycle restamp onto their frozen-source owners; the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-08-02T01:05+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/tasks/reopen.py` became `mcp/src/agents_remember/worktrees/reopen.py`, so this sidecar moved with it; `path`, the H1, and `governingOverview` (now `../../../overview.md`, matching the five sibling cards in this route — `worktrees/` has no route-local overview) follow. **The Purpose's stated rationale was inverted, not just re-pathed.** It read "it lives in the tasks package ... because the thing being reopened is the task"; the module now says the opposite and gives the reason: reopen rewrites the leaf's ENCLOSURE CONTRACT, emits a `WorktreeCommandResult` and renders through the worktree status payload, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent (`layers.toml`) — the task-document store could not be loaded without the whole worktree lifecycle. Behavior is unchanged; only the home and the justification are. Every self-citation was re-derived against the file at its new path rather than shifted by arithmetic — the module docstring was rewritten in the move, so all of them moved: `reopen_task` L45-L112 → L53-L120, `_reopen_blockers` L137-L151 → L145-L159, the split contract rewrite L63-L88 → L71-L96, the vocabulary cells L82-L87 → L90-L95, `_reset_leaf_doc` L154-L187 → L162-L195, `_reset_master_index` L190-L208 → L198-L216. The `worktree_contract.py` cross-file anchors also moved and were re-derived: `CleanupStatus` L55 → L67, `ContractCells` L171 → L183, `amend_contract` L188 → L200. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T10:12+02:00 — 260731-EFA-L4 curator: body corrected. The card now records that free-form
  provenance uses `dataclasses.replace`, vocabulary cells use `amend_contract(..., ContractCells(...))`,
  and `CleanupStatus` admits `reopened`; the current reference rows bind those claims to the frozen
  source. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 1 stale self-citation. Purpose cited
  the `task_reopen` implementation at L11, which is now a line inside the module docstring; the
  entry point is `reopen_task` at L43-L102 (the module docstring grew to L1-L22 and the
  landing-freeze imports/helper landed after it). Named the function explicitly so the anchor is
  self-checking. Claim unchanged.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-03T00:30+02:00 — Created for L11 (leaf reopen semantics): `reopen_task` resets a completed
  leaf's contract and doc back to planning under its original leaf id, replacing the suffixed `-rN`
  reopen workaround. Verification metadata pinned until closeout stamps the code commit.
