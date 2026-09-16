# mcp/tests/test_eve_capsule_binding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_eve_capsule_binding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T20:42+02:00 |
| lastVerifiedCommitHash | `8997e184efe67e853a60780912ef5ac21844a323` |
| lastVerifiedCommitDate | 2026-09-16T20:51:44+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The focused cases for the eve capsule carrier and the launch binding that proves it — the Python half
of the seam.

Every expectation here has a source **the code under test does not feed**: the instruction text is
compared against the compilation result's own render *and* against the block text the fixture wrote
into its corpus; the workspace identity is compared against `git` itself; the carrier digest is
recomputed from the bytes on disk with `hashlib`; the task facts are compared against the projection
the fixture's own task document produces. A case whose two sides both came from the carrier would
prove nothing.

The whole point of the seam is that a launch cannot run without an admitted capsule in the admitted
worktree, so **most of these cases assert a refusal** and the defect each refusal names. The cases that
execute the TypeScript half live in `test_eve_capsule_runtime.py`, because they need a real Node.

Unit-collected: no integration marker, no process, no Node.

## Code Commentary

### Logic

One module-scoped `world` fixture (63) builds the fixture world once; `_carrier_json` (68) reads the
carrier the production path wrote so a case can assert against the artifact rather than a re-derivation.

| Case group | What it proves |
| --- | --- |
| carrier content and addressing (`test_carrier_carries_the_compiled_capsule_verbatim`, `…identities_and_digests_match_the_compilation_manifest`, 69, 89) | the instruction blocks are the compiler's own bytes in the compiler's own order, and the identity/digest lists correspond one to one |
| workspace and digest (`…binds_the_admitted_worktree_git_identity`, `…digest_addresses_the_exact_bytes_on_disk`, 110, 124) | the carrier names the real worktree and branch, and its digest is recomputed from disk rather than trusted |
| launch environment (`…env_names_exactly_the_declared_binding`, 140) | the environment carries exactly the declared binding and nothing extra |
| format refusals (`…refuses_a_degenerate_instruction_set`, `…refuses_a_workspace_scope_that_is_not_its_workspace`, 161, 179) | the parse-time invariants actually refuse, naming the defect |
| role authority (`test_role_write_surfaces_follow_the_role_authority_table`, `test_materialize_refuses_an_unadmitted_surface_root`, 198, 233) | a curator gets the memory surface, a worker does not, an undeclared role falls back to the **smallest** set, and a named-but-unadmitted surface is a refusal rather than a silent narrowing |
| seat and projection (`…carrier_seat_builds_the_canonical_binding_reference`, `…carrier_task_context_is_the_admitted_projection`, `test_materialize_refuses_a_projection_that_disagrees_with_the_capsule`, 242, 257, 282) | the binding reference is built from admitted values, the task facts are the projection's markdown, and a projection that disagrees with the compiled capsule is refused |
| write confinement (`test_materialize_writes_only_the_carrier_file_it_declares`, 327) | the producer writes the carrier and nothing else — a case that fails if the seam acquires a side effect |
| launch verification (`test_launch_verification_accepts_the_admitted_capsule`, `…refuses_every_declared_defect`, `…refuses_a_workspace_on_another_branch`, 355, 364, 397) | `verify_capsule_binding` accepts the admitted binding and refuses each declared defect, including a workspace checked out on a different branch |

`test_building_a_carrier_by_hand_keeps_the_workspace_scopes_consistent` (297) is the one case that
builds a carrier without the producer, to prove the format's confinement invariant holds for any
constructor rather than only for the production path.

### Conventions

- A refusal case asserts **the named defect**, not merely that something raised: an over-strict
  verifier that refused everything would otherwise "pass" the whole refusal group.
- Cases read the on-disk carrier artifact (`_carrier_json`) instead of the in-memory value the producer
  returned, so a serialization defect cannot hide behind a successful return.
- The `world` fixture is module-scoped because building real repositories and worktrees is the
  expensive part; cases must not mutate it.
- Cases that need a real Node belong in `test_eve_capsule_runtime.py` — the split is by dependency, not
  by subject.

### Invariants And Boundaries

- **Both sides of every comparison must have independent provenance.** Comparing the carrier against
  itself, or against a value the fixture derived from the carrier, would make the case vacuous. This is
  the file's stated reason to exist and the property a future edit is most likely to break.
- **Every declared refusal needs a case.** The seam's value is failing closed, so a refusal path
  without a case is an untested guarantee.
- `test_materialize_writes_only_the_carrier_file_it_declares` is a **boundary case, not a redundant
  one**: it is what fails if the producer quietly acquires a second output.
- These cases do not prove runtime behaviour. The TypeScript half is proved separately, and the live
  end-to-end claim belongs to `live_eve_native_fixture.py`.

### Todos

None known.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation pass
was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; the second opinion the cases use is `git` itself and Python's own `hashlib`, not an external specification. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The producer under test and the format its output must satisfy. | `materialize_eve_binding`; `build_carrier`; `EveCapsuleCarrier` | mcp/src/agents_remember/application/eve_capsule/__init__.py:147-206; mcp/src/agents_remember/application/eve_capsule/__init__.py:282-324; mcp/src/agents_remember/models/eve_capsule_carrier.py:168-231 |
| The Python verifier these cases drive in both directions: accept the admitted binding, refuse each declared defect. | `verify_capsule_binding`; `EveWorkspaceBinding` | mcp/src/agents_remember/serving/eve_runtime_launch.py:129-143; mcp/src/agents_remember/serving/eve_runtime_launch.py:447-497 |
| The role authority table the write-surface cases assert against. | `ROLE_WRITE_SURFACES`; `write_scopes_for`; `WORKER_WRITE_SURFACES`; `CURATOR_WRITE_SURFACES` | mcp/src/agents_remember/application/eve_capsule/__init__.py:79-93; mcp/src/agents_remember/application/eve_capsule/__init__.py:327-365 |
| The fixture world supplying the real repositories, worktrees, corpus and task documents. | `FixtureWorld`; `build_world` | mcp/tests/eve_capsule_test_support.py:396-455; mcp/tests/eve_capsule_test_support.py:457-549 |
| The runtime cases that execute the shipped TypeScript for the same seam, which no Python case can observe. | `test_runtime_verifier_refuses_each_declared_defect` | mcp/tests/test_eve_capsule_runtime.py:267-288 |
| The live native fixture that proves the same binding against a real eve process. | `capsule-binding` scenario | mcp/tests/live_eve_native_fixture.py |

## Cross-Repo References

No external repository boundary is implemented by these cases; the git worktrees they assert against
are created inside the test's own temporary directory.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T20:42+02:00 — 260915-CAPS-L7 curator: created this card for the focused binding cases
  added by this leaf's change set. Records the organizing property — both sides of every comparison have
  independent provenance, which is what keeps the cases from being vacuous — the case grouping, and the
  deliberate refusal shape: most cases assert a **named** defect, because an over-strict verifier that
  refused everything would otherwise pass the whole refusal group. Records that
  `test_materialize_writes_only_the_carrier_file_it_declares` is a boundary case rather than a
  redundant one, and the dependency-based split from the runtime cases (these need no Node; those do).
  Verification metadata is pinned to the leaf's synced base `23cc7a72` because the candidate is
  deliberately uncommitted — the governed closeout stamps the real code commit, and no hash or
  fingerprint was invented here.
