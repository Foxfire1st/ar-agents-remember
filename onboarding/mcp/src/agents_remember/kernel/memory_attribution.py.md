# mcp/src/agents_remember/kernel/memory_attribution.py

## Governing Overview

[Nearest governing overview](../../../overview.md)

Working candidate verification: source inspected at 2026-09-15T01:02 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Owns the shared `Code-Commit` key, memory-message renderer, and committed-attribution reader. The
attribution is part of the memory commit object; this module does not create commits or files.

## Code Commentary

### Logic

`render_memory_content_message` appends a separate final attribution block after the supplied
body; the caller body remains verbatim. Worktree closeout (including recovery when memory is
still owed) and direct landing use `EffectiveCloseoutInput.memory_content_message`; baseline
adoption calls the shared renderer directly. Carryover writes the recovery worktree but commits
nothing; normal recovery-leaf closeout publishes its judged tree. The exact-path historical
rewriter `kernel/memory_backfill.py` reuses the original commit tree and is not a fourth
memory-content route. The prepared closeout producer is retired.

`attributed_commits` reads Git's trailer values for every commit reachable from the requested tip,
optionally excluding another history. It uses the full ancestry rather than only first parents,
so a mapping introduced on a merged branch remains visible. NUL-delimited records preserve commit
boundaries. A readable commit with no matching attribution is returned with `code_commit=None`;
an unreadable history raises `MemoryAttributionError` instead of looking like empty attribution.

`_trailer_value_from` accepts the declared hash-shaped value from Git's value-only output and keeps the last matching value. The separate message parser, `parse_code_commit_trailer`, normalizes line breaks, splits blank-line runs and inspects only the final paragraph after a preceding paragraph. That paragraph must consist of trailer-shaped key/value lines and their indented continuations; unindented ordinary prose refuses attribution. Continuation fragments are joined before the existing case-insensitive `Code-Commit` matcher accepts a four-to-sixty-four-character hexadecimal value. The last matching value in that final block wins. A matching body line outside it supplies no attribution. Other Git trailer shapes are outside this parser account.

`ledger_rows_from_attribution` preserves the Git walk's ordering and omits unattributed commits. `AttributedCommit.row(code_repository=...)` optionally checks that the named code commit exists.

The documentation correction removes the former runtime-table fallback story. This reader's
runtime implementation remains trailer-based. Explicit historical-table migration is owned by
`memory_backfill`, not activated by missing attribution in this module.

### Conventions

One frozen `AttributedCommit` value and module-level functions expose the reader. SHA-shaped text
is syntax; the optional code-repository check establishes object existence. The writer returns a
message string only and owns no publication or backfill policy.

### Invariants And Boundaries

- No cached or historical table is a runtime fallback for absent attribution.
- Unattributed commits and unreadable Git history remain different facts.
- The full reachable ancestry includes merge-side attribution.
- The shared key and renderer remain the only production spelling/format owner.
- Code-object validation applies when the caller supplies the code repository.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

The earlier L9 inspection account is historical. The references below support current source declarations and test assertions; they do not establish execution or acceptance.

- The single key, log format, renderer, and attribution value. [1]
- The history walk and message/value parsers define the actual read behavior. [2]
- Row conversion and optional object validation. [3]
- Runtime ledger derivation never consults cache text. [4]

- The source census and behavioral renderer case keep the producer seam visible. [5]
- The message parser reads only the final trailer-shaped paragraph, unfolds continuations and applies the existing last-match value syntax. [10]

- The full ancestry reader, final-block message parser and Git value-only parser have separate input boundaries. [6]
- Attributed rows optionally require a real code commit, retain supplied order and omit unattributed commits. [7]
- The consumer ledger is derived from committed attribution without consulting cached ledger text. [8]

### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.

- The three content routes use the one attribution renderer; converted carryover commits nothing and the exact historical rewriter preserves the original tree. [9]
