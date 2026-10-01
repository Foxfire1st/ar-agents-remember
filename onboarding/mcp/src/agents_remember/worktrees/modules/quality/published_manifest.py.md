# mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py

## Governing Overview

[worktrees/modules overview](../overview.md)

## Purpose

Defines the sole strict reader and immutable value model for the atomic current-quality-generation
manifest consumed by quality recovery. Since CCR-R22@v1 (L22, commit `685f83c44055`) the manifest
schema advanced to `3.1` (260831-CCR-L12, commit `cfd09381`) and carries the full repository-profile identity: profile digest, profile plan digest, profile
selection id, executor adapter id, the declared result decoder model, and the optional frozen
`runtimeAuthorityDigest` of the host-level shared Dagger authority admitted for the run. The generation
digest binds all of those fields with the candidate tree, files, and dependencies, so a published
generation cannot be replayed under a different profile identity or authority.

## Code Commentary

### Logic

`load_published_quality_manifest` reads `quality-report-set.json` exactly once and validates it
through the public `parse_published_quality_manifest` owner as schema `3.1`. The root must be an object with only `schemaVersion`, `generation`,
`candidateTree`, `profileDigest`, `profilePlanDigest`, `profileSelectionId`,
`executorAdapterId`, `resultDecoder`, `files`, and optional `attestation`/`dependencies`/`runtimeAuthorityDigest` (`_parse_runtime_authority_digest` accepts only a 64-hex digest when present).
Digest fields must be lowercase 64-hex strings; selection/executor ids must be nonblank;
`resultDecoder` is parsed through `JsonExitStatusDecoderDefinition.model_validate` and must name
a published file. File records contain exactly `sha256` and a non-negative integer `size`;
attestations contain string pairs. Parsed file/attestation mappings are immutable. `require_file`
selects a declared artifact without constructing an unverified path.

`quality_generation_digest(fields)` computes the generation id over exactly the declared field set
(`_GENERATION_DIGEST_FIELDS`) with sorted compact JSON; any other field set is refused. The parser
recomputes the expected generation from the parsed bound fields and refuses drift
(`generation id does not match its bound fields`). `quality_report_dependencies` declares the exact candidate, execution (rail-plan over the profile identity), report
bytes, and - when the manifest carries `runtimeAuthorityDigest` - one `shared-dagger-authority` admission edge consumed by
consumers, accepting only the exact profile-identity field set. `_parse_dependencies` re-derives
and compares the expected dependency record exactly as the evidence-dependency validator requires.

`published_manifest_payload` serializes the complete accepted snapshot, including dependencies and optional attestation/runtime authority, for retention in selected certificate rows. The same public parser reads that snapshot; the current pointer reader does not own a second schema or a compatibility parser.

Each manifest file key is also a strict POSIX relative report path. Empty, absolute, backslash-bearing,
non-normalized, or dot-segment paths are rejected before a `PublishedQualityFile` is constructed.
Nested evidence is addressable, but a manifest can never escape the immutable generation root or
smuggle an alternate path spelling.

### Invariants And Boundaries

- There is one current schema (`3.1`) and one reader; alternate roots, legacy shapes (including
  schema `3.0` / `2.0` / `1.0` without the runtime-authority field set), unknown fields, and
  partial records are rejected.
- The generation digest binds candidate tree + profile identity + files + dependencies + the optional
  runtime authority digest; a moved or modified bound field makes the manifest invalid before any
  artifact lookup.
- The result decoder must name a file present in the published files; recovery decodes through
  exactly that declared decoder.
- All filesystem, JSON, pydantic, and structural failures collapse to `ValueError` surfaces the
  callers convert; no manifest variant is silently tolerated.
- The parsed snapshot is immutable so one recovery cannot silently mix manifest generations.
- Nested file names must be canonical safe relative POSIX paths; traversal and alternate separator
  spellings are invalid manifest evidence.

### Todos

None recorded.

## Evidence

### Docs References

- The immutable quality manifest retains profile identity separately from gate certificates. [1]
- Report dependencies bind actual candidate, profile plan, bytes and optional runtime authority. [2]

### Repo-Internal References

- Pointer loading and retained-payload parsing use one strict schema-3.1 owner. [3]
- Serialization preserves the complete accepted snapshot. [4]
- Generation and dependency records are derived from exact bound input fields. [5]
- Manifest file keys are canonical safe relative paths. [6]
- Render an exact journal selection after full original-object and artifact readback. [7]

### Cross-Repo References

No meaningful cross-repository implementation reference applies.

## 260824-PDLS — Strict Schema-2 Evidence Pointer (Historical)

The manifest reader remains the one strict parser for the current immutable Dagger generation. The
PDLS wave required schema `2.0` with candidate tree, generation digest, exact file digest/sizes,
and typed attestation; schema `1.0` was deliberately rejected. CCR-R22 replaced that with schema `3.0` plus the mandatory profile identity, and CCR-R12@v4 (this
commit) advanced it to schema `3.1` with the optional shared-Dagger-authority digest, keeping the same
no-compatibility-reader discipline.
