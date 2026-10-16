# mcp/src/agents_remember/cli/role_instruction_details.py

## Purpose

Bind compiled capsule detail pointers to immutable per-request files and validate them on replay.

## Governing Overview

[MCP package overview](../../../overview.md)

## Current Contract

compose_launch_instructions freezes delivery.detail_references beside report_path, replaces {{detail:<source>}} placeholders in trusted baseline text with those concrete paths, and delegates user append/<overwrite> composition to the existing instruction owner. The composition record keeps sourcePath, path, revision and step for each detail.

validate_instruction_detail_artifacts permits a detail-free composition, but a present detailReferences must be a list of valid objects. Every item requires sourcePath/path/revision, the deterministic report-stem/source-hash name, the saved report canonical directory and a regular no-follow/nonblocking open whose SHA-256 equals revision.

A changed, missing, rebound or nonregular snapshot refuses before sending with original-file/report-access restoration and same-request retry advice. It never regenerates details from a changed corpus. Validation establishes the saved references’ targets and bytes, not a fresh compilation or independent semantic review.

Preparation calls composition; the receipt restoration path and delayed held-seat opening consume validation. User-note precedence remains with compose_role_instructions; detail snapshots do not confer new role authority.

## Evidence

- Freeze and substitute pointers before existing user-note composition. [1]
- Every saved detail is shape/identity/type/revision checked. [2]
- The target must be the deterministic sibling of the saved report. [3]
- Receipt restoration invokes the detail validator. [4]
- Test source distinguishes matching bytes from canonical identity. [5]
