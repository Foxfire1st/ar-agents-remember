# mcp/src/agents_remember/kernel/coordination_context/markdown_global_rules.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`markdown_global_rules.py` owns global Markdown path-rule line handling for the
fallback settings parser.

## Code Commentary

### Logic

The module handles the legacy top-level `onboarding.pathRules.include/exclude`
shape, selecting paths or fileTypes lists and appending the final global
storage rule to the parser's settings object.

### Invariants And Boundaries

- The module only operates on the parser state passed by `markdown_settings.py`.
- JSON path-rule parsing remains in `json_settings.py`.
- Global Markdown path rules are appended only when the parser observed a
  global include/exclude section.

## Evidence

### Docs References

No external documentation is needed for this local fallback parser helper.

No relevant external documentation is needed.

### Repo-Internal References

- The Markdown parser delegates global path-rule branches to this module. [1]
- Storage evaluation consumes parsed include/exclude paths and file types. [2]

### Cross-Repo References

No cross-repository evidence is needed for local path-rule parsing.

No meaningful cross-repo references found.
