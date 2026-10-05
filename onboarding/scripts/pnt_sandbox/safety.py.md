# scripts/pnt_sandbox/safety.py

## Governing Overview

[Route overview](../../overview.md)

## Purpose and current source account

The evaluator checks all reported/required roots after symlink resolution, selected-build package identity, required runtime values and at least one configured repository. It runs both dashboard and tool-server modes and rejects disagreement or unreadable resolution. This covers AR state roots; harness homes, caches and linked Eve resources are outside its measured scope.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]
