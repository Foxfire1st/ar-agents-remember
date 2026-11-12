# mcp/src/agents_remember/application/dataset_copy_survey.py

## Governing Overview

[mcp/src/agents_remember/application/overview.md](overview.md)

## Purpose

Survey, classification and owner release of leftover knowledge dataset copies: the read side of the copies command.

## Code Commentary

MIK-R82 rules 2 and 3 with MIK-R26 rule 6: content probes, filesystem discovery, rule classification, task and generation census, and the comparison-snapshot owner release. A copy under the notes of a `Completed` or `abandoned` task is deleted; an open task's is not. An unreadable task or generation document is an admission failure with no deletions, never silent absence. One eligible comparison snapshot is released through its generation owner so reopening that generation says its history was deleted and why. This module imports nothing from `legacy_dataset_copies` at runtime; that module keeps plan, apply and report.

## Evidence

- Copies are surveyed, classified and owner-released; finished-task copies delete, unreadable control documents refuse. [1]
