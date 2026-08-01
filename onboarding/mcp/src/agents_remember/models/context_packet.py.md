# mcp/src/agents_remember/models/context_packet.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/context_packet.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T09:26+02:00                     |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`context_packet.py` defines `ContextPacketV2`, the compact startup/bootstrap
response contract for `context_packet`.

## Code Commentary

The model separates repository Git facts, resolved paths, memory/storage facts,
worktree summary, provider summary, and drift summary into explicit nested
objects. `ContextPacketV2` (L115-L125) fixes `contextPacketVersion` to `2` and
carries a diagnostics hint pointing agents at `provider_diagnostics` for raw
provider details.

**Three of this file's vocabularies are imported from their producers, not
retyped here** (L9-L15) — the same rule the four gate/lifecycle/inbox/
orchestration models already followed:

- `RepoSummary.state` (L27) is `RepoState`, from `kernel.git_facts` (L22 there),
  the module that decides it. The packet assembles this block as
  `RepoSummary.model_validate(git_facts_to_packet(...))` over an untyped dict, so
  a retyped copy here would let a new degrade path reach pydantic before it
  reaches a reviewer.
- `MemorySummary.mode` (L85) is `MemoryMode`, from
  `worktrees.worktree_contract` (L51 there). It **was**
  `Literal["internal", "external"]` and was the only copy in the package missing
  `disabled` — `CoordinationContext.memory_mode` has always been able to carry it
  and `WorktreeSummary.memoryMode` in the *same response* declared it correctly,
  so one packet could pass `memoryMode="disabled"` and fail `memory.mode` on the
  identical value.
- `BranchFreshness.state` (L99) is `FreshnessState`, from
  `kernel.git_freshness` (L29-L38 there). `freshness_to_packet` hands over a
  plain dict, and half that vocabulary exists only on degrade paths a hand-copied
  `Literal` would be the last to hear about.

`FreshnessSummary` (L103-L108, issue #54) is the opt-in branch-freshness section:
`status` is `checked`/`not-checked` (defaulting like drift's not-checked), with
optional `BranchFreshness` blocks (L90-L100) for the code and memory repos
(`branch`, `upstream`, `fetched`, `ahead`/`behind`, `state`) plus
`ledgerMapsCodeHead`/`ledgerError`. The eight `state` members —
`current`/`behind`/`ahead`/`diverged` for a comparison that succeeded,
`no-upstream`/`no-branch`/`unknown`/`unavailable` for why one could not be made —
are now read off `FreshnessState` rather than listed here.
`ContextPacketV2.freshness` uses `default_factory=FreshnessSummary` so omitted
requests serialize as `{"status": "not-checked"}` under `exclude_none`.

`ContextPacketV2.worktree` is a `WorktreeSummary`, and its controller no longer
validates a dict into it — `worktrees.status.worktree_status_packet` returns the
model. `ContextPacketV2.drift` is `DriftSummary`, which since L4 also carries an
`error` field so `include_drift=true` against a repo with no onboarding root
reports why instead of raising.

## Invariants And Boundaries

- `memory.storage.pathRules` is the only path-rule location in the context
  packet contract.
- `rawStatus`, provider current-state internals, and duplicated raw provider
  payloads do not belong in `ContextPacketV2`.
- Nested model objects should be built explicitly or validated at narrow raw
  adapter boundaries.
- **A vocabulary this packet does not produce is imported, never retyped.**
  `RepoState`, `MemoryMode` and `FreshnessState` belong to `kernel.git_facts`,
  `worktrees.worktree_contract` and `kernel.git_freshness` respectively. A local
  copy is only ever measured against the producer when a real payload carries
  the new member — as a `ValidationError`, inside a tool handler with no
  `except` for one.
- **The same value must mean the same thing on every field of one response.**
  `memory.mode` and `worktree.memoryMode` are both `MemoryMode`; they cannot
  disagree about `disabled` again because they are now the same declaration.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The context controller constructs `ContextPacketV2` from resolver, Git, provider, worktree, and drift facts. | [context_packet.py](agents-remember/mcp/src/agents_remember/controllers/context_packet.py) |
| Provider readiness in the packet uses compact provider summary models. | [providers.py](agents-remember/mcp/src/agents_remember/models/providers.py) |
| `RepoState` (L22) and its `VALID_REPO_STATES` (L26); `git_facts_to_packet` (L104-L115) is the untyped dict `RepoSummary` validates. | [git_facts.py](agents-remember/mcp/src/agents_remember/kernel/git_facts.py) |
| `FreshnessState` (L29-L38) and `VALID_FRESHNESS_STATES` (L41); `freshness_to_packet` (L158-L169). | [git_freshness.py](agents-remember/mcp/src/agents_remember/kernel/git_freshness.py) |
| `MemoryMode` (L51) — the one declaration `memory.mode` and `worktree.memoryMode` now share. | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| `worktree_status_packet` (L14-L49) returns `WorktreeSummary` directly, so this packet's `worktree` block is constructed, not validated. | [status.py](agents-remember/mcp/src/agents_remember/worktrees/status.py) |

## Update History

- 2026-08-01T09:26+02:00 — 260731-EFA-L4 curator: body corrected. Three fields here declared their
  own copy of a vocabulary owned elsewhere, and one copy was wrong: `MemorySummary.mode` was
  `Literal["internal", "external"]` while `CoordinationContext.memory_mode` and
  `WorktreeSummary.memoryMode` — the latter in the SAME response — both accepted `disabled`, so
  one packet could pass `memoryMode="disabled"` and fail `memory.mode` on the identical value. All
  three now import: `RepoSummary.state` → `RepoState` (`kernel.git_facts` L22),
  `MemorySummary.mode` → `MemoryMode` (`worktrees.worktree_contract` L51),
  `BranchFreshness.state` → `FreshnessState` (`kernel.git_freshness` L29-L38). Rewrote the
  `FreshnessSummary` paragraph, which had listed four of the eight `state` members inline — that
  hand-list is exactly the artefact the import removes. Noted that `worktree` is now constructed
  rather than `model_validate`d and that `DriftSummary` gained an `error` field. Added two
  invariants. Citations: `ContextPacketV2` L115-L125, `FreshnessSummary` L103-L108,
  `BranchFreshness` L90-L100, `RepoSummary.state` L27, `MemorySummary.mode` L85,
  `BranchFreshness.state` L99, import block L9-L15; new reference rows for `git_facts.py`
  (L22/L26/L104-L115), `git_freshness.py` (L29-L38/L41/L158-L169), `worktree_contract.py` (L51)
  and `worktrees/status.py` (L14-L49). Verification metadata pinned until closeout stamps the L4
  commit.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/models/context_packet.py` since the L2 base commit is the whole-tree
  `ruff format` pass in `00e8379`, which re-wrapped 8 line(s), touching only magic trailing
  commas. Checked by parsing both revisions and comparing the abstract syntax trees (identical)
  and the comment tokens (identical), so no symbol, signature, default, decorator, control-flow
  branch, docstring, or assertion this card describes has moved, and every claim this card makes
  about its own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-06-10T08:39+02:00: Added `BranchFreshness` and `FreshnessSummary` and the `ContextPacketV2.freshness` field (issue #54 opt-in freshness section).
- 2026-05-28T19:52+02:00: Created after context packets moved to the compact V2 Pydantic contract.
