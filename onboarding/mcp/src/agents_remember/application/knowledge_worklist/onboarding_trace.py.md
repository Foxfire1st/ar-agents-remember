# mcp/src/agents_remember/application/knowledge_worklist/onboarding_trace.py

## Governing Overview

[Nearest governing overview](../overview.md)

## Purpose

The worklist's `onboarding_trace` item kind: its registration, the two memory sides the onboarding gate
compares, the storage settings it reads, and the merge of its items into the worklist document.

## Code Commentary

- **Registration.** `ONBOARDING_TRACE_KIND` registers the kind with the subject `onboarding:<path>` for a
  file card and `onboarding:<route>/overview` for a route overview, the facts `sources`, `markdown`,
  `sidecar` and `countedChange`, and its satisfying rule: a counted change of the card or overview between
  K_B and K_C, or the leaf's row with that subject and disposition `no_impact`.
- **Sides.** `onboarding_trace_sides(request)` reads K_C from a directory or a Git tree and K_B from its
  commit. It returns `None` when neither side is converted. A converted K_B with an unconverted K_C, and a
  K_C without a pinned conversion version, are `incomplete` sides. An unconverted K_B is replaced by its
  conversion: read from `request.held_base_tree` with `knowledge_tree_from_git` when the caller holds the
  converted tree, and otherwise produced by `converted_base_files` through the converted-base cache. Only
  onboarding files, history files and the layout marker of each side are passed on.
- **Settings.** `trace_context(contract)` returns the storage settings the gate applies. The memory
  worktree's own `system/settings.md` is probed with `observed_exists`; when it is a file, it is parsed with
  `parse_coordination_settings`. Otherwise the contract's coordination context is resolved
  (`contract_context`); when that fails with an `AgentsRememberError`, the default storage settings are
  used, under which every changed file is gated. The function records nothing itself: the probe, the
  settings parsers and the resolver record their own absent files, consumed bytes and path selections, so
  inside a recording block the rows are exactly what this call looked at. A file it never opened has no
  row.
- **One list.** `worklist_onboarding(document, contract, request)` leaves a document that is not `complete`
  as it is, computes the gate over the worklist's own changed paths and merges the result with
  `with_onboarding_items`. A side that cannot be read gives an `incomplete` worklist naming `K_B`; a
  history file the gate cannot read gives one naming `K_C`. The merged items are sorted with the others
  by kind and subject, the digest covers them, and rows about files the leaf did not change are listed
  under `onboardingTrace.unnecessaryRows`.

## Evidence

- The registered kind, its subjects, facts and satisfying rule. [12]
- The request, with the held converted base tree. [13]
- The sides: not converted, the two incomplete cases, and the held tree or the cache for an unconverted K_B. [14]
- The settings: the memory worktree's own, the resolved context, or the default. [15]
- The merge into one sorted list with its digest. [16]
- The gate over the worklist's own changed paths. [17]
- The call records the absent memory settings and the contract it read, and not the coordination settings it never opened. [18]
- Settings that are changed and restored while they are parsed are recorded with the bytes parsed. [19]
