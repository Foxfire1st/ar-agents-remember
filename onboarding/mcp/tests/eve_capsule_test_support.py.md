# mcp/tests/eve_capsule_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/eve_capsule_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T20:42+02:00 |
| lastVerifiedCommitHash | `8997e184efe67e853a60780912ef5ac21844a323` |
| lastVerifiedCommitDate | 2026-09-16T20:51:44+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The fixture **world** for the eve capsule/workspace binding: a real coordination tree and real git
worktrees, built on disk rather than simulated.

Every side of every L7 comparison has to come from somewhere the code under test does not feed, so this
module builds the things the production path actually *reads*:

- a **real git repository** with real `git worktree` checkouts on real branches, so the admitted
  worktree and the workspace git identity are observed rather than asserted;
- a **real coordination root** with a sprint document, a master, a leaf task document, an enclosure
  contract and an external memory repo, so the capsule compiler, the task projection and the
  coordination resolver all run against their real inputs;
- a small **canonical composition corpus**, authored here, so the instruction blocks the capsule
  carries can be compared against bytes this fixture chose.

Not pytest-collected: the filename does not match `test_*.py`. It is shared support, consumed by
`test_eve_capsule_binding.py` (focused cases), `test_eve_capsule_runtime.py`, `eve_adapter_test_support.py`
and `live_eve_native_fixture.py` — the last of which launches the real pinned eve runtime against a
capsule compiled from this world.

## Code Commentary

### Logic

`build_world` (457) is the entry point and returns a frozen `FixtureWorld` (396). The world is assembled
from composable pieces rather than one monolith:

| Piece | What it builds |
| --- | --- |
| `repository_with_commit` (147) | one real repository with one commit on a named branch |
| `add_worktree` (165) | one real `git worktree` checkout on a named branch, so the linked-worktree `.git`-file shape is exercised rather than the plain-directory shape only |
| `composition_corpus` (175) | the authored corpus the compiler's instruction blocks come from |
| `_sprint_document` / `_master_document` / `_leaf_document` (296, 268, 250) | the three real task documents the projection reads |
| `ContractAddresses` (326) + `_contract_text` (336) | the enclosure contract as a real file, addressed the way the resolver expects |
| `fixture_carrier_for` (565) | the one call into production `materialize_eve_binding`, returning the carrier path and digest |

`binding_env` (622) and `launch_env` (635) render the two environment shapes a launch can carry — a
complete binding and the unbound case — so a case can state which half is missing without hand-writing
variable names.

**The frozen vocabularies are spelled here rather than imported** (`ALL_ROLES`, `ALL_OPERATIONS`,
`ROLE_ALTITUDES`, `OPERATIONS_BY_ROLE`, 63-118, with `CORE_BLOCKS` at 120). This is deliberate: a
fixture that imported what the compiler enforces could not disagree with it, and the compiler's refusal
on a partial or contradictory manifest is itself behaviour worth keeping honest.

### Conventions

- `run_git` (123) is the only way git is invoked, and it fails loudly on a non-zero exit rather than
  returning a partial result a case might assert against.
- Git identity is configured inside the fixture so a case never depends on the operator's global git
  config.
- The world is built once per module (`scope="module"`) and handed to cases as a fixture, because
  building real repositories and worktrees is the expensive part.
- Constants name the addressing (`REPOSITORY`, `SPRINT`, `MASTER_DIR`, `LEAF_ID`, `TASK_PATH`,
  `WORK_BRANCH`, `SOURCE_BRANCH`) so cases and the source-derived consumer proofs agree on one world.

### Invariants And Boundaries

- **Nothing here may be replaced by a mock or a temp-directory shape.** The seam's whole claim is that
  a launch cannot run without an admitted capsule in the admitted worktree, and a simulated worktree
  would let the git-identity comparison pass without ever reading git metadata.
- **The fixture must not import the vocabulary it is used to test against** — see above. Importing
  `ALL_ROLES` from the compiler would make the corpus unable to disagree with the compiler.
- **The world is real, not hermetic-by-deletion.** Cases assert against bytes this fixture wrote into
  its own corpus, so a corpus change shows up as a failing case rather than a silently updated
  expectation.
- This module is **shared support with a lifecycle catalog row**, not a test module: it takes no lane
  row in `mcp/tests/test-evidence-lanes.toml` and its stable contract is declared in
  `mcp/tests/evidence-lifecycle.toml` with four source-derived consumers.

### Todos

None known.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation pass
was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; the fixture's external contract is git's own worktree metadata, which is read from the real repository the fixture creates. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The production producer this fixture drives, and the carrier type its result is handed back as. | `materialize_eve_binding`; `EveBoundLaunch`; `carrier_digest` | mcp/src/agents_remember/application/eve_capsule/__init__.py:147-206; mcp/src/agents_remember/models/eve_capsule_carrier.py:287-291 |
| The environment names the fixture renders, imported into the launch module from the carrier module so the fixture cannot invent a spelling the launch does not read. | `BINDING_REF_ENV`; `CAPSULE_DIGEST_ENV`; `CAPSULE_PATH_ENV`; `WORKSPACE_ROOT_ENV` | mcp/src/agents_remember/models/eve_capsule_carrier.py:34-37; mcp/src/agents_remember/serving/eve_runtime_launch.py:41-48 |
| The compiler and projection inputs this fixture supplies for real. | `compile_task_capsule`; `resolve_task_projection_scope` | mcp/src/agents_remember/application/skill_resources/__init__.py; mcp/src/agents_remember/application/task_projection/__init__.py |
| The lifecycle catalog row for this support module, including its four consumers and its replacement contract. | `path = "mcp/tests/eve_capsule_test_support.py"` row | mcp/tests/evidence-lifecycle.toml:714-724 |
| The focused cases that consume this world, and the runtime cases that execute the shipped TypeScript against it. | `world` fixture; `test_runtime_verifier_accepts_the_admitted_carrier_and_workspace` | mcp/tests/test_eve_capsule_binding.py:63-65; mcp/tests/test_eve_capsule_runtime.py:182-203 |
| The live native fixture that compiles a capsule from this world and launches the real eve runtime against it. | `build_world` consumer | mcp/tests/live_eve_native_fixture.py:87-95 |

## Cross-Repo References

No external repository boundary is implemented by this support module; the git worktrees it creates are
local to the test's temporary directory.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T20:42+02:00 — 260915-CAPS-L7 curator: created this card for the fixture world added by
  this leaf's change set. Records that it builds real git repositories, real `git worktree` checkouts,
  a real coordination root and an authored composition corpus rather than simulating any of them, the
  reason the frozen vocabularies are **spelled here instead of imported** (a fixture that imported what
  the compiler enforces could not disagree with it), the `scope="module"` cost decision, and the
  boundary that a simulated worktree would let the git-identity comparison pass without reading git
  metadata. Records its lifecycle catalog registration with four source-derived consumers and its
  deliberate absence from the evidence-lane manifest as shared support rather than a test module.
  Verification metadata is pinned to the leaf's synced base `23cc7a72` because the candidate is
  deliberately uncommitted — the governed closeout stamps the real code commit, and no hash or
  fingerprint was invented here.
