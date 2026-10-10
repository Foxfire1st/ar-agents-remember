# mcp/tests/test_legacy_expectation_kinds_parse_only.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

LOCR-R24 guards keep the retired expectation kinds (`turn-report-by`, `ack-by`) parse-only: stored v2 rows of either kind still read back through the store, the projection read and direct model validation, while the settings vocabulary and default SLAs exclude both, SLA lookups raise, and settings refuse SLA defaults for retired kinds as unknown. An AST precise-literal sweep proves no shipped module but the `ExpectationKind` Literal names a retired kind (docstring prose ignored), the notifier finding/action vocabularies stay free of them, and one real notifier sweep neither marks, writes nor delivers a retired row. The settings fixture writes the user settings file.

## Evidence

- Retired expectation kinds stay parse-only across store, projection and validation with the user-settings fixture move. [1]
