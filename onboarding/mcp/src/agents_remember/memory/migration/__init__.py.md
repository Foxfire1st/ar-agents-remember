# mcp/src/agents_remember/memory/migration/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/migration/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:00+02:00 |
| lastVerifiedCommitHash |  `2dcacb27446ecbaba01b69ee32e2ac40a1713b09`|
| lastVerifiedCommitDate |  2026-09-18T17:26:34+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The package surface and the contract statement for staged legacy migration: the scope inventory, the
parser, the mappings and the census. The docstring fixes what the package is allowed to do in one
sentence — it "reads the Markdown-era onboarding corpus and describes it. It **writes nothing to the
corpus**" — and names the single exception on the write side: the shipped candidate batch operation,
reached through the census record group in `memory/knowledge/census_records.py`. It also fixes the
package's place: a subpackage of `memory` rather than a new top-level package, because it ranks with
the thing it measures, and `layers.toml` already puts `memory_quality` below `memory` since reading
and judging memory content is what both do.

## Code Commentary

### Logic

**One statement, and the module is that statement.** The file is a single module docstring and
nothing else: no imports, no `__all__`, no names, no callables. Its four paragraphs carry the whole
contract — what the package reads, the single write path it is permitted, why it is a subpackage of
`memory`, and the interpretation boundary below. A reader who opens this file learns the package's
scope without opening a module, and the modules themselves carry their own docstrings for their own
responsibilities.

**The corpus direction is one-way, and the exception is named.** The docstring's second sentence is
the package's strongest claim: an artifact is read, parsed into claims and dispositions, and reported
against a frozen baseline — and the corpus is never written. The write path is not described as
"somewhere else"; it is named as the shipped candidate batch operation through the census record group
in `memory/knowledge/census_records.py`, so "this package writes nothing to the corpus" and "the
records it produces are stored through the shipped path" are two statements a reader can check
separately.

**The boundary is that nothing here interprets.** The last paragraph enumerates the division by the
verb each part is allowed: the parser reports what it read, a mapping names where a read artifact
goes, a reference resolves to one of three recorded states, and a mismatch is reported as the
mechanical fact it is. The semantic half is assigned away in the same paragraph — categories,
verdicts and mismatch classes are authored by a curator in record kinds other leaves own, and this
package only reads them. That is the invariant behind the census's separation of measurement from
curation: a module under this package has no field and no code path for a judgment.

**Rank is stated as a consequence, not a preference.** The subpackage placement is argued from
`layers.toml`: the package reads the memory repository's onboarding tree, and `memory_quality` ranks
below `memory` for the same reason, so joining `memory` keeps one ranking rule rather than adding a
second one for a package that does the same kind of work.

### Conventions

The module is documentation-only. It declares no `__all__`, so nothing is re-exported from this
package surface and every consumer imports its module by full path — `memory.migration.baseline`,
`memory.migration.census`, `memory.migration.cutover` — which is exactly how the tests and the
package's own modules reach one another. It has no imports, so importing the package has no side
effect and pulls in no module of the package. Its one naming decision, stated in the docstring, is the
package's own location under `memory/`.

### Invariants And Boundaries

- **The corpus is read, never written.** Nothing in this package writes to the Markdown-era onboarding
  corpus; the only write path is the shipped candidate batch operation, named by module in the
  docstring rather than left implicit.
- **This surface exports nothing.** There is no `__all__` and no imported name here, so the package
  surface cannot silently acquire a re-export or an import-time side effect; consumers address the
  modules directly.
- **Nothing in the package interprets.** Semantic categories, verdicts and mismatch classes are
  curator-authored records owned by other leaves; this package reads them and authors none.
- **The package's depth is part of its contract.** It sits under `memory` because it reads and
  reports on memory content, which is the ranking `layers.toml` already records for
  `memory_quality`.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

This file is the package's contract statement rather than an implementation: it fixes the read-only
direction toward the corpus, names the one shipped write path, states the interpretation boundary, and
argues the package's place in the layer ranking. The rows below cite that statement and the four
things it points at — the census record group, the layer ranking, the corpus the package reads, and
the interpretation boundary that the shipped write path enforces.

| Finding | Anchor | Source |
| --- | --- | --- |
| The package's scope and its strongest boundary in one statement: it reads the Markdown-era onboarding corpus, describes it, and writes nothing to it. | "writes nothing to the corpus"; "reported against a frozen baseline"; `memory.knowledge.census_records` | mcp/src/agents_remember/memory/migration/__init__.py:1-16 |
| The one write path the package uses, named by module: the shipped candidate batch operation reached through the census record group. | `apply_census_command`; `CENSUS_OPERATION` | mcp/src/agents_remember/memory/knowledge/census_records.py:100-102; mcp/src/agents_remember/memory/knowledge/census_records.py:401-401 |
| The ranking the package's placement is argued from: `memory_quality` below `memory`, which is why reading and reporting on memory content belongs under `memory`. | `memory_quality` | layers.toml:197-205; layers.toml:206-219 |
| The interpretation boundary: semantic categories, verdicts and mismatch classes are curator-authored in other leaves' record kinds, and this package only reads them. | `Mismatch` | mcp/src/agents_remember/memory/migration/resolution.py:101-110 |
| The census record kind the package's own write path carries, declared in the wire vocabulary rather than here. | `CensusInventoryRowPayload`; `CENSUS_PAYLOAD_MODELS` | mcp/src/agents_remember/models/knowledge/census.py:147-147; mcp/src/agents_remember/models/knowledge/census.py:346-350 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The docstring describes one local
onboarding corpus read at a frozen baseline and one local candidate store's write path; nothing here
reaches another repository, another dataset or a remote.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): created this one-to-one card for the `memory.migration` package surface. The file is a single module docstring with no imports, no `__all__` and no callables, so the card records the statement rather than a mechanism: the package reads the Markdown-era onboarding corpus and describes it while writing nothing to it, and the one write path it uses is the shipped candidate batch operation reached through the census record group in `memory/knowledge/census_records.py`. It records the interpretation boundary that makes the census's measurement separable from curation — the parser reports what it read, a mapping names where a read artifact goes, a reference resolves to one of three recorded states, and a mismatch is reported as the mechanical fact it is, while categories, verdicts and mismatch classes stay curator-authored in record kinds other leaves own. It records the placement argument the docstring makes from the layer ranking, where `memory_quality` sits below `memory` because reading and judging memory content is what both do, so the package joins `memory` rather than becoming a new top-level package. It records that the surface exports nothing, so every consumer imports its module by full path, which is how the package's own modules and the census cases reach one another. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
