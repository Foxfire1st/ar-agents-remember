# mcp/src/agents_remember/kernel/coordination_context/models.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/models.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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
`CoordinationContext` dataclass used by controllers and integrity tools.

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `MissingMemoryError` subclasses the typed `AgentsRememberError` base instead of bare `ValueError`. | error base import | [errors.py](agents-remember/mcp/src/agents_remember/errors.py) |
| Resolver assembly returns `CoordinationContext` instances defined here. | resolver assembly | [resolver.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/resolver.py) |
| Serialization converts these models to JSON-safe dictionaries. | serialization | [serialize.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/serialize.py) |

## Cross-Repo References

No cross-repository evidence is needed for local model declarations.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

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
