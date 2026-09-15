# mcp/src/agents_remember/worktrees/queue/closeout_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:58 |
| lastVerifiedCommitHash | `7cbda30d9a9a4c2944382fbef46ac58b85329935` |
| lastVerifiedCommitDate | 2026-09-15T05:15:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Owns restart-safe proof and journaling around closeout's real code and memory outputs. Finalization recovery re-proves exact task refs and accepted source ancestry, without consulting a ledger row or creating a cache-maintenance commit.

## CCR-R12@v5 Current Recovery Boundary

Recovery proves accepted code trees, exact code and memory refs, and journaled mutation/publication evidence. The code writer uses the prepared staged-index helper with `--no-verify`. Memory recovery consumes an already accepted output and may refresh its disposable cache; it never creates a ledger commit.

## Code Commentary

### Logic

`MemoryCloseoutOutcome` carries the real memory output plus onboarding/entity/route refresh data. Its `ledger_repair` field is informational cache status only. `prove_closeout_recovery_commits` requires the recorded code commit to equal the actual leaf HEAD or exact series work ref; non-external modes refuse an unexpected external-memory output.

`_prove_memory_output` requires a nonempty accepted memory output, reads the exact named series ref or clean leaf HEAD, and proves that the accepted memory base is its ancestor. Leaf cleanliness excludes only root `memory.md`; source content changes still refuse. Cache refresh occurs after the proof and cannot replace it.

`accepted_code_commit` either proves a clean existing output or journals intent, stages, commits, and proves the exact code mutation. It verifies the committed tree against the accepted candidate tree before returning. `resume_external_commits` reuses the proven memory output and publishes the code/memory recovery pair without replaying memory mutation.

### Conventions

Recovery state enters through typed `WorktreeArgs`; `report_operation_progress` publishes generation-bound facts. Verified-existing outputs do not acquire fabricated mutation evidence.

#### Invariants And Boundaries

- A nonempty recorded commit is evidence to prove, never a suggestion to overwrite.
- Actual code and memory refs, the accepted code tree, and memory source ancestry must agree.
- Cache bytes, cache presence, and cached pairings carry no Git authority.
- The disposable queue owns no mutation evidence despite this module's package location.
- Contract publication remains the coordinator's responsibility; this owner proves outputs.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `MemoryCloseoutOutcome` contains the memory commit and informational refresh results. | L28-L36 | [mcp/src/agents_remember/worktrees/queue/closeout_recovery.py](mcp/src/agents_remember/worktrees/queue/closeout_recovery.py) |
| `prove_closeout_recovery_commits` proves exact output refs without consulting a cache table. | L39-L55 | [mcp/src/agents_remember/worktrees/queue/closeout_recovery.py](mcp/src/agents_remember/worktrees/queue/closeout_recovery.py) |
| `_prove_memory_output` checks memory source ancestry and substantive cleanliness before best-effort cache refresh. | L58-L81 | [mcp/src/agents_remember/worktrees/queue/closeout_recovery.py](mcp/src/agents_remember/worktrees/queue/closeout_recovery.py) |
| `accepted_code_commit` commits or reuses the exact accepted code tree and records its proof. | L84-L141 | [mcp/src/agents_remember/worktrees/queue/closeout_recovery.py](mcp/src/agents_remember/worktrees/queue/closeout_recovery.py) |
| `resume_external_commits` re-proves existing memory output and republishes only the code/memory pair. | L144-L160 | [mcp/src/agents_remember/worktrees/queue/closeout_recovery.py](mcp/src/agents_remember/worktrees/queue/closeout_recovery.py) |

The current recovery primitives below establish exact two-output proof and cache-independent resumption.

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## R39 Series Closeout Recovery

Non-leaf closeout now records already-landed clean code: it requires a clean series/master checkout
and takes current HEAD. Leaf recovery retains commit/retry reconciliation. Series closeout cannot
become another code-commit or acceptance owner.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## 260821-CLIVE-L1 Evidence-Aware Commit Recovery

New code commits publish accepted mutation intent before Git and exact proof afterwards. Verified-existing commits report recovery cells without inventing a mutation. The same monotonic evidence principle remains for memory output; the removed ledger-recovery stage has no successor commit path. Direct-landing recovery remains outside this owner.

## 260821-CLIVE-L2 Current Contract

The current seams are `MemoryCloseoutOutcome`, `prove_closeout_recovery_commits`, `accepted_code_commit`, and `resume_external_commits`. They publish root-journal evidence from exact Git facts, independent of queue phase or ledger cache. The earlier package relocation did not make the queue an authority.


## Retired Ledger Recovery Boundary

The removed `integration/closeout/ledger_recovery.py` classified ledger byte/tree contradictions and recovered a third ledger mutation. That behavior is intentionally gone. Its durable principles remain here: recovery advances only proved outputs, recorded commit identity is immutable, and queue state cannot substitute for journal evidence. There is no current source owner for reconstructing a ledger commit, so its old one-to-one sidecar is retired.

The old sidecar's 2026-08-25 creation provenance was: “Created during PDLS whole-system reconciliation after source and requirement review. Verification remains closeout-owned.” This records the retired owner's history; it does not claim current ledger authority.

## Update History

- 2026-09-15T00:58 UTC — Rechecked the formatted L9 working candidate and rebound current references after source cleanup; source-sha256=6682e6c58d342bbdc3109fcd1f9eccdecfe492b6bf808ad108ee1e1529314ce7. The older working-candidate snapshot and verification provenance are retained.

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=a7ba0387d7ad07da815838182c4f5a3300204352b5076b7367818cce6d7f596b. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.

- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `MemoryCloseoutOutcome` repointed to mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:47-56. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `prove_closeout_recovery_commits` repointed to mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:59-74. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `accepted_code_commit` repointed to mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:168-226. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


- 2026-08-26T14:32+02:00 — Corrected closeout retry semantics for settings-only memory changes:
  exact current edges are reused, while a different historical same-code mapping causes a new
  memory-state row and ledger commit. Verification remains closeout-owned.
- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-input and ledger-recovery package relocations; journal-owned recovery proof and exact tuple reconciliation are unchanged.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/queue/closeout_recovery.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

- 2026-08-14T11:48:55+02:00 — R42 curator: recorded the move of `MemoryCloseoutOutcome` and
  `prove_closeout_recovery_commits` from the closeout coordinator into the recovery owner; updated
  direct forcing-test citations. Verification remains closeout-owned.

- 2026-08-14T11:25+02:00 — R39 curator: documented clean landed-code recovery for series/master
  closeout. Verification remains closeout-owned.

- 2026-08-14T09:37+02:00 — Reopened L23 acceptance ownership: series/master recovery records only
  a clean, already-landed code HEAD so no post-approval path can create an unreviewed master commit.
- 2026-08-14T05:26Z — Created for the L23 final candidate: documented monotonic closeout commit
  recovery and the exact code-to-memory-to-ledger reconciliation boundary. Verification remains
  closeout-owned until the source commit exists.
