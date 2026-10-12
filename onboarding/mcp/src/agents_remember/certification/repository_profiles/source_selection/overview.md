# Repository Source Applicability Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/certification/repository_profiles/source_selection` |

## Governing Overview

[Certification contract overview](../../overview.md)

## Purpose

This package determines whether an individual repository rail applies to an exact candidate, using repository-declared path prefixes before execution. It separates declaration validation, Git observation, pure decision compilation and retained decision reading. It does not own the Python dependency-closure selector or dashboard test commands.

## Hot Path Summary

`git.py` observes the exact base/candidate path delta when a selected rail declares source applicability. `compilation.py` derives the rail decision, and `models.py` validates the complete frozen record. `validation.py` checks evidence publication, command placeholders and conditional prerequisites during profile validation. `reader.py` reopens and validates the retained decision for consumers.

## How It Is Built

A source-applicability declaration names a selector and version, ordered unique dependency prefixes, a repository-relative evidence path and a non-applicability reason. Profile validation requires unique selector IDs and evidence paths, a declared same-gate evidence publication, and command consumption of exactly the rail's own and declared conditional source-selection inputs.

The Git observer requires the actual repository root and an exact Git-tree candidate. It resolves the base commit and tree, then obtains a recursive, NUL-delimited path delta with rename detection disabled. The observation records the base commit, both trees, sorted changed paths and a digest. Model validation checks canonical repository-relative paths, uniqueness, ordering and digest consistency.

The compiler selects changed paths by literal prefix matching and freezes the declaration, observation, mode, selected paths and applicability into a digested decision. Full mode makes an already selected rail applicable even when no path matches. Targeted mode makes it applicable only when a path matches; otherwise the decision carries the repository-declared reason. The decision model recomputes selected paths, applicability, selection identity and decision digest rather than trusting retained values.

The retained reader accepts a regular file within its 1,000,000-byte bound, reads with the same bound and validates the JSON as a frozen rail decision. Git output has a separate 16 MiB observation bound.

### File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `__init__.py` | [__init__.py.md](__init__.py.md) | covered |
| `models.py` | [models.py.md](models.py.md) | covered |
| `compilation.py` | [compilation.py.md](compilation.py.md) | covered |
| `git.py` | [git.py.md](git.py.md) | covered |
| `reader.py` | [reader.py.md](reader.py.md) | covered |
| `validation.py` | [validation.py.md](validation.py.md) | covered |

## Invariants And Boundaries

- Prefixes are literal string prefixes. Directory-only matching requires an explicit trailing slash.
- Failed, oversized or truncated Git observation refuses the selection; it does not widen applicability or substitute an empty census.
- Non-applicability is admitted before execution. A source-applicability rail cannot reclassify its result through a skipped exit code.
- A conditional prerequisite must also be a declared prerequisite, exist in the same gate and own a source-applicability declaration. Duplicate conditional edges are rejected.
- Full mode affects applicability of selected rails; it does not select additional rails.
- A path-based rail decision does not establish that another test selector can narrow its population.

No configured Domain Documentation source applies to this repository-owned contract. No cross-repository implementation boundary is owned by this route.

## Evidence

- Git observation binds the exact complete base/candidate path delta. [1]
- Decisions recompute prefix selection, applicability and identity. [2]
- Profile validation enforces publication, command and dependency contracts. [3]
