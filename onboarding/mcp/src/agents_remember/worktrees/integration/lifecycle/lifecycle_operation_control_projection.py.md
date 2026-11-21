# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_projection.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Derives advertised journal controls for an admitted direct-landing generation from its exact record and contract evidence.

## Code Commentary

### Logic

Legal direct-landing controls derive recoverability from the admitted record and actual code, memory and ref evidence. A changed direct request may replace eligible retired terminal evidence. The direct successor's message belongs to its memory-content commit.

It builds a context from the canonical record and contract and derives actions without mutation. A nonterminal direct record may offer recover and, when output is unchanged, cancel. An eligible cancelled record offers a new direct-landing call. An eligible completed record can offer retire. A retained direct `termination-required` cell offers exact cancellation only.

The legacy direct reuse filter checks compatible `taskIntent` or an accepted direct leaf binding. A door-bearing direct record remains visible for audit and offers no controls. Completed direct disposition uses the same exact owner and idle integration-claim predicates as admission. The completed owner may retire, and a new request goes through direct landing.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

#### Invariants And Boundaries

- Controls are projections of current durable evidence; unavailable actions stay absent and no control may imply a transition the journal cannot validate.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- Closeout and integration history offer no controls. The handler's direct compatibility filter allows recovery with canonical intent or accepted direct leaf input. The public status projector separately requires canonical intent before showing legal controls.

### Todos

None recorded.

## Direct-create recovery controls

Direct-create recoverability is classified from persisted same-generation code/ref/memory evidence. A mechanically recoverable cut advertises public recovery; real contradictions keep developer-decision. Controls are a projection of current evidence, not permission to bypass the mutation owner.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.


- The direct-landing control projector derives applicable actions from the exact generation and its evidence. [1]


- The direct-landing control projector derives applicable actions from the exact generation and its evidence. [2]


- `_direct_successor_control` constructs a direct successor from code identity and the memory-content message. [4]

The source file is the direct evidence for this unit; its governing overview records adjacent owners.



- A compatible task-intent record or accepted direct leaf binding permits generation reuse at control time. The status projection separately requires exact task intent. [5]



### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

No additional cross-repository evidence applies.

## CCR-R02@v2 Missing-Intent Control Barrier

The direct reuse filter removes recovery offers when both compatible task intent and the accepted direct leaf binding are absent. The status projector applies its own exact-intent check. An eligible legacy `termination-required` generation offers exact cancellation. The stored state is a compatibility fact.

## CCR-R18@v1 Exact Same-Generation Cancellation Cell

A direct generation in `termination-required` offers one action, cancel the exact generation. The projection still requires a doorless direct record, current authority and recoverable evidence.

## CCR-L42 current candidate



- Direct-landing recoverability is classified from the persisted generation's typed accepted input, exact code commit/tree, memory repository/ref and accepted or intended live memory evidence. [6]




- Exact completed direct owners are offered retire subject to disposition eligibility; direct supersede is unavailable. [7]


- Earlier door-bearing direct records remain readable but offer no controls. [8]
