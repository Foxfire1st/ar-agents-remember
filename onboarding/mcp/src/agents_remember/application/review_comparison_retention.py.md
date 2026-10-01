# mcp/src/agents_remember/application/review_comparison_retention.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**Where the things a comparison generation publishes come *from*.** The freeze publishes a record; this
module retains the bytes that record binds, and it exists as its own owner because *retaining content*
and *publishing a record about it* are different acts with different failure modes.

Two kinds of content, retained by two existing owners, and this module adds no third:

- **The code side** — a captured candidate tree is in **no commit**, so `git gc` may delete it at any
  moment. `retain_comparison_source` measures whether *named durable history* already holds the tree and
  asks the retention owner for a pin **only when it does not**. Custody is therefore a measurement, and
  a comparison whose content has landed stops acquiring refs.
- **Both knowledge halves** — copied through the **storage snapshot owner**
  (`memory/knowledge/closed_snapshot.freeze_closed_snapshot`), which pins a read transaction, copies
  through SQLite, normalises the journal mode and reopens the result read-only to prove it. What is
  retained is a closed, complete dataset of the recorded identity, not "a file that happened to be copied
  while a writer was live".

The module's own rule about failure is stated in its docstring and is the reason every entry point
returns a value: **a named refusal, never an escaping storage error**, "because the freeze has to publish
a named reason, and an escaping exception is not one".

## Code Commentary

### Logic

Explicit recovery supplies an already-recorded source capture from the exact retained manifest. `_retained_capture` validates it inside this owner and never installs it as a live candidate identity. Both knowledge copies must retain the parent's declared identities. A retained before or after snapshot that disappears before copy is a refusal, and the common freeze reclaims the partial stage/new pin; it cannot become ordinary not-selected history.

**Custody is measured against the history the caller names, and the work branch is deliberately not one
of the names.** `custody_names` (`:212-229`) derives exactly two kinds of name from the enclosure
contract: the leaf's **protected source branch** (`local_branch_ref(contract.code_source_branch)`) and
the commits the task record actually landed (`contract.code_commit`, `contract.integrated_code_commit`).
The leaf's own work branch is absent on purpose — it is the branch `worktree_abandon` force-deletes and
ordinary cleanup removes, so a commit that exists only on it is not custody, and treating it as one would
publish a generation whose source side disappears with the leaf. The names are recorded on the binding
(`custody_refs` / `custody_commits`), so a later reader — the release owner included — asks the same
question and gets a comparable answer.

**The pin is created only when the named history does not already hold the tree.**
`retain_comparison_source` (`:131-165`) first resolves the captured pair (`_unresolved_capture`,
`:168-209`), refuses by name if either bound object is not readable, and then asks
`code_object_custody(repository, candidate, names)`: `committed-history` returns an **unpinned** binding
(`_unpinned_binding`, `:232-243`) and no ref is written at all, while anything else goes to
`_pinned_outcome` (`:246-292`). A resolution that carries no enclosure contract is a **refusal**, not an
empty name set — "measuring against nothing would record `retained` for every tree and pin generations
whose content had already landed".

**A pin is keyed by the objects it keeps, so two freezes of one pair converge.** `_pin_key`
(`:295-302`) is `sha256({"baseline": …, "candidate": …})[:32]`, and `retention_ref(leaf, key)` names the
ref; `_ref_present` (`:305-309`) asks whether it already resolves *before* this call creates one, so
`created_pin` is `None` for a pre-existing ref and a failed publication cannot release a pin that
belongs to an already-published generation. `CodeObjectRetentionError` is converted into a typed
`_UNRESOLVED` refusal whose next action names both remedies (repair ref storage, or land the candidate).

**An intentionally unselected knowledge half has typed absence; a lost expected retained half refuses.**
`_side_binding` (`:344-357`) first preserves any named parent's retained expectation. If that expected file disappeared, it refuses before ordinary absence classification. Otherwise it branches on whether the dataset file exists and whether the caller declared that half in `historical_absence`:

- no file **and** declared → `not-recorded`, the reason stating that R05's historical absence is a fact
  about the repository's history rather than a missing input (`_absent_side`, `:360-382`);
- no file **and not** declared → `not-selected`, because this comparison selected no knowledge operand
  so nothing was asked of that half;
- file **and** declared → `_contradicted_absence` (`:385-397`) **refuses**, because "a recorded absence
  beside present bytes is how a real generation is written out of history", and the surface substitutes
  no other dataset;
- file **and not** declared → `_freeze_side` (`:400-444`).

**The pair is preflighted with R05's own reader before anything is copied**, so a half that is present
but cannot be read as a dataset is refused by name (`unreadable_half_refusal`) instead of raising out of
the storage owner mid-freeze (`retain_knowledge_sides`, `:315-341`).

**One half's snapshot is taken through the owner, under the identity the dataset itself holds.**
`_freeze_side` opens the dataset read-only under `review_namespace(resolved.repository_id, database)`,
reads `store.snapshot_identity()`, and **asks whether the dataset's own bound namespace is the one it was
opened under** before copying: asking here turns the storage owner's precondition into a refusal naming
both ids (`_namespace_refusal`, `:464-481`) rather than a storage error raised mid-copy. It then calls
`freeze_closed_snapshot(store, identity, stage_path)` and binds the prepared identity plus the *measured*
post-write size. A failure anywhere in that block is `_snapshot_refusal` (`:447-461`) — whose words say
the thing that matters: "the generation would record a digest of bytes it does not hold".

**The two deletion owners are named on everything the retention creates.** Each retained snapshot carries
`deletion_owner=SNAPSHOT_DELETION_OWNER` and a `cleanup_scope` of `knowledge/<side>` (`:441-442`), and a
pin carries `CODE_OBJECT_DELETION_OWNER` with the one ref as its scope (`:285-286`). Those two constants
live in `review_comparison_reclamation`, which is the module that actually performs the deletions, so
"who may delete this" is a value a reader can act on rather than a convention it has to know.

### Conventions

`__all__` publishes four names: the two retention entry points, the request value and the source-retention
outcome. `KnowledgeRetentionRequest` (`:88-98`) is deliberately **narrower** than the freeze's request —
it carries the resolution and the declared absences and nothing else — because "the retention owner has
no business reading a record's scope, records or lineage, and a narrower input is what keeps it from
growing one". Every value is a frozen dataclass; every fallible path returns
`… | ReviewRefusal`. The two refusal codes reused from the shipped comparison vocabulary are `_ABSENT`
and `_UNRESOLVED` (`:83-85`). `_Capture` (`:101-113`) exists so the two objects, the capture identity and
the custody names travel as one value, because every decision below reads all four.

### Invariants And Boundaries

- **Custody is measured, never assumed** — and only against **named** durable history. The leaf's own
  work branch is not custody.
- **A pin is created only when named history does not already hold the tree**, and `created_pin` is
  `None` whenever the ref pre-existed.
- **A declared historical absence beside present bytes is refused**, never believed and never resolved to
  another dataset.
- **`not-recorded` and `not-selected` are the only two non-retained states**, and each carries the reason
  that distinguishes it.
- **Retention answers with a value, never by raising at its caller.** Every storage, Git and refusal path
  is converted before it reaches the freeze.
- **The snapshot bytes come from the storage snapshot owner.** This module opens datasets and copies
  nothing itself.
- **Every artifact it creates names the operation that may delete it and the bounded scope that deletion
  may touch.**
- **Rank.** It is an `application` module and may import the memory, worktrees and models layers; it is
  the only thing in this package that writes a ref, and it does so through the retention owner rather
  than by running Git itself.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the module's own docstring and functions, in the four owners it
calls, and in the cases that measure custody and the typed absences. Three details a reader should carry:
`custody_names` is the whole definition of "durable history" for this feature and it **excludes the work
branch on purpose**; the pin is created only when that named history does not hold the tree; and a
declared absence standing beside real bytes is a refusal, because that is precisely how a real generation
gets written out of history.

- The module's own statement of the two kinds of content, the two owners that retain them, and the rule that a failure is a named refusal rather than an escaping error. [1]
- The published surface, the refusal codes and the four values. [2]
- **The deliberately narrow request: the resolution and the declared absences, and nothing a record owns.** [3]
- The four facts that travel together through every decision below. [4]
- **The source-retention outcome, with the pin *this call* created separated from the binding the record stores.** [5]
- **The one decision: measure custody against the named history, and pin only when it does not already hold the tree.** [6]
- **The refusal for a resolution with no enclosure contract, with the reason an empty name set would be wrong.** [7]
- **The whole definition of durable history for this feature — the protected source branch plus the recorded landed commits — and the stated reason the work branch is absent.** [8]
- The unpinned binding for content durable history already holds. [9]
- **The explicit pin: the object-derived ref key, the pre-existence question, and the binding that names the pin's deletion owner and bounded scope.** [10]
- **Both halves, preflighted with R05's own reader before anything is copied.** [11]
- **The four-way branch that decides one half: retained, `not-recorded`, `not-selected`, or a refused contradicted declaration.** [12]
- **One half copied through the storage snapshot owner, under the dataset's own bound namespace, with the two refusals that keep a storage error out of the freeze.** [13]
- The retention owner that writes the ref, and the custody measurement this module calls instead of reimplementing. [14]
- The two deletion-owner constants the bindings carry, defined by the module that performs the deletions. [15]
- The storage snapshot owner, and the identity value it returns for a proven-closed copy. [16]
- R05's own reader and its typed-absence spelling, called rather than restated. [17]
- The namespace a half is opened under: read from the record beside those bytes — the candidate's receipt, otherwise the before half's own generation record — and only from the requested repository when neither exists (the rule `260921-ICR-L34` corrected; the receipt-only form made a placed baseline unopenable and every continuity run's comparison unfreezable). [18]
- The branch spelling the protected source branch is named by. [19]
- **The two cases that protect the custody rule: the leaf's own work branch is *not* custody, and genuine protected history taking custody stops the pin while the generation still reopens.** [20]
- **The case that protects the typed absence, and the one that refuses a declared absence beside present bytes.** [21]
- The end-to-end case whose read-back of both halves proves the retained snapshots really are the recorded datasets. [22]

The following declarations carry the changed boundary.

- An old capture is validated for retention without becoming live. [23]
- Expected retained snapshot loss refuses before ordinary absence classification. [24]
- Copied retained knowledge must match the named parent identity. [25]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one repository's Git objects through
the shipped runner and writes snapshots into the coordination task root; neither is a boundary this
module crosses on its own authority.

No meaningful cross-repo references found.
