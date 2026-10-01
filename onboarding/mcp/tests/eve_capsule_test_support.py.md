# mcp/tests/eve_capsule_test_support.py

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

`build_world` (465) is the entry point and returns a frozen `FixtureWorld` (404). The world is assembled
from composable pieces rather than one monolith:

| Piece | What it builds |
| --- | --- |
| `repository_with_commit` (155) | one real repository with one commit on a named branch |
| `add_worktree` (173) | one real `git worktree` checkout on a named branch, so the linked-worktree `.git`-file shape is exercised rather than the plain-directory shape only |
| `composition_corpus` (183) | the authored corpus the compiler's instruction blocks come from |
| `_sprint_document` / `_master_document` / `_leaf_document` (304, 276, 258) | the three real task documents the projection reads |
| `ContractAddresses` (334) + `_contract_text` (344) | the enclosure contract as a real file, addressed the way the resolver expects |
| `fixture_carrier_for` (573) | the one call into production `materialize_eve_binding`, returning the carrier path and digest |

`binding_env` (630) and `launch_env` (643) render the two environment shapes a launch can carry — a
complete binding and the unbound case — so a case can state which half is missing without hand-writing
variable names.

**The frozen vocabularies are spelled here rather than imported** (`ALL_ROLES`, `ALL_OPERATIONS`,
`ROLE_ALTITUDES`, `OPERATIONS_BY_ROLE`, 63-127, with `CORE_BLOCKS` at 128). This is deliberate: a
fixture that imported what the compiler enforces could not disagree with it, and the compiler's refusal
on a partial or contradictory manifest is itself behaviour worth keeping honest.

**"Spelled rather than imported" only holds while the spelling is current** — that is the boundary the
sixteen failures of D19 taught. `bootstrap` is the tenth role and the ninth operation (260915-CAPS-L13
added it to `CAPSULE_ROLES`, `CAPSULE_OPERATIONS` and the real `composition-manifest.json`), and a
fixture that stopped at nine no longer *disagreed* with the compiler: it failed it, with
`HarnessControlError: manifest-vocabulary-mismatch: … compiler-only=['bootstrap']`. The four entries
were therefore added — `ALL_ROLES` += `bootstrap`, `ALL_OPERATIONS` += `bootstrap`,
`ROLE_ALTITUDES["bootstrap"] = "free-agent"`, `OPERATIONS_BY_ROLE["bootstrap"] = ("orientation",
"bootstrap", "recovery")` — mirroring the sibling fixture in `test_capsule_serving.py`, which already
carried them. The two fixtures must move together: whoever adds the next role adds it in both, or this
one silently starts failing the compiler it exists to check.

### Conventions

- `run_git` (131) is the only way git is invoked, and it fails loudly on a non-zero exit rather than
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
- **A stale spelling is not a disagreement.** A vocabulary that stops one role short of the compiler
  fails it instead of testing it, so the spelled sets track the compiler's current vocabulary and the
  sibling fixture in `test_capsule_serving.py` moves with them.
- **The world is real, not hermetic-by-deletion.** Cases assert against bytes this fixture wrote into
  its own corpus, so a corpus change shows up as a failing case rather than a silently updated
  expectation.
- This module is **shared support with a lifecycle catalog row**, not a test module: it takes no lane
  row in `mcp/tests/test-evidence-lanes.toml` and its stable contract is declared in
  `mcp/tests/evidence-lifecycle.toml` with four source-derived consumers.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation pass
was available for this file.

No configured `Domain Documentation` source; the fixture's external contract is git's own worktree metadata, which is read from the real repository the fixture creates.

### Repo-Internal References

- The production producer this fixture drives, and the carrier type its result is handed back as. [1]
- The environment names the fixture renders, imported into the launch module from the carrier module so the fixture cannot invent a spelling the launch does not read. [2]
- The compiler and projection inputs this fixture supplies for real. [3]
- The lifecycle catalog row for this support module, including its four consumers and its replacement contract. [4]
- The focused binding cases that consume this world, and the runtime case that executes the shipped TypeScript against it. [5]
- The live native fixture that compiles a capsule from this world and launches the real eve runtime against it. [6]

### Cross-Repo References

No external repository boundary is implemented by this support module; the git worktrees it creates are
local to the test's temporary directory.

No meaningful cross-repo references found.
