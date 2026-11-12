# scripts/check-python-runtime.py

## Governing Overview

[repository overview](../overview.md)

## Purpose

Provides the one executable capability and provenance check for an exact Agents Remember Python
runtime, emitting a structured proof record on success and an actionable refusal on mismatch.

## Code Commentary

### Logic

The probe requires an exact major/minor/patch version and optionally an exact base prefix. Linux
pidfd mode requires callable `os.pidfd_open` and `signal.pidfd_send_signal`. It records source URL,
source digest, builder commit, compiler, configure arguments, executable/base-prefix identity,
standard-library module health, and a content-derived build fingerprint as JSON.

### Conventions

The command is both validator and evidence producer. All required facts are observed from the exact
running interpreter; no build is accepted from its version label alone.

### Invariants And Boundaries

- A version, prefix, or pidfd mismatch fails loudly before a proof is emitted.
- Importing `ctypes` here proves the standard-library module is healthy; it is not a syscall wrapper
  and the probe never implements signaling.
- No third-party compatibility package, `killpg` fallback, or platform/filename guess is accepted.
- Provenance fields describe the supplied build inputs and are folded with observed build identity.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies; this executable contract reports the exact
runtime it observes.

No external source is required to interpret the structured internal proof.

### Repo-Internal References

- Exact version, prefix, and native pidfd capability mismatches are actionable refusals. [1]
- Provenance and observed build identity produce one deterministic fingerprint and JSON report. [2]

### Cross-Repo References

No meaningful cross-repository implementation source governs this probe.

The probe executes solely against the selected local interpreter.
