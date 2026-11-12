# Selected Code Execution And Retained Reports

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees/modules/quality/execution/` |

## Governing Overview

[Worktree modules overview](../../overview.md)

## Purpose

This directory prepares the code-executor transport for an explicitly selected certification suffix and the original report bytes of its reused prefix. It validates the frozen R21 reuse decision, admits a fresh or selected repository profile, and writes the candidate sandbox manifest. Lifecycle selection belongs to the surrounding journal owner; the neighboring clean executor prepares the sandbox, admits the Dagger runtime, starts execution, and manages sandbox replacement and runtime-owner release.

## Hot Path Summary

Start with `models.py` for the code-only launch contract, `retained_reports.py` for original report transport, and `sandbox.py` for profile admission and candidate manifest composition. The package marker has no initialization behavior.

## How It Is Built

`CodeCertificationExecution` revalidates serialized frozen objects and recomputes the canonical R21 reuse plan. Only a first gate of 1–4 enters this transport; Gate-5-only and finalization-only decisions have no code gate start and are rejected. Retained certificates must equal the exact reused prefix. Each retained result must be originally green and bound to its original publication authority.

For a fresh run, profile admission loads the candidate profile, resolves its purpose/mode selection, observes Git source selection, and admits the execution plan. For selected execution, admission retains the frozen semantic profile and plan, verifies candidate tree, mode, purpose and repository identity, and reads the candidate profile file only for bounded raw-byte provenance. It does not reload or reselect semantic authority.

Retained report membership comes jointly from the original result's evidence/artifact members and the frozen producer declarations. Inventory validation requires the exact publishing gate, publication inventory, digest and size; it rejects conflicting paths and enforces declaration byte limits, their aggregate bound, and a 4,096-file ceiling. Snapshotting resolves every original publication path before creating transport files, rereads and verifies bounded source bytes, and copies them with exclusive destination creation. A run starting at Gate 1 has no retained prefix to copy.

Manifest composition reobserves actual source selection in the prepared sandbox and refuses a mismatch with the frozen comparison authority. It atomically writes source and candidate provenance, comparison base, profile provenance and plan, executor adapter, result decoder, runtime authority, and declared publications. Selected execution additionally supplies its validated execution payload and retained report inventory. The surrounding gate passes explicit owner callbacks for start authorization and generation retention, then calls the owner's terminal-selection callback after recording a published generation.

| Source File | Onboarding | Role |
| --- | --- | --- |
| `__init__.py` | [__init__.py.md](__init__.py.md) | Documentation-only package marker |
| `models.py` | [models.py.md](models.py.md) | Exact selected code suffix and original prefix validation |
| `retained_reports.py` | [retained_reports.py.md](retained_reports.py.md) | Frozen producer bounds and confined original byte copies |
| `sandbox.py` | [sandbox.py.md](sandbox.py.md) | Fresh/selected profile and candidate admission manifest |

## Invariants And Boundaries

- A transport DTO or manifest does not confer lifecycle journal authority or prove that a gate ran. Command startup and returned-terminal selection remain neighboring owner responsibilities.
- No current-generation pointer or history search supplies a missing predecessor. Retained transport uses the explicitly supplied original publications.
- Original publication provenance remains distinct from semantic certificate and reuse identity. Selected profile raw-byte provenance likewise does not replace frozen semantic profile authority.
- Retained source paths are confined to their accepted original generations; unsafe paths, symlink components, changed bytes, conflicting producer paths, and exceeded bounds are refused.
- A candidate identity mismatch is refused during selected profile admission; a source-selection mismatch is refused before manifest publication.
- This directory does not implement Gate 5 or the production finalization continuation.

The configured Domain Documentation registry has no entries. The adjacent quality, certification-domain and lifecycle journal owners provide the same-repository boundaries; this directory defines no external protocol.

## Evidence

- The code boundary recomputes reuse and rejects zero-code-start decisions. [1]
- Original result membership and frozen declarations jointly bound retained files. [2]
- Snapshotting reopens the original publication before exclusive copies. [3]
- Selected admission preserves frozen semantic profile authority. [4]
- Manifest composition reobserves actual source selection. [5]
- The surrounding gate receives explicit owner selection/start/retention callbacks. [6]
