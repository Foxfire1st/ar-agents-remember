# mcp/src/agents_remember/memory_quality/style/citations/citation_index_settings.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/citation_index_settings.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T10:20+02:00 |
| lastVerifiedCommitHash | `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` |
| lastVerifiedCommitDate | 2026-09-17T10:09:37+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l14-ar` uncommitted source; base `0346da9c572e1eb913a8eb4130e9a9e9d37343c8` |
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Read the memory layer's own two citation-index settings blocks and hand them to the acquisition
as one immutable value. This is the module that makes the exclusion register and the index caps
**operator-configurable in the same file as `pathRules`**, instead of requiring a code edit.

## Code Commentary

### Logic

`read_citation_index_settings(memory_root)` reads `system/settings.json` under the memory root and
returns a frozen `CitationIndexSettings` carrying the excludes, the caps, and the settings path it
read them from.

Two blocks decide what the citation source index may read and how much of it:

| Key | Meaning |
| --- | --- |
| `onboarding.pathRules.exclude.paths` | the exclusion register the exclusion review agrees with the user **before** memory closeout and persists. It is the same key the storage resolver and the drift check already honour, read here through the same matcher, so one register means one thing across the quality surface. |
| `onboarding.citationIndex` | optional cap overrides. The module constants in `source_index_state` remain the defaults; this block exists so an operator can move a bound deliberately, instead of editing code. |

Both keys are accepted at the `onboarding` level **or** at the document root, matching the
existing JSON settings parser, which accepts `pathRules` in both places. The accepted override
keys are exactly `CAP_KEYS` — `maxFileBytes`, `maxSourceBytes`, `maxSourceFiles`, `hardStopBytes` —
and `read_citation_index_caps` refuses an unknown key by listing the accepted ones.

`configured` answers whether the settings supplied anything at all, which is how a caller tells
"the operator moved a bound" from "this memory layer has no register yet".

### Conventions

- A **missing** `system/settings.json` is the ordinary state of a fresh memory layer: it returns
  the defaults and means "no register yet", which is a legitimate answer.
- An **unreadable, non-JSON, or non-object** file is refused by name through `SourceIndexError`.
  Falling back to the defaults would silently index paths the user excluded, which is the failure
  mode the whole change exists to prevent.
- A malformed *value* is a typed refusal naming the key — never a silent fallback to the default,
  because a cap that silently ignores its configuration is the failure mode this change exists to
  prevent.
- The caps come back with `overridden` naming exactly the keys the settings supplied, so a report
  can say which bounds an operator moved.

### Invariants And Boundaries

- `pathRules.exclude` means the same thing here as it does in the storage resolver and the drift
  check; this module adds no second interpretation of a pattern.
- `hardStopBytes` must not sit below `maxSourceBytes` or `maxFileBytes`; both violations are
  refused by name with the route that fixes them (raise the hard stop, or lower the other key in
  the same block).
- Cap overrides are read **per acquisition**; nothing here caches, publishes or writes settings.
- The keys are mode-independent — no branch on the memory storage mode exists in this module.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one reader for both settings blocks, and the frozen value it returns. | `read_citation_index_settings`; `CitationIndexSettings` | mcp/src/agents_remember/memory_quality/style/citations/citation_index_settings.py:43-85 |
| The two relative keys and the settings file both blocks are read from. | `SETTINGS_RELATIVE_PATH`; `CITATION_INDEX_KEY`; `PATH_RULES_KEY`; `ONBOARDING_KEY` | mcp/src/agents_remember/memory_quality/style/citations/citation_index_settings.py:34-39 |
| Either key is accepted at the `onboarding` level or at the document root. | `read_path_rule_excludes` | mcp/src/agents_remember/memory_quality/style/citations/citation_index_settings.py:88-114 |
| The accepted cap-override keys and the unknown-key refusal that lists them. | `read_citation_index_caps`; `CAP_KEYS` | mcp/src/agents_remember/memory_quality/style/citations/citation_index_settings.py:117-163 |
| A cap that is not a positive integer is refused with the key and the offending value. | `_positive_integer` | mcp/src/agents_remember/memory_quality/style/citations/citation_index_settings.py:176-182 |
| The non-string-list refusal for `exclude.paths`. | `_string_list` | mcp/src/agents_remember/memory_quality/style/citations/citation_index_settings.py:166-173 |
| The cap defaults this block overrides. | `CitationIndexCaps` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:69-104 |
| The same `pathRules.exclude` matcher every other reader uses. | `matches_any` | mcp/src/agents_remember/kernel/coordination_context/storage.py:50-56 |
| The register that consumes these excludes. | `resolve_exclusion_register` | mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py:196-226 |

## Cross-Repo References

No sibling-repository contract defines these values.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T10:20+02:00 — 260915-CAPS-L14 curator: created this card for the module the leaf adds. Records the two settings blocks (`onboarding.pathRules.exclude.paths` and the optional `onboarding.citationIndex` cap overrides), that both keys are accepted at the `onboarding` level or the document root, the exact accepted override keys, and the refusal discipline — a missing file is "no register yet", while an unreadable, malformed or unknown-keyed value is refused by name rather than falling back to a default. States that the keys are mode-independent. Verification metadata is left at this leaf's synced base `0346da9c` with a `reviewedWorkingCandidate` row, because the candidate is deliberately uncommitted — the governed closeout stamps the real code commit and no hash or digest was invented here.
