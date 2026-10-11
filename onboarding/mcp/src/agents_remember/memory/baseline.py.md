# mcp/src/agents_remember/memory/baseline.py

## Governing Overview

[Nearest governing overview](../../../overview.md)

Working-candidate verification: source inspected at 2026-09-15T01:16 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Inspects and adopts an existing external-memory onboarding baseline. Adoption creates an attributed
memory-content commit; the consumer ledger is computed from Git and refreshed as a disposable cache.
On a converted tree the first baseline is validated before it is made: the adoption stages the
content on a private index, validates the staged tree with no comparison bases paired with the
attributed code commit, and records exactly that tree. A refusal, a dry run, or any validation
exception leaves the index, the refs and every owned file as they were.

## Code Commentary

### Logic

`BaselineRequest`, `baseline_status`, and `baseline_adopt` are the service entry points. CLI parsing
adapts into the request object, and `resolve_request_context` passes topology and coordination hints
through the shared resolver. Drift measurement uses the shared summary. An adoption selects
`write_report=not dry_run` before either storage-format branch: its dry-run preview files neither
the drift report nor observer snapshot and advertises no unfiled path. A mutating adoption keeps
its report-producing default and files the report before the adoption decision. The registered
baseline-status read accepts only the repository identifier and constructs a request with
`report=None`, so it selects `write_report=False`. Its converted payload omits `drift_report` rather
than advertising an unfiled path. An explicit internal or CLI report-path request is a producer;
that arm is not exposed as an exception to the registered read.

`ledger_status` reports the derived Git-history view or an unavailable-history diagnostic.
`base_payload` reuses that observation to classify `already-adopted` when readable history supplies a
memory-content commit, rather than performing a second unguarded history walk. Cache existence still
has no role in that decision.

A resolvable HEAD whose ancestry cannot be read reports top-level `unavailable`. `baseline_adopt`
returns that refusal before cache preparation, content staging, or ref mutation; accepting drift
cannot override unreadable history. An unborn repository has no resolvable HEAD, so its unavailable
initial walk does not by itself block bootstrap: it remains `ready` subject to the ordinary drift
rules. Drift reporting precedes the adoption decision only for the mutating producer; dry-run
measurement preserves the summary without filing report or snapshot.

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
trailer. Content staging excludes the shared memory-content policy rather than one inline name:
`commit_if_dirty(..., exclude_paths=MEMORY_CONTENT_EXCLUDES)` carries `("memory.md", "bootstrap")` on
the call that actually stages. That last half is load-bearing and is why the constant is imported
rather than spelled here: `commit_if_dirty` re-stages the whole worktree, so an exclusion applied to a
bare `git add` *before* it is inert and `bootstrap/` scaffolding lands in the baseline commit anyway.
The returned bootstrap contains `memoryContentCommit` and best-effort `ledgerCache`, with no
ledger-only commit.

Drift is measured with the one shared summary: `run_drift` calls `run_drift_summary` and no longer
classifies by itself, so the drift block of the baseline tools carries the converted rule-2 fields
on a converted tree and keeps today's behaviour elsewhere. The memory layer imports nothing from the
application layer; the optional converted comparison base stays with the application callers that own
a contract. The converted payload reports three blocking states — `blocked-invalid` while validator
violations exist, `blocked-drift` while stale anchors exist and drift was not accepted, and
`unavailable` as before — and `accept_drift` accepts stale anchors only, never a validator violation.
With filing disabled, `run_drift` returns the measured summary and `None`: it still refuses a failed
measurement, but does not raise merely because a read requested no report. Measured fields and the
adoption gate are preserved; absence of a report is an output distinction, not permission to skip
converted validation.

The converted adoption never writes the worktree's own index before validation passes.
`_private_staging_index` holds a mtime-preserving copy of the worktree index for one interval (an
absent index stages from an empty private file, exactly as `git add` would; any other copy failure
refuses loudly with no fallback). `_prepare_stage_validate` runs cache preparation, staging and
validation against that copy; any exception first restores the prepared `.gitignore` if and only if
its bytes are provably still ours — a concurrent external edit or an unreadable file is preserved,
never overwritten — then propagates with its name. A dry run validates and gives everything back;
a refusal gives the file back and raises `BaselineValidationRefused` with the worktree index
untouched. Only after validation passes does `_adopt_validated_converted_tree` publish: the commit
object is built from the immutable validated tree (`commit-tree`), the branch ref moves to it only
while it still points where validation saw it (expected-old `update-ref`), and the recorded tree is
verified — so a hook or a concurrent index change cannot smuggle different bytes into the
publication. The worktree's own index is then brought to the adopted state. Where the validator is
not bound, the adoption refuses; it never commits unvalidated.

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
- **The worktree's own index is never written before validation passes.** Prepare, stage and tree
  commands of the owned interval address the private copy; only the `.gitignore` file guard is kept,
  and only while its bytes are provably ours.
- **`accept_drift` never clears a validator violation.** It accepts stale anchors only; a dry run
  reports `would-adopt` only when the staged-tree validation would pass.

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
- The existing baseline case checks unborn readiness, one attributed commit, and unavailable-history refusal. [5]
- The shared memory-content policy the content commit excludes, and the reason the exclusion belongs on the staging call. [8]
- The recorded-default authority this file now follows instead of a literal. [11]

### Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

No additional configured cross-repository evidence is claimed.

- Drift is measured with the one shared summary; the memory layer classifies nothing by itself. [12]
- The converted payload carries the rule-2 fields with its three blocking states. [13]
- The converted gate accepts stale anchors only, never a validator violation. [14]
- The whole owned interval runs on a private index copy; an exception restores owned bytes, then keeps its name. [15]
- A dry run, a refusal or an exception leaves the index, the refs and every owned file as they were. [16]
- Publication records exactly the validated tree; a moved branch refuses instead of publishing past validation. [17]
- Converted adoption stages, validates with no bases paired with the code commit, and commits exactly that tree. [18]

- Registered status requests select unfiled measurement; an absent report pointer is omitted while measurement and explicit producer behavior remain intact. \[19] [19]

- Adoption previews select suppression before measuring; mutating adoption preserves its report-producing mode. [20]

- Cache preparation and refresh are separate from Git commit publication. [3]
- Shared staging excludes derived paths from the content commit. [4]
- Context, drift and Git-history adoption decisions. [6]
- Bootstrap branch proof from the branch `memory_init` recorded, and the one attributed content commit. [7]
- Shared staging, and the re-stage that makes a bare `git add` exclusion inert. [9]
- The branch-authority cases this leaf added: adoption follows the recorded branch, and `bootstrap/` never enters the baseline commit. [10]
