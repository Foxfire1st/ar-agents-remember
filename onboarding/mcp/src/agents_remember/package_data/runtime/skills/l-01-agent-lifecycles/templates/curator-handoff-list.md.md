# mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T17:09+02:00 |
| lastVerifiedCommitHash | `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80` |
| lastVerifiedCommitDate | 2026-09-20T02:00:33+02:00|
| governingOverview | `mcp/overview.md` |

## Governing Overview

[mcp route overview](../../../../../../../overview.md)

## Purpose

The **packaged, generated mirror** of the curator hand-off list template: the copy of
`skills/l-01-agent-lifecycles/templates/curator-handoff-list.md` that ships inside the
`agents_remember` package's runtime data and is served to clients as part of the shipped skills
tree. Its content is the producer's output shape for the requirement-shaped items a leaf's builder,
reviewer and orchestrator hand to the curator — thirteen fields split nine producer to four curator,
two rules (co-resolution and no-paraphrase) and the honest encodings for rulings with no placement.

**This copy is byte-identical to the canonical source.** `diff` between
`skills/l-01-agent-lifecycles/templates/curator-handoff-list.md` and this file is empty, both files
are 230 lines, their MD5 digests are both `6ab039ac49385760f44a3a50347a8de0`, and both were last
touched by the same commit — `7e6936c0d3b87f2fa0f462c5c63d6d86441ef10b` — which is what the shared
`lastVerifiedCommitHash` on this card and on the canonical card records. It is therefore a mirror
rather than a variant: a content edit belongs in `skills/` and reaches this path only through
`python3 scripts/sync-skills.py`, never by editing this file (the repository's own `AGENTS.md`
states the rule: "Do not edit generated skill copies directly; edit root `skills/` and run
`python3 scripts/sync-skills.py`.").

## Code Commentary

### Logic

**The content is the contract, and this copy carries it unchanged.** The thirteen fields are split by
ownership — nine producer (`id`, `statement`, `kind`, `target`, `found_at`, `disposition`,
`disposition_source`, `evidence`, `authority`) and four curator (`resolution`, `validated_at`,
`record_action`, `supersedes`) — because "a producer that fills a curator field has made the decision
the curator exists to make." Every entry carries all thirteen keys with the curator fields `null`.
The per-field table names the owner and payload of each; `target` is "**where it applies** — a list
of `{path, locator, governing_route}`", `found_at` is "**where it was evidenced** — a list of
`{path, locator, commit}`", and `disposition` is free text carried verbatim while `kind` may be an
enum.

**The shape block and its locator rules are what a producer copies.** The JSON skeleton carries the
thirteen keys; `target[].locator` is required and is `{kind: "symbol", value}` or
`{kind: "line_range", start, end}` or `{kind: "file"}`, line ranges are one-based and inclusive, and
`found_at[].locator` may additionally be `null` because "the source says it was found, not where" is
information.

**Rule 1 is co-resolution and Rule 2 is no paraphrase; both carry their measured cost.** A `target`
entry is a path *and* the construct inside it from one resolution act, because two independent
resolutions "do not compose, they disagree." The rule is measured: of 40 requirement entries on a
real leaf, "**20 named no path at all**, and **6 of the 20 that did named a file that did not hold
the construct**." `target` is a list and is never split, because splitting breaks `supersedes`;
`target` is identity while `found_at` is dated evidence, so `symbol` is preferred because "it
survives a move." Rule 2 carries `statement`, `kind`, `disposition`, `evidence` and every `found_at`
record verbatim, with the bar measured as "41 entries in, 41 entries out." Only `id` spelling and
path spelling may change.

**The honest encodings and the boundary close the document.** `target: []` is the honest encoding for
a ruling that applies nowhere (eight of the fixture's 41 entries), a `null` evidence locator is a
producer's honest record (13 of 58 real evidence records), a memory path is written once and
memory-root-relative without the `onboarding/` prefix, and `disposition` records the verdict the
producer actually holds while `disposition_source` records where it came from when that is not the
producer's own list. The last section states the template's boundary: "It is not the curator's side."
The curator consumes the list as data, fills the four curator fields, and decides what the record
does about each entry.

**How this copy is generated, shipped and consumed.** `scripts/sync-skills.py` treats the repository's
root `skills/` tree as canonical (`CANONICAL_SKILLS`) and copies it into nine targets, the first of
which is the MCP package data directory `mcp/src/agents_remember/package_data/runtime/skills`. The
copy is a whole-tree `shutil.copytree` into a staging path followed by two renames, and the script's
`sync_target` refuses to sync the canonical tree onto itself. At runtime the shipped tree is the
package's own copy: `application/skill_resources/provider.py` fixes `PACKAGED_SKILLS_DIRECTORY =
"runtime/skills"`, admits the lifecycle corpus inside it as `PACKAGED_COMPOSITION_ROOT =
"l-01-agent-lifecycles"`, and yields the corpus root and its manifest together through
`shipped_composition_corpus()` — "the two are one value because they are one admission." That is why
this file's path exists at all: the compiler reads the packaged corpus, not the authored tree.
`runtime_install` then ships a coordinator-facing copy as well: `install/runtime.py` requires the
packaged `skills` root to exist, and syncs it from the runtime asset root into
`<coordination-root>/skills` through a `RuntimeTreeSync`, preserving the tree's own `AGENTS.md`.

### Conventions

The file is generated output and carries no header marker of its own — unlike the harness starter
files, which say so in a comment — so the rule that it is not edited directly lives in `AGENTS.md`
and in the sync script rather than in the file. It preserves the canonical tree's structure exactly
(`l-01-agent-lifecycles/templates/curator-handoff-list.md` under `runtime/skills/`), so a skill-URI
path stays valid whether the reader resolved it from the authored tree or from the packaged copy. The
sync script ignores only `.DS_Store`, `.pytest_cache`, `.ruff_cache`, `__pycache__` and `*.pyc`, so
every content byte of this file is a deliberate copy of the canonical file rather than a build
product. Because the whole tree is replaced on each sync, a local edit to this file is not merged —
it is overwritten on the next run, and `--check` reports the tree as out of sync in the meantime.

### Invariants And Boundaries

- **This file is a byte-identical mirror, not an independent document.** Its content, its line count
  and its last commit match `skills/l-01-agent-lifecycles/templates/curator-handoff-list.md`; a
  content change is made in `skills/` and propagated, never made here.
- **The canonical tree is the only edit surface.** `scripts/sync-skills.py` copies `skills/` into
  this path among nine targets and refuses to sync the canonical tree onto itself.
- **The packaged copy is what the compiler reads.** `shipped_composition_corpus()` resolves the
  corpus root and the manifest under `runtime/skills`, so a corpus that disagrees with the authored
  tree is what a served capsule would actually compile.
- **The corpus root and its manifest are admitted together.** One without the other, or a manifest
  read from another root, "is a pairing that cannot select a source set."
- **The contract's content rules are unchanged by packaging.** The thirteen fields with four null
  curator fields, the required target locator, one-based inclusive ranges, the null evidence locator,
  the never-split target list and the no-paraphrase rule all hold exactly as the canonical file
  states them.
- **A hand edit here does not survive.** The sync replaces the whole tree through a staged copy, so a
  local change is discarded rather than merged, and `--check` is the way a stale copy is detected.
- **The installed coordinator copy is a third copy of the same bytes.** `runtime_install` syncs the
  packaged runtime `skills` root into the coordination root, so the packaged copy is the source of
  what a coordinator sees, not a separate artifact.

### Todos

No task-independent follow-up is recorded in the source. The generated copy carries no marker of its
own provenance, so the "do not edit generated copies" rule lives only in `AGENTS.md` and in the sync
script; that split is deliberate (the same script writes nine harness copies) rather than an open
item.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The first row is the mirror proof: the same lines of both copies are cited side by side, so a reader
can confirm that this generated file carries the canonical text at the same coordinates. The
remaining content rows cite this copy, and the last four cite the packaging code that generates and
serves it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The mirror proof: this packaged copy and the canonical `skills/` file carry the same opening text at the same line range, so the generated file is a byte-identical copy rather than a variant. | "producer's output shape"; "the requirement-shaped items a leaf's builder and reviewer already"; "where the two disagree, the schema note wins" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:3-6; skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:3-6; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:8-14 |
| The thirteen fields and the nine-producer/four-curator ownership split that is the point of the contract. | "Thirteen fields, and each has a job"; "the four the curator decides or verifies are" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:21-25; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:27-32 |
| The per-field table: each of the thirteen rows names its owner and what the field carries. | "the entry's stable identity, in the producer's own spelling" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:34-48 |
| The JSON skeleton a producer copies, with all thirteen keys and the four curator fields null. | "<the producer's own stable spelling>" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:56-82 |
| The locator rules: the required target locator, the three locator kinds, one-based inclusive ranges, and the permitted null on a found_at locator. | "Line ranges are **one-based and inclusive**" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:84-90 |
| Rule 1, co-resolution: name where the thing lives rather than where you looked, with the measured cost of getting it wrong. | "## Rule 1 — co-resolution: name where the thing lives, not where you looked"; "of 40 requirement entries" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:92-99; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:101-104 |
| Rule 1 continued: the target list is never split, and target is identity while found_at is dated evidence. | "`target` is a list because one requirement can apply in several places."; "it survives a move." | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:110-114; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:116-119 |
| Rule 2, no paraphrase, and the measured byte-identical bar it sets. | "## Rule 2 — no paraphrase: the entry is carried, not rewritten"; "41 entries in, 41 entries out" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:121-128; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:130-131 |
| The honest-encoding rules: a null evidence locator is a producer's honest record, and an empty target list is the encoding for a ruling that applies nowhere. | "13 of 58"; "is the honest encoding for a ruling that applies nowhere" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:138-140; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:209-212 |
| The template's own boundary: it states the producer's side only, and the curator consumes the list as data. | "It is not the curator's side." | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:225-230 |
| The generator: the canonical root the sync copies from, and the target list whose first entry is this package-data directory. | `CANONICAL_SKILLS`; `TARGETS` | scripts/sync-skills.py:15-15; scripts/sync-skills.py:43-47 |
| The serving path: the packaged skills directory and corpus root constants, the shipped tree the server registers, and the corpus-plus-manifest admission the compiler reads through. | `PACKAGED_SKILLS_DIRECTORY`; `PACKAGED_COMPOSITION_ROOT`; `shipped_skill_tree`; `shipped_composition_corpus` | mcp/src/agents_remember/application/skill_resources/provider.py:29-29; mcp/src/agents_remember/application/skill_resources/provider.py:33-33; mcp/src/agents_remember/application/skill_resources/provider.py:40-47; mcp/src/agents_remember/application/skill_resources/provider.py:51-64 |
| The install path: the packaged `skills` root is a required runtime tree, and `runtime_install` syncs it into the coordination root's own `skills/` tree. | `require_runtime_tree`; `skills_sync` | mcp/src/agents_remember/install/runtime.py:392-402; mcp/src/agents_remember/install/runtime.py:790-796 |
| The rules that keep this copy generated: the repository's own statement that the sync script copies root `skills/` into the package-data copy, and the corpus test that pins the contract's one home and its consequences. | "into the MCP package-data copy"; `test_the_curator_hand_off_list_contract_has_one_home_its_consequences_declared` | AGENTS.md:105-107; mcp/tests/test_role_instruction_corpus.py:604-640 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The packaged copy is generated inside this
repository from this repository's own `skills/` tree and served from the same package; no sibling
repository, remote or external system contributes to or reads it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T01:30+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared both enforced `citation_anchor_absent_from_range` rows this card carried, by changing only the two quoted anchor texts.** Both rows failed for the same structural reason: the checker removes backticked code spans from a quoted anchor *including their content* before matching, so a quote holding backticks can never be found in a source that still spells them. Row one's second quote was `"Prefer `symbol` in `target` — it survives a move."`, which can only be searched for as `Prefer in — it survives a move.`; it now reads `"it survives a move."`, verbatim on `...templates/curator-handoff-list.md:116` inside the cited `:116-119` and carrying the same Rule 1 fact (target is identity, so a symbol survives a move). Row two's quote was `"copies root `skills/` into the MCP package-data copy"`, searched for as `copies root into the MCP package-data copy`; it now reads `"into the MCP package-data copy"`, verbatim on `AGENTS.md:106` inside the cited `:105-107` (both verified with `grep -n`) and carrying the same fact (that line is the repository's own statement that the sync script copies root `skills/` into the package-data copy). Each row's other anchor — the `\`target\` is a list …` quote at `:110-114` and the corpus test name at `:604-640` — is untouched and still resolves, every range is unchanged, no Finding text was re-worded, and no citation was dropped. Reviewed against the working candidate `ar/260915-ks-l30-ar`; no commit exists for these bytes and the commit stamp is not advanced.
- 2026-09-20T01:00+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared none of the 2 enforced citation rows this card carried (citation_anchor_absent_from_range) — both cited ranges were hand-read and already hold the anchor text their claims name verbatim ("Prefer `symbol` in `target` — it survives a move." at mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:116, and "copies root `skills/` into the MCP package-data copy" at AGENTS.md:106), so the finding comes from the anchor being resolved with its backticked spans removed and no citation edit can clear it. No range was changed here; every claim wording, anchor and every other range is unchanged, and no verification stamp was advanced.
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 2 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `curator-handoff-list.md.md:153` (it survives a move.) — re-read the claim against the source line: the anchor literal embedded a code span, which the anchor grammar blanks, so it could never match its own source; re-anchored on a span-free literal from the same sentence; `curator-handoff-list.md.md:160` (into the MCP package-data copy) — re-read the claim against the source line: the anchor literal embedded a code span, which the anchor grammar blanks, so it could never match its own source; re-anchored on a span-free literal from the same sentence.

- 2026-09-19T17:09+02:00 — 260915-KS-L28 curator: created this one-to-one card for the packaged mirror
  of the curator hand-off list template. It records that the copy is byte-identical to
  `skills/l-01-agent-lifecycles/templates/curator-handoff-list.md` (empty `diff`, equal MD5
  `6ab039ac49385760f44a3a50347a8de0`, 230 lines, shared commit
  `7e6936c0d3b87f2fa0f462c5c63d6d86441ef10b`), the contract content the copy carries (thirteen fields
  with the nine/four ownership split, the field table, the shape block and locator rules, both rules
  with their measured bars, the honest encodings and the producer-side boundary), and the packaging
  path that generates, serves and installs it: `scripts/sync-skills.py` copying the canonical
  `skills/` tree into `runtime/skills`, the `skill_resources` provider serving the packaged tree and
  admitting the corpus together with its manifest, `runtime_install` syncing it into the coordination
  root, and the `AGENTS.md` rule that forbids editing generated copies directly. Verified against the
  committed source at `7e6936c0d3b87f2fa0f462c5c63d6d86441ef10b`.
