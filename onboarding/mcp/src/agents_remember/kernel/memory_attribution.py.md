# mcp/src/agents_remember/kernel/memory_attribution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/memory_attribution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T23:18+02:00 |
| lastVerifiedCommitHash |  `5bb124d43ea7b234edd570cf3995521e708714bd`|
| lastVerifiedCommitDate |  2026-09-13T23:22:52+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

The one reader of the ledger's **attribution**: it turns the `Code-Commit:` trailer a memory-content
commit carries into that commit's ledger row, so the code-to-memory map is read back out of the
hashed history instead of out of a table anyone edits. The trailer names the code commit the same
closeout landed, and the value sits inside the commit object, so no later step can add or change an
attribution without rewriting the commit that carries it.

The tracked `memory.md` table was hand-merged on every sync and produced three real hand-authoring
errors in one day (a superseded row kept, rows ordered so the validator rejects them, a header
disagreeing with its own first row). None of those needed judgement, and all three are properties of
a table that is written by hand rather than derived. This module is the derivation's reader half:
`worktrees/ledger_projection.read_ledger_source` calls it for the complete source ledger, so the
projection's trailing rows no longer come from the blob at `commit:memory.md`.

Nothing here writes. The module creates no commit, no file and no ledger row, and it does not retire
the tracked ledger commit — see the boundary note under `Invariants And Boundaries`.

## Code Commentary

### Logic

`attributed_commits` cit:([`attributed_commits`], mcp/src/agents_remember/kernel/memory_attribution.py:119-150) is one
`git log --date-order -z --format=%H%n%(trailers:key=Code-Commit,valueonly) <tip> [^<exclude>]`
cit:([`_LOG_FORMAT`], mcp/src/agents_remember/kernel/memory_attribution.py:60-60). Git's own trailer machinery renders the value, and
`-z` makes every record NUL-terminated so a message can never split into a second record.
`_attributed_records` cit:([`_attributed_records`], mcp/src/agents_remember/kernel/memory_attribution.py:153-159) reads the object
name from a record's first line and passes the remaining value lines to
`_trailer_value_from` cit:([`_trailer_value_from`], mcp/src/agents_remember/kernel/memory_attribution.py:162-175), which maps each line
through `_TRAILER_LINE` cit:([`_TRAILER_LINE`], mcp/src/agents_remember/kernel/memory_attribution.py:65-68) — the key anchored at the line
start, case-insensitively, followed by an object name of 4-64 hex characters. Only a line that is an
object name counts, so a value git emitted for a differently shaped trailer is not an attribution,
and the **last** match wins, which is what `%(trailers:key=...)` and
`git interpret-trailers --parse` report.

A commit with no trailer is still returned, as `AttributedCommit(memory_commit, None)`
cit:([`AttributedCommit`], mcp/src/agents_remember/kernel/memory_attribution.py:76-100), because "I read this commit and it
attributes nothing" is a different fact from "I did not read this commit".
`ledger_rows_from_attribution` cit:([`ledger_rows_from_attribution`], mcp/src/agents_remember/kernel/memory_attribution.py:184-203)
turns the walk into rows: one row per attributed commit, newest first, with no sort of its own —
the walk arrives in `git log` order, which is the order the ledger records, so this is a map, and a
commit that attributes nothing contributes nothing.

`AttributedCommit.row(code_repository=...)` cit:([`AttributedCommit.row`], mcp/src/agents_remember/kernel/memory_attribution.py:86-100)
applies the second truth test: a trailer naming a commit the code repository does not hold is not a
mapping, which is the same test the projection already applies to every row it keeps.
`code_commit_exists` cit:([`code_commit_exists`], mcp/src/agents_remember/kernel/memory_attribution.py:178-181) is the one
`git cat-file -e <commit>^{commit}` definition in the package —
`worktrees/ledger_projection.code_commit_exists` cit:([`code_commit_exists`], mcp/src/agents_remember/worktrees/ledger_projection.py:404-407)
now delegates to it instead of repeating the test.
`MemoryAttributionError` cit:([`MemoryAttributionError`], mcp/src/agents_remember/kernel/memory_attribution.py:71-72) is the refusal for a
history that cannot be walked at all; the caller converts it into its own remedy-bearing refusal,
which is how the projection keeps one refusal vocabulary.

**The walk is the whole ancestry rather than the first-parent line, and that is measured, not
preferred.** Measured on the real memory repository at tip `5e4899ea` with
`git merge-base --is-ancestor` — the projection's own truth test, which resolves object names — the
tracked table's
476 rows name 442 memory commits on the tip's first-parent line and 34 that are not on it; 21 of
those 34 are still ancestors, so a first-parent-only walk would silently drop 21 mappings the full
walk reaches, and the remaining 13 name a memory commit that is not an ancestor of the tip at all
(476 = 442 + 34, and 463 rows name an ancestor: the 442 on the line plus the 21 off it). Reading only
the line is therefore the "partial coverage looks like a gap" failure the trailer rule exists to
prevent. The older figures this module's and the test's docstrings carry — 35 rows off the line, 441
on it, 462 reachable, 14 not — came from comparing the table's written cells against `git rev-list`
output as TEXT; the whole difference is the table's single truncated memory-commit cell, `684c33b2`,
which resolves to a real ancestor on the first-parent line but never matches a full object name as
text.

`parse_code_commit_trailer` cit:([`parse_code_commit_trailer`], mcp/src/agents_remember/kernel/memory_attribution.py:103-116) is the
message-level reader for a caller that holds a message rather than a repository: it scans the whole
message for a matching line and returns the last one, so a body that merely mentions
`Code-Commit:` is not an attribution and a caller cannot append a second one and have it read as the
first. `exclude` is the branch selector: everything reachable from `tip` and not from `exclude` is
"this branch's own commits", which is how a caller asks for its own rows rather than the source's.

### Conventions

A frozen dataclass (`AttributedCommit`) plus module-level functions over `Path`s, mirroring
`kernel/memory_ledger.py`; the error type subclasses `RuntimeError` so a caller can wrap it in its
own refusal. The log format is a module constant rather than an inline argv string, because the
trailer key appears in the format, the value regex and the value-line re-wrap and must not be spelled
three ways.

**The two-literal drift this card first recorded is fixed, and the fix is the direction the layering
requires.** The first version of this change set declared the key twice — here, from this module's
constant comment, and again as a literal in `models/closeout/input.py` — while the comment claimed the
model imported it from here. The failure that shape produces is the worst one available: a writer
emitting trailers the reader silently ignores looks like "no attribution exists" rather than like a
bug. `models/closeout/input.py` now imports the key from here
cit:([`CODE_COMMIT_TRAILER_KEY`], mcp/src/agents_remember/models/closeout/input.py:9-9) and its literal
is deleted, so `grep -rn '"Code-Commit"' --include=*.py mcp/` returns exactly one hit, this module's
declaration cit:([`CODE_COMMIT_TRAILER_KEY`], mcp/src/agents_remember/kernel/memory_attribution.py:55-55). The direction is
kernel → models because the layer contract says so rather than because either module prefers it:
`layers.toml` declares `order = [errors, kernel, models, ...]` with "a module in package P may import
package Q only when rank(Q) < rank(P)"
cit:(["a module in package P may import package Q only when rank(Q) < rank(P)"], layers.toml:25-25), so
`kernel` ranks below `models` and a kernel module importing a model would break the declared contract;
a grep over `mcp/src/agents_remember/kernel/` finds zero imports of `agents_remember.models`, so the
cycle risk is real in the rejected direction and absent in the chosen one. The reader is the
lower-level fact — it reads a hashed object, and the writer is a caller of it, not its owner — and the
constant's comment now carries that reasoning.

### Invariants And Boundaries

- **The census is git's ancestry walk, not the table.** A row exists only for a commit that really
  carries the trailer; nothing is inferred from `memory.md` or from any side file.
- **One trailer, one row.** A commit with no trailer contributes no row. That is the deliberate class
  of memory commits with no code counterpart to name — a policy edit, a settings edit, a README, and
  the `memory.md`-only ledger commit itself. Absence is the detection, not a state to tolerate.
- **The attribution is bound by the hash.** The trailer is part of the commit object's message, so
  it cannot be added or altered later without rewriting the commit; `git notes` was rejected for
  exactly that reason.
- **The value must name a commit the code repository holds** before the row can mean anything.
- **The last trailer wins** in both readers, matching `%(trailers:key=...)` and
  `git interpret-trailers --parse`.
- **The whole ancestry is read.** A mapping that arrived through a merge is still an ancestor of the
  tip and must be found; a first-parent walk is not an acceptable implementation of this.
- **An unreadable history refuses.** `MemoryAttributionError` distinguishes "cannot be walked" from
  "attributes nothing"; collapsing the two would turn a broken repository into an empty ledger.
- **This module does not retire the tracked ledger.** `memory.md` is still written, committed and
  proved by the closeout family, and the ledger commit is still one of a closeout's three commit
  legs; reading the source ledger from the attribution is a reader change only. Retiring the tracked
  ledger commit spans worktree closeout, direct landing, queue recovery, series closeout, integration
  and sync, and is owned by this master's own leaf, not by this module.

### Todos

None. The second-literal defect this card first recorded was fixed in the same leaf; it is kept in
`Conventions` and in the history rather than deleted, because the failure shape it names — a writer
whose key the reader does not parse — is the one this module exists to make impossible.

## Docs References

The trailer is git's own mechanism rather than a repository-local format, but nothing in this module
depends on a documented git behaviour beyond `%(trailers:key=...)`, `-z`, and
`git cat-file -e <commit>^{commit}`; the repository's configured `system/sources.md` names no Domain
Documentation source for this code repository, so no external document is cited here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured for this repository; the proving evidence is git's own trailer rendering plus this repository's source. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one reader of the attribution: one `git log` record per reachable commit, the trailer value from git's own trailer machinery, the last object name winning. | `attributed_commits`; `_LOG_FORMAT`; `_attributed_records`; `_trailer_value_from`; `_TRAILER_LINE` | mcp/src/agents_remember/kernel/memory_attribution.py:119-150; mcp/src/agents_remember/kernel/memory_attribution.py:60-60; mcp/src/agents_remember/kernel/memory_attribution.py:153-159; mcp/src/agents_remember/kernel/memory_attribution.py:162-175; mcp/src/agents_remember/kernel/memory_attribution.py:65-68 |
| One row per attributed commit, newest first, with the code-commit truth test applied where the row is created. | `ledger_rows_from_attribution`; `AttributedCommit`; `AttributedCommit.row` | mcp/src/agents_remember/kernel/memory_attribution.py:184-203; mcp/src/agents_remember/kernel/memory_attribution.py:76-100; mcp/src/agents_remember/kernel/memory_attribution.py:86-100 |
| The message-level reader, used where the caller holds a message instead of a repository. | `parse_code_commit_trailer` | mcp/src/agents_remember/kernel/memory_attribution.py:103-116 |
| The single `cat-file -e` object test, which the projection's own `code_commit_exists` now delegates to. | `code_commit_exists` | mcp/src/agents_remember/kernel/memory_attribution.py:178-181; mcp/src/agents_remember/worktrees/ledger_projection.py:404-407 |
| The refusal for a history that cannot be walked, which the projection converts into a remedy-bearing `LedgerProjectionRefusal`. | `MemoryAttributionError`; `read_ledger_source` | mcp/src/agents_remember/kernel/memory_attribution.py:71-72; mcp/src/agents_remember/worktrees/ledger_projection.py:279-311 |
| The row type this module produces and the ledger format it never writes. | `LedgerRow` | mcp/src/agents_remember/kernel/memory_ledger.py:23-25 |
| The writer's key is this module's declaration: `models/closeout/input.py` imports it and declares no literal of its own. | `CODE_COMMIT_TRAILER_KEY` | mcp/src/agents_remember/kernel/memory_attribution.py:55-55; mcp/src/agents_remember/models/closeout/input.py:9-9 |
| The layer contract that fixes the import direction: the ordered packages, and the rule that a package may import only a lower rank. `kernel` is rank 1 and `models` rank 2, so models may import kernel and not the reverse. | "a module in package P may import package Q only when rank(Q) < rank(P)"; "The strict order, low to high. Position in this list IS the rank."; `order` | layers.toml:25-25; layers.toml:29-31; layers.toml:32-59 |
| The round trip that proves the writer's key and the reader's key are ONE key: the real writer renders the trailer, the message is committed as a real memory commit, and the real reader resolves the code commit out of it. The case restates no key literal, because a test that compared a literal against a literal could not catch a changed constant. | `test_the_rendered_trailer_is_the_one_the_reader_parses` | mcp/tests/test_memory_ledger.py:562-597 |
| The writer that renders the trailer into the memory-content message through the imported key, and the two routes that call it. | `memory_content_message`; `CODE_COMMIT_TRAILER_KEY` | mcp/src/agents_remember/models/closeout/input.py:145-160; mcp/src/agents_remember/models/closeout/input.py:160-160 |

## Cross-Repo References

The repository this module reads is the external memory repository, a separate Git repository
addressed through the worktree contract rather than an ambient checkout. The evidence below is the
reader path that makes it the memory history's own record.

| Finding | Anchor | Source |
| --- | --- | --- |
| The source-ledger reader is the one caller that feeds this module's rows into the projection, at the commit `resolve_memory_source_commit` resolves from the contract. | `read_ledger_source`; `resolve_memory_source_commit` | mcp/src/agents_remember/worktrees/ledger_projection.py:279-311; mcp/src/agents_remember/worktrees/ledger_projection.py:251-276 |

## Update History

- 2026-09-13T23:18+02:00 — 260913-LCA-L2 curator (same uncommitted change set): **the two-literal
  defect this card first recorded is fixed, and the entry below stands as the record of what was
  true when it was found.** The L2 curator found it in this pass's first review — the module's
  docstring claimed an import that did not exist — and the owner fixed it in the same change set by
  wiring the direction the layering requires: the writing model now imports the key from here
  (`models/closeout/input.py:9`) and its own literal is deleted, so
  `grep -rn '"Code-Commit"' --include=*.py mcp/` returns exactly one hit — this module's
  declaration, which moved from `:49` to `:55` because the constant's comment block grew to carry the
  reasoning — and every other occurrence is prose. The rejected direction was checked on a concrete
  ground rather than a preference: `layers.toml` declares `order = [errors, kernel, models, ...]`
  with "a module in package P may import package Q only when rank(Q) < rank(P)", so a kernel module
  importing a model would break the declared contract, and a grep over
  `mcp/src/agents_remember/kernel/` finds zero imports of `agents_remember.models`. A new case,
  `test_the_rendered_trailer_is_the_one_the_reader_parses`, drives the real writer's rendered message
  through a real commit and back out through the real reader (the owner reports reintroducing the
  writer-side defect fails exactly that case and nothing else); the test modules keep literal
  `Code-Commit` text as independent oracles on purpose, so those must not be "corrected" to read the
  constant. `Conventions`, `Todos` and the reference rows above are rewritten to the resolved state —
  the history is where the defect stays visible. Every citation in this card was repointed to the
  grown file. Verification metadata remains intentionally empty (unstamped): closeout owns the stamp.

- 2026-09-13T23:06+02:00 — 260913-LCA-L2 curator (uncommitted change set on `ar/260913-lca-l2-ar`):
  created the one-to-one sidecar for this new kernel module. Records the attribution reader — the
  full-ancestry `git log` census, the last-trailer-wins rule in both the commit walk and the
  message parse, the one-row-per-attributed-commit map with the code-commit truth test applied at
  row creation, and the single `cat-file -e` definition the projection's `code_commit_exists` now
  delegates to. States the measured reason the walk is the whole ancestry (at tip `5e4899ea`: 442 of
  the table's 476 rows on the first-parent line, 34 off it, 21 of those still ancestors), the
  boundary that this module only reads and the tracked ledger commit is **not** retired here, and
  the one measured defect it carries: the module docstring says `models/closeout/input.py` imports
  `CODE_COMMIT_TRAILER_KEY` from here, and that import does not exist — the writer declares its own
  literal at `models/closeout/input.py:16`, so the two agree only by value. Verification metadata is
  intentionally empty (unstamped): the candidate is uncommitted and no commit contains this file
  yet, so closeout owns the stamp.
