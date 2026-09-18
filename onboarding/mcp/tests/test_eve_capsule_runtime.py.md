# mcp/tests/test_eve_capsule_runtime.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_eve_capsule_runtime.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T20:42+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The **real-runtime** cases for the eve capsule/workspace binding: the shipped TypeScript verifier,
executed.

The runtime half of this seam is TypeScript inside the pinned eve application, and **no Python case can
observe whether it refuses a foreign binding, a tampered carrier or a sibling worktree**. These cases
therefore execute the *shipped* modules with the same Node the runtime launches under, inside a real git
fixture world, and read the refusal code each defect produces.

The modules under test are pure Node code — no eve import, no bundler — so this is a direct observation
of the shipped file rather than of a copy or a re-implementation.

Integration-collected (`pytestmark = pytest.mark.integration`): they need a real Node.

## Code Commentary

### Logic

A loader hook supplies the one thing Node's own type stripping does not: the `./x.js` specifier
convention the eve compiler uses for authored TypeScript. `_HOOK` catches a failed `.js` resolution and
retries it as `.ts`; `_REGISTER` installs it through `node:module`'s `register`. This means the shipped
`.ts` files are executed **as shipped**, with no build step and no copy.

`RuntimeProbe` (76) drives one verification over the real fixture world and captures the outcome.
`CarrierDefect` (58) and `LaunchDefect` (67) declare a defect as **data** — a label, a payload mutation
and the refusal code it must produce — so the parametrized cases are a table rather than a series of
near-identical bodies, and adding a defect is one row.

| Case | What it proves |
| --- | --- |
| `test_runtime_verifier_accepts_the_admitted_carrier_and_workspace` (182) | the admitted carrier and workspace are accepted — the control that keeps the refusal group from passing for the wrong reason |
| `test_runtime_verifier_refuses_each_declared_defect` (268) | every declared carrier defect produces **its own** refusal code, parametrized over the defect table (mismatched instruction counts, foreign binding, foreign workspace, foreign branch, two workspace scopes) |
| `test_runtime_verifier_refuses_an_unusable_launch_binding` (290) | an unbound or partly-declared launch is refused before execution |
| `test_runtime_write_admission_refuses_a_sibling_worktree_and_the_memory_surface` (317) | the write-scope admission refuses a sibling worktree and the memory surface, which is the negative half of the workspace-confinement claim |

### Conventions

- **The modules are loaded from the repository's own `eve_runtime/agent/lib`**, not from a packaged or
  staged copy, so a case fails if the shipped file regresses.
- A defect declares the **exact refusal code** it expects, not merely that an error occurred — the
  verifier's codes are part of its contract.
- Defects are declared as data (`CarrierDefect`, `LaunchDefect`) so the table is the specification and
  the case bodies stay trivial.
- Node comes from `resolve_node_executable`, the production resolver, so the interpreter under test is
  the one a launch would pick.
- The acceptance case is not optional scaffolding: it is what distinguishes "the verifier refuses bad
  input" from "the verifier refuses everything".

### Invariants And Boundaries

- **These cases must execute the shipped TypeScript, not a translation of it.** A Python
  re-implementation of the checks would test the re-implementation; the requirement forbids a second
  implementation of AR's obligation selection, and the same reasoning applies to its verification.
- **The loader hook exists only to resolve the eve compiler's `.js`-for-`.ts` convention.** It must not
  grow into a transform, because a transformed module is no longer the shipped one.
- **The acceptance control must stay.** Removing it would let an over-strict verifier pass the entire
  refusal group.
- These cases are integration-marked and need a real Node; the Python-only half of the seam is in
  `test_eve_capsule_binding.py`, and the end-to-end live claim is `live_eve_native_fixture.py`'s.

### Todos

None known.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation pass
was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; Node's `node:module` `register` API is the external mechanism the loader hook uses and is standard-library behaviour rather than a product contract. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shipped modules under test: the in-process carrier verifier and the git-workspace comparison. | `loadVerifiedCapsule`; `admitWritePath`; `verifyAdmittedWorkspace` | eve_runtime/agent/lib/capsule.ts:109-149; eve_runtime/agent/lib/capsule.ts:164-178; eve_runtime/agent/lib/git-workspace.ts:47-68 |
| The git metadata reader the workspace comparison is built on, and the linked-worktree `.git`-file shape it must handle. | `readGitHead`; `gitDirectory` | eve_runtime/agent/lib/git-workspace.ts:23-45; eve_runtime/agent/lib/git-workspace.ts:70-95 |
| The production Node resolver these cases use, so the interpreter under test is the one a launch would pick. | `resolve_node_executable` | mcp/src/agents_remember/serving/eve_runtime_launch.py:605-635 |
| The Python half of the same seam, which asserts the format and the launch-time verification these cases complement. | `verify_capsule_binding`; `test_launch_verification_refuses_every_declared_defect` | mcp/src/agents_remember/serving/eve_runtime_launch.py:447-497; mcp/tests/test_eve_capsule_binding.py:364-395 |
| The fixture world supplying the real repositories, worktrees and task documents. | `FixtureWorld`; `build_world` | mcp/tests/eve_capsule_test_support.py:396-455; mcp/tests/eve_capsule_test_support.py:457-549 |
| The live native fixture, which is the only artifact that proves the binding end to end against a real eve process. | "capsule-binding" | mcp/tests/live_eve_native_fixture.py:1137-1137 |

## Cross-Repo References

No external repository boundary is implemented by these cases: the Node they execute is the pinned eve
application's own, resolved from this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T20:42+02:00 — 260915-CAPS-L7 curator: created this card for the real-runtime cases added
  by this leaf's change set. Records why they exist at all — the runtime half is TypeScript inside the
  pinned application and no Python case can observe whether it refuses a foreign binding, a tampered
  carrier or a sibling worktree — and the mechanism that makes the observation direct rather than
  indirect: a `node:module` loader hook that resolves the eve compiler's `.js`-for-`.ts` convention, so
  the **shipped** modules execute with no build step, no copy and no transform. Records the defects-as-data
  design (`CarrierDefect`/`LaunchDefect` tables carrying the expected refusal code, not merely that an
  error occurred), and the boundary that the acceptance control must stay, because without it an
  over-strict verifier would pass the entire refusal group. Verification metadata is pinned to the
  leaf's synced base `23cc7a72` because the candidate is deliberately uncommitted — the governed
  closeout stamps the real code commit, and no hash or fingerprint was invented here.
