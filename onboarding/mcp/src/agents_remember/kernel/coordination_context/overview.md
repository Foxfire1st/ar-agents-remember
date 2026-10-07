# mcp/src/agents_remember/kernel/coordination_context/ — Coordination Context Modules

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

The package resolves the coordination context of a code repository: which memory root the repository uses,
where its settings, task, system and docs roots are, which storage and path rules apply, which adjacent
repositories are admitted as sources, and the facts of the worktree contract a request selects. It reads
only: it creates no memory root, changes no Git worktree and writes no onboarding. Callers outside the
package import from the facade `agents_remember.kernel.coordination_context_resolver`, which re-exports
the package's functions and models.

## Modules

- [models.py](models.py.md): the data of a resolution. `CoordinationRequest` carries the hints, the
  selector and the contract reader of one request; `CoordinationHints` and `EnclosureSelector` are its two
  parts; `CoordinationSelection`, `CoordinationRoots` and `CodeRepository` are intermediate results;
  `CoordinationContext` is the answer. `ContractReaderPort` is the contract-file surface the resolver may
  use, so that the kernel imports nothing from the `worktrees` package.
- [paths.py](paths.py.md): where the coordination root, a memory root, a settings file and an onboarding
  card live, and which onboarding roots are supported memory locations.
- [resolver.py](resolver.py.md): selects the memory root and assembles the context.
- [settings.py](settings.py.md): chooses the settings file to parse. [json_settings.py](json_settings.py.md)
  parses `settings.json`; [markdown_settings.py](markdown_settings.py.md) parses the fenced settings block
  of `settings.md` line by line, with the steps of two of its blocks in
  [markdown_cross_repo.py](markdown_cross_repo.py.md) and
  [markdown_global_rules.py](markdown_global_rules.py.md); [setting_values.py](setting_values.py.md)
  checks single values.
- [storage.py](storage.py.md): which storage a source file gets under the path rules.
- [contracts.py](contracts.py.md): finds and loads the contract a request selects, through the port.
- [cross_repo.py](cross_repo.py.md): resolves each allowed adjacent repository to a state with its reason.
- [serialize.py](serialize.py.md): the context as a dictionary and as text rows.

## Resolution

`resolve_coordination_context(code_repository_name, workspace_root, code_repository_root, *, request)`
takes one `CoordinationRequest`. A request without a contract reader is refused with `ValueError`.

- With `hints.onboarding_root`, the context is built from that root. The root must be one of the two
  supported locations: `<coordination root>/memory-repos/ar-<name>/onboarding`, or a memory worktree
  `<coordination root>/worktrees/<repository>/<group>/memory-<name>/onboarding`.
- Without it, `detect_coordination_selection` selects the root: an explicit settings path decides when
  given; otherwise the external root `<coordination root>/memory-repos/ar-<name>` is selected when it
  exists. A missing root raises `MissingMemoryError`, which names the coordination root and the external
  root that were checked.
- The only topology is `external`. A request for `internal`, a root `<code root>/ar-memory` and a settings
  file under a directory named `ar-memory` are refused as the removed mode, by name.
- `build_coordination_context` takes the task root, the worktree group, the memory mode, the two worktrees
  and the ledger path from the contract when the request selects one that loads. Without a contract the
  memory mode is the one the topology implies (`external`).

## Settings, Storage And Adjacent Repositories

- Settings are JSON first: when the sibling `settings.json` of a settings path exists, it is the only file
  parsed. Otherwise the fenced blocks of `settings.md` are parsed, and a missing file gives the defaults.
- `resolve_storage_for_source` answers the storage of one source file. Without path rules it is the
  default of the storage settings. With rules, the first rule that includes the file decides, a file a
  rule excludes is `disabled`, and a file no rule matches is `disabled` unless the mode is `hybrid`.
- `resolve_cross_repo_entry` gives every allowed adjacent repository one of three states. `excluded`: the
  entry is invalid, its code path is missing, or the code repository is not on the expected branch.
  `included-code-only`: memory inclusion is off, the memory repository is missing or on another branch, or
  its ledger does not load. `included`: code and memory both pass, and the ledger's last verified code
  commit and last memory content commit are attached.

## Recorded Reads

The file and path operations of root selection, settings selection and parsing, and the contract lookup go
through the kernel's read recorder ([recorded_reads.py](../recorded_reads.py.md)): `observed_text` for a
file's bytes, `observed_exists` for the probe of a file (a missing file is recorded as `absent`), and
`observed_resolve` and `observed_path_exists` for the resolution and existence of a path that selects
which file is read.

- Inside a recording block each of them leaves a row with the result: the SHA-256 of the bytes read,
  `absent`, `unreadable (...)`, or the target a path resolved to. A result that is kept together with these
  rows is recomputed when a settings file changes, a settings file of higher priority appears, a memory
  root appears or disappears, or a root link is retargeted, also when the new target holds identical
  bytes.
- Outside a recording block the same functions record nothing and answer as the plain `Path` calls do, so
  a caller that opens no block sees the same answers and the same errors.
- Recording blocks are opened by the reviewer's leaf-wide worklist computation and its memo
  (`application/reviewer_worklist_child.py`, `application/review_tree_knowledge.py`,
  `application/review_leaf_view_memo.py`), by the invariant gate (`application/knowledge_gate/gate.py`)
  and by the leaf-document lookup (`tasks/leaf_decisions.py`).
- The path through an onboarding-root hint, the fallbacks inside `build_coordination_context` and the
  adjacent-repository resolution use plain path calls for their own probes and resolutions and record
  nothing for those operations; what they consume downstream is still recorded — the settings parsers,
  the recorded contract resolver and the included-memory adjacent-repository ledger loader record their
  reads (or their absence or failure).

## Boundaries

- The package states facts. Creating or repairing a memory root belongs to the skills that
  `MissingMemoryError` names.
- The resolver's inputs are its arguments and the settings files it selects; it reads no `.env` file.
- A contract is read only through `ContractReaderPort`; the package imports nothing from `worktrees`.

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
- JSON sibling first, then the Markdown blocks, with every probe and read recorded. [12]
- Storage of one source file under the path rules. [13]
- Storage from one rule: not matched, excluded, or the rule's storage. [14]
- The states of an adjacent repository's code side. [15]
- The states of its memory side. [16]
- The ledger state of an included memory repository. [17]
- The contract candidate is resolved and probed through the recorder. [18]
- A path resolution as a recorded selection row. [19]
- A path's existence as a recorded selection row. [20]
- A skipped settings file of higher priority and a JSON-only settings file are recorded. [21]
