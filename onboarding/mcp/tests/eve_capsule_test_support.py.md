# mcp/tests/eve_capsule_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/eve_capsule_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T22:19+02:00 |
| lastVerifiedCommitHash | `0da444b3b2b61f6a86fa4076b283c305db025d22` |
| lastVerifiedCommitDate | 2026-09-20T02:38:15+02:00|
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
| The compiler and projection inputs this fixture supplies for real. | `compile_task_capsule`; "Resolve the admitted worktree/branch/task context the projection will read." | mcp/src/agents_remember/application/skill_resources/capsule.py:205-236; mcp/src/agents_remember/application/task_projection/scope.py:334-417 |
| The lifecycle catalog row for this support module, including its four consumers and its replacement contract. | "path = \"mcp/tests/eve_capsule_test_support.py\"" | mcp/tests/evidence-lifecycle.toml:1455-1455 |
| The focused binding cases that consume this world, and the runtime case that executes the shipped TypeScript against it. | `_carrier_json`; `test_runtime_verifier_accepts_the_admitted_carrier_and_workspace` | mcp/tests/test_eve_capsule_binding.py:64-66; mcp/tests/test_eve_capsule_runtime.py:182-203 |
| The live native fixture that compiles a capsule from this world and launches the real eve runtime against it. | `build_world` consumer | mcp/tests/live_eve_native_fixture.py:87-95; mcp/tests/live_eve_native_fixture.py:1175-1175 |

## Cross-Repo References

No external repository boundary is implemented by this support module; the git worktrees it creates are
local to the test's temporary directory.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T00:16:01+00:00: Generated citation repair: "path = \"mcp/tests/eve_capsule_test_support.py\"" repointed to mcp/tests/evidence-lifecycle.toml:1455-1455. No content impact: mechanical anchor-range projection bound to citation source snapshot b8fe5b3589f1357e836aaad1587e69ed38bbda0d58221eaa2150e96eb0561e93; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: "path = \"mcp/tests/eve_capsule_test_support.py\"" repointed to mcp/tests/evidence-lifecycle.toml:1453-1453. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T20:45:09+02:00 — 260915-KS-L23 post-closeout clearance (change set on `ar/260915-ks-l23`, memory base `ce3028e9`, code `5e4eb651`): **cleared the 1 enforced `citation_anchor_absent_from_range` row in this document.** The closeout's own code commit appended one `consumers` registration above every construct these cards cite, so each cited range ended exactly one line above the line that now carries the anchor row. Widened to the carrying line: `mcp/tests/evidence-lifecycle.toml:1448-1448` → `mcp/tests/evidence-lifecycle.toml:1448-1449` (row 122). Every line the author cited stays inside its range; no claim, Anchor cell or other range was dropped or re-worded, and each named anchor now resolves inside the widened range.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "path = \"mcp/tests/eve_capsule_test_support.py\"" repointed to mcp/tests/evidence-lifecycle.toml:1448-1448. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "path = \"mcp/tests/eve_capsule_test_support.py\"" repointed to mcp/tests/evidence-lifecycle.toml:1444-1444. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "path = \"mcp/tests/eve_capsule_test_support.py\"" repointed to mcp/tests/evidence-lifecycle.toml:1442-1442. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "path = \"mcp/tests/eve_capsule_test_support.py\"" repointed to mcp/tests/evidence-lifecycle.toml:1438-1438. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "path = \"mcp/tests/eve_capsule_test_support.py\"" repointed to mcp/tests/evidence-lifecycle.toml:1437-1437. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "path = \"mcp/tests/eve_capsule_test_support.py\"" repointed to mcp/tests/evidence-lifecycle.toml:1434-1434. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-16T22:19+02:00 — 260915-CAPS-L16 curator: **the frozen vocabularies caught up with the
  compiler** (defect D19, repaired by this leaf). `bootstrap` — the tenth role and ninth operation
  since 260915-CAPS-L13 — was added to `ALL_ROLES`, `ALL_OPERATIONS`, `ROLE_ALTITUDES`
  (`free-agent`) and `OPERATIONS_BY_ROLE`, mirroring the sibling fixture in `test_capsule_serving.py`,
  which already carried the four entries. This is what the card's own "spelled rather than imported"
  rule requires to stay true: a spelling that stops one role short does not *disagree* with the
  compiler, it fails it (`manifest-vocabulary-mismatch: … compiler-only=['bootstrap']`), which is what
  sixteen cases in `test_eve_capsule_binding.py` did until this change — and because the fixture now
  agrees, those cases **run and assert** instead of being skipped. The boundary sentence for that rule
  and the "the two fixtures move together" coupling were added to the body and to the invariants.
  Citation repair in the same pass, stated plainly: this change shifted every anchor at and below the
  vocabulary block by +8 lines, so the body's piece table and `run_git` were re-derived against the
  candidate. The card's anchors had **already** drifted 8 lines before this leaf's bytes (they were
  authored against a pre-L13 revision of the file, not against the leaf base), and three cross-file
  citations that were near-misses but still wrong were corrected with them (the catalog row, the
  binding suite's `world` fixture, the live fixture's consumer call). Left as written rather than
  re-derived: the two anchors that do resolve (`test_eve_capsule_runtime.py:182-203`, the live fixture's
  import block). Verification metadata moves to this leaf's synced base `8997e184`; the candidate is
  deliberately uncommitted, so the governed closeout stamps the real code commit and no hash or
  fingerprint was invented here.

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
