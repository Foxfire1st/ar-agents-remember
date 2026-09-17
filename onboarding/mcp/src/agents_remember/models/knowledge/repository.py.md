# mcp/src/agents_remember/models/knowledge/repository.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/repository.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T22:40+02:00 |
| lastVerifiedCommitHash |  `4904e08f0668ed6d11a2c44d0118716bb82f735c`|
| lastVerifiedCommitDate |  2026-09-17T22:32:32+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[models route overview](../../../overview.md)

## Purpose

The repository-namespace identity that scopes every stored knowledge row: a stable stored identifier plus the
authority home it was authored under.

## Code Commentary

### Logic

`RepositoryIdentity` carries `repository_id` (validated against `UUID_PATTERN`) and `authority_home`
(`min_length=1`, `max_length=LABEL_MAX_LENGTH`). Its `authority_home` field validator strips the value and
refuses a blank result with `"authority_home must not be blank"`.

Every canonical table in `memory/knowledge/schema.py` keys on `repository_id`, and the store's bound namespace is
this model's `repository_id`; a request naming another namespace is refused as `unauthorized_scope` before any
DML.

### Conventions

The namespace is a **stored identifier**, not a filesystem root, branch name or repository display name. Those all
change while the knowledge they scope does not, and a namespace that moved with them would silently re-scope every
revision underneath it.

### Invariants And Boundaries

- `repository_id` is opaque UUID text; the readable repository name belongs in `authority_home`, which is
  provenance rather than identity.
- Rebinding a populated store to a different namespace or authority home is refused
  (`repository_rebind_refusal`), because the stored revisions are addressed within the namespace that authored
  them.
- The authority home is authored input; the store never derives it from the running checkout or the Git remote.

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
| The namespace model and its nonblank authority-home rule. | `RepositoryIdentity` | mcp/src/agents_remember/models/knowledge/repository.py:19-31 |
| The `repository` table this identity keys, and its no-update/no-delete triggers. | `repository`; `repository_no_update`; `repository_no_delete` | mcp/src/agents_remember/memory/knowledge/schema.py:118-123; mcp/src/agents_remember/memory/knowledge/schema.py:337-344 |
| Rebinding a populated store to another namespace or authority home is refused. | `repository_rebind_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:162-181 |
| A request naming a foreign namespace refuses before any DML. | `scope_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:80-101 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new repository-namespace identity. It records that the namespace is a stored identifier rather than a path, branch or display name. Verification metadata remains empty until closeout stamps the code commit.
