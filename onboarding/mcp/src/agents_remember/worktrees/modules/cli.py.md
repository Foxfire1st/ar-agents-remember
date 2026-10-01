# mcp/src/agents_remember/worktrees/modules/cli.py

## Purpose

Owns command-line parsing and JSON print adapters for the worktree lifecycle.

## Code Commentary

### Logic

Closeout parsing accepts code and memory commit-message flags only; integrate accepts strategy and approval without a ledger-message flag. `command_closeout` normalizes those two messages before constructing the domain input. Synchronous apply still obeys the journal-required boundary.

The module builds the `start`, `attach`, `status`, `closeout`, `integrate`,
and `cleanup` subcommands (the `direct-closeout` subcommand was removed with
the direct-closeout surface, issue #62). Each command function
converts the raw `argparse.Namespace` into the typed `WorktreeArgs` DTO via
`WorktreeArgs.from_namespace(args)` before calling the result-returning service
functions, then prints payload JSON — keeping CLI transport concerns out of the
lifecycle operation modules.

260712-PTS-L1 adds the `heal-leaf-ids` subcommand (`--coordination-root`,
required; `--dry-run`) — the deliberate invocation seam for
`worktree_contract.heal_contract_leaf_ids`. `command_heal_leaf_ids` prints the
heal report as indented JSON and, unlike the lifecycle commands, deliberately
skips the `WorktreeArgs` DTO: healing legacy stem-shaped leaf ids is a one-shot
migration sweep, never a per-read side effect — run it once against a
coordination root (or at daemon startup) instead of relying on `load_contract`
to normalize, which it no longer does.

### Conventions

Accepted input, exact Git facts, and typed owner results stay distinct from disposable projections.

### Invariants And Boundaries

The ledger is a computed consumer cache; it cannot supply an additional Git output or lifecycle prerequisite.

### Todos

None recorded for the ledger-retirement boundary.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `command_closeout` normalizes code/memory messages before the journal-bound closeout adapter. [1]
- `build_parser` exposes closeout/integration options without ledger-message flags. [2]

- The CLI module exposes the public main entry point for `python -m` execution. (`main`) [3]
- MCP startup enters the result-returning application owner without CLI parsing. (`worktree_start_tool`) [4]
- MCP attachment enters the result-returning application owner without CLI parsing. (`worktree_attach_tool`) [5]
- MCP status enters the result-returning application owner without CLI parsing. (`worktree_status_tool`) [6]
- Start or observe the exact contract-addressed integration operation. (`worktree_integrate_tool`) [7]
- MCP cleanup enters the result-returning application owner without CLI parsing. (`worktree_cleanup_tool`) [8]
- The heal implementation this seam invokes (walk once, cheap-skip canonical ids, rewrite + report) lives in the contract module. (`heal_contract_leaf_ids`) [9]

### Cross-Repo References

No separately configured cross-repository implementation governs this file; any external-memory repository is addressed by the task contract.

No additional cross-repository evidence applies.

## Series-Contract Notes

The common CLI contract-path help now names `series-contract.md`, aligning command-line usage with the root/leaf contract schema.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## 260821-CLIVE-L1 Legacy CLI Boundary

The synchronous CLI closeout apply path now fails closed with `JOURNALED_CLOSEOUT_REQUIRED`. Dry-run loads the contract and uses the canonical normalizer, returning typed validation behavior without mutation. CLI flags are syntactically optional because enabledness is derived at runtime; enabled messages remain mandatory and explicit. The CLI does not provide a compatibility bypass around the lifecycle journal.

## 260821-CLIVE-L2 Current Contract

The current source seams include `parse_json_stdout`, `command_status`, `command_attach`. This module remains a public execution adapter over closed admission and exact mutation-owner reread; it does not duplicate reader exception families or lifecycle authority.

### Reconciled Source Evidence

- The current module exposes `parse_json_stdout`, `command_status`, `command_attach` at this ownership boundary. [10]

## Governing Overview

[Governing route overview](overview.md)
