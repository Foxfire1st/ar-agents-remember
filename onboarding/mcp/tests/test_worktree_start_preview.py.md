# mcp/tests/test_worktree_start_preview.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Registered public operation proofs for exact planned-parent preview, no startup-state materialization, truthful journal/ref facts and unchanged durable apply — plus the proof that the removed opt-out mode never previews.

## Code Commentary

The confined fixtures use real temporary code/external-memory repositories and the registered MCP/application/start/bootstrap path. `PreviewFixture` builds every world external-memory; repeated first-leaf preview is parametrized by commanded versus uncommanded parentage, not removed memory modes. Repeated previews materialize no startup contract, activation, ref, worktree or provider state, reserve nothing, and preserve repository refs, worktree lists and real index bytes. The whole-root comparison includes the transcript root inside coordination; harness receipts remain beside the observed root.

`test_disabled_start_is_refused_before_any_publication` separately checks that preview and actual requests naming `memory_mode="disabled"` return `memory-opt-out-refused` before any startup branch, worktree, contract or task binding is published. Both refused calls still record a daily line, any named detail and a completed-call river event. After each call, the same strict comparator checks those records cumulatively and preserves all other product/Git state; the typed refusal and no-parent-publication assertions remain separate. This is not global byte equality or a successful apply proof.

A registered preview is still a tool call. The proof admits and checks its UTC call-day tool-log lines and any detail files named by those new lines, plus the completed-call event in the workspace river. Earlier log/event bytes remain a prefix, tool identities and counts account for the calls, and previously written detail files remain unchanged. A call that raises has a log line but no completed-call river event. Daily path admission is bounded by the inclusive capture-day interval, including a midnight crossing; a stale-day record-shaped path is not admitted. New record paths must have the expected file/directory kind.

Only the modification time of an admitted record directory may move, and only when an admitted new direct child explains the entry creation. Every other observed path keeps its kind, mode, modification time and content. The fixture pre-creates the transcript root and empty workspace river lockfile as layout; the lockfile is not part of the call record. The shared comparator is [preview_read_only_test_support.py](preview_read_only_test_support.py.md), not a second production logging implementation.

The existing partial-bootstrap case drives one genuine journal before and after its original helper creates the exact memory ref. Preview reports `would-create` only in the first state, `existing` in the second, and actual apply recovers that same journal to durable source/parent/active authority. No manual parent/ref or replacement journal supplies the proof.

Default/durable rejection, foreign/unreadable parent, invalid leaf/source/base/ref, changed current source after preview and organizational direct-super remain separate operations. A fresh session preserves startup/Git state while checking its call records; it is not universal zero-I/O. A real start adopts the session's task lifecycle; a second leaf request in that session is
refused as `lifecycle-switch-required`, not made admissible by the removed `switch_lifecycle`
tool. The persisted-parent read-only preview therefore restarts the session and checks its
workspace-river records. The separate observer metadata case uses a real start and the second
request's refusal, verifies that its lifecycle event file changed, admits the unchanged kind/mode
first, and then deliberately changes mode to prove the guard fails. It is not the removed
helper's full ambient byte-prefix/tool-identity proof. Missing original discovery observer bytes remain missing, not reconstructed. These fixtures do not resume or accept the original L41 evidence.

Distinct negative cases reject a stray file beside the line file, a rewritten earlier log line, an unnamed detail file, a rewritten earlier river event, stale-day line/detail paths, a directory touch without an admitted entry and a lifecycle event mode change. These are assertion contracts, not a claim that the suite ran or that logging retention and budget-loss behavior are globally append-only.

## Evidence

No Domain Documentation source is configured in system/sources.md. These are current source/assertion anchors; the approved requirement and bound public receipts remain task artifacts.


- Fixture world is always external-memory. [7]
- First-leaf preview repeats without startup publication while checking its call records, commanded or not. [8]
- Typed disabled-mode preview and actual requests preserve refusal identity and no parent publication while checking their daily line/detail and river records cumulatively. [9]
- Partial-bootstrap preview and actual apply use the same journal. [10]
- The observer exception preserves kind and mode before allowing an append. [11]

- Negative cases reject writes and metadata changes beyond the checked record. [12]

- Losing the handoff fails and preview cannot supply durable authority. [13]
- Persisted artifact errors never select a synthetic valid parent. [14]
- Same journal/ref states and real apply/recovery remain truthful. [15]


- After a real start adopts the lifecycle, the second-leaf refusal changes its event file; unchanged kind/mode passes and deliberately changed mode fails the guard. [16]


- Actual apply re-resolves current source; fresh-session persisted-parent preview preserves startup/Git state and checks its call records. [17]
