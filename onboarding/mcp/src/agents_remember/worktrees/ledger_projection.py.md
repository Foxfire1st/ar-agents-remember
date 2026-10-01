# mcp/src/agents_remember/worktrees/ledger_projection.py

## Governing Overview

[Nearest governing overview](overview.md)

Working-candidate verification: source inspected at 2026-09-15T00:51 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Derives the consumer memory ledger from committed `Code-Commit` attribution and reports
informational differences from a disposable cache. It does not decide, create, or repair Git
transactions.

## Code Commentary

### Logic

`read_ledger_source(repository, commit, *, code_repository=None, repo_name=None)` calls
`derive_memory_ledger`. It never reads a `memory.md` blob or unions historical cached rows into the
result. When a code repository is supplied, missing code objects are excluded and reported;
`trailered_commits` counts attribution before that filtering. `_ledger_with_rows` recomputes both
the current header and oldest retained base pair. Empty attributed history remains an empty ledger.

`contract_ledger_projection` resolves the named source history and the actual selected memory tip.
A leaf uses its memory-worktree HEAD; a series uses the exact local memory work-branch tip.
`observed_ledger_state` reads the optional local cache only after resolving that Git state, and
`read_ledger_text` returns `None` for malformed cached text. Cache read failures are misses; an
unreadable repository, commit, or branch remains a distinct Git error.

`project_ledger` derives expected rows, order, base pair, and current header from the selected
memory Git history. Observed cache pairs cannot contribute mappings, even when both objects exist.
The removed `additions` input cannot inject a pair that no commit attributes. Source information is
reported relative to the selected history; it is not spliced into the expected rows as an
unconditional table tail.

`LedgerProjection` retains observed and computed rows/text, added/removed/reordered rows, headers,
source exclusions, and bounded operator diagnostics. Reasons distinguish missing code, unreachable
memory, absent attribution, and duplicate cached mappings. `cache_hit` and payload `cacheState`
distinguish a parseable observation from a miss; states are `cache-miss`, `diverged`, or
`already-correct`.

`is_fixed_point` and `is_interleaved_projection` are comparison data. `needs_write` compares cache
bytes with the canonical rendering; none of these properties grants Git authority.
`inspect_ledger_projection` reports unreadable history as `not-recomputed` with its reason.
Historical tables may still be explicit one-time migration input, but these runtime readers do not
use them as a substitute for committed attribution.

### Conventions

The frozen result family (`LedgerSource`, `LedgerWorld`, `LedgerRowRemoval`, `LedgerProjection`)
keeps omissions observable. Row payloads are capped at twenty with counts for elided detail.
The canonical ledger path constant remains owned by `kernel.memory_ledger`; this projection no
longer reexports it or accepts `read_ledger_source(relative=...)`.

### Invariants And Boundaries

- Only committed attribution determines expected mappings; source and branch code targets are checked when code authority is supplied.
- Cached headers, rows, order, and valid-looking pairs are observations, never input authority.
- Missing/malformed cache and absent attribution are valid data states, not Git refusals.
- Actual Git read failures remain explicit and cannot be repaired by editing cache bytes.
- The module reads and compares; it does not write onboarding, update refs, or create ledger commits.

### Todos

No new file-local follow-up is established by this documentation pass.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

- Source reads derive only Git attribution and recompute retained revision metadata. [1]
- Contract projection resolves actual memory history independently of cache availability. [2]
- Expected mappings and informational differences are built from the selected Git history. [3]
- The kernel walks committed attribution without reading a ledger file. [4]
- Cache forgery/misses and invalid attributed targets have focused regression coverage. [5]

### Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

No additional configured cross-repository evidence is claimed.

## Historical Context

The previous card recorded memory tip `f5edc613` as a 479-row cached table with one trailered commit,
and recorded 466 reachable rows plus 13 exclusions under the then-current union reader. It also
recorded the older `5e4899ea` observation as zero trailered commits among 958 reachable commits.
These are preserved observations from the earlier card, not measurements repeated in this pass or
claims about the working candidate. Their former table-union interpretation is superseded above.
