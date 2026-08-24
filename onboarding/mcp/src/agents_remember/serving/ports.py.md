# mcp/src/agents_remember/serving/ports.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/serving/ports.py`                    |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-24T14:43+02:00                                       |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`                   |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[serving overview](overview.md)

## Purpose

`serving/ports.py` (260731-EFA-L9, R8) is the canonical conversation read and control port
surface. It holds `ActiveConversationPort`, `ConversationLibraryPort`, `ControlSessionLike`,
`TerminalCatalogPort`, and `ControlPlanePort` so conversation modules no longer import
`harness_control_client` or `terminal_catalog` directly; `serving/conversation/ports.py`
re-exports these names for the conversation package.

## Code Commentary

### Logic

`ActiveConversationPort` (cit:(["class ActiveConversationPort"], mcp/src/agents_remember/serving/ports.py:62-62)) and `ConversationLibraryPort`
(cit:(["class ConversationLibraryPort"], mcp/src/agents_remember/serving/ports.py:94-94)) are the two read protocols; `ControlSessionLike`
(cit:(["class ControlSessionLike"], mcp/src/agents_remember/serving/ports.py:122-122)), `TerminalCatalogPort` (cit:(["class TerminalCatalogPort"], mcp/src/agents_remember/serving/ports.py:135-135)), and
`ControlPlanePort` (cit:(["class ControlPlanePort"], mcp/src/agents_remember/serving/ports.py:189-189)) expose the control/terminal seams. The canonical
definitions live here so serving modules can import them without triggering the conversation
package's route composition; `__all__` (cit:([`__all__`], mcp/src/agents_remember/serving/ports.py:272-278)) curates the surface.

### Invariants And Boundaries

- Exactly two read ports separate active exact-session reads from dormant native library reads;
  lifecycle/control authority is explicitly not a third read store port.
- Conversation modules must consume these ports rather than re-importing the moved
  harness-control/terminal-catalog modules (layering rail + conversation foundation tests).

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
| The conversation package re-exports the canonical definitions. | `__all__` | mcp/src/agents_remember/serving/conversation/ports.py:17-22 |
| The foundation suite pins the exact two-port topology. | `test_exactly_two_conversation_ports_exist` | mcp/tests/test_conversation_foundation.py:24-36 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260821-CLIVE Retention Port Contract

`TerminalCatalogPort.compact` accepts the exact set of task-registered execution ids. The port keeps
registration proof explicit at the deletion boundary; it does not grant the catalog a task reader
or permit unregistered worker/reviewer/curator rows to be reclaimed.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: extended the catalog port with explicit registered execution ids. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `ports.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the canonical port surface added
  by the backwards-edge removal. Verification metadata pinned until closeout stamps the L9 code
  commit.
