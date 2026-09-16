# mcp/src/agents_remember/models/eve_capsule_carrier.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/eve_capsule_carrier.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T20:42+02:00 |
| lastVerifiedCommitHash | `8997e184efe67e853a60780912ef5ac21844a323` |
| lastVerifiedCommitDate | 2026-09-16T20:51:44+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[models overview](overview.md)

## Purpose

The **format** of the one value AR hands a pinned eve runtime before it executes: the capsule carrier.
The launch environment can carry a reference and a digest but not the compiled instructions, so the
content travels as a file whose bytes are addressed by that digest.

This module owns the carrier's format **and nothing else**. It parses bytes it is handed and computes
digests over them. Reading the file, writing it, and deciding whether a launch may proceed belong to
the tiers that own those surfaces — which is exactly what lets one shape serve the compiler side
(`application`) and the launch side (`serving`) with neither importing the other.

It is also the single home of the two environment-name groups and the two instruction **channels**,
so the writer and the reader cannot drift into two spellings of the same binding.

## Code Commentary

### Logic

Four value types, each a frozen slots dataclass with `to_json`/`from_json` and no behaviour beyond
its own shape:

| Type | Carries |
| --- | --- |
| `EveCapsuleIdentity` (68) | the admitted seat: role, task reference, operation, binding reference, semantic digest |
| `EveCapsuleWorkspace` (104) | the admitted worktree root plus the git identity the runtime must find on disk: repository, work branch, base commit, contract path |
| `EveCapsuleWriteScope` (141) | one surface the seat may write: scope kind plus path and root |
| `EveCapsuleCarrier` (168) | the whole value: schema, identity, workspace, instruction blocks with their identities and digests, task-context markdown and digest, write scopes, granted tools, carry-forward units |

`to_bytes`/`from_bytes` (219, 225) are the on-disk contract; `carrier_digest` (287) is the content
address of one carrier's exact bytes and `instruction_digest` (293) the address of one applied block,
both `sha256:`-prefixed.

`require_identity` (273) refuses a carrier that belongs to another binding. A carrier left in an epoch
directory by a previous seat is the one realistic way the wrong instructions reach a runtime, and it is
exactly what the binding reference is for.

`_require_workspace_confinement` (299) is the confinement invariant, enforced at parse time: the
carrier must declare **exactly one** workspace scope and its root must equal the carrier's own
workspace root. Without it the two halves of confinement could disagree — the runtime reading and
executing in one directory while its write rule admitted another — which is precisely the failure a
confinement claim is supposed to make impossible.

### Conventions

- **Every consumer-needed field is required.** `_text` (328) refuses an absent or empty string at
  parse time naming the field, so a truncated or hand-written carrier fails instead of contributing
  an empty instruction block. Only genuinely optional fields go through `_optional_text` (335).
- The three parallel instruction lists (`instructions`, `instruction_identities`,
  `instruction_digests`) are required to correspond **one to one**; a length mismatch is refused.
- The environment names are declared **beside the format they address** — `AR_BINDING_REF`,
  `AR_CAPSULE_PATH`, `AR_CAPSULE_DIGEST`, `AR_WORKSPACE_ROOT` — because the writer (the binding seam)
  and the reader (the launch path) must agree byte for byte about which variable carries which value.
- `EVE_CAPSULE_CARRIER_SCHEMA = "ar-eve-capsule-carrier/v1"` is checked on parse; the same literal is
  re-declared as `CARRIER_SCHEMA` in the TypeScript reader so both halves name one schema version.
- JSON is the wire form; keys are lowerCamelCase (`taskReference`, `bindingRef`, `semanticDigest`,
  `writeScopes`, `grantedTools`, `carryForward`).

### Invariants And Boundaries

- **This module must not read or write the carrier file.** It has no filesystem import by design;
  adding file I/O here would put launch policy in the models tier and break the compiler/launch
  symmetry the module exists to preserve.
- **The two channels are a load-bearing distinction, not a style choice.** `ROLE_INSTRUCTION_CHANNEL`
  is `"system"` and `TASK_CONTEXT_CHANNEL` is `"user"`, because system-role instructions stay outside
  conversation history and are included on every model call — that is what makes them the trusted
  channel — while task facts are content rather than authority and belong in the durable user-role
  history where compaction may legitimately summarize them.
- **The workspace scope and the workspace root cannot disagree** — enforced at parse, not trusted.
- **The digest is over the exact bytes on disk**, so a carrier edited after it was written is refused
  by the reader instead of applied.
- **Nothing here is derived from a user message or a session id.** Every identity field is an
  admitted value carried through; a carrier whose identity could be influenced by conversation text
  would defeat the requirement's forging clause.

### Todos

None known. The schema is `v1`; a format change increments `EVE_CAPSULE_CARRIER_SCHEMA` and must be
made in the TypeScript reader in the same change.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation pass
was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; the serialization is plain JSON and the digest is standard `sha256`, so no external contract is being implemented. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The writer that builds this value from one compilation result plus its admitted projection. | `build_carrier`; `materialize_eve_binding` | mcp/src/agents_remember/application/eve_capsule/__init__.py:282-324; mcp/src/agents_remember/application/eve_capsule/__init__.py:147-206 |
| The Python reader that proves the declared digest, the binding identity and the git workspace before a process exists. | `verify_capsule_binding`; `_require_admitted_git_worktree` | mcp/src/agents_remember/serving/eve_runtime_launch.py:447-497; mcp/src/agents_remember/serving/eve_runtime_launch.py:499-527 |
| The TypeScript reader that re-verifies the same carrier in-process and admits writes from its scope list. | `loadVerifiedCapsule`; `admitWritePath` | eve_runtime/agent/lib/capsule.ts:35-79; eve_runtime/agent/lib/capsule.ts:109-149; eve_runtime/agent/lib/capsule.ts:164-178 |
| The git-identity comparison the workspace fields exist for, in both halves. | `verifyAdmittedWorkspace`; `readGitHead` | eve_runtime/agent/lib/git-workspace.ts:23-45; eve_runtime/agent/lib/git-workspace.ts:47-68 |
| The channel distinction is realized as two separately-authored dynamic instruction entries. | `ar-capsule.ts`; `ar-task-context.ts` | eve_runtime/agent/instructions/ar-capsule.ts:1-28; eve_runtime/agent/instructions/ar-task-context.ts:1-28 |
| The cases over this format's refusals: degenerate instruction sets, a workspace scope that is not the workspace, and the digest-versus-disk check. | `test_carrier_refuses_a_degenerate_instruction_set`; `test_carrier_refuses_a_workspace_scope_that_is_not_its_workspace`; `test_carrier_digest_addresses_the_exact_bytes_on_disk` | mcp/tests/test_eve_capsule_binding.py:161-177; mcp/tests/test_eve_capsule_binding.py:179-196; mcp/tests/test_eve_capsule_binding.py:124-138 |

## Cross-Repo References

No external repository boundary is implemented by this module: the carrier is AR's own format, read by
AR's own Python and TypeScript halves.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T20:42+02:00 — 260915-CAPS-L7 curator: created this card for the carrier format added by
  this leaf's change set. Records the four load-bearing properties the module enforces rather than
  trusts (self-describing identity, digest over the exact bytes, every consumer-needed field required
  at parse, workspace scope and workspace root forced equal), the parse-time confinement check and the
  failure it prevents, and the two-channel distinction as load-bearing rather than stylistic: system
  role for the trusted instructions so they survive turn boundaries, compaction and clear, user role
  for task facts because they are content and compaction may summarize them. Also records the
  boundary that this module performs no file I/O by design, which is what keeps compiler-side and
  launch-side consumers symmetric. Verification metadata is pinned to the leaf's synced base
  `23cc7a72` because the candidate is deliberately uncommitted — the governed closeout stamps the real
  code commit, and no hash or fingerprint was invented here.
