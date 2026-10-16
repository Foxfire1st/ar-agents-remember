# mcp/src/agents_remember/cli/role_handover_artifacts.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Persists and verifies the immutable compiled first assignment, its admitted instruction-detail snapshots and its step-up takeover material beside one request report.

## Code Commentary

write_handover_artifact publishes bounded mode-0444 bytes atomically and reuses only exact content. first_message prepends the path/digest recovery line. restore_handover_artifact checks saved reference/message and reached canonical file, reconstructing only missing exact bytes. A symlink at the artifact name is never followed.

## Current Contract — Scoped Launch And Settings Changes

write_detail_artifacts names each .detail-<SHA256(source_path)>.md beside the report and uses the existing write-once mode-0444 publisher for its admitted bytes. Conflicting request content refuses instead of overwriting the earlier snapshot.

write_step_up_artifact freezes bounded JSON takeover material in .step-up.json, returns path/canonicalPath/hash/bytes/content, and the primary handover names its exact hash. restore_step_up_artifact checks that saved path, canonical target, size, digest and primary-handover line agree before reusing or restoring only those saved bytes.

Unlike missing primary/takeover artifacts, missing detail snapshots are not reconstructed from today’s corpus: their validator requires restoring the original frozen detail. All write-once reuse checks now open with O_NOFOLLOW|O_NONBLOCK and fstat a regular descriptor before exact bounded byte comparison; this does not follow an artifact-name link or block on a swapped FIFO.

Primary handover size limit, exact first-message recovery line, atomic hard-link publication and canonical-folder validation remain in force.

## Evidence

- Per-source deterministic detail names reuse immutable publication. [7]
- Takeover reference retains exact bounded bytes. [8]
- Replay binds takeover bytes to the saved report and primary handover. [9]
- Descriptor-level regular-file and no-follow checks protect exact reuse. [10]
- Test source models a regular-to-link swap and unchanged foreign bytes. [11]

- Frozen implementation of write_handover_artifact supporting the stated file behavior. [1]
- Frozen implementation of restore_handover_artifact supporting the stated file behavior. [2]
- Frozen implementation of _write_once supporting the stated file behavior. [3]
- Checks path, bytes, digest, read-only mode, exact reuse and conflicting-content refusal. [4]
- Checks size limit and refuses links without changing their target. [5]
- Through leaf/taskless routes checks restoration/refusal, exact advice and unchanged receipt/foreign link target. [6]
