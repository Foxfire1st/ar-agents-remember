# mcp/src/agents_remember/serving/ports.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/serving/ports.py`                    |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-08T14:38+02:00                                       |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                   |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

`ActiveConversationPort` (cit:(["class ActiveConversationPort"], mcp/src/agents_remember/serving/ports.py:61-61)) and `ConversationLibraryPort`
(cit:(["class ConversationLibraryPort"], mcp/src/agents_remember/serving/ports.py:93-93)) are the two read protocols; `ControlSessionLike`
(cit:(["class ControlSessionLike"], mcp/src/agents_remember/serving/ports.py:121-121)), `TerminalCatalogPort` (cit:(["class TerminalCatalogPort"], mcp/src/agents_remember/serving/ports.py:134-134)), and
`ControlPlanePort` (cit:(["class ControlPlanePort"], mcp/src/agents_remember/serving/ports.py:186-186)) expose the control/terminal seams. The canonical
definitions live here so serving modules can import them without triggering the conversation
package's route composition; `__all__` (cit:([`__all__`], mcp/src/agents_remember/serving/ports.py:269-269)) curates the surface.

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

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the canonical port surface added
  by the backwards-edge removal. Verification metadata pinned until closeout stamps the L9 code
  commit.
