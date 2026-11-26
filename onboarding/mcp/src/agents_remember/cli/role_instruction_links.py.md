# mcp/src/agents_remember/cli/role_instruction_links.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Rewrites Markdown link destinations in launch instruction text either into absolute paths (default `compact_links=False`) or into compact logical `skill/<rel>` and `detail/<rel>` paths (opt-in `compact_links=True`), and compacts shipped `skill://` URIs outside code spans so Turn-1 prompts avoid expanded workstation roots and 64-hex hashes while keeping standalone callers and frozen detail files self-contained.

## Code Commentary

`relative_destinations` finds the destinations of inline links, images and reference definitions outside fenced, indented and inline code (`_all_link_destinations`). Absolute paths, `{{detail:...}}` placeholders and destinations with a URL scheme are left alone by `relative_destinations`. Code is masked without moving offsets (`_code_mask`, `_mask_inline_code`), so a found span indexes the original text.

`compact_skill_uri_links(text)` uses the same code-masked destination scanner to rewrite `SHIPPED_SKILL_URI_PREFIX` (`skill://agents-remember/skills/l-01-agent-lifecycles/`) URIs outside code into `skill/<quoted-rel>[?query][#fragment]` (preserving query and fragment via `_reattach_query_fragment`).

`bind_markdown_links(text, source, targets, *, compact_links=False, corpus_root=None, detail_targets=None)` resolves each relative destination against `source`'s folder (an empty path names `source` itself), percent-quotes the result, and preserves any query and fragment. Under default `compact_links=False` (used by standalone callers and for internal links inside written frozen detail files), mapped `targets` resolve to their frozen absolute paths and all other targets resolve to absolute corpus paths. Under opt-in `compact_links=True` (used for Turn-1 prompt carriers), `_format_bound_target` binds frozen detail targets (`detail_targets`) to `detail/<source>`, in-corpus targets (`target.is_relative_to(resolved_corpus)`) to `skill/<rel>`, out-of-corpus targets to absolute paths, and compacts `skill://` URIs via `compact_skill_uri_links`.

`require_no_unbound_links` raises `CapsuleDeliveryError` when text still holds a relative destination; it guards a baseline that has no source origins to bind it from.

## Evidence


- Relative destinations are found outside code; absolute, placeholder and scheme destinations are skipped. [1]

- Text without source origins may not keep a relative link. [3]
- Code spans and fences are masked without moving offsets. [4]

- `bind_markdown_links` and `_format_bound_target` preserve default absolute binding (`compact_links=False`) and under opt-in `compact_links=True` bind frozen details to `detail/<rel>`, in-corpus files to `skill/<rel>`, out-of-corpus targets to absolute paths, and shipped `skill://` URIs via `compact_skill_uri_links`. [2]
- `SHIPPED_SKILL_URI_PREFIX`, `_all_link_destinations`, and `compact_skill_uri_links` compact shipped `skill://` URIs outside fenced, indented, and inline code while preserving query and fragment. [5]
