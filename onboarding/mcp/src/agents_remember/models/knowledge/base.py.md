# mcp/src/agents_remember/models/knowledge/base.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/base.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T22:40+02:00 |
| lastVerifiedCommitHash |  `60e0820e6cb3b1d160518b9f8c7ac6241323a281`|
| lastVerifiedCommitDate |  2026-09-15T22:46:24+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[models route overview](../../../overview.md)

## Purpose

The frozen base class and the shared identifier/length validators every persisted knowledge value inherits:
canonical UUID spelling, the SHA-256 and Git-object patterns, the prose/label/reference/path length ceilings,
the two authored origin states and the `KnowledgeState` union.

## Code Commentary

### Logic

`KnowledgeModel` is a Pydantic `BaseModel` with `ConfigDict(extra="forbid", frozen=True)`. `extra="forbid"`
makes an undeclared field a refusal rather than silently dropped input; `frozen=True` makes the process-local
value immutable.

Module constants: `UUID_PATTERN` (lowercase hyphenated UUID text), `SHA256_PATTERN` (`^[0-9a-f]{64}$`),
`GIT_OBJECT_PATTERN` (40- or 64-hex Git object identity), `PROSE_MAX_LENGTH` 20000, `LABEL_MAX_LENGTH` 512,
`REFERENCE_MAX_LENGTH` 1024, `PATH_MAX_LENGTH` 4096, and `PROPOSED_STATE`/`ACCEPTED_STATE` with the
`KnowledgeState` literal union that both name.

`normalized_uuid` accepts a `UUID` instance or UUID text and returns the canonical stored spelling. It strips
and lowercases, parses, and then compares `str(parsed)` against the canonical form, raising `ValueError` with the
non-canonical input when they differ.

### Conventions

Two spellings of one identity never coexist: an identifier is validated into the canonical form at the model
boundary rather than normalized at the storage boundary. Length ceilings are generous for prose and far below any
SQLite limit; a legitimate value never approaches them.

### Invariants And Boundaries

- `frozen=True` is a property of the **value**, not of the row. Refusing an update to a stored revision is a
  storage rule enforced by schema triggers and the operation's preconditions — never by model immutability.
- A caller that supplies an identity supplies the identity that will be stored: non-canonical input is rejected,
  never quietly rewritten.
- `PROPOSED_STATE`/`ACCEPTED_STATE` live here because they decide something, so consumers import them rather than
  re-declaring their own literals.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The frozen, extra-forbidding base every knowledge model inherits. | `KnowledgeModel` | mcp/src/agents_remember/models/knowledge/base.py:34-37 |
| The canonical-spelling identifier rule and its refusal of non-canonical input. | `normalized_uuid` | mcp/src/agents_remember/models/knowledge/base.py:40-54 |
| The declared length ceilings and identifier patterns used by every sibling model. | `PROSE_MAX_LENGTH`; `LABEL_MAX_LENGTH`; `UUID_PATTERN`; `SHA256_PATTERN`; `GIT_OBJECT_PATTERN` | mcp/src/agents_remember/models/knowledge/base.py:18-27 |
| The two authored origin states are declared once here. | `PROPOSED_STATE`; `ACCEPTED_STATE` | mcp/src/agents_remember/models/knowledge/base.py:29-31 |
| The revision aggregate validates its own predecessor set against the identity pattern. | `InvariantRevision` | mcp/src/agents_remember/models/knowledge/invariant.py:56-117 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new frozen model base. It records that value immutability is distinct from row immutability and that identity spelling is validated rather than normalized. Verification metadata remains empty until closeout stamps the code commit.
