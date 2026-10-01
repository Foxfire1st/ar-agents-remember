# mcp/src/agents_remember/errors.py

## Governing Overview

[Governing route overview](../../overview.md)

## Purpose

Defines the common typed failure vocabulary used by certification, memory, lifecycle, authority, and harness boundaries. The base remains a ValueError, while subclasses preserve the distinctions callers need to refuse unsafe work, present bounded diagnostics, or determine whether a retry could duplicate an operation.

## Code Commentary

### Logic

`LockCapabilityError` names a failed resource-filesystem exclusion capability. The shared kernel lock raises it without assigning a coordinator role or registry policy. Control-plane callers translate it to `UnsafeLockFilesystemError`; the Dagger registry translates it to `DaggerRuntimeAuthorityError` with finding `runtime-authority-registry-lock-unsafe`.

`CertificationContractError` recursively freezes findings, including nested mappings and sequences. Profile admission, unavailable executor prerequisites, contradictory readiness, and invalid shared Dagger authority remain separate subclasses with stable statuses. `DaggerRuntimeAuthorityError` covers invalid declarations, connection-only inspection failures, authority conflicts and live-owner transition barriers before executor launch.

Task-intent failures carry an explicit next action. Seat occupancy, dispatch evidence, dispatch locking and structural routing retain separate error types. Configured-contract authority errors expose the failing authority cell; reread errors retain a closed reason and bounded expected/observed facts rather than leaking backend exception input.

`CuratorCoherenceError`, `MemoryCandidatePairError`, `CuratorCoherencePairError` and `FinalCertificationError` have distinct public response fields. Pair errors preserve the exact failing field and recovery arguments; the coherence adapter forwards the shared pair diagnosis. Final certification uses `certificationStatus`, while pair validation uses `pairStatus` and `pairField`.

Harness errors distinguish a request that sent no bytes, one that may have been sent, a busy adapter that proved zero bytes were sent, request-id conflicts, stale bridge epochs and non-pending interaction responses. Tokenizer and grammar failures remain explicit integrity failures; native-history unavailability does not automatically invalidate the harness adapter.

The role-capsule compiler adds a fourth family at the end of the module. cit:([`CapsuleCompilationError`], mcp/src/agents_remember/errors.py:490-531) is the typed refusal a capsule compilation raises, and its shape is what makes a refusal *explainable* rather than merely fatal: `status` is a stable, branchable code (the thirteen in `agents_remember.models.role_capsules.statuses`, plus the application tier's source-admission codes), `detail` names the exact defect for an operator who does not know the internals, `next_action` names **the owner that has to change something**, and `conflicts` carries the structured contradiction rows when the refusal is a stopped conflict. `conflicts` is frozen through `MappingProxyType` per row, so a caller cannot mutate a refusal's evidence after the fact. Two projections are provided: cit:([`render`], mcp/src/agents_remember/errors.py:516-521) is the one-line operator-facing text (`"<status>: <detail> (remedy: <next_action>)"`, with the remedy omitted when empty), and cit:([`response_fields`], mcp/src/agents_remember/errors.py:523-531) is the bounded fact set that adds `nextAction` and `conflicts` only when present, so a lower-layer diagnostic never leaks into a response.

Two subclasses narrow the family by defect source and are declarative today: cit:([`CapsuleManifestError`], mcp/src/agents_remember/errors.py:534-535) for an invalid canonical manifest or declared source path, and cit:([`CapsuleSourceError`], mcp/src/agents_remember/errors.py:538-539) for an absent, unreadable, unconfined, or non-UTF-8 instruction source. Neither overrides the base behavior; they exist so a caller can distinguish *which side of the boundary* refused without parsing the status string. **A third subclass, `CapsuleBindingError`, was removed on the A3 candidate** — the binding-defect class no longer has a distinct type, so do not cite one.

The **task-context projection** appends a separate family at the very end of the module rather than a fourth `Capsule*` member. cit:([`TaskProjectionSourceError`], mcp/src/agents_remember/errors.py:542-589) is raised when an admitted task/worktree binding cannot be projected into task context, and it deliberately subclasses `AgentsRememberError` **directly**, not `CapsuleCompilationError`: a projection that could not read its task has failed *before* any capsule compilation, and filing that under the capsule family would tell a caller the compiler refused when it was never reached. It keeps the same explainable-refusal shape — `status` a stable branchable code, `detail` the exact defect for an operator who does not know the internals, `next_action` the **owner that has to change something** — and adds one field of its own: `owner_status` carries the status the existing AR owner raised when this refusal wraps one, **so a caller can still branch on the owner's own vocabulary instead of matching prose**.

Its status vocabulary is **not** registered in `agents_remember.models.role_capsules.statuses`; the sixteen codes are raised at their own sites under `application/task_projection/`: `projection-binding-mismatch`, `projection-binding-unresolved`, `projection-branch-mismatch`, `projection-contract-unavailable`, `projection-memory-binding-unavailable`, `projection-operation-unsupported`, `projection-repository-mismatch`, `projection-requirement-declaration-unresolved`, `projection-requirement-packet-invalid`, `projection-requirement-packet-missing`, `projection-requirement-packet-unresolved`, `projection-role-altitude-mismatch`, `projection-scope-ambiguous`, `projection-task-binding-mismatch`, `projection-task-reference-invalid`, `projection-task-unknown`. Because they are absent from `CAPSULE_STATUSES`, do not assert membership there: the projection codes and the capsule codes are two vocabularies with two owners.

The family's defining invariant is that **a projection is either complete or refused** — there is no partial projection and no fallback to another branch, another task or a broader scope. It never repairs what it could not resolve, so the current task document is untouched by any of these refusals.

**The class is not interchangeable with `CapsuleCompilationError`.** `TaskProjectionSourceError` has no `conflicts` field and its `response_fields()` publishes `status`/`detail` plus `nextAction`/`ownerStatus`; the capsule family publishes `nextAction`/`conflicts`. A caller that branches on one family's response keys must not assume the other's.

`AtomicReplaceError` is a later, smaller member appended after the task-context projection family **and after `MemoryModeUnsupportedError`**, which the committed source already carries at `637-685` — it is not part of this change set: the typed failure of `kernel.atomic_write.atomic_replace`, which does two things that fail independently — the rename that makes new bytes reachable and the directory flush that makes the *name* durable. Both legs used to surface as one indistinguishable `OSError`, so a caller could not tell "the destination never changed" from "the destination already changed but the rename is not durable". It carries `leg` (`"replace"` or `"directory-fsync"`), `destination`, `destination_state` and the cause, and `response_fields()` projects the bounded `leg`/`destination`/`destinationState` triple. **The reachable states are exactly two:** the two raise sites in `atomic_replace` publish `"previous-bytes"` (failed rename, nothing published) and `"source-absent"` (successful rename, failed flush). The class docstring additionally lists a `"new-bytes"` state for "the rename completed and its name is not yet durable"; no raise site produces it today, so it is a declared-but-unreachable label and must not be presented as an observed state. The claim the class makes is a *measured* one — the test re-reads the destination after a failed flush and asserts it holds the new bytes — and it deliberately subclasses **both** `AgentsRememberError` and `OSError`, so every existing `except OSError` around a publish keeps observing the failure it always did rather than silently no longer matching it.

The durable-comparison-generation work appends **two smaller typed failures** beside `FutureCodeCandidateError`, and both are `status`-carrying members of the ordinary `AgentsRememberError` family rather than of a new one:

- cit:([`CodeObjectRetentionError`], mcp/src/agents_remember/errors.py:180-190) is the retention owner's failure — a comparison's explicit code-object retention could not be created, or was not released. Its statuses are `code-object-ref-invalid` (a ref that is not one name inside `refs/ar/retained-code/`, or whose leaf/generation segment could escape the namespace), `code-object-missing` (an object this repository cannot read), `code-object-ref-occupied` (a ref that already names a *different* pin, which a retention owner must never re-point), `code-object-ref-unwritable` (Git refused the `update-ref`) and `code-object-ref-moved` (a release was asked to delete a ref that no longer names the recorded commit). It is **raised rather than returned** because every caller is inside a publication that has not happened yet: the freeze converts it into a typed `ReviewRefusal`, and the retention owner itself has no result value that could carry both facts a caller needs — which ref, and which of the two objects.
- cit:([`ComparisonReclamationError`], mcp/src/agents_remember/errors.py:193-203) is the reclamation owner's failure, with two statuses: `snapshot-unreadable` (a retained snapshot could not be read before its discard) and `snapshot-bytes-mismatch` (its bytes are not the ones the generation froze). It is raised rather than returned for a different reason: **the caller is a deletion**, and a returned value would make "nothing was removed" easy to overlook at the one place where removing the wrong bytes is irreversible — so the operation raises *before* it records anything or unlinks anything.

Neither class adds a response projection: a caller that needs a bounded payload gets it from the layer that converts the failure (the freeze's refusal, or the deletion owner's returned record).

### Conventions

Raise the narrow typed family rather than a generic exception when a domain contract is known. Expected and observed dictionaries are copied at response boundaries; only certification findings are recursively frozen. A class that carries a machine-readable `status` sets it as an attribute in `__init__` and keeps `detail` as the `AgentsRememberError` message, so `except AgentsRememberError` keeps observing it.

### Invariants And Boundaries

- Lock capability failure must stay explicit through each caller's domain error; a shared primitive does not grant caller authority.
- Preserve certification refusal codes and ownership details; do not flatten them into successful or generic lifecycle output.
- A busy-adapter error means zero operation bytes were sent. Generic disconnects cannot establish that retry safety.
- Pair, coherence and final certification errors report missing authority; constructing an error does not validate or repair that authority.
- Grammar and tokenizer failures never silently replace the configured parser or vendored vocabulary.
- A capsule refusal is a **value with a remedy**, not a bare abort: `status` is a stable branching contract, `detail` is operator-facing prose, and `next_action` names the owner that has to change something.
- `conflicts` rows are frozen at construction. A caller may read a refusal's structured contradiction evidence but must not mutate it.
- `response_fields()` is the **bounded** projection: it adds `nextAction` and `conflicts` only when they exist, and it must never be widened to carry lower-layer diagnostics.
- The three `Capsule*` subclasses are boundary markers, not behavior. Adding a distinct meaning to one of them is a contract change for every caller that branches on the exception type.
- A compilation failure never becomes a partially valid capsule, so this family is raised **instead of** returning content — it is never a warning channel.
- A task-context projection is **either complete or refused**. There is no partial projection, no fallback branch, no nearest task match and no silent scope widening; a projection never repairs what it could not resolve.
- `TaskProjectionSourceError` keeps the wrapped owner's own status in `owner_status`. Do not collapse it into the projection's vocabulary — the whole point is that a caller can branch on the owner's code rather than on prose.
- `TaskProjectionSourceError` subclasses `AgentsRememberError` directly and **not** `CapsuleCompilationError`: a projection failure happens before any capsule compilation, so `except CapsuleCompilationError` must not be read as covering it.
- The sixteen `projection-*` codes are not members of `CAPSULE_STATUSES`. Do not assert membership there or register them in `models/role_capsules/statuses.py`.
- `AtomicReplaceError` subclasses **both** `AgentsRememberError` and `OSError`. That multiple inheritance is the contract, not an accident: existing `except OSError` call sites around a publish must keep observing a failed publish, so the class may not be re-based on the domain family alone.
- `AtomicReplaceError.leg` and `.destination_state` describe the **destination's measured state**, not the operation's intent: `"replace"`/`"previous-bytes"` means nothing was published, `"directory-fsync"`/`"source-absent"` means the rename already published the new bytes and only their durability is missing. A caller must not read either label as the other, and a retry decision must branch on them. The `"new-bytes"` label the class docstring mentions is not produced by any raise site — do not treat it as a reachable state.
- `CodeObjectRetentionError` is the **retention owner's** failure and `ComparisonReclamationError` the **deletion owner's**. They are raised, not returned, at two different boundaries: a retention failure happens inside a publication that has not happened yet (so the freeze converts it into a refusal and reports it as a state), while a reclamation failure happens at a deletion that must not proceed (so a returned value would let a caller overlook "nothing was removed").
- A retention ref **is never re-pointed**. `code-object-ref-occupied` exists so a ref naming a different pin is refused rather than overwritten, because the objects behind it may be another generation's only copy.
- `ComparisonReclamationError` is raised **before** anything is recorded or unlinked: `snapshot-bytes-mismatch` means no deletion record was written and no bytes were removed, and a caller must not read a raised reclamation failure as a partial deletion.
- Neither class widens the error vocabulary a caller branches on beyond its own `status`: they are ordinary `AgentsRememberError` members with no response projection of their own.

### Todos

No additional source change is performed by this documentation pass.

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

External domain documentation is not configured.

### Repo-Internal References

The error families preserve distinct authority, recovery and transport meanings. The shared lock capability has two domain-specific callers.

- Policy-free lock capability failure. [1]
- Immutable certification findings and pre-execution statuses. [2]
- Bounded configured-contract authority and reread errors. [3]
- Separate coherence, exact-pair and final-certification response shapes. [4]
- Composition, integrity, harness retry safety and history failures. [5]
- Control-plane translation preserves the durable-store error family. [6]
- Host registry translation preserves typed pre-launch authority refusal. [7]
- Role-capsule compilation refusal with its stable status, remedy and frozen conflict rows. [8]
- The two capsule subclasses that mark which boundary refused. `CapsuleBindingError` was removed on the A3 candidate and must not be cited. [9]
- The consumer that turns this family into a value with an explanation instead of an escaping exception. [10]
- The registered refusal-code vocabulary these errors carry. [11]
- The failure cases that assert a refusal advertises its own reason and remedy. [12]
- The task-context projection refusal: complete-or-refused, with the wrapped owner's status preserved. It subclasses `AgentsRememberError` directly, so it is **not** in the `Capsule*` family and is not covered by `except CapsuleCompilationError`. [13]
- The producer that raises this family for every unresolved or contradictory binding input. [14]
- The refusal that proves `None` is never a substitute for an unprojectable admitted task. [15]
- The case that pins the failure taxonomy: each unresolvable input returns its own status. [16]
- The typed failure of a two-leg atomic publish, subclassing both the domain family and `OSError` so existing `except OSError` call sites keep observing it. [17]
- **The retention owner's typed failure, whose five statuses distinguish an invalid ref, a missing object, an occupied ref, an unwritable ref and a moved ref.** [18]
- **The deletion owner's typed failure, raised before anything is recorded or removed.** [19]
- The retention owner that raises the first of the two, with one status per refusal direction. [20]
- **The deletion owner that raises the second, and the two raise sites that keep the mismatch from recording a deletion.** [21]
- The consumer that converts a retention failure into a typed refusal instead of letting it escape the freeze. [22]
- The publisher whose two legs raise it, one label per leg, with the destination's state. [23]

### Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

No cross-repository evidence is required for these file-local claims.
