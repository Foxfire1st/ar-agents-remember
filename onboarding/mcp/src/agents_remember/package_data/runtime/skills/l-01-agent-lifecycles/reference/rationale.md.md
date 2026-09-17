# reference/rationale.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/reference/rationale.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T18:19+02:00 |
| lastVerifiedCommitHash | `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` |
| lastVerifiedCommitDate | 2026-09-17T10:09:37+02:00|
| governingOverview      | `../../../../../../../overview.md` |

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
scoped to one kind of work goes to `../operations/`, and rationale/history/superseded rulings live here.
Its separation table's operations row reads **"nine blocks"**, and that count is current rather than
aspirational: the row was corrected from "eight" as part of the same change that added the ninth
operation, so the table and the corpus agree.

It also states the consolidation rule that produced the corpus: **frequency of repetition is never
authority** — a stale imperative does not become canonical because it appears in nine files — and it
records that each existing obligation was given an explicit old anchor, a disposition, and a new anchor
in a migration map that belongs to the task that produced it rather than to the shipped corpus, because
it describes the corpus's own history. **The "nine files" figure is not a registry claim and must not be
read as one:** it counts the files a past consolidation touched while stating why repetition is not
authority, it belongs to that historical narrative, and it was deliberately left as written. It is not
an operation count, not a role count, and it has no bearing on the ten-role registry below it.

`## Why the launcher is not a tenth role` is the heading the corpus's arithmetic makes worth reading
carefully, and the section now answers that arithmetic directly rather than leaving it to the reader.
Two facts are stated as separate: the **launcher** is a routing condition and not a role at all —
authoring its obligations in `../core/launcher.md` keeps `roles/` enumerable as seats only, so it never
becomes a registry member under any count — while the registry **does** hold ten roles, and the tenth is
`bootstrap`, the new user's first-hour **free agent**, reached by a session-open call with its role and
no task document rather than by dispatch. The heading is **kept deliberately**, because it remains true
of the launcher; the paragraph beneath it is what separates that fact from the count. The card records
no residual here: a reader who arrives believing "tenth role" means the launcher is corrected inside the
section that raised the question.

**The file is reference-only in the strict, checkable sense, and this is why an edit here cannot move a
compiled capsule.** `composition-manifest.json` declares `references.rationale` with
`"injected": false`; the manifest's `composition_order` and the compiler's frozen
`CAPSULE_COMPOSITION_ORDER` are both `core → role → operation → (repository-)specialization`, with no
reference plane in either; and no `roles.<role>` entry names this file among its sources. A `reference/`
edit therefore changes provenance prose and nothing else: no `semantic_digest`, no rendered capsule
text, and no production module digest moves because of it.

### Conventions

Rationale is not injected; a seat mid-task follows the rule where it is authored and reads this file only to understand why. Because the file sits outside every composition root, editing it is a provenance act rather than an instruction change — and the corpus's own propagation rule still applies: edit the canonical `skills/` copy and let `scripts/sync-skills.py` carry it to the nine generated trees.

### Invariants And Boundaries

- Nothing here is normative: the obligations live in `core/`, `roles/`, and `operations/`.
- The migration map stays in the task tree; this file must not become a second copy of it.
- Repetition is never authority; each rule has exactly one source.
- **The file cannot affect a capsule.** With `references.rationale` at `"injected": false`, no reference
  plane in `CAPSULE_COMPOSITION_ORDER`, and no role naming it as a source, a change here must not be
  credited with — or blamed for — any `semantic_digest`, rendered-text or module-digest movement.

### Todos

None recorded.

## Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

The migration map this file deliberately does not copy belongs to the task that produced the corpus
(`260915-CAPS-L1`, `notes/reports/caps-l1-obligation-map.md` under the coordination tasks tree) and has
no repository-relative path, so it is recorded here in prose rather than as a citation row.

| Finding | Anchor | Source |
| --- | --- | --- |
| The reference layer is declared non-injected, so it stays out of the normative path. | "injected"; "rationale" | skills/l-01-agent-lifecycles/composition-manifest.json:503-509 |
| The assembly order with no reference plane in it, which is the manifest half of the cannot-affect-a-capsule property. | "composition_order" | skills/l-01-agent-lifecycles/composition-manifest.json:530-535 |
| The compiler's frozen side of the same property. | `CAPSULE_COMPOSITION_ORDER` | mcp/src/agents_remember/models/role_capsules/vocabulary.py:113-118 |
| The four-way separation, including the operations row's current "nine blocks". | `## Why the corpus is shaped this way`; "nine blocks" | skills/l-01-agent-lifecycles/reference/rationale.md:8-25; skills/l-01-agent-lifecycles/reference/rationale.md:18-18 |
| The never-authority rule, read as the historical narrative it belongs to rather than as a registry count. | "frequency of repetition is never authority"; "nine files" | skills/l-01-agent-lifecycles/reference/rationale.md:21-25; skills/l-01-agent-lifecycles/reference/rationale.md:22-22 |
| The launcher-is-not-a-registry-member argument, and the heading the tenth role makes worth reading carefully. | `## Why the launcher is not a tenth role` | skills/l-01-agent-lifecycles/reference/rationale.md:48-53 |
| The paragraph that separates the count from the distinction: ten roles, the launcher not among them, and `bootstrap` the free agent reached by a session-open call rather than by dispatch. | "The registry holds **ten** roles, and the launcher is not one of them." | skills/l-01-agent-lifecycles/reference/rationale.md:55-59 |
| The tenth registry member, so a reader does not read "tenth role" as the launcher. | "**Inherits:**" | skills/l-01-agent-lifecycles/roles/bootstrap.md:12-13 |
| The generated copies are proved current by the generator's own read-only check rather than by hand-editing. | `CANONICAL_SKILLS`; `check_targets` | scripts/sync-skills.py:15-15; scripts/sync-skills.py:179-191 |

## Cross-Repo References

No sibling-repository contract defines this instruction file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T12:55+02:00 — 260915-CAPS-L14 curator: **D3 dead governing-overview link repaired.** This card's `governingOverview` was one directory level short, so it resolved to a path that does not exist instead of the `mcp/` route overview. The card directory sits seven levels below `onboarding/`, so seven `../` steps reach `onboarding/` and the correct target is `../../../../../../../overview.md` (→ `onboarding/mcp/overview.md`). Reversed here: `../../../../../overview.md` (which resolved to the nonexistent `mcp/src/agents_remember/overview.md`) or `../../../../../../overview.md` (→ the nonexistent `mcp/src/overview.md`) → **`../../../../../../../overview.md`**. The body's own `[mcp/overview.md](…)` link was re-pointed with it. No prose, anchor, range or verification stamp was otherwise changed.

- 2026-09-16T18:19+02:00 — 260915-CAPS-L13 curator: **refreshed against the A6 source, which corrected the two things this card had recorded as source defects.** The card and the source now agree, and the three parts of the split are stated for what each is:
  1. **The separation table's operations row now reads "nine blocks" in the source** (it read "eight"), so the previous entry's claim that the table "still reads eight blocks" is no longer true and has been replaced: the card now describes the correction that was made and notes that the row and the corpus agree. This was the one false statement in the card, and it was false only because the source caught up with it.
  2. **The launcher section now accounts for the tenth role.** A6 kept the heading — deliberately, because it remains true of the launcher — and added a paragraph stating that the registry holds ten roles, that the launcher is not one of them, and that the tenth is `bootstrap`, the first-hour free agent reached by a session-open call with its role and no task document rather than by dispatch. **I judge this sufficient and record no residual:** the fact that made the heading dangerous is now answered inside the section that raised it, so a reader who arrives thinking "tenth role" means the launcher is corrected in place. The card says so rather than hedging.
  3. **The never-authority rule's "nine files" was deliberately left alone and is not a registry claim.** The card now says that explicitly — it counts files a past consolidation touched while arguing that repetition is not authority, belongs to that historical narrative, and is not an operation count, a role count, or connected to the registry below it — so no reader can mistake it for a count or expect it to move.
  Added the **cannot-affect-a-capsule** property as a verified, checkable fact rather than an assurance, because A6 had zero capsule effect and the card is where that is explained: `references.rationale` is `"injected": false`, neither the manifest's `composition_order` nor the compiler's frozen `CAPSULE_COMPOSITION_ORDER` contains a reference plane, and no `roles.<role>` entry names this file among its sources — so an edit here moves provenance prose only, never a `semantic_digest`, rendered capsule text, or production module digest. Added three reference rows for that property (the manifest block, the manifest order, the frozen order) and one for the new tenth-role paragraph, and re-derived every range against the source's new 91-line shape (the separation row was `:8-26` and is now `:8-25`; the launcher row was `:48-54` and is now `:48-53`, with the new paragraph at `:55-59`). Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit.
- 2026-09-16T17:59+02:00 — 260915-CAPS-L13 curator: **body corrected for the tenth role** (`CAPS-R13@v1`).
  `## Why the launcher is not a tenth role` is now arithmetic a reader can get wrong, because the
  corpus does have a tenth role and it is `bootstrap`, not the launcher: the card states that
  distinction and preserves the file's actual argument (the launcher is a routing condition outside the
  registry under any count). The separation table's "eight blocks" and the never-authority rule's "nine
  files" are now attributed as the source's own L1-era statements, with the current nine-operation and
  ten-role counts named beside them rather than silently overwriting the quotation. **The Repo-Internal
  and Cross-Repo sections had lost their `| Finding | Anchor | Source |` header rows**, so their rows
  rendered as prose; both are restored, the manifest row's `:1-1` citation was repaired to the
  `references` block it names, and the two section ranges were re-derived against the 85-line file.
  Verification metadata is left at the leaf base commit because the source is uncommitted — the
  governed closeout stamps the real code commit.

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: Repaired citations this leaf falsified: the canonical lifecycle corpus was consolidated (the router shrank 620 → 179 lines; all nine role files and several templates were rewritten), so the cited anchors and ranges no longer resolved. No behavioral claim changed — the cited rule was re-pointed at its current home. Verification metadata remains closeout-owned. The migration-map row no longer emits a repository-relative path for a coordination-tree artifact, which would not resolve from this memory root.


- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: created this card for `skills/l-01-agent-lifecycles/reference/rationale.md` — a file added by the role-instruction corpus consolidation. The canonical source is a reference-only rationale file separated from the normative path by the consolidation.; the packaged copy is produced by `scripts/sync-skills.py` and is not hand-edited. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
