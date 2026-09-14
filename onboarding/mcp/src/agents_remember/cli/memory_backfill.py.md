# mcp/src/agents_remember/cli/memory_backfill.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/memory_backfill.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T18:20+02:00 |
| lastVerifiedCommitHash | `270704b86116728a64ada83ee258a0e7726206b4` |
| lastVerifiedCommitDate | 2026-09-14T18:18:08+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

CLI adapter for the memory-history trailer backfill:
`agents-remember memory-backfill --contract <leaf contract> [--apply] [--rescue-ref <ref>]
[--ref <ref> ...] [--expected-digest <digest>]`. It is the only way the migration in
`kernel/memory_backfill.py` is invoked, and it exists to make the safe invocation the default one:
planning is what happens when no flag is given, and planning is also the dry run.

## Code Commentary

### Logic

`run` cit:([`run`], mcp/src/agents_remember/cli/memory_backfill.py:76-97) resolves the request, plans, prints
`MemoryBackfillPlan.render()` line by line, and returns an exit status that is the gate's:
`EXIT_NOTHING_TO_DO` (0) when the history already carries every attribution the table records and no
code commit lost its mapping, `EXIT_WORK_REMAINS` (1) when anything is left to write or a mapping was
lost, and `EXIT_REFUSED` (2) when the invocation is refused. The 1-versus-0 distinction is the plan's
own `is_empty`, which includes the lost code commits: a fully written history that dropped a pairing
still reports work rather than claiming a completeness it does not have. `render()` is what puts that
in front of an operator — the census lines, one line per skip family including the zeroes, and one
line per lost mapping naming the memory commit that took it. A refusal from the kernel arrives as
`MemoryBackfillRefusal` and is printed rather than
raised, so an operator reads one line instead of a traceback, and the two adapters of that
distinction — a request that cannot be resolved and a plan that cannot be derived — are both mapped
to `EXIT_REFUSED`.

**`--contract` is required, and it is the write guard.** `_request_from`
cit:([`_request_from`], mcp/src/agents_remember/cli/memory_backfill.py:117-137) reads the leaf enclosure contract and
takes the memory repository, the code repository and the default ref from it, exactly as
`cli/memory_citations.py` does. There is therefore no argument list that can aim a history rewrite at
the official memory repository by hand. `_refusal_for`
cit:([`_refusal_for`], mcp/src/agents_remember/cli/memory_backfill.py:140-150) refuses three contract shapes before any
repository is read: a memory mode other than `external` (the trailer backfill is an external-memory
operation), a memory repository path that is not a directory, and a code repository path that is not
a directory. `_default_ref` cit:([`_default_ref`], mcp/src/agents_remember/cli/memory_backfill.py:153-154) prefers the
contract's memory work branch and falls back to its memory source branch, so the default run moves
the branch the leaf actually writes.

**`--apply` is the only writing flag, and it is not the default.** `_apply`
cit:([`_apply`], mcp/src/agents_remember/cli/memory_backfill.py:100-114) calls `apply_memory_backfill` with the
`--expected-digest` value the caller passed, prints the rewritten count, the memory tip transition,
the refs that moved and the rescue refs that were written, and then states the next step in the
operator's own terms: carry `memory.md`'s memory cells onto the new ids with the returned total
identity map, then re-read the projection at the new tip. `--rescue-ref` defaults to
`refs/backup/memory-pre-migration` (`DEFAULT_RESCUE_REF`
cit:([`DEFAULT_RESCUE_REF`], mcp/src/agents_remember/cli/memory_backfill.py:38-38)) and must not already exist: the
rescue ref is the only undo a message rewrite has, and an existing one records an earlier rewrite
nobody has read yet. `--ref` is repeatable and defaults to the contract's memory work branch, so the
complete list of refs a run may move is always explicit.

**Passing the plan's digest back is what makes an applied run the rehearsed run.**
`--expected-digest` is compared inside the kernel before any object is written, so a history or code
repository that moved between the preview and the apply is refused rather than half-migrated.

**The tip this command hands the kernel is the contract's memory WORK BRANCH NAME, not a commit.**
That is the ordinary path and the kernel resolves it to the exact commit it names before the table,
the digest or the rescue set are derived, so the printed plan is stated about one object rather than
about a name that could move under the run. The same resolution reaches every ref the run moves. It
is load-bearing rather than defensive: a rescue set built from a name and then read back as a hash
can never compare equal to the name, so the reviewed version wrote its rescue refs and then refused,
and the retry that followed tripped the existing-ref check on refs its own predecessor had just
created. With the resolution in place the first apply completes from a name, and a second apply over
the migrated history returns 0 having moved nothing — the kernel's empty-plan short-circuit runs
before the rescue guard, so a retry is a no-op rather than a refusal.

### Conventions

`add_arguments` cit:([`add_arguments`], mcp/src/agents_remember/cli/memory_backfill.py:41-73) plus `run` is the
package's CLI adapter shape — `cli/__main__.py` registers the subparser and `set_defaults(func=run)`,
so this module owns its own flags and nothing else. The three exit codes are module constants rather
than literals, and the module carries no `argparse` parsing of its own beyond the adapter contract.
Every help string states the consequence rather than the syntax: `--apply` says what it writes,
`--rescue-ref` says what an existing one means, `--ref` says what the default is.

### Invariants And Boundaries

- **Planning is the default and is the dry run.** Without `--apply` the command reads the history,
  prints the census, and writes nothing; a non-zero exit is the check, not a failure.
- **`--contract` is required and is the only target selector.** No flag names a repository directly,
  so a rewrite cannot be aimed at the official memory repository from a command line.
- **The command refuses an internal-memory contract and any missing repository directory** before it
  reads history.
- **`--apply` refuses when `--rescue-ref` already exists**, because the rescue ref records the
  history being replaced — but only when the run would rewrite something. An already-migrated
  history short-circuits on the empty plan first, so a retry after a completed apply succeeds as a
  no-op instead of refusing on the refs its own predecessor created.
- **Every name is resolved before a ref is written.** The tip this adapter passes is a branch name;
  the kernel turns it and every moved target into exact commits, and a name that cannot be restored
  refuses rather than being recorded.
- **Exit status is the gate's**: 0 nothing left to write and nothing lost, 1 work remains or a
  mapping was lost, 2 refused.
- **This adapter composes no Git command.** Every read and every rewrite goes through
  `kernel/memory_backfill.py`; the adapter resolves a contract, prints a plan and maps a refusal to
  an exit code.
- **The contract is not an authority to rewrite anything.** It names the repositories; whether a
  backfill should run, and when, is the developer's ruling and this master's integration step.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this repository. The command-line surface is
described by its own `--help` text and by the kernel module's contract, which is same-repository
evidence rather than external documentation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies to this adapter; the proving evidence is this repository's own CLI and kernel source. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The umbrella entrypoint that registers this subcommand and dispatches through `func=run`. | `build_parser`; `main` | mcp/src/agents_remember/cli/__main__.py:16-34; mcp/src/agents_remember/cli/__main__.py:37-39 |
| The planning half this prints: the census, the digest, and the empty-plan answer that becomes exit 0. | `plan_memory_backfill`; `MemoryBackfillPlan`; `render` | mcp/src/agents_remember/kernel/memory_backfill.py:257-308; mcp/src/agents_remember/kernel/memory_backfill.py:145-224; mcp/src/agents_remember/kernel/memory_backfill.py:200-224 |
| The writing half: the digest pin, the rescue refs, the single `update-ref --stdin` transaction and the total identity map the printed next step consumes. | `apply_memory_backfill`; `MemoryBackfillRequest`; `MemoryBackfillResult` | mcp/src/agents_remember/kernel/memory_backfill.py:625-661; mcp/src/agents_remember/kernel/memory_backfill.py:227-242; mcp/src/agents_remember/kernel/memory_backfill.py:245-254 |
| The refusal type the adapter prints as a line instead of raising. | `MemoryBackfillRefusal` | mcp/src/agents_remember/kernel/memory_backfill.py:109-110 |
| The peer adapter whose contract-required write guard this command reuses. | `add_arguments`; `run` | mcp/src/agents_remember/cli/memory_citations.py:48-101; mcp/src/agents_remember/cli/memory_citations.py:104-165 |
| The contract loader and its error type: the adapter resolves both repositories from the leaf enclosure contract rather than from flags. | `load_contract`; `ContractError` | mcp/src/agents_remember/worktrees/worktree_contract.py:434-464; mcp/src/agents_remember/worktrees/worktree_contract.py:89-90 |

## Cross-Repo References

The command reads a code repository and an external memory repository that are both named by the same
leaf enclosure contract, and it never assumes a layout beyond what the contract declares. No sibling
repository or external system is reached.

| Finding | Anchor | Source |
| --- | --- | --- |
| The pair of repositories is contract-owned rather than ambient, which is what keeps the rewrite scoped to the leaf's own memory line. | `_request_from`; `_refusal_for` | mcp/src/agents_remember/cli/memory_backfill.py:117-137; mcp/src/agents_remember/cli/memory_backfill.py:140-150 |

## Update History

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
