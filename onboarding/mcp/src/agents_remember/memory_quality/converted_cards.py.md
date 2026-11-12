# mcp/src/agents_remember/memory_quality/converted_cards.py

## Governing Overview

[memory_quality route overview](overview.md)

## Purpose

**A converted card's census identity: its kind and its source, read from the converted format (L37 fix round
P1b).** A legacy card names its kind and source in a `| Field | Value |` metadata table (`doc_type`, `path`,
`sourceRoute`). The conversion drops those rows (MIK-R24 rule 1): a converted card's kind and source are its place in
the tree, and its sidecar names the same source when the card has references (MIK-R21 rule 1). This module answers
in the legacy table's vocabulary, so the memory census and the curator candidates it feeds read both formats through
one shape.

## Code Commentary

### Logic

- `converted_card_metadata(card, onboarding, sidecar_text)` returns:
  - for an `overview.md`: `doc_type` `repo-overview` (the root route `.`) or `route-local-overview`, and
    `sourceRoute`, the route the sidecar declares or else the card's directory;
  - for `onboarding/entities.md`: `doc_type` `repo-entity-catalog`;
  - for any other card: `doc_type` `file-level-onboarding` and `path`, the source the sidecar declares or else the
    card's path without `.md`.
- `declared_sidecar_path(text, *, route)` returns the sidecar's `path` only when the text is JSON, is an object of
  the card's own kind (`ar-onboarding-route/v1` or `ar-onboarding-file/v1`) and holds a non-empty string `path`;
  an absent, unreadable or other-kind sidecar gives `None`.
- `card_sidecar_path(card)` is `<card without .md>.json`; `is_overview(card)` tests the file name.

### Conventions

- Callers: `memory_quality/memory_census._Tree._load_converted_metadata` and
  `application/memory_quality/census._governed_metadata`; `card_sidecar_path` and `is_overview` are also used by
  the card authoring and the fixer's document scope.

### Invariants And Boundaries

- **A card without references has no sidecar, and its place in the tree is then its identity.** The module never
  refuses: an unreadable sidecar falls back to the structural identity, and the knowledge validator refuses the
  sidecar by its own rule.
- The module reads text it is given and nothing else.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R21@v1` rule 1 and `MIK-R24@v1` rule 1, with the L37 decision of 2026-10-01T07:41:58 in `37_cutover-to-text-storage.json`; it lives outside the code and memory
repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: where a converted card's kind and source live. [1]
- A card's kind and source in the legacy table's keys. [2]
- The path a sidecar of the card's kind declares, or none. [3]
- The census loads converted cards' metadata through this module. [4]

### Cross-Repo References

No meaningful cross-repo references found: the module parses text.

No cross-repo boundary is crossed by this file.
