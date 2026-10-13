# mcp/src/agents_remember/application/read_file_cards.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Compute governing-card record counts and action-needed names using the existing knowledge-state selection, and resolve those names to actual card headings.

## Code Commentary

The record-selection and currentness owner remains the family-complete leaf machinery. This module projects its results into counts and action-needed invariant IDs, kinds, states and headings. An incomplete index qualifies surviving counts with skipped-file reasons; a failed selection or measurement is reported rather than presented as a clean empty result.

Converted evidence marks resolve through the card sidecar. A content-exact anchor match outranks a same-blob match, which outranks a path match. Ties prefer the record’s earliest differing anchor. If no section matches, the actual title is used with title_fallback; the module invents no section heading.

READ_AR_FILES_MAX_PATHS is the naming request bound. CODE_STATE_HEAD records this implementation’s HEAD-tree measurement; working-tree currentness is a separate reader-owner change, not implied by physical source reads.

## Evidence

- Card selection preserves computed states and partial-index qualifications. [1]
- Heading resolution reports an actual title fallback when no section scores. [2]
- Recorded content, blob and path identity determine section priority. [3]
