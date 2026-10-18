# docs/reference/repository-certification-profile.md

## Governing Overview

[Reference documentation overview](overview.md)

## Purpose

Documents repository-owned authority for explicitly requested certification, without making it an ordinary-closeout prerequisite.

## Code Commentary

Requested certification is explicitly selected repository-profile work through Dagger and commits nothing. The profile and loader are still authority for that requested Gates 1–4 work; a selection named `closeout` is not an automatic closeout invocation. Ordinary closeout runs no gate but the invariant gate, retains exact candidate/approval/lineage checks and code-then-memory Git publication, and does not run certification, code-quality checks, test suites or independent review. A missing profile or certification result does not block that transaction. This does not remove canonical Curator/Reviewer duties or confer independent semantic acceptance on diagnostics.

## Evidence

- Requested certification is explicitly selected repository-profile work through Dagger and commits nothing. The profile and loader are still authority for that requested Gates 1–4 work; a selection named `closeout` is not an automatic closeout invocation. Ordinary closeout runs no gate but the invariant gate, retains exact candidate/approval/lineage checks and code-then-memory Git publication, and does not run certification, code-quality checks, test suites or independent review. A missing profile or certification result does not block that transaction. This does not remove canonical Curator/Reviewer duties or confer independent semantic acceptance on diagnostics. [1]
