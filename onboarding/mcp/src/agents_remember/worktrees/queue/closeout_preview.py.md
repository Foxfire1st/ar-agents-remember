# mcp/src/agents_remember/worktrees/queue/closeout_preview.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_preview.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:53 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Builds response-only proposed commits, summaries, and ordering without mutating worktrees or protected refs.

## CCR-R12@v5 Current Transaction Preview

The preview describes the normal transaction sequence: validate candidate/source identity and
explicit approval, commit code, perform raw onboarding/entity/route-index refresh, commit external
memory content, refresh the derived ledger cache, and finalize the contract. It does not advertise strict
code quality, memory quality, selected certification, curator coherence, or independent review as
an automatic step. Series previews remain recording-only for already landed named refs; full suites
are an explicit developer request.

## Code Commentary

### Logic

The proposed payload has code and memory Git legs plus an informational `ledger_cache` object containing `would_update` and `path`. Only code and memory receive messages. Leaf ordering ends with cache refresh then contract publication; a series records exact named refs and proposes no cache write.

`proposed_closeout_commits` distinguishes ordinary leaves from exact named-ref atomic series. Series previews describe already-recorded code and external-memory commits and do not promise ambient refresh or ledger writes that apply will not perform. Summary and ordering helpers keep preview and apply handoffs aligned.

### Conventions

Accepted input, exact Git facts, and typed owner results stay distinct from disposable projections.

### Invariants And Boundaries

- Preview never writes Git, contract, queue, or memory state.
- Series facts are named-ref/candidate facts, not ambient checkout facts.
- Proposed work and ordering must remain executable by the corresponding apply route.

### Todos

None recorded for the ledger-retirement boundary.

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `proposed_closeout_commits` separates code/memory Git intent from informational ledger_cache output. | `proposed_closeout_commits` | mcp/src/agents_remember/worktrees/queue/closeout_preview.py:9-67 |
| `closeout_summary` describes named-ref series recording or leaf content and cache refresh. | `closeout_summary` | mcp/src/agents_remember/worktrees/queue/closeout_preview.py:70-81 |
| `closeout_order` orders real Git outputs, cache refresh, and contract publication without a ledger commit. | `closeout_order` | mcp/src/agents_remember/worktrees/queue/closeout_preview.py:84-102 |

| Finding | Anchor | Source |
| --- | --- | --- |
| Proposed commit payloads separate leaf mutation from exact series recording. (`proposed_closeout_commits`) | `proposed_closeout_commits` | mcp/src/agents_remember/worktrees/queue/closeout_preview.py:9-67 |
| Summary and ordering publish the same lifecycle altitude. (`closeout_summary`; `closeout_order`) | `closeout_order` | mcp/src/agents_remember/worktrees/queue/closeout_preview.py:84-102 |

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## 260821-CLIVE-L1 Preview Parity

Preview now requires normalized `effectiveInput` and renders each leg's typed intent. It includes a `message` only for enabled legs for code and memory; the separate cache view has no message. The same value is fingerprinted, journaled, rehydrated, recovered, and consumed by apply. This module describes proposed writes; it neither selects candidates nor owns lifecycle evidence.

## Cross-Repo References

No separately configured cross-repository implementation governs this file; any external-memory repository is addressed by the task contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## Update History

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=3025e1fc7eb6c92397a1a53d61f224bf9f791e87398fc040f67819fe26f4e3fa. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.

- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/queue/closeout_preview.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created closeout preview projection onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
