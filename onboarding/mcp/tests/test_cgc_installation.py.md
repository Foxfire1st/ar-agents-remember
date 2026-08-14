# test_cgc_installation.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_cgc_installation.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                         |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_cgc_installation.py` covers the CodeGraphContext (CGC) install and doctor
dry-run paths so the planned-command shape and the doctor verdict assembly are
protected without requiring Docker, FalkorDB, or a live coordinator. It is the
F13 unit contract for the provider-owned `cgc` installation module.

## Code Commentary

### Logic

The module imports `agents_remember.providers.lifecycle` plus the CGC layout and
installation entry points (`cgc_doctor`, `cgc_install`, `cgc_install_commands`,
`cgc_install_preflight`, `cgc_runtime_root_containment_check`) from the
provider-first package layout under `mcp/src`. Shared fixtures build a synthetic
coordination root: `_write_cgc_settings` lays down a workspace repo, a memory
repo, and a lifecycle settings file describing a single `codegraphcontext-code`
provider instance (with runner/backend roots, a `repo-a` root, and ownership
labels). `_parse_cgc` builds the real lifecycle parser, parses a `cgc`
subcommand, normalizes CGC defaults, resolves paths, and stabilizes the repo id
so args match the shape the lifecycle dispatch produces. `_scoped_install_args`
assembles a settings-backed, `--repo-id repo-a`, `--dry-run` install invocation.

`CgcInstallDryRunTests` asserts the scoped install dry-run returns the expected
result shape (`provider`, `action: install`, `ok`, `dryRun`, `repoId`) and that
dry-run short-circuits before the real path, so `doctor`/`backend` keys are
absent and the planned `commands` list contains exactly two Compose
invocations — an image build (`build runner`) and a doctor run
(`run --rm --no-deps runner doctor`). A second case proves the dry-run never
materializes the runtime root or state file on disk (the preflight short-circuits
before `ensure_cgc_runtime_layout`). A third case drops `--repo-id` so
`cgc_install` routes to the install-all aggregation and asserts the
`install-all` action, a backend ok flag, a per-repo result count of one, and the
aggregated per-repo `install` result for `repo-a`.

`CgcInstallPreflightTests` calls `cgc_install_preflight` directly and asserts the
dry-run returns no executed results, no backend result, and an early result that
carries `dryRun`, `ok`, the `install` action, and the same planned `commands`.

`CgcDoctorTests` asserts the doctor dry-run assembles its named checks in order
(`runtime-root-contained`, `source-artifact-clean`, `cgc-runner-image`,
`cgc-image-patches`); that the `cgc-runner-image` check fails because no image
was built, dragging the overall verdict to not-ok; and that the doctor `command`
is a Compose plan (`run --rm --no-deps runner doctor`) rather than a captured
run. A direct call to `cgc_runtime_root_containment_check` proves the
`runtime-root-contained` check passes for a coordination-rooted runtime and
reports `outsideSourceRepo: true`.

### Conventions

- Keep these tests synthetic and file-local: use `tempfile.TemporaryDirectory`
  and `--dry-run`, and do not require Docker, FalkorDB, CGC, network access, or a
  real `ar-coordination` root.
- Import the provider-first CGC modules from `mcp/src`
  (`agents_remember.providers.cgc.lifecycle.*`); do not import deleted or
  compatibility shims.
- Drive parsing through the real lifecycle parser via `_parse_cgc` so argument
  normalization matches the production dispatch path rather than hand-built args.
- Assert command shape by slicing trailing argv segments (for example
  `command[-5:]`) so the contract focuses on the planned Compose verbs, not full
  resolved paths.

### Invariants And Boundaries

Dry-run install must stay side-effect free: it must short-circuit before the
runtime layout and state file are created, and must not emit
`doctor`/`backend` keys reserved for the real install path. The planned install
commands must remain exactly the image build followed by the doctor run, and the
doctor dry-run must keep its four named checks in the documented order with the
runner-image check failing (and the overall verdict failing) when no image
exists. The runtime-root containment check must keep reporting the runtime as
outside the source repo for a coordination-rooted layout. These tests validate
planned-command shape, dry-run side-effect absence, and doctor verdict assembly
only; live install execution, Docker backends, patch application, and graph
query results remain lifecycle/provider integration concerns.

### Todos

None.

## Docs References

No external documentation is needed for these unit tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Shared fixtures build a synthetic coordination root and settings file for a single `codegraphcontext-code` provider instance and parse CGC arguments through the real lifecycle parser. | `_parse_cgc` | mcp/tests/test_cgc_installation.py:22-98 |
| The scoped install dry-run asserts the result shape, absence of `doctor`/`backend` keys, and the two planned Compose commands (image build, then doctor run). | `test_scoped_install_dry_run_returns_expected_shape_without_docker` | mcp/tests/test_cgc_installation.py:102-125 |
| The dry-run side-effect test proves the runtime root and state file are not materialized because preflight short-circuits before the layout is ensured. | `test_dry_run_does_not_create_runtime_layout_on_disk` | mcp/tests/test_cgc_installation.py:127-137 |
| The no-`--repo-id` install dry-run routes to install-all and asserts the aggregated action, backend ok flag, repo count, and per-repo `install` result. | `test_install_all_dry_run_aggregates_per_repo_results` | mcp/tests/test_cgc_installation.py:139-163 |
| The preflight dry-run returns no executed/backend results and an early result carrying `dryRun`, `ok`, the `install` action, and the planned commands. | `test_preflight_dry_run_returns_dry_run_result_and_no_executed_results` | mcp/tests/test_cgc_installation.py:167-181 |
| The doctor dry-run asserts the named check order, the failing runner-image check and overall verdict, and the Compose doctor command plan. | `test_doctor_dry_run_assembles_named_checks_without_docker` | mcp/tests/test_cgc_installation.py:185-229 |
| The runtime containment check passes for a coordination-rooted runtime and reports `outsideSourceRepo`. | `outsideSourceRepo` | mcp/tests/test_cgc_installation.py:249-249 |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired the scoped CGC-installation test citations; final exact frozen-snapshot check is clean.
- 2026-07-31T16:40+02:00 — 260731-EFA-L2: the whole-tree `ruff format` pass (`00e8379`) reflowed
  `mcp/tests/test_cgc_installation.py` and moved the lines this card cites, so the Citations
  column no longer pointed at the code its rows name. Corrected the ranges (L22-L100 → L22-L98;
  L104-L127 → L102-L125; L129-L139 → L127-L137; L141-L165 → L139-L163; L169-L185 → L167-L181;
  L189-L233 → L185-L229; L235-L244 → L231-L240). The behaviour described is unchanged — the file's
  AST is identical to the base revision — this is a citation repair only. Verification metadata
  pinned until closeout stamps the L2 commit.

- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
