# mcp/src/agents_remember/application/eve_capsule/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/eve_capsule/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T20:42+02:00 |
| lastVerifiedCommitHash | `8997e184efe67e853a60780912ef5ac21844a323` |
| lastVerifiedCommitDate | 2026-09-16T20:51:44+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application/ overview](../overview.md)

## Purpose

The **produce side** of the eve capsule/workspace binding seam: compile the admitted capsule through
the one shared compiler and the one shared projection, and write the carrier whose bytes a bound eve
runtime applies before its first model call.

It takes addressing the coordination surface already accepts — an enclosure contract, the task
document under it, a role and an operation — so a caller points this at **a task, not at a
directory**. The admitted workspace root and the git identity the runtime later verifies both come out
of the task projection rather than being re-derived here.

Three rules shape the whole module, and each is a refusal rather than a default:

- **Admission precedes execution.** Nothing guesses a role from prompt text, invents a workspace, or
  falls back to an unbound launch. A compiler or projection refusal is returned as that refusal and
  **no carrier is written**, so a runtime that cannot be bound correctly is never handed something to
  run.
- **One compiler.** The instruction text is the compiler's own block content in the compiler's own
  composition order; the task facts are the projection's rendered markdown taken verbatim. This module
  orders nothing and selects nothing — it transports a decided value.
- **The admitted worktree, not a re-derived path.** The workspace and its branch/base-commit identity
  are read out of the projection, so the runtime compares what it finds on disk against what the
  contract admitted.

## Code Commentary

### Logic

`materialize_eve_binding` (147) is the entry point and the only writer. It compiles through
`compile_task_capsule`, refuses a non-`ok` outcome with the compiler's own explanation, re-derives the
admitted projection (`_admitted_projection`, 228), builds the carrier, and writes it to
`<carrier_directory>/capsule/capsule-carrier.json`. After writing it **reads the file back and
requires it to parse equal** (193): a carrier that cannot be read is a runtime that cannot be bound,
and discovering that here costs nothing.

`_admitted_projection` is a *check*, not a second opinion. The compile outcome reports the capsule it
produced but not the projection it read, so this resolves the same scope through the documented
consumer contract and then requires the projection's task context to be byte-identical to the one the
capsule carries (`_require_matching_task_context`, 264, compared by each side's own
`content_digest`). A projection that disagreed with the compiled capsule is refused instead of
silently becoming the carrier's task facts.

`build_carrier` (282) projects one compilation result plus its admitted projection into the carrier
value: instruction blocks **verbatim and in composition order**, each with its identity and digest,
L3's task-context markdown whole, the granted tool policy, and the carry-forward units. Nothing is
re-rendered.

`write_scopes_for` (327) turns a role into explicit, runtime-enforceable scopes. A worker gets the
workspace and its report surface; a curator additionally gets the memory surface; **any other role
gets the worker's set**, which is the smallest — so a role whose scope nobody declared cannot inherit
the curator's memory write by accident. A surface the role's table names but nobody admitted is a
**refusal, not a silent narrowing**: a carrier whose declared surfaces disagreed with the role
authority table would be a runtime running under a policy that does not exist.

Fail-closed helpers: `_admitted_directory` (444) requires every surface root to be an **absolute,
existing directory** — a relative path would resolve against whatever the runtime's working directory
happened to be; `_workspace_of` (421) refuses a projection that carried no repository or work branch;
`binding_ref_for` (389) refuses a role/task/operation that is empty, untrimmed, or contains the `:`
separator the reference itself uses.

### Conventions

- The carrier lives under `CARRIER_DIRECTORY = "capsule"` **relative to a caller-admitted
  directory**, deliberately outside the admitted workspace: the runtime's own file tools are confined
  to the workspace root, so the instructions it applies are not a file the model can rewrite.
- `carrier_env` (368) builds the launch environment from the constant names declared in the carrier
  module, so the writer and the reader cannot drift into two spellings of `AR_BINDING_REF`,
  `AR_CAPSULE_PATH`, `AR_CAPSULE_DIGEST` and `AR_WORKSPACE_ROOT`.
- The launch environment is a **return value** (`EveBoundLaunch.env`), not a side effect, so a caller
  cannot start a runtime with a partly-applied binding.
- `EveCarrierSeat` is assembled once by `carrier_seat` (209) rather than passed as four independent
  arguments a caller could supply in part.
- `capsule_carrier_digest_of` (405) and `digest_of_file` (415) exist so a caller can report what a
  comparison was made *against*.

### Invariants And Boundaries

- **This module produces a carrier; it does not launch, verify or apply one.** The reader half is
  `serving/eve_runtime_launch.py::verify_capsule_binding` (Python, pre-process) and
  `eve_runtime/agent/lib/capsule.ts::loadVerifiedCapsule` (TypeScript, in-process). Adding launch
  policy here would put the same decision in two tiers.
- **It must not select or re-order instruction content.** The compiler owns composition; a second
  ordering here would be the TypeScript-reimplementation defect the requirement forbids, one layer in.
- **The binding reference is content-free by design.** `ar-binding:<role>:<task>:<operation>` names
  *which* seat this is and is built only from values the task layer admitted, so a carrier written for
  another binding is refused by name.
- **No carrier is written on any refusal path.** A partially-written or best-effort carrier is the
  failure this ordering exists to prevent.
- **The produce-side seam has no production caller yet.** `materialize_eve_binding` is referenced only
  by its own definition, its `__all__` entry and `mcp/tests/eve_capsule_test_support.py`. Wiring a
  production launch site that supplies the capsule is **leaf 15's** obligation
  (`CAPS-R15@v1`), which received it as an explicit transfer (finding `L7R-4`), not a closure. Nothing
  in this module should be read as that wiring existing.

### Todos

The production launch-site wiring belongs to `CAPS-R15@v1` (leaf 15). This module is complete for its
own side; it does not need to change for that wiring to be added.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation pass
was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; the carrier's cryptography is Node's/Python's standard `sha256`, not a documented external contract. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one compiler and the one projection this module transports from, unchanged and not re-implemented. | `compile_task_capsule`; `CapsuleCompileRequest`; `resolve_task_projection_scope`; `project_task_context` | mcp/src/agents_remember/application/skill_resources/__init__.py; mcp/src/agents_remember/application/task_projection/__init__.py |
| The carrier format and the environment names are declared in the models tier, so the producer and the consumer share one spelling. | `EveCapsuleCarrier`; `BINDING_REF_ENV`; `CAPSULE_DIGEST_ENV` | mcp/src/agents_remember/models/eve_capsule_carrier.py:32-42; mcp/src/agents_remember/models/eve_capsule_carrier.py:168-231 |
| The reader half that proves a carrier before a process exists, and the git-identity check behind it. | `verify_capsule_binding`; `_require_admitted_git_worktree` | mcp/src/agents_remember/serving/eve_runtime_launch.py:447-497; mcp/src/agents_remember/serving/eve_runtime_launch.py:499-527 |
| The in-process reader that applies the carrier the launch verified. | `loadVerifiedCapsule`; `admitWritePath` | eve_runtime/agent/lib/capsule.ts:109-149; eve_runtime/agent/lib/capsule.ts:164-178 |
| The focused cases over this module's refusals, including the unadmitted-surface and projection-disagreement refusals. | `test_materialize_refuses_an_unadmitted_surface_root`; `test_materialize_refuses_a_projection_that_disagrees_with_the_capsule` | mcp/tests/test_eve_capsule_binding.py:233-240; mcp/tests/test_eve_capsule_binding.py:282-295 |
| The fixture world that supplies this module's real inputs, and the one place `materialize_eve_binding` is currently called. | `FixtureWorld`; `fixture_carrier_for` | mcp/tests/eve_capsule_test_support.py:396-455; mcp/tests/eve_capsule_test_support.py:565-620 |
| The lifecycle catalog row registering the shared support module this seam's cases rest on, whose four declared consumers the loader re-derives from source. | `path = "mcp/tests/eve_capsule_test_support.py"` row | mcp/tests/evidence-lifecycle.toml:714-724 |

## Cross-Repo References

No external repository boundary is implemented by this module: the carrier is AR's own format and the
compiler it calls is AR's own.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T20:42+02:00 — 260915-CAPS-L7 curator: created this card for the produce side of the
  capsule/workspace binding seam, added by this leaf's change set. Records the three shaping rules
  (admission precedes execution, one compiler, the admitted worktree rather than a re-derived path),
  the read-back-equals-written check, the projection-agreement check and why it is a check rather than
  a second opinion, the fail-closed surface rules (absolute existing directories; the worker's set as
  the fallback so an undeclared role cannot inherit the memory write), and the explicit boundary that
  this module produces a carrier without launching, verifying or applying one. States the produce-side
  seam honestly: `materialize_eve_binding` still has **no production caller**, and the production
  launch-site wiring is leaf 15's `CAPS-R15@v1` obligation under the `L7R-4` transfer. Verification
  metadata is pinned to the leaf's synced base `23cc7a72` because the candidate is deliberately
  uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was
  invented here.
