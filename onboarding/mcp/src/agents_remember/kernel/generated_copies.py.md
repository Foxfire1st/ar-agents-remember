# mcp/src/agents_remember/kernel/generated_copies.py

## Governing Overview

[Area overview](../../../overview.md)

## Purpose

Parses repository-owned byte-copy declarations through a dependency-free shared kernel owner.

## Code Commentary

The present UTF-8 JSON must have exactly version/copies, with integer version1 (not bool). Each projection names source, nonempty labeled targets and string ignore lists. Paths must already be literal confined repository-relative POSIX paths, not normalized repairs. Sources and target paths are unique; source/target ancestor overlap and nested target overlap refuse. CopyProjection ignores any relative-path component matching a declared name or suffix.

## Invariants And Boundaries

Parsing does not acquire a tree, decide absence, compare bytes or suppress work: generators and candidate readers own those observations and their domain errors.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- Parses repository-owned byte-copy declarations through a dependency-free shared kernel owner. Parsing does not acquire a tree, decide absence, compare bytes or suppress work: generators and candidate readers own those observations and their domain errors. [1]
