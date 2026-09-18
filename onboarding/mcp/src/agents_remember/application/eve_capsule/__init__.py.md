# mcp/src/agents_remember/application/eve_capsule/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/eve_capsule/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T10:00+02:00 |
| lastVerifiedCommitHash | `2dcacb27446ecbaba01b69ee32e2ac40a1713b09` |
| lastVerifiedCommitDate | 2026-09-18T17:26:34+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l15-ar` uncommitted source (17 dirty paths); base `15fa0e2c0bb91d5bb1b2abf4ee8eb54916bd5ed4` |
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
- **The produce-side seam now has a production caller** (since `260915-CAPS-L15`).
  `application/role_capsules/launch.py::_compile_eve_task` calls `materialize_eve_binding` for a wired
  launch point, so the carrier one bound eve runtime reads is produced by a production path rather than
  only by `mcp/tests/eve_capsule_test_support.py`. That discharges the **produce** half of finding
  `L7R-4` — a production caller exists and the consumer's own gate accepts the carrier it writes — but
  it is **not** "a live eve seat runs with it": a dispatched eve seat still cannot start, because the
  next refusal is the inherited settings-chain effort gate (**D22**, owner **L17**). Nothing in this
  module changes for that; it needed no change for the wiring either.

### Todos

None for this module's own side. The **live-seat** half of the eve delivery story is the settings-chain
gate (`D22`), owned by **L17**; the typed-absence end state **(A)** for a taskless admission is a
successor obligation carried to the final-verification ledger. Neither requires an edit here.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation pass
was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; the carrier's cryptography is Node's/Python's standard `sha256`, not a documented external contract. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one compiler and the one projection this module transports from, unchanged and not re-implemented. | `compile_task_capsule`; `CapsuleCompileRequest`; `project_task_context`; "def resolve_task_projection_scope(" | mcp/src/agents_remember/application/skill_resources/capsule.py:91-108; mcp/src/agents_remember/application/skill_resources/capsule.py:205-236; mcp/src/agents_remember/application/task_projection/projection.py:78-90; mcp/src/agents_remember/application/task_projection/scope.py:334-417 |
| The carrier format and the environment names are declared in the models tier, so the producer and the consumer share one spelling. | `EveCapsuleCarrier`; `BINDING_REF_ENV`; `CAPSULE_DIGEST_ENV` | mcp/src/agents_remember/models/eve_capsule_carrier.py:32-42; mcp/src/agents_remember/models/eve_capsule_carrier.py:168-231 |
| The reader half that proves a carrier before a process exists, and the git-identity check behind it. | `verify_capsule_binding`; `_require_admitted_git_worktree` | mcp/src/agents_remember/serving/eve_runtime_launch.py:466-516; mcp/src/agents_remember/serving/eve_runtime_launch.py:518-546 |
| The in-process reader that applies the carrier the launch verified. | `loadVerifiedCapsule`; `admitWritePath` | eve_runtime/agent/lib/capsule.ts:109-149; eve_runtime/agent/lib/capsule.ts:164-178 |
| The focused cases over this module's refusals, including the unadmitted-surface and projection-disagreement refusals. | `test_materialize_refuses_an_unadmitted_surface_root`; `test_materialize_refuses_a_projection_that_disagrees_with_the_capsule` | mcp/tests/test_eve_capsule_binding.py:233-240; mcp/tests/test_eve_capsule_binding.py:282-295 |
| The fixture world that supplies this module's real inputs, and — before the wiring landed — the one place `materialize_eve_binding` was called. | `FixtureWorld`; `fixture_carrier_for` | mcp/tests/eve_capsule_test_support.py:396-455; mcp/tests/eve_capsule_test_support.py:565-620 |
| The production caller this seam now has, and the launch whose workspace is read back out of the carrier it writes. | `_compile_eve_task`; `compile_launch_capsule` | mcp/src/agents_remember/application/role_capsules/launch.py:362-405; mcp/src/agents_remember/application/role_capsules/launch.py:273-295 |
| The lifecycle catalog row registering the shared support module this seam's cases rest on, whose four declared consumers the loader re-derives from source. | "path = \"mcp/tests/eve_capsule_test_support.py\"" | mcp/tests/evidence-lifecycle.toml:1442-1442 |

## Cross-Repo References

No external repository boundary is implemented by this module: the carrier is AR's own format and the
compiler it calls is AR's own.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T15:12:32+00:00: Generated citation repair: "path = \"mcp/tests/eve_capsule_test_support.py\"" repointed to mcp/tests/evidence-lifecycle.toml:1442-1442. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "path = \"mcp/tests/eve_capsule_test_support.py\"" repointed to mcp/tests/evidence-lifecycle.toml:1438-1438. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "path = \"mcp/tests/eve_capsule_test_support.py\"" repointed to mcp/tests/evidence-lifecycle.toml:1437-1437. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "path = \"mcp/tests/eve_capsule_test_support.py\"" repointed to mcp/tests/evidence-lifecycle.toml:1434-1434. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-17T10:00+02:00 — 260915-CAPS-L15 curator: **the seam gained its production caller, so the
  invariant that said it had none was corrected in place.** `application/role_capsules/launch.py::_compile_eve_task`
  now calls `materialize_eve_binding` for a wired launch point, which discharges the **produce** half of
  `L7R-4` (a production caller exists, and the consumer's own gate accepts the carrier it writes, from
  the launch's own captured cwd and env — `E8`). The card states explicitly which half that is and which
  it is not: a dispatched eve seat still cannot start (the inherited settings-chain effort gate, `D22`,
  owner **L17**), so no reader takes the produce-side discharge for a live-seat one. The reader-half
  citation was re-anchored for this leaf's insertions, and the fixture row no longer stands in as the
  seam's only caller. Verification metadata moves to this leaf's base `15fa0e2c`; the candidate is
  deliberately uncommitted, so the governed closeout stamps the real code commit and no hash or
  fingerprint was invented here.
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
