# mcp/tests/test_sprint_archive.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Tests for archiving a sprint as a whole: preconditions, dry-run exactness, staying masters.

## Code Commentary

MIK-R82 rule 1: every precondition refusal names its row or file and clearing action; the dry run lists exactly what the real run would change; a master another live sprint commands stays, named with the keeping sprint. The cases assert that one readiness refusal names both blocked masters, and that `rowSurvey` lists a missing row and a differing terminal status without changing the task snapshot.

## Evidence




- Sprint-archive preconditions, exact dry runs and staying-master handling are pinned. [1]
