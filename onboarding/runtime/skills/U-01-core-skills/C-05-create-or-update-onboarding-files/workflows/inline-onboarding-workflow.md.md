# inline-onboarding-workflow.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/inline-onboarding-workflow.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-14T20:11+02:00                     |
| lastVerifiedCommitHash | `398184b757e336211e335569284f2cde309cd964` |
| lastVerifiedCommitDate | 2026-05-15T04:04:02+02:00|

## Purpose

This workflow defines the storage adapter for inline onboarding blocks. It keeps the semantic file-level onboarding model from the sidecar Markdown template, then adds source-comment placement, marker, digest, and fallback rules for files that can safely carry onboarding inline.

## Code Commentary

### Logic

The workflow starts from the canonical file-level onboarding content, chooses valid host-language comment delimiters, places the inline block at the highest safe point in the source file, preserves stable `@ar-onboarding` markers, recomputes a SHA-256 digest over the source body with the inline block removed, and falls back to sidecar onboarding when inline placement or parsing is unsafe.

### Conventions

Inline onboarding is an adapter layer, not a separate content model. It serializes the same semantic sections used by sidecar file-level onboarding and limits its own concerns to comment syntax, safe placement, digesting, marker stability, and fallback behavior.

### Invariants And Boundaries

Inline onboarding must not break runtime, parsing, build, or tooling behavior for the host source file. Missing markers or missing `sourceDigest` make inline onboarding unverified during drift detection, and unsupported text parsing falls back to sidecar onboarding rather than forcing a risky inline block.

### Todos

No current todo is recorded for this workflow.

### Docs References

No external domain documentation applies to this repository-local workflow file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This workflow is the inline-storage counterpart to the sidecar file-level onboarding workflow.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The workflow states that inline onboarding stores file-level onboarding inside the source file and keeps the semantic content from the file-level template. | L1-L5 | [inline-onboarding-workflow.md](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/inline-onboarding-workflow.md) |
| Inline workflow steps cover comment delimiter selection, safe placement, stable markers, digest recomputation, and sidecar fallback. | L11-L18 | [inline-onboarding-workflow.md](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/inline-onboarding-workflow.md) |
| Verification rules require timestamp and digest fields and classify missing markers or digest as missing verification. | L20-L25 | [inline-onboarding-workflow.md](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/inline-onboarding-workflow.md) |

## Cross-Repo References

No sibling repository evidence is needed for this workflow.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-14T20:11+02:00: Created file-level onboarding for the inline onboarding workflow while preparing direct closeout for the external-memory terminology alignment.
