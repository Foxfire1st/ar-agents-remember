# scripts/check-python-runtime.py

## Governing Overview

[repository overview](../overview.md)

## Purpose

Provides the one executable capability and provenance check for an Agents Remember uv-managed Python minor-line runtime without invoking `uv`, emitting a structured proof record on success and an actionable refusal on mismatch.

## Code Commentary

### Logic

The probe requires `--expected-version` in `major.minor` form (`_check_version`) and accepts any patch of that minor while refusing wrong minors with expected minor, observed version, and executable. `_base_prefix` reads the unresolved `pyvenv.cfg` `home` (via `agents_remember.python_runtime.read_venv_home`, or `sys.executable`'s base when `--base-interpreter` is passed) and verifies `is_uv_minor_base(base, minor)` plus any `--expected-base-prefix`, refusing exact patch directories and bases outside `uv_python_directory()`. Linux `--require-linux-pidfd` mode requires callable `os.pidfd_open` and `signal.pidfd_send_signal`. It reports built-in `readline` as `"built-in"` without crashing, records `provenance` (`uvVersion`, `pythonBuild` from `base/BUILD`, and optional `uvImageDigest`), compiler, configure arguments, executable/base-prefix identity, standard-library module health, and a content-derived `buildFingerprint` as JSON.

### Conventions

The command is both validator and evidence producer. All required facts are observed from the running interpreter without invoking `uv`; no build is accepted from its version label alone.

### Invariants And Boundaries

- A minor-version, uv minor-link base prefix, or pidfd mismatch fails loudly before a proof is emitted.
- Importing `ctypes` here proves the standard-library module is healthy; it is not a syscall wrapper and the probe never implements signaling.
- No third-party compatibility package, `killpg` fallback, or platform/filename guess is accepted.
- Provenance fields describe observed `uvVersion`, `pythonBuild`, and optional `uvImageDigest` folded with observed build identity.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies; this executable contract reports the exact runtime it observes.

No external source is required to interpret the structured internal proof.

### Repo-Internal References

- Minor-version, uv-managed base-prefix, and native pidfd capability mismatches are actionable refusals. [1]
- Provenance (`uvVersion`, `pythonBuild`, optional `uvImageDigest`) and observed build identity produce one deterministic fingerprint and JSON report. [2]

### Cross-Repo References

No meaningful cross-repository implementation source governs this probe.

The probe executes solely against the selected local interpreter.
