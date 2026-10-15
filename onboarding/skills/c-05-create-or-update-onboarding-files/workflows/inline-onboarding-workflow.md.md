# skills/c-05-create-or-update-onboarding-files/workflows/inline-onboarding-workflow.md

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

This source is the storage adapter for file-level onboarding embedded in source comments. It reuses the file-level content model and adds only language-valid delimiters, safe placement, stable markers, digest verification and sidecar fallback. Its goal is to avoid breaking runtime, parsing, build or tooling behavior; it does not define a second semantic onboarding model.

## Code Commentary

### Logic

The adapter starts from the file-level model, chooses idiomatic valid comments for the host language, and places the block at the highest safe location without disturbing shebangs, directives, encoding markers, generated notices or other required leading syntax. `@ar-onboarding` and `@ar-onboarding-end` delimit the block. `sourceDigest` is recomputed from the source body with the onboarding block removed, so the block is not its own digest input. If placement or text parsing cannot be made safe, the workflow falls back to sidecar onboarding instead of forcing inline storage.

### Conventions

The inline block template carries `format: 1`, `sourceDigest: sha256:<digest-of-source-with-this-block-removed>`, `verifiedAt: <YYYY-MM-DDTHH:MM>`, `scope: file` and `governingOverview`. It serializes governing context, purpose, logic, conventions, invariants and boundaries, durable todos and the three reference buckets. Only the outer comment syntax changes with the host language; markers and metadata keys remain stable. The template also requires a Markdown governing-overview link rather than a bare path. These are fields of the retained inline adapter, not metadata for this converted Markdown card.

### Verification And Fallback

The workflow specifies `verifiedAt` in `YYYY-MM-DDTHH:MM` format and SHA-256 for the source body excluding the block. It classifies missing markers or missing `sourceDigest` as missing onboarding or missing verification during drift detection; unsupported safe text parsing triggers sidecar fallback. This card describes the workflow's declared verification contract, not inspected drift-detector implementation or an observed successful verification run. Digesting and timestamps here must not be confused with legacy file-sidecar commit stamps.

### Applicability To Converted Memory

The canonical skill says inline onboarding is a storage-specific adapter reusing file-level semantics. Its Converted Memory section sends converted cards and overviews to `converted-card-workflow.md` and makes the retained unconverted instructions read-only; the file-level workflow has the same explicit redirect. The inline workflow itself contains no conversion procedure and does not establish that an inline block substitutes for a converted Markdown/JSON pair or that ordinary writes to legacy memory are allowed.

This onboarding card about the adapter is itself converted. It uses a canonical source-path title, a relative governing link, self-contained prose and temporary evidence-table authoring input. The converted workflow assigns sidecar-reference authoring to the fixer and typed entries to the writer. It forbids legacy metadata tables, Update History, hand-authored sidecar anchors and self-allocated reference numbers. The adapter's markers, digest and `verifiedAt` describe source-comment storage; they are not fields to add to this card, and a template grants no operational authority.

### Invariants And Boundaries

Inline storage must preserve the host file's behavior and tooling contract. It cannot move required leading syntax merely to achieve a higher block position. Shared semantics do not let the adapter invent a competing content schema, and unsupported storage falls back rather than weakening parsing safety. These are source-level instructions, not an account of exercising the adapter.

### Retained Notes And Discovery Scope

The inherited card records no current todo for this workflow. It also records that no external domain documentation applied, no relevant external documentation was found, no sibling repository evidence was needed and no meaningful cross-repo references were found. Preserve those as inherited repository-local discovery and boundary notes, not a new live search or a fresh registry-state claim. The source and actual file/inline templates support the adapter description, without re-certifying the broader historical discovery observations.

## Evidence

- Inline onboarding is source-embedded storage reusing the file-level template, with no independent semantic model. [1]
- Adapter steps choose comments and safe placement, preserve markers, remove the block from digest input and fall back to sidecars. [2]
- Verification specifies timestamp format and SHA-256, classifies missing markers or digest, and falls back on unsupported text parsing. [3]
- The block template declares markers and inline fields, including a Markdown governing link, without defining converted-card metadata. [4]
- Template guidelines keep keys and markers stable and adapt only comment syntax while preserving leading syntax and excluding the block from the digest. [5]
- The shared file-level template describes semantic parity and a self-sufficient source purpose. [6]
- The canonical skill identifies inline as an adapter and gives converted-card precedence over retained unconverted instructions. [7]
- The file-level workflow explicitly redirects converted memory instead of applying its retained metadata rules. [8]
- Converted cards use the mirrored prose/companion pair and owner-authored references and typed entries, not inline-template metadata. [9]
- Converted creation accepts temporary evidence tables; the workflow forbids legacy metadata/history and hand-authored references. [10]
