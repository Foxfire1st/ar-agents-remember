# mcp/src/agents_remember/kernel/git_command.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                          |
| path                   | `mcp/src/agents_remember/kernel/git_command.py`           |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated | 2026-09-06T17:13:06+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
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
variables named by cit:([`GIT_REPOSITORY_SELECTOR_ENV`], mcp/src/agents_remember/kernel/git_command.py:55-64): `GIT_DIR`, `GIT_WORK_TREE`,
`GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`,
`GIT_NAMESPACE`, and `GIT_PREFIX`.

`run_git(repo_root, args, *, input_text=None, timeout=GIT_LOCAL_TIMEOUT_SECONDS)` cit:([`run_git`], mcp/src/agents_remember/kernel/git_command.py:85-151) injects
`safe.directory`, runs at the supplied repository root, captures output as UTF-8 with
`surrogateescape`, applies the scrubbed environment, and returns non-zero outcomes for typed
interpretation by its caller. Two keyword arguments carry the consolidation:

- `input_text` cit:([`run_git`], mcp/src/agents_remember/kernel/git_command.py:85-151) feeds git's stdin; when it is `None`, stdin is `subprocess.DEVNULL`.
  `patch_id()` cit:([`patch_id`], mcp/src/agents_remember/memory/carryover.py:181-188) — `git patch-id --stable` — is the only caller that passes
  it.
- `timeout` cit:([`GIT_LOCAL_TIMEOUT_SECONDS`, `GIT_REMOTE_TIMEOUT_SECONDS`, `GIT_METADATA_TIMEOUT_SECONDS`], mcp/src/agents_remember/kernel/git_command.py:92-94) selects one of three module-level classes instead of the former hard-coded
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `_run_git` calls this runner with `GIT_METADATA_TIMEOUT_SECONDS` and converts `TimeoutExpired`/`OSError` into `AuthorityError`/`RouteIndexCensusError`; `_nul_records` splits its NUL-delimited stdout. | "git diff-files deletion census failed", "git census returned an empty NUL-delimited record" | mcp/src/agents_remember/kernel/route_index_census.py:91-91; mcp/src/agents_remember/kernel/route_index_census.py:222-222 |
| Carryover no longer defines its own input-bearing adapter: `require_git` delegates to `run_git`, and `patch_id` is the one caller that passes `input_text`. | `require_git`, `patch_id` | mcp/src/agents_remember/memory/carryover.py:113-117; mcp/src/agents_remember/memory/carryover.py:181-188 |


## Cross-Repo References

The runner can execute against configured code or external-memory repositories, but no sibling
repository defines this implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260821-CLIVE-L2 Current Contract

The current source seams include `IsolatedGitState`, `git_environment`, `run_git`. This supporting seam carries bounded error/command evidence used by the L2 owners. It does not become a second lifecycle authority, exception-family translator, or Git fallback path.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `IsolatedGitState`, `git_environment`, `run_git` at this ownership boundary. | `IsolatedGitState`; `git_environment`; `run_git` | mcp/src/agents_remember/kernel/git_command.py:85-91; mcp/src/agents_remember/kernel/git_command.py:94-100; mcp/src/agents_remember/kernel/git_command.py:103-154 |

## L34 Current Implementation

Binary configuration, commit, blob and tree readers preserve exact bytes. Private preparation uses the named sealed capability and journal-bound create/materialize/commit plan. Closeout publication performs an exact expected-old update-ref once, retaining command evidence and reopening physical/ref state; already-new and existing observations do not repeat the write. These functions retain the sole Git-spawn and repository-environment scrub boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| `GitCommandPlan` owns the corresponding behavior described above. | `GitCommandPlan` | `mcp/src/agents_remember/kernel/git_command.py:99-104` |
| `_GitRun` owns the corresponding behavior described above. | `_GitRun` | `mcp/src/agents_remember/kernel/git_command.py:108-112` |
| `admit_git_closeout_publication` owns the corresponding behavior described above. | `admit_git_closeout_publication` | `mcp/src/agents_remember/kernel/git_command.py:646-656` |
| `inspect_git_closeout_publication` owns the corresponding behavior described above. | `inspect_git_closeout_publication` | `mcp/src/agents_remember/kernel/git_command.py:659-669` |
| `closeout_publication_command` owns the corresponding behavior described above. | `closeout_publication_command` | `mcp/src/agents_remember/kernel/git_command.py:672-680` |
| `publish_git_closeout_ref` owns the corresponding behavior described above. | `publish_git_closeout_ref` | `mcp/src/agents_remember/kernel/git_command.py:683-706` |

## Update History
- 2026-09-06T22:41:21+00:00: Generated citation repair: `GIT_REPOSITORY_SELECTOR_ENV` repointed to mcp/src/agents_remember/kernel/git_command.py:55-64. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `GIT_LOCAL_TIMEOUT_SECONDS`; `GIT_REMOTE_TIMEOUT_SECONDS`; `GIT_METADATA_TIMEOUT_SECONDS` repointed to mcp/src/agents_remember/kernel/git_command.py:92-92; mcp/src/agents_remember/kernel/git_command.py:93-93; mcp/src/agents_remember/kernel/git_command.py:94-94. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


### 2026-09-06T17:13:06+00:00 — L34 implementation memory

Recorded the current private preparation/publication ownership from source. Existing verification identity is retained; this entry does not claim tests, certification or acceptance.

- 2026-08-31T20:30+02:00 — No content impact: corrected the source-file verification citation
  from the retired `mcp/tests/code_quality/` location to the current
  `mcp/test_support/agents_remember_test_support/code_quality/single_owner.py` owner. Git runner
  behavior and boundaries are unchanged.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: anchored 4 repository-internal reference rows and normalized 5 prose citation references for the single Git runner boundary; final scoped result 0 (checker-clean).

- 2026-07-31T20:50+02:00 — 260731-EFA-L3 curator: this file became the single owner, so the body
  was rewritten. Corrected the false "enforces a five-second timeout" claim: `run_git` now takes
  `timeout` and defaults to `GIT_LOCAL_TIMEOUT_SECONDS = 300`, with `GIT_REMOTE_TIMEOUT_SECONDS =
  120` and `GIT_METADATA_TIMEOUT_SECONDS = 30` as the other two classes cit:(["GIT_REMOTE_TIMEOUT_SECONDS = 120"], mcp/src/agents_remember/kernel/git_command.py:72-72), and callers pick
  one. Corrected the unconditional `stdin=DEVNULL` claim: stdin is `DEVNULL` only when the new
  `input_text` keyword is `None` cit:([`run_git`], mcp/src/agents_remember/kernel/git_command.py:85-151). Recorded the consolidation (six drifted `_run_git`
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
