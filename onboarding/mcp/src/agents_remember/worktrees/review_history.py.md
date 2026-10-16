# mcp/src/agents_remember/worktrees/review_history.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

Owns task-document transitions for the fixed-list review protocol: settings-owned pending-round admission, sealed-list result publication, cumulative recorded architect/developer allowances, and a same-round record-only result guarded by the independently resolved candidate identity.

## Code Commentary

### Logic

`begin_task_review` treats missing or explicit zero state as round zero and starts a pending first round with the supplied settings number, or its fallback. A pending replay stays on the same round and does not add allowance. Each new begin recomputes `limit` as the current settings number plus approved extras. At exhaustion an approval naming architect or developer and positive `additionalRounds` opens the next round, records normalized approval words and adds the allowance without resetting count or sealed findings. Earlier developerApproval input is normalized to developer approval. Premature or malformed approval is refused. A clean sealed review may begin a later round within the budget; it does not reopen the finding list. This module validates the recorded shape, not approval authenticity.

`record_task_review` accepts verdict, findings, remainingFindingIds, verdictRef, optional checked candidateTree and finite reviewKind (default code). An absent state permits the initial baseline record; a pending first result seals findings, and pending successors shrink only the preceding remaining set. A nonpending result passes only if the recorded authority-resolved candidateIdentity and the current resolved identity are present and equal; a recorded candidateTree also requires the same checked-tree claim. Missing, unproven or changed identity refuses with begin_review as the next step. The result stays on the recorded round, still cannot add/reintroduce findings, and a passing result leaves none unresolved. The caller supplies the independent binding, which is persisted when available. A first or legacy zero-limit record is backfilled from the supplied settings number plus extras; a positive stored limit is not rewritten by record.

`require_pending_review` returns the existing task-owned state unchanged, or a first-round pending default when the field is absent. Despite its name, it does not reject an existing nonpending state; actual begin/record admission is owned by the transition functions.

### Invariants And Boundaries

- Missing state means zero; no external history store or identity/authentication claim is introduced.
- The transition is monotonic over the sealed finding list: later rounds can only remove remaining IDs.
- The budget is the supplied current settings number plus positive cumulative approved extras; approval never resets count or baseline.
- This module owns state transitions and comparison/persistence of the supplied candidate binding, not candidate resolution, route-evidence construction, integration authority or reviewer authentication.
- The worker report records implementation checks only; this card does not claim review or acceptance.

### Todos

None.

## Current Contract

reviewKind defaults to code and explicitly selects memoryReviewState only for memory; other values refuse. Begin/record operate only on that lane, preserving sibling code state, sealed baseline/shrinking IDs, current settings limit, cumulative approved extras and unchanged-candidate guards. Successful pending results append one typed ReviewRound with the then-remaining Boolean. A record-only check appends no row and leaves its original findingsRemain/kind intact, though its verdictRef may be updated. Worker tries count failed code rows; Curator tries count failed memory rows. Missing state is zero; incomplete/nonsequential typed history or launch-recovered unreadable evidence is unavailable, not guessed from legacy rounds. Other roles count zero. require_pending_review remains code-only compatibility. No transition here steps a model up, authenticates a reviewer or creates a grant.

A try is a recorded code round with findings remaining for Worker, or an independent recorded memory round with findings remaining for Curator. Record-only checks are not tries. Other roles are on-request only. At the configured threshold the starter starts a successor from user-configured step-up choices; no new review round or allowance follows. Mode/permission features belong to the user-selected harness/model and are not borrowed across differing scopes; omitted cross-scope choices use host defaults. Counting and launch execution remain with their actual owners.

The governing workflow opens an independent memory review after CODE PASS on the same task using begin_review/record_review with reviewKind=memory. It has its own immutable baseline and shrinking IDs, under the same settings limit and extra-round approval rule, and never resets code reviewState. The signed rollout applies only to memory reviews begun after L88 lands; already-underway reviews (L168, L56, L57, L59) finish with their sealed-report workflow, with no migration/backfill. This describes the candidate contract, not a claim that the serving build already supports it.

This account is bound to the candidate source, not a claim of a running serving build or a fresh execution/acceptance verdict. Existing historical accounts remain historical.

## Evidence


- Worker/Curator typed review census, record-only exclusion and unknown history. [4]
- Reason admission, threshold and differing-harness/model inheritance boundary. [5]
- Record-only memory identity comes from memory authority, never the sibling code root. [6]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [7]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [8]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [9]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [10]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [11]

### Docs References

No external Domain Documentation source governs these task-owned transitions.

No configured external source applies.

### Repo-Internal References

- Error/status boundary, cap-aware begin semantics, and pending admission. [1]
- Publication field validation, architect/developer approval parsing, and sealed baseline creation. [2]
- Successor monotonicity and duplicate/blank-ID refusals. [3]

## Historical L41 Source File Binding

At the historical L41 preparation, the source bytes were SHA-256
`a9ef793019ed3e2a66c258d977a493d9f431194b91d2f6c4897acd5821a895b6`
(`9166` bytes, `235` lines). The source is an uncommitted preparation candidate, so
verification metadata remains blank until a genuine commit-owned refresh.
