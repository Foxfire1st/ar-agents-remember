# skills/l-01-agent-lifecycles/templates/curator-handoff-list.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/templates/curator-handoff-list.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T02:27+02:00 |
| reviewedWorkingCandidate | candidate `ar/260915-ks-l33-ar`, uncommitted; base `7dcec036094768c5f50e571fb45e59a27ae78efc` |
| lastVerifiedCommitHash | `3888cd8600e39a52c540d6038820759e3d4ffa7a` |
| lastVerifiedCommitDate | 2026-09-20T20:02:13+02:00|
| governingOverview | `skills/l-01-agent-lifecycles/overview.md` |

## Governing Overview

[lifecycle skill overview](../overview.md)

## Purpose

The **producer's output shape** for the curator hand-off list: the document a leaf's builder, its
reviewer and its orchestrator emit so that the requirement-shaped items of a leaf reach the curator
as data rather than as re-told prose. The opening paragraph states the routing — "the worker emits
its list, the reviewer emits its own in the same shape, and the orchestrator hands the curator **that
same list**, unparaphrased, as data" — and names the four seats that own their own side of the
contract: `roles/worker.md`, `roles/reviewer.md`, `roles/orchestrator.md` and `roles/curator.md`.

Two authorities bound the document. The contract's authority is the owning seat's schema note, the
increment's *260915-KS-curator-handoff-list-schema.md* at revision 1 — its thirteen fields, its
rules 1–9 — and this file "transposes revision 1 into the shape a producer writes and nothing more;
where the two disagree, the schema note wins." The worked example that priced revision 1 is a
41-entry fixture kept with the increment outside this repository, so the names are what a reader can
look up. The file is emitted as JSON, "either as a fenced block in the report or as a file beside
it — one document per list, so the curator ingests a list rather than reading a table."

## Code Commentary

### Logic

**The thirteen fields are split by ownership, and the split is the contract.** Nine belong to the
producer — `id`, `statement`, `kind`, `target`, `found_at`, `disposition`, `disposition_source`,
`evidence`, `authority` — and four to the curator — `resolution`, `validated_at`, `record_action`,
`supersedes`. The reason is stated as a rule rather than a preference: the producer answers "what is
true, and where", the curator answers "what the record does about it", so "a producer that fills a
curator field has made the decision the curator exists to make, and a curator that re-derives a
producer field has destroyed the evidence it was supposed to compare against." Every entry carries
all thirteen keys and every curator field is `null` in the producer's hands. `kind` may be an enum;
`disposition` may not — "it is free text carried verbatim."

**The field table is the per-field contract, and each row names the owner and the payload.** `id` is
"the entry's stable identity, in the producer's own spelling" (`KS-R22@v1 §3.2`, `A-1`, `S-4`,
`item 32`) and the thing a later revision names in `supersedes`; `statement` is "**what is true**, as
one sentence: the invariant, not 'the case passes' but what the passing case asserts about the
world"; `kind` is one of `clause`, `finding`, `carried-defect`, `decision`, `measurement`; `target`
is "**where it applies** — a list of `{path, locator, governing_route}`. This is the attribution: an
invariant is a citation beside code"; `found_at` is "**where it was evidenced** — a list of `{path,
locator, commit}`", and it may be plural "because one invariant is often realized in several places
while applying in one sense"; `disposition` is the producer's verdict in its own vocabulary
(`satisfied`, `partial`, `refused`, `fixed`, `recorded`) carried verbatim; `evidence` is the case
name, command or report path; `disposition_source` says "where the verdict came from, when it did not
come from the producer's own list"; and `authority` is the governing route plus the task document the
entry descends from. The four curator fields are the resolved extent with the moment it was resolved
(`resolution`), the moment it was last proved to hold (`validated_at`), the record decision
(`add`, `revise`, `supersede`), and the id this entry replaces (`supersedes`).

**The `Shape` block is the literal JSON skeleton a producer copies, and the locator rules that go
with it are exact.** `target[].locator` is `{kind: "symbol", value}` or `{kind: "line_range", start,
end}` or `{kind: "file"}`, and it is **required**: "a target that names a path and no construct is
refused as an omission rather than read as a whole-file citation, because 'the whole file is the
place' is a claim a producer has to make explicitly." Line ranges are one-based and inclusive, so
`{start: 0}` names nothing and is refused with that reason. `found_at[].locator` may additionally be
`null`, because "the source says it was found, not where" is information and different from an empty
list.

**Rule 1 is co-resolution: name where the thing lives, not where you looked.** A `target` entry is "a
path *and* the construct inside it, produced by one resolution act" — a `symbol` locator when the
invariant is a named construct, a `line_range` when it is an extent, `file` only when the file really
is the whole of the place. Two independent resolutions "do not compose, they disagree, and the
disagreement surfaces later as a citation that resolves to the wrong thing." The rule is stated that
hard because it was measured: on a real leaf, of 40 requirement entries "**20 named no path at all**,
and **6 of the 20 that did named a file that did not hold the construct**." A place the source names
without a path is not a target at all: leave it out, or leave `target` empty and say so, rather than
inventing a path from where a search happened to land. `target` is a list because one requirement can
apply in several places, and splitting such an entry breaks `supersedes` — "the second half of one
defect would read as a new entry rather than the rest of the first." And `target` is identity while
`found_at` is evidence: `symbol` is preferred because "it survives a move", while a line range in
`found_at` is "a **snapshot of where it was when written**", which is what `commit` and
`validated_at` exist to date.

**Rule 2 is no paraphrase: the entry is carried, not rewritten.** `statement`, `kind`, `disposition`,
`evidence` and every `found_at` record travel verbatim from the producer's own list; the statement is
not re-worded, the disposition is not normalised into an enum, the evidence pointer is not tightened
into a summary, and the entries are not re-ordered. The bar is measured: "41 entries in, 41 entries
out, with `statement`, `kind`, `disposition` and `evidence` byte-identical to the pre-revision list."
What may legitimately change is spelling, and only for the two fields that are spellings: `id` is
re-spelled when a later source names the same entry differently (`item 32` → `item 32 / A-1`), and
`target`/`found_at` paths are re-spelled to the contract's own convention. A `null` locator is a
producer's honest record, not a defect — 13 of 58 real evidence records carried none, and none used
`file` — because "null locators and empty target lists are honest encodings; a filler path is not."

**The two worked examples are the shapes producers most often get wrong, carried verbatim from the
fixture.** The first is one defect with two targets — the second place carries no `governing_route`
because none was named, and one `found_at` record has no locator at all (a pytest-budget defect
pointing at `mcp/tests/conftest.py` and `pyproject.toml`). The second is a finding with one
whole-file target and three evidence places dated by the commit they were measured at, showing that
"a `file` locator is honest when the file is the place, and the evidence side keeps the line
precision the producer could afford." Both entries keep all thirteen keys with the four curator
fields `null`.

**The remaining encodings section closes the cases a producer must get right.** `kind` has a mapping
rule because it had five values and no rule: `clause` is a numbered clause of a requirement packet,
`finding` is an entry a reviewer minted with a stable ID, `carried-defect` is a defect carried
forward in a plan's item list, `decision` is a ruling or a recorded choice, and `measurement` is a
report obligation with no code subject. `target: []` is the honest encoding for a ruling that
applies nowhere — a report obligation, a decision the leaf owes, or a bare commit with no code place —
and eight of the fixture's 41 entries are that shape, "none of them was invented into a place."
`governing_route` may be absent, and absent is honest: 3 of the fixture's 40 real target places had
no memory route at all, and the file records that an earlier revision's "11 of 41" was wrong by more
than three times. A memory path is written once, memory-root-relative and without the `onboarding/`
prefix, "because two spellings of one card are two records for one file." And `disposition` records
the verdict the producer actually holds while `disposition_source` records where it came from when
that is not the producer's own list — "an unaudited verdict has already cost a master one sealed
review finding."

**The closing section states the template's boundary.** "It is not the curator's side." The curator
consumes the list as data, fills `resolution`, `validated_at`, `record_action` and `supersedes`, and
decides what the record does about each entry; `roles/curator.md` owns that side, and
`templates/curator-brief.md` feeds the curator its inputs. This file states only the shape a producer
emits.

### Conventions

The document is a field schema, not a brief: it is written as a template with a shape block and rules,
and it deliberately does not restate the schema note's revision-1 prose — "the schema note wins" on
any disagreement. Field names are `snake_case` in JSON (`found_at`, `governing_route`,
`disposition_source`, `record_action`, `validated_at`) because the list is a data document rather
than a wire payload. Every rule carries its measured justification in italics (*Why the rule is
stated this hard*, *The bar this sets, measured*), so a producer can see the cost of getting it wrong
rather than only the instruction. Numbers in the prose are the fixture's own counts and are quoted
rather than re-derived, and one of them carries an explicit correction so a reader does not repeat a
retired figure. Ownership is stated twice on purpose — once as a sentence about the split and once as
the `who` column of the field table — because ownership is the contract.

### Invariants And Boundaries

- **Thirteen keys on every entry, and every curator field `null` in the producer's hands.** A
  producer emits no `resolution`, no `validated_at`, no `record_action` and no `supersedes`.
- **The producer supplies nine fields and the curator decides four.** Re-deriving a producer field
  destroys the evidence the curator compares against; filling a curator field makes the curator's
  decision for it.
- **`target[].locator` is required; `found_at[].locator` may be `null`.** A path with no construct is
  refused as an omission, and a null evidence locator is honest information rather than a defect.
- **Line ranges are one-based and inclusive.** `{start: 0}` names nothing.
- **`target` is a list and is never split.** One requirement realized in several places is one entry
  with several targets, because splitting breaks `supersedes` and makes a partly-touched entry read
  as resolved.
- **`target` is identity; `found_at` is evidence.** Only `found_at` may be plural or move without the
  statement changing, and it is dated by its `commit`.
- **No paraphrase.** The statement, kind, disposition, evidence and every `found_at` record travel
  verbatim; only `id` spelling and path spelling may change.
- **`disposition` is free text carried verbatim, never normalised into an enum.** `kind` is the field
  that may be an enum.
- **A memory path is memory-root-relative, once, without the `onboarding/` prefix.** Two spellings of
  one card are two records for one file.
- **No field is filled to look complete.** A filler path, an invented route or an invented verdict is
  worse than an empty target list or a null locator.

### Todos

No task-independent follow-up is recorded in the file. The two named external artifacts — the
revision-1 schema note *260915-KS-curator-handoff-list-schema.md* and the 41-entry fixture
*260915-KS-curator-handoff-fixture-L23-rev1.json* — live with the increment that produced them,
outside this repository, so this template is the only form of the contract a reader can open here.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The rows below separate the contract document's own rules from the seats that emit or consume it and
the registry that routes it. Two facts are worth carrying while reading them: the producer's entry
carries a path, a locator and a governing route but **no blob identity** — the blob is read and
attached later by the curator's own ingest, which stores the anchor with the tree-read
`source_identity` — and the field ownership split is asserted from both sides, by this template and
by the curator's role file.

| Finding | Anchor | Source |
| --- | --- | --- |
| What the document is: the producer's output shape for a leaf's requirement-shaped items, the authority of the revision-1 schema note, and the JSON emission rule. | "producer's output shape"; "where the two disagree, the schema note wins"; "either as a fenced block in the report or as a file beside it" | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:3-6; skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:8-14; skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:16-17 |
| The thirteen fields and the ownership split that is the point of the contract. | "Thirteen fields, and each has a job"; "the four the curator decides or verifies are" | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:21-25; skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:27-32 |
| The per-field table: each of the thirteen rows names its owner and what the field carries. | "the entry's stable identity, in the producer's own spelling" | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:34-48 |
| The JSON skeleton a producer copies, with all thirteen keys and the four curator fields null. | "<the producer's own stable spelling>" | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:56-82 |
| The locator rules: the required target locator, the three locator kinds, one-based inclusive ranges, and the permitted null on a found_at locator. | "Line ranges are **one-based and inclusive**" | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:84-90 |
| Rule 1, co-resolution: name where the thing lives rather than where you looked, with the measured cost of getting it wrong. | "## Rule 1 — co-resolution: name where the thing lives, not where you looked"; "of 40 requirement entries" | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:92-99; skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:101-104 |
| Rule 1 continued: the target list is never split, and target is identity while found_at is dated evidence. | "`target` is a list because one requirement can apply in several places."; "it survives a move." | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:110-114; skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:116-119 |
| Rule 2, no paraphrase, and the measured byte-identical bar it sets. | "## Rule 2 — no paraphrase: the entry is carried, not rewritten"; "41 entries in, 41 entries out" | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:121-128; skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:130-131 |
| The honest-encoding rules: a null evidence locator is a producer's honest record, and an empty target list is the encoding for a ruling that applies nowhere. | "13 of 58"; "is the honest encoding for a ruling that applies nowhere" | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:138-140; skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:209-212 |
| The template's own boundary: it states the producer's side only, and the curator consumes the list as data. | "It is not the curator's side." | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:225-230 |
| The four seats on either side of the contract: the worker emits it as its hand-off, the reviewer emits its own in the same shape, the curator ingests it as data by field owner, and the orchestrator passes it through unparaphrased. | "That list is your hand-off to the curator"; "Ingest it as data, and treat the fields by their owner"; "Emit it in the same list shape the worker emits"; "the list is the interface" | skills/l-01-agent-lifecycles/roles/worker.md:84-88; skills/l-01-agent-lifecycles/roles/curator.md:23-31; skills/l-01-agent-lifecycles/roles/reviewer.md:88-96; skills/l-01-agent-lifecycles/roles/orchestrator.md:127-133 |
| The registry wiring: the four template lists that declare the hand-off list for the seats that emit or ingest it (each anchor quotes a sibling entry of the same list, because the shared file name appears in all four). | "master-handover-packet.md"; "turn-report.md"; "curator-brief.md"; "impact-analysis.md" | skills/l-01-agent-lifecycles/composition-manifest.json:231-238; skills/l-01-agent-lifecycles/composition-manifest.json:371-375; skills/l-01-agent-lifecycles/composition-manifest.json:402-405; skills/l-01-agent-lifecycles/composition-manifest.json:433-438 |
| The corpus router that names this contract on its own line, and the test that pins its one home, its four consequence sections and the registry wiring. | "the **producer's output shape** for the requirement-shaped"; `test_the_curator_hand_off_list_contract_has_one_home_its_consequences_declared` | skills/l-01-agent-lifecycles/SKILL.md:138-143; mcp/tests/test_role_instruction_corpus.py:604-640 |
| Where the blob identity actually enters: the curator's own target plan builds the stored anchor with the tree-read `source_identity`, and the citation carries that anchor plus the claim citing it. | `_TargetPlan`; `citation` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:479-540; mcp/src/agents_remember/application/knowledge_curator_ingest.py:528-537 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It is a producer-facing shape inside this
repository's own lifecycle corpus; the two artifacts it names as authorities are increment documents
kept outside the repository and are named rather than linked, and no sibling repository or external
system is addressed by any field.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T02:27+02:00 — 260915-KS-L33 curator, reopened-claim re-read (uncommitted change set on `ar/260915-ks-l33-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **re-read the reopened blob-identity row (line 206) and retained its wording unchanged, with one range repointed.** The row names `_TargetPlan` and `citation`, and its wording is still true of the candidate: the curator's target plan still builds the stored anchor with the tree-read `source_identity`, and the citation still carries that anchor plus the claim citing it. Its second range `:443-451` no longer reached `citation`, though — this leaf's CYCLE-04 repair changed `_TargetPlan.citation()`'s body, and the method is now declared at `463-471` — so that range was regenerated to the method's own extent, `mcp/src/agents_remember/application/knowledge_curator_ingest.py:463-471`. The first range `:398-446` was left exactly as written: `_TargetPlan`'s own declaration still sits at `421` inside it. No anchor was renamed, no second range was added, no citation was dropped and no claim wording was changed. This decision is recorded rather than left implicit because the claim's evidence changed structurally after its verification stamp, and the honest reading of that is "re-read, wording retained, range regenerated", not "re-stamped". `reviewedWorkingCandidate` was recorded as this leaf's candidate `ar/260915-ks-l33-ar` on the same base, because that is the candidate this reading was performed against; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded. No commit, no verification stamp advanced, no acceptance claim made.
- 2026-09-20T01:02+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared the 3 enforced citation rows this card carried (citation_claim_reopened, citation_anchor_absent_from_range). Two were verified against the working tree and needed no edit: the `_TargetPlan` row's projected range `mcp/src/agents_remember/application/knowledge_curator_ingest.py:398-446` still contains the class's own declaration (the module has since grown, so the declaration now sits at 421 inside that range) and the reopened claim is current there. The third was fixed by hand in the Anchor cell only: the checker reads a quoted anchor that embeds code spans as the blanked join of its fragments, so `"Prefer \`symbol\` in \`target\` — it survives a move."` could never be found in any range; the quote now reads `"it survives a move."`, the verbatim clause the cited `skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:116-119` actually holds. No claim wording was changed, both ranges are untouched, and no verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 1 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `_TargetPlan`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `curator-handoff-list.md.md:198` (it survives a move.) — re-read the claim against the source line: the anchor literal embedded a code span, which the anchor grammar blanks, so it could never match its own source; re-anchored on a span-free literal from the same sentence.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 1 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `curator-handoff-list.md.md:205` (`_TargetPlan`, `citation`).

- 2026-09-19T17:09+02:00 — 260915-KS-L28 curator: created this one-to-one card for the curator
  hand-off list template. It records the document's role as the producer's output shape, the
  authority split with the revision-1 schema note and the 41-entry fixture it prices, the thirteen
  fields and their nine-producer/four-curator ownership, the per-field table, the required target
  locator and the permitted null evidence locator, Rule 1 (co-resolution, with the measured 20-of-40
  and 6-of-20 counts) and Rule 2 (no paraphrase, with the 41-in/41-out bar), the honest encodings for
  a ruling that applies nowhere and an unrecorded governing route, the template's own boundary that
  it is not the curator's side, the four seats that emit or ingest it, the four registry lists that
  declare it, and the fact that the blob identity is attached downstream by the curator's own ingest
  rather than carried by the producer. Verified against the committed source at
  `7e6936c0d3b87f2fa0f462c5c63d6d86441ef10b`.
