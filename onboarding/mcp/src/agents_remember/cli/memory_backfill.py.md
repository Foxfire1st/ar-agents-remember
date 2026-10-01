# mcp/src/agents_remember/cli/memory_backfill.py

## Governing Overview

[Nearest governing overview](../../../overview.md)

Working candidate verification: source inspected at 2026-09-15T01:06 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Adapts the memory-history backfill to the command line. Planning is the default and reads without
rewriting; `--apply` explicitly invokes the kernel migration over refs selected from the request.

## Code Commentary

### Logic

`add_arguments` owns `--contract`, `--apply`, rescue-ref selection, repeatable target refs, and the
optional expected plan digest. `_request_from` loads the supplied contract and obtains the code and
memory repositories from it. `_refusal_for` checks external-memory mode and that both repository
paths are directories. The adapter does not add a separate leaf-kind validation predicate.

`run` prints the kernel plan and its loss/skip census. An empty plan returns 0, a nonempty plan
without apply returns 1, and request/planning refusals return 2. With explicit apply, `_apply` forwards
the expected digest, reports the rewritten count, old/new tip, moved refs and rescue refs, and
returns 0 after a successful kernel apply. That exit is not a separate check of lossless coverage;
the plan's explicit loss accounting remains visible.

The next-step message now tells the caller to reconcile the selected worktrees and contract bases
with the rewritten refs, then rebuild the consumer ledger cache from commit trailers without
committing it. It no longer instructs manual carrying of memory.md cells as the runtime follow-up.
The command prints this guidance; it does not automatically reconcile worktrees or update bases.

The contract's memory work branch is the normal tip/default target; the kernel resolves named refs
to exact objects before planning and publication. Repeated `--ref` values name the allowed target
set, and the empty-plan path returns before rescue collision checks so an unchanged retry can be a
no-op. The kernel owns digest, rescue, rewrite, and target-update mechanics.

### Conventions

The umbrella CLI registers this module's `add_arguments` and `run` functions. This adapter constructs
no Git commands; it resolves the contract, prints results, and maps expected refusal to exit status.
A contract identifies repository facts, not independent user authorization to rewrite shared history.

### Invariants And Boundaries

- No apply flag means planning only, with no history rewrite.
- Actual loss and skip census remain distinct from the CLI's return status.
- Follow-up cache rebuilding is derived from trailers and must not create a cache commit.
- Printed reconciliation guidance does not claim those follow-up operations already ran.
- This sidecar update performs no migration or live-state operation.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

- Flags, request resolution, and mode/directory refusal define the adapter scope. [1]
- Planning and apply status/output remain separate. [2]
- The kernel owns loss-aware planning and the explicit apply transaction. [3]
- Actual branch-name invocation and retry behavior are tested through the CLI. [4]

### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.
