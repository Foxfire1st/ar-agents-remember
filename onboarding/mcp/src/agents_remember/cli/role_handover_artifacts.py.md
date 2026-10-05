# mcp/src/agents_remember/cli/role_handover_artifacts.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Persists and verifies one immutable compiled first-assignment artifact.

## Code Commentary

write_handover_artifact publishes bounded mode-0444 bytes atomically and reuses only exact content. first_message prepends the path/digest recovery line. restore_handover_artifact checks saved reference/message and reached canonical file, reconstructing only missing exact bytes. A symlink at the artifact name is never followed.

## Evidence

- Frozen implementation of write_handover_artifact supporting the stated file behavior. [1]
- Frozen implementation of restore_handover_artifact supporting the stated file behavior. [2]
- Frozen implementation of _write_once supporting the stated file behavior. [3]
- Checks path, bytes, digest, read-only mode, exact reuse and conflicting-content refusal. [4]
- Checks size limit and refuses links without changing their target. [5]
- Through leaf/taskless routes checks restoration/refusal, exact advice and unchanged receipt/foreign link target. [6]
