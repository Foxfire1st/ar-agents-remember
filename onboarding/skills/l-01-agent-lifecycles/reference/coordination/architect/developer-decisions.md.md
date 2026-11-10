# skills/l-01-agent-lifecycles/reference/coordination/architect/developer-decisions.md

## Governing Overview

[overview](../../../overview.md)

## Purpose

The Architect's rules for relaying a developer decision from the question through delivery of the resulting instruction. It grants no additional authority.

## Code Commentary

The Architect does the work it can first, then asks the developer in plain words in its own chat and ends the turn, so his answer starts the next one; a blocking question tool is used only when no agent waits on the Architect. While a point is under discussion, agents receive nothing on it; once settled, one consolidated instruction names the earlier messages it replaces. A design change reaches the coordinating agent or a requirement only on the developer's explicit word to send it. A ruling about role instructions names the exact packet or role file, heading and superseded sentence, and its delivery follows the instruction-change section of `coordination/shared/child-questions.md`; measurement-loop changes follow `curator-measurement.md`'s no-ruling-record rule.

## Evidence

- Ask without blocking agents, consolidate settled instructions, and send a design change only on the developer's word. [1]
- Instruction rulings name their exact target and hand delivery to the child-questions and measurement files. [2]
- The Architect role points here before relaying a developer decision. [3]
