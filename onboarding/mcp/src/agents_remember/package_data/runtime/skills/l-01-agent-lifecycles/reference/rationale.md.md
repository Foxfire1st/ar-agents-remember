# reference/rationale.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

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

## Evidence

### Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

No relevant documentation found after checking live sources.

### Repo-Internal References

The migration map this file deliberately does not copy belongs to the task that produced the corpus
(`260915-CAPS-L1`, `notes/reports/caps-l1-obligation-map.md` under the coordination tasks tree) and has
no repository-relative path, so it is recorded here in prose rather than as a citation row.

- The reference layer is declared non-injected, so it stays out of the normative path. [1]
- The assembly order with no reference plane in it, which is the manifest half of the cannot-affect-a-capsule property. [2]
- The compiler's frozen side of the same property. [3]
- The four-way separation, including the operations row's current "nine blocks". [4]
- The never-authority rule, read as the historical narrative it belongs to rather than as a registry count. [5]
- The launcher-is-not-a-registry-member argument, and the heading the tenth role makes worth reading carefully. [6]
- The paragraph that separates the count from the distinction: ten roles, the launcher not among them, and `bootstrap` the free agent reached by a session-open call rather than by dispatch. [7]
- The tenth registry member, so a reader does not read "tenth role" as the launcher. [8]
- The generated copies are proved current by the generator's own read-only check rather than by hand-editing. [9]

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.
