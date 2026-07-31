# mcp/tests/test_diff_coverage.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_diff_coverage.py`          |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T15:32+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Behavioural suite for `agents_remember.code_quality.diff_coverage` — the **100% per-diff
coverage floor** this leaf added. Every statement and branch arc on a changed line must be
exercised, and the failure names each uncovered line rather than reporting a percentage.

## The Method That Matters

Every test drives a **real throwaway git repository** rather than a stubbed diff. That is
deliberate and must not be undone: the gate's whole job is to read what git says changed,
and a fake `git diff` string proves only that the parser agrees with whoever wrote the
fixture — not that it agrees with git's hunk headers for an added file, a one-line
deletion, a rename, or a change that exists only in the working tree.

Module helpers: `git()`, `write()`, `coverage_report()` (a Coverage.py JSON report shaped
exactly like the wrapper's), and `seeded_repository()` (one committed module plus the
commit it was committed in).

## Code Commentary

### `BaseResolutionTests` — which commit "changed" is measured against

The precedence ladder, each rung tested: explicit base → `AR_GATE_DIFF_BASE` → the GitHub
Actions pull-request base → the configured upstream → the default branch → the empty tree.
An unknown explicit base is an **error, not a silent fallback**; a candidate with no shared
history is skipped rather than used; a first commit with no merge base compares against the
empty tree; a broken git invocation raises rather than reporting "nothing changed" (the
failure mode that would silently disable the floor).

### `ChangedLineTests` — what counts as a changed line

Added, modified and renamed files all report their **new** line numbers. A pure deletion
contributes no changed lines and a deleted file is not a changed file — there is nothing
left to cover. Working-tree edits count, because they are what coverage measured. A
`/dev/null` post-image drops the file rather than keeping the previous one; an unparsable
hunk header is dropped rather than guessed at; non-Python changes are not collected.

### `MeasurementTests` — the verdict

Statements and branches are scored **together**. An uncovered changed line is *named*, not
only counted; an untaken branch on a changed line is named with its destination, and a
branch that leaves the function is reported as an exit. A changed line carrying no
statement is not counted as covered. A new module the suite never imports scores zero. An
empty diff says so rather than reporting a ratio, and a diff touching only non-Python files
is its own state. Changed Python outside the measured packages is named on every run. The
report states the base and the floor it was judged against. **A report without branch
measurement is refused** — the same fail-loud rule the CRAP reader carries.

### `WrapperIntegrationTests` — the floor as the gate runs it

Same coverage JSON, same exit code. A diff below the floor fails the wrapper; a diff at the
floor passes; a missing `coverage.json` fails instead of passing by default; an unusable
base fails the step rather than the process. The floor runs **inside** the wrapper rather
than beside it, and `--diff-base` / `--diff-floor` are real flags. The default is **zero
uncovered changed lines**.

## Invariants And Boundaries

- Real repositories only. Do not replace them with canned diff text.
- Every failure mode fails **closed**: unknown base, broken git, missing coverage JSON, and
  statement-only coverage all fail rather than reporting a clean diff.
- The floor is per-diff, not per-file or per-project; it says nothing about total coverage.
- The floor lives in the full (pre-push) tier and in CI, because it needs a diff base.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The module under test: base resolution, changed-line collection, and the measurement. | [diff_coverage.py](agents-remember/mcp/src/agents_remember/code_quality/diff_coverage.py) |
| The wrapper that runs the floor as a step and exposes its two flags. | [check.py](agents-remember/mcp/src/agents_remember/code_quality/check.py) |
| The tier that carries the floor, and why the fast tier cannot. | [_gate.sh](agents-remember/.githooks/_gate.sh) |

## Update History

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  changed-lines coverage floor suite. Verification metadata is pinned to the leaf's
  reformat commit until closeout stamps the code commit.
