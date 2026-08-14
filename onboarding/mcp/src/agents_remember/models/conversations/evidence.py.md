# mcp/src/agents_remember/models/conversations/evidence.py

| Field                  | Value                                                          |
| ---------------------- | -------------------------------------------------------------- |
| repository             | agents-remember                                                |
| path                   | `mcp/src/agents_remember/models/conversations/evidence.py`      |
| doc_type               | `file-level-onboarding`                                        |
| lastUpdated            | 2026-08-08T14:38+02:00                                         |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                     |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                                  |

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/evidence.py` (260731-EFA-L9, R2/R8) is the protocol-neutral evidence wire
contract set shared by the control plane and the conversation projectors: evidence frames,
pages, truncation envelope, and native-page windowing. Declaration bodies are unchanged from the
pre-split module.

## Code Commentary

### Logic

The reserved event keys (`AR_EVIDENCE_KEY`/`AR_EVIDENCE_METHOD_KEY`/`AR_TERMINAL_OUTCOME_KEY`,
cit:([`AR_EVIDENCE_KEY`], mcp/src/agents_remember/models/conversations/evidence.py:17-17)), the truncation marker and budgets
(`EVIDENCE_TRUNCATION_MARKER`/`MAX_PRESERVED_EVIDENCE_SCALAR_CHARS`/`MAX_NATIVE_EVIDENCE_PAGE`/
`EVIDENCE_PAGE_BYTE_BUDGET`), and the frame/page models (`EvidenceFrame`/`EvidencePage`/
`NativeEvidenceFrame`/`NativeEvidencePage`, cit:(["class EvidenceFrame"], mcp/src/agents_remember/models/conversations/evidence.py:80-80)) define the
wire shapes. `NativePageReader` (cit:(["class NativePageReader"], mcp/src/agents_remember/models/conversations/evidence.py:138-138)) is the native-domain page
protocol; `clip_evidence_payload` (cit:([`clip_evidence_payload`], mcp/src/agents_remember/models/conversations/evidence.py:301-301)) applies the bounded
truncation with the visible marker; `window_native_evidence_page`
(cit:([`window_native_evidence_page`], mcp/src/agents_remember/models/conversations/evidence.py:364-364)) windows native-domain pages with typed
identity and an opaque continuation cursor.

### Invariants And Boundaries

- The two coordinate domains (deque-domain vs native-domain) are disjoint and rejected
  cross-typed; every evidence response carries `bridgeEpoch`.
- Control-plane modules import the evidence contracts from here — legal because `serving` is
  above `models` (move ledger 2a).

### Todos

No known follow-up.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The harness-control evidence suite pins the shared evidence substrate. | `EvidenceBufferTests` | mcp/tests/test_harness_control_evidence.py:366-366 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the shared evidence module moved
  from `serving/harness_control_models.py`. Verification metadata pinned until closeout stamps
  the L9 code commit.
