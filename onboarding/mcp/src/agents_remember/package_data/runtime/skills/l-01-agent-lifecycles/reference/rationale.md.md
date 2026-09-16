# reference/rationale.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/reference/rationale.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `3054af87fdf0e21e9ec7132a5d62ba0d514600ba` |
| lastVerifiedCommitDate | 2026-09-16T08:23:52+02:00|
| governingOverview      | `../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../overview.md)

## Purpose

Reference-only rationale, provenance, and credits for the instruction corpus — kept out of the
normative path so that *why* a rule reads the way it does stays available without competing with
obligations for a seat's attention. Nothing in this file is injected into a capsule.

## Code Commentary

### Logic

The file opens by stating its own status: reference-only, with the normative sources named as
`../SKILL.md`, `../core/`, `../roles/`, and `../operations/`. `## Why the corpus is shaped this way`
records the problem and the four-way separation it produced — rules that genuinely apply across roles go
to `../core/` authored once, seat-specific rules stay self-contained in `../roles/<role>.md`, procedure
scoped to one kind of work goes to `../operations/` as eight blocks, and rationale/history/superseded
rulings live here.

It also states the consolidation rule that produced the corpus: **frequency of repetition is never
authority** — a stale imperative does not become canonical because it appears in nine files — and it
records that each existing obligation was given an explicit old anchor, a disposition, and a new anchor
in a migration map that belongs to the task that produced it rather than to the shipped corpus, because
it describes the corpus's own history.

### Conventions

Rationale is not injected; a seat mid-task follows the rule where it is authored and reads this file only to understand why.

### Invariants And Boundaries

- Nothing here is normative: the obligations live in `core/`, `roles/`, and `operations/`.
- The migration map stays in the task tree; this file must not become a second copy of it.
- Repetition is never authority; each rule has exactly one source.

### Todos

None recorded.

## Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| The reference layer is declared non-injected, so it stays out of the normative path. | `"injected": false` | skills/l-01-agent-lifecycles/composition-manifest.json:1-1 |
| The four-way separation and the never-authority rule. | `## Why the corpus is shaped this way` | skills/l-01-agent-lifecycles/reference/rationale.md:6-24 |
| The task-local migration map this file deliberately does not copy. It lives in the coordination tree, not in this repository, so no repository-relative path is cited. | `caps-l1-obligation-map.md` (`ar-coordination/tasks/agents-remember/260915_role-capsules-and-native-eve/notes/reports/`) | (coordination tree — not a repository path) |

## Cross-Repo References

No sibling-repository contract defines this instruction file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: Repaired citations this leaf falsified: the canonical lifecycle corpus was consolidated (the router shrank 620 → 179 lines; all nine role files and several templates were rewritten), so the cited anchors and ranges no longer resolved. No behavioral claim changed — the cited rule was re-pointed at its current home. Verification metadata remains closeout-owned. The migration-map row no longer emits a repository-relative path for a coordination-tree artifact, which would not resolve from this memory root.


- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: created this card for `skills/l-01-agent-lifecycles/reference/rationale.md` — a file added by the role-instruction corpus consolidation. The canonical source is a reference-only rationale file separated from the normative path by the consolidation.; the packaged copy is produced by `scripts/sync-skills.py` and is not hand-edited. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
