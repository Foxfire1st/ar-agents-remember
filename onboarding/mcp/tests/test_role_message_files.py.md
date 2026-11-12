# mcp/tests/test_role_message_files.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers the shape a message between agents takes: the wake text is bounded by the configured limit and
the whole text is a file that the text names. It also holds the filesystem transaction around a message
— copies, workspace links, collisions and rollback — and the registered tool's refusals.

## Code Commentary

### Logic

`_sha()` computes the digest the stored file reports, `_FailingWriter`/`_fail_writes_after()` make a
write-mode binary fail after a number of writes so a partial copy can be observed, and the cases use
`paseo_role_tools_test_support` plus `_user_settings_guard` for the settings tree.

- **The limit.** `MessageLimitTests` delivers a text of exactly the limit and refuses one character more,
  falls back to 1000 when the settings name no number, applies a changed number on the next call without a
  restart, and refuses a settings number that is not a positive whole number at load.
- **The file.** `MessageFileTests` checks that the stored file holds the head, the message and the body
  while the delivered text names the file, that a 200 000-character body is written whole, that a message
  with neither head nor body gets no added line but keeps its file, and that two messages in one second
  get a counter.
- **Attachments.** An `attach` inside the record is named and not copied; one outside is copied and the
  copy named; a missing attachment is refused and nothing is written.
- **Folders and links.** The folder is the narrowest task both agents share; a leaf workspace gets its
  messages link at creation, a first inbound message links the recipient's workspace, an occupied
  recipient path is preserved with a warning, and sender-first and recipient-first converge on the leaf
  folder.
- **Retention.** A refused delivery keeps its first file when the sender sends again, and a wait reply
  longer than the limit comes back whole with its `textTruncated` flag set, its file and digest named.
- **Transaction.** `TransactionTests` removes a partial target after a failed copy, removes completed
  copies when a later store fails, and names a folder-creation failure.
- **Cost.** `CollisionCostTests` writes once per message across a same-second batch and keeps every
  payload when same-stem stores run concurrently.
- **Refusals through the tool.** `RegisteredRefusalTests` drives the limit and the archived-successor
  answer through the registered tool rather than the function alone.

### Conventions

Cases count writes, syncs, links and scans where cost matters, and read the stored bytes rather than the
returned text alone.

### Invariants And Boundaries

- The wake text is bounded; the payload is the file, written whole.
- A failed preparation leaves no message-owned residue behind.

## Evidence


- Boundary settings and reload assertions separate the bounded wake text from the file payload. [1]


- Message fixtures inspect stored payloads, pointers, reply files and workspace links. [2]

- Faults and collisions exercise rollback and retained concurrent payloads. [3]

- Successor guidance and strict refusal fields stay separate from automatic retargeting. [4]


- The composed fixtures pin retained refusal files on a non-holdable unresumable session and archive the old holder before successor fixtures. [5]



- The former fifty-character wait-reply truncation control is retired with that subject. Reply-file content and bound/refusal assertions remain; current source retains the full reply instead of claiming the old lower cut is still enforced — mcp/tests/test_role_message_files.py. [6]
