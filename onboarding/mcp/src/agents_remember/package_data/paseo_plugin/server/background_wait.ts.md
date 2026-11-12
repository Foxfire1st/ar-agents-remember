# mcp/src/agents_remember/package_data/paseo_plugin/server/background_wait.ts

## Governing Overview

[Native Paseo plugin](../overview.md)

## Purpose

The text and naming of the declared background wait: how a seat says that a process it started still runs, how long the plugin waits before it checks, and the words of the check and of the seat message sentences that teach both declarations. It holds no state, timer or gate; those stay with the turn-end decision.

## Code Commentary

A seat declares the wait with a line of its last assistant message that starts `WAITING FOR BACKGROUND:` behind leading spaces, Markdown markers or quoting marks; the comparison is case-sensitive, and the helper wait's keyword is read by the same `textDeclares`. Any seat may declare either wait, whatever its provider. `readBackgroundDeclaration` takes the first declaring line, quotes what follows the keyword (at most 300 characters) and reads `check in <N> minutes` from that line or the lines after it: no value gives three minutes, and a value outside 1 to 30 is clamped. `backgroundDeclaredReason` writes the declared row's reason: the time used, whether it was the default, the named value or a clamped one, and, when a helper wait declared in the same end brings the one check earlier, that it does.

A check covers the helper wait, the background wait or both (`waitCheckKind`), and its rows are named `<wait>-wait-<event>`. `composeBackgroundWaitCheck` names the seat as the seat message does, quotes the declaration, asks for each process's state and, when helpers were declared too, for each helper's progress, and says how to declare again; the plugin recognises its two background first lines as its own message. `PublishedDeclaredWait` is the shape the host-activity record carries for an open wait: what it waits for, since when, the next check while one is armed, and the declaration's words.

## Relationships

`turn_ended.ts` calls these functions and owns the tracker, the timers and the gates; `declared_wait_state.ts` keeps the open declaration and writes its rows; `host_activity.ts` publishes `PublishedDeclaredWait` and compares it by `declaredWaitSignature`. `background_wait.test.ts` exercises the wait through the decision with a fake clock.

## Evidence

- The declaration keyword and the check's own first lines are fixed strings. [1]
- The check waits three minutes by default, and a named value is kept within 1 to 30 minutes. [2]
- A seat not on ACP is told about the helper declaration, and every seat about the background declaration. [3]
- A keyword counts only at the start of a line, behind the allowed markers. [4]
- The declaration is read from its line, quoted up to 300 characters, and its check time is clamped. [5]
- The declared row names the time used and where it came from. [6]
- The published wait carries what it waits for, since when, the due check and the declaration's words. [7]
- One check kind covers the waits one end declared. [8]
- The background check quotes the declaration and asks for each process's state, and for helpers too when both were declared. [9]
