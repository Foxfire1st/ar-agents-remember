# mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T10:05+02:00 |
| lastVerifiedCommitHash | `cfd0938103b1392e471144b6997c51a41591ad2b` |
| lastVerifiedCommitDate | 2026-09-04T08:34:11+02:00 |
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
as schema `3.1`. The root must be an object with only `schemaVersion`, `generation`,
`candidateTree`, `profileDigest`, `profilePlanDigest`, `profileSelectionId`,
`executorAdapterId`, `resultDecoder`, `files`, and optional `attestation`/`dependencies`/`runtimeAuthorityDigest` (`_parse_runtime_authority_digest`, lines 259-267, accepts only a 64-hex digest when present).
Digest fields must be lowercase 64-hex strings; selection/executor ids must be nonblank;
`resultDecoder` is parsed through `JsonExitStatusDecoderDefinition.model_validate` and must name
a published file. File records contain exactly `sha256` and a non-negative integer `size`;
attestations contain string pairs. Parsed file/attestation mappings are immutable. `require_file`
selects a declared artifact without constructing an unverified path.

`quality_generation_digest(fields)` computes the generation id over exactly the declared field set
(`_GENERATION_DIGEST_FIELDS`) with sorted compact JSON; any other field set is refused. The parser
recomputes the expected generation from the parsed bound fields and refuses drift
(`generation id does not match its bound fields`). `quality_report_dependencies` (lines 296-346) declares the exact candidate, execution (rail-plan over the profile identity), report
bytes, and - when the manifest carries `runtimeAuthorityDigest` - one `shared-dagger-authority` admission edge consumed by
consumers, accepting only the exact profile-identity field set. `_parse_dependencies` re-derives
and compares the expected dependency record exactly as the evidence-dependency validator requires.

Each manifest key is also a strict POSIX relative report path. Empty, absolute, backslash-bearing,
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

CCR-R22@v1 requires each gate certificate to name the exact admitted profile and its gate-specific
plan digest, and a profile or referenced-input change to invalidate only the declared certificate
dependency closure. The manifest v3 field set is this requirement's durable record in the quality
publication path.

| Finding | Anchor | Source |
| --- | --- | --- |
| Each gate certificate names the exact admitted profile and its gate-specific plan digest. | `profile_plan_digest` | mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:129-130 |
| A profile or referenced-input change invalidates only the declared certificate dependency closure. | `quality_report_dependencies` | mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:261-302 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The loader reads the sole manifest pointer and returns one strict schema-3.1 snapshot with profile identity and optional runtime authority digest. | `load_published_quality_manifest`; `_parse_manifest` | mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:107-116; mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:117-193 |
| Generation and dependency digests require the exact bound field sets; a present runtime authority digest participates in both. | `quality_generation_digest`; `quality_report_dependencies` | mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:239-248; mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:296-346 |
| Manifest file keys are safe canonical relative paths before they become evidence records. | `is_safe_relative_report_path` | mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:347-357 |
| The quality gate recovery recompiles the expected plan digest for the candidate before reuse, then decodes via the declared decoder; report/test-results render the authority digest when present. | `recover_strict_code_quality_gate`; `_write_test_results_report` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:294-362; mcp/src/agents_remember/worktrees/modules/quality/gate.py:425-480 |

## Cross-Repo References

No meaningful cross-repository implementation reference applies.

## 260824-PDLS — Strict Schema-2 Evidence Pointer (Historical)

The manifest reader remains the one strict parser for the current immutable Dagger generation. The
PDLS wave required schema `2.0` with candidate tree, generation digest, exact file digest/sizes,
and typed attestation; schema `1.0` was deliberately rejected. CCR-R22 replaced that with schema `3.0` plus the mandatory profile identity, and CCR-R12@v4 (this
commit) advanced it to schema `3.1` with the optional shared-Dagger-authority digest, keeping the same
no-compatibility-reader discipline.

## Update History

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): advanced the card to the schema-`3.1` manifest: new optional root field `runtimeAuthorityDigest` (64-hex, parsed by `_parse_runtime_authority_digest`), a `shared-dagger-authority` admission dependency edge in `quality_report_dependencies` when the digest is present, and refreshed loader/generator/recovery ranges.


- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): rewrote the card for the profile-bound schema-v3 manifest. Added the mandatory profileDigest/profilePlanDigest/profileSelectionId/executorAdapterId/resultDecoder fields, generation-digest field-set discipline, decoder-names-published-file rule, and the re-derived dependency identity; schema 1.0/2.0 without profile identity is now rejected like every legacy shape.

- 2026-08-31T04:50+02:00 -- 260821-ARSPAWN-L5 independent-review repair: added the explicit nested-path safety contract for immutable report manifests. Verification remains closeout-owned.

- 2026-08-25T08:16+02:00 -- 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T21:23+02:00 -- 260824-PDLS centralized strict manifest parsing and retained explicit schema-1 rejection after advisory review.

- 2026-08-24T14:19+02:00 -- 260821-DAGQC-L2: created for the strict schema-1.0 published-quality manifest boundary. Verification remains blank until architect-owned closeout stamps the code commit.
