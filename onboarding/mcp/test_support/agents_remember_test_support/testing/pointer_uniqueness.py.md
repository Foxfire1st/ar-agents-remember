# mcp/test_support/agents_remember_test_support/testing/pointer_uniqueness.py

## Governing Overview

[overview](overview.md)

## Purpose

The module checks that one native first message points to each lifecycle-skill file once per action, admitting a repeat only for actions listed as distinct for that file and its source.

## Code Commentary

A pointer is any unfenced Markdown link resolving to a skill file (`{{detail:F}}`, served `skill://`, relative or same-file anchor), keyed by target file; links from one sentence or table row to one file count once. Its action comes from `manifest_step_derivation.action_of`, else the text before the link, a table row's first cell, or the text after a leading link. `duplicate_pointers` takes a first message's `(source, text)` units and reports the same action twice, an unlisted repeat, two wordings of one action from the exclusive groups, a listed action from an unlisted source, and a sentence linking one file twice unless listed in `MULTI_LINK_SENTENCES`. Its reader is `mcp/tests/test_l84_unique_detail_pointers.py`.

## Evidence

- Admitted repeats are listed per target file with the reason the actions differ. [1]
- Each listed action is admitted only from its named source files. [2]
- Pointers are collected once per sentence and target file, fences excluded. [3]
- A first message's duplicate, unlisted, cross-worded or foreign-source repeats are reported. [4]
