# mcp/src/agents_remember/models/sprint_archive.py

## Governing Overview

[mcp/src/agents_remember/models/overview.md](overview.md)

## Purpose

Bounded, sprint-owned proof for archiving one orchestration sprint as a whole.

## Code Commentary

MIK-R82 rule 1: `SprintArchiveRecord` and `SprintArchiveMasterEntry` bound what the archive operation may claim: reason, time, every commanded master with its folder, every staying master with why, and what a repeated request is compared with. The record moves with the sprint folder under `0_archive/` and carries the same protection a retirement record carries.

## Evidence

- Sprint-owned record and master-entry models bound the archive claim and its repeat comparison. [1]
