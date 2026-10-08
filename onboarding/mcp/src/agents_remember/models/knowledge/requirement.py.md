# mcp/src/agents_remember/models/knowledge/requirement.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

Carries the exact task-document identity that owns a requirement and the result of resolving that owner.

## Code Commentary

`RequirementOwnerRef` names the task-relative path, stable requirement ID and version under their declared patterns. `RequirementOwnerResolution` carries the resolved owner or its refusal. These are frozen values, not filesystem admission or a durable requirement revision. RequirementRevisionPayload and its canonical writer/read graph were retired; ownership resolution cannot silently substitute another requirement version.

## Evidence

### Repo-Internal References

- `RequirementOwnerRef` owns the current boundary described above. [23]
- `RequirementOwnerResolution` owns the current boundary described above. [24]
