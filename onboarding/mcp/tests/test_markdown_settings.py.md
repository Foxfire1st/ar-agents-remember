# test_markdown_settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_markdown_settings.py`      |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f`                         |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_markdown_settings.py` exercises `parse_settings_block` with populated
`onboarding:` and `crossRepo:` markdown bodies, proving how the settings parser
resolves storage mode, path rules, and cross-repo allow entries from realistic
content rather than empty input.

## Code Commentary

### Logic

The tests insert the MCP `src` tree onto `sys.path` and import
`parse_settings_block`, then call it with hand-written YAML-like blocks and a
`topology` argument (`"internal"` or `"external"`), asserting on the returned
`(storage, cross_repo, saw_settings)` triple.

Storage cases confirm that a full `storage:` block reports both `mode` and
`default`; that a bare `mode:` (with a value) propagates into `default`; that an
explicit `default:` after `mode:` overrides only the default; that `layout:` is
accepted as an alias for `mode:`; and that a valueless `mode:` keeps the
topology-derived default (`repo-sidecar` for internal, `memory-repo` for
external) instead of collapsing to a literal. They also check that a block with
only `pathRules:` still yields a `StorageSettings` whose mode reflects the
topology default, that an empty block reports no settings and no storage, and
that comments and blank lines are ignored.

Path-rule cases cover global rules (collecting include/exclude paths and
fileTypes, defaulting includes to `["*"]` when absent), scoped rules under
`pathRules:` keyed by `path:` or `repo:` with nested `include:`/`exclude:`
eligibility sections, and storage-nested rules that use direct
`includes:`/`excludes:` keys plus a per-rule `storage:` destination override.

Cross-repo cases assert that a legacy bare-string allow entry is recorded as
`state == "excluded"` with an error containing "expectedBranch is required"
(v2 requires `expectedBranch`), that an inline list records each repo as
excluded, and that an empty allow list yields no entries and no errors. A
combined test feeds storage, path rules, and cross-repo together and checks all
three result facets at once.

### Invariants And Boundaries

These tests pin the parser's public contract: topology must drive the default
storage mode, a valueless `mode:` must never override that default, and
legacy string cross-repo entries must be surfaced as excluded errors rather
than silently accepted. They assert against the returned dataclasses and rule
dicts only; they do not reach into parser internals or reconstruct the markdown
emission side.

### Conventions

Each block is built as an explicit newline-joined string literal that mirrors
the indentation the parser expects (2/4/6/8/10 spaces for nested sections).
Assertions narrow the optional `storage` with `assert storage is not None`
before reading attributes. Tests are grouped by concern into
`MarkdownSettingsStorageTests`, `MarkdownSettingsPathRulesTests`,
`MarkdownSettingsCrossRepoTests`, and `MarkdownSettingsCombinedTests`, and the
module runs under `unittest.main()`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The parser under test exposes `parse_settings_block`. | [markdown_settings.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/markdown_settings.py) |
| Returned `StorageSettings`, `StorageRule`, and `CrossRepoSettings` shapes are defined here. | [models.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/models.py) |
| Topology-derived default modes come from `default_storage_mode`. | [paths.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/paths.py) |
| The legacy "expectedBranch is required" cross-repo error originates here. | [markdown_cross_repo.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/markdown_cross_repo.py) |

## Update History

- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
