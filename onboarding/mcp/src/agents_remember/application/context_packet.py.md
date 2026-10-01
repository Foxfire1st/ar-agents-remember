# mcp/src/agents_remember/application/context_packet.py

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
- Worktree status projection supplies the read-only worktree summary — as the MODEL: `worktree_status_packet` (L14-L49) returns `WorktreeSummary`, so there is no dict boundary here to validate. [3]
- `DriftSummaryPacket` (L17-L20) — the `TypedDict` `_drift_packet` now returns — and `DriftStatus` (declared in `models/drift.py`). [4]
- Public payload builder validates this application entry point output through the model registry. [5]
- Branch freshness facts (upstream, fetch, ahead/behind) come from the freshness kernel. [6]
- `ledgerMapsCodeHead` reuses the ledger loader and mapping lookup. [7]

## 260821-CLIVE-L2 Current Contract

The current source seams include `ContextPacketError`, `ContextPacketRequest`, `build_context_packet`. This read-only degraded projector is intentionally distinct from configured-contract mutation admission: it may report unreadable/pre-adoption lifecycle facts, but it cannot mutate, adopt, migrate, or invent normal authority.

### Reconciled Source Evidence

- The current module exposes `ContextPacketError`, `ContextPacketRequest`, `build_context_packet` at this ownership boundary. [8]
