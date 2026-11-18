# mcp/tests/test_curator_coherence_measured_quality.py

## Governing Overview

[Tests](overview.md)

## Purpose

Checks measured quality binding across coherence publication and a later full quality check.

## Code Commentary

Integration cases run quality, publish coherence and run quality again on the unchanged candidate, both with and without a published assessment. Assessment listing alone preserves freshness. Changes to candidate identity, measured report content, findings or other attestation facts make the binding stale.

The suite also checks dependency reconstruction, old generations without measured fields, and complete-file integrity. Historical readability does not make an old record current.

## Relationships

The tests use shared lifecycle fixture support and the production quality/coherence paths. Their assertions describe the regression contract; this card does not claim an additional execution of the suite.

## Evidence

- Publication remains current after the next unchanged quality check. [1]
- Assessment listing is excluded from measured identity. [2]
- Complete stored bytes retain independent integrity checks. [3]
