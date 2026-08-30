# test_wire_vocabulary_exhaustiveness.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_wire_vocabulary_exhaustiveness.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `346507af24396ab7b491e02511c4af006ccd3dc5` |
| lastVerifiedCommitDate | 2026-08-30T07:51:57+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The 260731-EFA-L4 central guard: **every value a producer can emit must validate at the wire
boundary it crosses**. The failure it exists to make impossible is a set difference, not a typo —
a producer's vocabulary grows, the response model's hand-written copy does not, and nothing
notices until a real payload carries the new member, at which point pydantic raises a
`ValidationError` inside an `@server.tool()` handler that has no `except` for one.

The number the module docstring records for that: **165 of the 213 `series-contract.md` files on
disk (77.5%) made `context_packet` raise, across seven independent gaps** cit:(["165 of the 213"], mcp/tests/test_wire_vocabulary_exhaustiveness.py:7-7).

## Code Commentary

### Logic

#### What defends what — and what the AST scan defends on its own

The module docstring carries a `WHAT DEFENDS WHAT` table cit:(["WHAT DEFENDS WHAT"], mcp/tests/test_wire_vocabulary_exhaustiveness.py:10-10). Read it before trusting any
test below, because the three mechanisms are **not interchangeable**. Stated honestly, and as the
docstring itself states it cit:(["Any claim that the scan alone keeps a vocabulary honest would be false"], mcp/tests/test_wire_vocabulary_exhaustiveness.py:15-16):

> the AST scan is the weakest of the three. It reads *bare string literals*. It does not evaluate
> expressions … Any claim that the scan alone keeps a vocabulary honest would be false, and was.

So the answer to "which vocabulary does the AST scan alone defend?" is **nothing**. Every row of
the table names a *type-level or runtime* defender, and the scan is only ever the measurement
laid beside it:

| vocabulary | defended by (the table rows above) |
| --- | --- |
| the six contract cells (`workflow_kind`, `memory_mode`, `human_review_status`, `closeout_status`, `integration_status`, `cleanup`) | pyright, at `ContractCells`' typed fields and `WorktreeContract`'s own. `ProducedLiteralTests` supplies the two invariants that make that coverage *total* (below). |
| `phase` / `nextOperation` / `nextTool` | pyright, at `LifecycleGuidance`'s TypedDict and `next_guidance`'s typed parameters. The scan measures the emitted set and asserts it EQUALS the alias. |
| the seven listed in the docstring | pyright, at direct typed constructor calls (`GitFacts(state=…)` and friends). The scan asserts produced == declared. |
| `ContractTask.workflow_kind` / `.memory_mode` | **runtime**, at `_task_vocabulary`. Deliberately plain `str` — it is what a caller asked for, arriving from `worktree_start`'s MCP signature, and there is no type to check. |

Six spellings evade the scan, and they are exactly the shapes an off-vocabulary value arrives in:
a concatenation (`"a" + "b"`), an f-string, a dict subscript (`_MAP["x"]`), a name imported from
another module, a local bound elsewhere, and `cast`. `cast` passes
both pyright and the literal scan *as it must* — it is a programmer overriding the checker on
purpose — and the readability rule below is the only thing that refuses it here.

#### cit:([`ProducedLiteralTests`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:645-834) — the set difference itself

cit:([`produced_literals`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:325-340) parses **every `*.py` under the installed package root**
(`PACKAGE_ROOT` cit:([`PACKAGE_ROOT`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:145-145); `_module_trees` cit:([`_module_trees`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:309-311)) and collects the string literals passed at the
six contract-cell keywords of cit:(["CONTRACT_CALLS = frozenset"], mcp/tests/test_wire_vocabulary_exhaustiveness.py:163-163). The producible set is therefore derived **from the producers' source,
not from the `Literal` alias** — which is what stops the suite passing by agreeing with itself
cit:(["make it agree with itself"], mcp/tests/test_wire_vocabulary_exhaustiveness.py:331-331). cit:([`test_the_scan_actually_found_the_writers`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:660-667) pins five known literals so a
scan that silently matched nothing cannot pass.

Two further rules make pyright's coverage of those six fields total:

- cit:([`test_no_contract_cell_is_written_through_dataclasses_replace`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:669-677) asserts
  cit:([`contract_cells_written_through_replace`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:350-377) `contract_cells_written_through_replace() == []`. **No `dataclasses.replace` call
  anywhere in the package may carry one of the six keywords.** typeshed types `replace` as
  `**changes: Any`, so `replace(contract, cleanup="reclaimed-ish")` produced *zero* pyright
  diagnostics against a four-member `Literal` — one `Any` in a third-party stub voiding the whole
  guarantee. `amend_contract(contract, ContractCells(...))` puts those fields back in front of the
  checker; this rule refuses the spelling that routes around it. The check matches on the *keyword
  name*, so a `replace` on some other dataclass owning a `cleanup` field is reported too — a
  cit:(["inference that makes a scan lie"], mcp/tests/test_wire_vocabulary_exhaustiveness.py:363-363). The declaring module
  `worktrees/worktree_contract.py` cit:(["VOCABULARY_DECLARING_MODULE ="], mcp/tests/test_wire_vocabulary_exhaustiveness.py:173-173) is exempt from both scans. In the `replace` scan,
  `amend_contract` **is** the one sanctioned `replace`, and its own parameters did the checking a
  line earlier cit:(["The declaring module is exempt because", "its own parameters did the checking one line earlier. \"\"\" offenders: list[str] = [] for path, tree in _module_trees(): if path.as_posix().endswith(VOCABULARY_DECLARING_MODULE): continue"], mcp/tests/test_wire_vocabulary_exhaustiveness.py:365-371).
  The typed-writer scan applies the same declaring-module exemption
  cit:(["def unreadable_contract_writes() -> list[str]:  # pragma: no cover"], mcp/tests/test_wire_vocabulary_exhaustiveness.py:398-398).
- cit:([`test_every_contract_cell_is_written_as_something_this_scan_can_read`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:693-702) asserts
  cit:([`unreadable_contract_writes`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:397-411) `unreadable_contract_writes() == []`. Every value reaching a **typed** writer
  cit:(["TYPED_CONTRACT_WRITERS ="], mcp/tests/test_wire_vocabulary_exhaustiveness.py:168-168) must be an
  expression the scan can enumerate: a bare string constant, a conditional between two readable
  branches, or an attribute read — the last being how a lifecycle write says "leave this cell as
  it was" (`contract.integration_status`). See `_readable_expression` cit:([`_readable_expression`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:380-393). `ContractTask`
  is excluded on purpose cit:(["is excluded on purpose"], mcp/tests/test_wire_vocabulary_exhaustiveness.py:165-165): its two vocabulary fields are plain `str` because they are a
  *request*, narrowed at runtime by `_task_vocabulary` and pinned by `ContractBoundaryTests`.

cit:([`test_the_typed_writer_moves_only_the_cells_it_is_handed`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:679-691) holds `amend_contract` to
`replace` semantics: an omitted cell keeps its value, a given one moves, nothing else changes.

Where the scan is exact the assertion is set **EQUALITY**, which also catches the other direction —
a declared member no producer can ever emit:

- cit:([`test_every_next_guidance_literal_validates_at_its_wire_field`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:704-719):
  cit:(["def guidance_next_moves"], mcp/tests/test_wire_vocabulary_exhaustiveness.py:415-415) `guidance_next_moves()` == `set(get_args(NextOperation))` / `set(get_args(NextTool))`.
- cit:([`test_every_phase_the_guidance_module_writes_validates`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:721-730): the `phase` literals
  cit:([`_dict_literal_values`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:437-460) reads out of `worktrees/modules/guidance.py` ==
  `set(get_args(WorktreePhase))`. That helper reads **both** dict spellings (`{"phase": "x"}` and
  `dict(phase="x")`), because reading only the first left a producer shape invisible.
- the seven that had the identical construction but had not drifted yet, each
  measured produced-from-source == declared: `RepoSummary.state` ← `kernel.git_facts.RepoState`
  cit:([`test_every_repo_state_the_git_facts_reader_writes_validates`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:754-764); `BranchFreshness.state` ← `kernel.git_freshness.FreshnessState`
  cit:([`test_every_freshness_state_the_git_reader_writes_validates`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:766-775);
  `DriftCheckResponse.status` ← the drift summary's own dict literals, now one declaration serving
  both the packet and the tool cit:([`test_every_drift_status_validates_at_both_of_its_wire_models`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:777-786); `FileRead.status` ← `application.read_files`
  `_resolve_onboarding`'s returned tuple cit:([`test_every_onboarding_status_the_read_entry_point_returns_validates`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:788-795); and the three `models.terminal` response
  vocabularies for `spawn_agent_session` / `session_retire` / `session_rename` cit:([`test_every_spawn_status_the_tool_can_return_validates`, `test_every_retire_status_the_tool_writes_validates`, `test_every_rename_status_the_tool_writes_validates`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:797-817; mcp/tests/test_wire_vocabulary_exhaustiveness.py:819-826; mcp/tests/test_wire_vocabulary_exhaustiveness.py:828-834).

The reading helpers are deliberately narrow so the scan cannot lie in the expensive direction:
cit:([`_value_literals`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:477-490) returns only strings an expression can *evaluate* to and never a
comparison operand; cit:([`_dataclass_field_writes`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:530-548) reads the field's positional index off
the class body and also follows the same-named local both git readers assign; cit:([`_builder_statuses`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:592-613) follows a refusal builder handed a variable through the first cell of the table its
function walks, which is how two of the thirteen spawn statuses are reached at all.

#### cit:(["class AdvertisedVocabularyTests(unittest.TestCase):"], mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:49-49) — the published input contract

This class reads vocabularies **out of a tool's own docstring, by AST**, and holds them to the
published output contract:

- cit:([`_advertised_workflow_kinds`], mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:547-552) parses `worktree_start`'s docstring in
  `mcp/registration/worktrees.py` with `re.findall(r"'([a-z-]+-task)'", …)`.
  cit:([`test_the_workflow_kinds_advertised_and_declared_are_the_same_set`], mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:46-63) asserts it EQUAL
  to `set(get_args(WorkflowKind))` **and** to `{"light-task", "chat-task"}`. Held only one way,
  the alias could grow a member no tool advertises and no writer emits — which is exactly what had
  happened: `WorkflowKind` carried a bare `chat` and `light` beside `chat-task` and `light-task`,
  the un-reconciled union of the old hand-written copy and the new one, with zero occurrences
  across the 213 contracts on disk.
- cit:([`_advertised_statuses`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:625-642) reads `mcp/registration/sessions.py`: the closing
  `Status …` roster plus any inline `status 'x'` mention in the prose above it, and nothing else —
  the backticked `dispatch-brief` in `spawn_agent_session` is a message kind, and reading it as a
  status would assert the existence of one that was never meant to exist.
  cit:([`test_agent_session_tools_are_structural_and_exact_id_tools_are_absent`], mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:65-98) asserts that the agent roster declares structural dispatch/child administration and excludes raw spawn, retire, and rename tools plus their private id fields.
- cit:([`test_every_memory_mode_the_contract_accepts_validates_on_both_fields`], mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:100-112): one packet
  reports the mode twice (`WorktreeSummary.memoryMode` and `MemorySummary.mode`); both copies must
  accept `VALID_MEMORY_MODES`.

#### The behavioural halves

- cit:([`GuidanceWalkTests`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:229-306) drives one contract per `lifecycle_guidance` branch, in the
  order the machine tries them cit:([`_phases`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:237-263), and crosses each result through
  `WorktreeSummary` with cit:([`cross_the_wire`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:211-226) — the same field-by-field projection
  production does, filtered to `GUIDANCE_WIRE_KEYS` cit:(["GUIDANCE_WIRE_KEYS ="], mcp/tests/test_wire_vocabulary_exhaustiveness.py:150-150). It pins the two gaps that were
  measured writable-and-unrepresentable (`request_carryover_decision`) and the current read-only
  carryover guidance (`memory_carryover_plan`), the omission of `nextTool` on a done phase, and every writable
  `cleanup` value.
- cit:([`RecoveryGuidanceTests`], mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:115-150) holds the *other* side of the vocabulary split so it cannot
  be undone by accident: `recovery_guidance` emits the same four keys in the same order, omits
  `nextRequiredArgs` when there are none — and its vocabulary must **not** validate at
  `WorktreeSummary`.
- cit:(["class ContractBoundaryTests(unittest.TestCase):"], mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:159-159) is the other half of the same guarantee, and the one place
  tolerance is the correct answer. `load_contract` is the single entry point of
  `worktree_closeout_apply`, `worktree_integrate`, `worktree_cleanup`, `worktree_sync`,
  `worktree_abandon` and `worktree_status`, **none** of which catches `ContractError`, so one
  unreadable token took all six down at once. The split is by direction: the **reader** substitutes
  the declared fallback, records the raw token in `unknown_cells` and reports it through
  `WorktreeSummary.unknownContractCells` (`OFF_VOCABULARY_CELLS`;
  `test_every_vocabulary_cell_degrades_rather_than_stranding_the_task`); the
  **writer** refuses, reachable only through a deliberate `cast`
  cit:([`test_the_writer_refuses_what_the_reader_tolerated`], mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:316-331). `memory_mode` is the one cell
  whose fallback is *inferred* rather than declared — a recorded memory worktree is an external
  topology cit:([`test_an_unreadable_memory_mode_degrades_to_the_topology_on_disk`], mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:281-304). A rewrite by any lifecycle tool heals the file, and that is the recovery
  path cit:([`test_a_rewrite_heals_the_file_and_that_is_the_recovery_path`], mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:306-314). Every refusal names the contract file it was reading cit:([`test_every_refusal_names_the_contract_it_was_reading`], mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:348-378), and the
  refusal reaches `worktree_status` as a payload rather than a traceback cit:([`test_the_invalid_contract_payload_carries_the_file_to_open`], mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:421-437).
  cit:([`test_a_healthy_contract_omits_the_next_required_args_it_has_none_of`], mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:494-513) pins the
  declared wire shape: measured across the 213 contracts on disk, **48 responses that carried
  `"nextRequiredArgs": []` now omit the key**.
- cit:([`ProducerWireCrossingTests`], mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:516-543) does for the two `kernel` readers what
  `GuidanceWalkTests` does for the phase machine, and stays offline: an absent repo is answered
  before any subprocess runs, and the freshness read is told not to fetch.

### Conventions

`sys.path.insert(0, mcp/src)` **and** `mcp/tests` before package imports cit:(["MCP_SRC =", "MCP_TESTS ="], mcp/tests/test_wire_vocabulary_exhaustiveness.py:109-110). Vocabulary
membership is asserted through `_accepts(model, base, field, value)` cit:([`_accepts`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:180-185) — a
`model_validate` over a minimal base dict with only the field under test undecided
(`REPO_BASE` cit:(["REPO_BASE ="], mcp/tests/test_wire_vocabulary_exhaustiveness.py:474-474) / `SESSION_BASE` cit:(["SESSION_BASE ="], mcp/tests/test_wire_vocabulary_exhaustiveness.py:475-475)) — rather than by reading the alias, so the assertion is
about the wire model and not about the constant beside it. Every scan is source-reading, never
import-time reflection: cit:([`_module_tree`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:463-465) re-parses one module by repo-relative
path, `_module_trees()` walks the whole package. Contract fixtures go through
`_contract(root, **overrides)` cit:([`_contract`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:188-208), which builds one fully-populated `WorktreeContract` and then
`replace`s — the test module is outside the package, so the no-`replace` rule does not apply to it.

### Invariants And Boundaries

- The producible set must stay derived from the producers' **source**. Re-deriving it from a
  `Literal` alias would make the suite agree with itself and prove nothing.
- `contract_cells_written_through_replace()` must stay `[]`, and `unreadable_contract_writes()`
  must stay `[]`. These two are what make pyright's coverage of the six contract cells total; a
  new writer that needs an exception needs the exception to be argued, not added.
- `VOCABULARY_DECLARING_MODULE` is the only exemption, and only because `amend_contract` is the
  sanctioned `replace`. Widening it re-opens the hole.
- Where the two sets are asserted EQUAL they must stay equal in both directions — a declared
  member no producer can emit is a vocabulary that has outgrown its own writer.
- The AST scan must never be described, in code or in this card, as defending a vocabulary on its
  own. Six spellings walk past it.
- `ContractTask`'s two vocabulary fields stay plain `str`: they are a caller's request, checked at
  runtime by `_task_vocabulary`, and typing them would refuse a bad request in the wrong place.
- The reader tolerates, the writer refuses. Neither may be swapped: refusing on read strands the
  task; tolerating on write puts an unknown token on disk.
- The suite must stay offline — no worktrees, no remote probe, no network.

### Todos

The two undocumented-but-producible `spawn_agent_session` statuses (`leaf-ref-not-found`,
`leaf-ref-ambiguous`) are pinned as a known difference rather than fixed. Closing the gap means
adding them to the tool docstring and tightening `test_every_status_the_session_tools_roster_validates`
to a plain equality.

## Docs References

No external Domain Documentation source is configured for this memory repo (`system/sources.md`
records `No entries configured yet.`), so the claims here are proven by repository source only.
One explanatory test docstring records the relevant typeshed behavior for
`dataclasses.replace`; the behavior described and asserted by this card is
otherwise repository-local.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external or domain documentation was found for this repository-local test module; live retrieval was not available and the registry is empty. | — | — |

## Repo-Internal References

The suite reads producer source and validates against wire models, so its
evidence is split across the declaring module, the models, and the producers
themselves.

| Finding | Anchor | Source |
| --- | --- | --- |
| The six contract cells (declared in models/worktree.py), typed amendment, tolerant read, and refusing write. | "WorkflowKind = Literal["; "CleanupStatus = Literal["; "class ContractCells"; "def amend_contract"; "def load_contract"; "def write_contract"; "VALID_MEMORY_MODES: frozenset[MemoryMode]" | mcp/src/agents_remember/models/worktree.py:21-21; mcp/src/agents_remember/models/worktree.py:26-26; mcp/src/agents_remember/worktrees/worktree_contract.py:72-72; mcp/src/agents_remember/worktrees/worktree_contract.py:181-181; mcp/src/agents_remember/worktrees/worktree_contract.py:198-198; mcp/src/agents_remember/worktrees/worktree_contract.py:437-437; mcp/src/agents_remember/worktrees/worktree_contract.py:488-488 |
| The wire model every contract and guidance value must validate at. | `WorktreeSummary` | mcp/src/agents_remember/models/worktree.py:148-198 |
| Guidance state machines use the grouped wire-alias import and keep separate lifecycle, next-step, and recovery builders and recovery vocabulary. | "from agents_remember.models.worktree import ("; `RecoveryOperation`; `RecoveryTool`; `lifecycle_guidance`; `next_guidance`; `recovery_guidance` | mcp/src/agents_remember/worktrees/modules/guidance.py:10-14; mcp/src/agents_remember/worktrees/modules/guidance.py:38-55; mcp/src/agents_remember/worktrees/modules/guidance.py:130-144; mcp/src/agents_remember/worktrees/modules/guidance.py:147-170; mcp/src/agents_remember/worktrees/modules/guidance.py:225-235 |
| Worktree status projects invalid-contract errors onto the payload. | `worktree_status_packet`; `status_payload` | mcp/src/agents_remember/application/worktree_status.py:46-128 |
| Published workflow kind and structural agent-session tool docstrings. | `worktree_start`; `dispatch_agent`; `retire_child`; `rename_child`; `rename_self` | mcp/src/agents_remember/mcp/registration/worktrees.py:28-92; mcp/src/agents_remember/mcp/registration/sessions.py:27-57; mcp/src/agents_remember/mcp/registration/sessions.py:59-73; mcp/src/agents_remember/mcp/registration/sessions.py:75-89; mcp/src/agents_remember/mcp/registration/sessions.py:91-94 |
| Session response vocabularies. | `SpawnAgentSessionResponse`; `SessionRetireResponse`; `SessionRenameResponse` | mcp/src/agents_remember/models/terminal.py:91-135; mcp/src/agents_remember/models/terminal.py:175-191; mcp/src/agents_remember/models/terminal.py:201-212 |
| Terminal refusal/result production is split across the centralized spawn-refusal builder and the knob, retire, and rename result seams. | "def spawn_refusal("; "def _knob_refusal("; "def _retire_payload("; "def _rename_payload(" | mcp/src/agents_remember/application/terminal_spawn_results.py:13-31; mcp/src/agents_remember/application/terminal_tools.py:466-484; mcp/src/agents_remember/application/terminal_tools.py:917-952; mcp/src/agents_remember/application/terminal_tools.py:1090-1111 |
| Leaf-reference refusal statuses. | `LeafRefResolutionError` | mcp/src/agents_remember/worktrees/leaf_refs.py:39-66 |
| Git facts, freshness, onboarding-read, and drift-status producers. | `git_facts_to_packet`; `freshness_to_packet`; `_resolve_onboarding`; `run_drift_summary` | mcp/src/agents_remember/application/read_files.py:218-247; mcp/src/agents_remember/kernel/git_facts.py:104-115; mcp/src/agents_remember/kernel/git_freshness.py:158-169; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py:35-90 |
| Invalid-contract start result. | `invalid_contract_request_result` | mcp/src/agents_remember/worktrees/modules/startup/leaf_ref_start.py:38-53 |
| The suite's own producer scan and behavioural test classes. | "class GuidanceWalkTests(unittest.TestCase):"; "class ProducedLiteralTests(unittest.TestCase):"; "class AdvertisedVocabularyTests(unittest.TestCase):"; "class RecoveryGuidanceTests(unittest.TestCase):"; "class ContractBoundaryTests(unittest.TestCase):"; "class ProducerWireCrossingTests(unittest.TestCase):" | mcp/tests/test_wire_vocabulary_exhaustiveness.py:230-230; mcp/tests/test_wire_vocabulary_exhaustiveness.py:646-646; mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:49-49; mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:121-121; mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:159-159; mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:516-516 |

## Cross-Repo References

The reviewed behavior is wholly repository-local: every producer, wire model,
and docstring this suite reads lives in `mcp/src/agents_remember/`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found — the whole import surface is same-repository. | `ProducerWireCrossingTests` | mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:516-543 |

## L23 Refusal Vocabulary Ownership

Produced-literal analysis now includes `terminal_spawn_results.py` alongside the
terminal facade, so moving the builder cannot hide a public status from the
closed spawn response vocabulary.

## 260821-CLIVE-L1 Contract-Pure Closeout Guidance

`GuidanceWalkTests.test_closeout_pending_guidance_is_pure_when_the_worktree_is_missing` proves
`lifecycle_guidance` can publish closeout-pending status without observing or materializing the
candidate. The wire carries only static `nextRequiredArgs=["intent_note"]`; its summary directs the
caller to closeout preview/apply for the exact candidate-derived message plan. This keeps status
projection contract-pure and prevents guidance from becoming a second applicability owner.

## Update History

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-22T11:29+02:00 — No content impact: candidate12 adds explicit absence
  assertions after both `cross_the_wire` and `lifecycle_guidance`, strengthening the already
  documented missing-worktree purity contract without changing its meaning. Reviewed against
  candidate tree `8f03b256fe24aa77262da805f1538ee39ccb4dd6`, full diff SHA
  `ccb36a898b455cd67ca00c378e5ba0f18851be01faf3d26eced3b9af062f429e`, same-reviewer PASS;
  commit-derived verification metadata remains unchanged until governed closeout.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: added the contract-pure closeout-guidance regression
  (`mcp/tests/test_wire_vocabulary_exhaustiveness.py:279-289`) and rebound later source citations to
  accepted candidate tree `4241908c`; verification metadata remains closeout-owned.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1 curator: repaired the `rename_self` citation range (sessions.py:27-86 → 27-94) surfaced by the leaf-scoped quality check; no content impact. Verification metadata remains closeout-owned.

- 2026-08-16T00:45+02:00 — Re-read the exact NextTool producer set after protected-memory apply guidance was retired; the suite now pins `memory_carryover_plan` while preserving exact set equality. Verification remains closeout-owned.
- 2026-08-14T05:26Z — L23 final curator: re-anchored the expanded recovery vocabulary and the
  lifecycle/next/recovery builders after their final structural edits. Verification remains
  closeout-owned.

- 2026-08-13T12:53+02:00 — No content impact: the stabilized package scan root reads
  `sys.modules["agents_remember"].__file__` after normal package submodule imports. Vocabulary
  scanners and assertions are unchanged, and no Ruff config exception remains. This supersedes the
  12:26 import-shape note; provenance stays closeout-owned.

- 2026-08-13T12:26+02:00 — No content impact: the final Ruff-safe form imports
  `agents_remember.__file__` directly as `agents_remember_file` when deriving the same package scan
  root. Scanners, vocabulary sets, and exhaustiveness assertions are unchanged; verification
  provenance remains closeout-owned.

- 2026-08-13T11:57+02:00 — No content impact: Ruff I001 moved the `agents_remember` import below
  the vocabulary/worktree imports without changing the package root, scanners, declared
  vocabularies, or assertions. Sanctioned citation repair updated all resulting one-line range
  shifts, including cross-card references; verification provenance remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented extracted refusal-builder vocabulary coverage; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T14:29+02:00 — Re-read the structural session tool declarations and widened the
  session-registration range to include the decorated `dispatch_agent` declaration; verification
  metadata remains unchanged for governed closeout.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-04T09:54:46+02:00 — 260731-EFA-L6 S18-B07 second bounded correction: made package traversal, exemption branches, readable-expression behavior, base dictionaries, and the bounded history citations checker-visible; same-reviewer delta pending.

- 2026-08-02T18:15:05+02:00 — 260731-EFA-L6 curator W1-B09 resumed: repaired 1 citation finding and normalized 4 citation ranges; scoped recheck clean (0 findings).
- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 35 citation finding(s); 1 citation finding remains unresolved because the scoped live check/fix hit the 268435456-byte citation source-index cap while building the dirty code snapshot.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T08:35+02:00 — 260731-EFA-L4 curator: created for the new leaf-central wire-vocabulary
  suite. Recorded the three mechanisms and the honest answer to what the AST scan defends on its
  own — **nothing**: the module docstring states the scan reads bare string literals and that "any
  claim that the scan alone keeps a vocabulary honest would be false, and was" cit:(["Any claim that the scan alone keeps a vocabulary honest would be false"], mcp/tests/test_wire_vocabulary_exhaustiveness.py:15-16), and the
  six spellings that evade it are named (concatenation, f-string, dict subscript, imported name,
  local bound elsewhere, `cast`). The brief that commissioned this card described the
  `WHAT DEFENDS WHAT` table as carrying a row reading "**nothing** — the AST scan alone"; the table
  has no such row — all four of its rows name pyright (three) or the runtime
  `_task_vocabulary` narrowing (one), and the scan appears only as the measurement laid beside
  them. This card states what the source says. Recorded `ProducedLiteralTests`' derivation from the
  producers' source rather than from the alias cit:(["def produced_literals"], mcp/tests/test_wire_vocabulary_exhaustiveness.py:326-326), the two rules that
  make pyright total — no `dataclasses.replace` may carry one of the six contract-cell keywords
  (`contract_cells_written_through_replace` cit:([`contract_cells_written_through_replace`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:350-377); typeshed's `**changes: Any` is
  the reason), and every value at a typed writer must be a statically readable expression
  (`unreadable_contract_writes` cit:([`unreadable_contract_writes`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:397-411)) — plus the declaring-module exemption
  cit:([`VOCABULARY_DECLARING_MODULE`], mcp/tests/test_wire_vocabulary_exhaustiveness.py:173-173), applied by both scan branches:
  cit:(["The declaring module is exempt because", "its own parameters did the checking one line earlier. \"\"\" offenders: list[str] = [] for path, tree in _module_trees(): if path.as_posix().endswith(VOCABULARY_DECLARING_MODULE): continue"], mcp/tests/test_wire_vocabulary_exhaustiveness.py:365-371) and
  cit:(["def unreadable_contract_writes() -> list[str]:  # pragma: no cover"], mcp/tests/test_wire_vocabulary_exhaustiveness.py:398-398). `AdvertisedVocabularyTests` reads its docstring by AST, including the pinned
  `{"leaf-ref-not-found", "leaf-ref-ambiguous"}` difference, and the behavioural halves are covered by
  `GuidanceWalkTests`, `RecoveryGuidanceTests`, `ContractBoundaryTests`, and `ProducerWireCrossingTests`.
  Verification metadata pinned to the pre-leaf source authority
  (`abc7cbcc74921cdcb57a61529445f61641e919e7`) as a placeholder until closeout stamps the L4 code
  commit — this source file is new and not yet committed.
