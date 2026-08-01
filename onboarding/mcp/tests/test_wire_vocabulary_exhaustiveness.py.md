# test_wire_vocabulary_exhaustiveness.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_wire_vocabulary_exhaustiveness.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T08:35+02:00                           |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
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
disk (77.5%) made `context_packet` raise, across seven independent gaps** (L7-L8).

## Code Commentary

### Logic

#### What defends what — and what the AST scan defends on its own

The module docstring carries a `WHAT DEFENDS WHAT` table (L18-L40). Read it before trusting any
test below, because the three mechanisms are **not interchangeable**. Stated honestly, and as the
docstring itself states it (L12-L16):

> the AST scan is the weakest of the three. It reads *bare string literals*. It does not evaluate
> expressions … Any claim that the scan alone keeps a vocabulary honest would be false, and was.

So the answer to "which vocabulary does the AST scan alone defend?" is **nothing**. Every row of
the table names a *type-level or runtime* defender, and the scan is only ever the measurement
laid beside it:

| vocabulary | defended by (table row, L18-L40) |
| --- | --- |
| the six contract cells (`workflow_kind`, `memory_mode`, `human_review_status`, `closeout_status`, `integration_status`, `cleanup`) | pyright, at `ContractCells`' typed fields and `WorktreeContract`'s own. `ProducedLiteralTests` supplies the two invariants that make that coverage *total* (below). |
| `phase` / `nextOperation` / `nextTool` | pyright, at `LifecycleGuidance`'s TypedDict and `next_guidance`'s typed parameters. The scan measures the emitted set and asserts it EQUALS the alias. |
| the seven listed in the docstring (L75-L81) | pyright, at direct typed constructor calls (`GitFacts(state=…)` and friends). The scan asserts produced == declared. |
| `ContractTask.workflow_kind` / `.memory_mode` | **runtime**, at `_task_vocabulary`. Deliberately plain `str` — it is what a caller asked for, arriving from `worktree_start`'s MCP signature, and there is no type to check. |

Six spellings evade the scan, and they are exactly the shapes an off-vocabulary value arrives in:
a concatenation (`"a" + "b"`), an f-string, a dict subscript (`_MAP["x"]`), a name imported from
another module, a local bound elsewhere, and `cast` (L14-L15; L383-L385; L689-L690). `cast` passes
both pyright and the literal scan *as it must* — it is a programmer overriding the checker on
purpose — and the readability rule below is the only thing that refuses it here.

#### `ProducedLiteralTests` (L635-L820) — the set difference itself

`produced_literals()` (L324-L339) parses **every `*.py` under the installed package root**
(`PACKAGE_ROOT`, L157; `_module_trees`, L308-L310) and collects the string literals passed at the
six contract-cell keywords of `CONTRACT_CALLS = frozenset({"WorktreeContract", "ContractTask",
"ContractCells"})` (L175). The producible set is therefore derived **from the producers' source,
not from the `Literal` alias** — which is what stops the suite passing by agreeing with itself
(L327-L330). `test_the_scan_actually_found_the_writers` (L650-L657) pins five known literals so a
scan that silently matched nothing cannot pass.

Two further rules make pyright's coverage of those six fields total:

- `test_no_contract_cell_is_written_through_dataclasses_replace` (L659-L667) asserts
  `contract_cells_written_through_replace() == []` (L348-L375). **No `dataclasses.replace` call
  anywhere in the package may carry one of the six keywords.** typeshed types `replace` as
  `**changes: Any`, so `replace(contract, cleanup="reclaimed-ish")` produced *zero* pyright
  diagnostics against a four-member `Literal` — one `Any` in a third-party stub voiding the whole
  guarantee. `amend_contract(contract, ContractCells(...))` puts those fields back in front of the
  checker; this rule refuses the spelling that routes around it. The check matches on the *keyword
  name*, so a `replace` on some other dataclass owning a `cleanup` field is reported too — a
  deliberate trade over inference that would make the scan lie (L356-L360). The declaring module
  `worktrees/worktree_contract.py` (`VOCABULARY_DECLARING_MODULE`, L185) is exempt, because
  `amend_contract` **is** the one sanctioned `replace` and its own parameters did the checking a
  line earlier.
- `test_every_contract_cell_is_written_as_something_this_scan_can_read` (L683-L692) asserts
  `unreadable_contract_writes() == []` (L394-L408). Every value reaching a **typed** writer
  (`TYPED_CONTRACT_WRITERS = frozenset({"WorktreeContract", "ContractCells"})`, L180) must be an
  expression the scan can enumerate: a bare string constant, a conditional between two readable
  branches, or an attribute read — the last being how a lifecycle write says "leave this cell as
  it was" (`contract.integration_status`). See `_readable_expression`, L378-L391. `ContractTask`
  is excluded on purpose (L176-L179): its two vocabulary fields are plain `str` because they are a
  *request*, narrowed at runtime by `_task_vocabulary` and pinned by `ContractBoundaryTests`.

`test_the_typed_writer_moves_only_the_cells_it_is_handed` (L669-L681) holds `amend_contract` to
`replace` semantics: an omitted cell keeps its value, a given one moves, nothing else changes.

Where the scan is exact the assertion is set **EQUALITY**, which also catches the other direction —
a declared member no producer can ever emit:

- `test_every_next_guidance_literal_validates_at_its_wire_field` (L694-L709):
  `guidance_next_moves()` (L411-L429) == `set(get_args(NextOperation))` / `set(get_args(NextTool))`.
- `test_every_phase_the_guidance_module_writes_validates` (L711-L720): the `phase` literals
  `_dict_literal_values` (L432-L455) reads out of `worktrees/modules/guidance.py` ==
  `set(get_args(WorktreePhase))`. That helper reads **both** dict spellings (`{"phase": "x"}` and
  `dict(phase="x")`), because reading only the first left a producer shape invisible.
- the seven that had the identical construction but had not drifted yet (docstring L69-L87), each
  measured produced-from-source == declared: `RepoSummary.state` ← `kernel.git_facts.RepoState`
  (L744-L754); `BranchFreshness.state` ← `kernel.git_freshness.FreshnessState` (L756-L765);
  `DriftCheckResponse.status` ← the drift summary's own dict literals, now one declaration serving
  both the packet and the tool (L767-L776); `FileRead.status` ← `controllers.read_files`
  `_resolve_onboarding`'s returned tuple (L778-L785); and the three `models.terminal` response
  vocabularies for `spawn_agent_session` / `session_retire` / `session_rename` (L787-L820).

The reading helpers are deliberately narrow so the scan cannot lie in the expensive direction:
`_value_literals` (L471-L484) returns only strings an expression can *evaluate* to and never a
comparison operand; `_dataclass_field_writes` (L522-L540) reads the field's positional index off
the class body and also follows the same-named local both git readers assign; `_builder_statuses`
(L583-L604) follows a refusal builder handed a variable through the first cell of the table its
function walks, which is how two of the thirteen spawn statuses are reached at all.

#### `AdvertisedVocabularyTests` (L823-L881) — the published input contract

This class reads vocabularies **out of a tool's own docstring, by AST**, and holds them to the
published output contract:

- `_advertised_workflow_kinds()` (L1255-L1260) parses `worktree_start`'s docstring in
  `mcp/registration/worktrees.py` with `re.findall(r"'([a-z-]+-task)'", …)`.
  `test_the_workflow_kinds_advertised_and_declared_are_the_same_set` (L826-L843) asserts it EQUAL
  to `set(get_args(WorkflowKind))` **and** to `{"light-task", "chat-task"}`. Held only one way,
  the alias could grow a member no tool advertises and no writer emits — which is exactly what had
  happened: `WorkflowKind` carried a bare `chat` and `light` beside `chat-task` and `light-task`,
  the un-reconciled union of the old hand-written copy and the new one, with zero occurrences
  across the 213 contracts on disk.
- `_advertised_statuses(tool)` (L615-L632) reads `mcp/registration/sessions.py`: the closing
  `Status …` roster plus any inline `status 'x'` mention in the prose above it, and nothing else —
  the backticked `dispatch-brief` in `spawn_agent_session` is a message kind, and reading it as a
  status would assert the existence of one that was never meant to exist.
  `test_every_status_the_session_tools_roster_validates` (L845-L867) asserts docstring ==
  response enum for `session_retire` and `session_rename`, and for `spawn_agent_session` **pins
  the difference rather than tolerating it**: `vocabulary - advertised == {"leaf-ref-not-found",
  "leaf-ref-ambiguous"}` — two statuses that are producible and undocumented.
- `test_every_memory_mode_the_contract_accepts_validates_on_both_fields` (L869-L881): one packet
  reports the mode twice (`WorktreeSummary.memoryMode` and `MemorySummary.mode`); both copies must
  accept `VALID_MEMORY_MODES`.

#### The behavioural halves

- `GuidanceWalkTests` (L241-L305) drives one contract per `lifecycle_guidance` branch, in the
  order the machine tries them (`_phases`, L249-L275), and crosses each result through
  `WorktreeSummary` with `cross_the_wire` (L223-L238) — the same field-by-field projection
  production does, filtered to `GUIDANCE_WIRE_KEYS` (L162). It pins the two gaps that were
  measured writable-and-unrepresentable (`request_carryover_decision` /
  `memory_carryover_apply`), the omission of `nextTool` on a done phase, and every writable
  `cleanup` value.
- `RecoveryGuidanceTests` (L884-L919) holds the *other* side of the vocabulary split so it cannot
  be undone by accident: `recovery_guidance` emits the same four keys in the same order, omits
  `nextRequiredArgs` when there are none — and its vocabulary must **not** validate at
  `WorktreeSummary`.
- `ContractBoundaryTests` (L922-L1222) is the other half of the same guarantee, and the one place
  tolerance is the correct answer. `load_contract` is the single entry point of
  `worktree_closeout_apply`, `worktree_integrate`, `worktree_cleanup`, `worktree_sync`,
  `worktree_abandon` and `worktree_status`, **none** of which catches `ContractError`, so one
  unreadable token took all six down at once. The split is by direction: the **reader** substitutes
  the declared fallback, records the raw token in `unknown_cells` and reports it through
  `WorktreeSummary.unknownContractCells` (`OFF_VOCABULARY_CELLS`, L948-L970;
  `test_every_vocabulary_cell_degrades_rather_than_stranding_the_task`, L1009-L1019); the
  **writer** refuses, reachable only through a deliberate `cast`
  (`test_the_writer_refuses_what_the_reader_tolerated`, L1056-L1068). `memory_mode` is the one cell
  whose fallback is *inferred* rather than declared — a recorded memory worktree is an external
  topology (L1021-L1044). A rewrite by any lifecycle tool heals the file, and that is the recovery
  path (L1046-L1054). Every refusal names the contract file it was reading (L1080-L1148), and the
  refusal reaches `worktree_status` as a payload rather than a traceback (L1150-L1162).
  `test_a_healthy_contract_omits_the_next_required_args_it_has_none_of` (L1205-L1222) pins the
  declared wire shape: measured across the 213 contracts on disk, **48 responses that carried
  `"nextRequiredArgs": []` now omit the key**.
- `ProducerWireCrossingTests` (L1225-L1252) does for the two `kernel` readers what
  `GuidanceWalkTests` does for the phase machine, and stays offline: an absent repo is answered
  before any subprocess runs, and the freshness read is told not to fetch.

### Conventions

`sys.path.insert(0, mcp/src)` **and** `mcp/tests` before package imports (L106-L109). Vocabulary
membership is asserted through `_accepts(model, base, field, value)` (L192-L197) — a
`model_validate` over a minimal base dict with only the field under test undecided
(`REPO_BASE` / `SESSION_BASE`, L467-L468) — rather than by reading the alias, so the assertion is
about the wire model and not about the constant beside it. Every scan is source-reading, never
import-time reflection: `_module_tree(relative)` (L458-L460) re-parses one module by repo-relative
path, `_module_trees()` walks the whole package. Contract fixtures go through `_contract(root,
**overrides)` (L200-L220), which builds one fully-populated `WorktreeContract` and then
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
One third-party behaviour is load-bearing and is recorded from the source that observes it: typeshed
types `dataclasses.replace` as `**changes: Any`, which is why pyright reported nothing at the six
contract cells and why the no-`replace` rule exists.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external or domain documentation was found for this repository-local test module; live retrieval was not available and the registry is empty. | `system/sources.md` — "No entries configured yet." | — |

## Repo-Internal References

The suite reads the producers' source and validates against the wire models, so its evidence is
split across the declaring module, the wire models, and the producers themselves.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The six contract cells, their `Literal` aliases, `ContractCells`, `amend_contract` (the sanctioned `replace`), `load_contract`'s tolerant read and `write_contract`'s refusal. | `WorkflowKind`, `CleanupStatus`, `ContractCells`, `amend_contract`, `load_contract`, `write_contract`, `VALID_MEMORY_MODES` | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| The wire model every contract cell and guidance key must validate at. | `WorktreeSummary` | [worktree.py](agents-remember/mcp/src/agents_remember/models/worktree.py) |
| The phase state machine whose `phase` literals and `next_guidance` call sites are scanned, plus `recovery_guidance` — the separate builder whose vocabulary must not reach `WorktreeSummary`. | `lifecycle_guidance`, `next_guidance`, `recovery_guidance`, `WorktreePhase`, `NextOperation`, `NextTool` | [guidance.py](agents-remember/mcp/src/agents_remember/worktrees/modules/guidance.py) |
| The projection under test end to end: `worktree_status_packet` puts `str(error)` on the payload verbatim, which is why adding the path at the raiser gave every tool the named file. | `worktree_status_packet`, `status_payload` | [status.py](agents-remember/mcp/src/agents_remember/worktrees/status.py) |
| The `worktree_start` docstring `AdvertisedVocabularyTests` parses for advertised `*-task` kinds. | `worktree_start` | [worktrees.py](agents-remember/mcp/src/agents_remember/mcp/registration/worktrees.py) |
| The session-tool docstrings whose closing `Status …` roster and inline `status 'x'` mentions are the published status contract. | `spawn_agent_session`, `session_retire`, `session_rename` | [sessions.py](agents-remember/mcp/src/agents_remember/mcp/registration/sessions.py) |
| The three session response models and their `VALID_*_STATUSES` tuples, asserted equal to the producers' scanned sets. | `SpawnAgentSessionResponse`, `SessionRetireResponse`, `SessionRenameResponse` | [terminal.py](agents-remember/mcp/src/agents_remember/models/terminal.py) |
| The spawn/retire/rename refusal builders and payloads the status scan reads (`_spawn_refusal`, `_knob_refusal`'s table, `_retire_payload`, `_rename_payload`). | `_spawn_refusal`, `_knob_refusal`, `_retire_payload`, `_rename_payload` | [terminal.py](agents-remember/mcp/src/agents_remember/mcp/tools/terminal.py) |
| The two leaf-ref statuses the tool never writes itself — `LeafRefResolutionError` decides them and the refusal payload copies them verbatim. | `status` assignments in `LeafRefResolutionError` | [leaf_refs.py](agents-remember/mcp/src/agents_remember/worktrees/leaf_refs.py) |
| The two `kernel` git readers whose `state` literals are scanned off their `GitFacts` / `BranchFreshness` writes and then crossed through the packet models. | `VALID_REPO_STATES`, `git_facts_to_packet`; `VALID_FRESHNESS_STATES`, `freshness_to_packet` | [git_facts.py](agents-remember/mcp/src/agents_remember/kernel/git_facts.py); [git_freshness.py](agents-remember/mcp/src/agents_remember/kernel/git_freshness.py) |
| The read-controller status vocabulary scanned out of `_resolve_onboarding`'s returned tuple. | `VALID_FILE_READ_STATUSES`, `_resolve_onboarding` | [read_files.py](agents-remember/mcp/src/agents_remember/controllers/read_files.py) |
| The one drift-status declaration now serving both the packet model and the tool response. | `status` dict literals in the drift summary | [summary.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py) |
| The refused-start result the `worktree_start` handler returns instead of raising, since it has no `except ContractError` either. | `invalid_contract_request_result` | [leaf_ref_start.py](agents-remember/mcp/src/agents_remember/worktrees/modules/leaf_ref_start.py) |
| The sibling conformance suite for MCP tool payloads, which this file is the wire-vocabulary counterpart of. | `ToolResponseConformanceTests` | [test_tool_response_conformance.py](agents-remember/mcp/tests/test_tool_response_conformance.py) |

## Cross-Repo References

The reviewed behaviour is wholly repository-local: every producer, every wire model and every
docstring this suite reads lives in `mcp/src/agents_remember/`. Imports were reviewed at
L111-L155; none crosses a repository or external-system boundary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found — the whole import surface is same-repository. | L111-L155 | [test_wire_vocabulary_exhaustiveness.py](agents-remember/mcp/tests/test_wire_vocabulary_exhaustiveness.py) |

## Update History

- 2026-08-01T08:35+02:00 — 260731-EFA-L4 curator: created for the new leaf-central wire-vocabulary
  suite. Recorded the three mechanisms and the honest answer to what the AST scan defends on its
  own — **nothing**: the module docstring states the scan reads bare string literals and that "any
  claim that the scan alone keeps a vocabulary honest would be false, and was" (L12-L16), and the
  six spellings that evade it are named (concatenation, f-string, dict subscript, imported name,
  local bound elsewhere, `cast`). The brief that commissioned this card described the
  `WHAT DEFENDS WHAT` table as carrying a row reading "**nothing** — the AST scan alone"; the table
  at L18-L40 has no such row — all four of its rows name pyright (three) or the runtime
  `_task_vocabulary` narrowing (one), and the scan appears only as the measurement laid beside
  them. This card states what the source says. Recorded `ProducedLiteralTests`' derivation from the
  producers' source rather than from the alias (`produced_literals`, L324-L339), the two rules that
  make pyright total — no `dataclasses.replace` may carry one of the six contract-cell keywords
  (L659-L667; `contract_cells_written_through_replace`, L348-L375; typeshed's `**changes: Any` is
  the reason), and every value at a typed writer must be a statically readable expression
  (L683-L692; `unreadable_contract_writes`, L394-L408) — plus the declaring-module exemption
  (L185), `AdvertisedVocabularyTests`' docstring-by-AST reading (L823-L881; `_advertised_statuses`
  L615-L632; `_advertised_workflow_kinds` L1255-L1260) including the pinned
  `{"leaf-ref-not-found", "leaf-ref-ambiguous"}` difference, and the behavioural halves
  (`GuidanceWalkTests` L241-L305, `RecoveryGuidanceTests` L884-L919, `ContractBoundaryTests`
  L922-L1222, `ProducerWireCrossingTests` L1225-L1252). Every line range was read off the current
  1264-line source. Verification metadata pinned to the pre-leaf source authority
  (`abc7cbcc74921cdcb57a61529445f61641e919e7`) as a placeholder until closeout stamps the L4 code
  commit — this source file is new and not yet committed.
