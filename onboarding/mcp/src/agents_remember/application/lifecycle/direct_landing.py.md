# mcp/src/agents_remember/application/lifecycle/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/lifecycle/direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:19+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application overview](../overview.md)

## Purpose

The application boundary for the journaled direct-landing operation. It admits the configured
contract through the one closed application API, passes that exact accepted observation into the
task/contract-addressed direct-landing generation, and projects typed admission or operation
refusals. Durable mutation and recovery remain below this wrapper; it owns neither queue state nor
an alternate configured-contract reader.

## Code Commentary

### Logic

`direct_landing_tool(config, request)` calls `worktrees.direct_landing.direct_landing(config,
request)` and returns its success dict; on `DirectLandingError` it returns
`{ok: False, operation: "direct_landing", state: "refused", status: exc.status, detail: str(exc)}`
so the fail-closed reason reaches the wire in the strict response shape.

### Conventions

The application layer owns error translation; all validation and mutation live in
`worktrees/direct_landing.py`. Re-exports `DirectLandingError`, `DirectLandingRequest`, and
`direct_landing_tool` for the payload builder.

### Invariants And Boundaries

- Refusals always carry a typed `status` and human `detail`; no silent fallback to a success shape.
- This module never commits, never moves refs, and never reads the ledger itself.
- Recovery projection may add nested door/lifecycle evidence but cannot overwrite `ok`, top-level
  `state`, `status`, or the refusal detail selected by the application boundary.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The application boundary translates operation errors into typed refused responses. | `direct_landing_tool` | mcp/src/agents_remember/application/lifecycle/direct_landing.py:54-103 |
| The operation it wraps. | `direct_landing` | mcp/src/agents_remember/worktrees/direct_landing.py:132-144 |
| The request model it accepts. | `DirectLandingRequest` | mcp/src/agents_remember/worktrees/direct_landing.py:105-120 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L1 Input Boundary

This wrapper returns the full typed refusal payload—status/detail plus `invalidFields`,
`resolvedPlan`, and `correctedCall`—and passes successful `effectiveInput` through unchanged. L2
extends that boundary with closed configured-contract admission and durable recovery below it:
memory and ledger remain sequential Git commits, but write-ahead journal evidence and
same-generation reconciliation now make every partial cut recoverable. The landing lock remains
transient serialization and is not recovery authority.

## 260821-CLIVE-L2 Current Contract

The current source seams include `direct_landing_tool`. The application wrapper now admits the configured contract through the one closed API, passes the exact accepted observation into the journaled direct-landing operation, and projects typed refusals. It no longer describes direct landing as an unjournaled synchronous sequence.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current module exposes `direct_landing_tool` at this ownership boundary. | L54-L103 | `mcp/src/agents_remember/application/lifecycle/direct_landing.py` |

## 260821-DAGQC-L2 Outcome Normalization

The wrapper normalizes any non-final lower-level projection into the exact refused outcome before
adding recovery guidance. Merge order is explicit: nested journal state remains observable, while
the application-owned outcome/status cannot be overwritten by generic recovery dictionaries or an
unreadable-journal projection.

## Update History

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: made refused outcome/status authoritative over nested recovery projection and kept journal state below the top-level direct-landing vocabulary. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/application/lifecycle/direct_landing.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for the direct landing operation (L16-R8):
  the error-translating application boundary over the worktree operation. Verified at code
  commit a9d50e08.
