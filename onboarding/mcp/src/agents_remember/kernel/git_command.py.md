# mcp/src/agents_remember/kernel/git_command.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                          |
| path                   | `mcp/src/agents_remember/kernel/git_command.py`           |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated            | 2026-07-18T20:03+02:00                                   |
| lastVerifiedCommitHash | `abc7cbcc74921cdcb57a61529445f61641e919e7`               |
| lastVerifiedCommitDate | 2026-07-31T21:50:08+02:00|
| governingOverview      | `../../../overview.md`                                   |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

`git_command.py` owns the only `git` subprocess spawn in this package. Six near-identical private
`_run_git` copies used to sit beside it and had drifted apart — only this one passed a scrubbed
`env=` — so the copies were deleted and every caller now goes through `run_git`. It fixes command
isolation, decoding, stdin, and the timeout class in one place.

## Code Commentary

### Logic

`git_environment()` copies the process environment and removes all eight repository-selection
variables named by `GIT_REPOSITORY_SELECTOR_ENV` (L24-L33): `GIT_DIR`, `GIT_WORK_TREE`,
`GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`,
`GIT_NAMESPACE`, and `GIT_PREFIX`.

`run_git(repo_root, args, *, input_text=None, timeout=GIT_LOCAL_TIMEOUT_SECONDS)` (L67-L96) injects
`safe.directory`, runs at the supplied repository root, captures output as UTF-8 with
`surrogateescape`, applies the scrubbed environment, and returns non-zero outcomes for typed
interpretation by its caller. Two keyword arguments carry the consolidation:

- `input_text` feeds git's stdin; when it is `None`, stdin is `subprocess.DEVNULL` (L82-L84).
  `patch_id()` in `memory/carryover.py` — `git patch-id --stable` — is the only caller that passes
  it.
- `timeout` selects one of three module-level classes (L53-L55) instead of the former hard-coded
  five seconds: `GIT_LOCAL_TIMEOUT_SECONDS = 300` is the default and bounds work that can
  legitimately churn (`rebase`, `merge`, `worktree add`); `GIT_REMOTE_TIMEOUT_SECONDS = 120` bounds
  network calls, which are wedged rather than slow; `GIT_METADATA_TIMEOUT_SECONDS = 30` bounds the
  constant-time reads that sit on interactive paths (`rev-parse`, `branch --show-current`,
  `ls-files`). Callers name the class they need — `route_index_census._run_git` and
  `coordination_context/cross_repo.py` take the metadata bound, `worktrees/modules/cleanup.py`
  takes the remote one — and `git_freshness.fetch_remote` keeps its own shorter
  `DEFAULT_FETCH_TIMEOUT = 30` for the fetch.

### Conventions

The selector tuple is production authority and is imported by tests instead of copied. Repository
paths are rendered with `as_posix()` for stable Git configuration values. The module stays standard-
library-only and does not interpret Git records.

### Invariants And Boundaries

- Ambient repository selectors must never redirect a command away from the explicit `repo_root`.
- UTF-8 `surrogateescape` is required so NUL-delimited Git records retain non-UTF-8 path identity.
- `check=False` is intentional: callers translate return codes and stderr into their domain's typed
  failure without losing evidence.
- Every command stays bounded, but by a class that fits it. Five seconds was a fine bound for
  `rev-parse` and an impossible one for `rebase`/`merge`/`push --delete`, so raising the default to
  `GIT_LOCAL_TIMEOUT_SECONDS` is paired with call sites that name the shorter class; a raised
  default is not a removed bound, and `subprocess.TimeoutExpired` still escapes to the caller.
- `stdin` is `DEVNULL` unless a caller passes `input_text`: under the stdio MCP transport the
  parent's stdin IS the JSON-RPC request pipe, and a child holding or reading it wedges the tool
  call (GitHub #49).
- No second runner may appear. Only this module may spawn `git`; re-exports and typed wrappers
  (`coordination_context/cross_repo.py`, `code_quality/diff_coverage.py`) are fine, a new
  `subprocess.run(["git", ...])` anywhere in the package is not.
- Root validation, census parsing, and containment belong to callers such as
  `route_index_census.py`; this runner only executes the bounded command.

### Todos

None known for the MX-FIX-4 Git command boundary.

## Docs References

No Domain Documentation source is configured for this repository. Git behavior is verified by the
package's production-path regression matrix.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `_run_git` calls this runner with `GIT_METADATA_TIMEOUT_SECONDS` and converts `TimeoutExpired`/`OSError` into `AuthorityError`/`RouteIndexCensusError`; `_nul_records` splits its NUL-delimited stdout. | L189-L205; L217-L223 | [route_index_census.py](agents-remember/mcp/src/agents_remember/kernel/route_index_census.py) |
| Carryover no longer defines its own input-bearing adapter: `require_git` delegates to `run_git`, and `patch_id` is the one caller that passes `input_text`. | L92-L96; L200-L208 | [carryover.py](agents-remember/mcp/src/agents_remember/memory/carryover.py) |
| Tests import the production selector inventory and cover every selector. | L34-L39; L592-L640 | [conftest.py](agents-remember/mcp/tests/conftest.py); [test_route_index.py](agents-remember/mcp/tests/test_route_index.py) |
| `DecoyRepositoryTests` re-exports the selectors against a decoy repo inside its own scope; `RunnerContractTests` covers `input_text` vs `DEVNULL`, `surrogateescape`, and the per-call timeout; `SingleRunnerTests.test_only_the_kernel_module_defines_a_git_runner` AST-sweeps the package and asserts `kernel/git_command.py` is the only module that spawns git. | L84-L140; L143-L220; L322-L402 | [test_git_command.py](agents-remember/mcp/tests/test_git_command.py) |

## Cross-Repo References

The runner can execute against configured code or external-memory repositories, but no sibling
repository defines this implementation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-31T20:50+02:00 — 260731-EFA-L3 curator: this file became the single owner, so the body
  was rewritten. Corrected the false "enforces a five-second timeout" claim: `run_git` now takes
  `timeout` and defaults to `GIT_LOCAL_TIMEOUT_SECONDS = 300`, with `GIT_REMOTE_TIMEOUT_SECONDS =
  120` and `GIT_METADATA_TIMEOUT_SECONDS = 30` as the other two classes (L53-L55), and callers pick
  one. Corrected the unconditional `stdin=DEVNULL` claim: stdin is `DEVNULL` only when the new
  `input_text` keyword is `None` (L82-L84). Recorded the consolidation (six drifted `_run_git`
  copies removed, this the only module that may spawn git) in Purpose and as a new invariant.
  Repaired 2 citations into files this leaf changed: the census row's whole-file `L1-L226` became
  `L189-L205; L217-L223` (`_run_git` + `_nul_records`), and the carryover row's unanchored "Git
  runner" became `L92-L96; L200-L208` — that row's claim of a "separate input-bearing Git adapter"
  was false, since carryover's local `run_git` was deleted and `require_git`/`patch_id` now call
  this one. Added a row for the new `mcp/tests/test_git_command.py`. The `conftest.py` /
  `test_route_index.py` ranges were left alone: this leaf did not touch either file. The L2 entry
  below cites `git_command.py L9-L18` for the selector tuple; that was true at its commit and is
  left as the historical record — the tuple now sits at L24-L33.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The row
  carries two source paths, and only its second range moved: `conftest.py` L34-L39 still holds the
  `GIT_REPOSITORY_SELECTOR_ENV` import and the `os.environ.pop` scrub loop, while the coverage test
  `test_ambient_git_repository_selectors_cannot_redirect_the_census` shifted to `test_route_index.py`
  L592-L640. Re-verified that its `selectors` dict still names all eight tuple entries from
  `git_command.py` L9-L18.

- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: added the authoritative selector scrub and
  surrogate-preserving output boundary used by deterministic route-index census and carryover.
- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
