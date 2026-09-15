# mcp/src/agents_remember/models/knowledge/source.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/source.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T22:40+02:00 |
| lastVerifiedCommitHash | `60e0820e6cb3b1d160518b9f8c7ac6241323a281`|
| lastVerifiedCommitDate | 2026-09-15T22:46:24+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[models route overview](../../../overview.md)

## Purpose

The shared source vocabulary: what a knowledge claim points at, in which exact revision of the selected
repository, and via which locator.

## Code Commentary

### Logic

`GitBlobIdentity` is the one v1 source identity (`kind: "git_blob"` plus an object id matching
`GIT_OBJECT_PATTERN`), and `SourceIdentity` is an alias of it. Three locators are declared: `FileLocator`
(`kind: "file"`), `LineRangeLocator` (`kind: "line_range"`, one-based inclusive `start_line`/`end_line`, with a
validator that refuses an `end_line` preceding `start_line`) and `SymbolLocator` (`kind: "symbol"`, nonblank
`language` and `qualified_name`). `SourceLocator` is the discriminated union of the three, keyed on `kind`.

`SourceAnchor` is one attributed location: a `UUID` `anchor_id`, a repository-relative `path`, a
`SourceIdentity`, a `SourceLocator` and the `Authorship` envelope. Its `_require_confined_relative_posix_path`
validator refuses a blank path, an absolute or `~`-prefixed path, a backslash separator, a NUL byte, and any
empty, `.` or `..` segment, and bounds the length.

### Conventions

A stored locator is a well-formed record even when no resolver currently supports it: a symbol locator remains
readable after the symbol moves, and losing resolvability never erases the claim.

### Invariants And Boundaries

- The blob identity is a Git object identity, **not a copy of the bytes** — there is no second content store here.
- Path shape is checked at the vocabulary boundary; resolution against a real filesystem belongs to the filesystem
  boundary, so an absolute, drive, UNC, backslash or parent-escaping path never reaches a stored record.
- `SourceLocator` is declared *shared* with the selective read/diff contributor (KS-R07/KS-R08): the union is
  designed so that consumer can discriminate on `kind` without a second locator vocabulary. That consumer does not
  exist yet; nothing here claims it does.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The single v1 source identity and the alias a caller may name. | `GitBlobIdentity`; `SourceIdentity` | mcp/src/agents_remember/models/knowledge/source.py:28-35 |
| The three locators and the discriminated union over them. | `FileLocator`; `LineRangeLocator`; `SymbolLocator`; `SourceLocator` | mcp/src/agents_remember/models/knowledge/source.py:38-79 |
| The anchor model and its repository-relative POSIX path rule. | `SourceAnchor`; `_require_confined_relative_posix_path` | mcp/src/agents_remember/models/knowledge/source.py:82-115 |
| The stored `source_anchor` table, its immutability trigger and its canonical column order. | `source_anchor`; `source_anchor_no_rewrite` | mcp/src/agents_remember/memory/knowledge/schema.py:217-229; mcp/src/agents_remember/memory/knowledge/schema.py:335-339 |
| The codec that stores and decodes an anchor row through the discriminated union. | `anchor_row`; `decode_anchor_row` | mcp/src/agents_remember/memory/knowledge/records.py:208-226 |
| The later requirement packets this vocabulary is declared shared with. | `KS-R07`; `KS-R08` | ar-coordination/tasks/agents-remember/260915_knowledge-substrate/requirements/KS-R07-v1-selective-snapshot-read.md; ar-coordination/tasks/agents-remember/260915_knowledge-substrate/requirements/KS-R08-v1-invariant-family-candidate-diff.md |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new shared source vocabulary. It records that the locator union is declared shared with a read/diff consumer that does not exist yet, and that the blob identity is a Git object identity rather than a byte copy. Verification metadata remains empty until closeout stamps the code commit.
