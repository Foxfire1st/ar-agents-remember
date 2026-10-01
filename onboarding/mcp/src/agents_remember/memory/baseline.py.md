# mcp/src/agents_remember/memory/baseline.py

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
repository-default memory branch. `_baseline_default_branch` proves that default from the branch
`memory_init` recorded, **not from a fixed name**: the memory repository is founded on the code branch
the developer chose, so the old `branch != "main"` refusal would have refused every repository whose
memory is founded on anything else. It still supports the exact unborn branch memory initialization
created, and it refuses — with the recorded-value name in the message — when the repository records no
`agents-remember.defaultBranch` value at all. It does not create, switch, or commit an integration ref.

The code source-branch commit is resolved once. The fixed adoption subject is passed through
`render_memory_content_message`, so the resulting memory commit carries that exact `Code-Commit`
trailer. Cache preparation adds the ignore rule and removes the cached ledger from the index. Content
staging excludes the shared memory-content policy rather than one inline name:
`commit_if_dirty(..., exclude_paths=MEMORY_CONTENT_EXCLUDES)` carries `("memory.md", "bootstrap")` on
the call that actually stages. That last half is load-bearing and is why the constant is imported
rather than spelled here: `commit_if_dirty` re-stages the whole worktree, so an exclusion applied to a
bare `git add` *before* it is inert and `bootstrap/` scaffolding lands in the baseline commit anyway —
the defect this seam carried until this leaf fixed it. The returned bootstrap contains
`memoryContentCommit` and best-effort `ledgerCache`, with no ledger-only commit.

### Conventions

MCP application functions call the service directly rather than parsing CLI stdout. `dry_run`
defaults to false; an explicit dry run previews adoption. The kernel owns message rendering and
cache computation, while the shared Git module owns content staging.

### Invariants And Boundaries

- External topology, bootstrap branch ownership, and drift acceptance remain real admission rules.
- The default branch is **data, not a constant**: every comparison validates the recorded name against
  a real ref, and `main` is never assumed. Reintroducing a name comparison here is the regression the
  branch-authority cases catch.
- Cache existence, content, or a missing cache path cannot authorize or block adoption.
- A resolvable HEAD with unavailable ancestry cannot be adopted as a new baseline, even with drift accepted.
- Attribution is stored in the real memory commit, not reconstructed from a hand-written pair.
- Repeating adoption with readable attributed history returns `already-adopted` without another commit.
- **`bootstrap/` is excluded from the baseline commit, not deleted from the worktree.** The exclusion
  must ride the staging call; a bare `git add` before `commit_if_dirty` is inert.

### Todos

No new file-local follow-up is established by this documentation pass.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets were checked in the L13 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

- Context, drift, and Git-history adoption decisions. [1]
- Bootstrap branch proof and the one attributed content commit. [2]
- Cache preparation and refresh are separate from Git commit publication. [3]
- Shared staging excludes derived paths from the content commit. [4]
- The existing baseline case checks unborn readiness, one attributed commit, and unavailable-history refusal. [5]
- Context, drift and Git-history adoption decisions. [6]
- Bootstrap branch proof from the branch `memory_init` recorded, and the one attributed content commit. [7]
- The shared memory-content policy the content commit excludes, and the reason the exclusion belongs on the staging call. [8]
- Shared staging, and the re-stage that makes a bare `git add` exclusion inert. [9]
- The branch-authority cases this leaf added: adoption follows the recorded branch, and `bootstrap/` never enters the baseline commit. [10]
- The recorded-default authority this file now follows instead of a literal. [11]

### Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

No additional configured cross-repository evidence is claimed.
