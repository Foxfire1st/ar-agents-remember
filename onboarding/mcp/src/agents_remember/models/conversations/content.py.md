# mcp/src/agents_remember/models/conversations/content.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/models/conversations/content.py`     |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-29T17:23+02:00                                       |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`                   |
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/content.py` (moved by 260731-EFA-L9 from
`serving/conversation/_models_blocks.py`) owns the typed content blocks, choices, correlation,
sub-agent reference, and conversation-item grammar of the wire contract.

## Code Commentary

### Logic

The typed block family starts at `MarkdownBlock` (cit:(["class MarkdownBlock"], mcp/src/agents_remember/models/conversations/content.py:25-25)) and includes text,
thinking, code, tool-input/output, diff, image-reference, file-reference, and vendor blocks;
`ConversationCorrelation` (cit:(["class ConversationCorrelation"], mcp/src/agents_remember/models/conversations/content.py:127-127)) carries the correlation product;
`ConversationAgentRef` (cit:(["class ConversationAgentRef"], mcp/src/agents_remember/models/conversations/content.py:139-139)) is the evidence-bound sub-agent
reference; `ConversationItem` (cit:(["class ConversationItem"], mcp/src/agents_remember/models/conversations/content.py:160-160)) is the item root with stable ids,
monotonic revisions/ordinals, typed blocks, provenance, and the additive per-item `agent`.

### Invariants And Boundaries

- Sub-agent identity is never fabricated: unresolved identity renders as `agent <short-id>`.
- Unknown-vendor blocks preserve raw input without guessing semantics.

### Todos

No known follow-up.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


- 2026-08-29T17:23+02:00 — No content impact: reviewed the Python 3.13 type-alias syntax migration for `ConversationContentBlock` and confirmed that the discriminated content grammar remains as documented. Verification remains closeout-owned.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: preserved the L7 split card and rewrote it for
  the `models/conversations/content.py` home; symbol surface and grammar knowledge retained.
  Verification metadata pinned until closeout stamps the L9 code commit.
