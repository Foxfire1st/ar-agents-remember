# mcp/src/agents_remember/worktrees/modules/args.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/args.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `4117c3d98eadb4265af6e55f3dd8f2552e8589a0`                         |
| lastVerifiedCommitDate | 2026-06-01T20:31:44+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Defines the typed cross-layer DTO that carries worktree operation inputs from
the MCP controllers and the worktree CLI into the worktree domain functions.
`WorktreeArgs` replaces the loosely typed `argparse.Namespace` that previously
flowed across those layers (F17), giving every layer a single explicit field set
to read and write.

## Code Commentary

`WorktreeArgs` is a `@dataclass(frozen=True)`. Every field carries a default, so
any operation can construct just the subset it needs without supplying the rest;
fields are grouped by concern (coordination/repository resolution, start inputs,
provider setup, lifecycle flags, and closeout/integrate commit messages). The
frozen dataclass means callers that need a variant produce a new instance rather
than mutating an existing one.

`from_namespace` builds an instance from an `argparse.Namespace`, falling back to
the field defaults. It iterates the dataclass `fields`, copies only attributes
the namespace actually defines (`hasattr` guard), and applies them onto a default
instance via `replace`. This tolerates argparse subparsers that only populate the
arguments they declare and tests that construct partial namespaces, so any field
the namespace omits keeps its dataclass default rather than raising.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider setup config is typed through the companion worktree models module. | [models.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/models.py) |
| Worktree CLI builds argparse namespaces that this DTO adapts via `from_namespace`. | [cli.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/cli.py) |

## Update History

- 2026-06-01T20:45+02:00 — `WorktreeArgs` gained `force` and `teardown_providers` for the abandon/cleanup teardown path.
- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
