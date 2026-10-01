# mcp/src/agents_remember/models/context_packet.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`context_packet.py` defines `ContextPacketV2`, the compact startup/bootstrap
response contract for `context_packet`.

## Code Commentary

The model separates repository Git facts, resolved paths, memory/storage facts,
worktree summary, provider summary, and drift summary into explicit nested
objects. cit:([`ContextPacketV2`], mcp/src/agents_remember/models/context_packet.py:114-124) fixes `contextPacketVersion` to `2` and
carries a diagnostics hint pointing agents at `provider_diagnostics` for raw
provider details.

**Three of this file's vocabularies are imported from their producers, not
retyped here** (cit:(["from agents_remember.kernel.git_facts import RepoState", "from agents_remember.kernel.git_freshness import FreshnessState", "from agents_remember.models.worktree import MemoryMode"], mcp/src/agents_remember/models/context_packet.py:9-15)) — the same rule the four gate/lifecycle/inbox/
orchestration models already followed:

- `RepoSummary.state` (cit:(["state: RepoState"], mcp/src/agents_remember/models/context_packet.py:26-26)) is `RepoState`, from `kernel.git_facts` (cit:(["RepoState = Literal["], mcp/src/agents_remember/kernel/git_facts.py:23-23)),
  the module that decides it. The packet assembles this block as
  `RepoSummary.model_validate(git_facts_to_packet(...))` over an untyped dict, so
  a retyped copy here would let a new degrade path reach pydantic before it
  reaches a reviewer.
- `MemorySummary.mode` (cit:(["mode: MemoryMode"], mcp/src/agents_remember/models/context_packet.py:84-84)) is `MemoryMode`, from
  `kernel.memory_mode` since L9 (cit:(["MemoryMode = Literal["], mcp/src/agents_remember/kernel/memory_mode.py:35-35)). It **was**
  `Literal["internal", "external"]` and was the only copy in the package missing
  `disabled` — `CoordinationContext.memory_mode` has always been able to carry it
  and `WorktreeSummary.memoryMode` in the *same response* declared it correctly,
  so one packet could pass `memoryMode="disabled"` and fail `memory.mode` on the
  identical value.
- `BranchFreshness.state` (cit:(["state: FreshnessState"], mcp/src/agents_remember/models/context_packet.py:98-98)) is `FreshnessState`, from
  `kernel.git_freshness` (cit:([`FreshnessState`], mcp/src/agents_remember/kernel/git_freshness.py:30-39)). `freshness_to_packet` hands over a
  plain dict, and half that vocabulary exists only on degrade paths a hand-copied
  `Literal` would be the last to hear about.

`FreshnessSummary` (cit:([`FreshnessSummary`], mcp/src/agents_remember/models/context_packet.py:102-107), issue #54) is the opt-in branch-freshness section:
`status` is `checked`/`not-checked` (defaulting like drift's not-checked), with
optional `BranchFreshness` blocks (cit:([`BranchFreshness`], mcp/src/agents_remember/models/context_packet.py:89-99)) for the code and memory repos
(`branch`, `upstream`, `fetched`, `ahead`/`behind`, `state`) plus
`ledgerMapsCodeHead`/`ledgerError`. The eight `state` members —
`current`/`behind`/`ahead`/`diverged` for a comparison that succeeded,
`no-upstream`/`no-branch`/`unknown`/`unavailable` for why one could not be made —
are now read off `FreshnessState` rather than listed here.
`ContextPacketV2.freshness` uses `default_factory=FreshnessSummary` so omitted
requests serialize as `{"status": "not-checked"}` under `exclude_none`.

`ContextPacketV2.worktree` is a `WorktreeSummary`, and its application entry point no longer
validates a dict into it — `application.worktree_status.worktree_status_packet` returns the
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

## Evidence

### Repo-Internal References

- The context application entry point constructs "packet = ContextPacketV2(" from resolver, Git, provider, worktree, and drift facts. [1]
- Provider readiness in the packet uses compact provider summary models. [2]
- `RepoState` (L22) and its `VALID_REPO_STATES` (L26); `git_facts_to_packet` (L104-L115) is the untyped dict `RepoSummary` validates. [3]
- `FreshnessState` (L29-L38) and `VALID_FRESHNESS_STATES` (L41); `freshness_to_packet` (L158-L169). [4]
- `MemoryMode` (L209) — the one declaration `memory.mode` and `worktree.memoryMode` now share (kernel-owned since L9). [5]
- `worktree_status_packet` (L65-L152) returns `WorktreeSummary` directly, so this packet's `worktree` block is constructed, not validated. [6]
