# mcp/src/agents_remember/models/knowledge/source.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/source.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T23:50+02:00 |
| lastVerifiedCommitHash | `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80`|
| lastVerifiedCommitDate | 2026-09-20T02:00:33+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

The shared source vocabulary: what a knowledge claim points at, in which exact revision of the selected
repository, and via which locator. The anchor is split into a **draft** — what the author decided — and
the **stored** record, which is the draft plus the provenance envelope that recorded it.

## Code Commentary

### Logic

`GitBlobIdentity` is the one v1 source identity (`kind: "git_blob"` plus an object id matching
`GIT_OBJECT_PATTERN`), and `SourceIdentity` is an alias of it. Three locators are declared: `FileLocator`
(`kind: "file"`), `LineRangeLocator` (`kind: "line_range"`, one-based inclusive `start_line`/`end_line`, with a
validator that refuses an `end_line` preceding `start_line`) and `SymbolLocator` (`kind: "symbol"`, nonblank
`language` and `qualified_name`). `SourceLocator` is the discriminated union of the three, keyed on `kind`.

`SourceAnchorDraft` is one attributed location as its author supplies it: a `UUID` `anchor_id`, a
repository-relative `path`, a `SourceIdentity` and a `SourceLocator`. Its
`_require_confined_relative_posix_path` validator refuses a blank path, an absolute or `~`-prefixed path, a
backslash separator, a NUL byte, and any empty, `.` or `..` segment, bounds the length, and — since 260915-KS-L7 —
**delegates the Git-pathspec half to the one shared `require_plain_git_path`**, so a spelling such as
`:(exclude)src/x.py` cannot be stored. `SourceAnchor` subclasses it and adds the `Authorship` envelope, so
provenance cannot be supplied by a caller who is only proposing a location.

**Why the pathspec refusal lands here rather than only at the tree lookup:** a stored path is later handed to
`git ls-tree`, and Git reads a leading `:` as pathspec magic — answering with an error (`:(exclude)`, `:!`) or
about a *different* location (`:(top)`, `:/`). Reporting that answer as an absent path would be a false
statement about the repository. **The glob characters `*`, `?` and `[` are admitted**, because `ls-tree`
addresses them literally; refusing them (this leaf's round-1 predicate) made a legitimate anchor un-authorable
and, through the read path, reported a file the tree really holds as `path_absent`.

`anchor_id` is a real `UUID`, not a pattern-constrained string. This is a repair of an L1 defect: the
field was declared `anchor_id: UUID = Field(pattern=UUID_PATTERN)`, and Pydantic refuses to apply a string
`pattern` constraint to its UUID schema, so **every** anchor construction raised `TypeError: Unable to
apply constraint 'pattern' … for schema of type 'uuid'`. It was latent because no L1 test constructed an
anchor. The canonical stored text is now derived from the parsed value at the storage boundary
(`records.anchor_row` writes `str(anchor.anchor_id)`), exactly as it is for an authorship operation
identity.

### Conventions

A stored locator is a well-formed record even when no resolver currently supports it: a symbol locator remains
readable after the symbol moves, and losing resolvability never erases the claim.

### Invariants And Boundaries

- The blob identity is a Git object identity, **not a copy of the bytes** — there is no second content store here.
- Path shape is checked at the vocabulary boundary; resolution against a real filesystem belongs to the filesystem
  boundary, so an absolute, drive, UNC, backslash or parent-escaping path never reaches a stored record.
- **A draft carries no provenance.** `SourceAnchorDraft` deliberately has no `provenance` field, so the
  admitted application attaches the envelope (`admitted_anchor_request`) and
  `memory/knowledge/anchors.source_anchor_from_draft` is the single construction point for a stored anchor.
**The pathspec half of the path rule is shared, not restated.** `require_plain_git_path` is the one place a
leading-`:` spelling is refused; this model and `PathSeed` both call it, so a spelling the write path refuses
cannot then be presented as a seed that is answered with an absence. The glob characters `*`, `?` and `[` are
admitted on purpose — `ls-tree` addresses them literally — so a legitimate anchor containing one is authorable.

- **An identity is a parsed value, not a formatted string.** A `pattern`-constrained string declaration on a
  `UUID` field is unconstructible rather than merely lax, so a new identifier field must choose one of the
  two shapes deliberately — the L1 defect this file repaired.
- `SourceLocator` is declared *shared* with the selective read/diff contributor (KS-R07/KS-R08): the union is
  designed so that consumer can discriminate on `kind` without a second locator vocabulary. **The read half now
  exists** — `memory/knowledge/read_anchors.py` observes a stored locator through one accessor and reports a
  symbol locator as `unsupported_locator` rather than guessing — and the diff half (KS-R08) does not exist yet.

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
| The single v1 source identity and the alias a caller may name. | `GitBlobIdentity`; `SourceIdentity` | mcp/src/agents_remember/models/knowledge/source.py:29-36 |
| The three locators and the discriminated union over them. | `FileLocator`; `LineRangeLocator`; `SymbolLocator`; `SourceLocator` | mcp/src/agents_remember/models/knowledge/source.py:38-43; mcp/src/agents_remember/models/knowledge/source.py:44-58; mcp/src/agents_remember/models/knowledge/source.py:59-79; mcp/src/agents_remember/models/knowledge/source.py:84-87 |
| The draft/stored split, the repository-relative POSIX path rule, and the repaired `UUID` identifier field. | `SourceAnchorDraft`; `SourceAnchor`; `_require_confined_relative_posix_path` | mcp/src/agents_remember/models/knowledge/source.py:82-127; mcp/src/agents_remember/models/knowledge/source.py:130-133 |
| **The Git-pathspec half of the path rule, delegated to the one shared validator so the write path and the seed path cannot disagree.** | `require_plain_git_path` | mcp/src/agents_remember/models/knowledge/base.py:59-92 |
| **The node that measures a pathspec-magic spelling being refused at this boundary and never answered as an absence.** | "test_a_pathspec_magic_spelling_is_refused_by_the_typed_path_and_never_answered_as_absence" | mcp/tests/test_knowledge_read_paths.py:178-255 |
| The stored `source_anchor` table, its immutability trigger and its canonical column order. | `source_anchor`; `source_anchor_no_rewrite` | mcp/src/agents_remember/memory/knowledge/schema.py:267-279; mcp/src/agents_remember/memory/knowledge/schema.py:385-389 |
| The codec that derives the canonical identity text and decodes an anchor row through the discriminated union. | `anchor_row`; `anchor_row_digest`; `decode_anchor_row` | mcp/src/agents_remember/memory/knowledge/records.py:226-236; mcp/src/agents_remember/memory/knowledge/records.py:366-381; mcp/src/agents_remember/memory/knowledge/records.py:237-246 |
| The single construction point that attaches provenance to a draft. | `source_anchor_from_draft` | mcp/src/agents_remember/memory/knowledge/anchors.py:82-96 |
| The later requirement packets this vocabulary is declared shared with: requirement packets `KS-R07` and `KS-R08`, which live in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address them. | — | — |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T00:56:30+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): verified the 1 enforced citation row this card carried (citation_anchor_absent_from_range) against the source by hand-reading it — the locator-union row's `SourceLocator` cell already reads `mcp/src/agents_remember/models/knowledge/source.py:84-87`, which holds the declaration `SourceLocator = Annotated[FileLocator | LineRangeLocator | SymbolLocator, ...]` at line 84, so the earlier mechanical projection was correct and needed no further edit; the claim's wording, all four anchors and its other three ranges (`:38-43` `FileLocator`, `:44-58` `LineRangeLocator`, `:59-79` `SymbolLocator`) are unchanged, and no verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 1 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `SourceLocator`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 1 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `source.py.md:100` (`FileLocator`, `LineRangeLocator`, `SymbolLocator`, `SourceLocator`).
- 2026-09-17T06:49:47+00:00: Generated citation repair: `source_anchor_from_draft` repointed to mcp/src/agents_remember/memory/knowledge/anchors.py:82-96. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): recorded that **the write path's path rule now delegates its Git-pathspec half to the one shared `require_plain_git_path`**, so a stored anchor can no longer carry a spelling Git would read as pathspec magic (`:(exclude)`, `:!`, `:(top)`, `:/`) — a spelling that would otherwise be reported later as an absent path the tree was never asked about. The card states the corrected predicate explicitly: **the glob characters `*`, `?` and `[` are admitted**, because `ls-tree` addresses them literally; refusing them (this leaf's round-1 predicate) made a legitimate anchor un-authorable and reported a real file as `path_absent`. It also records that the read half of the KS-R07/KS-R08-shared locator union now exists in `memory/knowledge/read_anchors.py`, which reports a symbol locator as `unsupported_locator` rather than guessing. Citation ranges re-derived against the working tree. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): **superseded the L1 account of the anchor's identity field and type shape.** The earlier card described `SourceAnchor` as one model carrying a `UUID` `anchor_id` plus the `Authorship` envelope, and cited the anchor range at `82-115`. That account was wrong in the load-bearing respect: the field was declared `anchor_id: UUID = Field(pattern=UUID_PATTERN)`, and Pydantic refuses a string `pattern` constraint on a UUID schema, so **every** anchor construction raised `TypeError: Unable to apply constraint 'pattern' … for schema of type 'uuid'` — the class was unconstructible and no L1 test constructed one. The card now records the repair (`anchor_id: UUID`, canonical text derived at the storage boundary) and the draft/stored split (`SourceAnchorDraft` without provenance, `SourceAnchor(SourceAnchorDraft)` adding it), and re-cites the anchor range, the locator ranges and the codec rows against the corrected source. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new shared source vocabulary. It records that the locator union is declared shared with a read/diff consumer that does not exist yet, and that the blob identity is a Git object identity rather than a byte copy. Verification metadata remains empty until closeout stamps the code commit.
