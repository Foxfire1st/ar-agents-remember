# mcp/test_support/agents_remember_test_support/testing/capsule_audience_v13_fixtures.py

## Governing Overview

[overview](overview.md)

## Purpose

The module retains historical pre-short-rule operation and stage hashes, plus exact short-rule and path inverse functions. The current audience test does not import this module.

## Code Commentary

When called, inverse_v13_short_rules restores its recorded tool-name, catalog-drop and short-rule spans; inverse_v13_paths applies its recorded path substitutions longest first.

The two historical hash tables retain recorded operation and stage hashes. The short-rule inverse requires each admitted short-rule span to occur exactly once and each tool-name or catalog-drop span at most once before replacing it, and replaces the catalog-drop intake markers wherever they stand. The path inverse replaces longest paths first and only the paths it lists. Raw operation-source spans come from `capsule_audience_v13_operation_inverse.py`; per-role stage spans are listed here.

## Evidence

- The path inverse lists exact current-to-earlier reference paths. [2]

- Each admitted short-rule span must occur once and each admitted tool-name or catalog-drop span at most once, and each is replaced by its earlier text. [3]

- Only the pinned path substitutions are undone, longest first. [4]

- Historical pre-short-rule operation and stage hashes remain recorded. [1]
