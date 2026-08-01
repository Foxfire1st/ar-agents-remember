# mcp/src/agents_remember/controllers/context_packet.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/controllers/context_packet.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T10:07+02:00                     |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                              |

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
controller validates the serialized provider summary through
`ProviderSummary.model_validate(...)` (L89-L96) before inserting it into the packet, then
returns the JSON-compatible model dump of `ContextPacketV2` (L102).

**Two of the five nested blocks stopped being adapter boundaries in 260731-EFA-L4**, because
the producer now hands over the typed thing rather than a dict:

- `worktree=worktree_status_packet(context.contract_path)` (L88) — **no
  `WorktreeSummary.model_validate(...)`**. `worktrees.status.worktree_status_packet` returns the
  model. The old `dict[str, Any]` return is what let a value the worktree state machine can emit
  and this packet cannot accept survive every type check up to the moment the packet was built,
  at which point the `ValidationError` escaped the `@server.tool()` handler — nothing on this
  path catches one. Constructing the model at the projection puts the checker on the seam
  instead.
- `_drift_packet(...)` (L169-L180) is typed `-> DriftSummaryPacket`, the `TypedDict` from
  `memory_quality.integrity.onboarding_drift_check.models`, instead of `dict[str, Any]`. Its
  `status` is the producer's `DriftStatus`, whose `error` member — and the matching `error` key —
  `DriftSummary` now accepts, so `include_drift=true` against a repo with no onboarding root
  reports the reason rather than raising out of the tool.

The four that remain `model_validate` boundaries — `repo` (L81), `providers` (L89), `drift`
(L97) and `freshness` (L98) — are the ones whose producers legitimately hand over a dict; their
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
  current-state payloads in this controller.
- Construct nested model objects explicitly, or validate raw service payloads
  at narrow adapter boundaries with `NestedModel.model_validate(...)`.
- **Prefer a producer that returns the model over an adapter that validates a
  dict.** `worktree` is built, not validated, because `worktrees.status` can
  return `WorktreeSummary`; a `dict[str, Any]` in between is where an
  unacceptable value hides until pydantic raises it inside this tool handler,
  which has no `except` for a `ValidationError`.
- Where a dict boundary is genuine, the wire model must import the producer's
  vocabulary rather than retype it — that is what keeps `repo`, `drift` and
  `freshness` honest here.
- Keep the provider-summary validation boundary in this controller; skipped
  provider fields that are omitted from JSON must be modeled as optional in the
  provider response model, not bypassed by removing validation here.
- Context packet construction may read provider status and write current-state
  snapshots through the provider status path; it must not start providers or
  mutate onboarding.
- The freshness section's only repository mutation is the optional
  remote-tracking fetch inside `read_branch_freshness`; it never touches
  working trees, and fetch/ledger failures degrade to `unknown`/`ledgerError`
  data instead of failing the packet.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `ContextPacketV2` and nested summary models define the response shape. | [context_packet.py](agents-remember/mcp/src/agents_remember/models/context_packet.py) |
| Provider summary projection keeps context compact and points details at diagnostics. | [status.py](agents-remember/mcp/src/agents_remember/providers/status.py) |
| Worktree status projection supplies the read-only worktree summary — as the MODEL: `worktree_status_packet` (L14-L49) returns `WorktreeSummary`, so there is no dict boundary here to validate. | [status.py](agents-remember/mcp/src/agents_remember/worktrees/status.py) |
| `DriftSummaryPacket` (L17-L20) — the `TypedDict` `_drift_packet` now returns — and `DriftStatus` (L14), the alias both drift wire models read. | [onboarding_drift_check/models.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py) |
| Public payload builder validates this controller output through the model registry. | [core.py](agents-remember/mcp/src/agents_remember/mcp/tools/core.py) |
| Branch freshness facts (upstream, fetch, ahead/behind) come from the freshness kernel. | [git_freshness.py](agents-remember/mcp/src/agents_remember/kernel/git_freshness.py) |
| `ledgerMapsCodeHead` reuses the ledger loader and mapping lookup. | [memory_ledger.py](agents-remember/mcp/src/agents_remember/kernel/memory_ledger.py) |

## Update History

- 2026-08-01T10:07+02:00 — 260731-EFA-L4 curator: body updated. Two of the five nested blocks
  stopped being `model_validate` adapter boundaries, and the card described all five the same
  way. `worktree=` (L88) no longer calls `WorktreeSummary.model_validate(...)` —
  `worktrees.status.worktree_status_packet` (L14-L49 there) returns the model, which moves "a
  value the state machine emits and this packet rejects" from a runtime `ValidationError` inside
  a handler with no `except` to a type error at the projection; the `WorktreeSummary` import was
  dropped from this file accordingly. `_drift_packet` (L169-L180) is now typed
  `-> DriftSummaryPacket` (the producer's `TypedDict`) instead of `dict[str, Any]`, and the
  `DriftSummary` it feeds now accepts the `error` status and key, so `include_drift=true` against
  a repo without an onboarding root reports the reason instead of raising. Named the four blocks
  that remain genuine dict boundaries and why they are safe (their wire models import the
  producer's `Literal`). Added two invariants. Citations: `build_context_packet`'s construction
  sites pinned — `repo` L81, `worktree` L88, `providers` L89-L96, `drift` L97, `freshness` L98,
  the dump L102, `_freshness_packet` L105-L132, `_drift_packet` L169-L180; the `status.py`
  reference row was re-pointed to `worktree_status_packet` L14-L49 with its new return type, and
  a row was added for the drift-check models module (L14, L17-L20). Verification metadata pinned
  until closeout stamps the L4 commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: the `resolve_coordination_context` call moved onto the
  resolver's new `CoordinationHints` / `EnclosureSelector` parameter objects. Packet contents,
  request flags and validation boundaries are unchanged. Verification metadata pinned until
  closeout stamps the L2 code commit.
- 2026-06-10T08:39+02:00: Added the opt-in `freshness` section (issue #54): `include_freshness`/`fetch_timeout` on the request, `_freshness_packet()` with code+memory `read_branch_freshness` and the `ledgerMapsCodeHead` mapping check; default stays `not-checked`.
- 2026-06-08T09:57+02:00: Restored the provider-summary model-validation boundary after skipped provider summaries moved the omitted nullable `ok` contract into the provider response model.
- 2026-06-06T12:28+02:00: Corrected the context-packet payload-builder reference after the former `mcp/tools.py` module became the `mcp/tools/` package; source behavior unchanged.
- 2026-05-31T12:50+02:00 — `ContextPacketError` re-typed to subclass `AuthorityError` (imported from `agents_remember.errors`) instead of `ValueError`; noted the new base in Invariants And Boundaries (1.0.0 review remediation).
- 2026-05-28T19:52+02:00: Updated after context packets moved to explicit `ContextPacketV2` model construction and compact provider summaries.
- 2026-05-24T02:47+02:00: Created after context packets imported drift summary from the new memory quality package.
