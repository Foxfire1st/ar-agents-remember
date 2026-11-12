# mcp/src/agents_remember/application/context_packet.py

## Current operative account — orientation and internal packet

`build_context_packet` retains rich V2 context for internal/CLI/dashboard consumers and optionally reports the derived index. The mounted payload applies `slim_context_packet`: version 3, shared roots, optional readable active-leaf task ID/master, action lines only where needed, optional serving build and paired commits. `roots.code` is absolute; join shorter relative memory, enclosure and task-document paths to it. Settings/storage/provider policy blocks do not travel in the mounted answer. A partial index asks for action; an unreadable index is omitted.

The tool log preserves the delivered slim answer, not an automatic V2 dump. `include_freshness=true` may fetch remotes; default reads do not fetch. Root factoring is a compactness mechanism, not proof of a universal token ceiling for arbitrary names. The older rich-wire account below is internal/historical context, not the mounted answer.

### Preserved provider-knob removal


The current source facts below replace the former operative inventory. The separately labelled superseded claims describe only the pre-repair card. Original paragraphs, dated closures, evidence and citation identities remain intact in the explicitly historical section; they grant no current call, restored route or fresh execution acceptance.

- Provider inclusion/detail knobs are gone: `build_context_packet` calls `provider_summary_packet(config)` with no inclusion parameter, so the provider block is the retired skipped summary.
- With `include_drift=false` the drift block is `not-checked`. When drift is requested for an existing unconverted memory directory, `_drift_packet` returns `status: "error"` and the shared `legacy_format_refusal` message for `context_packet`, without measuring drift. This is unconditional: a converted branch elsewhere is not an admission prerequisite. Convert first through the procedure named by the refusal, then repeat; a missing root still reaches the existing summary error.

### Superseded inventory

- Pre-repair card claim: Card directs detailed troubleshooting to provider_diagnostics. This is superseded archival wording, not a current prescription.

### Source and authority bounds

- Source comparison: `mcp/src/agents_remember/application/context_packet.py:113-115` (`provider_summary_packet(config)`).
- Source comparison: `mcp/src/agents_remember/models/tools/public_roster.py:22 (PUBLIC_TOOLS =)`.

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

## Current source contract evidence


- Current candidate source supports the operative account; historical sections grant no current tool or execution acceptance. [12]


## Historical original card — preserved, not the current operative account

<details>
<summary>Retained original source accounts and producer history</summary>

## Governing Overview

[application overview](overview.md)

## Purpose

`context_packet.py` builds the modeled `ContextPacketV2` startup packet that
agents use to learn repository, coordination, memory, worktree, provider, and
optional drift and branch-freshness facts.

## Code Commentary

`build_context_packet()` resolves the allowed repo ID, builds coordination
context — since 260731-EFA-L2 through `resolve_coordination_context(...,
hints=CoordinationHints(coordination_root, onboarding_root),
selector=EnclosureSelector(contract_path))` rather than five loose keyword arguments — reads Git
facts, projects paths and memory state into explicit
Pydantic nested models, obtains read-only worktree status, obtains compact
provider summary status, and adds a drift summary only when requested. The
application entry point validates the serialized provider summary through
`ProviderSummary.model_validate(...)` cit:(["ProviderSummary.model_validate("], mcp/src/agents_remember/application/context_packet.py:97-97) before inserting it into the packet, then
returns the JSON-compatible model dump of `ContextPacketV2` cit:(["ContextPacketV2("], mcp/src/agents_remember/application/context_packet.py:87-87).

**Two of the five nested blocks stopped being adapter boundaries in 260731-EFA-L4**, because
the producer now hands over the typed thing rather than a dict:

- `worktree=worktree_status_packet(context.contract_path)` cit:([`build_context_packet`], mcp/src/agents_remember/application/context_packet.py:64-110) — **no
  `WorktreeSummary.model_validate(...)`**. `application.worktree_status.worktree_status_packet` returns the
  model. The old `dict[str, Any]` return is what let a value the worktree state machine can emit
  and this packet cannot accept survive every type check up to the moment the packet was built,
  at which point the `ValidationError` escaped the `@server.tool()` handler — nothing on this
  path catches one. Constructing the model at the projection puts the checker on the seam
  instead.
- A leaf context that names an enclosure contract compares against the application-owned converted base
  for that leaf (`_leaf_drift_base`), so this route agrees with the drift tool on the same candidate and
  contract; a context without a contract keeps today's semantics with no separate base.
- `_drift_packet(...)` cit:(["def _drift_packet("], mcp/src/agents_remember/application/context_packet.py:177-177) is typed `-> DriftSummaryPacket`, the `TypedDict` from
  `memory_quality.integrity.onboarding_drift_check.models`, instead of `dict[str, Any]`. Its
  `status` is the producer's `DriftStatus`, whose `error` member — and the matching `error` key —
  `DriftSummary` now accepts, so `include_drift=true` against a repo with no onboarding root
  reports the reason rather than raising out of the tool.

The four that remain "repo=RepoSummary.model_validate(git_facts_to_packet(git_facts))" boundaries — cit:(["repo=RepoSummary.model_validate(git_facts_to_packet(git_facts))"], mcp/src/agents_remember/application/context_packet.py:89-89), cit:(["from agents_remember.models.providers import ProviderSummary"], mcp/src/agents_remember/application/context_packet.py:42-42), cit:(["drift=DriftSummary.model_validate(_drift_packet(request"], mcp/src/agents_remember/application/context_packet.py:105-105) and cit:(["from agents_remember.kernel.git_freshness import freshness_to_packet"], mcp/src/agents_remember/application/context_packet.py:19-19) — are the ones whose producers legitimately hand over a dict; their
vocabularies are covered instead by the wire models importing the producer's `Literal`
(`RepoState`, `FreshnessState`, `DriftStatus`).

Provider summary still performs the underlying provider status/current-state
read so runtime state remains current, but the context packet only receives
compact readiness, runtime, identity, watcher, target-repo, and recovery-action
facts. Detailed provider internals are intentionally moved to the
`provider_diagnostics` tool.

`_freshness_packet()` (issue #54) adds the opt-in `freshness` section: with
`include_freshness=true` on `ContextPacketRequest` it reads
`kernel.git_freshness.read_branch_freshness` for the code repo and — when the
memory root is a git repo — for the external memory repo (each performs one
bounded `git fetch` of the upstream remote, `fetch_timeout` default 30s), and
reports `ledgerMapsCodeHead` by running `find_mapping` over the official
`memory.md` ledger against code HEAD (skipped when the ledger file is absent;
parse failures land in `ledgerError` instead of raising). The default request
leaves the section as `{"status": "not-checked"}`, mirroring the drift
`not_checked()` convention, so everyday packets stay fast and offline-safe. The
l-01 trust checkpoint is the intended opt-in caller.

## Invariants And Boundaries

- Repo IDs must be allowed by MCP settings.
- `ContextPacketError` (the authority-gate failure raised when the request
  violates MCP authority settings) subclasses `AuthorityError` from
  `agents_remember.errors`, not bare `ValueError`.
- Context packet version is now `contextPacketVersion: 2`.
- Do not embed `rawStatus`, duplicated top-level `pathRules`, or full provider
  current-state payloads in this application entry point.
- Construct nested model objects explicitly, or validate raw service payloads
  at narrow adapter boundaries with `NestedModel.model_validate(...)`.
- **Prefer a producer that returns the model over an adapter that validates a
  dict.** `worktree` is built, not validated, because `application.worktree_status` can
  return `WorktreeSummary`; a `dict[str, Any]` in between is where an
  unacceptable value hides until pydantic raises it inside this tool handler,
  which has no `except` for a `ValidationError`.
- Where a dict boundary is genuine, the wire model must import the producer's
  vocabulary rather than retype it — that is what keeps `repo`, `drift` and
  `freshness` honest here.
- Keep the provider-summary validation boundary in this application entry point; skipped
  provider fields that are omitted from JSON must be modeled as optional in the
  provider response model, not bypassed by removing validation here.
- Context packet construction may read provider status and write current-state
  snapshots through the provider status path; it must not start providers or
  mutate onboarding.
- The freshness section's only repository mutation is the optional
  remote-tracking fetch inside `read_branch_freshness`; it never touches
  working trees, and fetch/ledger failures degrade to `unknown`/`ledgerError`
  data instead of failing the packet.

## Evidence

### Repo-Internal References

- `ContextPacketV2` and nested summary models define the response shape. [1]

- Provider summary projection keeps context compact and points details at diagnostics. [2]


- Worktree status projection supplies the read-only worktree summary — as the MODEL: `worktree_status_packet` returns `WorktreeSummary`, so there is no dict boundary here to validate. [3]

- `DriftSummaryPacket` (L17-L20) — the `TypedDict` `_drift_packet` now returns — and `DriftStatus` (declared in `models/drift.py`). [4]

- Public payload builder validates this application entry point output through the model registry. [5]

- Branch freshness facts (upstream, fetch, ahead/behind) come from the freshness kernel. [6]
- `ledgerMapsCodeHead` reuses the ledger loader and mapping lookup. [7]

## 260821-CLIVE-L2 Current Contract

The current source seams include `ContextPacketError`, `ContextPacketRequest`, `build_context_packet`. This read-only degraded projector is intentionally distinct from configured-contract mutation admission: it may report unreadable/pre-adoption lifecycle facts, but it cannot mutate, adopt, migrate, or invent normal authority.

### Reconciled Source Evidence


- The current module exposes `ContextPacketError`, `ContextPacketRequest`, `build_context_packet` at this ownership boundary. [8]


- A leaf drift block compares against the leaf's converted base and agrees with the drift tool. [9]

</details>

- Slim orientation factors shared roots and optional task/actions/build/pair fields without rich policy blocks. [10]

- Rich V2 assembly remains internal and optionally includes index facts. [11]
