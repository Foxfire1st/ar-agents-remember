# skills/l-01-agent-lifecycles/reference/curator/memory-handover.md

## Governing Overview

[overview](../../overview.md)

## Purpose

The Curator's rules for sending a memory candidate for review or returning a memory repair: which trees the Reviewer compares, what each handover names, and who receives it.

## Code Commentary

The Reviewer compares the leaf's base and candidate in Git (the code trees and the knowledge files of both memory trees), so the Curator records no separate comparison. Each handover names the leaf, the Worker's exact code head and change hash, the memory candidate's identity, the report or verdict path and the whole next stretch requested. The memory lane's separate reports, finding identifiers, pass count, code-state isolation and recorded extra-pass approval are not restated here: the file sends the reader to the review operation's boundaries section before sending a candidate. Memory findings or a passing verdict come directly from the Reviewer and are repaired within that lane; the Manager relays none of these handovers.

## Evidence

- The Reviewer compares base and candidate trees in Git; the Curator records no comparison. [1]
- Each handover names the leaf, code head, change hash, memory candidate, report path and whole next stretch, and the memory-lane rules come from the review operation's boundaries. [2]
- Findings and verdicts travel directly between Reviewer and Curator, without a Manager relay. [3]
- The review operation's boundaries hold the memory lane's separate reports, identifiers and pass count. [4]
