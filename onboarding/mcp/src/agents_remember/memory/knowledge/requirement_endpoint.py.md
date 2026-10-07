# mcp/src/agents_remember/memory/knowledge/requirement_endpoint.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Resolves a requirement endpoint of a knowledge record and reads the approval state of a requirement from
its owning task. A record's link names a packet as `{task: {repository, path}, packet, id, version}`. This
module locates the owning task's root and hands the packet reference to the requirement owner, whose
answer it carries back unchanged. It also answers which version of a stable ID the owning task's manifest
approves.

## Code Commentary

- **The task root.** `requirement_task_root` is `<coordination root>/tasks/<repository>/<task path>`, or
  `None` when `repository` contains a slash or backslash or is `.` or `..`.
- **Resolution.** `resolve_requirement_endpoint(coordination_root, reference)` returns a
  `RequirementEndpoint` and never raises for an endpoint that does not resolve:
  - without a coordination root: `unresolved` with `requirement-task-plane-unavailable`;
  - with a repository that is not one directory name: `unresolved` with `requirement-task-outside-tasks`;
  - otherwise the owner's answer from `consume_owner_resolution`: `resolved`, or `unresolved` with the
    owner's refusal code and detail.
  `task_root` is set whenever the root could be located. `key` is
  `<repository>/<task path>#<id>@<version>`.
- **Approval.** `_manifest` reads `<task root>/requirements/manifest.json` and requires the format
  `approved-requirement-corpus` and a `packets` list; otherwise it returns the reason as text.
  `requirement_approval` answers `approved` with the highest approved version of the ID and its packet path,
  `not_approved` when the manifest approves no entry of the ID, or `unknown` with the reason when there is
  no manifest it can read. Versions compare by the integer after `v` (`version_number`).
  `RequirementApproval.newer_than(version)` is true only for a higher approved version.
  `latest_approved_requirement_version` returns the same lookup's `latest`.
- **What is recorded.** The approval state and the packets live outside every Git tree. `_manifest` reads
  the manifest's bytes once and records the SHA-256 of exactly those bytes, `absent` for a missing
  manifest, or `unreadable (<error type>)` for a failed read. The module does not record the packet: the
  requirement owner records its own path resolutions and the bytes it reads
  (`tasks/task_intent.py`, `_approved_packet_ref`). Outside a recording block nothing is recorded.

## Evidence

- The two root answers and the manifest constants. [15]
- One endpoint with the owner's answer and its key. [16]
- The owning task's root, or none for a repository that is not one directory name. [17]
- Resolution hands the reference to the owner and reports an unresolved endpoint. [18]
- The manifest is read once and recorded as bytes, absent or unreadable. [19]
- The approval of one stable ID. [20]
- The comparison of versions. [21]
- A manifest read that fails is recorded as unreadable under the manifest's path. [22]
