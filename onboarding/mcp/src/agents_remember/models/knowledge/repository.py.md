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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The namespace model and its nonblank authority-home rule. [1]
- The `repository` table this identity keys, and its no-update/no-delete triggers. [2]
- Rebinding a populated store to another namespace or authority home is refused. [3]
- A request naming a foreign namespace refuses before any DML. [4]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
