# test_route_index.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember-md                                     |
| path                   | `runtime/skills/U-01-core-skills/tests/test_route_index.py` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-05-19T03:23+02:00                                 |
| lastVerifiedCommitHash | `5b26015bb3e9deec8113b1a69a12608bba82cc27`             |
| lastVerifiedCommitDate | 2026-05-19T03:27:34+02:00|

## Purpose

This unittest module validates the route-index generator and the sidecar availability classifier used by C-04/C-05.

## Code Commentary

### Logic

The main test builds temporary source and onboarding trees, writes root and route overview fixtures, adds one file sidecar, runs `build_route_indexes`, and asserts both generated index files contain the expected route, child route, source scope, covered file, coverage counts, fallback, routing terms, copied hot-path summary, candidate hints, and anchor hints. Separate tests verify `sidecar_status` and the overview-only sparse-memory route case.

### Conventions

The tests use only Python standard-library fixtures so they run anywhere the runtime helpers run. Temporary directories keep generated indexes out of the working tree, and fixture prose intentionally includes code spans, constants, filenames, and function-like anchors so hot-path extraction stays covered.

### Invariants And Boundaries

The tests protect the MVP behavior that matters for benchmark and agent-read efficiency: indexed absence must work without repeated missing-file probes, overview-only routes must remain useful, and hot-path summaries/hints must be emitted from maintained overview prose rather than hand-edited index content.

### Todos

After closeout commits this new source file, refresh verification metadata to the committed source revision.

## Docs References

No external domain documentation applies to this repository-local unit test.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The primary fixture proves root and route indexes, child route wiring, coverage counts, fallback metadata, copied hot-path summary, candidate hints, and anchor hints. | L17-L78 | [test_route_index.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_route_index.py) |
| `sidecar_status` is tested for present, absent-in-scope, and out-of-scope paths. | L81-L88 | [test_route_index.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_route_index.py) |
| The overview-only route test proves sparse memory still indexes source scope and reports empty covered sidecars plus an absent sidecar status. | L91-L111 | [test_route_index.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_route_index.py) |

## Cross-Repo References

No sibling repository evidence is needed for this unit test.

## Update History

- 2026-05-19T03:23+02:00: Created onboarding for the new route-index generator tests. Verification metadata remains pinned until closeout commits the source change.
