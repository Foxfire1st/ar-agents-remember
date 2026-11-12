# dashboard/scripts/check-diff-coverage.mjs

## Governing Overview

[dashboard/scripts overview](overview.md)

## Purpose

Reports diagnostic changed-line dashboard coverage from the existing v8 artifact. Changed executable statement lines contribute to the denominator; positive execution contributes to the numerator. Missing lines remain visible, but no mandatory percentage or 90% floor can fail delivery. The CLI retains its Dagger admission and missing/malformed artifact failures.

## Code Commentary

### Logic

The pure helpers separate the accounting from the runner:
`executableStatementLines` spans every statement range in `statementMap`;
`coveredStatementLines` spans only ranges with a positive execution count;
`measureDiffCoverage` normalizes `dashboard/` keys, drops test/dev/types files,
and tallies `{covered, total, missing}` per changed line that carries an
executable statement (round-8 ruling OPTION 1). `resolveBase` mirrors the Python
resolver order — `AR_GATE_DIFF_BASE` → `GITHUB_BASE_REF` (`origin/<ref>` then
`<ref>`) → `@{upstream}` → `origin/HEAD` → `main` → empty tree (F9 parity) — and
`main()` first invokes the canonical Dagger-environment validator, then runs the
diff with a 256 MiB pipe buffer so series-fork diffs cannot ENOBUFS. The guard is
inside `main`, not module import: Vitest can import and exercise the pure scoring
helpers directly, while invoking the changed-lines CLI remains Dagger-only.

### Conventions

Node ESM, pure exported helpers, `#!/usr/bin/env node` runner; read-only.

### Invariants And Boundaries

Only `src/` production lines count; tests, `src/test`, `src/dev`, `src/types` are
excluded. Files without a v8 entry contribute nothing. The script never modifies
coverage or git state. Direct targeted Vitest may import the pure helpers for
diagnostic unit tests, but direct CLI execution cannot score or publish changed-lines
evidence outside a matching nonce-attested Dagger run. There is no bypass, shadow
configuration, fallback executor, or compatibility reader.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution evidence.

- Executable statement-line accounting [1]
- Covered statement ranges [2]
- Production filtering and changed-line tally [3]
- Dagger admission and comparison-base selection [4]
- Required coverage artifact and diagnostic result without a floor [5]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
