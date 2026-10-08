# mcp/tests/conversation_open_test_support.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Launch, capability, resume-target and catalog doubles for the conversation open-service tests. The real service remains under test; these doubles replace its external launch and history seams.

## Code Commentary

`_Host`, `_Gates`, `_Port`, `_CodexKindPort`, `_Opener` and `_DedupeOpener` preserve the service scenarios' exact identities, refusal shapes and live-row absorption. `_BlockingPort` signals that native resolve was entered before parking on the caller's gate. The pre-launch negative assertion follows that signal, and release remains the test's own action. Neither the doubles nor their fixed evidence values qualify a live harness.

## Evidence

No Domain Documentation source is configured; the references below establish repository-owned fixture and assertion behavior.

- Resolve entry is observed before the launch gate is released. [1]
- Capability and resume-target doubles retain their identities and refusal arms. [2]
- The opener creates the catalog row; replay absorbs an existing live row. [3]
