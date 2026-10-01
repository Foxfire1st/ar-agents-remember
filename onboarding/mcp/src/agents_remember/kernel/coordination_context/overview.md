# mcp/src/agents_remember/kernel/coordination_context/ — Coordination Context Modules

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/kernel/coordination_context/` |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`coordination_context/` contains the extracted implementation for the `c-08-ar-coordination-context-resolver` skill
package resolver. The public import and `python -m` entrypoint remain
`agents_remember.kernel.coordination_context_resolver`, while this package owns
the focused resolver, settings, storage, contract, cross-repo, serialization,
and CLI responsibilities.

## Hot Path Summary

Start in `resolver.py` for topology and context assembly, `settings.py` for
JSON-first settings selection, `json_settings.py` and `markdown_settings.py`
for settings formats, `markdown_cross_repo.py` and
`markdown_global_rules.py` for legacy Markdown parser branches, `storage.py`
for path-rule eligibility, `cross_repo.py` for branch-gated adjacent repo facts,
`contracts.py` for root/leaf series-contract fact loading, and `serialize.py` plus
`cli.py` for output adapters.

## Route Model

The package is intentionally split by responsibility:

- `models.py` owns dataclasses and typed dictionaries — with one deliberate exception since
  260731-EFA-L4: `CoordinationContext.memory_mode` (line 151) is no longer an independently
  declared `Literal["internal", "external", "disabled"]` but
  `worktrees.worktree_contract.MemoryMode`, imported at line 8. The two were the same three
  members, written twice, and this package is a *consumer* of that vocabulary rather than an
  author of it: `resolver._resolve` assigns `contract.memory_mode` straight into the field
  (line 284, reaching the constructor at line 307) whenever a contract is in scope, and falls
  back to `_memory_mode(topology)` (line 342, `internal`/`external` only — a resolved context
  is `disabled` only because a contract said so) when none is. Retype it here and the two
  copies can disagree again, which is a type error at line 284 in the good case and, in the
  bad one, a value this dataclass accepts that the contract writer refuses.
- `paths.py` owns path/topology primitives.
- `resolver.py` composes a `CoordinationContext` without performing mutation.
- `settings.py` chooses JSON settings over Markdown fallback and delegates
  concrete parsers.
- `json_settings.py`, `markdown_settings.py`, and `setting_values.py` own
  settings parsing details.
- `markdown_cross_repo.py` and `markdown_global_rules.py` keep the Markdown
  parser below complexity and maintainability thresholds.
- `storage.py` owns storage/path-rule decisions.
- `contracts.py` and `cross_repo.py` load external facts used by the resolver; contract lookup goes through active task-root resolution plus alias-aware leaf-enclosure resolution, excluding archived task roots.
- `serialize.py` and `cli.py` adapt the context to text/JSON output.

## Invariants And Boundaries

- `c-08-ar-coordination-context-resolver` skill remains facts-only; this package does not create memory roots, modify
  Git worktrees, or write onboarding.
- MCP settings and explicit arguments are resolver authority; source-checkout
  `.env` and `.env.example` are not runtime coordination-root inputs.
- The facade preserves the public resolver import path and selected test seams,
  but implementation code belongs in the focused modules.
- Settings parsing is JSON-first; Markdown fenced settings are accepted only
  when a sibling `settings.json` is absent.

## Evidence

### Repo-Internal References

- The package-local facade keeps existing callers pointed at the split implementation. [1]
- The current resolver constructs the context; retired parity suites provide no current pass. [2]

## 260731-EFA-L2 Resolver API

`resolve_coordination_context` is now
`(code_repository_name=None, workspace_root=None, code_repository_root=None, *, hints:
CoordinationHints | None = None, selector: EnclosureSelector | None = None)`. The nine former
resolution arguments live on the two frozen bundles in `models.py`, which also owns
`CodeRepository` (replacing the untyped repo dict the private helpers passed around) and
`CoordinationRoots`. `build_coordination_context(repo, *, roots, storage, cross_repo, selector)`
and `contracts.resolve_contract(selector, coordination_root, code_repository_name)` match. All four
models are re-exported from the `kernel.coordination_context_resolver` facade, which is the
supported import path for callers outside this package. Resolution order, the onboarding-root
branch and contract-lookup precedence are unchanged.

## 260731-EFA-L9 Route Impact

The resolver CLI moved to `cli/coordination_resolver.py` (the `cli` package sits above kernel),
and the resolver now consumes a `ContractReaderPort` bound to
`worktrees/modules/contract_reader.py::WorktreeContractReader` instead of importing worktrees
directly. The coordination-context detection/assembly behavior is unchanged.

## 260915-KS-L23 The Second Supported Memory Shape, And The Refusal That Now Names It

`paths.py` had one topology inference and one refusal, and the refusal named a single supported
shape — `<ar-coordination>/memory-repos/ar-<code-repository-name>/onboarding`. That was **false as a
general statement**: a leaf enclosure's memory worktree is a memory root the product itself uses,
because the contract-scoped memory-quality route takes its onboarding root from the *contract*
rather than from this resolver. The practical cost (D-34, item 27) was that a curator wanting the
package-local checker's answer for a leaf — rather than the whole checklist's, which arrives by the
MCP tool under D-33's fixed serving build — had no route at all.

The route now decodes the second shape **structurally** and states both:

- `memory_worktree_enclosure(onboarding_root)` (`paths.py`) returns
  `(coordination_root, code_repository_name)` for
  `.../worktrees/<repo>/<group>/memory-<name>/onboarding`, and `None` for anything that does not match
  every segment — a directory that merely happens to be named `memory-something` earns no acceptance,
  and the name segment must be longer than the bare prefix.
- `infer_topology_from_onboarding_root` returns `"external"` for it, which is what the memory
  genuinely is: external to the code repository.
- `infer_settings_path` resolves a memory worktree's settings to the **official** memory repo's
  `system/settings.md`, because a memory worktree carries no `system/` of its own; an unknown
  worktree falls back to the older context-root inference so it reports the missing file rather than
  resolving to another repository's settings.
- The refusal (`ValueError`) now names **both** supported shapes, says which one the
  contract-scoped route already measures, and echoes the received path.

**What this does not change.** Resolution order, the onboarding-root branch, contract-lookup
precedence, the facts-only boundary, settings authority and the L2 `hints=`/`selector=` API are all
untouched; this is one accepted shape added to one inference, and one error message made true. The
consumer is `memory_quality/integrity/check_missing_onboarding.py`, which carries its own sidecar.
