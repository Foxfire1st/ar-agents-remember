# mcp/src/agents_remember/models/knowledge/read_anchor.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The observation one recorded source anchor earns against a requested code tree, as a value
vocabulary.** It declares the closed set of seven resolution states an observation can reach
(`AnchorResolutionState`, declared as a literal type) and the observation value
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

## Evidence

### Repo-Internal References

- `AnchorResolution` implements the retained boundary described above. [9]
