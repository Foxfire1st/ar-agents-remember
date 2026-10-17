# mcp/tests/test_route_review_clean_sync_door.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Guard the closeout door's exact clean-sync review boundary.

## Code Commentary

## Exact-path clean-sync regression boundary

This module drives the closeout door's own review-provenance check using real temporary Git repositories, canonical leaf documents and recorded route reviews. It checks the plane stamp, disjoint-sync acceptance with the original digest, overlap refusal, added-path and mode refusal, unrelated-base refusal and missing-stamp refusal. Its CR/LF cases distinguish replacement, false overlap and same-map key collision. These cases guard exact byte path identity, not the complete closeout transaction, integration acceptance or every kernel-runner behavior. Source assertions and retained producer execution evidence are separate; the Curator did not rerun tests.

## Evidence

- The plane stamps the actual leaf review base. [1]
- Disjoint sync keeps proven provenance and the original review digest. [2]
- An overlapping reviewed/incoming path is refused. [3]
- Extra paths and changed executable mode are refused. [4]
- An unrelated recorded base is refused. [5]
- Legacy evidence without a base stamp gains no clean-sync admission. [6]
- Replacing a CR path with an LF path cannot preserve the reviewed delta. [7]
- Distinct CR/LF reviewed and incoming paths do not falsely overlap. [8]
- Two same-diff CR/LF paths retain separate entries. [9]
