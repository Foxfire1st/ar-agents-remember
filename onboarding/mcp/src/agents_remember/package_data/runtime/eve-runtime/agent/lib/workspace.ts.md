# mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/lib/workspace.ts

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/eve-runtime/agent/lib/workspace.ts` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-17T10:20:31+00:00|
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview      | `../../../../../../../overview.md`         |

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored
`eve_runtime/agent/lib/workspace.ts`, produced by `scripts/sync-runtime.py` (the `eve-runtime`
target). Edit the authored file and re-run the generator.

## Code Commentary

### Application-side workspace helper

A library helper of the AR-owned eve application that locates the agent's workspace for the
application's tools. It is application code inside the installed image
(`<coordination_root>/runtime/eve-agent`); the admitted workspace address remains the launch's and
the control plane's, not an application-side invention.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/agent/lib/workspace.ts` is the authored source.
- Helper only: the admitted workspace address stays launch- and control-plane-owned.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The launch records the admitted workspace and seat rather than letting a consumer re-derive them. | `_compile_eve_task`; `AdmittedTaskSeat` | mcp/src/agents_remember/application/role_capsules/launch.py:362-404; mcp/src/agents_remember/application/role_capsules/launch.py:108-122 |
| The generator declares the `eve-runtime` target with its per-target ignore set. | `TARGETS` | scripts/sync-runtime.py:61-78 |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: **created** for the packaged mirror this leaf
  adds as a generator target. The card records generated content and names the authored source as the
  edit route. Verification metadata names the leaf base commit because the candidate is
  **uncommitted**; the real stamp is closeout-owned.
