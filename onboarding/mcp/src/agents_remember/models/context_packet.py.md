# mcp/src/agents_remember/models/context_packet.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/context_packet.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                              |

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

- `RepoSummary.state` (cit:(["state: RepoState"], mcp/src/agents_remember/models/context_packet.py:26-26)) is `RepoState`, from `kernel.git_facts` (cit:(["RepoState = Literal["], mcp/src/agents_remember/kernel/git_facts.py:22-22)),
  the module that decides it. The packet assembles this block as
  `RepoSummary.model_validate(git_facts_to_packet(...))` over an untyped dict, so
  a retyped copy here would let a new degrade path reach pydantic before it
  reaches a reviewer.
- `MemorySummary.mode` (cit:(["mode: MemoryMode"], mcp/src/agents_remember/models/context_packet.py:84-84)) is `MemoryMode`, from
  `kernel.coordination_context.models` since L9 (cit:(["MemoryMode = Literal["], mcp/src/agents_remember/kernel/coordination_context/models.py:209-209)). It **was**
  `Literal["internal", "external"]` and was the only copy in the package missing
  `disabled` — `CoordinationContext.memory_mode` has always been able to carry it
  and `WorktreeSummary.memoryMode` in the *same response* declared it correctly,
  so one packet could pass `memoryMode="disabled"` and fail `memory.mode` on the
  identical value.
- `BranchFreshness.state` (cit:(["state: FreshnessState"], mcp/src/agents_remember/models/context_packet.py:98-98)) is `FreshnessState`, from
  `kernel.git_freshness` (cit:([`FreshnessState`], mcp/src/agents_remember/kernel/git_freshness.py:29-38)). `freshness_to_packet` hands over a
  plain dict, and half that vocabulary exists only on degrade paths a hand-copied
  `Literal` would be the last to hear about.

`FreshnessSummary` (cit:([`FreshnessSummary`], mcp/src/agents_remember/models/context_packet.py:102-107), issue #54) is the opt-in branch-freshness section:
`status` is `checked`/`not-checked` (defaulting like drift's not-checked), with
optional `BranchFreshness` blocks (cit:([`BranchFreshness`], mcp/src/agents_remember/models/context_packet.py:90-100)) for the code and memory repos
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The context application entry point constructs "packet = ContextPacketV2(" from resolver, Git, provider, worktree, and drift facts. | "packet = ContextPacketV2(" | mcp/src/agents_remember/application/context_packet.py:79-96 |
| Provider readiness in the packet uses compact provider summary models. | `ProviderSummary` | mcp/src/agents_remember/models/providers.py:75-93 |
| `RepoState` (L22) and its `VALID_REPO_STATES` (L26); `git_facts_to_packet` (L104-L115) is the untyped dict `RepoSummary` validates. | `RepoState`; `VALID_REPO_STATES`; `git_facts_to_packet` | mcp/src/agents_remember/kernel/git_facts.py:22-22; mcp/src/agents_remember/kernel/git_facts.py:26-26; mcp/src/agents_remember/kernel/git_facts.py:104-115 |
| `FreshnessState` (L29-L38) and `VALID_FRESHNESS_STATES` (L41); `freshness_to_packet` (L158-L169). | `FreshnessState`; `VALID_FRESHNESS_STATES`; `freshness_to_packet` | mcp/src/agents_remember/kernel/git_freshness.py:29-38; mcp/src/agents_remember/kernel/git_freshness.py:41-41; mcp/src/agents_remember/kernel/git_freshness.py:158-169 |
| `MemoryMode` (L209) — the one declaration `memory.mode` and `worktree.memoryMode` now share (kernel-owned since L9). | "MemoryMode = Literal[" | mcp/src/agents_remember/kernel/coordination_context/models.py:209-209 |
| `worktree_status_packet` (L14-L49) returns `WorktreeSummary` directly, so this packet's `worktree` block is constructed, not validated. | `worktree_status_packet` | mcp/src/agents_remember/application/worktree_status.py:61-143 |

## Update History
- 2026-09-06T22:41:21+00:00: Generated citation repair: `worktree_status_packet` repointed to mcp/src/agents_remember/application/worktree_status.py:61-143. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: corrected 4 citations: `MemoryMode` is declared at worktrees/worktree_contract.py L64 (was L63); the table row's inline line note updated to match. Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-08-03T10:15+02:00 — 260731-EFA-L6 W3-B07 curator: repaired all 20 assigned citation findings (5 missing anchors, 5 malformed sources, and 10 prose citations); final scoped check is clean.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:26+02:00 — 260731-EFA-L4 curator: body corrected. Three fields here declared their
  own copy of a vocabulary owned elsewhere, and one copy was wrong: `MemorySummary.mode` was
  `Literal["internal", "external"]` while `CoordinationContext.memory_mode` and
  `WorktreeSummary.memoryMode` — the latter in the SAME response — both accepted `disabled`, so
  one packet could pass `memoryMode="disabled"` and fail `memory.mode` on the identical value. All
  three now import: `RepoSummary.state` → `RepoState` (cit:([`RepoState`], mcp/src/agents_remember/kernel/git_facts.py:22-22)),
  `MemorySummary.mode` → `MemoryMode` (cit:(["MemoryMode = Literal["], mcp/src/agents_remember/kernel/coordination_context/models.py:209-209)),
  `BranchFreshness.state` → `FreshnessState` (cit:([`FreshnessState`], mcp/src/agents_remember/kernel/git_freshness.py:29-38)). Rewrote the
  `FreshnessSummary` paragraph, which had listed four of the eight `state` members inline — that
  hand-list is exactly the artefact the import removes. Noted that `worktree` is now constructed
  rather than `model_validate`d and that `DriftSummary` gained an `error` field. Added two
  invariants. Citations: cit:([`ContextPacketV2`], mcp/src/agents_remember/models/context_packet.py:114-124), cit:([`FreshnessSummary`], mcp/src/agents_remember/models/context_packet.py:102-107),
  cit:([`BranchFreshness`], mcp/src/agents_remember/models/context_packet.py:89-100), cit:(["state: RepoState"], mcp/src/agents_remember/models/context_packet.py:26-26), cit:(["mode: MemoryMode"], mcp/src/agents_remember/models/context_packet.py:84-84),
  cit:(["state: FreshnessState"], mcp/src/agents_remember/models/context_packet.py:98-98), cit:(["from agents_remember.kernel.git_facts import RepoState", "from agents_remember.kernel.git_freshness import FreshnessState", "from agents_remember.models.worktree import MemoryMode"], mcp/src/agents_remember/models/context_packet.py:9-9; mcp/src/agents_remember/models/context_packet.py:10-10; mcp/src/agents_remember/models/context_packet.py:14-14); new reference rows for `git_facts.py`
  (cit:([`RepoState`, `VALID_REPO_STATES`, `git_facts_to_packet`], mcp/src/agents_remember/kernel/git_facts.py:22-22; mcp/src/agents_remember/kernel/git_facts.py:26-26; mcp/src/agents_remember/kernel/git_facts.py:104-115), cit:([`FreshnessState`, `VALID_FRESHNESS_STATES`, `freshness_to_packet`], mcp/src/agents_remember/kernel/git_freshness.py:29-38; mcp/src/agents_remember/kernel/git_freshness.py:41-41; mcp/src/agents_remember/kernel/git_freshness.py:158-169), cit:(["MemoryMode = Literal["], mcp/src/agents_remember/kernel/coordination_context/models.py:209-209))
  and cit:([`worktree_status_packet`], mcp/src/agents_remember/application/worktree_status.py:21-56). Verification metadata pinned until closeout stamps the L4
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
