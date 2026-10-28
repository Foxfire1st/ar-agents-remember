# `server/subagent_wait.test.ts`

## Governing Overview

[Plugin overview](../overview.md)

The package test for the declared helper wait: the declaration, the three-minute check, and both
ways a wait ends.

## What it pins

- The module declares eighteen test cases for the helper-wait contract; declarations and assertions do not establish an invocation or pass. [1]

The source cases cover:

- a declared ACP seat that stays idle is asked for progress **at** three minutes and not before;
- a seat that answers every check and declares again is asked again and is never sent the
  no-hand-off message;
- a check that falls due inside a running turn waits for the turn, and a declaring end arms a
  fresh one;
- a check due while the host still shows the seat in a turn is skipped and not sent;
- a limited declared seat gets the check's text with the reset sentence, not the no-hand-off
  message;
- a check due in a permission wait, or with an unreadable host state, is re-armed for three
  minutes;
- a turn opened by the check does not reset the silent-end run, and a declared end neither counts
  nor resets it;
- a declared end without a hand-off gives the parent nothing.

- a task step plus declaration remains a wait, while a sibling hand-off keeps the parent’s hand-off line;
- a Worker that stops declaring receives the ACP seat message naming the declaration;
- an ACP Worker’s delegate_task call without a declaration arms only the ordinary sixty-second wake;
- an Investigator’s declaration gets checks, and its silent end keeps its existing parent-line behavior;
- only the last assistant message decides, with the exact keyword at a line start behind supported markers; lowercase and mid-line text do not declare;
- a non-ACP seat keeps the ordinary wake behavior;
- the plugin distinguishes its own progress check from an external message;
- archiving ends the declared wait and cancels its check;
- shedding a limited check at the deferred-fleet cap writes one check-skipped row and arms no resume;
- a declaring end already reported archived ends its earlier wait and arms nothing.

Together they hold the two ends of the feature that matter in production: that waiting is not
silence, and that a declared end is not a hand-off.

## Frame

The clock is driven, not waited on, so the three-minute boundary is asserted exactly rather than
approximately. The row kinds these paths write are covered in `server/turn_ended.ts`; the
provider verdict that decides who may declare at all is covered by `server/acp_providers.test.ts`.
