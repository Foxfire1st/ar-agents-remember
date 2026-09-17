# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/lib/capsule.ts

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/lib/capsule.ts` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-17T10:20:31+00:00|
| lastVerifiedCommitHash | `58bf4cde0f5271bbe420ad8e045d18b433f11253` |
| lastVerifiedCommitDate | 2026-09-17T12:31:16+02:00|
| governingOverview      | `../../../../../../../overview.md`         |

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/lib/capsule.ts`, produced by `scripts/sync-runtime.py` (the `eve-runtime` target).
Edit the authored file and re-run the generator.

## Code Commentary

### Application-side capsule helper

A library helper of the AR-owned eve application, used by the application's instruction modules. It
is application code, not the capsule compiler and not the corpus: the compiler is
`application/role_capsules`, its corpus is `packaged_source_root()/runtime/skills`, and the launch
supplies the compiled capsule through the harness's own carrier.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/lib/capsule.ts` is the authored source.
- No corpus ownership and no compilation duty on the application side.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The compiler owns capsule compilation and resolves its corpus from the packaged skills tree. | `packaged_source_root` | mcp/src/agents_remember/application/skill_resources/operation.py:1-120 |
| The generator declares the `eve-runtime` target with its per-target ignore set. | `TARGETS` | scripts/sync-runtime.py:61-78 |

## Update History

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: **created** for the packaged mirror this leaf
  adds as a generator target. The card records generated content and names the authored source as the
  edit route. Verification metadata names the leaf base commit because the candidate is
  **uncommitted**; the real stamp is closeout-owned.
