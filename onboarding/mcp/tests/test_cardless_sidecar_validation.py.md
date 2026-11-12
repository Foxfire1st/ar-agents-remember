# mcp/tests/test_cardless_sidecar_validation.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Check the validator's entries-only sidecar rule: a newly authored sidecar that holds only realization or proof entries needs no Markdown card, a reference-bearing sidecar still refuses without one, and cardless entries keep the identity, link, anchor and history checks.

## Code Commentary

The base fixture supplies a layout and one invariant without a Markdown card. `test_a_new_entry_sidecar_without_references_needs_no_markdown` runs `require_valid_commit` over two entry-sidecar fixtures and asserts a clean result with no `.md` file. `test_references_still_require_their_markdown_card` adds a reference to the entry sidecar and asserts `R22.3-markers` and `R22.3-sidecar-without-markdown` refuse; adding the card's prose accepts the tree. The parametrized fault cases keep `R22.2-identity`, `R22.1-shape`, `R22.3-record-links`, `R22.6-locator`, `R22.6-content` and `R22.6-anchor-path` refusing for cardless entries. A closed history file stays frozen under `R22.7-history-frozen`, and a malformed history field still refuses under `R22.1-shape`.

## Evidence

- A new entries-only sidecar passes without a Markdown card. [1]
- References without their card refuse under the marker and sidecar rules. [2]
- Cardless entries keep identity, link, locator, content and anchor-path checks. [3]
- Closed history freezing and shape checks remain. [4]
