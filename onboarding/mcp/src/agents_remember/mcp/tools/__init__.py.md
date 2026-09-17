# mcp/src/agents_remember/mcp/tools/__init__.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                               |
| path                   | `mcp/src/agents_remember/mcp/tools/__init__.py`  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-04T20:19:44+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[MCP tools overview](overview.md)

## Purpose

Facade that preserves the public import surface of the former `mcp/tools.py`.
L11 re-exports `task_reopen_payload` from `.task_doc` — the task-domain payload
module — not from `.worktree`.

## Code Commentary

### Logic

Re-exports the shared constants and `_tool_payload` from `base`, and every
`*_payload` builder from the domain submodules (`core`, `gates`, `lifecycle`,
`lifecycle_finalize`, `memory`, `operator_inbox`, `orchestration`, `providers`, `terminal`, `worktree`, `benchmark`,
`task_doc`). 260707-HFX-L8 adds `session_rename_payload`/`session_retire_payload` to the `terminal`
import block and `__all__`, exactly per the documented re-export pattern.
Task 25 keeps the split gate/block/wait builders re-exported for internal
compatibility and tests while making `lifecycle_gate_payload` the only public
agent-facing gate junction. `__all__` lists the full builder import surface, not
only the advertised MCP tools. 260713-TES-L4 adds `operator_inbox_supersede_payload` to the
`operator_inbox` import block and `__all__`, exactly per the documented re-export pattern.
260815-DAG-L16 adds `direct_landing_payload` to the import block and `__all__` per the same pattern.
260815-DAG-L15 adds `memory_quality_check_start_payload` / `memory_quality_check_poll_payload` to
the `memory` import block and `__all__` per the same pattern (the async quality surface, L15-R7).
260831-LOCR-L30 adds `worktree_checkpoint_landing_payload` to the `.worktree` import block and
`__all__` per the same pattern, so the partial-master landing builder is reachable from the package
boundary the registrar imports. 260831-LOCR-L37 adds `worktree_pause_payload` the same way (import
block at `:104`, `__all__` at `:196` inside the `:115-201` extent), so the stop's payload builder is
reachable from the same boundary as the publication's.

### Invariants And Boundaries

- Consumers import builders from `agents_remember.mcp.tools` regardless of which
  submodule owns them; the facade must keep re-exporting the full set.
- Re-exporting a builder here does not make it an advertised MCP tool; `server.py`
  and `PUBLIC_TOOLS` define that public surface.
- `_tool_payload` is re-exported with `from .base import _tool_payload as
  _tool_payload` so the conformance test's `tools._tool_payload` attribute
  access resolves and Ruff/Pyright treat it as an intentional re-export.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `gate_response_wait_payload` is imported from `gates`. | "from .gates import (" | mcp/src/agents_remember/mcp/tools/__init__.py:20-28 |
| `gate_response_wait_payload` is listed in `__all__`. | "__all__ = [" | mcp/src/agents_remember/mcp/tools/__init__.py:116-116 |
| The gate response wait payload builder is owned by the `gates` submodule. | `gate_response_wait_payload` | mcp/src/agents_remember/mcp/tools/gates.py:171-188 |
| The post payload builder is owned by the `operator_inbox` submodule. | `operator_inbox_post_payload` | mcp/src/agents_remember/mcp/tools/operator_inbox.py:20-37 |
| The poll payload builder is owned by the `operator_inbox` submodule. | `operator_inbox_poll_payload` | mcp/src/agents_remember/mcp/tools/operator_inbox.py:51-68 |
| The consume payload builder is owned by the `operator_inbox` submodule. | `operator_inbox_consume_payload` | mcp/src/agents_remember/mcp/tools/operator_inbox.py:71-86 |
| The inbox payload builders (post/poll/consume/supersede since 260713-TES-L4) are re-exported by this facade. | "from .operator_inbox import (" | mcp/src/agents_remember/mcp/tools/__init__.py:60-60 |
| The orchestration nudge payload builder is owned by the `orchestration` submodule. | `orchestration_nudge_manager_payload` | mcp/src/agents_remember/mcp/tools/orchestration.py:19-36 |
| The orchestration nudge payload builder is re-exported by this facade. | "from .orchestration import orchestration_nudge_manager_payload" | mcp/src/agents_remember/mcp/tools/__init__.py:66-66 |
| The lifecycle finalizer payload builder is owned by the `lifecycle_finalize` submodule. | `lifecycle_finalize_task_payload` | mcp/src/agents_remember/mcp/tools/lifecycle_finalize.py:15-32 |
| The lifecycle finalizer payload builder is re-exported by this facade. | "from .lifecycle_finalize import lifecycle_finalize_task_payload" | mcp/src/agents_remember/mcp/tools/__init__.py:45-45 |
| The terminal payload builders (`attach_terminal_session_to_task_payload`, `spawn_agent_session_payload`, `session_retire_payload`, `session_rename_payload`) are owned by the `terminal` submodule. | `attach_terminal_session_to_task_payload`, `spawn_agent_session_payload`, `session_retire_payload`, `session_rename_payload` | mcp/src/agents_remember/mcp/tools/terminal.py:27-44; mcp/src/agents_remember/mcp/tools/terminal.py:47-64; mcp/src/agents_remember/mcp/tools/terminal.py:67-84; mcp/src/agents_remember/mcp/tools/terminal.py:87-96 |
| The terminal payload builders are re-exported by this facade. | "from .terminal import (" | mcp/src/agents_remember/mcp/tools/__init__.py:90-90 |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

## 260815-DAG-L3 Queue Payload Export

The tool package now exports `closeout_queue_payload`, keeping the registered task-tool import on
the same curated payload surface as the other public MCP tools.

## 260815-DAG-L15 Async Memory-Quality Exports

The facade re-exports `memory_quality_check_start_payload` and `memory_quality_check_poll_payload`
(the async quality surface, L15-R7) from `.memory` in the import block and `__all__`, exactly per
the documented re-export pattern.

## 260821-CLIVE-L2 Current Contract

The current source seams include the module-level vocabulary. The public schema/composition layer exposes task-addressed controls plus explicit legacy and enclosure-adoption routes without private operation ids. Registration and payload building do not own journal state or compatibility decisions.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes the module-level vocabulary at this ownership boundary; the anchor is the stop builder's own `__all__` entry, which pins the list this claim is about. | "\"worktree_pause_payload\"," | mcp/src/agents_remember/mcp/tools/__init__.py:115-201 |
| The pause payload builder is re-exported by this facade from the `.worktree` import block and listed in the `__all__` extent, exactly per the documented pattern. | "from .worktree import (" | mcp/src/agents_remember/mcp/tools/__init__.py:88-110; mcp/src/agents_remember/mcp/tools/__init__.py:115-201 |

## 260821-CLIVE Closeout-Door Export

The tools package now exports `closeout_door_payload` alongside the disposable
`closeout_queue_payload`. The former publishes or observes canonical contract-owned scheduling
intent; the latter only reads/rebuilds its current projection. Exporting both does not merge their
authority or introduce a compatibility alias.

## MCAR-L02 Adapter Export

The package exports `curator_coherence_payload` alongside the existing task/door adapters so the
task registrar imports the one canonical payload boundary. This is wiring only; it creates no
second action implementation.

## 260831-CCR-L15 Status-Wait Export

**Superseded.** The `worktree_status_wait_payload` builder and its tool were removed; this facade
re-exports no wait payload today. Recorded so the paragraph above is not read as current.

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: "__all__ = [" repointed to mcp/src/agents_remember/mcp/tools/__init__.py:116-116. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "from .operator_inbox import (" repointed to mcp/src/agents_remember/mcp/tools/__init__.py:60-60. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "from .orchestration import orchestration_nudge_manager_payload" repointed to mcp/src/agents_remember/mcp/tools/__init__.py:66-66. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "from .terminal import (" repointed to mcp/src/agents_remember/mcp/tools/__init__.py:90-90. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T17:20:55+00:00: Generated citation repair: "__all__ = [" repointed to mcp/src/agents_remember/mcp/tools/__init__.py:115-115. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37 citation review (curator-authored, not a mechanical
  projection): re-read the `__all__` claim against the current source and re-cited it to the
  declaration itself, `"__all__ = ["` at `mcp/src/agents_remember/mcp/tools/__init__.py:115-201`, which
  is the list the claim names and the extent the L37 export extended. The wording holds unchanged; the
  previous range had arrived from a generated anchor-range projection, which is not evidence that a
  claim still holds.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: re-exported `worktree_pause_payload` from `.worktree` in
  the import block (`:104`) and `__all__` (`:196`), per the documented re-export pattern, and
  re-derived the `__all__` extent (`115-201`). Reference health: the
  `260831-CCR-L15 Status-Wait Export` section is marked superseded — the wait builder and its tool are
  gone. The facade contract this sidecar describes is unchanged. Verification metadata remains
  closeout-owned; no acceptance claim.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: re-exported `worktree_checkpoint_landing_payload`
  from `.worktree` in the import block and `__all__`, per the documented re-export pattern, and
  re-derived the `__all__` extents shifted by it. The facade contract this sidecar describes is
  unchanged. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "__all__ = [" repointed to mcp/src/agents_remember/mcp/tools/__init__.py:113-113. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "from .operator_inbox import (" repointed to mcp/src/agents_remember/mcp/tools/__init__.py:59-59. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "from .orchestration import orchestration_nudge_manager_payload" repointed to mcp/src/agents_remember/mcp/tools/__init__.py:65-65. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "from .lifecycle_finalize import lifecycle_finalize_task_payload" repointed to mcp/src/agents_remember/mcp/tools/__init__.py:45-45. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "from .terminal import (" repointed to mcp/src/agents_remember/mcp/tools/__init__.py:89-89. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `__all__` repointed to mcp/src/agents_remember/mcp/tools/__init__.py:113-197. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: "__all__ = [" repointed to mcp/src/agents_remember/mcp/tools/__init__.py:116-116. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): recorded the `worktree_status_wait_payload` package export.
- 2026-08-29T08:52+02:00 — Exported the sole curator-coherence payload adapter. Verification
  remains closeout-owned.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: documented the canonical closeout-door payload export. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-20T21:30+02:00 — 260815-DAG-L15: `memory_quality_check_start_payload` /
  `memory_quality_check_poll_payload` join the `memory` import block and `__all__` per the
  documented re-export pattern (L15-R7 async quality surface). Verified at code commit de3a0fd9.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: `direct_landing_payload` joins the facade imports and
  `__all__` per the documented re-export pattern; citation ranges regenerated for the L16 line
  movement. Verified at code commit a9d50e08.


- 2026-08-15T09:10+02:00 — L3 content update: recorded the closeout-queue payload export;
  verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current MCP-tool card for `__init__.py` with structural tool exposure and control-plane ownership boundaries.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded `operator_inbox_supersede_payload`
  joining the facade import block and `__all__` per the re-export pattern. Verification
  metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-03T02:32:19+02:00 — Curator W3-B02 repaired 7 Repo-Internal citation rows, including 14 manifest findings, with exact current builder anchors and repository-relative ranges; verification metadata was preserved.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-08T02:43+02:00 — No content impact: 260707-HFX-L8 adds `session_rename_payload`/
  `session_retire_payload` to the `terminal` import block and `__all__` exactly per the documented
  re-export pattern; the facade contract this sidecar describes is unchanged. Verification metadata
  pinned until closeout stamps the HFX-L8 commit.
- 2026-07-04T12:31+02:00 - L3: the new `orchestration` tools submodule joins
  the facade exports with `orchestration_nudge_manager_payload`, preserving the
  package-wide import surface pattern. Verification metadata pinned until
  closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — No content impact: L2 adds `spawn_agent_session_payload` to the `terminal`
  import block and `__all__` exactly per the documented re-export pattern; the facade contract this
  sidecar describes — re-export every `*_payload` builder regardless of owning submodule — is unchanged.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-03T00:30+02:00 — L11 re-exports `task_reopen_payload` from the task-domain payload module.
- 2026-07-02T17:04+02:00 — L9: the new `terminal` tools submodule joins the facade exports with
  `attach_terminal_session_to_leaf_payload`, preserving the package-wide import surface pattern.
  Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-27T22:00+02:00 — No content impact: task 28 adds `lifecycle_turn_end_notification_payload` (the NOTIFY-AND-CONTINUE turn-end builder) to the `lifecycle` import block and `__all__` exactly per the documented re-export pattern; the facade contract this sidecar describes — re-export every `*_payload` builder regardless of owning submodule — is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T14:16+02:00 — Task 25: documented that the facade still exports split gate/block/wait compatibility builders while the advertised MCP surface uses `lifecycle_gate` for live agent gate choreography.
- 2026-06-25T07:17+02:00 — Task 19: the `gates` submodule facade exports now include `gate_response_wait_payload` alongside create/decide/wait/list. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-23T22:50+02:00 — Dashboard task 14: the new `lifecycle_finalize` submodule joined the facade exports (`lifecycle_finalize_task_payload`). Verification metadata pinned until closeout stamps the source commit.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: the new `operator_inbox` submodule joined the facade exports (`operator_inbox_post_payload`/`operator_inbox_poll_payload`/`operator_inbox_consume_payload`). Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-18T01:05+02:00 — Task 6 slice 6a: the new `gates` submodule joined the facade exports (`gate_create_payload`/`gate_decide_payload`/`gate_wait_payload`/`gate_list_payload`); added it to the documented submodule list. Verification metadata pinned until closeout stamps the 6a code commit.
- 2026-06-13T22:34 — Slice 3c commit 1: the new `task_doc` submodule joined the facade exports (`task_doc_payload`); added it to the documented submodule list. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T16:41+02:00 — Slice 2b: the new `lifecycle` submodule joined the facade exports (the six `lifecycle_*` builders); added it to the documented submodule list. Verification metadata pinned until closeout stamps the 2b code commit.
- 2026-06-11T06:47+02:00 — No content impact: `direct_closeout_preview_payload`/`direct_closeout_apply_payload` left the facade exports (issue #62 worktree-only closeout) exactly per the documented re-export pattern; the facade contract this sidecar describes is unchanged.
- 2026-06-10T09:56+02:00 — No content impact: `worktree_sync_payload` joined the facade exports (GitHub #54 sub-task D) exactly per the documented re-export pattern; the facade contract this sidecar describes is unchanged.
- 2026-06-01T20:45+02:00 — Added `worktree_abandon_payload` to the tools-package facade exports for the new abandon tool.
- 2026-05-29T18:35+02:00: Created as the package facade when `mcp/tools.py` was split (commit `01f503d`).
