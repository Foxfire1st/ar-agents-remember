# mcp/test_support/agents_remember_test_support/testing/capsule_audience_v13_fixtures.py

## Governing Overview

[overview](overview.md)

## Purpose

The module pins the current bytes of every lifecycle operation source and per-role compiled stage, and supplies the two exact inverses that carry those bytes back to the reviewed pins in `capsule_audience_fixtures.py`. `mcp/tests/test_role_capsule_audiences.py` is its consumer.

## Code Commentary

The audience test compares in three steps: the current bytes must equal the current pin; `inverse_v13_short_rules` replaces each admitted short-rule span with its earlier text and the result must equal the pre-short-rule pin; `inverse_v13_paths` then maps moved reference paths back to their earlier names and the result must equal the reviewed pin. Any other byte change fails one of the three comparisons.

All four pin tables are renewed together in the change that alters an operation source or a compiled stage, so a stale pin in any one of them fails. The short-rule inverse requires each current span to occur exactly once before replacing it. The path inverse replaces longest paths first and only the paths it lists. Raw operation-source spans come from `capsule_audience_v13_operation_inverse.py`; per-role stage spans are listed here.

## Evidence


- Current operation bytes are pinned. [1]

- The path inverse lists exact current-to-earlier reference paths. [2]
- Each admitted short-rule span must occur once and is replaced by its earlier text. [3]
- Only the pinned path substitutions are undone, longest first. [4]
