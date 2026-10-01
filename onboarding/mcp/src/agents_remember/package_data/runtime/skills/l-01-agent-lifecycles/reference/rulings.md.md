# reference/rulings.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Reference-only index of the durable rulings the corpus obeys — each row recording the ruling, its date or
anchor, what it decides, and what it superseded. It is normative in exactly one direction: a seat follows
the rule where it is authored, and this file is where the reason and the **supersession** are recorded.

## Code Commentary

### Logic

`## The ruling index` collects the standing rulings that shape the corpus — lifecycle-and-job are one
entity; no per-harness role files; the designer is an inline architect hat; the strategist is spawn-first;
the developer owns the loop by talking to one architect; the reviewer is also every requested loop's
reviewer seat; the two adversarial seams; the strategist pass is proposed and never auto-run; free chat is
a launcher, not a role seat; the spool-up chain is fixed and self-driving; no seat-local watchers; review
independence and evidence-type matching; orchestration seats use no native sub-agents; a candidate change
cannot reopen acceptance; optional review stays optional; Git transactions do not re-acquire a tracked
ledger leg; and the computed ledger cache is preserved.

Because each row records **what it supersedes**, this file is what stops a retired rule from being
reintroduced: the corpus's stated position is that frequency of repetition is never authority, and these
citations are.

### Conventions

Add a row when a durable ruling changes what the corpus obeys, and record the superseded rule in the same row; never rewrite history here.

### Invariants And Boundaries

- A ruling recorded here is followed where it is authored, not in this file.
- Supersession is explicit: the row that replaces a rule names what it replaced.
- Repetition is never authority; the citation is.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

No relevant documentation found after checking live sources.

### Repo-Internal References

| The reference layer is declared non-injected, so it stays out of the normative path. | `"injected": false` | skills/l-01-agent-lifecycles/composition-manifest.json:1-1; skills/l-01-agent-lifecycles/composition-manifest.json:25-25; skills/l-01-agent-lifecycles/composition-manifest.json:525-525; skills/l-01-agent-lifecycles/composition-manifest.json:530-530; skills/l-01-agent-lifecycles/composition-manifest.json:535-535; skills/l-01-agent-lifecycles/composition-manifest.json:540-540; skills/l-01-agent-lifecycles/composition-manifest.json:545-545 |
| The ruling index and its supersession column. | `## The ruling index` | skills/l-01-agent-lifecycles/reference/rulings.md:8-30 |
| The router's registry reflects the nine-role ruling this file indexes. | `## The Role Registry` | skills/l-01-agent-lifecycles/SKILL.md:67-86 |

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.
