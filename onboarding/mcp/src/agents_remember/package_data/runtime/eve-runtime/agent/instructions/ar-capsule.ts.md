# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/instructions/ar-capsule.ts

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/instructions/ar-capsule.ts` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-17T10:20:31+00:00|
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview      | `../../../../../../../overview.md`         |

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/instructions/ar-capsule.ts`, produced by `scripts/sync-runtime.py` (the
`eve-runtime` target). Edit the authored file and re-run the generator.

## Code Commentary

### The application's capsule-facing instruction module

This module is the application side of the capsule path: it is where the eve application consumes the
capsule material the launch supplies. It is **not** the capsule compiler and **not** the canonical
corpus — the compiler lives in `application/role_capsules` and resolves its corpus from
`packaged_source_root()/runtime/skills`, and the launch supplies the compiled capsule through the
harness's own carrier.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/instructions/ar-capsule.ts` is the
  authored source.
- Application-side consumer only: it neither compiles the capsule nor owns the instruction corpus.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The compiler resolves its corpus from the packaged skills tree. | `shipped_composition_corpus` | mcp/src/agents_remember/application/skill_resources/provider.py:50-63 |
| The launch path compiles the capsule and supplies it through the harness's own carrier. | `compile_launch_capsule`; `capsule_channel_reason` | mcp/src/agents_remember/application/role_capsules/launch.py:273-294; mcp/src/agents_remember/serving/launch_capsule.py:251-272 |
| The generator declares the `eve-runtime` target with its per-target ignore set. | `TARGETS` | scripts/sync-runtime.py:61-78 |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: **created** for the packaged mirror this leaf
  adds as a generator target. The card records generated content and keeps the application-side
  consumer distinct from the compiler and the corpus. Verification metadata names the leaf base commit
  because the candidate is **uncommitted**; the real stamp is closeout-owned.
