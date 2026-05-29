# mcp/src/agents_remember/memory/baseline.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory/baseline.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `23f4d7681f7fcd729049c5f27878c84bbb8f8e58` |
| lastVerifiedCommitDate | 2026-05-29T20:24:00+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`baseline.py` is the package-local C-10 implementation for inspecting and
adopting an existing external-memory onboarding baseline.

## Code Commentary

### Logic

The module exposes `BaselineRequest`, `baseline_status()`, and
`baseline_adopt()` as service entry points for MCP controllers. The CLI
commands now adapt parsed arguments into that request shape, print the returned
payload, and return the service return code.

### Invariants And Boundaries

- Adoption requires external topology.
- Actionable drift blocks adoption unless explicitly accepted.
- This module is invoked through typed MCP payloads, not through a coordinator
  runtime script path.
- MCP controllers should call `baseline_status()` and `baseline_adopt()`
  directly rather than invoking `main(argv)` and parsing stdout.
- Baseline status imports drift classifiers from the `memory_quality.integrity`
  package; the old top-level `drift` package is no longer present.
- `baseline_adopt`'s `dry_run` defaults to `False` (act-by-default); `dry_run=true`
  previews the adoption plan without committing.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `memory_baseline_status` and `memory_baseline_adopt` call this module. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |
| Ledger parsing and writing live in the kernel. | [memory_ledger.py](agents-remember-md/mcp/src/agents_remember/kernel/memory_ledger.py) |

## Update History

- 2026-05-29T18:35+02:00: Typed drift rows as `list[drift.DriftRow]`, normalized `topology` to `Literal['internal','external'] | None` at the argparse boundary, and added a ledger-path guard in `baseline_adopt`; behavior-preserving (commit `0549b28`).
- 2026-05-24T02:47+02:00: Updated after drift imports moved under `memory_quality.integrity`.
- 2026-05-24T00:35+02:00: Updated after adding request/service entry points for MCP controllers.
- 2026-05-23T13:09+02:00: Copied into the MCP package and patched to package imports.
