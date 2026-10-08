# mcp/src/agents_remember/models/knowledge/repository.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The repository-namespace identity that scopes every stored knowledge row: a stable stored identifier plus the
authority home it was authored under.

## Code Commentary

### Logic

`RepositoryIdentity` carries `repository_id` (validated against `UUID_PATTERN`) and `authority_home`
(`min_length=1`, `max_length=LABEL_MAX_LENGTH`). Its `authority_home` field validator strips the value and
refuses a blank result with `"authority_home must not be blank"`.

Every retained base schema table keys its rows on repository_id, and the opened index store queries its bound namespace. This model declares namespace identity; neither it nor the read-only store exposes repository rebinding or foreign-namespace DML.

### Conventions

The namespace is a **stored identifier**, not a filesystem root, branch name or repository display name. Those all
change while the knowledge they scope does not, and a namespace that moved with them would silently re-scope every
revision underneath it.

### Invariants And Boundaries

- `repository_id` is opaque UUID text; the readable repository name belongs in `authority_home`, which is
  provenance rather than identity.
- Historical canonical-database writes refused rebinding through repository_rebind_refusal. That factory and writer were retired by MIK-R26. The current value retains namespace and authority-home identity; it grants no rebinding operation.
- The authority home is authored input; the store never derives it from the running checkout or the Git remote.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The namespace model and its nonblank authority-home rule. [1]
- The `repository` table this identity keys, and its no-update/no-delete triggers. [2]

- The repository value declares namespace and authority home; the old rebinding writer is retired. [3]


- The index reader queries its bound namespace and opens a read-only connection. [4]


### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
