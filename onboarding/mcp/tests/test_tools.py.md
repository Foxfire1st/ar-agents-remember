# test_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_tools.py`                  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-18T14:57+02:00 |
| lastVerifiedCommitHash | `0dd04d6adbca3e8ba61849b605ece3137005829e` |
| lastVerifiedCommitDate | 2026-09-18T15:05:30+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l3-ar` uncommitted source (`mcp/tests/test_tools.py` **364 → 468 lines**, 10 → **12** cases); base `a12c511f6e76bd1188719cad0a9104d78d46920c` |
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks ping and safe server-info payloads, memory-initialization authority repair after config-write failure, and typed CGC/grepAI input refusal before provider execution. Since 260831-LOCR-L29 it also holds the public-surface inventory contract: the live registration order must equal `PUBLIC_TOOLS`, and every advertised name must have a response model that validates; 260831-LOCR-L30 added the per-tool response-model case for the checkpoint landing tool, 260831-LOCR-L36 added the case that pins that tool's **published description** — it must present a partial publication and deny being the pause — and 260831-LOCR-L37 added the matching case for the stop: `worktree_pause`'s description must present a stop that publishes NOTHING and must name `worktree_checkpoint_landing` as the separate, explicitly requested PUBLICATION. 260831-LOCR-L38 extended that stop case so the description must also stay true about a master holding no selection: the removed `atomic-series-activation-selection-missing` refusal is pinned **out** of the registered text and the release the description still advertises is pinned **in**, so the absence cannot be satisfied by emptying the text. These cases establish payload behavior with controlled configuration; the registration probe builds no runtime and no live provider is exercised. Since `260918-TSIP-L3` it also holds the **curator-coherence publish contract** (`T50`): one case compares the registered `curator_coherence` description against the nine fields the validator actually requires and pins that the JSON schema cannot carry the requirement, and its pair drives a real `publish` request once per omitted field — with the complete shape accepted first as the positive control — asserting the refusal names exactly the field it dropped.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Ping payload | `test_ping_payload` | mcp/tests/test_tools.py:60-70 |
| Server info payload reports safe config summary | `test_server_info_payload_reports_safe_config_summary` | mcp/tests/test_tools.py:71-117 |
| Memory init repairs authority after config write failure | `test_memory_init_repairs_authority_after_config_write_failure` | mcp/tests/test_tools.py:118-154 |
| Typed cgc payloads reject invalid inputs before provider execution | `test_typed_cgc_payloads_reject_invalid_inputs_before_provider_execution` | mcp/tests/test_tools.py:155-166 |
| Grepai payloads reject invalid scope and trace inputs | `test_grepai_payloads_reject_invalid_scope_and_trace_inputs` | mcp/tests/test_tools.py:167-197 |
| Live FastMCP registration order equals the advertised public tuple | `test_live_registration_matches_the_public_inventory_in_order` | mcp/tests/test_tools.py:232-241 |
| The record-landing tool has a registered response model that validates | `test_worktree_record_landing_has_a_response_model_that_validates` | mcp/tests/test_tools.py:243-261 |
| The checkpoint-landing tool has a registered response model that validates, which the set comparison alone cannot establish | `test_worktree_checkpoint_landing_has_a_response_model_that_validates` | mcp/tests/test_tools.py:263-282 |
| The checkpoint description presents a partial publication and denies being the pause: it says `PUBLISH`, says "not a pause", says pausing is a "separate matter and is NOT this call", and no longer opens with "Use this to pause". | `test_the_checkpoint_description_publishes_rather_than_pausing` | mcp/tests/test_tools.py:284-306 |
| The pause description presents a stop that publishes NOTHING, names the checkpoint landing as the separate publication, and — since the already-vacant stop — advertises no refusal the verb no longer performs while still naming the release it does perform. | `test_the_pause_advertises_a_stop_that_publishes_nothing` | mcp/tests/test_tools.py:308-343 |
| The description names every field `curator_coherence`'s `publish` requires, and pins that the JSON schema cannot carry the requirement. | `test_the_description_names_every_field_publish_requires` | mcp/tests/test_tools.py:391-410 |
| `publish` refuses by naming **every** missing field, one omission per field with the complete-shape acceptance as the positive control. | `test_publish_refuses_by_naming_every_missing_field` | mcp/tests/test_tools.py:412-450 |
| The one list both pins compare — the nine publish-required fields, spelled once. | `PUBLISH_REQUIRED_FIELDS` | mcp/tests/test_tools.py:351-368 |
| The permissive registration-time config stub the registration cases build against | `_permissive_registration_config` | mcp/tests/test_tools.py:453-464 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Public-Surface Inventory Coverage (260831-LOCR-L29)

`PublicSurfaceInventoryTests` exists because the advertised surface's own agreement was unenforced.
`server_info` reports `mcp.tools.PUBLIC_TOOLS` itself, so a case that reads that payload and compares
it to the tuple is self-referential. `worktree_record_landing` shipped registered by
`mcp/registration/closeout.py`, advertised by FastMCP, and absent from both `PUBLIC_TOOLS` and
`TOOL_RESPONSE_MODELS`, and the suite stayed green while `finalize_tool_response`'s by-name registry
lookup made the tool unable to return a payload at all.

`test_live_registration_matches_the_public_inventory_in_order` registers every entry in
`TOOL_REGISTRARS` against a probe `FastMCP("inventory-probe")` and compares the
`asyncio.run(server.list_tools())` names to `PUBLIC_TOOLS`. The comparison is ordered because
FastMCP publishes in registration order, so a misplaced row is a reordering bug rather than a
missing one. `test_worktree_record_landing_has_a_response_model_that_validates` asserts
`set(PUBLIC_TOOL_RESPONSE_MODELS) == set(PUBLIC_TOOLS)` and then drives one
`finalize_tool_response("worktree_record_landing", ...)` call — the call a missing registry row
raises on, which the surface comparison alone cannot see.

`_permissive_registration_config()` is the stub both cases need. Every registrar only closes over
the config and none validates it while registering, so a permissive chain keeps these cases about
the inventory rather than about building a runtime. The probe starts no server process, reads no
provider state, and reaches no network.

### Why There Is A Case Per Landing Tool (260831-LOCR-L30)

`test_worktree_checkpoint_landing_has_a_response_model_that_validates` exists because the L29 case's
set comparison cannot distinguish the two landing envelopes: `worktree_checkpoint_landing` and
`worktree_record_landing` sit adjacent in `TOOL_RESPONSE_MODELS` and declare the same field names
apart from the operation literal, so a registry swap between them still validates as a set. The L30
case drives `finalize_tool_response("worktree_checkpoint_landing", …)` with the checkpoint payload
(`state: "checkpointed"`, `integratedCodeCommit`, empty memory and ledger commits) and asserts the
returned operation, which is what pins the name to the model that declares its literal.

The general rule the two cases establish: one validating call per public tool name, not one for the
whole registry.

### The Stop's Half Of The Split (260831-LOCR-L37)

`test_the_pause_advertises_a_stop_that_publishes_nothing` is the L36 case's counterpart, and the two
are deliberately a pair. The checkpoint case pins the publication's side of the split; this one pins
the stop's. It registers every registrar against a probe `FastMCP("pause-surface-probe")`, reads the
advertised descriptions, and asserts that `worktree_pause` is a `PUBLIC_TOOLS` member, that
`worktree_checkpoint_landing` is too, and that the stop's text says all three things an agent needs:
that it is a pause of an atomic master, that it **publishes NOTHING**, and that the publication it
must not reach for is named and separate.

Neither case would catch the other's regression. The L36 case cannot see the stop's wording because
it reads only the checkpoint's text, and a description-only edit is invisible to the set comparison
and to the per-name response-model cases. Together they are what makes "two registered tools, not one
verb with two names" an enforced claim rather than a comment.

**The stop case also pins what the description must not say (260831-LOCR-L38).** The pause used to
refuse a master holding no selection with `atomic-series-activation-selection-missing`; it now reports
that master as already stopped, so a registered description still advertising the removed refusal
would describe a tool the caller does not have. The case asserts the identifier is absent — both the
full status and the `selection-missing` fragment — and, in the same case, that
`releases the master's atomic-series activation selection` is still present. The positive half is the
load-bearing one for this check: without it, deleting the description would satisfy the absence. This
is an advertisement pin, not a behavioural one — the behaviour is proved in
`test_pause_stop_only_end_to_end.py` — and it pins the absence, so it constrains no production edit
other than re-advertising a status the verb no longer returns.

## The Curator-Coherence Publish Contract (260918-TSIP-L3)

`CuratorCoherencePublishContractTests` exists because **the published contract and the enforced
contract disagreed, and neither surface could show it** (`T50`). `curator_coherence`'s `publish` was
refused twice on a real curator with *"publish requires every identity, predecessor, and caller
field"* although every field the registered description named had been supplied. The validator
(`models/lifecycles/curator_coherence.py:294-328` `_action_has_one_input_shape`) requires **nine**
non-null fields, and the description named neither `semantic_requirement_revision` nor
`delivery_attempt` nor `caller` as required; the refusal named a class of fields and none of them,
and a model-level validator reports `loc: ()`, so the message was the caller's only route to the
missing field. Two disagreements, pinned separately because either can regress alone:

- `test_the_description_names_every_field_publish_requires` registers every `TOOL_REGISTRARS` entry
  against a probe `FastMCP("curator-coherence-description-probe")`, reads the advertised
  `curator_coherence` text, and asserts each of the nine names appears in it. In the same case
  `CuratorCoherenceRequest.model_json_schema()["required"]` must stay
  `["action", "contract_path"]` — **the schema cannot carry the requirement**, because it is
  conditional on `action == "publish"`, and the pin stops someone "moving the repair into the
  schema" on the assumption that it could.
- `test_publish_refuses_by_naming_every_missing_field` builds the complete nine-field request and
  asserts it is accepted **first**, as the positive control: without that arm a mistyped field name
  would make every later assertion pass for a reason unrelated to the repair. Then, one omission per
  field, it asserts `missing: <field>` is in `errors()[0]["msg"]` — never `str(error)`, because the
  rendered error echoes `input_value` and a substring check against the echo reports "named" for a
  message that names nothing, which is the instrument fault this case exists to catch.

`PUBLISH_REQUIRED_FIELDS` spells the nine once so both arms compare against one list. The two cases
belong to the **integration** lane because that is where the two existing published-description pins
live; the module was already registered, so this leaf added no lane row and **no line of
`mcp/tests/test-evidence-lanes.toml` moved**.

## Update History
- 2026-09-18T14:57+02:00 — 260918-TSIP-L3 curator (uncommitted change set on `ar/260918-tsip-l3-ar`,
  base `a12c511f`): this file is one of the leaf's five changed paths, so the card gained a **body**
  update rather than a restamp. Added the `## The Curator-Coherence Publish Contract (260918-TSIP-L3)`
  section, the Purpose sentence, and **three reference rows** for the two new cases and the
  `PUBLISH_REQUIRED_FIELDS` list they share; **eleven retained rows moved +2** (two one-line
  insertions above them) and were re-derived against the new bytes. **One row was re-scoped rather
  than moved:** `_permissive_registration_config` was cited as `:344-359`, and the 102-line insertion
  this leaf makes at old `:348` now lies *inside* that range — so a prefix-preserving move would have
  produced `:346-463`, a range naming the previous case's tail, the whole new publish-contract block
  and the stub at once (the one-anchor-two-extents shape the shipped fixer declines). It now cites
  the stub's own extent, `:453-464`, which is the only place its anchor resolves. The three earlier
  history entries that quote the old numbers are as-of records and are deliberately not renumbered.
  `lastUpdated` advances with this body edit; `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are
  deliberately unchanged because the candidate is uncommitted and the governed closeout owns the real
  code commit.
- 2026-09-15T13:18+02:00 — 260831-LOCR-L38 verification envelope (uncommitted change set on
  `ar/260831-locr-l38`, base `67b21aeb`): extended the existing stop case
  `test_the_pause_advertises_a_stop_that_publishes_nothing` — no new case, so the module's case count
  and the integration population are unchanged — with the requirement-9 pin. The registered
  `worktree_pause` description must carry neither `atomic-series-activation-selection-missing` nor the
  `selection-missing` fragment, and must still say
  `releases the master's atomic-series activation selection`, so the absence cannot be satisfied by an
  emptied description. Recorded that this is an advertisement pin whose premise is
  **preserved-false**: no registered description ever advertised the removed refusal (the docstring is
  changed only by this leaf's own text pin plus L37's registration), so the case pins the absence
  rather than repairing a live text. Re-derived the shifted ranges (the stop case is now `306-341`,
  `_permissive_registration_config` `344-359`, the live-registration case `230-239`).
  Verification metadata remains closeout-owned; no verification stamp advanced and no acceptance
  claim.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: recorded the new case
  `test_the_pause_advertises_a_stop_that_publishes_nothing`, which pins the stop's published
  description (a pause of an atomic master, "Publishes NOTHING", and the checkpoint named as the
  separate, explicitly requested publication) and both roster memberships, and recorded why it is the
  L36 checkpoint case's counterpart rather than a duplicate. Re-derived the retained-test and stub
  ranges (`_permissive_registration_config` 332-347). Verification metadata remains closeout-owned; no
  execution or acceptance claim.
- 2026-09-13T18:07+02:00 — 260831-LOCR-L36: recorded the new case
  `test_the_checkpoint_description_publishes_rather_than_pausing`, which registers every tool against
  a probe `FastMCP` and pins the checkpoint description: it must present a partial **publication** and
  deny being the pause (no "Use this to pause", and the pause is named as a "separate matter and is NOT
  this call"). The case exists because the old invitation routed an ordinary stop request into a
  protected-branch publication. Rebound `_permissive_registration_config` to its current range.
  Verification metadata remains closeout-owned; no execution or acceptance claim.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: added the
  `test_worktree_checkpoint_landing_has_a_response_model_that_validates` case, recorded why a per-name
  case is required (the two landing envelopes differ only in the operation literal, so a set
  comparison misses a swap), corrected the Purpose sentence, and re-derived the shifted retained-test
  and stub ranges. Verification metadata remains closeout-owned; no execution or acceptance claim.
- 2026-09-12T01:41:08+02:00 — 260831-LOCR-L29 public-surface repair: recorded
  `PublicSurfaceInventoryTests` (live-registration-order equality with `PUBLIC_TOOLS`, plus a
  validating `finalize_tool_response` call for `worktree_record_landing`) and its
  `_permissive_registration_config` stub, corrected the Purpose sentence that claimed this module
  had no registration coverage, repointed all five shifted retained-test ranges after the import
  block grew, and added the three new reference rows. Verification metadata remains closeout-owned;
  no execution or acceptance claim.

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-30T17:08:05+02:00 — ARSPAWN-L4 Dagger repair: the unit fixture now passes the strict
  payload expected by the transport-thin builder. Verification remains closeout-owned.

- 2026-08-30T15:15:36+02:00 — ARSPAWN-L4 pins the complete shared serving-build payload in
  `server_info`. Verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: added closeout_queue to the public tool census;
  verification remains closeout-owned.

- 2026-08-13T09:05+02:00 — L23 curator: reviewed the runtime-install import move and confirmed the
  tool regression contract is unchanged; final provenance remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_tools.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T03:07:44+02:00 — W3-B05 curator: resolved 7 Tier-2 table findings with exact anchors and source paths; fixer generated all final ranges.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 code-quality gate: the provider, memory, and benchmark
  payload builders moved their loose keywords into parameter objects, so the GrepAI and CGC cases
  now pass `GrepaiSearchQuery` / `GrepaiTraceQuery` / `GrepaiRepoScope` and a module-level
  `DRY_RUN_SCOPE = ProviderQueryScope(dry_run=True)` instead of `dry_run=True`, carryover planning
  passes a `CarryoverSelection`, and the benchmark sandbox case passes a `CodexBenchmarkRun`.
  Corrected the `dry_run` paragraph, which still claimed the CGC test passes `dry_run=True` per
  call, and added a paragraph naming the parameter objects. Two further real changes are now
  recorded in Invariants: `RealMcpIntegrationTests` gained
  `@pytest.mark.agents_remember_real_mcp_config` on top of its `AGENTS_REMEMBER_REAL_MCP_CONFIG`
  skip, and its `--workspace` assertion stopped comparing against the stale literal
  `agents-remember-memory`, deriving the expected value from `grepai_workspace(load_config(...))`
  instead. No test case was added, removed, or renamed.

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental curator: added the public closeout-description
  regression contract for mandatory CRAP, quality-before-mutation, and approval-before-apply;
  verification remains pinned until the code commit.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-04T11:10+02:00 — L2: the expected public-tool subset now includes `spawn_agent_session`,
  pinning the agent-facing session-dispatch surface in `PUBLIC_TOOLS` beside
  `attach_terminal_session_to_leaf`. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-02T17:04+02:00 — L9: public-tool coverage now expects
  `attach_terminal_session_to_leaf`, pinning the new agent-facing hosted chat reassignment surface in
  `PUBLIC_TOOLS`. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-02T15:40+02:00 — The typed CGC command-construction assertions now
  expect `cgc_dependencies_payload(..., dry_run=True)` to expose
  `analyze deps <module>`, matching the current CodeGraphContext CLI.
- 2026-06-26T14:16+02:00 — Task 25: public tool expectations now include `lifecycle_gate` and assert the retired split helpers are absent from `PUBLIC_TOOLS`.
- 2026-06-25T07:17+02:00 — Task 19: added `gate_response_wait` to the expected public-tool surface. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: `test_phase_04_tools_are_reported` now expects `operator_inbox_post`, `operator_inbox_poll`, and `operator_inbox_consume`; the existing public-description smoke test covers their server docstrings. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-06-11T06:47+02:00 — `test_phase_04_tools_are_reported` no longer expects `direct_closeout_preview`/`direct_closeout_apply` (issue #62 worktree-only closeout removed the tools from `PUBLIC_TOOLS`).
- 2026-06-10T05:30+02:00 — Diagnostics/watchers tool tests assert the S4 compact wire shape: rawStatus/currentState bodies absent inline, present in the `reportPath` file, `currentStateFile` still on disk.
- 2026-06-02T04:40+02:00: Updated the skills_install payload tests for the flat installer — dropped the `layout == "tree"` assertion and replaced the legacy-namespace-symlink test with a per-skill flat-destination symlink-replacement test. `l-01-session-job-lifecycle` skill series, Sub-task B/S7, mcp 1.1.0.
- 2026-06-02T02:00+02:00 — Added `test_grepai_search_resolves_uppercase_repo_id_to_normalized_project`: a configured uppercase repo id (`Cobalt`) is queried as `--project cobalt` and accepted in any casing. Updated Code Commentary.
- 2026-05-31T12:50+02:00 — `test_ping_payload` now asserts `payload["version"] == SERVER_VERSION` (imported from `agents_remember.mcp`) instead of the `0.9.6` literal; the Codex benchmark policy test flips the fixed default to `default`/`omitted` and asserts `danger-full-access` separately; added `test_codex_benchmark_tools_refuse_when_disabled`; removed the three Docker-mode `test_provider_integrity_ignores_*` cases and their `check_provider_runner_integrity`/`manifest_path_for_config` imports. Corrected the version-assertion, Codex benchmark, and provider-integrity prose to match (1.0.0 review remediation).
- 2026-05-31T01:06+02:00: Updated `test_ping_payload`'s version assertion to `0.9.6` (MCP 0.9.6, `w-02-light-task-workflow` skill design section). Verification metadata stays pinned until closeout commits the change.
- 2026-05-30T22:29+02:00: Updated `test_ping_payload` for the S6 token-counter wiring — it now asserts populated `tokens`/`tokenizer`/`tokenCountExact` instead of the zero defaults, and the version assertion moved to `0.9.5`. Typed the `fake_run` stub against `RuntimeInstallRequest` (with its import) to clear a Pyright error. Verification metadata stays pinned until closeout commits the change.
- 2026-05-30T21:51+02:00: Documented the new coverage — every public tool must register a description, and `runtime_install_payload` exposes/forwards `no_cache` (default `False`). Repaired the stale `tools.py` reference to the split `mcp/tools/` package. Verified against `57944df`.
- 2026-05-29T21:00+02:00: Updated the `ping_payload()` version assertion to MCP release `0.3.0`.
- 2026-05-29T20:25+02:00: Updated after the `skills_install`/`route_index_refresh`/`memory_init` payload tests moved to act-by-default assertions and the typed CGC command-construction test pinned `dry_run=True` (`dry_run`-default flip task).
- 2026-05-28T19:52+02:00: Updated after public tool payloads began validating through Pydantic response models and `ping_payload()` started emitting token metadata defaults.
- 2026-05-28T15:43+02:00: Updated after `ping_payload()` version expectations moved to MCP release `0.2.0`. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-28T12:32+02:00: Updated after MCP tool tests added provider watcher status current-state coverage.
- 2026-05-26T23:11+02:00: Refreshed verification metadata after source commit `5ab704a` landed GrepAI MCP command-shape and real stdio integration coverage.
- 2026-05-26T22:54+02:00: Updated after GrepAI search/trace unit tests and gated real MCP stdio integration tests covered the new tool shape.
- 2026-05-26T12:51+02:00: Updated after provider integrity stopped treating CodeGraphContext host venvs as authority because CGC is Docker-owned.
- 2026-05-25T19:16+02:00: Updated after service tests patched `providers.lifecycle.main` directly and the `provider_lifecycle.py` compatibility module was deleted.
- 2026-05-25T18:07+02:00: Updated after provider integrity removed `_bin` from current runner authority and kept old `_bin` manifest entries ignored.
- 2026-05-25T17:40+02:00: Updated after provider integrity tests switched the blocking case to CGC runner state and added Docker-mode legacy GrepAI binary/current-manifest ignore coverage.
- 2026-05-24T19:25+02:00: Added regression coverage that provider runner integrity failures block CGC query and watcher execution before lifecycle services run.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` covered `.codex` skill roots and benchmark sandbox payloads.
- 2026-05-24T09:23+02:00: Updated after MCP tool tests moved normal harness-root fixtures from `.agents` to Codex `.codex`.
- 2026-05-24T08:56+02:00: Updated after missing-Codex benchmark payload coverage began asserting `sandboxArgument` for fixed and default sandbox modes.
- 2026-05-24T06:57+02:00: Updated after missing-Codex benchmark payload tests began asserting explicit benchmark-only `PATH` resolution policy.
- 2026-05-24T02:47+02:00: Updated after public tool expectations added `memory_quality_check`.
- 2026-05-24T00:35+02:00: Added regression coverage that service-backed MCP tools no longer expose command-capture artifacts.
- 2026-05-23T20:56+02:00: Added regression coverage that MCP provider tools do not route through the provider lifecycle CLI main.
- 2026-05-23T20:42+02:00: Added typed CGC public-tool and fixed command-shape coverage.
- 2026-05-23T18:05+02:00: Created during direct closeout prep for public MCP tool test coverage.
