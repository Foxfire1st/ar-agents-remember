# mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T10:20+02:00 |
| lastVerifiedCommitHash | `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` |
| lastVerifiedCommitDate | 2026-09-17T10:09:37+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l14-ar` uncommitted source; base `0346da9c572e1eb913a8eb4130e9a9e9d37343c8` |
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Reduce every reason a path may be left out of a citation index to one answer and one record:
*is this path outside the candidate population, and which rule said so*. The module is the
**shared exclusion register** three sources feed, and it is a record as much as a filter — the
rule set it resolves is serialized onto the manifest of every published generation, so a later
reader sees which rules produced an index instead of reconstructing them from the checkout.

The register, its caps and its settings key are **mode-independent**: nothing here branches on
the memory storage mode.

## Code Commentary

### Logic

`resolve_exclusion_register` is the one construction point for an acquisition. It reads the
memory layer's `system/settings.json` through `read_citation_index_settings` (unless the caller
already holds the parsed settings), folds the settings excludes and the caller's own excludes
into `ExclusionRule` records carrying their `source`, and attaches the code root's
`.gitignore` lines as written plus the caller's statement of `gitignore_authority`.

The three sources and what each one means:

| Source | Where it comes from | How it is matched |
| --- | --- | --- |
| `pathRules.exclude` (`EXCLUSION_SOURCE_PATH_RULES`) | `onboarding.pathRules.exclude.paths` in the memory layer's `system/settings.json` — the register the exclusion review agrees with the user **before** closeout | `matches_any` from `kernel.coordination_context.storage`, the same matcher the storage resolver and the drift check already use |
| `gitignore` (`EXCLUSION_SOURCE_GITIGNORE`) | the code repository's own `.gitignore` | inside a Git work tree **Git is the authority** (`ls-files --exclude-standard` already removed them) and the register only records the patterns; outside a work tree `FallbackIgnoreMatcher` applies them |
| `caller` (`EXCLUSION_SOURCE_CALLER`) | `exclude=` on the `citation_fix` MCP tool and `--exclude` on the CLI, scoped to that one call | exactly like `pathRules.exclude`, through the same `matches_any` |

`excluding_rule` deliberately consults **only** the `pathRules.exclude` and `caller` components.
The `.gitignore` component is a separate branch because `matches_any` does not implement Git's
anchoring and negation rules; a pattern is therefore never read twice.

`validate_caller_excludes` refuses a caller pattern **by name** when it cannot mean anything — an
empty pattern, an absolute one, or one carrying `..` — rather than letting it quietly match
nothing, because "I excluded it and it is still indexed" is harder to see than a refusal at the
call.

### The non-Git fallback and its deliberate divergence from Git

`FallbackIgnoreMatcher` is the bounded `.gitignore` reading the non-Git fallback walk uses.
`parse_gitignore` reduces each line to `GitIgnoreRule` (comments and blanks skipped, `!` negation,
a leading `/` anchored to the code root, a trailing `/` directory-only, `*`/`?` not crossing `/`
and `**` crossing it); a character class is not part of this subset and matches literally, which
is why no unescaped bracket ever reaches `re`.

Two properties matter and are both stated in the source:

- **A file inherits its ancestors' rules.** `vendor/` is directory-only and never matches the file
  `vendor/lib.py` directly, so the decision is taken over the path's whole ancestor chain,
  shallowest first, last match wins (`excludes`, `_ancestry`). Dropping that ancestor walk is what
  made a negation silently disable directory-only exclusion.
- **This is the register's rule, not Git's, and the difference is deliberate.** Git does *not*
  re-include a file whose parent directory is excluded — `git check-ignore vendor/keep.py` reports
  it ignored under `vendor/` plus `!vendor/keep.py`, because Git never descends into an excluded
  directory to find the negation. The register **does** re-include it, because the register's
  contract answers *"did the exclusion review's rules admit this file?"* rather than *"what would
  `git add` do?"*. The divergence is pinned by
  `test_the_register_admits_a_negated_file_under_an_excluded_directory_where_git_does_not`, so a
  future reader cannot mistake it for an accident. The direction is the safe one: the register
  admits a file, it never silently drops one Git would have kept.

`has_negation` is reported rather than hidden because it changes how the walk behaves: with a
negation present a directory is never pruned, so the walk descends and decides per file. Pruning a
directory a later `!` rule re-includes would be the silent omission this subset must not make.

### Conventions

- Exceeding a cap is a **reported skip naming the file and its size** — never a silent omission and
  never a whole-tree refusal. The caps themselves live in `source_index_state`; this module only
  reads their overrides.
- A missing `system/settings.json` is the ordinary state of a fresh memory layer and means "no
  register yet"; an unreadable or malformed one is refused by name, because falling back to the
  defaults would silently index paths the user excluded.
- `gitignore_authority` is an explicit argument because the acquisition has already asked Git the
  same question and must not ask it twice.

### Invariants And Boundaries

- One register means one thing: a pattern read through `pathRules.exclude` matches identically in
  the storage resolver, the drift check and the citation index.
- `.gitignore` patterns are recorded whether or not this register applies them; the record's job is
  to say which rule set was in force, and inside a work tree the answer is "these, honoured by Git".
- Nested `.gitignore` files are read only in a work tree, where Git owns them.
- The register reports membership facts; it never decides policy.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one construction point folding settings, ignore file and call into one register. | `resolve_exclusion_register` | mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py:196-226 |
| The three source constants the register records. | `EXCLUSION_SOURCE_PATH_RULES`; `EXCLUSION_SOURCE_GITIGNORE`; `EXCLUSION_SOURCE_CALLER` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:54-61 |
| The three `gitignoreAuthority` values the register may carry. | `GITIGNORE_AUTHORITY_GIT`; `GITIGNORE_AUTHORITY_REGISTER`; `GITIGNORE_AUTHORITY_ABSENT` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:45-52 |
| Only the path-rule and caller components are matched here; the ignore file is a separate branch. | `excluding_rule` | mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py:144-161 |
| A caller pattern that cannot mean anything is refused by name instead of matching nothing. | `validate_caller_excludes` | mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py:171-193 |
| The code root's ignore lines are recorded as written, minus comments and blanks. | `read_gitignore_patterns` | mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py:229-249 |
| The bounded fallback matcher, its ancestor walk and its pinned divergence from Git. | `FallbackIgnoreMatcher` | mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py:253-297 |
| Last match wins over the path's whole ancestor chain. | `_ancestry` | mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py:308-318 |
| A negation prevents directory pruning, so the walk descends and decides per file. | `has_negation` | mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py:286-288 |
| A path rule excludes a file by name, and a directory by name or by its contents. | `_pattern_excludes` | mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py:164-168 |
| The one glob matcher shared with the storage resolver and the drift check. | `matches_any` | mcp/src/agents_remember/kernel/coordination_context/storage.py:50-56 |
| The register is built from the memory layer's own settings keys. | `read_citation_index_settings` | mcp/src/agents_remember/memory_quality/style/citations/citation_index_settings.py:56-85 |

## Cross-Repo References

No sibling-repository contract defines these values.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T10:20+02:00 — 260915-CAPS-L14 curator: created this card for the module the leaf adds. Records the three sources feeding one register, the `matches_any` semantics shared with the storage resolver and the drift check, the two-part `.gitignore` story (Git is the authority inside a work tree; the bounded matcher applies the patterns outside one), the reported-skip rule, and the register's **deliberate, pinned divergence from Git** on a negated file under an excluded directory. Verification metadata is left at this leaf's synced base `0346da9c` with a `reviewedWorkingCandidate` row, because the candidate is deliberately uncommitted — the governed closeout stamps the real code commit and no hash or digest was invented here.
