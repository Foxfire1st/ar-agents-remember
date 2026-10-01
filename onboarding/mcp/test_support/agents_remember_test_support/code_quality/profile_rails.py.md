# mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py

## Governing Overview

[Python quality verification overview](overview.md)

## Purpose

Repository-owned executable adapters for the certification-profile Python rails: it translates one
`quality-config` / `selection-ownership` / `python-suite` / `python-crap` /
`python-diff-coverage` / `verify-teardown` rail invocation into the check.py config and
execution surface, and L19 binds the exact repository selector result into every rail config.

## Code Commentary

### Logic

`build_parser` exposes the six rail subcommands. `_profile_config` rebuilds check.py argv from
the rail arguments, derives the config via `check.config_from_args`, and
`_require_exact_scope` validates the selector's published `repository-selector-result/v2`
JSON against the exact repository-owned derivation (`profile_selection.selection_payload`) and
against the derived executable rail scope; the validated `selection.selectionDigest` is stamped
back into the config via `dataclasses.replace(config, selection_digest=...)`. The
`selection-ownership` and `quality-config` rails run the same exact-scope proof without
executing tests. `_run_python_suite` runs the pytest rail (with retry/causal continuation),
and `_run_post_coverage` dispatches CRAP or diff-coverage from the exact suite artifacts.
`_verify_teardown(summary, proof, source_selection)` loads the admitted ambient-role decision. A not-applicable decision requires the summary to be absent, then writes a passing zero-start proof bound to the decision digest with no replications. An applicable decision requires exactly two ordered, passing, non-retry reports. Each report and the summary must match the frozen candidate tree, base commit, mode and selected paths. Every report must carry a passing `L5-C10` checkpoint; unsafe basenames and malformed or missing evidence refuse. The proof binds the actual summary and replication bytes by SHA-256.

`_paths` canonicalizes scope comparison by sorting each path's POSIX string. `Path` component ordering differs from the selector's string ordering for siblings such as `conversation/` and `conversation-library/`; equal populations now compare in the same order. Sorting retains duplicates, so missing, extra or repeated paths still refuse before pytest.

### Conventions

The `verify-teardown` CLI requires `--summary`, `--proof` and `--source-selection`; it uses the same Dagger admission boundary as the Python rails. Persisted proof bytes are a declared rail artifact, while printed PASS remains diagnostic output.

### Invariants And Boundaries

- Every rail requires the Dagger admission capability; refusals surface as
  `repository certification rail refused: ...` with exit 1.
- The selector contract must match the repository-owned derivation byte-for-byte; a mismatch
  refuses before any test command.
- Only the exact immutable selection digest may enter the retry identity.
- Memory-cap bytes must be non-negative; teardown summaries must be schema-checked.

### Todos

None recorded.

## Evidence

### Docs References

No external Domain Documentation source is configured. These are repository-owned implementation and verification contracts; no external documentation claim is made.

No configured external domain source.

### Repo-Internal References

These source owners establish the current behavior and the stated fixture boundaries.

- The teardown command requires a proof destination. [1]
- Executable scope receives the exact selector digest. [2]
- Published selection is compared with its repository-owned derivation and executable scope. [3]
- The Python rail handles declared retry and causal continuation without changing ownership. [4]
- CRAP and changed coverage consume the exact suite artifact. [5]
- Actual report bytes must carry passing L5-C10 checkpoints; skipped applicability is explicit. [6]
- The persisted proof binds summary bytes and observed replication reports. [7]
- Canonical POSIX-string order aligns equivalent populations without deduplicating them. [8]

### Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

No cross-repository evidence is required.
