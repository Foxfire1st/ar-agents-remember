# mcp/tests/test_mcp_registration_wiring.py

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/tests/test_mcp_registration_wiring.py` |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `a89a6fc88d9330eb2749c87b3dcc3f6c4e46c4bd`  |
| lastVerifiedCommitDate | 2026-08-14T12:44:51+02:00|
| governingOverview      | `overview.md`                               |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

What each advertised MCP tool **does with the arguments it is handed**.

`agents_remember.mcp.registration` is the tool surface: one module per family, each
declaring `@server.tool()` bodies that translate a flat MCP argument list into the
parameter objects the application entry points take. `test_tools.py` proves the surface *advertises* the
right names; nothing proved what a call to one of those names actually does.

That translation is the whole content of these bodies, and it is exactly where a split goes
wrong: an argument dropped on the floor, a flag landing in the wrong parameter object, a
default that silently changes what a call means. This module exists because 163 parameter
objects were introduced across the codebase — the registration layer is where the flat wire
schema meets them.

260731-EFA-L7 (trace delta): the registration-wiring suite was split in place into `test_mcp_registration_wiring_tests_1.py` / `_2.py`; this card remains the family entry.
## Method

Each test calls the tool **through the live `FastMCP` instance**, so the registered schema,
its defaults and its coercions are all in the path. One live server per test, with the
family's payload builder replaced by a `Recorder` (stands in for a payload builder and
remembers the one call it received). Each test states what the builder is handed and that
the tool returns its result unchanged.

## The Defaults That Are Load-Bearing

Several tests exist because the *default* is the security or cost property:

- `codex_benchmark_prepare` / `codex_benchmark_run` default to a **preview**, not a real
  run — a real prepare clones repositories.
- `runtime_install` defaults to a real install with the layer cache and no benchmark
  fixtures.
- `gate_decide` attributes a plain decision to the model via `cli`; with a deciding role it
  must **not** claim to be the model's own cli decision — `by` is left for the server to
  fill from the role and `via` becomes `orchestration`.
- `operator_inbox_post` over MCP is **always** attributed to the model, fixed here rather
  than taken from the caller, so an agent cannot post as the developer.
- `lifecycle_gate` with `wait=False` must raise with a wait that says so rather than
  inheriting `GateWait`'s blocking default of 300 seconds.
- `spawn_agent_session` must arrive with every retired spend control **unset**, so the
  refusal path is never triggered by the wiring itself.
- `orchestration_nudge_manager` keeps the manager being nudged and the seat the nudge is
  about distinct — collapsing them nudges the wrong mailbox.
- `session_retire` keeps the retiring seat's own id and the target id distinct, because
  authority is checked against `actor_session_id`.

## The Parameter-Object Splits Pinned Here

`resolve_context` (`TaskRef` holds repo/task/leaf/parent/contract; worktree name and
topology override stay separate), `spawn_agent_session` (three declared groups: the seat,
the retired spend controls, the spawner), `worktree_start` (identity / bases / execution),
`closeout_apply` (`CloseoutApproval` is the gate-bearing half — folding it into the commit
messages would let a dry run read as an approved apply), `task_doc` (document target vs.
the edit itself), `memory_carryover_plan` (one `CarryoverSelection`), `grepai_search`
(query / repo scope / execution scope), `operator_inbox_post` (address / message / poster /
delivery), `lifecycle_finalize_task` (the documents it ticks).

`lifecycle_*` payloads act on the process-wide **ambient** lifecycle: the registrar takes
the config only to keep one signature, and these six must be called without it.

## Invariants And Boundaries

- Tests go through the real server, never by calling the tool function directly — the
  registered schema and its coercions are part of what is under test.
- Only the payload builder is doubled; no application entry point runs.
- This module is the behavioural companion to `test_tools.py`'s name/description surface,
  and to `test_code_quality_check.py::ToolSignatureExemptionTests`, which proves every
  function under `registration/` is a published tool declaration.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The tool surface under test: one module per family of `@server.tool()` declarations. | `TOOL_REGISTRARS` | mcp/src/agents_remember/mcp/registration/__init__.py:35-48 |
| The advertised-surface companion (names, descriptions, response conformance). | `test_every_public_tool_has_a_description` | mcp/tests/test_tools.py:138-152 |
| The AST test that keeps the `PLR0913` exemption over `registration/` honest. | `ToolSignatureExemptionTests` | mcp/tests/test_code_quality_check.py:512-588 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 citation maintenance: refreshed the shifted tool-
  exemption proof; registration wiring behavior is unchanged.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T23:35:00+02:00 — 260731-EFA-L7 curator (trace delta): body verified against the current code and updated (260731-EFA-L7 (trace delta): the registration-wiring suite was split in place into `test_mcp_registr...). Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-03T04:32:19+02:00 — W3-B08 curator: curated 6 citations (citation_anchor_missing=3, citation_prose_not_in_cit_form=0, citation_source_malformed=3); final scoped citation check clean.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  registration-wiring suite. Verification metadata is pinned to the leaf's reformat commit
  until closeout stamps the code commit.
