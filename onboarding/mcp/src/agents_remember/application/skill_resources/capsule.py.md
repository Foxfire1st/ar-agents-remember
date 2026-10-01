# mcp/src/agents_remember/application/skill_resources/capsule.py

## Governing Overview

[application overview](../overview.md)

## Purpose

The **read-only capsule operation**: admitted task binding in, typed capsule or a refusal-with-remedy
out. One call resolves the worktree enclosure that admits the seat, binds the task document to it,
projects the task context through L3, admits exactly the source files the canonical composition
manifest routes for that seat and operation, and compiles through L2.

Nothing is written. A refusal is a **value** carrying its own stable status, an operator-legible
detail and a named remedy, rather than an exception the caller has to translate — and the binding
resolved so far travels with the refusal, so an operator always sees which seat and which revision the
operation was addressing.

## Code Commentary

### Logic

Four steps, each of which can only refuse, in `compile_task_capsule`:

1. `_enclosure` resolves the enclosure selector through the coordination-context resolver and loads
   the worktree contract. The **repository identity is read out of the resolved contract**, never
   taken from the caller, so the admitted facts and the task reference are anchored to the enclosure
   that actually owns them. Since `260915-CAPS-L15` the root that resolution *uses* is resolved first
   by `_declared_repository_root` — the caller's own value when it supplied one, otherwise
   `code_repo_path` read out of the contract the request already names — because the **registered**
   `role_capsule_compile` tool exposes no repository field at all and the coordination resolver refuses
   without one (defect **D13**). The same resolved root travels onto `AdmittedEnclosure` and is what
   `_projection` hands the task projection, so projection and admission resolve against one root
   instead of two derivations; without that second half the projection refused
   (`projection-binding-unresolved`) in any tree whose repository does not sit directly under the
   workspace.
2. `require_repo` gates the resolved repository against the server's authority
   (`repository-not-allowed` on refusal).
3. `_admitted_facts` builds `CapsuleAdmittedFacts`: the role must be one of the frozen
   `CAPSULE_ROLES` (`unknown-role`); the task reference is built from the enclosure's repository plus a
   caller-supplied path parsed by the task layer's own reference type (so an escaping or non-canonical
   path refuses before any read); `TaskDocumentTopology.validate_role` decides whether the addressed
   document may carry that role; a contract whose `leaf_id` disagrees with the document's own `id`
   refuses (`task-binding-mismatch`); and the admitted revision is the digest of the JSON bytes the
   task store actually hands over (`capture_task_doc_source`), not of a value re-read later.
4. `_compile_routed` opens the composition corpus, reads the manifest, routes the source set, and
   calls L2's `compile_admitted_capsule` with the projection. `CapsuleCompileOutcome.ok` is true only
   when a compilation *and* a result both exist — a refusal is an outcome too, and every caller that
   branches on success must see it as failure.

Supporting decisions:

- `routed_admission_request` reads the selection from the manifest, never from the caller: the shared
  core blocks this seat composes, its own role file, the operation's file, and the root file of every
  skill it declares. `routed_admission_for` is the same selection routine taking the two values that
  actually decide it (`CapsuleSeatAddress`: role + operation), added by `260915-CAPS-L15` so a launch
  with **no task document** — and therefore no `CapsuleCompileRequest` to hand over — still goes
  through this one routing rule rather than re-deriving a source set. Both entry points share the
  routine; neither is a second rule.
- `_skill_root_source` admits `skills.<name>.source` as the path, and uses the declared `uri` only to
  check provenance (it must begin with `skill://<origin>/` and end in the skill's own name). It never
  re-derives a filesystem path from the URI.
- `admitted_tool_policy` snapshots the published `PUBLIC_TOOLS` roster as the tool policy: a capsule
  *requests* tools and never *grants* them, and the compiler narrows every request against this
  snapshot, so a tool identity this server does not advertise cannot be requested through it.
- `_composition_tree` holds the corpus open for the whole compile, because the default corpus is the
  package's own copy and the packaging helper may materialize it for the duration of one call.

### Conventions

Refusals are typed values (`CapsuleCompilationError`, `TaskProjectionSourceError`) with `status`,
`detail` and `next_action`; the operation translates each into the response envelope rather than
raising. `CapsuleCompileOutcome` carries `binding` in **both** shapes on purpose — an operator gets the
seat and revision on a refusal too.

### Invariants And Boundaries

- **A caller cannot acquire another role by changing a string.** The seat is derived from the task
  document's own altitude; `role` is an input to a check, never the source of the seat. `M1` of the
  leaf's mutation probe removes the altitude refusal and the dedicated case fails, which is what keeps
  this invariant executable rather than aspirational.
- **No arbitrary filesystem read is exposed.** The caller names no path inside the corpus; a required
  block that is missing is a refusal rather than a silently thinner capsule.
- **The admitted revision is the bytes the store handed over.** It is computed from the same captured
  source the projection compares against, so the comparison is between two independently obtained
  facts rather than between a value and itself.
- **The manifest's `skills.<name>.source` is the admitted path.** The published `uri` is provenance
  only; re-deriving a path from a URI produces two spellings of one file and is refused by L2's own
  declared-path rules (`source-not-declared`).
- Nothing here writes to the task, memory or skills trees. `test_the_capsule_operation_writes_nothing_to_the_tree_it_reads`
  is the executor.
- This module owns no compilation semantics: routing, dedup, conflict and digest rules belong to
  `models/role_capsules/**` and `application/role_capsules/**` (layer rank 2), and task projection to
  `application/task_projection/**` (layer rank 3).
- **The repository root has one derivation per compile.** A caller-supplied `code_repository_root` wins
  when present; otherwise the named contract's `code_repo_path` is the authority. Nothing re-derives a
  root beside it, and the value the projection receives is the value the admission used.
- **The registered tool's declared schema is load-bearing.** A schema that loses `contract_path` fails
  the case that asserts it, because the resolution depends on it — the boundary must stay the surface
  callers actually have, not a richer request object only tests can build (D13's own lesson).

### Todos

None recorded.

## Evidence

### Docs References

No external documentation governs this internal admission boundary. The domain contract it consumes
is specified by the sibling requirement packets and the `l-01-agent-lifecycles` composition manifest,
both cited below as repository-internal evidence. No relevant documentation found after checking live
sources.

### Repo-Internal References

- The four refusal-capable steps and the outcome that carries the binding in both shapes. [1]
- The seat is derived from the document's altitude and the role string is validated against it, never used as authority. [2]
- The admitted revision is the digest of the JSON bytes the task store handed over. [3]
- The role/altitude rule the operation checks against. [4]
- Selection comes from the manifest, and the declared skill `source` is the admitted path while the `uri` is provenance. [5]
- The seat-addressed form of the same routing rule, for a caller with no task document. [6]
- D13's repair: the root read out of the contract the request names, and carried onto the enclosure so the projection uses the same one. [7]
- The registered boundary the repair makes usable, and the case that fails if the declared schema loses the field the resolution depends on. [8]
- The launch compiler that consumes the seat-addressed routing entry point for a taskless seat. [9]
- The tool policy is a snapshot of the published roster, so a capsule requests tools and never grants them. [10]
- The advertised roster the tool policy snapshots. [11]
- The corpus root, its manifest and its publishing origin travel together as one admission. [12]
- The composition manifest that routes the admitted source set. [13]
- The consumer the operation compiles through. [14]
- The projection consumer. [15]

### Cross-Repo References

No meaningful cross-repository reference applies. The MCP SDK is a pinned external dependency, not a
sibling repository.
