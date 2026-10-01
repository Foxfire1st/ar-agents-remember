# mcp/src/agents_remember/application/review_comparison_freeze.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The act that produces a durable comparison generation**, and the reclamation of an attempt that did
not become one. `review_comparison_generation` owns *what* a generation is and
`review_comparison_reopen` owns resolving one; this module owns the production path between them:
**resolve → compose → freeze**, a hidden stage → validation → seal → **one rename**, a sweep for the
stages a killed freeze left behind, and reclaim-on-failure.

Its governing property is that it **composes owners and re-implements none of them**: the source
endpoints and the capture identity come from the review's own resolution (R01), both knowledge halves
are copied by the storage snapshot owner (`freeze_closed_snapshot`), the inventory / comparison identity
/ record collections are the values the review composition already produced, and the retention of code
objects and snapshots belongs to `review_comparison_retention` — "the only thing in this package that
writes a ref".

The production entry resolves once and delegates to `freeze_resolved_review`. That shared entry collects normal R14 owner inputs for the exact resolved pair when no explicit bundle was supplied, composes the review, and hands the resulting bindings to `freeze_comparison_generation`. A caller-supplied bundle remains explicit: positive assessments must carry their complete immutable owner artifacts and exact unique assessment-channel provenance. Missing, incompatible or duplicate required provenance refuses before retention or publication; optional low-level currentness is independent.

**The freeze is deliberately not wired to any route, read path or closeout path — but since
`260921-ICR-L34` it does have a production caller**, the CLI subcommand
`agents-remember review-record-comparison`; see *Invariants And Boundaries*.

## Code Commentary

### Logic

Reserved curator owner references are admitted only through validated record inputs. Generic evidence citations cannot impersonate them. A named expected artifact that failed validation refuses capture; a genuinely non-applicable curator plane remains explicit unavailable metadata while otherwise valid source/knowledge capture proceeds. Explicit EMPTY input never silently fetches today's authority.

freeze_resolved_review accepts an already resolved admitted pair, composes it through the same review owner, and passes only that composition to the existing generation freeze. freeze_review_comparison remains the normal resolver entry. The explicit unchanged-knowledge producer uses this seam after its own checks; no second retention implementation is introduced.

**Publication is one rename of a fully validated directory.** `_stage` (`:647-661`) creates one hidden
sibling of the destination — same filesystem, so the publish is a same-filesystem rename, and a
discovery pass listing generations never sees a stage — named `.{pid}-{uuid}.stage` so two concurrent
freezes cannot share one and a stage a killed process left can be told from a live one. `_publish`
(`:327-351`) retains both knowledge halves into the stage, assembles the field set, seals it with
`assemble_manifest`, and only then calls `atomic_replace(staged.directory, final)`. Everything
referenced has been read back inside the stage before that rename; a generation therefore exists or it
does not.

**A published generation is never overwritten, and an exact retry converges.** If the destination
already exists, `_reuse_or_refuse` (`:354-386`) reads the published record: the same `binding_digest`
returns that record unchanged with `reused=True` (immutability is a property of bytes, not of
intention), while a different binding under an occupied id is refused — "an immutable generation is
never overwritten to describe a different comparison". The id is derived from the bindings, so an
occupied id holding the same binding *is* this generation.

**Every failure path reclaims the ephemeral state, and the refusal survives it.** `_reclaim`
(`:420-431`) removes the stage and releases a pin **this call** created, in that order, because a
cleanup failure must not replace the refusal that says why the freeze stopped. `_release_quietly`
(`:717-732`) suppresses its own errors for the same reason and is given `staged.created_pin`, which is
`None` when the ref already existed — an existing pin belongs to a generation that is already published,
and reclaiming it here would delete a record this call did not make.

**A hard failure is reclaimed exactly like a refusal.** `freeze_comparison_generation` wraps `_publish`
in `except (KnowledgeStorageError, OSError)` as well as its own `_FreezeRefused` (`:302-309`), so a
failure raised *outside* the operation's control flow — an unreadable record at the destination, a
filesystem that refuses the rename — goes through `_storage_refusal` (`:406-417`) and leaves no stage and
no unpublished pin behind.

**The stale-stage sweep reclaims only from the dead.** `_sweep_stale_stages` (`:664-684`) runs at every
freeze start inside the leaf's generation root — the directory the record itself names as
`temporary_storage_scope` — and removes only hidden entries ending in `.stage`. `_issuer_alive`
(`:687-708`) answers from the pid in the name via `os.kill(pid, 0)`: a name with no parsable pid, this
process, a permission error or any other `OSError` all count as **live**, so a concurrent freeze never
has its work removed from under it and the sweep never removes something it cannot attribute to a dead
freeze. Removal failures are suppressed; a stage this call cannot remove is reported by the next.

**The field set is assembled from the owners' own values, dumped through their own models.**
`_manifest_payload` (`:437-470`) builds the payload with `_json` (`:473-477`), which calls
`model_dump(mode="json")` when the value has one — because the seal is a digest over the *stored*
encoding, and handing the models themselves to the sealer would digest whatever the encoder happened to
do with them. Per binding:

- `_scope_binding` (`:480-494`) digests **R02's own inventory payload verbatim** and carries the owner's
  `listed_total` as `changed_path_count`; `_selector_id` (`:497-510`) reads the seed's own declared
  identity field (`invariant_id`, `family_id`) so a revision seed — which selects one revision of an
  identity — yields no identity this scope claims to have selected.
- `_record_binding` (`:513-544`) records counts and one digest over the three collections, and states in
  its `detail` that "whether an owner published none or could not be read is R14's fact, and this record
  asserts neither". `current` is deliberately **not** digested (it is a caller measurement keyed by
  tuples with no canonical JSON spelling); `current_measured` records that a measurement was supplied.
- `_policy_stamps` (`:599-611`) emits five stamps, every one a constant its owner publishes:
  `DIFF_POLICY_VERSION` (or the comparison's own `policy_version`), `KNOWLEDGE_REVIEW_SURFACE_VERSION`,
  `ORIGIN_VERSION`, `GENERATION_VERSION` and this record's own `COMPARISON_GENERATION_VERSION`.
- `_lineage` (`:614-623`) names the predecessor by id *and* manifest digest, the comparison's own
  binding digest, and `_receipt_digest` (`:626-641`) — the candidate dataset's admission receipt digest
  when one is beside it. A receipt that exists but cannot be read yields `None` rather than an error:
  the receipt is the *candidate's* record, this feature neither owns nor depends on it, and refusing a
  freeze over a file nothing in the comparison reads would make an unrelated file the gate.

**A citation is read and digested while freezing, and one that escapes the task root is refused.**
`_evidence_reference` (`:555-587`) resolves the caller's task-relative path through `_confined`
(`:590-596`), which refuses an absolute path or any `..` part, then reads the bytes and records their
digest and length. That is what makes the citation checkable at reopen rather than merely recorded; a
path that does not resolve or does not read is a refusal, not a citation nobody can follow.

**The options value carries the caller-known contributions.** `ComparisonFreezeOptions` carries optional owner records, cited artifacts, explicit historical absence and the predecessor. Omitted records ask the existing collection owner for the already resolved pair; explicit recovery alone sets `retain_parent_inputs` to reuse the named historical capture. `EMPTY_FREEZE_OPTIONS` is the shared frozen default.

### Conventions

`__all__` publishes `EMPTY_FREEZE_OPTIONS`, the two input dataclasses, the request, the outcome and the
two entry points. All five are **frozen dataclasses**, not pydantic models: they are values passed
between this operation and its callers, while the manifest it publishes is the stored wire shape. The
internal control flow is one private exception, `_FreezeRefused` (`:224-229`), carrying the
`ReviewRefusal` that stopped the freeze; every public outcome is a returned
`ComparisonGenerationFreeze` whose `state` is `"published"` or `"refused"`. The three refusal codes
(`_ABSENT`, `_UNRESOLVED`, `_REFUSED`, `:127-129`) are the **shipped** comparison vocabulary reused
rather than widened. `_now()` (`:741-744`) is the module's one clock read.

### Invariants And Boundaries

- **Nothing is published until every referenced byte has been read back inside the stage.** The rename is
  the last act, and it is one act.
- **A partial capture is unpublished and reclaimable**: the stage is removed on every failure path and a
  pin this call created is released again.
- **A pin this call did not create is never released here.**
- **A tree comparison is never frozen (MIK-R25).** `_unfreezable` refuses a resolution that carries `trees` or
  `knowledge_unavailable` before anything is staged, so no knowledge dataset copy is created or retained for a
  review of a converted leaf.
- **An occupied generation id is converged on or refused, never overwritten.**
- **The temporary-storage scope of a generation is the one leaf directory the record names**, and the
  sweep never leaves it, never touches a non-stage entry, and never removes a stage whose owner may be
  alive.
- **A refused composition publishes nothing.** The production entry returns the surface's own refusal
  unchanged rather than inventing a second reason.
- **No second capture path and no second snapshot path.** The capture identity is carried verbatim from
  the resolution, and the snapshot bytes come from `freeze_closed_snapshot`.
- **Boundary: the freeze is not wired to any route, read path or closeout path, and it has had a
  shipped production caller since `260921-ICR-L34`.** The caller is the CLI subcommand
  `agents-remember review-record-comparison`
  ([`cli/review_comparison_record.py`](../cli/review_comparison_record.py.md)), which resolves one
  enclosure contract, composes through the surface's own resolution and composition, and publishes only
  what that composition bound. **Superseded in part:** as ICR-L11 wrote it, "nothing in this leaf calls
  it from a serving surface, an HTTP route, the dashboard or a closeout path … and its consumer is a
  later leaf". The first half is still true and is the point — ordinary capture uses a live resolved pair and explicit recovery uses a named retained parent through the same owners. The operation remains an explicit command rather than a read-side mutation. The second half is no longer true: the consumer exists, and
  ICR-R21's own wiring is a different thing (it attaches the *selected generation* to the closeout
  preview and the delivered receipt to closeout apply and integration, and adds the reopen's fourth
  channel, without calling this operation). A reader must still not read the boundary as dead code:
  the production entry is complete and measured by fifteen production-composition cases.
- **Boundary: the freeze does not reclaim a published generation.** Releasing a pin and discarding a
  retained snapshot belong to `review_comparison_reclamation`, and this module neither calls it nor
  reaches for a ref or a snapshot of a generation that is already published.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the module's own docstring and functions, in the four owners it
composes, and in the cases that drive the production entry against a real enclosure. Three details a
reader should carry: the publish is **one rename** of a directory whose every referenced byte was read
back first; the stage name carries the creating **pid**, which is what makes "reclaim only from the dead"
possible; and a receipt the comparison does not read is never allowed to gate a durable generation.

- The module's own statement of the composition rule and of the one-rename publication. [1]
- The published surface and the three shipped refusal codes it reuses. [2]
- **The caller-known contributions and the shared default that collects actual owner inputs.** [3]
- **Everything one freeze binds, as values other owners produced**, including the declared historical absences and the predecessor. [4]
- **The outcome: a published record, or the refusal that stopped it, with `reused` separating the two ways a freeze succeeds.** [5]
- The staging directory and the pin *this call* created, kept apart because an existing pin belongs to an already-published generation. [6]
- **The production entry: resolve exactly as the surface does, compose exactly as the surface does, freeze only what was bound.** [7]
- **The operation itself, and its two reclaim paths — its own refusal and a hard failure raised outside its control flow.** [8]
- The refusal for a comparison with no task artifact plane to survive in. [9]
- **Stage, seal, and publish by one rename.** [10]
- **Convergence on an already-published record, and the refusal to overwrite one with a different binding.** [11]
- The knowledge halves, retained through the retention owner, with its refusal stopping the freeze. [12]
- The refusal for a failure the freeze could not classify, whose next action states that nothing was published. [13]
- **The field set assembled from the owners' own values, each nested value dumped through its owner's model.** [14]
- **The scope: R02's inventory payload digested verbatim, and a selector identity read from the seed's own declared field.** [15]
- **The record binding, which asserts what the composition supplied and explicitly not what an owner published (R14's fact).** [16]
- **A citation read and digested while freezing, and the task-root confinement that refuses one that escapes.** [17]
- **Every policy stamp as a constant its owner publishes.** [18]
- **The lineage, and the candidate receipt digest that is `None` rather than fatal when unreadable.** [19]
- **The one hidden stage, the sweep that runs before it, and the pid-based liveness question that makes "reclaim only from the dead" possible.** [20]
- The two quiet cleanups: one stage removal and one pin release, neither of which may replace the refusal. [21]
- The owners it composes rather than re-implements. [22]
- The retention owner this module hands the code pin and the two snapshots to. [23]
- The record the freeze seals, and the `assemble_manifest` that seals and derives the id in one call. [24]
- The storage snapshot owner the two knowledge halves are copied through. [25]
- The record-collection inputs the caller supplies and the empty value the freeze defaults to. [26]
- **The production-composition case: a refused freeze publishes nothing, leaves no hidden stage, releases the pin it created, and the same leaf freezes afterwards.** [27]
- **The case that separates a stage a dead freeze left from a live one, driven through a real child process.** [28]
- **The end-to-end journey the packet names: freeze, `git gc --prune=now` measured against a control object, remove the worktree, reopen in a child process.** [29]

| `freeze_resolved_review` owns the behavior described above. | `freeze_resolved_review` | mcp/src/agents_remember/application/review_comparison_freeze.py:255-257 |
| `freeze_review_comparison` owns the behavior described above. | `freeze_review_comparison` | mcp/src/agents_remember/application/review_comparison_freeze.py:233-235 |
| `freeze_comparison_generation` owns the behavior described above. | `freeze_comparison_generation` | mcp/src/agents_remember/application/review_comparison_freeze.py:319-321 |

The following declarations carry the changed boundary.

- Ordinary and explicit recovery paths share exact resolved-pair composition. [30]
- Complete authentic owner records and channel provenance are checked before publication. [31]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The task artifact root it publishes into is
under the coordination root, which is outside both the code and the memory repository.

No meaningful cross-repo references found.

## 260921-ICR-L34 The Freeze Gets Its Production Caller, And A Placed Baseline Becomes Freezable

`260921-ICR-L34` (D62) is the leaf that made a leaf's review comparison producible at all. Two things
about *this* module are what it changed or established, and both belong on this card.

**The production entry now has a shipped caller.** `freeze_review_comparison` was complete and measured
but had **no caller outside the test suite**, so no leaf could publish a generation and every closed
leaf's review reopened from `history:recorded-source-range`. The caller is the CLI subcommand
`agents-remember review-record-comparison`
([`cli/review_comparison_record.py`](../cli/review_comparison_record.py.md)): it loads one enclosure
contract, composes a `ReviewSurfaceRequest` from that contract's own recorded identities, and calls this
function once, printing the outcome. Ordinary capture still requires the live candidate identity. L41 also permits the CLI to recover from an explicitly named retained parent and original curator digest. The retention owner revalidates that historical capture; closed resolutions continue to carry no live candidate identity.

**The caller is the first shipped caller to supply `parent`, and that is what makes a successor
readable.** `ComparisonFreezeOptions.parent` is documented as a caller-known fact, and the freeze derives
the successor's recorded index from it: a caller that names none publishes an **index 1** generation. A
leaf whose comparison legitimately changed therefore came to hold two index-1 generations with different
bindings, and `review_comparison_reopen` refuses a tied highest index by design — the leaf's own review
could no longer say which comparison it was reading. The CLI now discovers the standing generation
through `read_generation_refs` and names it, so a re-freeze publishes the next index with recorded
lineage rather than a second claim on index 1. Lineage was chosen over reclamation deliberately:
`review_comparison_reclamation` deletes only the *content* a manifest names and never the manifest
itself, so it cannot remove an index-1 identity, and a successor with recorded lineage is the only
owner-provided resolution.

**Carried, and the single most important thing for the next leaf on this route:** the owner still
permits the state it then refuses to read. `freeze_comparison_generation` will publish an index-1
generation for a leaf that already holds a readable one if a caller names no `parent`; the CLI supplies
it, but the next caller can reintroduce exactly the ambiguity. The guard belongs beside
`_reuse_or_refuse` — compute the parentless manifest, and if its generation id is *not* already
published while the leaf holds readable generations, refuse and name the predecessor. It was not added
here because it changes this owner's contract, and the leaf's mandate was to make the route reachable.
A second carried fact, measured by the leaf's adversarial verifier: because `lineage` sits **inside**
the seal (`review_comparison_generation._UNSEALED_FIELDS` names only `binding_digest`, `generation_id`
and `recorded_at`), naming a parent changes the derived id, so `_publish`'s `if final.exists()` reuse
branch is never taken in the ordinary sequence and `reused` is unreachable — every no-op retry appends a
generation with two full retained knowledge snapshots.

- **The production entry this leaf gave a caller, and the caller itself.** [32]
- **The caller options, including explicit predecessor identity and retained-parent recovery control.** [33]
- **The reuse branch that is never taken in the ordinary sequence, and the seal omissions that make it so.** [34]
- The lineage a named predecessor records: the id *and* that generation's manifest digest, so a successor is readable by identity. [35]
- Ordinary publication requires a live capture; explicit recovery revalidates the named retained parent capture without inventing a live identity. [36]
- The discovery the caller reads to name the predecessor, in a total order by index then id. [37]

## 260928-MIK-L25 A Tree Comparison Is Refused Before Anything Is Staged

**MIK-R25: no database copy is created, retained or read for a review.** `freeze_comparison_generation` now asks
`_unfreezable(resolved)` first. A resolution carrying `trees` (a converted leaf's four-tree comparison) or
`knowledge_unavailable` (a legacy comparison) is refused by `tree_comparison_refusal` (public since L37, so the
unchanged-knowledge freeze returns the same refusal): the comparison is four Git
trees, recorded with its pinning refs when it was resolved, so there is nothing to freeze; the next action is to
reopen it from its record under `notes/reports/review-comparisons`, whose refs are deleted when the task is
archived. The old refusal for a hand-assembled pair with no task root is unchanged and comes second. A dataset
comparison of an unconverted leaf freezes exactly as before.

- A tree or legacy comparison is unfreezable; a pair with no task root keeps its own refusal. [38]
- The refusal: recorded by trees, never copied (public since L37). [39]
- A tree comparison is never frozen into a dataset generation. [40]
