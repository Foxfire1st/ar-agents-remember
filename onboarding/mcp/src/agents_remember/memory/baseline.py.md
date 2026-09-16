# mcp/src/agents_remember/memory/baseline.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/baseline.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:16 |
| lastVerifiedCommitHash | `7cbda30d9a9a4c2944382fbef46ac58b85329935` |
| lastVerifiedCommitDate | 2026-09-15T05:15:42+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[Nearest governing overview](../../../overview.md)

Working-candidate verification: source inspected at 2026-09-15T01:16 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Inspects and adopts an existing external-memory onboarding baseline. Adoption creates an attributed
memory-content commit; the consumer ledger is computed from Git and refreshed as a disposable cache.

## Code Commentary

### Logic

`BaselineRequest`, `baseline_status`, and `baseline_adopt` are the service entry points. CLI parsing
adapts into the request object, and `resolve_request_context` passes topology and coordination hints
through the shared resolver. Drift discovery includes sidecar and inline onboarding and writes its
report before the adoption decision.

`ledger_status` reports the derived Git-history view or an unavailable-history diagnostic.
`base_payload` reuses that observation to classify `already-adopted` when readable history supplies a
memory-content commit, rather than performing a second unguarded history walk. Cache existence still
has no role in that decision.

A resolvable HEAD whose ancestry cannot be read reports top-level `unavailable`. `baseline_adopt`
returns that refusal before cache preparation, content staging, or ref mutation; accepting drift
cannot override unreadable history. An unborn repository has no resolvable HEAD, so its unavailable
initial walk does not by itself block bootstrap: it remains `ready` subject to the ordinary drift
rules. Drift reporting still precedes the adoption decision.

`has_adopted_baseline` remains the direct bootstrap guard inside `adopt_initial_baseline`. Actionable
drift still blocks new adoption unless `accept_drift` is explicit.

`adopt_initial_baseline` requires real onboarding, docs, or system content and the checked-out
repository-default memory branch. `_baseline_default_branch` also supports the exact unborn `main`
created by memory initialization, using its configured default-branch authority. It does not create,
switch, or commit an integration ref.

The code source-branch commit is resolved once. The fixed adoption subject is passed through
`render_memory_content_message`, so the resulting memory commit carries that exact `Code-Commit`
trailer. Cache preparation adds the ignore rule and removes the cached ledger from the index; the
shared `commit_if_dirty(..., exclude_paths=("memory.md",))` stages content without it. The returned
bootstrap contains `memoryContentCommit` and best-effort `ledgerCache`, with no ledger-only commit.

### Conventions

MCP application functions call the service directly rather than parsing CLI stdout. `dry_run`
defaults to false; an explicit dry run previews adoption. The kernel owns message rendering and
cache computation, while the shared Git module owns content staging.

### Invariants And Boundaries

- External topology, bootstrap branch ownership, and drift acceptance remain real admission rules.
- Cache existence, content, or a missing cache path cannot authorize or block adoption.
- A resolvable HEAD with unavailable ancestry cannot be adopted as a new baseline, even with drift accepted.
- Attribution is stored in the real memory commit, not reconstructed from a hand-written pair.
- Repeating adoption with readable attributed history returns `already-adopted` without another commit.

### Todos

No new file-local follow-up is established by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Context, drift, and Git-history adoption decisions. | L71-L82; L89-L114; L236-L245; L248-L275; L284-L322 | [mcp/src/agents_remember/memory/baseline.py](mcp/src/agents_remember/memory/baseline.py) |
| Bootstrap branch proof and the one attributed content commit. | L133-L169; L172-L227 | [mcp/src/agents_remember/memory/baseline.py](mcp/src/agents_remember/memory/baseline.py) |
| Cache preparation and refresh are separate from Git commit publication. | L44-L62; L65-L91 | [mcp/src/agents_remember/kernel/memory_cache.py](mcp/src/agents_remember/kernel/memory_cache.py) |
| Shared staging excludes derived paths from the content commit. | L191-L197; L200-L207 | [mcp/src/agents_remember/worktrees/modules/git.py](mcp/src/agents_remember/worktrees/modules/git.py) |
| The existing baseline case checks unborn readiness, one attributed commit, and unavailable-history refusal. | L303-L387 | [mcp/tests/test_memory_attribution_producers.py](mcp/tests/test_memory_attribution_producers.py) |

## Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No additional configured cross-repository evidence is claimed. | — | — |

## Update History

- 2026-09-15T01:16 UTC — Documented status classification from the already-derived observation, the existing-HEAD unavailable-history refusal before Git/content/cache mutation, and legitimate unborn readiness under the existing drift rules. Working candidate verified against the formatted source; real commit metadata and earlier history remain unchanged.


- 2026-09-15T01:06 UTC — Rebound source citation ranges after final shared-helper updates and formatting; current body contracts rechecked against the working candidate. No committed-source hash or execution claim was advanced.


- 2026-09-15T00:51 UTC — Replaced cache-existence and ledger-only publication contracts with attributed-history adoption, one content commit, and best-effort cache reporting; retained drift and bootstrap branch authority. Working candidate verified by source inspection; real last-touch commit metadata retained, with no future commit hash or certification claim.

- 2026-09-13T23:52+02:00 — 260913-LCA-L4 curator (uncommitted change set on `ar/260913-lca-l4-ar`,
  base `5bb124d4`): baseline adoption became one of the five memory-content producers, and it was the
  one whose commit message is nobody's argument — its hard-coded adopt subject was the whole message, so
  a fresh baseline's only memory commit carried no attribution and the projected ledger had no first
  row. Recorded that the code source-branch commit is now resolved once (`:208`) and used twice — the
  renderer call (`:210-216`) and `create_initial_ledger` (`:217-221`) — that the trailer is rendered by
  `kernel.memory_attribution.render_memory_content_message` rather than by a route-local format, that the
  `memory.md`-only ledger commit (`:224`) stays unattributed by rule, and the public end-to-end case that
  proves both documented git readers see the trailer. Rebound the stale `memory_baseline_status_tool`
  range (353-360 → 353-361). Verification metadata remains closeout-owned; no acceptance claim and no
  verification stamp advanced.

- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `load_ledger`, `write_ledger` repointed to mcp/src/agents_remember/kernel/memory_ledger.py:202-205, mcp/src/agents_remember/kernel/memory_ledger.py:216-238. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: regenerated the memory-tool ranges
  via the scoped fixer; exact non-fixing check returns zero findings.

- 2026-08-02T20:43+02:00 — W2-B08: anchored 2 baseline reference claims and repointed the MCP call-site reference from the removed `application/skill_tools.py` to `application/memory_tools.py`; ranges remain generated by the scoped fixer. Verification metadata stays pinned until closeout.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2: call-site update for the resolver's new signature —
  `resolve_request_context` now wraps `topology`/`coordination_root` in a `CoordinationHints`.
  Behaviour unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-05-31T12:50+02:00 — Renamed the argparse adapter `resolve_context` to `resolve_baseline_context` in the source; noted the new name in Logic (behavior-preserving, thin delegate to `resolve_request_context(request_from_args(args))`) (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Typed drift rows as `list[drift.DriftRow]`, normalized `topology` to `Literal['internal','external'] | None` at the argparse boundary, and added a ledger-path guard in `baseline_adopt`; behavior-preserving (commit `0549b28`).
- 2026-05-24T02:47+02:00: Updated after drift imports moved under `memory_quality.integrity`.
- 2026-05-24T00:35+02:00: Updated after adding request/service entry points for MCP controllers.
- 2026-05-23T13:09+02:00: Copied into the MCP package and patched to package imports.
