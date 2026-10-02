# skills/c-09-git-worktree-manager

| Field | Value |
| --- | --- |
| sourceRoute | `skills/c-09-git-worktree-manager` |

## Purpose

This route owns the agent-facing Git worktree lifecycle: start, attach, status, source-pair
selection, resumable synchronization, closeout routing, integration, finalization, cleanup,
abandonment, and reopen recovery. The skill describes public contract-addressed operations; it does
not move private journal, ref, or queue identity into agent prompts.

## Hot Path Summary

Closeout, sync, checkpoint and integration bind the actual code/memory refs and content. Ledger cache files remain available for downstream readers; their missing/stale/malformed state cannot block these operations or request another commit.

## Detailed Route Context

Atomic-series admission is a contract-scoped authority: each canonical series contract owns its own
activation record, so masters that share one exact code/memory source pair never share that state.
Manager dispatch, worker dispatch, and atomic start/attach are selecting operations; reviewer and
curator inspection is not. Selection publishes `reconciling` for that exact contract, which suspends
nothing — not its chat, process, worktree, contract, or already-claimed lifecycle journal — then
reconciles both protected source tips and publishes `active` only when they are current. One master's
selection never pauses or excludes another, and multiple nonterminal contracts remain valid. Task
authoring never consults the activation authority, and the closeout queue merely projects active,
reconciling, or vacant waiting candidates.

Nothing serializes a graph-less sprint. A sprint without an `executionGraph` declares no
dependencies, so the shipped `atomic-sequential` default describes the sprint's SHAPE — every
commanded master executes atomically — and is not a serialization mechanism: independent atomic
masters proceed concurrently and no master is held because another master is selected. Only an
explicit `executionGraph` gates masters on real predecessors.

`worktree_sync` is one durable enclosure-root transaction. It pins pre-sync heads and source tips,
retains code or memory conflicts in operation-owned `.sync` worktrees, and advertises
`resolution_action=continue|cancel` on the same contract. Continue validates staged resolution and
resumes; cancel restores pinned heads, removes retained temporary worktrees, terminalizes the
journal, and releases an exact reconciling selection to durable `vacant`. No direct-Git recovery,
tolerant reader, or contract-presence fallback is part of the doctrine. For external memory,
continuation proves the admitted Git history and leaves the ledger to its rebuild: the transaction
does not commit `memory.md` or use its rows as a Git guard. A row the
rebuild cannot resolve is reported as an exclusion. Repeated code commits are valid
newest-first state history; the newest row supplies current authority and older same-code rows
remain audit evidence.

Ordinary series integration records absent source-door authority as explicit `not-applicable` and
does not consult `directExecutionEnabled`. The policy-gated direct-landing route is only for an
explicitly selected leaf delivery without an enclosure; a fresh enclosed leaf continues to require
its exact claimed closeout source.

Terminal cleanup releases the exact selected contract before its authority can disappear. A newer
selection is never cleared by cleanup of an older contract. Integration conflicts are agent-owned
when current requirements and evidence determine the resolution; only genuine semantic ambiguity
returns through the architect.

## Conventions

- Address every operation by canonical enclosure contract, never by private operation id.
- Preview before live mutation; dry-run must leave selector, refs, journal, and worktrees unchanged.
- Treat the enclosure-root journal and pinned refs as durable recovery evidence.
- Route closeout sequencing to `c-12-closeout`; this skill resumes at integration/finalization.

## Invariants And Boundaries

- Each canonical series contract owns its own activation record; multiple nonterminal contracts
  remain valid and one master's selection excludes no other.
- Contract presence, task order, and queue rows never elect a selected master.
- Conflicts are retained, resumable, and cancellable; they are not silently aborted.
- Cleanup releases only the exact selected terminal pointer and preserves newer selections.
- No fallback reader or duplicated lifecycle evidence is allowed.
- Memory-merge validation proves Git state only: it requires no row list and never imposes global
  code-key uniqueness. A row the projection cannot resolve is the projection's to report.
- Ordinary series integration is never reclassified as direct execution merely because it uses a
  root series contract.


### Todos

Exact source claims and citations are reconciled to the frozen canonical skill; verification
metadata awaits the real code commit.


## CCR-R12@v5 Transaction Boundary

Closeout and integration are authorized Git transactions over code and memory-content legs, followed by best-effort consumer-cache refresh. Their transaction-owned commit legs suppress automatic quality and test hooks; ordinary explicit Git hook policy outside closeout/integration remains unchanged. Preview, conflict, and ref safeguards remain in this route; quality, tests, memory-quality, certification, and review operations are contextual or explicit rather than automatic.

## Evidence

### Repo-Internal References

- The canonical skill owns contract-scoped admission, resumable sync, integration conflict ownership, and exact terminal release doctrine. [1]
- Ordinary series integration and leaf direct landing remain distinct policy routes. [2]
- The graph-less atomic-sequential default describes sprint shape and serializes nothing between the masters. [3]
- Public sync composes the selection and transaction owners without exposing private ids. [4]
- Stable operation recovery is stored below the enclosure root. [5]

Current working-candidate evidence for this route:

- Real memory ancestry is the landing proof. [6]

## 260915-CAPS-L18 Complete Curation Reaches This Route

CAPS-R18@v1 inverted the optional/narrow-curation doctrine in the shipped instruction sources. The
sentences that presented the full `memory_quality_check` operation and the `curator_coherence`
certification as developer-request-only diagnostics, "never routine closeout/integration prerequisites",
are gone. The rule is now normative: **curation is complete on every leaf** — the full operation runs at
the leaf's contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every
curator-actionable finding is repaired or escalated as blocked with its exact returned code, and the
operation is re-run after every repair until `curatorActionableCount=0` and the **raw**
`qualityChecklistStatus=ready-for-closeout`. The **combined** `checklistStatus` is rewritten to
`coherence-required` **only when the coherence record is then missing or stale** — that is the coherence
gate, cleared by publishing the `curator_coherence` authority with `prepare` → `publish` → `validate`.
On the success path, where the record is already current, the combined field is **not rewritten** at all
and keeps its incoming `ready-for-closeout` value, with `closeoutReady=true`; `ready-for-closeout` is
therefore observable in the combined field once the whole pipeline is already complete. **Field-name
correction (`D35`, made by 260915-CAPS-L10):** this sentence previously named
`checklistStatus=ready-for-closeout` as the loop's termination condition; read the raw field to end the
loop and the combined field to decide the coherence gate
(`application/memory_quality/controller.py:664`, `:671`, `:678`, `:685-687`).

**Warrant corrected by `CAPS-R19` (leaf `260915-CAPS-L19`).** The `D35` correction above originally rested
on the sentence *"`ready-for-closeout` is never a value of the combined field."* That absolute claim is
**literally false**, and `CAPS-R19`'s revision note records it as superseded by the three-path model now
stated here. The field-name correction it supported still holds; only its stated warrant was wrong.
**Attribution is complementary and both halves hold:** `260915-CAPS-L10`'s curator corrected the
**onboarding cards** that carried the wrong form, while `CAPS-R19` corrected the **shipped sources** — the
five loop-gate carriers, their nine generated copies, and the guard registry's own docstring — and brought
`docs/reference/mcp-tools.md` into both the loop-gate census and the guard's `LOOP_GATE_DOCUMENTS`.

Two corrections the inversion must not collapse, both preserved: closeout still owns only the Git
transaction and **invokes** nothing — it **carries** the completed curation as a prerequisite; and the
rule is about the completeness of curation, not about unscoped runs, so "complete" always means the whole
operation at the leaf's contract scope. The ruling is forward-looking: the already-landed and finalized
leaves are not re-curated, and whole-layer completeness is discharged by L11's full-scope run at the
frozen tip.

## 260928-MIK-L38 Finalization Reaches The Master That Lists A Leaf Naming None

The route's finalization doctrine gains two clauses (MIK-R38; ruling 2026-09-30T12:33:07 Q3): the finalizer derives
and reconciles the exact row when the bound leaf declares an existing immediate parent "or names none and its
folder's `task.json` master lists it", and "a sub-task naming none whose folder `task.json` is not a master is
refused" (review R1 note 5, ruling 13:11:32; "sub-task" rather than "leaf" by ruling 14:12:52, so a `light` task that
is its own `task.json`, which finalizes standalone, is not covered). Standalone leaves, the identity assertions and
the rule that the parent task itself is not completed are unchanged. `scripts/sync-skills.py` rewrote the package
copy and the eight harness starter copies byte-identically.

- The finalizer paragraph's two new clauses. [7]

## 260928-MIK-L37 The Closeout Preview Asks The Mandatory Gate On Converted Memory

The route's closeout paragraph gains one statement: the preview, which runs no quality, test, memory, certification
or review tool, does ask the mandatory invariant gate on converted memory, and a leaf the apply would refuse is
answered `knowledge-gate-refused` with the open findings, never `would-closeout`. `c-12-closeout` holds the detail.
`scripts/sync-skills.py` rewrote the package copy and the eight harness starter copies byte-identically.

- The preview asks the mandatory gate on converted memory. [8]

## Ungoverned Mirror Status (known defect)

This route overview lives in the `onboarding/skills/**` tree, which mirrors the code repository's
`skills/**` route. `skills/**` is absent from `settings.json`'s `pathRules.include`, so this whole
onboarding tree sits outside normal onboarding census coverage: it is legacy and ungoverned. It is
retained here only because the contract-scoped memory-quality checker still validates these documents
whenever `skills/**` is part of a leaf's changed set, which is exactly why this overview was updated
by hand rather than by a governed maintenance pass. The remaining sibling sidecars under
`onboarding/skills/**` — the other role, criteria, and template cards — are knowingly stale and are
deliberately left untouched pending a follow-up decision on whether this mirror should be governed or
removed. That mismatch between the declared path rules and the enforced checking scope is itself the
recorded defect.
