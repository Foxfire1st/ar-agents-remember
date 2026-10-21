# mcp/tests/test_role_first_message.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The lasting proof that every role AR can start receives a sane first message: the projection only, within its recorded budget, nothing said twice, and every hand-over name it carries reachable — across every harness and every kind of start the code admits.

## Code Commentary

FirstMessageMatrixTests derives its combinations from the code's own tables rather than a list in the test, so a role, harness or start kind added to the product is covered without editing the matrix. check_paths asserts that every absolute path the sent message emits exists at the moment the host is handed that message, and treats a missing send snapshot as a failure rather than a clean read. _missing_paths is the single predicate for which emitted paths must exist and which are exempt, so the send-time observer and the later checks cannot drift apart. _emitted_paths reads the paths out of the message itself, which is why a path containing a space is read whole instead of being cut at the space.

## Evidence

- The matrix derives every combination from the code and checks each built message. [1]
- Which emitted paths must exist is decided by one predicate. [2]
- The path check reads a whitespace-containing path whole and runs at send. [3]
- The paths are read out of the message that was actually sent. [4]
