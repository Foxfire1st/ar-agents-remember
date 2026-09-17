# reference/rulings.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/reference/rulings.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T22:19+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview      | `../../../../../../../overview.md` |

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

## Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| The reference layer is declared non-injected, so it stays out of the normative path. | `"injected": false` | skills/l-01-agent-lifecycles/composition-manifest.json:1-1 |
| The ruling index and its supersession column. | `## The ruling index` | skills/l-01-agent-lifecycles/reference/rulings.md:8-30 |
| The router's registry reflects the nine-role ruling this file indexes. | `## The Role Registry` | skills/l-01-agent-lifecycles/SKILL.md:67-86 |

## Cross-Repo References

No sibling-repository contract defines this instruction file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-16T22:19+02:00 — **No content impact:** 260915-CAPS-L16 curator. The canonical source's
  LOCR-1 migration-map row gained a sentence break (the anchor cell now ends `…*Completion Truth And
  Handoff Acceptance*.`) — punctuation in a historical anchor name, taken to break a detector's
  reverse-window adjacency, with the anchor's identity and every ruling it carries unchanged. This
  card's Logic enumerates the standing ruling index and the supersession rule, which that row does not
  alter, so nothing in the body asserts the sentence that moved; reviewed and deliberately left as
  written. The one-home fact the row names (`core/acceptance.md` owns the boundary) is unchanged and
  remains the reason the pre-consolidation `SKILL.md` section is not restored. **Repaired in the same
  pass (D16):** this card's `governingOverview` field and link pointed five levels up, at
  `onboarding/mcp/src/agents_remember/overview.md`, which does not exist — the card's own link text says
  "MCP package overview", which from `reference/` is **seven** levels up. Both now resolve to
  `onboarding/mcp/overview.md`. Verification metadata moves to this leaf's synced base `8997e184`; the
  candidate is deliberately uncommitted, so the governed closeout stamps the real code commit and no
  hash or fingerprint was invented here.

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: created this card for `skills/l-01-agent-lifecycles/reference/rulings.md` — a file added by the role-instruction corpus consolidation. The canonical source is a reference-only index of the durable rulings the corpus implements, with their supersessions.; the packaged copy is produced by `scripts/sync-skills.py` and is not hand-edited. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
