# mcp/src/agents_remember/kernel/coordination_context/ — Coordination Context Modules

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

The package resolves the coordination context of a code repository: which memory root the repository uses,
where its settings, task, system and docs roots are, which storage and path rules apply, which adjacent
repositories are admitted as sources, and the facts of the worktree contract a request selects. It reads
only: it creates no memory root, changes no Git worktree and writes no onboarding. The facade
`agents_remember.kernel.coordination_context_resolver` re-exports the package's functions and models and
passes the resolution request into this package.

## Hot Path Summary

`resolve_coordination_context(code_repository_name, workspace_root, code_repository_root, *, request)`
takes one `CoordinationRequest`. It resolves the code repository, selects the onboarding-hint route or the
root-selection route, parses settings, and calls `build_coordination_context` to assemble the answer.

- With `hints.onboarding_root`, the supplied onboarding path selects its own route. Topology is inferred
  from that path; settings supply the coordination and memory roots. A memory-worktree hint can select
  settings from the official memory repository. A loaded contract can subsequently select the effective
  memory root and its existing onboarding and docs children.
- Without that hint, `detect_coordination_selection` uses an explicit settings path when supplied;
  otherwise it selects the external root `<coordination root>/memory-repos/ar-<name>` when it exists.
  A missing selected memory root raises `MissingMemoryError`, whose message names the coordination root
  and default external root checked by selection.
- Settings are JSON first. For settings outside the coordination-root settings location, the JSON
  candidate is the sibling `settings.json`. For coordination-root settings, it is the user's settings
  file returned through the user-settings location guard. If the JSON candidate exists, only it is
  parsed. Otherwise the fenced blocks of the selected Markdown settings file are parsed; a missing
  Markdown file gives defaults.
- Contract lookup tries an explicit contract path, then a task selector, then a worktree selector when
  the previous lookup supplied no candidate. An absent candidate, or a load failure other than the canonical-place check,
  produces no loaded contract while retaining its candidate path in the result; a candidate path that is not the
  contract's own canonical place propagates a named refusal that states the found and recorded paths rather than
  falling through to the next selector.
- `build_coordination_context` takes the task root, worktree group, memory mode, code and memory
  worktrees, and ledger path from a loaded contract. Without one, it derives the task root and worktree
  group from the selector when present, otherwise uses the repository task root and no worktree group;
  the memory mode defaults to `external`.
- `resolve_cross_repo_entry` gives each allowed adjacent repository one of three states. `excluded`:
  the entry is invalid, code inclusion is disabled, its code path is missing, or its code repository is
  detached, is not a Git repository, or is not on the expected branch. `included-code-only`: memory
  inclusion is off, the memory repository is missing or on another branch, or its ledger raises
  `LedgerError`. `included`: code and memory both pass, and the ledger's last verified code commit and
  last memory content commit are attached.

## How It Is Built

- [models.py](models.py.md): the data of a resolution. `CoordinationRequest` carries the hints, the
  selector and the contract reader of one request; `CoordinationHints` and `EnclosureSelector` are its two
  parts; `CoordinationSelection`, `CoordinationRoots` and `CodeRepository` are intermediate results;
  `CoordinationContext` is the answer. `ContractReaderPort` is the contract-file surface the resolver may
  use, so that the kernel imports nothing from the `worktrees` package.
- [paths.py](paths.py.md): where the coordination root, a memory root, a settings file and an onboarding
  card live, and which onboarding roots are supported memory locations.
- [resolver.py](resolver.py.md): selects the memory root and assembles the context.
- [settings.py](settings.py.md): chooses the settings file to parse. [json_settings.py](json_settings.py.md)
  parses `settings.json`; [markdown_settings.py](markdown_settings.py.md) parses the fenced settings blocks
  of `settings.md` line by line, with the steps of two of its blocks in
  [markdown_cross_repo.py](markdown_cross_repo.py.md) and
  [markdown_global_rules.py](markdown_global_rules.py.md); [setting_values.py](setting_values.py.md)
  checks single values.
- [storage.py](storage.py.md): which storage a source file gets under the path rules.
- [contracts.py](contracts.py.md): finds and loads the contract a request selects, through the port.
- [cross_repo.py](cross_repo.py.md): resolves each allowed adjacent repository to a state with its reason.
- [serialize.py](serialize.py.md): the context as a dictionary and as text rows.

### Recorded Reads

The recorded portions of root selection, settings selection and parsing, and contract lookup use the
kernel's read recorder ([recorded_reads.py](../recorded_reads.py.md)). `observed_text` records the SHA-256
of the exact bytes consumed, or an absent or unreadable input. `observed_exists` records a negative
existence probe but does not record a successful probe by itself. `observed_resolve` records a logical
path and its resolved target; `observed_path_exists` records both present and absent path predicates.

- Inside a recording block these operations leave rows describing the observations. A caller that
  checks those rows before reusing a kept result can detect changed consumed settings, the appearance
  of a previously absent higher-priority settings file, a recorded memory root appearing or
  disappearing, or a recorded root link being retargeted even when its new target has identical bytes.
  Reuse and recomputation belong to the caller; the recorder does not recompute results itself.
- Outside a recording block the same functions record nothing and perform their underlying reads,
  probes and resolutions normally. `observed_text` reads raw bytes, decodes UTF-8 and normalizes line
  endings; it does not simply delegate to `Path.read_text`.
- Recording blocks are opened by the reviewer's leaf-wide worklist computation and its memo
  (`application/reviewer_worklist_child.py`, `application/review_tree_knowledge.py`,
  `application/review_leaf_view_memo.py`), by the invariant gate (`application/knowledge_gate/gate.py`)
  and by the leaf-document lookup (`tasks/leaf_decisions.py`).
- The onboarding-hint route uses plain calls for its initial onboarding and explicit-settings
  resolutions and some settings-inference probes, but its downstream memory-root inference and
  external-root derivation use recorded resolutions. The child-root, system-root and final
  path-settings existence probes inside `build_coordination_context`, and the adjacent-repository
  path probes and Git metadata operations, are not recorded by those operations. Settings parsers,
  contract candidate resolution and negative probes, the production contract loader, and the
  adjacent-repository memory-ledger loader still record the observations they make. The injected
  contract reader determines how its own lookups and loads are observed.

## Invariants And Boundaries

- A resolution request without a contract reader is refused with `ValueError`; context construction
  independently enforces the same requirement. A contract is read through `ContractReaderPort`, and the
  package imports nothing from `worktrees`.
- The supported topology is `external`. An explicit request for `internal` is refused by name. Selection
  without an explicit settings path also refuses an existing `<code root>/ar-memory`; settings-root and
  onboarding-root inference refuse their detected `ar-memory` layouts. An explicit settings path takes
  precedence over the repository-side legacy-root check.
- Onboarding topology inference admits an official memory-repository layout whose parent name starts
  with `ar-` under `memory-repos`, or the structurally decoded
  `<coordination root>/worktrees/<repository>/<group>/memory-<name>/onboarding` layout. Unsupported paths
  receive a refusal naming the two supported locations. The official-repository branch checks the
  parent layout; unlike the memory-worktree decoder, it does not independently check the final path
  component's name.
- `resolve_storage_for_source` answers the storage of one source file. Without path rules it returns
  `settings.mode`, except that `hybrid` uses `settings.default` or `external`. With rules, the first rule
  whose base and inclusion predicates match decides: an exclusion returns `disabled`; otherwise a
  non-hybrid mode returns `settings.mode`, while hybrid uses the rule's storage or its configured
  default. A file no rule matches is `disabled` unless the mode is `hybrid`, which uses its default or
  `external`.
- The package states facts. Creating or repairing a memory root belongs to the skills that
  `MissingMemoryError` names. The resolver consumes its arguments, selected settings, contract-reader
  results and adjacent-repository Git and ledger facts; it reads no `.env` file itself.
- A loaded contract's memory mode is reported as recorded, including a readable legacy `disabled`
  value. That reported metadata is outside the resolver's operative promises: context resolution does
  not establish lifecycle permission or a current task status.

## Evidence

- The facade passes one request to the resolver. [3]
- The request: hints, selector and contract reader. [4]
- The contract-file surface the resolver may use. [5]
- A request without a contract reader is refused; an onboarding-root hint selects its own path. [6]
- Root selection: explicit settings, the removed repository root, the external root, the missing-memory error. [7]
- The context takes task root, worktree group, memory mode, worktrees and ledger path from the contract. [8]


- The memory mode a topology implies. [9]


- The memory-worktree shape, decoded segment by segment. [10]
- The two supported onboarding roots and the refusal that names both. [11]
- JSON candidate first, then the Markdown blocks, using recorded readers and probes. [12]


- Storage of one source file under the path rules. [13]
- Storage from one rule: not matched, excluded, or the rule's storage. [14]
- The states of an adjacent repository's code side. [15]
- The states of its memory side. [16]
- The ledger state of an included memory repository. [17]

- An explicit contract candidate is resolved through the recorder; candidate absence is recorded. [18]



- A path resolution as a recorded selection row. [19]
- A path's existence as a recorded selection row. [20]

- A skipped settings file of higher priority and a JSON-only settings file are recorded. [21]
