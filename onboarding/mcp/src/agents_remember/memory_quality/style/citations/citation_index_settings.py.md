# mcp/src/agents_remember/memory_quality/style/citations/citation_index_settings.py

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

## Evidence

### Repo-Internal References

- The one reader for both settings blocks, and the frozen value it returns. [1]
- The two relative keys and the settings file both blocks are read from. [2]
- Either key is accepted at the `onboarding` level or at the document root. [3]
- The accepted cap-override keys and the unknown-key refusal that lists them. [4]
- A cap that is not a positive integer is refused with the key and the offending value. [5]
- The non-string-list refusal for `exclude.paths`. [6]
- The cap defaults this block overrides. [7]
- The same `pathRules.exclude` matcher every other reader uses. [8]
- The register that consumes these excludes. [9]

### Cross-Repo References

No sibling-repository contract defines these values.

No meaningful cross-repo references found.
