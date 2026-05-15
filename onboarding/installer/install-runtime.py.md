# installer/install-runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `installer/install-runtime.py`             |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-15T01:55+02:00                     |
| lastVerifiedCommitHash | `398184b757e336211e335569284f2cde309cd964`         |
| lastVerifiedCommitDate | 2026-05-15T04:04:02+02:00|

## Purpose

`install-runtime.py` is the checkout entrypoint for installing package-owned runtime mechanics into a target `ar-coordination` root.

## Notes

The installer reconciles package-owned runtime directories by pruning stale files from installed `skills/` and `scripts/`, then copying the current runtime skill tree, runtime scripts, and four runtime `AGENTS.md` templates. It creates missing user-owned coordinator folders but does not run repo onboarding bootstrap, copy settings defaults, or overwrite live memory, task, note, worktree, temp, or settings content. `runtime/system/defaults/` remains checkout template material for initialization skills rather than installed coordinator state.

## Update History

- 2026-05-15T01:55+02:00: Created with pending verification metadata for the first runtime-layout closeout commit.
- 2026-05-15T03:06+02:00: Corrected installer ownership notes so system defaults remain source-side templates instead of installed runtime files.
