# mcp/src/agents_remember/cli/role_handover_artifacts.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Persists and verifies the immutable compiled first assignment, its flat/standalone instruction-detail snapshots, and its step-up takeover material beside one request report.

## Code Commentary

`write_handover_artifact` publishes bounded mode-0444 bytes atomically and reuses only exact content. `first_message` appends the trailing suffix `artifact_line` (`"holds the launch handover above this line"`) after the saved handover base so dynamic locator paths and SHA-256 digests never precede the static capsule prefix; `legacy_prefix_artifact_line` preserves the pre-CAP-L2 leading locator line for replay of saved legacy receipts. `resolve_handover_envelope` filters structural boundary candidates from `role_handover_file.handover_envelope_candidates` against exact recorded suffix or legacy-prefix locator text and `sha256(content)`, requiring a unique match and refusing zero or ambiguous matches. `restore_handover_artifact` and `checked_handover_artifact_target` verify the saved reference, envelope boundary, and reached canonical file, reconstructing only missing exact bytes. A symlink at the artifact name is never followed. The complete handover is a second file whose rendering, planning, write-once publication, boundary candidate extraction, and restore live in `role_handover_file.py`, which this module calls, and `artifact_line` names both files.

`write_detail_artifacts` handles flat/non-compact (`compact_links=False`) detail publication: it names each `.detail-<SHA256(source_path)>.md` beside the report and uses the write-once mode-0444 publisher for its admitted bytes, refusing conflicting request content instead of overwriting an earlier snapshot. Turn-1 compact launches (`compact_links=True`) freeze details under `<stem>.details/<source_path>` via `role_instruction_details._write_nested_detail_artifacts`.

`write_step_up_artifact` freezes bounded JSON takeover material in `.step-up.json`, returning `path`/`canonicalPath`/`sha256`/`bytes`/`content`, and the primary handover names its exact hash. `restore_step_up_artifact` checks that saved path, canonical target, size, digest, and primary-handover line agree before reusing or restoring only those saved bytes.

Unlike missing primary and takeover artifacts, missing detail snapshots are not reconstructed from today's corpus: their validator requires restoring the original frozen detail. Write-once reuse checks open with `O_NOFOLLOW|O_NONBLOCK` and `fstat` a regular descriptor before exact bounded byte comparison (`immutable_artifact.holds_exactly`), never following an artifact-name link or blocking on a swapped FIFO.

## The published path and the canonical file

`handover_artifact_reference` and `write_handover_artifact` name the artifact twice. `path` is where the agent reaches it: the request's locator directory plus the artifact's own basename when a locator is given. `canonicalPath` is the same file beside the report with every link of its folder resolved. The file is still created, reused and checked at its canonical place, with its own name, write-once mode 0444 and exact bytes; only the path the agent is given changes. `checked_handover_artifact_target` rebuilds a lost request locator at the folder the receipt recorded before it compares the reached file, and refuses a locator that leads to another folder with the refusal's remedy. `artifact_line` therefore names the locator and the digest in the first message, while the complete hand-over keeps its own sibling path.

## Evidence

- Takeover reference retains exact bounded bytes. [8]

- Replay binds takeover bytes to the saved report and primary handover. [9]

- Test source models a regular-to-link swap and unchanged foreign bytes. [11]

- `write_once`, imported from `cli/immutable_artifact` as `_write_once`, is how this module's artifacts are created once and reused only when they already hold the same bytes. [3]


- `write_handover_artifact` publishes bounded read-only handover text bytes beside the report and returns locator and canonical references. [1]
- `restore_handover_artifact` verifies the handover envelope and target file before restoring missing exact bytes. [2]
- Checks path, bytes, digest, read-only mode, exact reuse, and conflicting-content refusal. [4]
- Checks size limit and refuses links without changing their target. [5]
- Through task-bound and taskless routes checks restoration/refusal, exact advice, and unchanged receipt/foreign link target. [6]
- `write_detail_artifacts` publishes flat/standalone `.detail-<sha256>.md` snapshots via immutable write-once custody. [7]
- Exact reuse is protected by `cli/immutable_artifact.holds_exactly` descriptor-level regular-file and `O_NOFOLLOW` checks, reached through the imported `preflight` and `_write_once` seams. [10]
- `first_message` appends the suffix `artifact_line`, `legacy_prefix_artifact_line` preserves legacy prefix replay, and `resolve_handover_envelope` selects the unique exact locator and digest match. [13]
