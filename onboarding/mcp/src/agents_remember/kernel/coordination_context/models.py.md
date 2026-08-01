# mcp/src/agents_remember/kernel/coordination_context/models.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/models.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T10:45+02:00                     |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
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
`CoordinationContext` dataclass (L131-L158) used by controllers and integrity
tools.

`CoordinationContext.memory_mode` (L153, with the explanatory comment at
L148-L152) is `MemoryMode`, **imported** from `worktrees.worktree_contract`
(L51 there) rather than re-spelled as
`Literal["internal", "external", "disabled"]` as it was until 260731-EFA-L4. The
import direction follows the data: **`resolver.build_coordination_context`**
(`resolver.py` L268-L313) reads `contract.memory_mode` straight into this field
at **line 284**, falling back to `_memory_mode(roots.topology)` (L342-L343) only
when there is no contract in scope. So the vocabulary genuinely *is* the
contract's, and the kernel copy was a third spelling of it.
(`models.context_packet.MemorySummary.mode` was the fourth, and that one had
drifted — it lacked `disabled`, so a packet could report
`worktree.memoryMode="disabled"` and fail `memory.mode` on the same value.) This
is a deliberate `kernel` → `worktrees` import: the contract file is the artefact
that persists the value, so it is where the vocabulary is declared.

Note the fallback's narrower type: `_memory_mode` returns
`Literal["internal", "external"]` — a contract-free resolution can never produce
`disabled`, because only a contract records that choice. `disabled` therefore
reaches this field exclusively through `contract.memory_mode`, which is a second
reason the alias belongs to the contract module rather than here.

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
- **`memory_mode` is not this module's vocabulary to declare.** It is
  `worktrees.worktree_contract.MemoryMode`, because the contract file is what
  persists the value and `resolver.build_coordination_context` copies it here
  unchanged (`resolver.py` line 284). Re-spelling it locally is what let four
  copies of one three-member enum exist, one of them missing a member. There is
  no `resolver._resolve` — an earlier version of this comment named one, and the
  function does not exist in `resolver.py`.
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
| Resolver assembly returns `CoordinationContext` instances defined here, reading `contract.memory_mode` straight into the field and falling back to the topology only when there is no contract. | `build_coordination_context` L268-L313 (the read at L284); `_memory_mode` L342-L343 | [resolver.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/resolver.py) |
| `MemoryMode` — the single declaration of the three-member memory vocabulary, beside the contract file that persists it, with `VALID_MEMORY_MODES` derived from it. | L51; L60 | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| The wire face of the same value, which now imports the same alias for `memory.mode` — and used to be the copy that lacked `disabled`. | `MemorySummary.mode` L85 | [models/context_packet.py](agents-remember/mcp/src/agents_remember/models/context_packet.py) |
| Serialization converts these models to JSON-safe dictionaries. | serialization | [serialize.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/serialize.py) |

## Cross-Repo References

No cross-repository evidence is needed for local model declarations.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-01T10:45+02:00 — 260731-EFA-L4 curator (post-wave source change): the comment on
  `memory_mode` was rewritten after the 10:02 entry below, and both it and this card had cited a
  function that **does not exist**. `resolver._resolve` is not defined anywhere in
  `resolver.py` (checked by symbol walk over the module). The real reader is
  `resolver.build_coordination_context` (L268-L313), and the assignment is at **line 284**:
  `memory_mode = contract.memory_mode if contract is not None else _memory_mode(roots.topology)`.
  Corrected the reference in Code Commentary, in the invariant, and in the reference row, and left
  an explicit note that no `resolver._resolve` exists so the name is not reintroduced. Recorded the
  fallback the new comment names — `_memory_mode(roots.topology)` (L342-L343) when there is no
  contract — and added the consequence it makes visible: that helper returns
  `Literal["internal", "external"]`, so `disabled` can only reach this field through
  `contract.memory_mode`, which is a second reason the alias belongs to the contract module.
  **Citation repairs:** the four added comment lines shifted the dataclass, so `CoordinationContext`
  L130-L156 → **L131-L158** and `memory_mode` L151 → **L153**. Re-checked and still landing:
  `worktree_contract.py` L51 / L60 and `models/context_packet.py` `MemorySummary.mode` L85.
  Verification metadata pinned until closeout stamps the L4 commit.
- 2026-08-01T10:02+02:00 — 260731-EFA-L4 curator: body updated.
  `CoordinationContext.memory_mode` (L151) changed from a locally re-spelled
  `Literal["internal", "external", "disabled"]` to `MemoryMode` imported from
  `worktrees.worktree_contract` (L51 there) — the module that persists the value, which
  `resolver._resolve` copies here unchanged. The card's Logic section had not mentioned the field
  at all, so the third copy of a four-copy enum was invisible in onboarding; recorded it, recorded
  that the fourth copy (`models.context_packet.MemorySummary.mode`) was the one that had drifted
  by lacking `disabled`, and noted that the `kernel` → `worktrees` import direction is
  deliberate. Added the matching invariant. Citations: `CoordinationContext` pinned to L130-L156
  and `memory_mode` to L151; the resolver row now names `_resolve` and what it reads, and rows
  were added for `worktree_contract.py` (L51, L60) and `models/context_packet.py` (L85).
  Verification metadata pinned until closeout stamps the L4 commit.
  **[Superseded 2026-08-01T10:45+02:00 — this entry names `resolver._resolve`, which does not
  exist. The reader is `resolver.build_coordination_context`, line 284. See the entry above.]**
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
