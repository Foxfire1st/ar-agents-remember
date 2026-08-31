# mcp/src/agents_remember/serving/terminal_catalog.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/serving/terminal_catalog.py`        |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated | 2026-08-31T04:59+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[serving overview](overview.md)

## Purpose

Owns the durable hosted-occupant catalog and structural seat queries. It runs the one-way legacy
catalog migration before strict current parsing.

## Code Commentary

### Logic

`TerminalCatalog` reads/writes current task-document-and-role rows, looks up the singular running
occupant of a structural seat, and retains replacement/provenance/evidence fields. Reads migrate
legacy rows first and then validate the current model; writers do not emit both schemas.
`active_for_task` consumes the shared incumbent/staged-heir selector.
`DispatchBriefReceiptStore` composes with the catalog atomic storage unit to idempotently bind one
durable inbox receipt to the exact generation and refuse a different second receipt.
Address-bound receipt lifetime is owned by the row transformation: same-seat promotion retains it,
while cross-seat or role movement clears it before this store writes the new row.

### Conventions

Catalog methods expose runtime ids only as occupant correlations. Topology qualification lives in the
task/structural resolver rather than this persistence class.

### Invariants And Boundaries

- One running occupant may claim a singular task-document-and-role seat.
- Migration is one-way and precedes strict parsing.
- Spawn ancestry remains audit provenance.
- Current writers never restore leaf-key fields.
- A staged heir is current only after the incumbent leaves.
- One generation may bind exactly one pinned dispatch-brief receipt.
- Receipt evidence cannot migrate to another canonical address.

### Todos

Removal of migration code requires a separately governed durability-epoch decision.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The catalog queries current occupancy by task document and role through the shared selector. | `active_for_task` | mcp/src/agents_remember/serving/terminal_catalog.py:86-95 |
| One exact generation idempotently binds one durable pinned-brief receipt. | `DispatchBriefReceiptStore` | mcp/src/agents_remember/serving/terminal_catalog.py:419-448 |
| Legacy rows migrate before strict model parsing. | "rows = migrate_terminal_catalog_v1(self.path.parent.parent.parent, rows)" | mcp/src/agents_remember/serving/terminal_catalog.py:399-399 |
| The current catalog model owns strict row serialization. | `TerminalCatalogEntry` | mcp/src/agents_remember/models/terminal_catalog.py:67-550 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## 260821-CLIVE Execution-Evidence-Safe Compaction

Compaction recognizes task-bound worker and curator rows plus reviewer rows whose recorded spawn
altitude is leaf (including legacy rows with no recorded level) through their current or replacement
task-document ref. Master and sprint reviewers are review-plane seats, not leaf execution evidence.
A terminated leaf-execution row past retention is reclaimable only after its id is
present in the explicit task-registered set. Running, exited, landed, recent, and unregistered leaf
execution rows remain. Thus ordinary retention cannot turn observed execution into “never started.”

## Update History

- 2026-08-31T04:59+02:00 — 260821-ARSPAWN-L5 independent-review repair: bounded execution-evidence
  compaction to worker/curator and leaf-altitude reviewer generations rather than treating every
  polymorphic reviewer as leaf execution. Verification remains closeout-owned.

- 2026-08-26T16:03+02:00 — Post-failure repair: extracted dispatch-receipt mutation into
  `DispatchBriefReceiptStore`, preserving the same atomic catalog storage boundary while returning
  `TerminalCatalog` to the 15-operation surface cap. Verification remains closeout-owned.


- 2026-08-25T23:19+02:00 — Contract-wide citation curation: re-read the current anchored claim(s), retained the supported wording, and cleared verification metadata for closeout-owned restamping.

- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2 final curation: clarified one-receipt idempotency
  and the prohibition on carrying address-bound proof across a document or role move. Verification
  remains closeout-owned.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: current-seat lookup now recognizes the staged heir
  after incumbent exit, and the catalog owns idempotent pinned-brief receipt binding. Verification
  remains closeout-owned.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: recorded task-registration gating for terminated leaf-seat reclamation. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-11T14:29+02:00 — Re-read the current `TerminalCatalogEntry` model used by this store
  and widened its citation to include the dataclass declaration; verification metadata remains
  unchanged for governed closeout.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: rewrote after the row vocabulary moved to
  `models/terminal_catalog.py`; preserved the batch/compact/atomic-write store knowledge from the
  pre-split card. Verification metadata pinned until closeout stamps the L9 code commit.
