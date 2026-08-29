# mcp/src/agents_remember/application/curator_coherence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/curator_coherence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T08:52+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[application overview](overview.md)

## Purpose

Owns the configured-contract application boundary for the single curator-coherence lifecycle API.
It admits one exact leaf enclosure and translates both configured-authority and coherence-domain
failures into the public typed refusal shape.

## Code Commentary

### Logic

`curator_coherence_tool` resolves the caller's exact `contract_path` through the shared configured
contract admission API, executes `curator_coherence_action` inside that admitted authority, and
returns its result unchanged. `_domain_refusal` preserves coherence status, detail, expected and
observed facts, and the legal next action. `_configured_refusal` projects the lower-level configured
contract family once rather than teaching the public tool every failure subtype.

### Conventions

The application layer owns failure-family translation. The MCP payload adapter and registration
remain thin, while the worktree closeout package owns the structured record and publication rules.

### Invariants And Boundaries

- `contract_path` resolves exactly one configured leaf; there is no official-checkout fallback.
- Domain failures return controlled tool responses instead of escaping as implementation errors.
- This layer does not author judgments, inspect Markdown, or select historical filenames.
- All actions use one API and one contract authority.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; this is a repository-owned lifecycle boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for the configured-contract translation. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One admitted contract executes the coherence action and translates the complete domain family. | `curator_coherence_tool`; `_domain_refusal`; `_configured_refusal` | mcp/src/agents_remember/application/curator_coherence.py:19-83 |
| Configured admission is the shared lower-level API rather than repeated exception lists. | `admit_configured_contract`; `execute_configured_contract_operation` | mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py:96-169; mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py:314-323 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

| Finding | Anchor | Source |
| --- | --- | --- |
| The operation remains inside the configured coordination and repository roots. | — | — |

## Update History

- 2026-08-29T08:52+02:00 — Created for MCAR-L02 A005's single configured curator-coherence API
  boundary. Verification remains closeout-owned.
