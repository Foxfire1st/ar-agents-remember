# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/instructions.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/instructions.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-17T10:20:31+00:00|
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview      | `../../../../../../overview.md`            |

## Governing Overview

[overview.md](../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/instructions.md`, produced by `scripts/sync-runtime.py` (the `eve-runtime`
target). Edit the authored file and re-run the generator.

## Code Commentary

### The eve application's own instruction entry

This is the top-level instruction document of the AR-owned eve application — the text the agent
definition loads — and it is distinct from, and not a substitute for, the **capsule** instruction
corpus the compiler delivers. The capsule corpus is resolved by
`application/skill_resources` from `packaged_source_root()/runtime/skills`; this file belongs to the
eve application and travels with it into `<coordination_root>/runtime/eve-agent`.

The distinction matters for the cutover: withholding the legacy coordinator `AGENTS.md` chain does
not touch this file, and installing the eve application does not deliver the capsule corpus.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/instructions.md` is the authored source.
- It is the eve application's instruction entry, not the capsule corpus and not a legacy startup
  target.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The compiler resolves its corpus from the packaged skills tree, not from this application's instructions. | `shipped_composition_corpus` | mcp/src/agents_remember/application/skill_resources/provider.py:50-63 |
| The startup targets the capsule mode withholds are the coordinator `AGENTS.md` chain, not this file. | `WITHHELD_STARTUP_TARGETS` | mcp/src/agents_remember/install/experiment.py:103-118 |
| The generator declares the `eve-runtime` target with its per-target ignore set. | `TARGETS` | scripts/sync-runtime.py:61-78 |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: **created** for the packaged mirror this leaf
  adds as a generator target. The card records generated content, the authored source, and the
  boundary between the eve application's instruction entry and the capsule corpus. Verification
  metadata names the leaf base commit because the candidate is **uncommitted**; the real stamp is
  closeout-owned.
