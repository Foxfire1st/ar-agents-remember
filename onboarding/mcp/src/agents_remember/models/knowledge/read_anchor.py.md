# mcp/src/agents_remember/models/knowledge/read_anchor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/read_anchor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T16:42:25+02:00 |
| lastVerifiedCommitHash | `9b2f775f1ab0fca5f82b4f661785dd8216d4a8b3` |
| lastVerifiedCommitDate | 2026-09-28T17:43:09+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The observation one recorded source anchor earns against a requested code tree, as a value
vocabulary.** It declares the closed set of seven resolution states an observation can reach
(`AnchorResolutionState`, mirrored as the runtime tuple `ANCHOR_RESOLUTIONS`) and the observation value
`AnchorResolution`, including the structured line ranges an exact recorded blob supports. It is the anchor
half of the read vocabulary: `models/knowledge/read.py` imports and re-exports every name here, so callers
keep importing from `read.py`. The resolver that produces the value is
`memory/knowledge/read_anchors.py`; this module holds no resolution, no Git call and no SQL.

## Code Commentary

### Logic

**The recorded identity stays on the observation whatever the outcome.** `AnchorResolution` carries the
anchor id, path, recorded source identity, the observed identity when one was seen, the anchor's own
structured `locator` (`SourceLocator`: `file`, `line_range` or `symbol`), the `resolution` state and a
diagnostic `detail` sentence. An anchor whose bytes differ, whose path is gone or whose locator cannot be
resolved is reported as that observation and never promoted to a current realization.

**`resolved_ranges` is the region, stated as values rather than prose.** It holds the one-based inclusive
`LineRangeLocator`s the recorded locator addresses in the recorded blob: the recorded range of a
`line_range` locator, or every extent the shipped extractor found defining a `symbol` locator's name. A
`file` locator addresses the whole blob and carries none. It defaults to `()`, so every observation that
is not an exact-blob region carries an empty tuple, and it travels on every read item that carries an
anchor — the knowledge read, the diff and the family roster alike — as an additive field.

**The one validator is the region rule.** `_require_ranges_only_on_the_recorded_bytes` refuses any
non-empty `resolved_ranges` beside a resolution other than `exact_recorded_blob`, because a range is a
statement about bytes this observation actually holds; beside a mismatch or an absence it would place the
recorded claim on bytes the read did not find at the path. The converse is **not** enforced: an
`exact_recorded_blob` observation may carry no range (a `file` locator, or a recorded line range the blob
does not reach), which is why a consumer reads the region from `resolved_ranges` and never infers it from
the resolution.

### Conventions

- Bounds come from `models/knowledge/base.py` (`LABEL_MAX_LENGTH`, `PATH_MAX_LENGTH`, `PROSE_MAX_LENGTH`,
  `UUID_PATTERN`); the locator types come from `models/knowledge/source.py`.
- The `Literal` and its tuple are declared side by side and must stay equal; the anchor vocabulary has
  exactly the owner's seven members.
- `__all__` publishes the three names; `read.py` keeps all three in its own `__all__`.

### Invariants And Boundaries

- **No range beside bytes the read did not find.** The validator is the structural guarantee, so no
  producer can publish a region on a mismatched, absent or unavailable anchor.
- **No member was added to the resolution vocabulary.** A recorded range past the blob's end is an
  `exact_recorded_blob` observation with no range and a `detail` saying why, not a new state.
- **Boundary.** Values only. The resolver, the pager and every consumer decide; this module declares.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The module is small and self-describing; the rows below name the declarations and the two places that
give them meaning — the re-export that keeps existing imports working and the resolver that fills the
ranges.

| Finding | Anchor | Source |
| --- | --- | --- |
| The published surface of the anchor-observation vocabulary. | `__all__` | mcp/src/agents_remember/models/knowledge/read_anchor.py:25-25 |
| **The owner's seven resolution states, as a type and as a runtime tuple.** | `AnchorResolutionState`; `ANCHOR_RESOLUTIONS` | mcp/src/agents_remember/models/knowledge/read_anchor.py:27-45 |
| **One recorded anchor observed against the requested snapshot, carrying its recorded identity whatever the outcome and its structured locator.** | `AnchorResolution` | mcp/src/agents_remember/models/knowledge/read_anchor.py:48-78 |
| **The structured region: the recorded line range or every defining extent, only on an exact recorded blob; none for a file locator.** | `resolved_ranges` | mcp/src/agents_remember/models/knowledge/read_anchor.py:64-69 |
| **The validator refusing ranges beside any resolution other than the exact recorded blob.** | `_require_ranges_only_on_the_recorded_bytes` | mcp/src/agents_remember/models/knowledge/read_anchor.py:71-78 |
| The re-export that keeps every existing `read.py` import of these names working. | `AnchorResolution` | mcp/src/agents_remember/models/knowledge/read.py:47-51 |
| The read item field that carries the observation onto every realization-claim item. | `anchor` | mcp/src/agents_remember/models/knowledge/read.py:329-367 |
| The resolver that fills `resolved_ranges` for symbol and line-range locators on the exact recorded blob. | `_observed_line_range`; `_observed_symbol` | mcp/src/agents_remember/memory/knowledge/read_anchors.py:203-214; mcp/src/agents_remember/memory/knowledge/read_anchors.py:227-300; mcp/src/agents_remember/memory/knowledge/read_anchors.py:303-351 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-28T16:42:25+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): created this one-to-one card for the anchor-observation vocabulary, extracted verbatim from `models/knowledge/read.py` (which re-exports every name) and extended with the additive structured `resolved_ranges` field and its one validator. The module is untracked at the base commit, so `lastVerifiedCommitHash` names the leaf base and the verified basis is the working-tree delta on top of it; the closeout records the real commit.
