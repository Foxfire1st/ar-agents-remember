# Code Shape and Refactor Discipline

## Design Philosophy

Agents Remember is a memory and onboarding system. The codebase must therefore be easy for both humans and agents to navigate.

The rule is not: "Put the new logic wherever the nearby logic already lives."

The rule is: "Every meaningful concept gets a clear home, and files must stay small enough that their purpose can be understood without re-reading half the project."

A source file is a local unit of ownership. It should usually explain one concept, one adapter boundary, one workflow step, one parser, one service, or one policy area. When a file grows because it has become the easiest place to append behavior, that is architecture drift.

Code structure must preserve these properties:

1. A developer can tell what a file owns from its path and name.
2. An agent can find the right file without scanning thousands of lines.
3. New behavior can be added without touching unrelated responsibilities.
4. Tests can target one behavior boundary without needing the whole system.
5. Onboarding notes can remain local and meaningful because the code file itself remains local and meaningful.

Large files are allowed only when they are explicitly boring: generated output, static data, fixtures, or intentionally centralized declarations. Large files containing branching behavior, orchestration, parsing, command handling, or policy decisions are not acceptable.

## File Size Budget

Treat these as hard review signals for Python source files:

| File size | Meaning | Required behavior |
|---:|---|---|
| 0-300 lines | Healthy default | Normal edits allowed. |
| 300-600 lines | Acceptable but watchful | New logic is allowed only if it fits the existing single responsibility. |
| 600-900 lines | Refactor pressure | Before adding logic, explain why this file is still the right home. Prefer extraction. |
| 900-1200 lines | Soft limit exceeded | Do not add new feature logic without also extracting something. |
| 1200+ lines | Hard limit exceeded | Stop and propose a split plan before adding behavior. |
| 2000+ lines | Architectural failure | Treat the file as a refactor target. New logic belongs elsewhere unless the developer explicitly approves an exception. |
| 4000+ lines | Emergency cleanup target | Do not append. Identify responsibilities, seams, and extraction order. |

The most important rule:

**No agent may make an already-too-large file larger merely because it was the fastest place to patch the task.**

## Function and Class Budget

Use these as defaults unless the file is a generated artifact or intentionally declarative data:

| Unit | Target | Hard pressure |
|---|---:|---:|
| Function / method | <= 40 lines | > 80 lines requires extraction or explanation |
| Class | <= 250 lines | > 400 lines requires split or explanation |
| Public methods per class | <= 10 | > 15 indicates too many responsibilities |
| Function arguments | <= 5 normal args | Use a dataclass/config object when arguments represent a concept |
| Local variables | <= 12 | Too many locals usually means hidden sub-steps |
| Nested blocks | <= 3 levels | Prefer guard clauses, extracted functions, or strategy objects |
| Cyclomatic complexity | <= 10 | > 10 requires simplification or explicit justification |

A long function is not fixed by adding comments. Comments can clarify intent, but extraction creates a reviewable boundary.

## Split Triggers

Create or use a separate module when any of these are true:

1. The new logic introduces a new noun:
   - resolver
   - validator
   - formatter
   - planner
   - registry
   - adapter
   - provider
   - policy
   - checker
   - parser
   - renderer
   - reporter

2. The new logic introduces a new lifecycle phase:
   - discovery
   - classification
   - validation
   - execution
   - reporting
   - closeout
   - migration
   - cleanup

3. The new logic introduces a new external boundary:
   - filesystem
   - Git
   - MCP transport
   - CLI
   - workspace settings
   - memory repo
   - worktree state
   - benchmark output

4. The existing file already owns two different concerns.

5. The existing file is above 600 lines and the new logic is not a tiny bug fix.

6. The new logic needs tests that would be clearer if aimed at a smaller unit.

## Responsibility Rules

A module should normally be one of these things:

### CLI adapter

Owns argument parsing, command wiring, and conversion into application calls.

Must not own core business logic.

### Application entry point

Owns high-level request flow.

May coordinate services.

Must not contain deep parsing, Git mechanics, filesystem traversal, or policy details inline.

### Service

Owns one domain operation.

May call lower-level helpers.

Must not know about CLI formatting or MCP transport details.

### Policy module

Owns decisions.

Examples:
- whether onboarding is stale
- whether a worktree is valid
- whether a memory update is allowed
- whether a file belongs to a checker category

Policy modules should be easy to test with plain inputs and outputs.

### Adapter / provider

Owns interaction with an external system.

Examples:
- Git command adapter
- filesystem adapter
- MCP adapter
- workspace adapter

Adapters should not decide business policy. They provide facts or perform requested operations.

### Parser

Owns conversion from text/files/process output into structured data.

Parsers should not perform side effects.

### Reporter / formatter

Owns display output.

Reporters should not perform discovery, mutation, or policy decisions.

### Model / dataclass

Owns structured state.

Models should not grow behavior-heavy methods unless that behavior is intrinsic to the model.

## Anti-Patterns

The following patterns are not acceptable:

1. "Just add one more helper at the bottom."
2. "This file already handles related things, so I added another related thing."
3. "The function was already long, so adding a few branches does not matter."
4. "I avoided creating a new file because that seemed heavier."
5. "I kept the logic inline so the reader can see everything in one place."
6. "I added comments instead of extracting the concept."
7. "I reused the application entry point because it already had access to all dependencies."
8. "I added another mode flag instead of creating separate strategies."
9. "I passed more booleans instead of introducing a request/options object."
10. "I changed unrelated logic because it was nearby."
11. Accidentally quadratic: superlinear cost from cross-layer composition — each layer looks O(1) or O(n) in isolation, but the composed call path (e.g. a sweep that re-reads a growing store per item) is O(n^2) or worse.
12. An unbounded append-only log without a named compactor: a store that only grows, with no declared cap, eviction policy, or retention owner landed in the same change that introduces it.

These are drift behaviors. Agents must call them out before continuing.

## Source Comment Scope

Source comments explain the technical **why** of the code and must stand alone for a maintainer who has only this repository.

1. Do not place task, leaf, decision-item, review, requirement, or audit identifiers in source comments.
2. Do not use conversation provenance such as who requested or ruled on a change, and do not point source comments at report or task paths.
3. Keep the technical constraint, evidence boundary, invariant, or trade-off that a future maintainer needs to preserve.
4. Product-role vocabulary is allowed when it names a real runtime role, and shipped `docs/design/` pointers are allowed when they explain the product contract.
5. Put workflow history and review provenance in Git history, task artifacts, and onboarding rather than source comments.

## Required Agent Behavior Before Editing

Before adding code to any Python file, inspect the current file shape.

If the target file is above 600 lines, the agent must state:

1. Current approximate file length.
2. Existing responsibility of the file.
3. Whether the new behavior belongs there.
4. Whether extraction is more appropriate.
5. The intended destination if a new module should be created.

If the target file is above 900 lines, the agent must not add new feature logic without a split plan.

If the target file is above 1200 lines, the default action is extraction, not extension.

If the task is urgent and the developer accepts a tactical patch, the agent must mark the file as a refactor follow-up and explain the smallest safe extraction seam.

## Refactor-First Rule for Large Files

When a large file must be changed, prefer this sequence:

1. Identify the smallest coherent responsibility inside the file.
2. Extract that responsibility into a named module.
3. Preserve public behavior.
4. Add or move tests around the extracted boundary.
5. Then apply the requested feature/fix through the new boundary.

Do not perform huge speculative rewrites. The preferred style is small, named extractions that make future work safer.

## Naming Rules for New Modules

Use boring names that describe ownership.

Good:

- `worktree_state.py`
- `worktree_registry.py`
- `memory_health.py`
- `onboarding_resolver.py`
- `drift_reporter.py`
- `quality_policy.py`
- `git_status_parser.py`
- `mcp_tool_registry.py`

Bad:

- `utils.py`
- `helpers.py`
- `common.py`
- `misc.py`
- `manager.py` without a precise noun
- `processor.py` without a precise noun
- `handler.py` without the event or boundary it handles

`utils.py` is allowed only for tiny, dependency-free primitives that are genuinely shared and have no domain ownership.

## Pydantic Response Model Construction

Public MCP response models should make nested structure explicit at construction time.

Do not rely on Pydantic constructor coercion by passing plain dictionaries or lists into nested model fields in application entry points, tool adapters, or response builders. That works at runtime, but it hides the response boundary from static analysis and makes model contracts harder to inspect.

Use these patterns instead:

1. For locally assembled response data, construct the nested model directly.

```python
packet = ContextPacketV2(
    ok=True,
    repo=RepoSummary(...),
    paths=ContextPaths(...),
    memory=MemorySummary(...),
    worktree=WorktreeSummary(...),
    providers=ProviderSummary(...),
    drift=DriftSummary(...),
)
```

2. For intentionally raw data returned by an adapter, provider, parser, or legacy application entry point, validate it at the narrow boundary where it becomes modeled data.

```python
providers = ProviderSummary.model_validate(provider_summary_packet(...))
```

3. For raw/detail diagnostics that intentionally preserve provider-native fields, use the dedicated flexible diagnostic model. Do not let flexible raw payloads leak into compact public context models.

The transport boundary should serialize the final model once through `model_dump(mode="json", exclude_none=True)` or the shared response serialization helper once token accounting is wired.

## Boolean Flag Rule

Avoid adding boolean mode flags to functions that already have branching behavior.

Bad:

```python
def update_memory(path: Path, dry_run: bool, force: bool, skip_validation: bool) -> None:
    ...
```

Good: split the modes into separate functions, or pass one small typed options/strategy object, so each call site reads as a single intent rather than a matrix of flags.

## Error Handling

Domain failures use the typed error family in `errors.py`, not bare exceptions.

1. Raise an `AgentsRememberError` subclass (`ConfigError`, `AuthorityError`, `LedgerError`, `ContractError`, `ContextProviderError`, `ContextPacketError`, `MissingMemoryError`) for invalid input, settings/authority violations, and broken contracts.
2. New typed errors subclass `AgentsRememberError` (which subclasses `ValueError`, so existing `except ValueError` handlers keep working). Put the base in `errors.py`, not a per-module ad-hoc class.
3. Reserve bare `RuntimeError` for genuinely-unexpected states, not for validation or authority failures.
4. Do not broadly `except Exception` to build a response; catch the typed family (or a specific error) at the boundary.

## Security Boundaries

Path-confinement and repo-allowlist checks are centralized, never copy-pasted.

1. Resolve-and-confine a caller path through `application/_guards.require_within_coordination`; resolve a caller repo id through `require_repo`. Do not re-implement the "resolve, then check `is_relative_to`" guard inline.
2. A confinement guard returns the resolved path or raises `AuthorityError`. Callers use the returned value; they do not re-resolve.
3. Rationale: a security check duplicated across call sites is the one you forget to update — and the one you forget is the vuln.

## Secure Defaults

Public, agent-callable surfaces default to the safe option.

1. A tool's default must be the least-privileged choice. Dangerous modes (e.g. a full-access sandbox) are explicit opt-in, never the default value baked into the public signature.
2. Capabilities that execute untrusted or third-party code are gated behind an explicit settings flag and refuse when it is unset — they are not always-on.
3. Document the execution/trust model where the capability is exposed (README + settings reference), not only in code.

## Cross-Layer DTOs

Arguments that cross a layer boundary are a typed object, not `argparse.Namespace` or `Any`.

1. Do not pass `argparse.Namespace` from an application entry point or CLI into the domain layer as the shared argument type. Build a frozen dataclass (e.g. `WorktreeArgs`) and convert argparse output to it at the CLI edge.
2. `Any` on a parameter that has a concrete type is a defect, not a shortcut. Type provider layouts, request objects, and results with their real classes — removing `Any` here surfaced latent `None`-handling bugs the type checker had been unable to see.
3. This complements the Boolean Flag Rule: prefer a typed request/options object over threading many positional or boolean args.

## Single Source of Truth

A value or algorithm lives in exactly one place.

1. The package version derives from installed metadata (`importlib.metadata`), not a hand-maintained literal duplicated across modules and tests.
2. A shared constant or helper lives in one module and is imported; do not copy it. Byte-identical duplicates drift silently (the cgc/grepai provider-settings extractor had already diverged before it was consolidated).
3. When you find the same function in two places, consolidate rather than edit both.

## Atomic Mutations

An operation that mutates more than one repo, branch, or file is all-or-nothing.

1. Pre-validate every step before mutating anything (e.g. confirm both fast-forwards are possible before performing either).
2. If a later step can still fail after an earlier mutation, capture the pre-mutation state and roll back on failure.
3. Never leave a half-applied state — one branch advanced while the other is behind is a bug, not an edge case.

## Dead Code and Theater Tests

Do not ship code that does nothing, and do not test that it does nothing.

1. A test asserts real behavior. A test that asserts a feature has no effect (an empty watch-list, a no-op result) is theater — remove the feature or make it do something, then test that.
2. Do not wire in an inert feature (a loop over an empty constant, a CLI subcommand returning a static no-op). Implement it or remove it.
3. Prefer deleting dead code over keeping it "just in case". Unreferenced functions, parameters a function immediately discards, and unreachable branches are removed, not retained.

## Parse By Schema, Not Heuristics

Parsers (per the Responsibility Rules) extract fields by the source's declared shape.

1. Read structured fields from their documented keys and event types. Do not substring-scan a serialized blob or take "the longest string" to guess a value.
2. When the upstream format is known (e.g. a provider's event stream), match its schema explicitly, add a fixture from real output, and test against it.

## Smell vs Defect

A code smell is not automatically a defect.

1. Before "fixing" a pattern, confirm it is actually wrong. Some indirection is intentional — a flexible-by-design model boundary, a deliberate test seam. Verify against the code and its tests first.
2. If a flagged smell turns out to be intentional, document the intent at the site (a short comment, or a note here) instead of refactoring it into something worse.
3. Behavior-preserving cleanups keep the suite green at each step; do not bundle a risky structural change with unrelated edits.
4. Correct-but-superlinear is a DEFECT, not a smell: a change that passes every correctness test but composes into an accidentally-quadratic call path (see Anti-Patterns and "Stability, Bounded Resources, and Reclamation" below) ships broken even with a fully green suite. Do not wave it through as style.

## Stability, Bounded Resources, and Reclamation

D1 — Stability precedes delivery. The liveness and stability of a shared substrate outrank the delivery of any single signal that rides on it. There is no communication with a dead system, so agent communication is best-effort under a system-stability budget: no delivery, retry, escalation, or logging mechanism may threaten the CPU, memory, disk, or I/O of the substrate it runs on. When the two conflict, shed the signal, not the system.

D2 — Bounded by construction. Unbounded growth is a design defect, not a tuning problem. Every store is capped and evictable; every loop over a store carries a per-cycle budget; every append-only log names its compactor and retention owner in the same change that introduces it. Correct-but-superlinear is its own defect class (algorithmic slop) independent of functional correctness — an O(n^2) that passes every correctness test is still broken.

D3 — Guaranteed reclamation, proven by scaling. No feature may create data — durable or temporary — without a named, bounded reclamation path landed in the same change. Scaling is a property, so it is proven by scaling: assert behaviour across >=2 input sizes (never a single-N smoke), and bound worst-case time and on-disk / in-memory size. If you can make it, you must be able to guarantee getting rid of it.

See Anti-Patterns above (accidentally-quadratic composition, unbounded append-only log without a named compactor) and Smell vs Defect above (correct-but-superlinear is a defect) for the cross-linked failure modes this doctrine rules out. Cross-referenced from `AGENTS.md` "Code Quality Instructions" as MUST-READ before adding or editing a store, a loop over a store, a queue, or an append-only log. Catching engagement: 260707-HFX2-L7 (dead-seat storm) — see `criteria/code-seam.md` CS-6 and `criteria/plan-review.md` PR-6 for the reviewer-facing counterpart of D1/D2/D3.
