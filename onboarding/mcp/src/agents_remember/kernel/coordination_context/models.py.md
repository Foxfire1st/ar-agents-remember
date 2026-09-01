# mcp/src/agents_remember/kernel/coordination_context/models.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/models.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a` |
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`models.py` owns the dataclasses and typed dictionaries returned or consumed by
the coordination-context resolver.

## Code Commentary

### Logic

The module defines missing-memory errors, storage/path-rule model types,
cross-repo allow state, coordination selection, and the final
`CoordinationContext` dataclass (cit:(["class CoordinationContext"], mcp/src/agents_remember/kernel/coordination_context/models.py:179-179)).

`CoordinationContext.memory_mode` uses the shared `MemoryMode` alias declared here by
260731-EFA-L9 (cit:(["MemoryMode = Literal"], mcp/src/agents_remember/kernel/coordination_context/models.py:209-209))
and used by the field declaration (cit:(["memory_mode: MemoryMode"], mcp/src/agents_remember/kernel/coordination_context/models.py:201-201)).
The resolver assembly is named by **`build_coordination_context`** and selects the contract's mode
when a contract exists, otherwise calling `_memory_mode(roots.topology)` as its fallback
(cit:(["memory_mode = contract.memory_mode if contract is not None else _memory_mode(roots.topology)"], mcp/src/agents_remember/kernel/coordination_context/resolver.py:299-299)).

Since 260731-EFA-L2 it also owns the **four frozen parameter objects the resolver's public API is
signed on**. They are the vocabulary of coordination-context resolution; a caller building one is
answering one question, not filling in a keyword list:

- **`EnclosureSelector(contract_path=None, task_name=None, parent_task=None, leaf_id=None,
  worktree_name=None)`** — *how a caller names the enclosure to resolve*. Either directly, by
  `contract_path`, or indirectly: a task (with `parent_task` to disambiguate a repeated task name)
  plus the leaf id or worktree name that picks one enclosure inside it. A caller supplying a subset
  is still supplying one selector, and the whole set travels from the tool boundary down to
  `resolve_contract` unchanged.
- **`CoordinationHints(topology=None, coordination_root=None, settings_path=None,
  onboarding_root=None)`** — *what a caller already knows about where the coordination tree is*.
  Every field is a hint, not a fact: a requested topology overrides detection, an explicit
  coordination root or settings file short-circuits the search, and an `onboarding_root` selects
  the from-onboarding resolution path entirely. Detection fills in whatever is absent.
- **`CodeRepository(name, root, workspace)`** — a resolved code repository. This replaces the
  untyped `dict[str, Path | str]` the resolver used to pass around, which forced `Path(repo["root"])`
  / `str(repo["name"])` casts at every read.
- **`CoordinationRoots(topology, coordination_root, memory_root, onboarding_root, settings_path)`**
  — the coordination tree after resolution: which topology won and the four roots it implies.
  Detection produces them together and no reader wants a subset.

All four are re-exported from the `kernel.coordination_context_resolver` facade.

### Invariants And Boundaries

- Models should stay behavior-light and importable by parser, resolver, and
  serialization modules.
- **`memory_mode` uses the shared vocabulary.** `MemoryMode`, cit:(["MemoryMode ="], mcp/src/agents_remember/kernel/coordination_context/models.py:209-209), is the kernel-side declaration (moved from `worktrees.worktree_contract` by L9), and `resolver.build_coordination_context`, cit:(["def build_coordination_context"], mcp/src/agents_remember/kernel/coordination_context/resolver.py:272-272), is the current assembly entry point.
- The four parameter objects are frozen and fully defaulted, so a resolver call that supplies
  neither `hints` nor `selector` still resolves — `None` is replaced by an empty instance rather
  than branching on absence.
- `MissingMemoryError` subclasses `AgentsRememberError` (imported from
  `agents_remember.errors`), so it joins the package's typed error family while
  staying catchable by existing `except ValueError` handlers. It keeps the
  checked internal and external memory paths so callers can report actionable
  initialization guidance, naming the skills in full — initialize memory with
  `c-00-initialize-memory-repo`, then run `c-03-repo-bootstrap`.

## Docs References

No external documentation is needed for these package-local data models.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `MissingMemoryError` subclasses the typed `AgentsRememberError` base. | `MissingMemoryError` | mcp/src/agents_remember/kernel/coordination_context/models.py:10-29 |
| `AgentsRememberError` remains a `ValueError`-compatible base. | `AgentsRememberError` | mcp/src/agents_remember/errors.py:18-19 |
| Resolver assembly returns `CoordinationContext` instances defined here, reading `contract.memory_mode` straight into the field and falling back to the topology only when there is no contract. | `build_coordination_context`; `_memory_mode` | mcp/src/agents_remember/kernel/coordination_context/resolver.py:268-313; mcp/src/agents_remember/kernel/coordination_context/resolver.py:342-343 |
| `MemoryMode` is the three-member memory vocabulary declaration (kernel-owned since L9). | "MemoryMode =" | mcp/src/agents_remember/kernel/coordination_context/models.py:209-209 |
| The wire face of the same value imports and uses the shared alias for `memory.mode`. | `MemorySummary` | mcp/src/agents_remember/models/context_packet.py:79-86 |
| Serialization converts these models to JSON-safe dictionaries. | `context_to_dict` | mcp/src/agents_remember/kernel/coordination_context/serialize.py:69-98 |

## Cross-Repo References

No cross-repository evidence is needed for local model declarations.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-04T15:56:39+02:00 — 260731-EFA-L6 S18-B10 curator: closed same-reviewer residual D18 by binding the resolver prose to the operative contract-or-topology conditional call; rechecked this card through the locked exact-document fixer/check.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T10:45+02:00 — 260731-EFA-L4 curator (post-wave source change): corrected the current source-backed resolver symbols. `resolver.build_coordination_context`, cit:(["def build_coordination_context"], mcp/src/agents_remember/kernel/coordination_context/resolver.py:272-272), and `_memory_mode`, cit:(["def _memory_mode"], mcp/src/agents_remember/kernel/coordination_context/resolver.py:366-366), are the current named entries. The card's current dataclass and shared `MemoryMode` references were rechecked; no historical symbol-walk claim is retained. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-08-01T10:02+02:00 — 260731-EFA-L4 curator: body updated to record the shared
  `MemoryMode`, cit:(["MemoryMode ="], mcp/src/agents_remember/kernel/coordination_context/models.py:209-209),
  and the current resolver assembly, cit:(["def build_coordination_context"], mcp/src/agents_remember/kernel/coordination_context/resolver.py:272-272).
  The matching invariant and wire-facing `MemorySummary` reference remain in this card.
  Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions): added
  the four frozen parameter objects the resolver API is now signed on — `EnclosureSelector`,
  `CoordinationHints`, `CodeRepository`, `CoordinationRoots`. `CodeRepository` replaces the
  untyped `dict[str, Path | str]` the resolver passed between its private helpers. Additive to
  this module; the signature change lands in `resolver.py` and the
  `coordination_context_resolver` facade. Verification metadata pinned until closeout stamps the
  L2 commit.
- 2026-06-02T16:24+02:00 — Normalized skill references in the missing-memory guidance message to full lowercase skill names (`c-00-initialize-memory-repo`, then `c-03-repo-bootstrap`); previously abbreviated C-00/C-03. Reference-style normalization; behavior unchanged.
- 2026-05-31T12:50+02:00 — `MissingMemoryError` now subclasses `AgentsRememberError` (imported from `agents_remember.errors`) instead of the builtin `ValueError`; updated Invariants And Boundaries to state the typed-error-family base and `except ValueError` compatibility, and added the errors.py repo-internal reference (1.0.0 review remediation).
- 2026-05-25T20:57+02:00: Created by extracting coordination-context model declarations from the monolithic resolver.
