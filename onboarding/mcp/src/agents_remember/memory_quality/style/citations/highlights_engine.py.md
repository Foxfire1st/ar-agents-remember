# mcp/src/agents_remember/memory_quality/style/citations/highlights_engine.py

## Governing Overview

[memory_quality/ overview](../../overview.md)

## Purpose

Implements the pure, language-agnostic tree-sitter syntax highlighting engine: `; inherits:` query bundle composition, `\n` newline normalization on a copy, deterministic `O(M log M)` capture precedence sweeping, and `O(N)` UTF-8 byte-to-UTF-16 code-unit offset conversion.

## Code Commentary

Declares `HIGHLIGHT_VERSION = "ar-highlights/1"` independently of `EXTRACTOR_VERSION` so presentation-only query changes never affect knowledge anchor identity. `classify_capture` walks dot-separated tree-sitter capture prefixes against `_CAPTURE_MAP`: `@none` has absolute suppressor rank `100`, `@string.special.key` has rank `80` (`kind=None`, keeping JSON keys unstyled over enclosing `@string`), styled families occupy ranks `30`–`70`, and unstyled captures such as `@variable` or `@property` return `(None, 0)` and are dropped before sweeping.

`parse_inherits_directive` and `compose_highlight_queries` expand leading `; inherits: a, b` comments from base to derived with cycle protection (`visiting` set) and text deduplication. `normalize_newlines` normalizes `\r\n` and lone `\r` to `\n` on a copy without mutating caller text. `_collect_capture_spans` and `_sweep_byte_spans` execute a deterministic sweep-line with max-priority tuple `(is_none, -(end - start), rank, query_index, pattern_index)` — so `@none` wins first, narrower child spans split parent spans cleanly, higher-rank captures break ties, and later queries/patterns resolve equal-span ties — then `_append_merged` merges adjacent same-kind spans.

`_pack_utf16_payload` enforces `HIGHLIGHT_MAX_SPANS` (returning `None` above 20,000 spans or when empty), takes an ASCII fast path when `normalized.isascii()` and otherwise builds an `O(N)` `array("I")` byte-to-UTF-16 lookup table handling 2/3-byte BMP and 4-byte astral (2 UTF-16 code units) characters, and computes a 16-hex SHA-256 `digest` bound to `HIGHLIGHT_VERSION`, `language_id`, `version_tag`, `kinds`, and `spans`. `compute_highlights` enforces `HIGHLIGHT_MAX_BYTES` and runs parse -> collect -> sweep -> pack.

## Relationships

Called exclusively by `highlights_service.py` after out-of-process smoke compilation; emits `SyntaxHighlights` from `models/highlights.py`. Holds no hardcoded language lists or suffix tables. Verified by `mcp/tests/test_unified_tree_sitter_highlights.py`.

## Evidence

- Defines `HIGHLIGHT_VERSION`, capture-precedence table `_CAPTURE_MAP`, and prefix-walking `classify_capture`. [1]
- Parses `; inherits:` headers and expands composed bundles base-first with cycle protection. [2]
- Performs deterministic `O(M log M)` precedence sweep with `@none` suppression and adjacent same-kind merging. [3]
- Maps UTF-8 byte offsets to UTF-16 code units on a `\n`-normalized copy, enforces byte/span caps, and packs `SyntaxHighlights`. [4]
