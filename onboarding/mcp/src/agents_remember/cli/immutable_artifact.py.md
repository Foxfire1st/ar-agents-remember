# mcp/src/agents_remember/cli/immutable_artifact.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

One immutable file of a launch, created once and never followed at its own name — the single implementation of the contract every artifact beside a report obeys.

## Code Commentary

write_once publishes a finished temporary file by hard link, so a reader never sees a partial file and an existing name is reused only when it already holds exactly those bytes; different content is refused in the caller's own words and nothing changes. preflight answers the same question without writing, which is what lets a launch decide a refusal before it creates anything. A target that is not a regular file — a link, a directory or a device at the artifact's own name — is refused there in the caller's own words too, because each caller (the complete hand-over's publication, the restore of saved takeover material, the artifact's own writer) passes a refusal that names its file and its remedy. holds_exactly compares the reached file with the expected bytes, and a non-regular file it reaches without preflight keeps the module's fixed sentence, so a caller that skipped preflight is told only that the path is not a regular file. canonical_path resolves the file's own name without following a link at it, so a link planted at the artifact name is never written through.

## Evidence

- The file is published by hard link of a finished temporary file and reused only on equal bytes. [1]
- The refusal is decided without writing, so a caller can leave every target as it was, and a target that is not a regular file is refused with the caller's own words rather than a fixed sentence. [2]
- An existing file is compared with the expected bytes exactly. [3]
- A link at the artifact's own name is never followed. [4]
