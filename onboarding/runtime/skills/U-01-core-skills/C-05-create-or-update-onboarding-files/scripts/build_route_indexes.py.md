# build_route_indexes.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember-md                                     |
| path                   | `runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/scripts/build_route_indexes.py` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-05-19T03:23+02:00                                 |
| lastVerifiedCommitHash | `5b26015bb3e9deec8113b1a69a12608bba82cc27`             |
| lastVerifiedCommitDate | 2026-05-19T03:27:34+02:00|

## Purpose

This script is the C-05 command-line wrapper for refreshing generated route-level onboarding indexes after overview or sidecar maintenance.

## Code Commentary

### Logic

The script computes the core skill root, places `_shared` on `sys.path`, imports `build_route_indexes`, parses `--code-repository-root`, `--onboarding-root`, optional `--repository`, `--dry-run`, and `--format`, then delegates all index construction to the shared generator. Text output reports route count, write mode, written count, unchanged count, and each index path. JSON output returns the generator result dictionary.

### Conventions

The wrapper contains no route-index business logic. Keeping the CLI thin lets C-05, tests, installed runtimes, and benchmark fixtures share the same generation behavior through `_shared/agents_remember/route_index.py`.

### Invariants And Boundaries

The script is safe to run after any onboarding maintenance pass. `--dry-run` must not write indexes. Output formatting must not change the generated index semantics; the shared generator owns that contract.

### Todos

After closeout commits this new source file, refresh verification metadata to the committed source revision.

## Docs References

No external domain documentation applies to this repository-local CLI wrapper.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The wrapper imports the shared route-index generator by adding the core `_shared` directory to `sys.path`. | L9-L13 | [build_route_indexes.py](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/scripts/build_route_indexes.py) |
| The CLI exposes repository root, onboarding root, repository name, dry-run behavior, and text/JSON formatting before delegating to `build_route_indexes`. | L16-L31 | [build_route_indexes.py](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/scripts/build_route_indexes.py) |
| Text output reports generated route-index counts and prints every generated index path. | L33-L41 | [build_route_indexes.py](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/scripts/build_route_indexes.py) |

## Cross-Repo References

No sibling repository evidence is needed for this wrapper.

## Update History

- 2026-05-19T03:23+02:00: Created onboarding for the new C-05 route-index refresh CLI. Verification metadata remains pinned until closeout commits the source change.
