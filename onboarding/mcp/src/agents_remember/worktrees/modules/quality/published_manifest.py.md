# mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `../overview.md` |

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

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| The immutable quality manifest retains profile identity separately from gate certificates. | `PublishedQualityManifest` | mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:84-104 |
| Report dependencies bind actual candidate, profile plan, bytes and optional runtime authority. | `quality_report_dependencies` | mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:320-368 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Pointer loading and retained-payload parsing use one strict schema-3.1 owner. | `load_published_quality_manifest`; `parse_published_quality_manifest` | mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:131-138; mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:141-215 |
| Serialization preserves the complete accepted snapshot. | `published_manifest_payload` | mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:107-128 |
| Generation and dependency records are derived from exact bound input fields. | `quality_generation_digest`; `_parse_dependencies`; `quality_report_dependencies` | mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:263-270; mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:231-249; mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:320-368 |
| Manifest file keys are canonical safe relative paths. | `is_safe_relative_report_path` | mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:371-379 |
| Recovery rechecks candidate/profile/plan before evidence reuse. | `recover_strict_code_quality_gate` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:327-399 |

## Cross-Repo References

No meaningful cross-repository implementation reference applies.

## 260824-PDLS — Strict Schema-2 Evidence Pointer (Historical)

The manifest reader remains the one strict parser for the current immutable Dagger generation. The
PDLS wave required schema `2.0` with candidate tree, generation digest, exact file digest/sizes,
and typed attestation; schema `1.0` was deliberately rejected. CCR-R22 replaced that with schema `3.0` plus the mandatory profile identity, and CCR-R12@v4 (this
commit) advanced it to schema `3.1` with the optional shared-Dagger-authority digest, keeping the same
no-compatibility-reader discipline.

## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-05T22:19+00:00 — L30 source review at `6e4ab81f6ae52bce35003377bb3aec7877554ed7`: Exposed the sole strict parser and complete snapshot serializer for certificate-selected generations; preserved schema-3.1 and dependency invariants.

- 2026-09-05T08:46+02:00 — L31 scoped MCP curator: reviewed 2 declined citation claims against frozen code `ea35964985f30080488270e71ac81657ac40682b`. Corrected the category error: the cited field belongs to the published quality manifest, not a gate certificate. Separated recovery admission from report rendering and selected the current function bodies. Existing verification hash/date are retained; this scoped source read and citation repair do not certify the entire card or a gate.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): advanced the card to the schema-`3.1` manifest: new optional root field `runtimeAuthorityDigest` (64-hex, parsed by `_parse_runtime_authority_digest`), a `shared-dagger-authority` admission dependency edge in `quality_report_dependencies` when the digest is present, and refreshed loader/generator/recovery ranges.


- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): rewrote the card for the profile-bound schema-v3 manifest. Added the mandatory profileDigest/profilePlanDigest/profileSelectionId/executorAdapterId/resultDecoder fields, generation-digest field-set discipline, decoder-names-published-file rule, and the re-derived dependency identity; schema 1.0/2.0 without profile identity is now rejected like every legacy shape.

- 2026-08-31T04:50+02:00 -- 260821-ARSPAWN-L5 independent-review repair: added the explicit nested-path safety contract for immutable report manifests. Verification remains closeout-owned.

- 2026-08-25T08:16+02:00 -- 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T21:23+02:00 -- 260824-PDLS centralized strict manifest parsing and retained explicit schema-1 rejection after advisory review.

- 2026-08-24T14:19+02:00 -- 260821-DAGQC-L2: created for the strict schema-1.0 published-quality manifest boundary. Verification remains blank until architect-owned closeout stamps the code commit.
