# mcp/src/agents_remember/cli/memory_backfill.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/memory_backfill.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:06 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview | `../../../overview.md` |

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

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Flags, request resolution, and mode/directory refusal define the adapter scope. | `add_arguments`; `_request_from`; `_refusal_for` | mcp/src/agents_remember/cli/memory_backfill.py:41-73; mcp/src/agents_remember/cli/memory_backfill.py:117-150 |
| Planning and apply status/output remain separate. | `run`; `_apply` | mcp/src/agents_remember/cli/memory_backfill.py:76-97 |
| The kernel owns loss-aware planning and the explicit apply transaction. | `MemoryBackfillPlan`; `plan_memory_backfill`; `apply_memory_backfill` | mcp/src/agents_remember/kernel/memory_backfill.py:144-224; mcp/src/agents_remember/kernel/memory_backfill.py:257-308 |
| Actual branch-name invocation and retry behavior are tested through the CLI. | `test_the_cli_applies_a_branch_name_tip_and_survives_its_own_retry` | mcp/tests/test_memory_backfill.py:853-909 |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:06 UTC — Corrected the post-apply guidance to reconcile selected worktrees/contract bases and rebuild an uncommitted trailer-derived cache; retained flags and kernel ownership, and clarified the actual contract checks and exit-status scope. Working candidate verified by source inspection; commit metadata records real committed history only.


- 2026-09-14T18:20+02:00 — 260913-LCA-L3 curator (same uncommitted change set, `ar/260913-lca-l3-ar`,
  base `7317108b`): the adapter's source is unchanged by the reviewed fix, but what it reports is not,
  so this card records the new contract. Exit 0 now means the plan is empty under the kernel's
  widened `is_empty` — nothing left to write **and** no code commit left unmapped — so a fully
  written history that dropped a pairing stays at exit 1, and `render()` is described as printing one
  line per skip family plus one line per lost mapping with the memory commit that took it. Added the
  paragraph recording that this command hands the kernel the contract's memory **work-branch name**,
  that the kernel resolves it and every moved target to exact commits before deriving the plan or
  writing a rescue ref, and that the empty-plan short-circuit precedes the rescue guard so a second
  apply over a migrated history is a no-op success rather than a refusal about refs its own
  predecessor created — the defect the review found on this exact path. The `--apply` rescue
  invariant and the exit-status invariant were rewritten to match. Every kernel citation was
  re-derived against the grown module: `plan_memory_backfill` 208-239 → 257-308, `MemoryBackfillPlan`
  106-175 → 145-224, `render` 156-175 → 200-224, `apply_memory_backfill` 348-383 → 625-661,
  `MemoryBackfillRequest` 178-193 → 227-242, `MemoryBackfillResult` 196-205 → 245-254,
  `MemoryBackfillRefusal` 85-86 → 109-110. Verification metadata remains closeout-owned; no
  acceptance claim and no verification stamp advanced.

- 2026-09-14T17:20+02:00 — 260913-LCA-L3 curator (uncommitted change set on `ar/260913-lca-l3-ar`,
  base `7317108b`): created the one-to-one sidecar for this new CLI adapter. Records the command
  shape and the exit-status contract (0 already attributed, 1 work remains, 2 refused), the
  `--contract` requirement as the write guard that keeps a rewrite off the official memory repository,
  planning as the default and therefore the dry run, the `--apply`/`--rescue-ref`/`--ref`/
  `--expected-digest` flags with the consequence each one carries, the three contract refusals taken
  before any repository is read, and the printed next step (carry the table's memory cells onto the
  returned total identity map, then re-read the projection). Verification metadata names the leaf's
  base commit and remains closeout-owned; no acceptance claim and no verification stamp advanced.
