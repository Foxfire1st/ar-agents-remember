# mcp/src/agents_remember/application/runtime/startup.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/runtime/startup.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T19:24+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted source; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Initializes MCP-process application collaborators and owns the one application-layer gateway that
hands the MCP adapter its boot-resolved serving-build payload. Since `260915-KS-L23` it also owns the
**ruler stamp** the measuring surfaces carry, so a memory-quality or citation count says which build
produced it.

## Code Commentary

### Logic

`initialize_mcp_application` migrates recognized durable logs without the dashboard-owned notifier
log, then installs ambient lifecycle state. `mcp_serving_build_payload` converts the cached serving
stamp to the strict shared wire model at the application boundary; MCP registration never imports
the serving domain directly. Dashboard autostart remains a separate startup hook.

`measuring_build_stamp` (`:36-51`) is the second reader of that same process-cached identity, and it
exists because of the measurement D-33 recorded: the MCP surface answers a tool call from a **fixed**
serving build while the candidate under curation may carry different code, and until this stamp existed
a checklist reader could not tell a candidate-ruler count from a serving-build-ruler count. It returns
`{"servingBuild": <resolved payload as wire JSON>}` — a dict copy of the identity
`process_serving_build()` resolved once per process, not a probe — with `dirty` riding along so an
uncommitted serving tree reads as such instead of being taken for the commit it names. Its consumers are
the memory-quality controller's three public entry points and the two citation tools; the omission of
`drift_check` is deliberate, because a tree-integrity count is not a curation count.

### Conventions

Migration runs before any strict store can parse current records; ownership boundaries determine
which process may migrate which log.

### Invariants And Boundaries

- Migration is one-way, idempotent deployment work.
- MCP startup does not mutate the dashboard-owned notifier log.
- No dual-schema reader is installed.
- MCP transport reaches serving identity through this application entry point only.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| MCP startup migrates its owned logs before ambient installation. | `initialize_mcp_application` | mcp/src/agents_remember/application/runtime/startup.py:22-27 |
| The application boundary returns the one cached, strict serving-build payload. | `mcp_serving_build_payload` | mcp/src/agents_remember/application/runtime/startup.py:30-33 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-09-18T19:24+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **recorded the second serving-build reader this leaf's item 26 added, which this card did not mention.** `measuring_build_stamp` (`:36-51`) returns the process's resolved boot identity as `{"servingBuild": …}` wire JSON — a dict copy of the identity `process_serving_build()` caches once per process, `dirty` included — and is consumed by the memory-quality controller's three public entry points and by `citation_fix_tool`/`citation_migrate_tool`; the Purpose and `### Logic` sections now state it and its reason (D-33: a fixed serving build measuring a different candidate, indistinguishable in the output). It is a stamp, not a second resolution, and it does not move `initialize_mcp_application` or `mcp_serving_build_payload`. Read against the delivered but **uncommitted** working tree, so the verification stamp is not advanced: no commit carries these bytes and closeout owns the real stamp; the reference rows are left to the citation-range repair pass that owns them.
- 2026-08-30T17:08:05+02:00 — ARSPAWN-L4 Dagger repair: added the application-owned serving-build
  payload gateway so MCP transport no longer imports the serving domain directly. Verification
  remains closeout-owned.

- 2026-08-13T08:40+02:00 — L23 integration-gate repair: moved this preserved startup card with its source into the cohesive `application/runtime/` package and rebound all current citations; startup behavior is unchanged. Verification metadata remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current application-layer card for `server_startup.py` with qualified seat resolution and terminal/session orchestration boundaries.
- 2026-08-10T18:31+02:00 — 260731-EFA-L21: split out the idempotent pre-config MCP trust
  declaration while preserving `prepare_mcp_process` as the supervision operation. Verification
  metadata remains pinned until approved closeout.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
