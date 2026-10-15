# skills/c-09-git-worktree-manager

| Field | Value |
| --- | --- |
| sourceRoute | `skills/c-09-git-worktree-manager` |

## Purpose

This route owns the agent-facing Git worktree lifecycle: start, attach, status, source-pair selection, resumable synchronization, closeout routing, integration, finalization, cleanup, abandonment, and reopen recovery. The canonical skill describes public contract-addressed operations; private journal, ref, and queue identities are not agent prompt inputs. It supplies worktree context to `c-12-closeout` rather than replacing the implementation workflow.

## Hot Path Summary

Closeout, sync, checkpoint and integration bind the actual code/memory refs and content. Ledger cache files remain available for downstream readers; their missing/stale/malformed state cannot block these operations or request another commit.

## Construction

The configured enclosure contract is the public operation address. Public sync loads that contract, validates the request and worktree authority, and delegates to the selection or sync transaction owner. Its preview skips fetching and does not publish selection or mutate journal residue.

Atomic-series admission is contract-scoped: each canonical series contract owns its activation record, including when masters share an exact code/memory source pair. The skill identifies manager dispatch, worker dispatch, atomic start, and attach as selecting operations; reviewer and curator inspection is not selection. Selection publishes `reconciling` without suspending chat, process, worktree, contract, or an already-claimed lifecycle journal. It reconciles both protected source tips and publishes `active` only when they are current. One master's selection excludes no other, and multiple nonterminal contracts remain valid. Task authoring does not consult activation authority; the closeout queue projects active, reconciling, or vacant waiting candidates.

The graph-less `atomic-sequential` default describes sprint shape: every commanded master executes atomically, with no declared dependency serializing independent masters. The queue implementation nevertheless refuses a sprint without `executionGraph` as `task-execution-topology-migration-required`; its message describes that default and offers graph authoring. The concurrency description therefore does not promise graph-less queue admission.

`worktree_sync` is one resumable enclosure-root transaction. It pins pre-sync heads and source tips, retains code or memory conflicts in operation-owned sync worktrees, and advertises continuation or cancellation on the same contract. Continue validates staged resolution and resumes. Cancel restores pinned heads, removes retained temporary worktrees, terminalizes the journal, and releases the exact reconciling selection to durable `vacant`. For external memory, the skill requires Git-history reconciliation, excludes `memory.md` from merge output, and refreshes that cache separately. Repeated code attributions remain valid newest-first memory history rather than being collapsed.

The sync store places its canonical record at `<enclosure-root>/reports/sync-operation.json`. It first reads that path; when absent, it reads the legacy `<enclosure-root>/.lifecycle/sync-operation.json`. After publishing a canonical record it attempts to retire the legacy copy. The skill separately states a no-fallback doctrine. This overview states the reader's actual fallback predicate and endorses neither store location as intended; it does not change the code or resolve the doctrine's policy.

Ordinary master/series integration records absent source-door authority as explicit `not-applicable` and does not require `directExecutionEnabled`. A present direct-landing door must still be proved, and a new leaf integration requires its exact claimed closeout source. The policy-gated direct-landing route is distinct from ordinary series integration. Accepted-series standing approval and explicitly raised developer approval gates retain their separate authority boundaries.

Integration checks the accepted objects and actual memory-source ancestry before moving protected refs. Its memory ancestry predicate does not consult ledger rows or require global code-key uniqueness. A cache projection's unresolved attribution is not a substitute for this Git proof.

Finalization proves the immediate landed branch edge and resolves the exact contract-bound task document. When the leaf names an existing immediate parent, or its folder's `task.json` master lists a leaf naming none, the finalizer derives that parent and reconciles its exact row to `Completed`. Supplied parent path and subtask number are identity assertions. A sub-task naming none whose existing folder task document is not a master is refused; standalone/no-parent leaves remain supported. The finalizer does not complete the parent task itself or recursively complete ancestors.

The public guidance names the judgment per route: leaf integration and recorded landing rejudge actual pairs; master final/checkpoint/recorded landings run validator, net staleness, chain and history ownership. Preview runs the same admission without mutating refused state. Public direct recovery availability must not be inferred from executor settlement.

## Invariants And Boundaries

Address operations by the configured canonical contract, never by a private operation id. Preview before live mutation; previews must leave selector, refs, journals, and worktrees unchanged. Pinned refs and the enclosure-root journal provide durable recovery evidence. Closeout sequencing belongs to `c-12-closeout`; this route resumes at integration and finalization.

Contract presence, task order, and queue rows do not elect a selected master. Selection is contract-scoped, and task mutation is not blocked by activation or operation state. Conflicts remain resumable and cancellable rather than being silently aborted. Direct-Git imitation of continuation or cancellation, tolerant readers, contract-presence fallbacks, and duplicated lifecycle authority remain prohibited by the skill; the sync-store account above describes current code without endorsing either location as intended.

Terminal cleanup releases only the exact selected contract and preserves a newer selection. The skill requires proven terminal evidence and archive/readback/receipt before deleting a live enclosure; it also defines a bounded no-remains exception when no locator was published and neither worktree folder nor work branches exist. Task completion and permission to delete an enclosure are separate proofs. Integration conflicts belong to the agent when current requirements and evidence determine the resolution; genuine semantic ambiguity returns through the architect.

Closeout and integration own Git transactions over code and memory-content legs, with consumer-cache refresh separate from committed content. They carry completed curation as a prerequisite rather than invoking the full memory-quality operation themselves. Full quality, test, certification, and review operations are not automatic transaction steps. Closeout preview nevertheless asks the mandatory invariant gate on converted memory: an apply-refused leaf returns `knowledge-gate-refused` with its open findings rather than `would-closeout`.

Every publication route requires the repository pre-commit check on its exact tree. Ordinary closeout/direct landing check before commit-tree; prepared code and memory use ordinary git commit hooks. Integration accepts a matching tree-bound Commit-Check-Pass fact or checks the candidate before protected ref movement. Reference-transaction hooks remain possible. Legacy strict-code-no-verify vocabulary is readable journal compatibility, not permission to skip checks.

Curation is complete at every leaf's contract scope: the full memory-quality operation is required, a named check or subset does not replace it, and every curator-actionable finding is repaired or escalated as blocked with its exact returned code. The raw `qualityChecklistStatus` controls quality readiness; the combined `checklistStatus` controls the coherence gate. When raw quality is not ready, coherence is not evaluated. When raw quality is ready but coherence validation fails, the combined status becomes `coherence-required`; publish the exact authority through prepare, publish, and validate. When coherence is already current, the combined ready status is retained and `closeoutReady=true`. Thus `ready-for-closeout` can be a combined-field value; its supposed impossibility is not a valid warrant for the raw-field rule.

The earlier card's forward-looking intent that already-landed and finalized leaves are not re-curated is retained as historical policy intent, not evidence of their current lifecycle status. Its attribution of whole-layer completeness to an earlier full-scope run requires the parent Curator's historical authority check.

## Verification Metadata

Exact source claims and citations are reconciled to the frozen canonical skill; verification
metadata awaits the real code commit.

This retained verification statement is metadata, not proof of a commit, acceptance, or completed lifecycle. No lifecycle authority was supplied or examined for those statuses.

## Coverage Boundary

The memory layer's configured onboarding include paths do not contain `skills/**`, although this card mirrors that source route. That configuration establishes a census-coverage mismatch. It does not establish that every sibling sidecar is stale, why this card was previously maintained by hand, or a current decision to retain or remove the mirror. The memory-quality controller separately checks governing overview resolution across the onboarding root; that check does not establish complete maintenance coverage for this mirror.

## Evidence

- Public sync composes selection and transaction owners without caller-supplied private ids; preview skips fetching and mutation. [4]
- Stable sync recovery is below the enclosure root; the current store includes a legacy-path reader contrary to the no-fallback doctrine. [5]
- Real memory ancestry is the landing proof. [6]
- Complete contract-scoped curation and coherence publication are prerequisites carried to closeout and integration. [9]
- Raw quality readiness and combined coherence readiness have three distinct paths. [10]
- Publication routes have different commit-hook behavior; ref hooks remain possible. [11]
- Governing-overview validation separately walks the onboarding root; it does not establish complete mirror maintenance coverage. [12]

- The canonical skill owns contract-scoped admission, resumable sync, integration conflict ownership, and exact terminal release doctrine. [1]
- Ordinary series integration and leaf direct landing remain distinct policy routes, with standing-series and raised-gate approval boundaries. [2]
- The graph-less default describes concurrency, but queue admission refuses a missing execution graph. [3]
- Finalization derives the immediate parent row while preserving identity assertions and standalone behavior. [7]
- Closeout preview asks the mandatory gate on converted memory. [8]
