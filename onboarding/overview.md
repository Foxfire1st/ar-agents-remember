# agents-remember — Onboarding Overview

| Field | Value |
|---|---|
| sourceRoute | . |

> **Status:** active baseline

## 260928-MIK-L37 The Cutover To Text Storage

Repository-level consequence of leaf `260928-MIK-L37` (MIK-R37; decision record DEC-YZA7E4): on a converted memory
line, knowledge is text (Markdown and JSON sidecars under `onboarding/`, records under `knowledge/`), written through
the curator file writer and read through the derived index; the knowledge database is frozen there; and the
validator, the onboarding gate on history files, the worklist and the mandatory gate govern every closeout of a
converted line. The plain worktree closeout runs that gate itself before it commits a leaf's memory (decision record
DEC-TJ0CX7). A memory line that is still unconverted, in a repository that holds converted memory, is only read: the
cutover lock refuses its writes, checks, managed memory syncs, closeouts and landings, naming the crossing sync
(decision record DEC-FCNRNT).

The skills say how a curator works on converted memory: the c-05 skill gains `workflows/converted-card-workflow.md`,
and the c-02 skill, the c-05 skill, its file-level workflow and the curator role each gain a converted-memory
paragraph. The c-12 and c-09 skills say that the closeout preview and apply ask the mandatory gate on converted
memory, and the curator hand-off template's History section states the rules for a row's items, a cover's
rationale, naming a row again and the governing row of a changed invariant or family. These are the authored `skills/` copies, synchronized by `scripts/sync-skills.py` into the package copy
and the eight harness starter copies this route governs. The package copies' cards carry the detail.

- The converted-card workflow's opening, in the authored skill copy. [67]
- The curator role's converted-memory step, in the authored skill copy. [68]


## 260928-MIK-L38 A Finished Leaf Shows Completed On Its Master

Repository-level consequence of leaf `260928-MIK-L38` (MIK-R38, developer direction D32): `lifecycle_finalize_task`
completes a leaf's row on the master that lists it even when the leaf names no `master`, because the finalizer, reopen
and the task-document master sync now resolve a leaf's master by one rule (the named master, else the folder's
`task.json` master). A leaf without a listing master finalizes standalone as before. Finalize and reopen also refuse,
before any write, a leaf or master stored under a file name the store would not write it back to, so a hand-made
document can never be written over the series `task.json`. The c-09 skill says so: the authored `skills/` copy,
synchronized by `scripts/sync-skills.py` into the package copy and the eight harness starter copies this route
governs. **This is not gated on the memory conversion**: it applies to every task folder once this build is installed.

- The skill's finalizer paragraph, mirrored into the package and starter copies. [1]

## 260928-MIK-L14 A Changed Ground Reopens A Rejected Alternative, Not Yet Used

Repository-level consequence of leaf `260928-MIK-L14` (MIK-R14@v2): once a memory tree is converted, a decision's
rejected or deferred alternative comes back up when a leaf changes a target its `reconsider_on` link names (a
record, a history row's subject, a code anchor, or a requirement packet whose owning task approved a newer version).
The worklist lists it as a reconsideration candidate, and the curator answers it: `still_rejected` with a reason
(the link is refreshed to what was judged, so the same condition is not raised again, while a later change is), or
`raise`, which puts the decision under reconsideration and appends a question to the leaf's task document for the
developer. The curator never reverses a decision, and a linked alternative cannot be reordered to another index.
The curator's hand-off template says how to write the row: the authored `skills/` copy, synchronized by
`scripts/sync-skills.py` into the package copy and the eight harness starter copies this route governs.
**Nothing the installed runtime does changes before MIK-R37**: unconverted memory gets no worklist and no file
write.

- The template's reconsideration-row bullet, mirrored into the package and starter copies. [2]
- The decision section's reorder refusal. [3]

## 260928-MIK-L05 A File Sees The Families Whose Territory It Lies In, Not Yet Used

Repository-level consequence of leaf `260928-MIK-L05` (MIK-R05@v2): once a memory tree is converted, reading a
file through `read_ar_files`, or through `knowledge_read` with `view: "source_context"` and `sourcePath`, also
returns one compact row per family with a route on the file's directory or an ancestor, after the file's own
family content, so a new or unattributed file still sees the families whose territory it is in. Each row's
`expand` reads that family whole (`source_context` with `familyRevisionId` and no `sourcePath`). A repeated
`read_ar_files` in the same session may shorten an unchanged row to `served_earlier`; `knowledge_read` never
does. The skill `c-04-retrieval-strategy-router` teaches this in one paragraph (ruling Q5): the authored
`skills/` copy, synchronized by `scripts/sync-skills.py` into
[the package copy](mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md.md)
and the eight harness starter copies this route governs. **Nothing the installed runtime does changes before
MIK-R37**: unconverted reads are byte-identical to base.

- The skill's route-chain paragraph, mirrored into the package and starter copies. [4]

## 260928-MIK-L10 Every Unexplained Change Needs An Authored Disposition, Not Yet Used

Repository-level consequence of leaf `260928-MIK-L10` (MIK-R10@v2): once a memory tree is converted, every change a
leaf makes that no recorded entry covers becomes a worklist item the closeout gate will require an answer for. In a
covered file the curator attaches the change to an existing invariant, authors a new one, or records a
`no_invariant` history row with a reason; a delete-only change admits only the row. In a file the knowledge graph
does not cover yet, the file's onboarding trace answers it. The curator's hand-off template says how to write the
row: the authored `skills/` copy, synchronized by `scripts/sync-skills.py` into the package copy and the eight
harness starter copies this route governs. **Nothing the installed runtime does changes before MIK-R37**:
unconverted memory gets no worklist.

- The template's no_invariant-row bullet, mirrored into the package and starter copies. [5]

## 260928-MIK-L13 Decisions Are Recorded With The Alternatives They Rejected, Not Yet Used

Repository-level consequence of leaf `260928-MIK-L13` (MIK-R13@v2): once a memory tree is converted, a developer
ruling or requirement-packet choice that keeps governing code can be kept as a decision record with the
alternatives that were weighed. The knowledge validator refuses a decision with fewer than two alternatives, with
no chosen alternative or several, with a rejected or deferred alternative that does not say when to reconsider it,
with a stored `superseded`, or with a `reconsider_on` link to an alternative that does not exist or is chosen. The
curator writer reports each requirement packet a record links as `resolved` or `unresolved` through the requirement
owner, and never refuses on it; admission never treats a decision as an export. The curator's hand-off template and
role (step 3) say how to lift decisions at closeout: the authored `skills/` copies, synchronized by
`scripts/sync-skills.py` into the package copies and the eight harness starter copies this route governs.
**Nothing the installed runtime does changes before MIK-R37**: the conversion writes no decisions, and unconverted
memory is unchanged.

- The template's decision-record section, mirrored into the package and starter copies. [6]
- The curator role's step-3 pointer to lifting decisions. [7]

## 260928-MIK-L01 A Path Is Read With Its Whole Family, Not Yet Used

Repository-level consequence of leaf `260928-MIK-L01` (MIK-R01@v2): once a memory tree is converted, reading a
file through `read_ar_files`, or through `knowledge_read` with `view: "source_context"` and `sourcePath`, returns
the file's own invariants, every family containing them with its guarantee and routes, every member's statement
and entries, and the families one hop further as advertised rows -- one selection, under one manifest digest, on
both surfaces, paged by the MIK-R02 threshold when it does not fit one response. A `repositoryRoot` with no
commit is now refused by name instead of raising, on every read. The skill `c-04-retrieval-strategy-router`
names this view (rule 6): the authored `skills/` copy, synchronized by `scripts/sync-skills.py` into
[the package copy](mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md.md)
and the eight harness starter copies this route governs. **Nothing the installed runtime does changes before
MIK-R37**: a database read keeps its recorded-scope selection, byte-identical.

- The skill's paragraph naming the family-complete leaf read, mirrored into the package and starter copies. [8]

## 260928-MIK-L06 A Family's Routes Must Follow The Code, Not Yet Used

Repository-level consequence of leaf `260928-MIK-L06` (MIK-R06@v2): once a memory tree is converted, a leaf
whose change breaks a family's routes (a route directory gone, a route left with none of the family's
realizations, a realization outside every route, or a family without routes that the leaf reaches) gets a
`family_route_condition` worklist item. It is answered only by the leaf's family row (never `no_impact`) and a
family record that satisfies MIK-R04 again, so a stale route cannot survive the closeout of the leaf that
caused it. A route already dead before the leaf stays a validator report for the migration, and retired
families raise nothing. The curator writer can now record a directory move with `moved` rows that relocate
an entry to its new file. **Nothing the installed runtime does changes before MIK-R37**: unconverted leaves
get no worklist.

## 260928-MIK-L27 New Knowledge Records Must Be Admitted, Not Yet Used

Repository-level consequence of leaf `260928-MIK-L27` (MIK-R27@v1): once a memory tree is converted, every
**new** invariant, family and decision record must state the admission criterion it meets with a
one-sentence justification in words, and the knowledge validator refuses one that does not (developer ruling
D14: each record must be meaningful, not a second test suite written as prose). Exported and existing
records are only reported, never refused; a record is exported only when its ID derives from its
`legacyId` (ruling 2026-09-29T23:04:57 F2); retired records are exempt; and the live `legacy-unassessed`
records are counted until migration (MIK-R19) assesses or demotes them. The curator template, the c-14
knowledge-bootstrap skill and the reviewer criteria (OM-4, by requirement, ruling 22:11:24 Q3) state the
rule: the authored `skills/` copies, synchronized by `scripts/sync-skills.py` into
[the package copy of the template](mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md.md),
[the package copy of c-14](mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md.md),
[the package copy of the criteria](mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/onboarding-memory.md.md)
and the eight harness starter copies this route governs. **Nothing the installed runtime does changes before
MIK-R37**: the validator runs only over converted trees, the conversion carries only exports, so nothing is
refused until records are authored on a converted line.

- The template's admission section, mirrored into the package and starter copies. [9]
- OM-4, mirrored likewise. [10]
- c-14 step 3's admission paragraph, mirrored likewise. [11]

## 260928-MIK-L11 A Leaf's Planned Knowledge Effects Are Reconciled With What It Delivered, Not Yet Used

Repository-level consequence of leaf `260928-MIK-L11` (MIK-R11@v2): once a memory tree is converted, a leaf's
task document may declare, before implementation, the invariant and family effects it expects
(`expectedKnowledgeEffects`), and the change-to-knowledge worklist reconciles that plan with the leaf's history
rows. Every invariant and family item is marked `planned` or `unplanned`; every declared effect no row delivers
as declared becomes a `planned_untouched` item, which only an authored planned row answers
(`realized_elsewhere`, `deferred`, or `dropped` citing a decision of the leaf's task document). An approved
strengthening that never happened is therefore visible, and a `no_impact` row cannot clear it. The curator
template gains the planned-row bullet and the adversarial reviewer's role gains one line (check a leaf's
declaration against its packet): the authored `skills/` copies, synchronized by `scripts/sync-skills.py` into
[the package copy of the template](mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md.md),
[the package copy of the reviewer role](mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md.md)
and the eight harness starter copies this route governs. **Nothing the installed runtime does changes before
MIK-R37**: unconverted leaves get no worklist, and no real task document may carry the field before that
install, because the installed runtime refuses unknown task-document fields (architect ruling Q2,
2026-09-29T21:56:18+02:00). An absent declaration leaves every existing task-intent digest unchanged.

- The template's planned-row bullet, mirrored into the package and starter copies. [12]
- The reviewer's declaration check, mirrored likewise. [13]

## 260928-MIK-L02 A Bounded Knowledge Page Continues Through `knowledge_read`, Not Yet Used

Repository-level consequence of leaf `260928-MIK-L02` (MIK-R02@v2): once a memory tree is converted, every
bounded knowledge read is cut to one token threshold (8,000 `tiktoken:o200k_base` tokens), stated on every
response, and the knowledge block of a `read_ar_files` response is bounded as a whole. A page's continuation
is accepted by the mounted `knowledge_read` whichever surface minted it, so an agent holding a partial read
can finish it; the token binds the memory tree, the seed, the selection policy and manifest, the ordering and
the code tree, and a mismatch is refused with no partial page. The skill `c-04-retrieval-strategy-router`
teaches that route (rule 6): the authored `skills/` copy, synchronized by `scripts/sync-skills.py` into
[the package copy](mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md.md)
and the eight harness starter copies this route governs. **Nothing the installed runtime does changes before
MIK-R37**: a database read keeps its budgets and cursors, byte-identical, and the skill keeps the by-identity
read for it.

- The skill's taught route through `knowledge_read`, mirrored into the package and starter copies. [14]

## 260928-MIK-L30 The Onboarding Gate Moves To History Files, Not Yet Used

Repository-level consequence of leaf `260928-MIK-L30` (MIK-R30@v1): once a memory tree is converted, the
onboarding refresh gate no longer reads Update History or `lastVerifiedCommit*`. Every changed source file's
card, and its nearest governing route overview, needs either a counted change (Markdown, or a sidecar field
other than an anchor's `blob`, line numbers and `content`) or an `onboarding_trace` row with disposition
`no_impact` in the leaf's history file. The rule is
[`worktrees/modules/onboarding_trace.py`](mcp/src/agents_remember/worktrees/modules/overview.md); the
curator's memory-quality run and the closeout validator dispatch to it only on a converted tree, and its items
join the leaf's worklist. The canonical curator hand-off template's writer section gains a bullet for the
onboarding row, synchronized by `scripts/sync-skills.py` into the package copy and the eight harness starter
copies this route governs. **Architect rulings (2026-09-29):** 18:49:50 (on converted trees only a counted change or a history row satisfies a trace, so curator-coherence no-impact judgments no longer count there; `onboarding_trace` items go into the persisted `knowledge-worklist.json`; the root route's subject is `onboarding:overview`; the converted-base cache is v2 and also holds onboarding Markdown; deleting `memory_quality/style/update_history/` is left to MIK-R37; the wiring outside the Scope list is accepted); 19:23:45 (mixed formats give an incomplete side, never a vacuous pass; items are sorted by `(kind, subject)`; a v1 cache file is ignored and rewritten; an unreadable sidecar never satisfies a trace); 19:53:54 (`onboarding_item_open` agrees with the live gate; an unreadable K_B sidecar is an incomplete input, an unreadable K_C sidecar keeps the item open, and a readable repair counts). **Nothing the installed runtime does changes before MIK-R37**: every
unconverted tree keeps today's gate, byte-identical, including this master's own closeouts.

- The hand-off template's onboarding-row bullet, mirrored into the starter copies. [15]
- The history-file gate's rule. [16]

## 260928-MIK-L28 Test Proofs Are Read Back And Listed, Not Yet Used

Repository-level consequence of leaf `260928-MIK-L28` (MIK-R28@v1): the tests that prove an invariant become
first-class. Hand-off evidence names a test as `path::name` or as `path -k name` (architect ruling), and a
proof is still written only once the curator authors its facet.
[`application/knowledge_proofs.py`](mcp/src/agents_remember/application/overview.md) reads proofs back for
`knowledge_read`'s `invariant` and `family` views (an optional `proofs` field, accepted by architect ruling)
and lists the invariants without proof in the curator checklist, as information and never counted toward
`curatorActionableCount` (architect ruling). Rule 3 and the stale-proof clause moved to L08 and L03 by
architect ruling. The canonical curator hand-off template's writer section now names both evidence forms and
gains "Proofs are shown and counted (MIK-R28)", synchronized by `scripts/sync-skills.py` into the package copy
and the eight harness starter copies this route governs. **Nothing the installed runtime does changes before
MIK-R37**: no production memory tree is converted, and database reads carry no `proofs`.

- The template's new proof guidance. [17]
- The two readings of proofs. [18]

## 260928-MIK-L21 The Text Knowledge Format Is Declared, Not Yet Used

Repository-level consequence of leaf `260928-MIK-L21` (MIK-R21@v1), the first leaf of the
maintained-invariant-knowledge master: the package now **declares** the text knowledge format that will
replace the SQLite knowledge store as the source of truth (Markdown for prose, canonical JSON for
structured facts: global records under `knowledge/`, file and route sidecars under `onboarding/`). The
declaration is `mcp/src/agents_remember/models/knowledge_files/`, applied by the new
`agents-remember knowledge-format` command. **Nothing the installed runtime does changes before MIK-R37**:
the live memory repository is still read and written through the knowledge store, and the canonical
curator hand-off template (synchronized into the package and the eight harness starter copies by
`scripts/sync-skills.py`) only gained an informational section saying where each hand-off field will land.

- The format declaration's own statement that text files become the source of truth. [19]
- The template's informational section and its no-change-before-MIK-R37 statement. [20]

## 260928-MIK-L12 The Curator Writer Writes Knowledge As Files, Not Yet Used

Repository-level consequence of leaf `260928-MIK-L12` (MIK-R12@v2): the package gains the curator file writer,
[`application/knowledge_writer/`](mcp/src/agents_remember/application/overview.md), which creates and updates
every knowledge kind (invariant, family, decision and the seven other facet records; realization and proof
entries; history rows) as files, fills every mechanical field (IDs, anchors with `blob` and `content` at the
code candidate C, revisions, origin with the hand-off evidence, canonical formatting), and runs the knowledge
validator over the whole resulting tree before it writes anything. `agents-remember knowledge-ingest` and
`agents-remember knowledge-bootstrap` choose their writer by the memory tree they write: a converted tree
(`knowledge/layout.json`) goes to the file writer, and every other tree keeps today's database ingest
unchanged; the database modules stay until MIK-R26 (leaf L26), and `knowledge_change` stays registered and
refusing. An anchor's `content` has exactly one definition,
[`models/knowledge_files/anchor_content.py`](mcp/src/agents_remember/models/overview.md). The canonical
curator hand-off template gained the section "The file writer's sections (MIK-R12)", synchronized by
`scripts/sync-skills.py` into the package copy and the eight harness starter copies. **Nothing the installed
runtime does changes before MIK-R37**: no production memory tree is converted.

- The template's file-writer section and its converted-memory condition. [21]

- The writer refuses an unconverted memory tree. [22]

## 260928-MIK-L04 Family Routes Are Checked, Not Yet Used

Repository-level consequence of leaf `260928-MIK-L04` (MIK-R04@v2): in the text knowledge format a family
record owns its `routes`, the repository directories where its code lives (`.` for the repository root), and
the knowledge validator now refuses a converted memory commit whose routes do not cover every member's
realization or hold a route with none. The curator places routes; `agents-remember knowledge-routes` shows a
mechanical suggestion and never writes one. The canonical curator hand-off template gained an informational
"Family routes (MIK-R04)" subsection, synchronized by `scripts/sync-skills.py` into the package copy and the
eight harness starter copies. **Nothing the installed runtime does changes before MIK-R37**: no production
memory tree is converted or holds a family record.

- The template's family-routes subsection. [23]

## Current reviewer and publication ownership

The Intent Reviewer composes recorded family context with complete source review. Its normal entry shares one subject catalogue with the task entry; source selection remains independent of attribution. Historical reads prefer retained comparisons and otherwise reconstruct only exact recorded source and memory endpoints with that distinction visible. Ordinary curation publishes through the admitted knowledge writer and records the reviewed comparison; code-only recording explicitly validates unchanged knowledge. Curators author applicability, conditions and exclusions instead of relying on a workflow-shaped default.

## 260921-ICR-L45 Curators Author A Rationale Per Realization Target; The Writer Generates None

Repository-level consequence of leaf `260921-ICR-L45` (ICR-R20@v1 repair; developer ruling "require
rationale"): the one knowledge writer (`knowledge-ingest` / `knowledge-bootstrap`, both driving
`application/knowledge_curator_ingest.py`) no longer fabricates realization rationale. Every **new**
realization target must carry an authored `rationale` (its own, or the entry's explicit
`realization_rationale` default); otherwise its entry is refused by name before any identity is minted.
The canonical instructions that teach this live at repository root — `skills/l-01-agent-lifecycles/`
(`templates/curator-handoff-list.md`, `roles/curator.md`, `operations/curation.md`) and
`skills/c-14-knowledge-bootstrap/SKILL.md` — and reach the package and the eight harness starter
packages only through `scripts/sync-skills.py`. Knowledge already published keeps its old generated
sentences unchanged; replacing them is authored successor work, not a rewrite. Exact retries of
operations already committed replay unchanged.

- The canonical template's per-target rationale section. [24]

## 260921-ICR-L34 The Intent Reviewer's Comparison Becomes Recordable, And A Placed Baseline Becomes Openable

`260921-ICR-L34` (D62) is a delivery leaf rather than a repair: the repository had a complete, measured
**producer** for a leaf's durable review comparison and **no caller for it outside its own test suite**,
so no leaf could record a comparison and the Intent Reviewer's knowledge column rendered its empty
sheet for every leaf of this master.

**The umbrella CLI gains its sixth subcommand, and it is a caller rather than a mechanism.**
`agents-remember review-record-comparison` (`cli/review_comparison_record.py`) takes a required
`--config` (the coordination authority the freeze reads) and a required `--contract` (the write guard:
a generation is published under the task root that enclosure document records, so no argument list can
aim a record at another leaf's line), composes the review through the surface's own resolution and
composition, names the leaf's standing generation as the successor's predecessor, and publishes only
what that composition bound. It authors no knowledge, places no dataset and establishes no before half.
One **package-level fact** follows for a reader of this repository: the freeze is a command an operator
runs while the leaf's enclosure is live, not a route, a pane or a closeout path.

**The ordinary continuity route was broken, and it was invisible.** A dataset's namespace was read from
`candidate-receipt.json` **alone**. A *candidate* half has one — an admission wrote it — but a **before**
half placed by a run handed a published `--baseline` never does, because a published dataset is not an
admitted candidate and carries `baseline-generation.json` instead. The read therefore fell back to the
requested repository name while the bytes were bound to a namespace id, the storage owner refused the
mismatch, and the freeze answered `candidate_dataset_absent` — so **every leaf on the ordinary
`knowledge-ingest --baseline` route produced a comparison that could not be frozen**, and no test could
see it because the fixtures hand-assemble their pairs. The rule is now **the record beside the bytes**:
the receipt when there is one, otherwise the before half's own generation record, with the requested
repository used only when **neither** exists. The consequence a reader acts on is that
`/api/review/intent` and `/api/review/intent/entries` answer for a leaf of this master from the recorded
comparison instead of refusing, and the mounted reviewer renders families, joint guarantees, member
statements, linked expressions and evidence.

**Two limits are recorded rather than smoothed.** The producer is **live-leaf-only**: the retention
owner requires a captured candidate identity and both closed-leaf resolutions deliberately pass `None`,
so a closed leaf cannot publish. And the new command is **not idempotent as its own docstring claims** —
`lineage` sits inside the seal, so naming a standing generation changes the derived id and an ordinary
retry appends a successor with two full retained knowledge snapshots rather than reusing the record.
Both are carried on the new sidecar; the per-file detail lives there and in
`mcp/src/agents_remember/application/review_candidate_resolution.py.md`.

## 260921-ICR-L32 The Pre-R25 Repair: The Seat Policy Moves, And Two Long-Route Defects Close

`260921-ICR-L32` is a repair leaf rather than a requirement's first delivery: it closes findings earlier leaves
routed away, and one of them changes a **policy** this repository had twice written down.

**The curator seat is admitted taskless (D56).** `serving/task_binding.py`'s `TASKLESS_SEAT_ROLES` gained
`curator` on the developer's 2026-09-24 ruling, so a document-less session opened for the curator receives the
curator's capsule (`free-agent:curator`) instead of `400 task-binding-required`, and a route-level case pins
the whole five-arm status table rather than the constant alone. The coupling is the larger half: L27 had
landed a sentence saying such a seat does not exist, so the six instruction carriers and all ten of their
generated copies were corrected first, and a test module's own docstrings with them. The seat-policy notes on
this repository's cards are dated statements about the bytes each curation read, which is why this leaf adds a
second note rather than editing the first.

**The Git path-enumeration family is NUL-safe (D02).** `changed_files_with_counts`, `changed_worktree_paths`,
`_diff_paths` and `committed_changed_paths` now read NUL-delimited Git output on all four, pair the two-field
rename form correctly, and rewrite nothing — measured, five real changes in and five rows out, where the
leaf's base returned four rows, two of them addresses no file holds and one real change absent. This is
`ACCEPTANCE.md`'s A24 row.

**The rail census is restored (D54).** `mcp/tests/test_curator_family_authoring.py` (1320 lines at L28) is
split into 818 lines plus a purpose-named sibling of 578, so the ≥1200 offender census returns to **27** under
the rail's own `git ls-files '*.py'` scope and **26** under the narrower `mcp/`-only scope, with the catalog
still **16 contracts / 66 artifacts**. **Two production sentences now name both write entry points (D55)**
where they named one, and **the first ordinary `--contract` run of a baseline-forked candidate commits (D57)**
where it used to refuse a family revision its own baseline stores.

## 260921-ICR-L27 The Knowledge Foundation Gets A Procedure, And First-Time Creation Gets A Real Entry

`260921-ICR-L27` (`ICR-R27@v1`, curator-led knowledge bootstrap workflow) gives the repository a
dedicated, operable process for creating a project's **initial knowledge foundation**, and it makes that
process reachable from ordinary new-project setup and from an explicit bootstrap of an existing project.
A repository's memory has two halves that are created in different ways: **onboarding** is Markdown a
seat writes, and the **knowledge foundation** is authored records in the knowledge database —
invariants and facets, the families and guarantees that hold obligations together, the exact source
realizations, and the external sources they rest on. Nothing scaffolded the second half, and before this
leaf the only shipped instruction that authored any knowledge was the leaf route, which requires an
enclosure contract. A repository whose first knowledge is being written has no leaf and no contract, so
first-time creation had no operational process at all.

**One new canonical instruction home, and the existing owners around it.** The delivery adds
`skills/c-14-knowledge-bootstrap/SKILL.md` — a **procedure**, not a role and not a second orchestration
system. The semantic owner is the existing curator, the writer is the existing admitted knowledge batch
writer, and the publication lands at the one location the ordinary read route already selects. The
procedure states the order those owners are used in and the states a run must distinguish; it adds no
agent, no parallel onboarding track, no second database and no new destination.

**The carriers that reach it are the existing ones, and each gained one bounded step.**
`c-13-install-and-onboard` delegates the foundation to `c-14` and stops reporting a repository ready
without its outcome; `c-03-repo-bootstrap` names the foundation in its handoff as a separate step and
states that onboarding is one optional input to it; and the `l-01-agent-lifecycles` carriers state who
runs it — `roles/curator.md` and `operations/curation.md` own the authoring, `roles/bootstrap.md` and
`operations/bootstrap.md` own the first-hour seat that reads the foundation's state and hands it on.

**The seat gate is the part most easily stated falsely, and it took a second leaf to finish stating it.** The shipped
opener admits a role with **no** task document only for the taskless seats
(`bootstrap`, `chat`, a plain `terminal` pane, and — since the developer's **2026-09-24 ruling** —
`curator`); every other role is refused, in the product's own words, `400 {"status": "task-binding-required",
"detail": "named role scope is required"}`. At L27's bytes **a taskless curator seat did not exist**, and an
independent round-one verdict found the first revision of that delivery asserting the opposite in the
procedure and in four sibling carriers and called it **`blocking`**; that leaf's corrected text stated the
route which then existed, quoted the refusal verbatim, and reported the residual gap as a limit rather than
as compliance. **`260921-ICR-L32` then closed the gap from the other side**: on the developer's 2026-09-24
ruling `curator` joined the taskless seat roles, so a repository that must build its foundation before any
task exists now has two carriers — a **taskless curator session**, which authors under the curator's own
rules, and the taskless **bootstrap** seat, which reads the state and hands the step on — while the taskless
writer still runs from a session with **no enclosure in scope** and refuses one (`enclosure_in_scope`), so a
bootstrap can never publish onto a task's memory line. The instruction carriers and their ten generated
copies were corrected first (`scripts/sync-skills.py --check` green) and this memory follows them.

> **Seat-policy note at L27's bytes (dated 2026-09-24).** This records the policy of the candidate that curation read: code base `06ed70cfcde7e3860ee5b53435727e7512e4335c` plus that leaf's working-tree delta, where `TASKLESS_SEAT_ROLES` was `{"chat", "terminal", "bootstrap"}` and a document-less `curator` session was refused `task-binding-required`. That was true of those bytes and is **superseded**: whether `curator` joined the set was then a product decision under revision, and it was taken in `260921-ICR-L32`. The carrier instructions and their ten generated copies changed first and this memory followed them.
>
> **Seat-policy note at these bytes (L32 curation, dated 2026-09-24T17:20+02:00).** At the bytes this curation read — code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus this leaf's working-tree delta — `TASKLESS_SEAT_ROLES` is `{"chat", "terminal", "bootstrap", "curator"}`: a document-less `curator` session is **admitted** and receives the curator capsule, while every other role is still refused `task-binding-required`. Read the sentences above as the policy **at these bytes**, not as a permanent property of the product.

**Four knowledge states are four different facts.** `not-recorded` (no publication is recorded — the
first-foundation entry), `recorded` (a dataset bound to this repository stands there; read it before
extending and never reinitialize it), `unusable` (something stands there that is not a dataset this
route can answer from, or it belongs to another repository's authority home, with the shipped refusal
codes `selected_input_unavailable` and `snapshot_unavailable`), and `context-not-admitted`, which is the
**admission** refusing and is not a knowledge state at all. A location with no file-system entry is
`not-recorded`; a directory where the dataset belongs is `unusable`; a null or missing count is never
rendered as a measured zero, and a missing optional source is absent rather than failed.

**Two writers, and the enclosure is what separates them.** The taskless entry is
`agents-remember knowledge-bootstrap --repo <repo_id> --list <hand-off list> --authorization-ref <ref>
--commit`, which derives its own admission from the declared repository entry, the resolved memory line
and the real revisions — no development leaf, worktree or synthetic enclosure, and no boolean granting
admission. The leaf route remains `agents-remember knowledge-ingest --contract <this leaf's enclosure
contract> … --publish --commit --json`. **Planning is the default and planning is the dry run**: without
the developer's commit word nothing is written, and `--authorization-ref` is both the admission and the
actor the authorship envelope names, so one reference keeps "who authorized this" and "who authored it"
one recorded fact. Exit zero is never a publication claim: the report's per-entry outcomes, the
independent publication read-back (`confirmed` / `mismatch` / `unavailable`), the destination contents
and the remaining/unmeasured/carried work are what state a result, and an empty destination or a
committed-nothing batch is not a populated foundation.

**Propagation is generated, and the installed harness roots are a separate fact with its own
measurement.** The root `skills/` tree is canonical; `scripts/sync-skills.py` copies it into the
package-owned `mcp/src/agents_remember/package_data/runtime/skills/` copy and into the eight self-hosted
harness starter packages. This leaf ran the generator and its `--check` and installed no harness skill
root; **that install landed later, and this paragraph said the opposite until the `260921-ICR-L25`
curator corrected it on 2026-09-24.** Measured at that correction, `~/.agents/skills` — the root the
delivered server reports as `server_info.harnessSkillRoot` — holds
`c-04-retrieval-strategy-router/SKILL.md` at **241 lines**, sha256
`4a8bf5a83d202ca72685aa68c89d575ff4a1870e127d026c8e48273580c09c88`, and
`c-14-knowledge-bootstrap/SKILL.md` at **311 lines**, sha256
`87aaacd18fd072563ba71af10ca40a25506d18a00d2c97f5460377cfa036ed8d`, each byte-identical (`cmp`) to the
canonical `skills/**` in the accepted tree. **The other installed roots do not follow it**: at the same
reading `~/.claude/skills`, `~/.codex/skills`, `projects/.claude/skills`, `projects/.codex/skills`,
`projects/.pi/skills`, `projects/.hermes/skills`, `projects/.deepseek/skills` and
`projects/.kimi-code/skills` each still hold `c-04` at 179 lines, sha256
`45174b88161cfc57365ac56c27b143cbf1c23f1f032d4f235403d009aedcc66b`, and **no `c-14` at all** (measured
absent), while `~/.hermes/skills` carries **no `c-04`** in any revision — measured absent, not stale. A
fresh session on this host can therefore load the new procedure through the delivered root, and the
leaf's own sentence is superseded rather than repeated.

**One test module carries the delivery's readings.** `mcp/tests/test_knowledge_bootstrap_procedure.py`
(453 L, seven cases) keeps four readings apart — the served catalog publishes the procedure and the
served bytes are the canonical tree's; every invocation the procedure prints parses through the shipped
command line; the seats it names are admitted or refused **by observed status** at the dashboard's own
open route; and the instructions that are delivered name it. On the leaf's base the module is **5 failed
/ 2 passed** and on the candidate **7 passed**, with the two base-passing cases disclosed as the seat
gate that constrained the correction.

## 260921-ICR-L28 The Curator's Family Plane And External-Source Plane Reach The Store

`260921-ICR-L28` (`ICR-R28@v2`, grounded family and invariant foundation) is the leaf that makes the
curator's two authored planes **reach the database** rather than stop in a report. The repository gains
**five purpose-named application owners** under `mcp/src/agents_remember/application/` — the authored
family plane, its resolution against the candidate, its coverage, the seam that reads both planes, and
the bounded external-source manifest — plus one twenty-case test module, thin wiring in the ingest and
its report, and the curator method in the `l-01-agent-lifecycles` carriers.

**Why the shape is what it is.** The obligation is `ICR-R28@v2`'s: where source evidence and project
intent justify a joint obligation, the curator authors the family identity, its **independent**
joint-guarantee revision and memberships linking **exact** family and invariant revisions, while an
external source is retained through `Authorship.origin_refs` and never through a fabricated Git anchor.
That splits cleanly into four questions with four owners, and the split is the point: nothing is
grouped by inference, and no two of the three family outcomes (`member`, a *deliberate* `no_family`
with its basis, and *unexamined*) can be read as one another anywhere along the seam.

**A closed defect worth carrying forward.** During the fix round the operation could report
`recorded` / `authored` / `added` over a store holding **zero** family rows: the replay short-circuit
decided "is there anything left to write" from the *invariant-revision* replay set, so a run whose
entry's revision already existed skipped the batch — including the family commands the same plan
carried — while the report was still assembled from the plan's own states. The fix makes the operation
ask the **batch** what it would carry, and a replayed entry now contributes **its family plane alone**.
The leaf's own reference rows and history entries record the correction rather than the superseded
behaviour: a plan-based claim is not evidence of a write.

**Scope boundaries held.** No new agent role, no new store, no bulk Markdown import, and no route that
lets operational Markdown become the database. The five new owners write nothing themselves: the
commands travel into the one batch `knowledge_ingest.py` builds, so the one writer and the one
transaction stay the only implementations.

## 260921-ICR-L31 The Comparison-Bound Family Review Context

`260921-ICR-L31` (`ICR-R31@v1`) gives the normal task review a composition it had no way to state
before: for the review's selected subject, **which recorded families it belongs to on each of the two
bound snapshots, each selected family revision's own authored joint guarantee, and that revision's
complete recorded member roster — unchanged siblings included**. The flat subject catalogue
(`ICR-R09@v1`) lists subjects and the relationship union (`ICR-R08@v1`) states movement; neither
carries the guarantee and its member obligations together, which is what a reviewer of a changed member
actually has to read.

Two new owners under `mcp/src/agents_remember/application` carry it — `review_family_context.py`
composes, `review_family_rosters.py` reads one exact family revision's roster — with the value
vocabulary in `mcp/src/agents_remember/models/knowledge/review_family_context.py`. The composition
calls the shipped read operation and `ICR-R07@v1`'s own head rule over the snapshots' authored
predecessor edges, so it selects no revision by label, by version or by order: several legitimate heads
stay several, carried as inspectable candidates with no revision chosen and no guarantee presented as
the family's own. A family selection's revision population is the **family owner's own list**, so a
revision that cites no member is still a revision of its family; a family the snapshot records with a
guarantee and no members is a context with a measured empty roster; and `no_family_recorded` is a
measured zero reserved for a family neither snapshot records.

`knowledge_review.compose_review` calls the composition once and carries it on the payload as the
required `family_context` field; `review_task_context.task_context_review` answers that field with the
one state that claims nothing, because a review that selected no subject compared no operand. The
union of bounded collections this surface publishes gained its third member (`family_members`), and the
one collection the projection continues is one family revision's recorded roster, walked with the read
owner's own cursor.

Three case modules accompany it (`mcp/tests/test_review_family_context.py`, its `…_population.py`
sibling added by fix round 1, and `…_values.py`), and the leaf re-pinned the evidence-lifecycle
catalog twice for the two consumer rows those modules are derived from — sixteen contracts and
sixty-six artifacts unchanged, no artifact identity moved.

## 260921-ICR-L23 The Review Surface Measures The Raw-Git Identity Boundary

`260921-ICR-L23` (`ICR-R23@v1`) makes the review surface measure a fact it had no way to state
before: a declared identity that a *raw* Git operation — a rebase, a cherry-pick, a revert, a
checkout that left its declared branch — replaced with no managed transaction behind it. Until
now the only recorded movement was a managed sync's rebinding, so a rewritten branch read exactly
like an untouched one. The boundary lives in
`application/review_external_git_movement.py`, its vocabulary and support matrix in
`models/knowledge/review_external_movement.py`, and its cases in
`mcp/tests/test_review_external_git_movement_read.py`.

Three facts belong at repository altitude rather than on any one route. **A replaced identity
outranks both carried comparison and recorded rebinding**, because neither survives the branch
being rewritten under it, so the review reports `stale` and names the identities that were
replaced. **An unperformed comparison is its own state, `not-measured`**, and is deliberately not
`stale`: no movement was observed, and `stale` additionally disables submission, a consequence the
absence has not earned. And **the boundary never gates**: on the closeout preview, the closeout
apply and the integration result it is an attached statement that refuses nothing, leaving the
closeout door's own source-lineage checks as the only checks on that transaction. There are no
global Git hooks and no replacement Git layer; `docs/reference/worktrees-c09.md` carries the
support matrix, including the four transition shapes this system does not reconcile.


## 260921-ICR-L15 Measured assessment currentness

`260921-ICR-L15` (`ICR-R15@v1`) makes an assessment's currentness a **measured fact** rather than the
presence of a mapping. A stored assessment's binding is reported in one of four states — `not-measured`,
`current`, `stale`, `unavailable` — and the read layer's subject status adds `none-recorded` (the
unassessed subject) and `unresolved` beside them, `not-measured` being requirement 4.3's fifth state: a
record nobody measured is reported as exactly that, never promoted to `current` and never demoted to
`stale`. The rule lives in one place, `models/lifecycles/review_assessment_binding.py`'s
`measured_binding_status`, over a measurement whose **keys are its coverage**: a failed measurement is
`unavailable`, a measured disagreement is `stale` (the shipped `disputed_dependencies` comparison's own
answer), a completed measurement that covered every declared identity and disagreed nowhere is
`current`, and everything else — including an empty measurement, which is measured and covers nothing —
is `not-measured`. `assessment_state_for` has no argument meaning "assume current" or "assume stale",
and `SubjectAssessmentState` re-derives its counts and status from the entries it summarises, so a
summary that contradicts its own records is unrepresentable.

## This Repository's Published Knowledge Now Has One Declared Location, And The Ordinary Write Side Reaches It

A repository-level fact rather than a route one, recorded here because it is the spelling two otherwise
unrelated routes have to agree on. The ordinary **read** route declares one published dataset location —
`<memory_root>/knowledge.sqlite`, where the memory root is the canonical external memory root with no
enclosure in scope and a task's memory **worktree** inside one — and, since `260921-ICR-L20`
(`ICR-R20@v1`), the ordinary **write** route publishes there: the curator's ingest run selects that
location with `--publish`, resolving it through the read side's own declaration, and reads the published
identity back through the reader's owner. A caller-named `--publish-to` remains the other selection and
the two are mutually exclusive; a run that names no destination and passes no `--publish` still commits
without publishing, which is why the destination is a *selection* rather than a default.

Three consequences a reader of this overview should carry, because they are what the change is for:

- **One spelling, owned once.** The location is computed in `application/published_intent.py` and
  consumed by both sides, so the place a curator writes and the place a later task's planner selects
  cannot drift apart by two conventions agreeing today.
- **A successful process exit is not a publication claim.** The run's report carries the destination it
  selected, the publication owner's own result and an independent read-back of the location
  (`confirmed` / `mismatch` / `unavailable`); a refused publication establishes nothing and is read back
  not at all.
- **The knowledge batch and its publication keep their existing owners.** `--commit` is the
  knowledge-batch write word and acquires no Git or acceptance meaning; the mounted `knowledge_change`
  tool still refuses every record kind and names the real write route — since `260921-ICR-L32`, **both**
  shipped CLI entry points that reach the one writer (`knowledge-ingest` on a leaf enclosure's ordinary
  route and `knowledge-bootstrap` on the taskless repository-foundation one), where `ICR-R20@v1` could
  name only the first because the second did not exist yet.

- **The declaration both sides resolve, and the constant that names the file.** [25]
- **The write side's route: the declared location, the admission derived from the run's own baseline, and the read-back.** [26]
- The CLI selection that reaches it, its refusals, and the report line that completes the admission from the run's own report. [27]
- The context rule that decides *which* memory root the location is, with no fallback between the two. [28]
- **The canonical carrier instructions that now tell the curator seat to invoke that route.** [29]
- The mounted refusal that names it, and the operation document that carries it. [30]

## Memory Preparation And Final Certification

Memory quality is useful before gate admission: a contract-scoped full request observes the exact code/memory pair and candidate trees, runs quality checks, and builds an enclosure-local curator worklist covering repair findings, commit-owned findings, missing onboarding, stale route indexes and source drift. Use that worklist to perform the authorized semantic onboarding updates before entering the expensive certification sequence. It is not necessary to obtain code-gate certificates merely to discover the memory work.

The tool surface those steps use states its own inputs. The curator-coherence request now refuses by
naming the exact missing member: `publish` requires nine non-`None` request members, two of which
(`semantic_requirement_revision`, `delivery_attempt`) `prepare` does not derive and does not echo, and
the refusal names them instead of naming a prose category. `prepare` states the complete input set from
the same declaration, and a `status`/`prepare`/`validate` refusal names the publication-only field it
received. This matters to this repository's own record rather than only to callers: two leaves of the
`260915-KS` master read the old refusal as an impassable tool defect and carried an unpublished
coherence authority as an external blocker (`notes/DISCLOSURES.md` D-11).

Preparation does not grant a final certificate. The interactive catalog projection explicitly lacks affected-closure and code-prefix authority. The existing prepared-memory adapter consumes the selected four original code terminals and exact prepared candidate, runs the final memory producer, publishes its physical result and selects Gate 5 through the normal owner. Finalization requires that selected original fifth certificate and its bound memory inputs. MCAR continues from these existing owners; this overview does not declare the unfinished master accepted or create a second final proof path.

Candidate capture uses an isolated add-all index and stable observed HEAD, leaving the user's real index unchanged. External-memory identity binds configured repositories, worktree roots, branches, bases, onboarding root and contract digest; the ledger path is informational and excluded from candidate authority. A changed pair or candidate must refuse stale publication. Metadata stamping and cache refresh cannot substitute for substantive memory repair.

## Development And Certification Policy

Ordinary Python development is supported directly through `mcp/.venv/bin/python -m pytest`; four workers run the isolated unit population. `-m integration` selects the small real-boundary population and `-m ""` selects both. Focused file/node execution, including serial debugging, is valid development work and does not acquire certification authority. The repository declares budgets of **4,000 unit and 1,000 integration** parametrized collected cases (`unit_case_budget` at `pyproject.toml:278` and `integration_case_budget` at `:279`; raised from 3,000 / 600 by the `260918-TSIP-L13` budget-and-landable-closeout leaf on 2026-09-20 under a second direct developer decision, that pair having been raised from 2,300 / 400 by the `260918-TSIP-L7` agreement leaf under a direct developer decision — the first raise on this line that is a **policy** rather than a measurement, because every increment before it was earned from a collected population: 1,500 / 400 by the `260915-KS` master's owning seat, then 2,000 and 2,200 on the merged line, then **2,300** by `260915-KS-L21` over its measured 2,206-case candidate). Extend or consolidate distinct behavior protection before adding cases; do not restore deleted matrices, private-branch tests or unused fixture machinery because an old milestone names them.

Coverage, including changed-line coverage, is diagnostic only. No percentage floor requires additional tests. Production-only CRAP retains 20 as a review trigger, not a delivery blocker; tests and verification support are excluded. Lint, formatting, typing, structural rules and test failures still enforce. Diagnostic-tool execution errors remain visible failures distinct from metric findings. There is no coverage baseline, score-exception registry or ratchet.

Only genuine Dagger admission and the existing lifecycle owners can issue immutable candidate-bound certifying evidence. A host pytest pass, copied report, green helper result or use of Dagger alone is insufficient. Reuse the existing shared engine and preserve process identity, disposable state, credential isolation, exact candidate and publication ownership. Full-suite execution and whole-master independent review belong to the master aggregation boundary under the current execution policy; this overview does not impose either on every leaf. Focused development evidence remains useful without pretending to be final acceptance.

## Historical Frontend Quality Milestone

The earlier frontend milestone introduced broader static measurement and a changed-lines coverage floor. The floor is retired by current diagnostic-only policy; static, type, build and behavior failures remain meaningful. Historical population counts are not current requirements.

## What This Repo Is

`agents-remember` is the source repository for the Agents Remember workflow system. It defines the doctrine, skills, MCP tools, task workflows, and design references that agents use to maintain durable onboarding knowledge beside code. Durable memory is reached through three retrieval substrates routed by `c-04-retrieval-strategy-router` skill: **by path** (a source file's deterministic one-to-one onboarding unit, verified against Git history), **by meaning** (semantic memory search over the onboarding), and **by relationship** (a code-relationship graph). By-path notes are the core and need no provider; meaning and relationship are served by opt-in Docker providers (GrepAI, CodeGraphContext) and return candidate routing evidence, not proof. Overviews and entity catalogs use route scopes or curated evidence fingerprints before an agent relies on them. The earlier sidecar-only, anti-retrieval positioning (no embeddings / no vector store) predated those providers and has been retired from the public spine and from this overview's framing.

The current checked-in guidance places durable memory in a **memory repository of its own** and keeps `ar-coordination/` as local coordination. Selective external memory repos under `ar-coordination/memory-repos/ar-<repo>/` are the only supported topology, with `disabled` available for a task that carries no memory lane; the former repo-local `ar-memory/` internal mode was **removed from the product** and is now refused by name with its exact artifact rather than substituted or defaulted. `c-08-ar-coordination-context-resolver` skill exposes that split through `code_repository_name`, `code_repository_root`, `memory_root`, and `coordination_root`; `c-09-git-worktree-manager` skill owns worktree lifecycle mutation, ordinary series integration back to source branches, and the narrowly policy-gated branch-addressed landing of an explicitly selected leaf implemented without an enclosure. It also documents `task_reopen` — reopening a fully landed leaf task in place under its exact leaf id — while `c-10-adopt-memory-baseline` skill provides the adoption path for existing external-memory onboarding that needs adoption into attributed memory history.

The provider runtime guidance now routes through the MCP/package boundary:
MCP settings outside the coordinator are authority, coordinator files can only
teach the model what to ask for, and provider runtime state lives under one
coordinator provider root plus a central log root. Managed provider containers
run memory-capped since L12 (watchers 512m; a runaway OOM-recycles itself instead
of exhausting the host). Managed providers use
`providers/runners/` for provider instances, `providers/data/` for durable
provider database data, `logs/mcp/` for MCP transcripts, and `logs/providers/`
for provider operator logs/status/setup summaries. `providers/_bin/` and
`providers/_venvs/` are not managed executable contracts. Providers that need
databases, native binaries, or daemons should use Docker-wrapped managed mode;
GrepAI uses a workspace-mode PostgreSQL/pgvector Docker backend for multiple
memory roots, and CGC uses a Docker runner plus FalkorDB Docker backend for
configured code roots.

## Feature Inventory

This is the maintained current-state inventory of the system surface. When a
feature is added, removed, renamed, or moved between skills, MCP tools, package
modules, runtime assets, or public docs, update this section in the same
onboarding pass.

| Feature | What It Offers | Primary Surface |
| --- | --- | --- |
| Path-derived onboarding memory | Deterministic Markdown memory beside source files, plus route overviews and repo entity catalogs for larger scopes. | `README.md`, `onboarding/`, `c-05-create-or-update-onboarding-files` skill |
| External memory roots (and the disabled mode) | Selected external memory repos under `ar-coordination/memory-repos/ar-<repo>/` are the **only supported topology**, plus `disabled` for a task that carries no memory lane and computed `memory.md` consumer caches derived from committed code/memory attribution. The former repo-local `ar-memory/` internal mode was **removed from the product**; a contract, settings file or memory root that still records it is reported with its exact artifact and refused with status `memory-mode-unsupported`, naming the supported set and the route out — never substituted with `external` and never migrated automatically. `repo-sidecar` survives only as a per-artifact storage placement, not as a memory topology. | `c-00-initialize-memory-repo` skill, `c-08-ar-coordination-context-resolver` skill, `c-09-git-worktree-manager` skill, `c-10-adopt-memory-baseline` skill, `kernel/memory_mode.py`, `kernel/memory_ledger.py` |
| Context resolution and startup packets | Resolved code, coordination, memory, onboarding, task, temp, ledger, storage, path-rule, cross-repo, provider-summary, worktree, Git, and optional drift facts through compact `ContextPacketV2`; detailed provider state is intentionally excluded. | `c-08-ar-coordination-context-resolver` skill, `resolve_context`, `context_packet`, `ContextPacketV2` |
| Memory quality control | Task-start drift classification, closeout memory quality, new-file missing-onboarding checks, overview/entity fingerprint checks, and update-history style checks. | `c-02-memory-quality-control` skill, `drift_check`, `memory_quality_check`, `check_missing_onboarding` |
| Retrieval routing | Semantics, Relationship, and Intent routing across provider accelerators, route indexes, onboarding, and bounded source confirmation. Since 260921-ICR-L19 the Intent route also reads the repository's **published intent** — the invariants a previous task already recorded about the requested paths, at their exact snapshot and without requiring a task — through the ordinary `read_ar_files` call. | `c-04-retrieval-strategy-router` skill, `overview.index.json`, GrepAI tools, CGC tools, `read_ar_files` |
| Onboarding bootstrap and slice maintenance | Repo bootstrap, route-local overview creation, evidence packs, file cards, onboarding waves, curator review artifacts, and route/slice refresh or deletion cleanup. | `c-03-repo-bootstrap` skill, `c-05-create-or-update-onboarding-files` skill |
| File and entity onboarding maintenance | File-level sidecars, inline onboarding adapter rules, repo entity catalogs, deterministic entity fingerprints, reference health checks, and generated route indexes driven by one Git/path-rule census. | `c-05-create-or-update-onboarding-files` skill, `route_index_refresh`, `kernel/route_index.py`, `kernel/route_index_census.py` |
| Findings capture | Confirmed current-state findings are routed to durable task-local artifacts and can be propagated into onboarding after verification and approval. | `c-01-findings-capture` skill |
| Workflow modes | The `l-01-agent-lifecycles` architect lifecycle's build decision at `decide`: a research-only exit for no-code answers, otherwise a `w-02-light-task-workflow` skill task — chat is never a build route, so one-session edits take the minimal artifact — escalating to a master + light sub-task series for larger phased work (the retired heavy workflow and the retired chat build are no longer modes). | `l-01-agent-lifecycles` skill, `w-02-light-task-workflow` skill |
| Agent lifecycles (one per role) | Developer-requested multi-agent series run through the unified `l-01-agent-lifecycles` skill. Spawn-role env and fresh briefs select role seats; otherwise free chat remains a launcher. Ordinary role-shaped work compiles the canonical architect brief and calls `dispatch_agent` once on the sprint document; an explicit developer-declared task-seat takeover instead targets the named role at its canonical altitude. The identity-free call uses target-document/role-altitude authority; after handoff, hosted seats use plane identity and direct-child scope, with no plane-to-ambient fallback. Architect owns the initial plan loop and recommends the developer-approved strategist when the evidence-backed topology/classification reasoning is missing or stale — graph absence alone is not a trigger. A reviewed graph-less atomic-sequential choice is valid, but its runtime admission is no longer exclusive: the activation record is keyed per canonical series contract, so a master that is `reconciling` holds only its own activation until its exact code/memory sources are current, and two atomic masters that share one protected source pair keep independent records rather than pausing one another. A sanctioned strategist skip transfers the complete dependency, route, seam, classification, priority, and topology-reasoning duty to the orchestrator, which adopts a graph only when present. One effective priority governs a candidate (candidate override, otherwise master default), while the orchestrator retains portfolio comparison. Graph adoption from a graph-less sprint first attaches every master, then publishes one complete nodes-plus-evidence-edges batch. Exact proposed completion candidates are reviewed before refs move; handover cites canonical candidate/code ancestry/memory ancestry/per-leaf ledger refs rather than copying maps, and failed review routes to a leaf rather than an integration workbench. | `l-01-agent-lifecycles` skill, `skills/l-01-agent-lifecycles/templates/architect-brief.md`, `skills/l-01-agent-lifecycles/roles/architect.md`, `skills/l-01-agent-lifecycles/roles/orchestrator.md`, `skills/l-01-agent-lifecycles/roles/reviewer.md`, `system/git-workflow.md` |
| Approval-gated closeout | Applicable authority gates for implementation, worktree-backed closeout, memory refresh and memory quality: standalone/final work uses explicit developer approval, while subordinate accepted-series work can proceed under recorded delegated series authority. Closeout itself is worktree-only — the retired direct current-checkout closeout path remains removed (issue #62). The separate `direct_landing` operation is only the explicitly selected delivery route for a leaf implemented without its own enclosure; ordinary master/series closeout and integration never require `directExecutionEnabled`. Since 260731-EFA-L4, where the quality gate runs it first resets the index and stages the whole task worktree, so the gate is shown the commit's content rather than only the paths already tracked; two refusals guard that step (not a task worktree, or unresolved merge conflicts). Body/history gates reject header-only or unmarked history-only onboarding refreshes for changed sources and their nearest-governing route overviews; explicit `No content impact:` / `No route impact:` Update History markers attest reviewed-no-impact and are surfaced in closeout payloads. | `c-09-git-worktree-manager` skill, `c-12-closeout` skill, `worktree_closeout_*`, `direct_landing` |
| Worktree lifecycle | Worktree start, attach, status, **stop**, closeout preview/apply, integration, lifecycle finalization, cleanup, task contracts, replay/fast-forward integration, and external-memory compatibility checks. The stop is its own public verb — `worktree_pause` — and it publishes nothing: it releases the master's atomic-series activation selection and hands the turn back, while `worktree_checkpoint_landing` remains the separate, explicitly requested publication of an unfinished master. The two are separate registered tools with separate descriptions and neither is reachable from the other. Atomic implementation admission uses one disposable activation record per canonical series contract: it publishes this contract's own `reconciling` state and exposes it as active only after sync, so atomic masters that share one protected code/external-memory source pair never share that state and a foreign master is never a waiting reason. Sync evidence survives in the enclosure-root journal and pinned Git refs; real conflicts are retained for staged `continue`, while explicit `cancel` restores operation-owned pre-sync heads. | `c-09-git-worktree-manager` skill, `lifecycle_finalize_task`, `worktree_*`, `worktrees/` |
| Observable session lifecycle | The observer event log and projection retain trust provenance, lifecycle status, metrics, attention and task context. Public tool completion passes through application-owned enrichment and the single model finalizer; `nextStep` is bounded and optional, rather than attached unconditionally to every response. Lifecycle gate decisions and turn-end notification have distinct contracts. | `agents_remember.observer`, `application/tool_response.py`, `models/tool_response.py`, `mcp/tools/base.py` |
| JSON-primary task documents | The `ar-task-document/v1` document is the source of truth for a task's plan + progress and `task.md` is its deterministic render. Sprint documents carry the canonical `executionGraph`; master documents carry explicit `executionNature` (`organizational` or `atomic`). A sprint without an `executionGraph` uses the atomic-sequential default, which describes the sprint's shape — every commanded master executes atomically — and serializes nothing; its runtime admission is this contract's own per-contract activation record rather than a task-authoring lock, permanent series lane, or shared per-source-pair slot. Task mutations publish their authored state; field classification invalidates closeout evidence for semantic/readiness changes, while observation-only updates do not invalidate task intent. `task_doc.author_execution_graph` bootstraps or edits the graph, and there is no implicit inference or compatibility reader. The `task_doc` MCP tool validates cross-document graph references, authors/replaces documents, and republishes the affected JSON/Markdown set atomically; observer projection exposes the same topology. | `agents_remember.tasks`, `task_doc` tool, `tasks/` route overview |
| Gate control plane | The durable, attributed record of decision points on a lifecycle (closeout/integration/cleanup approvals, agent questions, alarm acks): an append-only `ar-gate-record/v1` `GateRecord` + `GateStore` co-located with the observer event log. The public agent-facing MCP junction is `lifecycle_gate`: it creates the typed durable gate, blocks the active lifecycle with the developer-facing ask, waits for a developer decision or gate-specific inbox response, and can carry `required_decision`; lower-level gate payloads/stores remain the implementation substrate. `controlplane/enforcement.py` binds `worktree_closeout_apply` to a developer-approved `closeout-approval` gate, or to an opt-in delegated orchestration approval that passes the `gate_policy.py` rules; model self-approval and owner lifecycle self-approval remain non-binding. The default policy is all-human, human-pinned integration/push/cleanup gates are not configurable away, and delegated decisions can require reviewer-verdict evidence refs that surface on gate records/projections. Task 19 adds the single-current-gate invariant (new lifecycle gates expire older open lifecycle gates) plus targeted dashboard decisions via `gate_decide_for_lifecycle`. Lifecycle skills now raise `lifecycle_gate(kind=...)`, handle the returned developer decision or operator-inbox message from that public junction, and clear with `lifecycle_resume`, split across plan/worktree/closeout/push/integration/cleanup/agent-question gate kinds. Dashboard gate projection is live and now renders human-readable previews with raw JSON as diagnostics. | `agents_remember.controlplane`, `lifecycle_gate`, `gate_*` stores/tools, `controlplane/` route overview |
| Dashboard serving layer | `agents-remember dashboard` serves projection snapshots/deltas, raw retained events, typed operator actions, the packaged frontend, and hosted harness sessions. The serving package composes protocol, catalog, submission, conversation and bridge authorities as well as HTTP/WebSocket transport. Controlled chats use a structured conversation surface with a read-only diagnostic line log. Optional settings discovery, supervised daemon start/status/stop, and version-aware daemon reconciliation remain CLI/runtime concerns. | `agents_remember.serving`, `agents-remember dashboard`, `serving/overview.md`, `dashboard/src/overview.md` |
| Dashboard frontend | The root React dashboard exposes Operations and the canonical Chats cockpit, plus task, requirement, artifact, lifecycle, event and provider views. Controlled sessions submit through the typed submission authority and render structured conversation history; inspector tabs retain evidence and capabilities without inventing missing telemetry. Grammar components and route-local overviews own the detailed current layout and behavior. Earlier slice-by-slice frontend descriptions are retained below as historical development context. | `dashboard/src/overview.md`, `dashboard/src/panels/overview.md`, `dashboard/src/data/overview.md`, `dashboard/src/grammar/overview.md` |
| Sessions live set controls (260715-FEUI-L4) | The Sessions cockpit now re-fetches the exact live-session capability snapshot, derives effort only from the selected model row's session-settable options, and keeps requested, pending, echo-evidenced effective, and readback-confirmed values separate across all five SetResult acceptances. Model+effort changes serialize model → evidence/readback → effort; unknown/queued outcomes promote by readback; shared worded chips, per-seat ledger/rail attention, collapsed background toasts, cycle-effort commands, and polite/assertive live regions carry the evidence. | `dashboard/src/data/{sessionCapabilities,setAcceptance,pairChange,setClient,setChips,setControlsCopy,announcer}.ts`, `dashboard/src/panels/session-cockpit/` overview |
| Hosted chat task attachment | The operator HTTP `attach-task` route changes a hosted session’s canonical `taskDocumentRef` and role binding subject to catalog, role and altitude validation. Agent-facing creation and messaging use structural task/role addresses; the old public `attach_terminal_session_to_leaf` tool is retired. | `serving/_app_terminal_routes.py`, `serving/response_contract.py`, `serving/terminal_catalog.py` |
| Agent-facing session dispatch | One MCP tool — `dispatch_agent` — is the sole public spawn surface for plane-hosted seats and identity-free ambient launchers; `spawn_agent_session` is retained only as an internal primitive and wire identity. Caller kind is derived from process context, never a request field: plane identity selects seat/direct-child authority and cannot fall back to ambient, while absent identity selects canonical target-document and role-altitude validation. Ordinary ambient work targets the sprint architect; only an explicit developer-declared task-seat takeover targets another named role at its canonical altitude. Both modes submit the same target document, role, complete brief, and optional label, then share settings resolution, creation/reconciliation, readiness, exact brief pinning, rollback, and canonical seat publication in one transaction. Settings resolve one complete typed harness/model/effort selection; role-table `dispatch` and `tools` rows describe structural authority/capability rather than override keys. The own adapter discovers its token-free per-install/account catalog, validates effort under the selected model, and applies native Claude/Codex/Pi initial configuration before the real vendor session starts. The same exact-session bridge serializes `set_model` and `set_effort` with prompt submission and returns a normalized `SetResult` whose acceptance is one of `echo-verified`, `immediate`, `queued`, `unknown`, or `unsupported`. Spawn model/effort env stays provenance, explicit free-form launch/session controls remain separate, caller spend overrides refuse before side effects, and neither initial nor mid-session selection is composer-pasted. Each spawned session is its own harness process, and dashboard and agent-facing launches still share one opener. | `dispatch_agent`; `spawn_agent_session` (internal primitive), `skills/l-01-agent-lifecycles/templates/architect-brief.md`, `serving.harness_launch`, `serving.harness_control_runner`, `serving.harness_control_bridge`, `serving.harness_submission_authority`, `serving.terminal_opener`, `operator_inbox_*`, `mcp/tools/terminal.py`, `models/terminal.py` |
| Daemon harness capability and control API | The serving daemon exposes the own-adapter contract without ACP transport: dynamic token-free pre-session catalogs use an install-aware bounded cache with explicit auth refresh; terminal open accepts an optional complete native model/effort pair; exact live sessions advertise and return honest model/effort `SetResult` evidence; whole-message submit and same-id reconciliation use the native control socket with no paste fallback. Live reopen reports immutable process truth or conflicts, failed refresh quarantines stale data, duplicate request ids are idempotent, public responses omit adapter-private raw payloads, and liveness is established before 404/409 support classification. | `serving.harness_capability_catalog`, `serving.harness_control_api`, `serving.harness_control_client`, `serving.terminal_opener`, `serving.app` |
| Reliable controlled-session submission (260715-FEUI-L5) | One `HarnessSubmissionAuthority` per bridge generation owns prompt/model/effort ordering, immutable request/source/payload idempotency, atomic queued-withdraw versus dispatch, exact full-operation-ref completion, early-terminal dominance, raw-free status, and bounded privacy-aware retention. The dashboard's shared CodeMirror composer keeps one epoch/id/text through retry/reconcile, treats only the exact pre-dispatch certificate as retry-safe, and implements authoritative Alt+Up pop-back with revision-CAS recovery. Claude, Codex, and Pi dispatch now under guarded write seams; no adapter/native queue or PTY-paste fallback is authority. | `serving.harness_submission_authority`, `serving.harness_control_{api,bridge,client,models}`, `serving.harness_submission_authority`, `dashboard/src/data/{submitMachine,submitClient,submissionLifecycleClient,submitRetention}.ts`, `dashboard/src/panels/SessionComposer.tsx` |
| Sessions inspector and status integration (260715-FEUI-L7) | The Sessions cockpit completes its end-to-end operator audit with stable-mounted accessible Evidence / Capabilities / Bus tabs and a persistent StatusLine. Evidence retains explicit-mark-seen set outcomes and terminate/retire residuals after source-row removal; exact-session capability truth stays separate from pre-session launch catalogs; the fleet-global pending Bus preserves entry-keyed reply state across filters, virtualization, and hidden tabs, and reverse replies address only the projected sender without consuming the source. The status footer keeps its contractual fact order and literal empty UA-5 context/cost slot rather than inventing telemetry. | `dashboard/src/panels/session-cockpit/{SeatInspector,EvidencePane,CapabilitiesPane,BusPane,BusDeveloperReply,VirtualizedInspectorList,StatusLine}.tsx`, `dashboard/src/panels/session-cockpit/` overview |
| Canonical Chats cockpit and hardening (260715-FEUI-L8) | One product-facing `Chats` destination now uses the keep-alive session cockpit; the old Chats component, session-list grouping, and separate Sessions navigation are retired. Operations remains the default and RailChat remains contextual. The inspector defaults closed, is toggleable and responsive without losing deliberate intent; authoritative launch, attach, highlight routing, landed cleanup, ended/restored states, accessibility, scenario coverage, and performance/fetch tripwires are pinned end to end. At FEUI-L8 controlled sessions still exposed the runner line-log in xterm because UA-1 structured transcript/history authority was not yet implemented; **260718-CHATS-L4 supersedes that** — controlled sessions now default to the structured conversation surface and the line-log is demoted to a read-only diagnostics drawer (see the 260718-CHATS-L4 narrative below). | `dashboard/src/panels/session-cockpit/` overview, `dashboard/src/data/` overview, `docs/design/dashboard/{scenario-catalog,session-cockpit-upstream-register,session-cockpit-closeout-evidence}.md` |
| Agent orchestration communications | Durable messages address canonical task/role seats and survive vacancies until a matching generation can receive them. Hosted delivery uses the controlled harness bridge; physical delivery or a transport acknowledgement alone is not task completion. Consume attribution and terminal message state remain durable. Runtime session identifiers are private correlation data. | `mcp/registration/orchestration.py`, `serving/inbox_delivery.py`, `controlplane/` |
| Event River lifecycle task labels | Event River readable history rows translate lifecycle-bound activity into task-facing context. When a retained event still has a lifecycle id but its live lifecycle projection is gone, the formatter uses projected task documents to show the task title before falling back to raw enclosure or lifecycle ids. The panel waits for raw-stream hydration before showing an empty feed and renders all retained rows it receives; backend lifecycle retention owns the cutoff. | `dashboard/src/panels/eventSummary.ts`, `dashboard/src/data/taskIdentity.ts`, `dashboard/src/panels/EventRiver.test.tsx` |
| Authoritative browser session open | Every dashboard raw or harness create entrance crosses one `POST /api/terminal` client, validates exact request/response identity, and materializes only the accepted server row. Network, HTTP, protocol, identity, or server-declared failure creates no registry row, focus change, readiness/submit transition, or dependent context delivery. | `dashboard/src/data/terminalOpen.ts`, `dashboard/src/data/sessions.ts`, dashboard data/panels/session-cockpit overviews |
| Runtime and skill installation | MCP-owned install of coordinator `AGENTS.md` templates, packaged skills, system defaults, provider defaults, optional benchmark fixtures, and harness skill layouts. | `runtime_install`, `skills_install`, `install/`, `package_data/runtime/` |
| Harness starter packages | Harness-native first-run packages for Claude Code, Codex, Cursor, Antigravity, VS Code + Copilot, Hermes, Pi.dev, and OpenClaw. Each package carries MCP settings templates, skill folders, and either startup hooks or always-on instruction files that load the coordinator first-action directive. | `.claude/`, `.codex/`, `.cursor/`, `.agents/`, `.github-vscode/`, `.vscode/`, `.hermes/`, `.pi/`, `.openclaw/`, `docs/install/` |
| MCP server and authority settings | Installable stdio MCP server with trusted settings outside the coordinator root, allowed repo/provider scopes, timeout caps, transcript roots, and path containment. Since 260731-EFA-L3 it also **starts with no network egress**: the `o200k_base` tokenizer vocabulary ships inside the package under `package_data/tiktoken/` instead of being downloaded while the tool surface imports, so a fresh container, an offline machine, and a hermetic CI job can all start the server. | `agents-remember-mcp`, `mcp/config.py`, `mcp/server.py`, `models/tokens.py`, `package_data/tiktoken/` |
| Public MCP response contracts | Pydantic models for every public MCP tool response, registry coverage for the tool surface, compact strict contracts where the repo owns shape, flexible envelopes where provider/service-native details are intentionally passed through, and token metadata fields for later cost accounting. | `mcp/src/agents_remember/models/`, `PUBLIC_TOOL_RESPONSE_MODELS`, `test_models.py` |
| Provider lifecycle and discovery tools | Docker-managed GrepAI memory search/trace, CodeGraphContext symbol/caller/callee/dependency/complexity/visualization queries, compact provider status, dedicated provider diagnostics, watcher lifecycle, and current-state snapshots. Readiness is content-gated (2.5.0/2.5.1): graph/workspace content probes drive `indexed`/`indexing`/`empty`/`backend-unreachable` states for both providers, empty/unreachable targets degrade the global packet `ok`, crash-looping containers are not ready, and healthy-but-busy targets surface in the compact summary's `indexing` list. Provider launch is contained since 260707-HFX-L1: launch-capable operations (watcher start/restart/index rebuild, one-shot query runners, worktree provider setup, benchmark provider synthesis, the install rebind) re-read the on-disk MCP authority fail-closed — the boot snapshot is not launch authority, so `providers: {}` on disk is a live fleet-wide kill-switch — while stop/status/cleanup stay ungated; provider setup is serialized fleet-wide (one non-dry-run prepare at a time); and the dashboard daemon samples per-container containment metrics (label-discovered, read-only, dockerless-safe) that ride `provider_status`. | `provider_status`, `provider_diagnostics`, `provider_watchers`, `grepai_*`, `cgc_*`, `providers/`, `providers/metrics.py` |
| Tool response token budgets | Verbose tools (`runtime_install`, `provider_diagnostics`, `provider_watchers`, carryover plan/apply) keep compact outcomes inline and file bulk diagnostics under `temp/tool-reports/<tool>/` with an inline `reportPath` (keep-last-5 / 7-day write-time prune, secret redaction); budget tests are the regression line (2.5.1/2.5.2). | `mcp/tool_reports.py`, `compact_*_payload` builders, `test_tool_response_budgets.py` |
| Memory baseline adoption | Adoption of existing external-memory onboarding into attributed memory history after drift/status review; the ledger is a rebuildable consumer view. | `c-10-adopt-memory-baseline` skill, `memory_baseline_*`, `memory/baseline.py` |
| Branch memory carryover | Carry richer onboarding from a source branch into official memory only after the corresponding code has landed. Candidates cover file sidecars and route overviews (route-keyed, `kind`-tagged): overviews whose route covers a landed path auto-carry only when branch and official content are identical (metadata re-verification), otherwise they are always review-required; official-side `overview.index.json` files are regenerated after carry — never copied — guarded on a clean official-ref checkout. | `c-11-memory-carryover-from-branch` skill, `memory_carryover_*`, `memory/carryover.py` |
| Branch-gated cross-repo context | Optional cross-repo context inclusion guarded by configured branch and memory-ledger checks. | `c-08-ar-coordination-context-resolver` skill, `crossRepo.allow` |
| Benchmark harness | Package-owned Codex benchmark fixtures, workspace preparation, paired source-only versus memory-enabled runs, JSONL/result capture, and metric summaries. | `codex_benchmark_prepare`, `codex_benchmark_run`, `benchmarks/` |
| Source quality tooling | Ordinary isolated pytest supports development; the existing pinned Dagger/lifecycle publication is the sole certifying authority. Coverage is diagnostic and production CRAP20 prompts review without blocking. Current master execution uses focused development checks and final aggregation/review; historical per-leaf acceptance procedures are not imposed here. Exact candidate, runtime and immutable publication bindings remain required. | `docs/design/python-pytest-bootstrap.md`, `docs/design/python-test-evidence.md`, `mcp/certification-profile-v1.json` |
| Self-hosted harness configuration | The nine dogfooded harness configuration trees (`.claude/`, `.codex/`, `.cursor/`, `.github-vscode/` + `.vscode/`, `.hermes/`, `.openclaw/`, `.pi/`, `.agents/`) are **generated from one source and checked**, not eight independent copies. `scripts/harness/` holds the fragment libraries and shared bodies; `scripts/sync-harness.py` fans out 45 files three ways (verbatim, composed body + per-harness framing, and programs assembled from named fragments with derived imports). `--check` verifies generated projection drift. `scripts/harness/README.md` is the ruled classification of genuine per-harness requirements versus drift. | `scripts/sync-harness.py`, `scripts/harness/` |
| Public docs and harness guides | User-facing setup, concepts, architecture, workflows, references, guides, and install notes for Codex, Claude Code, Cursor, Antigravity, VS Code Copilot, Hermes, Pi, and OpenClaw. | `docs/`, `README.md` |
| Canonical runtime and skills asset sync | Root runtime asset folders (`agents-md-files/`, `benchmarks/`, `providers/`, `system/`) are canonical editable assets synced into MCP package data by `scripts/sync-runtime.py`; root `skills/` is the canonical skill tree synced into package data plus every harness starter skill folder by `scripts/sync-skills.py`. Both carry `--check` and both local hook tiers run those deterministic checks. The pull-request-only GitHub workflow invokes `_gate.sh targeted`, so generated-copy drift is checked without running tests or Dagger. The production projection owners remain separate from the reduced retained test population. | `scripts/sync-runtime.py`, `scripts/sync-skills.py`, `.githooks/_gate.sh`, `.github/workflows/quality-checks.yml` |
| Dashboard bundle release build | The built cockpit (`dashboard/dist/`) is placed into `package_data/dashboard/` by `scripts/sync-dashboard.py`. This is a **release build step, not a sync check**: the bundle is a generated artifact that is **not in version control** (master decision OQ6, 2026-07-31), so there is no `--check` mode and no hook runs it. The release job builds the frontend, runs the placement, packages, and asserts the wheel and sdist both carry the bundle plus its `dashboard.fingerprint` sidecar. Placement refuses an absent `dist` and refuses a `dist` that does not carry the current build-input fingerprint Vite compiled into it, so it cannot stamp over a stale artifact. | `scripts/sync-dashboard.py`, `.github/workflows/publish-mcp-to-pypi.yml`, `dashboard/vite.config.ts` |

Task 10 external-chat inbox current state spans three route families: the control-plane inbox
(`OperatorInboxEntry` / `OperatorInboxStore` plus the `operator_inbox_*` MCP tools), the dashboard
serving endpoint (`POST /api/operator-inbox`, trusted developer/dashboard attribution), and the
dashboard Gate Respond fallback (`GateResponder` calls `data/operatorInbox.postOperatorInbox` when no
hosted chat session is attached). Hosted chat injection remains preferred; the inbox is the pull-based
return channel for external agents that cannot receive direct dashboard injection.

Task 23/24 changes the lifecycle of those gate/inbox interactions: prompts, responses, pending pickup
signals, and attention-queue gate rows are disposable interaction data. Explicit dismiss/clear paths
delete immediately; inbox consume records a terminal audit snapshot, and passive TTL cleanup removes
it at the 24-hour interaction window. The only durable lifecycle records are
the task/worktree documents, commits and contracts. Consumer ledger rows are recomputed from attributed Git history.

Task 31 updates the root dashboard/provider current-state story: live dashboard projection now refreshes
provider current-state before serving snapshots, worktree provider stacks can be inspected from their
isolated runtime settings, and Engine Room renders expected provider roles as observed, configured-only,
failed/degraded, or missing instead of letting empty provider containers imply no expectation. The detail is
route-local under `mcp/`, `mcp/src/agents_remember/observer/`, `mcp/src/agents_remember/serving/`, and
`dashboard/src/panels/engine-room/`.

Task 29 S7 updates the root Event River and attention-queue story: raw events are retained by the
backend lifecycle policy and the frontend no longer hides rows with its own short cap, `/api/events`
emits a ready marker after retained backlog replay, actionable-drift notices name the affected
repository/memory pair, and only actionable drift can be dismissed without a lifecycle/worktree target.
The former Lifecycle Flow tab is hidden from the cockpit; `FlowTab.tsx` remains dormant source.

HFX2-L12 updates the root runtime-scaling story for mission-control operation: supervisor signal and
expectation stores compact on read while escalation/cooldown budgets bound repeated work; raw Event
River data is startup-compacted and served through bounded/offloaded paths; projection hot paths cache
lifecycle, task-document, gate, and Git-status reads while guarding task-document body payload size;
terminal catalog/liveness reads batch and compact active sessions; and provider metric/degradation logs
compact instead of growing without reclamation. Remaining follow-up scope is explicit: live Event River
compaction, full task-document body windowing/on-demand retrieval, and heartbeat coalescing are routed to
the next HFX2 leaf rather than claimed complete here. Detail lives in the `mcp/`, `controlplane/`,
`observer/`, `serving/`, and provider route overviews plus their file sidecars.

The current Chats registry is structurally keyed by canonical task document plus role: sprint roles
occupy the sprint document, managers the master, and worker/reviewer/curator their leaf documents.
The left rail projects that real task hierarchy and resolves the current hosted occupant; replacement
does not change the row address. Qualified leaf keys remain only for leaf display/context helpers,
not seat identity. This supersedes the earlier leaf-keyed registry described in semantic history.
The operations-dashboard **polish** surface also includes resizable
persisted rails, drill-state that survives a view switch, the File/Diff viewer rendering opened route
overviews as markdown and the corrected Change-Set selected-row highlight, the Hangar filtering archived
enclosures, and faint siege-tank/battlecruiser empty-state backdrops). L5 also lands a **lifecycle
event-retention correctness fix** at the observer boundary: the durable enclosure — not the prunable
lifecycle event log — is the source of truth for liveness, so a running worktree no longer vanishes from
the Engine Room when its log ages out, and a not-yet-retired master series protects every leaf's event
history from the inactivity TTL until the series is archived plus a one-week grace. **L6** keeps the chat
assignment timing explicit: when an operator starts an agent chat on the displayed leaf or attaches a free
chat through task assignment, the right-rail chat may still inject projected leaf task/worktree context
once for the successful bind. That context package is not addressing authority. Detail lives in the
`observer/`, `serving/`, and `dashboard/src/` route overviews.

## Hot Path Summary

Git lifecycle operations carry code and memory-content outputs. Memory commits encode their code attribution; `memory.md` remains available as a computed cache for consumers. Root memory-cache changes are excluded from memory staging/candidate authority, and missing or malformed cache bytes cannot block closeout, synchronization, integration or cleanup.

Use [MCP package](mcp/overview.md) for composed services, [memory quality](mcp/src/agents_remember/memory_quality/overview.md) for preparation/final checks and [worktrees](mcp/src/agents_remember/worktrees/overview.md) for contract-owned lifecycle and protected refs. The retained [test route](mcp/tests/overview.md) describes present assertions and distinguishes helper-only files from suites. Exact source/pair identity, durable owner journals and original physical publications govern acceptance; a historical test name does not.

## Architecture At A Glance

```text
agents-remember/
  AGENTS.md
    source checkout instructions and installed-runtime handoff
  README.md
    public setup and conceptual model
  layers.toml
    enforced top-level package dependency order and package charters
  mcp/
    package-managed MCP server, runtime/skills install, provider lifecycle/setup, benchmark tools, settings, and integrity checks
  mcp/src/agents_remember/package_data/runtime/
    agents-md-files/
      coordinator/AGENTS.md
      skills/AGENTS.md
      system/AGENTS.md
      tasks/AGENTS.md
    skills/
      flat c-* core maintenance and resolver skills
      the `l-01-agent-lifecycles` skill and the `w-02-light-task-workflow` skill (the retired heavy workflow and its phase skills are no longer present)
    system/defaults/examples/
      coordinator and memory-repo example settings, sources, and tools files
  roadmap/
    design specs and historical planning notes

workspace ar-coordination/
  AGENTS.md
  skills/
  memory-repos/ar-agents-remember/
    memory.md
    onboarding/
      current onboarding baseline for this repo
  tasks/
    durable planning artifacts for worktree-support rollout
  temp/
    temporary generated artifacts such as drift reports
```

## Code Structure

| Area                 | Path                                                                                                                                                                            | Purpose                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Source checkout instructions | [AGENTS.md](agents-remember/AGENTS.md)                                                                                                                               | Defines how agents work on this source checkout and when to hand off to the installed runtime instructions.    |
| Public documentation | [README.md](agents-remember/README.md) and [docs](agents-remember/docs)                                                                                       | Keeps the root README as the public front door while focused docs pages own setup, concepts, architecture, workflows, install guides, guides, and reference material. |
| Package dependency contract | [layers.toml](agents-remember/layers.toml) | Declares one fail-closed top-level package order and one charter per package. The repository-neutral `certification` contract is rank 3 between wire models and the stateful control plane; later integer ranks shift without changing their package charters or runtime behavior. |
| MCP package          | [mcp](agents-remember/mcp)                                                                                                                                                       | Package-managed MCP server exposing context, runtime install, skills install, provider, worktree, memory, benchmark, settings-derived lifecycle, and memory quality tools. |
| Core skills (C-*)    | [mcp/src/agents_remember/package_data/runtime/skills](agents-remember/mcp/src/agents_remember/package_data/runtime/skills)                                                                                                           | Resolver, memory quality control, repo bootstrap, onboarding maintenance, and related support skills — flat directly under `skills/`. |
| Lifecycle + task workflow | [mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles) and [mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow) | The unified agent lifecycles — now a **thin router** plus a shared `core/`, nine self-contained role files, eight `operations/` blocks, a prose-free `composition-manifest.json`, and reference-only rationale/rulings — and the durable light task workflow (which escalates to a master + light sub-task series for larger work). |
| Runtime AGENTS templates | [mcp/src/agents_remember/package_data/runtime/agents-md-files](agents-remember/mcp/src/agents_remember/package_data/runtime/agents-md-files)                                                                                                        | Package-owned coordinator, skills, system, and tasks `AGENTS.md` templates for runtime installation.           |
| System defaults      | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples](agents-remember/mcp/src/agents_remember/package_data/runtime/system/defaults/examples)                                                                                          | Example settings, sources, and tools files used as scaffolding material.                                       |

### 260915-KS-L22 Route Impact — The Intent Reviewer Surface, And The Port That Keeps It Path-Free

`260915-KS-L22` (`KS-R22@v1`) adds the repository's first read-only **Intent Reviewer** surface: one
HTTP route, the application adapter behind it, a display vocabulary with its prohibitions built into
its constructors, and the dashboard panes that render it. Four facts belong at repository altitude.

1. **The route cannot be pointed at a dataset.** `GET /api/review/intent`
   (`mcp/src/agents_remember/serving/review.py`) is GET-only and accepts **no filesystem path**: the
   query string carries `repo`, `master`, `leaf`, `selectorKind` and `selectorId`, and the candidate
   whose datasets are compared is resolved behind the route from the canonical task context — the
   leaf's enclosure contract is located from the recorded task root, never from a caller-supplied
   path. Current `HEAD` and a guessed worktree path are unavailable as fallbacks, because neither is
   reachable from the route's inputs.
2. **Transport is separated from composition by rank, not by taste.** `layers.toml` ranks `serving`
   below `application`, so the HTTP shim may not import the read, diff and view operations it
   composes; it takes `KnowledgeReviewPort` — a callable from the typed request to the typed result —
   the way the launch route takes the capsule compiler. `ServingCollaborators.knowledge_review`
   (`serving/_app_common.py`) carries it in, `serving/app.py` registers the route, and
   `cli/dashboard.py`'s `serving_collaborators` builds the application adapter in production. A
   process that omits the port **refuses the route by name with `503`** rather than serving an empty
   pane, because an empty pane and an unreachable adapter are different facts. `404` marks a
   candidate that does not resolve, is not live, or has no dataset; `400` a selector kind the surface
   does not admit; `200` the typed result serialized once through the model that declares its shape.
3. **The surface owns no record kind and no conclusion.** `models/knowledge/review.py` defines the
   vocabulary of what the panes carry: **no** summary, narrative, severity, score, conflict verdict,
   causal explanation or approval exists anywhere in it, so the display cannot grow one by filling a
   blank; "unassessed" is the absence of a value rather than a value; a missing operand is a named
   state rather than an empty string; and a stale payload must carry the submission state that
   disables submission against it. Every value it renders comes from a record another owner already
   stores. `application/knowledge_review.py` is the thin adapter over the shipped read, diff and view
   operations — it selects nothing, computes no scope, widens no frontier and re-resolves no
   reference; R07's selection policy, R08's comparison result, `Route` as the recorded scope axis and
   L20's review matrix are consumed exactly as their owners publish them, and every absence is a
   typed state.
4. **The dashboard half is a rendering, not a second authority.** `dashboard/src/data/review.ts` and
   `dashboard/src/panels/review/ReviewSurface.tsx` carry the request/response binding and the panes;
   `Cockpit.tsx`, `panels/changeset/ChangeSetViewer.tsx` and
   `panels/detail-panel/changeSetBar.tsx` gained the entry points into them. The surface is
   read-only end to end, and `mcp/tests/test_knowledge_review_surface.py` is the case that holds its
   prohibitions: `test_the_whole_payload_schema_has_no_field_a_generated_conclusion_could_occupy`,
   `test_the_surface_defines_no_record_kind_no_table_and_no_status_of_its_own`,
   `test_an_unassessed_subject_is_displayed_unassessed_and_never_defaulted_to_compatible`,
   `test_a_missing_side_is_its_own_state_and_never_an_empty_string`,
   `test_a_stale_comparison_keeps_the_previous_input_and_disables_submission` and
   `test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path` would each
   redden on the corresponding regression. No case was added or replaced by this pass. (Since
   `260921-ICR-L57`, the resolution case lives in `mcp/tests/test_knowledge_review_resolution_and_route.py`,
   moved verbatim with the surface module's other resolution and transport cases.)

### 260915-CAPS-L6 Route Impact — A Native eve Session Adapter, And A Root Tree Outside The Path Rules

`260915-CAPS-L6` (`CAPS-R06@v1`) adds a native eve session adapter to the repository. Two facts belong
at repository altitude because they change the shape of the tree rather than the behaviour of one
module:

1. **The controlled application is a new repository-root tree, `eve_runtime/`.** It is an AR-owned eve
   application (`package.json`, `package-lock.json`, `README.md`, `agent/**`), not a package under
   `mcp/`, and the adapter launches it as a child process instead of shelling out to a `PATH` command.
   **This tree is outside this memory root's `pathRules` and deliberately has no sidecars.** Its
   authored surface is documented where it is consumed: the launch module's card owns root resolution,
   staging and the launch environment; the wire module's card owns the queue policy the authored
   channel mirrors; the live fixture's card owns the workspace-confined tool contract. Inventing
   sidecars for an ungoverned tree would create onboarding no rule maintains, and the canonical
   `skills/**` tree is the standing precedent for the same boundary.
2. **The adapter is an implementation of existing seams, not a new plane.** It registers in
   `serving/harness_control_factories.py`'s built-in protocol set (now four ids) while the kernel's
   developer-curated terminal harness set keeps three rows. No new service, scheduler, registry or
   approval surface appears, and the requirement's exclusions (no production cutover, no global
   configuration change, no replacement agent loop) are preserved.

Machine-local build products the change set introduces (`eve_runtime/.eve/`, `node_modules/`,
`.output/`) are ignored by the `.gitignore` entries the same change set adds; they are not repository
content and are never onboarded.

### 260915-CAPS-L1 Route Impact — Lifecycle Corpus Restructured And Made Single-Source

The `l-01-agent-lifecycles` instruction corpus was consolidated across the whole repository route in
260915-CAPS-L1 (requirement `CAPS-R01@v1`). The structural change future readers must know about:

**Read this section as STRUCTURE, not as a saving.** It was always a design intent — one
single-source, role-addressed corpus — and it is **not** a measured context reduction. The one
measurement that exists (§ 260915-CAPS-L10 Measured Result) reports the assembled capsule **larger**
than the legacy startup chain at the worker elevation, and no line-count change is evidence about
tokens a session reads: the doctrine moved into the new layers below rather than disappearing.

- **The entrypoint is now a router and carries no doctrine.** `SKILL.md` went from 620 to 179 lines and
  contains only the three routing conditions, the nine-role registry, the composition map, an
  orientation diagram of the super-integration topology, and pointers.
- **Four new layers hold what the entrypoint used to carry**: `core/` (six shared blocks — authority,
  invariants, lifecycle-frame, loop, acceptance, launcher), `operations/` (eight operation-scoped
  procedure blocks on a frozen vocabulary), `reference/` (rationale and the durable-rulings index), and
  `composition-manifest.json` (prose-free routing metadata for the deterministic capsule compiler).
- **All nine role files were rewritten into one readable order** — purpose/authority → required inputs →
  normal workflow → permitted writes → stop/escalation → completion/handoff, then the knob block — and
  each declares its shared sources with `**Inherits:**` instead of restating them. A role file may name a
  sibling role file only for wearing that hat or dispatching that seat.
- **The canonical tree is `skills/`; every other tree is generated.** `scripts/sync-skills.py` writes the
  MCP package-data runtime copy and the eight harness starter trees, and `--check` proves them
  byte-identical. Editing a generated copy is drift.
- **The role files' readable order was itself superseded.** leaf `260915-CAPS-L22` (under the developer's 2026-09-17 ruling) rewrote
  all **ten** role files under `skills/l-01-agent-lifecycles/roles/` — and their byte-identical package-data
  copies — into the **function shape**: `# <Role>`, `## Inputs`, `## Process`, `## Outputs`,
  `## What you may do`, `## What you must not do`, and a closing `## Stop and …` section, with a per-role
  extra only where the role has one. The numbered `## 1 — Purpose And Authority` … `## 6 — Completion And
  Handoff` sections, the `## Knobs, Tool Surface, And Dispatch Authority` block and the `**Inherits:**`
  line are gone from every one of them, so any card or overview that still cites one is stale. The ten
  files now total **1,578** lines.

**Onboarding consequence, recorded because it is a boundary rather than a defect:** the canonical
`skills/**` tree sits **outside this memory root's `pathRules` include set** (`mcp/**`, `dashboard/src/**`,
`scripts/**`, `installer/**`, `runtime/**`, `examples/mcp/**`, `AGENTS.md`, `README.md`), so the canonical
corpus has no sidecars of its own. The sidecars for this corpus live on its tracked generated copy under
`mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/**`, which is governed — that
tree gained 18 new cards in this pass (the manifest, `core/` ×6, `operations/` ×8, `reference/` ×2) and 17
existing cards were updated in the body. The legacy `onboarding/skills/l-01-agent-lifecycles/**` tree is
outside the current path rules and is retained as history.

## Functional Areas

### Source Checkout Contract

`AGENTS.md` is the authoritative behavioral contract for agents operating on this source checkout. It now starts by separating the package source repository from the installed `ar-coordination` runtime: when the file is reached through a workspace-level pointer during sibling-repository work, agents should use the installed runtime `AGENTS.md` instead. For work on this repository itself, it keeps `agents-remember` as the resolver target, routes sessions by role through the `l-01-agent-lifecycles` skill (a spawned role follows its brief; a developer session starts in free chat, answers research inline, or durably pins a complete architect brief and dispatches the architect on the sprint; explicit seat takeovers use the named role and canonical task document), requires `c-08-ar-coordination-context-resolver` skill resolution plus `c-02-memory-quality-control` skill memory quality control before relying on onboarding, separates implementation approval from commit approval, and points active settings reads at the resolved memory layer rather than a root-level source checkout `system/` directory.

### Package Layer Contract

`layers.toml` is the fail-closed authority for allowed top-level package knowledge, not a snapshot
of whichever imports happen to exist today. Order position is rank: a package may import only a
lower-ranked package, and undeclared packages or upward edges fail the layering rail without a
baseline or exception. The generic certification domain is explicitly rank 3 in the sequence
`errors < kernel < models < certification < controlplane`. That keeps its immutable registry,
planning, bounded-admission, and typed-result contracts below their future stateful consumers while
leaving concrete repository profiles, executors, lifecycle terminalization, and memory gates with
their higher-layer owners. `controlplane` consequently remains the lowest stateful interaction
service rather than the lowest domain contract.

- The order declares `certification` between `models` and `controlplane`, and those package tables carry matching ranks 3 and 4. [31]
- The production checker loads that one contract, rejects undeclared package directories, and reports invalid dependency direction. [32]

### Public Documentation

The public README is now intentionally short: product positioning, a fast Core Features pitch, a core path-derived memory example, one generic quickstart, a ToC-linked **Run The Dashboard** section (260703 L3 — unpinned `uv tool install agents-remember-mcp` as the first-class install, flag-free discovery-backed `agents-remember dashboard`, daemon mode + the `dashboard.autoStart` key, pinning as the debugging path, one rc-period pre-release note; the PyPI `mcp/README.md` Install And Run carries the same story), harness install links, docs links, and a compact source/runtime layout. Detailed user-facing material moved under `docs/`: `docs/features.md` is the concentrated product tour, `docs/README.md` is the documentation index, `getting-started.md`, `concepts.md`, `architecture.md`, `workflows.md`, and `FAQ.md` own core narrative, `docs/install/` owns harness-specific setup, `docs/guides/` owns operational tasks, and `docs/reference/` owns exact runtime/settings/skill behavior. Its Status section states the current version (bumped every release) and that the 3.0 cockpit arc has shipped — the dashboard is served from the MCP package via the `agents-remember dashboard` CLI. A separate `docs/design/` subtree holds developer-facing design specs for in-flight major work — distinct from the user-facing pages above and from the historical `roadmap/` notes. Its entries include `docs/design/observable-lifecycle.md` (the approved 3.0 design for an observable, controllable session lifecycle — the browser-dashboard direction, issues #2/#43), `docs/design/harness-matrix.md`, and the **engine-room** design language: `docs/design/engine-room/engine-room-visual-language.html` (the canonical living spec for the engine-room visual primitives — state colours, motion, glow, timing) and `docs/design/engine-room/podstage.html` (the prototype the production canvas was built from). Historically slice 05k admitted design documents into onboarding. The current recovery memory’s `system/settings.json` excludes `docs/**`; retained design/reference overviews preserve prior knowledge and do not imply present one-to-one file-card eligibility. README onboarding and governing overviews carry the applicable implementation account.

### Harness Starter Packages

The hidden root packages `.claude/`, `.codex/`, `.cursor/`, `.agents/`, `.github-vscode/`, `.vscode/`, `.hermes/`, `.pi/`, and `.openclaw/` are source-owned starter packages even though current path rules exclude their one-to-one file sidecars. Their first-action surfaces defer to spawn-role env or a fresh role brief; otherwise they open the developer-facing free-chat launcher. Research-only questions stay inline, while role-shaped work spawns a clean architect with the settings-owned profile. Backend orchestrators remain spawned seats and relay developer decisions through the architect. Canonical skill content is synchronized into these mirrors; the package-data runtime copy is the eligible onboarding evidence.

### Runtime AGENTS Templates

`mcp/src/agents_remember/package_data/runtime/agents-md-files/` is the package-owned source for installed coordinator instructions. The current package has four installable templates: `coordinator/AGENTS.md` for the coordinator root, `skills/AGENTS.md` for compact C-* skill routing, `system/AGENTS.md` for the hard onboarding maintenance gate, and `tasks/AGENTS.md` for task-folder collaboration doctrine. `runtime_install` MCP tool installs those templates to `ar-coordination/AGENTS.md`, `ar-coordination/skills/AGENTS.md`, `ar-coordination/system/AGENTS.md`, and `ar-coordination/tasks/AGENTS.md`. Memory repos are not expected to provide a root-level `AGENTS.md`; repo-specific memory guidance lives in the memory layer's `system/*` files.

### Core Resolver And Memory Quality Control

`c-08-ar-coordination-context-resolver` skill resolves the active coordination context: topology, code repository, `coordination_root`, `memory_root`, onboarding/docs/system roots, settings paths, repo-specific task root, temporary artifact root, contract path, worktree group, ledger path, storage settings, path rules, and branch-gated cross-repo allowances. Without a task name, `task_root` is the repository namespace under `ar-coordination/tasks/<repo>/`; with a task name or contract, it is the concrete task folder. Path-rule defaults in `system/settings.json` now carry the standard generated/vendor/build/cache/IDE/env/Zone.Identifier excludes. For worktree-backed task names, `c-08-ar-coordination-context-resolver` skill resolves current wrapper folders first and persisted `*-ar` task folders second. `c-02-memory-quality-control` skill consumes that context and owns memory quality control: task-start drift verifies file-level onboarding metadata, overview `sourceRoute` metadata, inline digests, and repo entity `git-blob-set-v1` fingerprints against the current source state; pre-code-commit checks catch newly added files without onboarding; closeout checks combine drift integrity with memory style. Drift reports are temporary coordination artifacts under `temp_root`; even explicit report paths inside the durable memory repo should be redirected back to coordination temp.

### Onboarding Maintenance

`c-05-create-or-update-onboarding-files` skill owns file-level onboarding and repo-level entity catalogs. It is the maintenance path for creating or updating onboarding artifacts; `c-02-memory-quality-control` skill detects memory quality issues but does not rewrite onboarding content. File-level onboarding now records the nearest governing `overview.md` when route-local overview coverage exists, while remaining self-sufficient for the concrete source file. Entity catalogs carry one deterministic fingerprint row per entity over a small curated evidence file set; `c-05-create-or-update-onboarding-files` skill chooses and refreshes those paths after review. After closeout memory edits, `memory_quality_check` combines drift integrity with style checks such as newest-first update history ordering before the memory content commit. `c-05-create-or-update-onboarding-files` skill also detects route-level create, refresh, move, and deletion cleanup cases and routes those structural changes to `c-03-repo-bootstrap` skill `existing-memory-slice-maintenance`. Generated `overview.index.json` files live beside route overviews and expose route scope, covered sidecars, child routes, copied hot-path summaries, and mechanically derived source-anchor hints so `c-04-retrieval-strategy-router` skill can route cheaply before opening full overview prose.

### MCP And Context Provider Runtime

The runtime has optional local discovery providers, but they remain accelerators rather than proof. The MCP settings file, not coordinator `system/settings.json`, declares allowed providers and repositories for the MCP path. That file is also the LIVE provider launch authority (260707-HFX-L1): launch-capable operations re-read it from disk fail-closed instead of trusting a server's boot snapshot, so disabling providers on disk bites running servers immediately; stopping, status, and cleanup stay legal, non-dry-run provider setup runs one-at-a-time host-wide behind a HOST-scoped setup lock in the system temp dir (outside every prunable coordination root and benchmark workspace — the guarded resource is the host), and the dashboard daemon samples labeled provider containers into a central containment metrics store under `logs/observer/providers/` that `provider_status` attaches even while providers are disabled. `context_packet` reports provider and watcher state, `runtime_install` installs runtime assets and provider dependencies from package-local code, and `skills_install` copy-installs packaged skills into harness skill roots. Managed provider installs should be coordination-owned without host executable fallbacks: pinned requirements under `providers/requirements/`, provider instances under `providers/runners/`, durable databases under `providers/data/`, operator logs under `logs/providers/`, MCP transcripts under `logs/mcp/`, and patches under `providers/patches/`. `providers/_bin/` and `providers/_venvs/` are stale-artifact cleanup targets, not runtime authority. Database, native-binary, and daemon infrastructure should be Docker-wrapped rather than installed as host services.

GrepAI runs in workspace mode with explicit `{ projectId, path }` roots generated from MCP repository/memory settings. Current managed mode indexes live memory roots in place and git-ignores GrepAI's per-root `.grepai/` working directory instead of mirroring roots under a separate index-root tree. Its runtime config, state, cache, and home artifacts belong under `providers/runners/grepai/`; its shared PostgreSQL/pgvector Docker data belongs under `providers/data/grepai/postgres/`; and `.grepai/` content should not be treated as durable memory. Managed GrepAI prefers non-conflicting auto host ports (`61432` for Postgres, `61434` for Ollama) while keeping the Docker container service ports (`5432` and `11434`) inside the provider network. Worktree isolation clones the source GrepAI database into a worktree-scoped PostgreSQL backend and rewrites provider settings so containers, logs, and runtime paths are isolated while the logical workspace key remains reusable. CodeGraphContext keeps one provider instance per configured repo under `providers/runners/codegraphcontext/<repo-id>/.codegraphcontext/`, with all instances sharing the FalkorDB Docker data root under `providers/data/codegraphcontext/falkordb/`; worktree setup seeds CGC by exporting, path-rewriting, and importing an existing graph bundle. Seed/clone operations are guarded by stall watchdogs (kill on zero progress), never total-duration caps — the copy-instead-of-reindex mechanic is what makes rapid worktree provider deployment viable and it scales with index size by design; the CGC seed accepts relatable HEAD divergence and hands additions/modifications to post-watcher catch-up; deletions and rename sources remain explicit residual staleness, while unrelatable heads refuse seeding. On stdio transport, package subprocesses must never inherit the server's protocol pipes (`stdin=DEVNULL` or piped input, AST-guarded; the 2.5.1 fix for the multi-minute tool hangs).

### Code Quality And Refactor Baseline

Current development commands, diagnostic metrics and certification authority are described in Development And Certification Policy above. Static product/verification ownership remains explicit; uncovered lines do not create a test obligation and CRAP findings do not block delivery.

### Task Workflows

`w-02-light-task-workflow` skill is the compact durable-task workflow used by the current worktree-support task stack. It creates a task wrapper folder and `task.md` once task class and naming are clear, stops for implementation approval, then treats the checklist, onboarding propagation, checks, and worktree-backed commit approval handoff as one implementation cycle. When refreshed external-memory onboarding is part of intake, the substantive memory content is committed and the consumer ledger is refreshed before `c-09-git-worktree-manager` skill starts worktrees.

Requirement delivery history is append-only without turning every implementation/test rerun into a
formal attempt. Semantic revisions advance only through explicit developer approval; workers mint
delivery attempts only when handing an exact candidate to independent review or after reviewer
rejection. Internal runs stay in a separate protocol-event log. Per-requirement journal records are
lightweight and link a content-addressed frozen expanded-evidence artifact; rebuildable master
summaries exclude protocol events and never gate task authoring, lifecycle, closeout, integration,
or queue work.

### Bootstrap Memory Build

`c-03-repo-bootstrap` skill now treats the root repo overview as the minimum successful bootstrap and scales through route-local overview construction pillars, evidence packs, file cards, onboarding waves, curator reviews, and handoff artifacts. Its templates live beside the skill under `mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/` and define the shape of input ledgers, state files, coverage plans, governing route maps, overview cards, route-local overviews, docs packs, boundary packs, file cards, wave manifests, curator reviews, and final handoffs. Route-local overviews are durable memory in the mirrored onboarding hierarchy directly under the resolved onboarding root, not detached area appendices, and file-level onboarding links back to the nearest governing overview. Existing-memory slice maintenance handles added, moved, deleted, refreshed, and newly important routes without pretending the repo is blank; automated bootstrap starts after source inventory intake and stops at handoff before separate closeout approval.

### Worktree Support

The worktree and cross-repo roadmap specs are still useful design references, but core implementation now exists for the first support slice: memory ledger parsing/writing, worktree contract parsing/writing, `c-08-ar-coordination-context-resolver` skill contract-aware facts, the `c-09-git-worktree-manager` skill `start`, `attach`, `status`, `closeout`, `integrate`, `lifecycle_finalize_task`, and `cleanup` command surface, and the `c-10-adopt-memory-baseline` skill `status`/`adopt` adoption workflow for pre-existing external-memory onboarding. `c-00-initialize-memory-repo` skill initializes missing memory roots before `c-09-git-worktree-manager` skill worktree use. `c-09-git-worktree-manager` skill external-memory start blocks substantive dirty source-memory content while ignoring its disposable cache so a refreshed onboarding pass cannot be accidentally stranded outside the ledgered baseline. `c-09-git-worktree-manager` skill closeout dry-run is the non-mutating preview path before explicit commit approval. Real external-memory closeout runs the explicit repository-profile Dagger lane before the accepted code commit, then applies the separately owned memory/ledger lifecycle boundaries — since 260731-EFA-L4 over the *staged* task worktree, which is the one index mutation that precedes the gate; missing profile authority, CRAP at or above threshold, or a failing required rail fails closed. Only after that gate passes does closeout commit code, use `c-02-memory-quality-control` skill memory quality control to produce the maintenance worklist, refresh affected onboarding verification metadata and entity fingerprints, run `memory_quality_check`, then commit memory content and ledger when clean. `lifecycle_finalize_task` is the terminal lifecycle operation after the branch edge has landed: it proves the landed commit is reachable from the local parent/source branch, verifies memory carryover, runs or verifies cleanup, and reconciles the JSON-primary leaf task plus immediate parent row to `Completed`; it does not attempt squash equivalence or recursively complete ancestors. Closeout is worktree-only: the former direct-closeout current-checkout path was removed (issue #62), so every closeout runs against a task contract.

### Historical Observable Session Lifecycle Build-up

This section preserves tasks 27–29 as historical development context. Current tool-response enrichment, structural seats, and lifecycle decision ownership are described in the feature inventory and the application/lifecycle, MCP/tools, and serving overviews. Statements below about every response receiving a hint or parked public gates are not current API guarantees.

The `agents_remember.observer` package is the 3.0 browser-dashboard direction: it
makes a working session a first-class, observable entity. The **write side** is an
append-only, replayable `ar-observer-event/v1` event log with trust provenance
(declared vs observed vs inferred), an ambient process-singleton lifecycle (the six
`lifecycle_*` signal tools, a heartbeat ticker, and a TTL project-and-prune sweep),
and a `_tool_payload` emission hook that attributes every tool call. The **read
side** is a pure projection reducer — the single owner of interpretation — that
folds the event logs plus file snapshots into resolved state for any client
(dashboard, future TUI, or agent): the lifecycle/enclosure/provider tree, metrics,
staleness, the per-lifecycle token fuel gauge, the analytical surfaces (drift read
from a persisted snapshot, sidecar staleness, provider setup, route coverage, tool
reports, ledger currency), and precomputed action availability, written atomically.
The lifecycle-signal and gate substrates are now **adopted by the lifecycle
skills**, so the agent's behavior — not just the dashboard's reads — makes the
session observable: the `l-01-agent-lifecycles` developer-facing lifecycle (the
orchestrator pre-HFX-L6; the architect since the seat split, with spawned backend
orchestrators parking durable gates and relaying decision items) carries a **Gate
Choreography** (every approval junction calls public `lifecycle_gate`, which
blocks the ambient lifecycle, creates the durable kind-typed gate, and initializes
wait state; the **developer** resolves or sends a message — never the agent's own
model-attributed `gate_decide` — and the agent always *clears* with
`lifecycle_resume`), with the junctions split by kind across
the skills: `plan-approval`/`push-approval` (l-01), `worktree-intent` +
`integration-approval`/`cleanup-approval` (the `c-09-git-worktree-manager` skill),
and `closeout-approval` — which **is** the single commit gate — (the
`c-12-closeout` skill, now extended to the full raise→wait→clear pattern). This
completes the observable-lifecycle gate story end-to-end. Detailed per-file routing
lives in the `observer/` route overview; the full design (lifecycle entity, event
schema, enforced gates, the cockpit) is `docs/design/observable-lifecycle.md`. The
serving layer and the cockpit UI are later slices of the same series. **Task 27** adds
the **lifecycle next-step hint engine** ([next_step.py](agents-remember/mcp/src/agents_remember/application/next_step.py)):
every MCP tool response now carries a `nextStep` computed from the projected lifecycle
state at the `_tool_payload` choke point — a one-time front-half prose rundown from
`lifecycle_start`, then a linear per-tool chain that delegates to the worktree
`guidance.lifecycle_guidance` state machine and points at the existing `lifecycle_gate`
at gate junctions; it is built on the existing gate, with auto-firing left to a later step.
**Task 28** then makes **NOTIFY-AND-CONTINUE** the active turn-end model: a new public
`lifecycle_turn_end_notification` tool drives a non-terminal `awaiting-developer` lifecycle
state (the agent notifies the developer and stops — no gate, no wait — and the next AR tool
call auto-resumes at the `_tool_payload` choke point via `resume_from_await`), the next-step
ACTIVE hints repoint off `lifecycle_gate` onto it, and a one-line reducer dedup
(`_lifecycle_attention`'s `... and lifecycle.gate is None`) collapses the duplicate
gate-open/blocked-gate attention item; the `lifecycle_gate`/inbox stack stays valid but
parked (un-hinted). Detail lives in the `observer/`, `mcp/tools/`, and `models/` route overviews.
Task 28 is also a **doctrine reframe** across the root skill trees (`skills/` and its mirrors
`.claude/skills/`, `.agents/skills/`, `.hermes/…`, `.codex/…`, `.cursor/…`, … = the `.` route): the
active-developer hand-off in `l-01-agent-lifecycles`, `c-09-git-worktree-manager`, and
`c-12-closeout` now teaches **notify-and-continue** at every junction (reframe / plan / worktree-intent /
commit-closeout / push / integration / cleanup / turn-end) — dry-run → chat report →
`lifecycle_turn_end_notification(summary=…)` + STOP, with the next turn's first AR tool call auto-resuming —
and parks block-and-wait `lifecycle_gate` (+ `lifecycle_resume`) and the operator inbox as the fallback. The
packaged bundle copies under `mcp/src/agents_remember/package_data/runtime/skills/` are propagated from the
canonical `skills/` by `scripts/sync-skills.py`.

### JSON-Primary Task Documents

The `agents_remember.tasks` package makes the task document machine-readable: the
persisted `ar-task-document/v1` JSON (status, info, requirements, step/substep
progress, decisions) is the source of truth, and `task.md` is a deterministic render
of it (the `w-02-light-task-workflow` `template.md` is the render spec). The `task_doc`
MCP tool authors documents — create, full-document replace for task resets/replans,
set status, set a step/substep, append a decision — and re-renders the markdown on
every write; the markdown is never parsed back. This
closes note-03 gap #8 (no machine-readable task registry) and is the per-lifecycle
work-content layer the observer projects (keyed by the contract's `lifecycle_id`) so
the dashboard can show step/substep progress. Scope covers `light`, `subTask`, **and**
`master` documents — a master carries a structured `subTasks` series index + an ordered
`sections` passthrough that preserves its bespoke prose, so a series wrapper is
machine-readable too; live adoption follows the runtime shipping `task_doc`. **R1 (masters
observable):** the observer now also projects `master` docs **folder-keyed**
(`read_series_documents` → `Analytics.series`), aggregating the declared `subTasks` checkboxes into
whole-series progress — so clicking a series master on the dashboard shows its overall progress, not
just per-lifecycle leaves. Task 17 extends that surface with master `objective` and structured leaf
`createdAt` metadata; dashboard readers can therefore show authored master content and default leaf
lists to creation order without interpreting filename or task-slug prefixes.

The execution-topology extension separates that organizational task tree from Git scheduling
facts. Each commanded master declares `organizational` or `atomic`, while the sprint document owns
the canonical reasoned AON graph. Membership, cycles, and derived waves are mechanical and
projected to the dashboard; priority and rescheduling judgment remain orchestrator concerns.

This relates to — but does not build — the parked neutral-repo task/contract sharing substrate
(issue #79). Detail lives in the `tasks/` route overview. (Slice 3c: commit 1 = engine +
tool; commit 2 = the `w-02-light-task-workflow` JSON-primary adoption and the observer
reader; commit 3 = master JSON support; reopened R1 = the folder-keyed series projection; reopened R2 = the heading-vs-outcome renderer fix (distinct `Step.outcome`); reopened R3 = the deferred-examples honesty field (`codeExamplesNote`); reopened R4 = leaf-doc fidelity (`statusNote`/`headerNotes`/freeform leaf sections) — all landed.)

### Dashboard Serving Layer

The `agents_remember.serving` package is the 3.0 dashboard's transport spine (slice 04): a
FastAPI app, launched by `agents-remember dashboard` (the new umbrella `agents-remember` CLI),
that serves the observer projection live. One shared projector ticks `project_and_write`,
diffs each projection against the last, and fans **per-entity deltas** out to every client
over a single multiplexed SSE stream (`GET /api/stream`: an `event:snapshot` then named
`lifecycle`/`enclosure`/`provider`/`metrics`/`analytics` upserts and `*.removed` markers);
`GET /api/state` returns the projection once. The reducer owns projected state interpretation; serving also composes the controlled-session and operator-action authorities. Coordination paths are resolved through `McpRuntimeConfig` +
`observer.paths` (North-Star #5), never raw host paths. Local-first: bound to `127.0.0.1`,
no auth in v1. The **frontend** is a root-level sub-project (`dashboard/`) whose built bundle
ships as `package_data/dashboard/`, placed there by `scripts/sync-dashboard.py`. Since
260731-EFA-L1 that placement happens **in the release job**, not at commit time: the bundle is
git-ignored, no hook and no CI job checks it, and the frontend rail in CI proves only that
`npm run build` still succeeds. A checkout with no build serves 503 with the build command from
`serving/static.py` rather than a placeholder — the slice-04 hand-authored placeholder is gone and
must not return. Slice 4b added
the raw `event` SSE channel (`GET /api/events`, byte-offset `Last-Event-ID` resume), sim-mode
replay (a replay clock + fixture feeder over the projector's `now`/`before_tick` seams, so the
frontend cannot tell sim from live), and the `POST /api/actions/{action}` plane
(validated against the reducer's `ActionAvailability`; slice 6b records gate-decision verbs as
developer-attributed gate decisions via `gate_decide_for_lifecycle`, lifecycle transitions stay no-mutation). Slice 05 (5b)
builds the read-only **cockpit** on this stream — the four core panels (attention queue, live
session strip, the two-axis BY REPO | BY LIFECYCLE operation tree, and the detail panel with the
Request→Close phase stepper + display-only gate banner) on the podracer state-grammar, fed the
server-computed `Analytics.attentionQueue`. **Slice 05 (5c)** then rebuilt the cockpit to represent
the real model (notes 01/03/06): the **lifecycle is the unit** — paused persistent lifecycles
synthesized from worktree contracts show even when idle — in one de-duped BY REPO | BY PHASE list; a
**task reader** rendering the full task document; a **per-worktree engine room** (each worktree's
CGC↔code / GrepAI↔memory stack); the lifecycle → worktree → provider spine; and the topology
constellation. This drove a projection correction (per-worktree provider stacks, full task content on
`TaskDocNode`, persistent-lifecycle synthesis) detailed on the `observer/` route, plus a `serving/`
sim/events fix. **Slice 05 (5d)** then re-architected the React/TS frontend and brought `dashboard/src/**` **into
memory scope** (now onboarded, governed by the `dashboard/src/` route overview): the ~1,200-line
global `tokens.css` monolith was retired into the layered blueprint — **Panda CSS** (typed tokens +
build-time/zero-runtime recipes) for styling and **React Aria** (`react-aria-components`) for headless
behavior/a11y (the mode bar + pivot `ToggleButtonGroup`s, the lifecycle `ListBox`), with the CRT
effects isolated in `index.css`. A dev `/dev/bench` gallery plus `/dev/reference` mc2 mount drive
the screenshot-annotate review loop. The former `build_rich_sim.py` 35-lifecycle generator was
later retired because no maintained product or acceptance consumer used it; do not restore a
self-validating generator/test pair as evidence.
**Slice 6d** begins **Mode B2** — the dashboard-hosted terminal: 6d-1 lands the `serving.terminal`
host (a `TerminalHost` registry of tmux-wrapped stdlib-`pty` sessions that launch the real harness
render-not-scrape — raw VT bytes for xterm.js, fixed-argv with no shell-injection surface, OS-user
creds, localhost; the PTY/tmux spawn seam is injectable so CI drives a real kernel PTY without tmux),
6d-2 bridges it to the browser over the `/api/terminal/{session}` WebSocket — binary PTY bytes
out, JSON `stdin`/`resize` in, `{type:exit}` on child exit (the `websockets` dep is uvicorn's WS
impl); the xterm.js Chats tab (6e) follows. Task 22 makes those dashboard terminal sessions durable:
the serving layer persists a terminal catalog, rehydrates cataloged tmux sessions after browser
refresh/server restart, lets multiple browser tabs attach independent tmux clients to the same chat,
and keeps explicit `End`/terminate hidden across later exit bookkeeping. **Task 26** adds a
**hot-reload dev env** — a `--reload` flag on the `agents-remember dashboard` CLI. Task 29 S7 hides the
former **Lifecycle Flow** tab from the cockpit while leaving
[FlowTab.tsx](agents-remember/dashboard/src/panels/FlowTab.tsx) dormant in source.
**260707-HFX-L8** adds explicit seat lifecycle management on top of the catalog: server-authoritative
retirement (`POST /api/terminal/{session}/retire`, authority-policy-checked, provenance-stamped,
never a zombie row), post-spawn identity rename (`POST /api/terminal/{session}/rename`, label only,
never role), and a live turn-state badge (working/turn-ended/awaiting-input/stale) classified from
pane text on the existing liveness-sweep cadence. **260707-HFX2-L11** reverses the leaf-integrate
and master-finalize completion edges' automated behavior: a successful worker/reviewer/manager seat
is no longer auto-retired there — it is **landed** (`status:"landed"`, kept alive, non-terminated,
inspectable in a dashboard "landed archive" group with a group-cleanup control), since successful
completion is not chat cleanup (ruled design constraint 10); explicit `session_retire` or that
cleanup control are what actually reclaim chat volume. Detail
lives in the `serving/` + `observer/` + `dashboard/src/` route overviews.

## 260915-CAPS-L18 Complete Curation Reaches This Route

CAPS-R18@v1 inverted the optional/narrow-curation doctrine in the shipped instruction sources. The
sentences that presented the full `memory_quality_check` operation and the `curator_coherence`
certification as developer-request-only diagnostics, "never routine closeout/integration prerequisites",
are gone. The rule is now normative: **curation is complete on every leaf** — the full operation runs at
the leaf's contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every
curator-actionable finding is repaired or escalated as blocked with its exact returned code, and the
operation is re-run after every repair until `curatorActionableCount=0` and the **raw**
`qualityChecklistStatus=ready-for-closeout`.

**The two status fields are different fields, and a reader who merges them loops forever** (`D35`, a
landed-defect repair recorded by 260915-CAPS-L10). Read the **raw** `qualityChecklistStatus` to decide
whether the repair loop can end. Once it reaches `ready-for-closeout`, the **combined** `checklistStatus`
is rewritten to `coherence-required` **only when the coherence record is then missing or stale**; on the
success path, where the record is already current, the combined field is not rewritten at all and keeps
its incoming `ready-for-closeout` value, with `closeoutReady=true`. `ready-for-closeout` therefore *is*
observable in the combined field, but only once the whole pipeline — repairs and validation — is already
complete. `application/memory_quality/controller.py` is the authority: `:664` publishes the raw field,
`:671` gates on it, `:678` publishes the combined `coherence-required`, `:685-687` leave the combined
field untouched when the record is current and set `closeoutReady` after validation.

**Warrant corrected by `CAPS-R19` (leaf `260915-CAPS-L19`).** This card's `D35` correction originally
rested on the sentence *"`ready-for-closeout` is never a value of the combined field."* That absolute
claim is **literally false**, and `CAPS-R19`'s revision note records it as superseded by the three-path
model above. The field-name correction the sentence supported is still right; only its stated warrant was
wrong. **Attribution is complementary and both halves hold:** `260915-CAPS-L10`'s curator corrected the
**onboarding cards** that carried the wrong form, and `CAPS-R19` (`260915-CAPS-L19`) corrected the
**shipped sources** — the five loop-gate carriers, their nine generated copies, the guard registry's own
docstring — and brought `docs/reference/mcp-tools.md` into both the loop-gate census and the guard's
`LOOP_GATE_DOCUMENTS`.
The sentence this section previously carried named the combined field as the loop's termination
condition; that was wrong in the shipped sources and in the cards that quoted them, and it is corrected
here and on the other affected cards.

Two corrections the inversion must not collapse, both preserved: closeout still owns only the Git
transaction and **invokes** nothing — it **carries** the completed curation as a prerequisite; and the
rule is about the completeness of curation, not about unscoped runs, so "complete" always means the whole
operation at the leaf's contract scope. The ruling is forward-looking: the already-landed and finalized
leaves are not re-curated, and whole-layer completeness is discharged by L11's full-scope run at the
frozen tip.

## 260915-CAPS-L10 Measured Result — The Capsule Did Not Reduce Startup Context (adoption FAILED)

This is the experiment's measured outcome, and it is a **negative result**. It governs every other
section of this onboarding that describes the role-capsule compiler, the instruction corpus
restructure, or the experimental cutover: those sections record **structure and design intent**, and
**none of them is evidence of a context reduction.**

**The measurement.** `CAPS-R10@v1` behaviour 6 requires "a demonstrated reduction in AR-added startup
material for matched worker, manager and architect cases without missing required obligations." That was
**not demonstrated.** At the one elevation that could be measured (worker), the capsule is **larger** than
the legacy chain:

- **The delivered capsule is 11,828 tokens against a 5,928-token baseline — +5,900.** "Delivered" means
  the `orientation` capsule the measured run actually carried, read back from the consumer's own first
  prompt and matching it exactly.
- The like-for-like `implementation` capsule is **11,645** against the same 5,928 (**+5,717**). These are
  two different compilations, not two measurements of one quantity; the delivered figure is the one that
  governs, and it makes the gap larger, not smaller.
- **Manager (`coordination`) and architect (`planning`) are UNMEASURED**, refused with
  `binding-unresolved` because the frozen world carries no series contract at the master or sprint
  altitude. They are **unmeasured elevations inside the adoption failure — not passes**, and they are not
  evidence of a reduction either.
- **Obligation preservation is intact**: 36/36 cases across **ten** declared roles plus launcher routing,
  with the E1 falsification observed (a deliberately removed required instruction fails the check). The
  failure is on the reduction half alone.
- The two sides are **different kinds of object**: the capsule side is a role- and operation-selected
  payload (core + this role's block + one operation block); the baseline side is an **unscoped** chain —
  the same five files for every role and every operation. A "saving" computed across them would compare a
  selected package with an unselected one, and this onboarding states none.

**The delivery claim that DID hold, and the evidence class that carries it.** Separately from the size
result, a started session really does receive its compiled capsule:

- On **native eve**, the started session's **own system block** carries the capsule **exactly once** — on
  the second call, after **compaction**, after **clear** and after **resume**; a **forged** delivery never
  reached the system block; an **edited carrier** was **refused** (`carrier-digest-mismatch`) and made
  **no model call**; the seat wrote only its admitted workspace and an unbound launch was refused with no
  model call. Scenario summary `8 / 8` passed. The runtime process was staged from the builder's own
  worktree and asserted **byte-equal** to the authored tree (`agent.ts` sha256 `287dbbf0…`).
- On **Codex**, the capsule arm completed a real representative code leaf end to end: the repair landed in
  the **admitted** worktree and the fixture check went `1 failed, 2 passed` → **`3 passed`, exit 0**.
- **Honest boundary:** the eve arm's **model** is the fixture's deterministic local provider. What is
  native is the runtime process, the HTTP transport, the durable event stream and the adapter.
  **`--real-model` was NOT run** (no hosted provider credential in this environment) and is recorded
  **UNRUN**, not as a pass.

**Unobservable values are recorded as unobservable, never estimated.** Peak context occupancy is
**unobservable on both harnesses** (Codex's stream carries cumulative usage only; eve's
`serving/eve_events.py::EveEventMapper._HANDLERS` maps no usage frame). Cumulative usage is unobservable
on eve. Occupancy and cumulative usage were kept in separate columns and **never summed**. The baseline
arm's compilation cost is `not-applicable`, an honest absence rather than a zero folded into a total.

**The disposition is REVISE, and it is a recommendation to the owner, not a decision.** A complete
report recommends revise/discard and **remains a failed adoption acceptance**; it never closes an
unresolved functional requirement, never weakens mandatory native-eve functionality, and **no IAS landing
is authorized** by this leaf or by any green result. The prior 4k-in-a-32k-window figure stays a **stretch
direction**, never a hard truncation rule and never a fabricated achieved result.

**Not supportable from this evidence, stated so a reader cannot infer it.** The measurement does **not**
say the capsule is worse for a real session: the legacy figure counts the always-injected routing layer
only, and the skill corpus it routes to is read on demand and deliberately excluded from the measure. A
fair total-instruction-read comparison is a session-level measurement that **does not exist yet**. The
result is also **not** attributed to the compiler, because the two arms differ in installation mechanism
as well as in content.

**Frozen artifacts (this section's sources).** Method
`notes/reports/caps-l10-measurement-method.md` (digest `sha256:902676a630075f34b21c70e412eecee51bf8acc42488f3d1fc35a5b4b81ce528`);
frozen evidence `notes/reports/260915-CAPS-L10-evidence/` (991 entries, index digest
`sha256:c6581df2640f2514dde7e51393bcc1c95bb61e92affd62ad79b02906978900d5`); builder report
`notes/reports/260915-CAPS-L10-worker-report.md`; disposition `notes/reports/caps-l10-disposition.md`;
verdicts `260915-CAPS-L10-verdict-baseline.md` and `-verdict-fixverify-r2.md`. Both independent review
rounds closed with no open findings, and clearing six findings did **not** convert this into a pass.

**Design intent is labelled as intent, not as a measured reduction.** Three families of statements
elsewhere in this onboarding describe real structural changes and must not be read as savings measured by
this leaf: the `l-01-agent-lifecycles` corpus restructure (`SKILL.md` 620 → 179 lines, doctrine moved into
`core/` · `operations/` · `reference/`) is a **single-source restructuring**; the L2 compiler's determinism
and refusal-as-value properties are **correctness** properties; and the L9 installation cutover's
withholding of the four coordinator `AGENTS.md` targets is an **installation** change whose measured
effect on startup material was, at the one elevation measured, the opposite of a reduction.

**Residuals carried with owners (recorded, not repaired here).** `F-6`: the install does not manage the
harness's own skill root — **both measured arms read `~/.agents/skills/l-01-agent-lifecycles/SKILL.md`**,
so the cutover withholds only the coordination root's chain, which is the duplicate-corpus path its own
docstring says it exists to prevent (owner L9 / harness-surface). `F-5`: a mutation seed is vacuous **by
construction** because the earlier source read already refuses — a behavioural fact about the compiler's
refusal order (`models/role_capsules/` owner). **The matched Codex baseline completion is UNRUN**: the
legacy chain fails closed without the plane-injected `AR_HOSTED_SESSION_ID`, and supplying it by hand
would hand the product a value its own control plane produces, so a matched baseline needs a launch
through the **production control plane** — an owning-seat action, not a leaf's. Also filed, not repaired:
`F-1` (ten roles/nine operations — the code's counts, not the brief's nine/eight), `F-2` (an emptied
admitted source raises an uncaught `ValueError` instead of the documented refusal shape), `F-3` (launcher
skill admission), `F-4`/`C4` (`closeout` vs `authorized-closeout`, no reconciliation owner), `F-7` (the
legacy chain needs the plane's complete identity and fails closed without it) and `D34`/`D35`.

## Evidence

### Cross-Repo References

This repository is selected into an external coordination workspace by configured path rules, but onboarding content should cite same-repo files for repository behavior and task files only as planning references.

- The source checkout distinguishes installed runtime work from sibling-repo work and keeps implementation approval separate from commit approval. [33]
- Repository instructions define certifying delivery, enforcing checks, and diagnostic-only coverage and production CRAP. [34]
- The docs index owns the start-here, install, operational, and reference map. [35]
- Runtime asset sync treats root runtime folders as canonical and exposes a check form. [36]
- GitHub runs the deterministic non-test gate on pull requests only; tag publishing proves main reachability instead of regating. [37]
- The staged-quality boundary refuses unsafe linked/conflicted worktrees, binds the accepted candidate tree, stages exactly what will commit, and invokes targeted Dagger quality; the transaction-only closeout no longer imports it. [38]
- The staged-quality owner enforces its exact-candidate delivery boundary. [39]
- Contributor guidance separates host feedback from Dagger-owned certifying evidence and defines the retained protection policy. [40]
- Provider guidance keeps provider runtime paths under configured provider roots. [41]
- The MCP settings example declares repository and coordination authority. [42]
- The memory-repo tools example provides the `Code Quality` section. [43]

HFX2-L21 advances the existing Dashboard frontend feature: the Chats session rail is now a
persisted, pointer- and keyboard-adjustable 220–560 px sidebar instead of a fixed 16 rem column. The
resize separator preserves terminal working width and adds no new route or serving behavior.

260712-TRH-L1 restores the existing Dashboard task reader's functional contract without enlarging
the recurring projection: the selected document hydrates its complete body on demand before notes or
change-set counters mount, shows honest loading/fallback state, and caches by path plus body revision.
The implementation stays within the established `dashboard/src/data` and `dashboard/src/panels`
routes and ships through the existing generated-dashboard package boundary.

### Repo-Internal References

These current source and policy ranges establish the development/certification distinction and the existing memory preparation surfaces. A citation is source evidence, not a recorded test execution.

- Development commands, budgets, diagnostic metrics and isolation. [44]
- Certifying publication and accepting consumers. [45]
- Exact contract scope, full check and curator worklist publication. [46]
- Interactive catalog names missing authority without eligibility. [47]
- Final memory adapter requires the selected four-code-terminal prefix. [48]
- Finalization consumes original selected fifth-certificate inputs. [49]

Current working-candidate evidence for this route:

- Git attribution is the source of the consumer ledger. [50]

- Closeout writes or reuses one actual memory-content output (since MIK-R09, on converted memory, after closing the leaf's history file and validating and gating the exact tree). [51]

- Integration proves exact memory source ancestry independently of cache rows. [52]

### Docs References

Same-repository files remain the direct evidence for Agents Remember's own runtime and memory behavior. Public install pages now also link official harness documentation for volatile skill-location claims.

## Historical 260712-TRH-L4 Route Impact (later structural dispatch supersedes session-id addressing)

Repository onboarding now records spawned-unbriefed → harness-ready → briefed hosted dispatch, exact session-id continuity, delivered-plus-harness-log-confirmed assignment, canonical l-01 ownership with generated mirrors, and fully serialized catalog writers with lock-free atomic readers.


### 260713-PHA-L5 Route Contract Review

The route remains governed by the shared hosted protocol bridge: exact adapter snapshots provide
readiness and liveness, correlated receipts sit beneath durable inbox rows, interactions use durable
gates, legacy/custom sessions are explicit unsupported states, and pane/log signals are diagnostic
only. Dashboard and packaged projections remain additive and synchronized.

## Historical milestone context: 260718-CHATS-L5I Current Repo Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The interactive Chats round strengthens the repository's runtime-truth contract across the cockpit and serving daemon. Persistent chat and terminal surfaces preserve local state across view changes; active conversation streams recover from server-minted cursors instead of retrying unusable coordinates; structured questions and native interrupts are exact-session operations with explicit evidence; and dashboard state serving avoids repeated whole-tree walks and repeated projection serialization. These changes retain the existing rule that optimistic browser activity, transport acknowledgement, and terminal settlement are different facts.

The historical Chats commit-gate delta first made the wrapper mandatory at closeout, pre-push,
and CI. L23 supersedes that cadence: targeted Dagger acceptance runs once at leaf closeout, full
Dagger acceptance runs once at master integration, pre-push is deterministic non-test feedback,
and GitHub validation is pull-request-only and non-test. The enforcement topology in the Hot Path
Summary is authoritative. Canonical hooks, workflows, setup/public docs, root skill mirrors, and
generated dashboard assets are pathRules-disabled onboarding subjects; their current contract is
represented here and in eligible README, MCP package authorities, route cards, and memory-system
guidance rather than by duplicate sidecars.

## Historical 260731-EFA-L1 Repository Impact — The Gate Now Runs

This leaf's subject was enforcement itself, and it changes facts a future agent will otherwise get
wrong. The durable contracts:

1. **The cockpit bundle is built at release and is NOT in version control.**
   `package_data/dashboard/` and `package_data/dashboard.fingerprint` are git-ignored, as are
   `mcp/build/` and `mcp/dist/`. `scripts/sync-dashboard.py` lost its `--check` mode along with the
   subject it compared against; it now refuses an absent `dist` and refuses a `dist` that does not
   carry the build-input fingerprint `vite.config.ts` compiled into it as `__AR_DASHBOARD_BUILD__`.
   The fingerprint sidecar is therefore a value read *out of* the bundle, never stamped over it.
2. **The pre-commit hook gates staged content on a fast tier; pre-push repeats deterministic
   non-test checks.** `.githooks/pre-commit` and `.githooks/pre-push` are thin wrappers over
   `.githooks/_gate.sh <fast|targeted>`. The fast tier isolates the index with
   `git stash --keep-index --include-untracked`
   under restore traps, and skips isolation when the tree already matches the index or a sequencer
   operation is in progress.
3. **GitHub validation is pull-request-only and deterministic.** It runs generated-copy,
   formatting, lint, and type checks; ordinary pushes launch no duplicate and GitHub invokes
   neither host tests nor Dagger acceptance.
4. **The publish workflow verifies landed provenance instead of regating.** A tag must point to a
   commit reachable from `origin/main`; the workflow then builds the dashboard and package and
   asserts the wheel and sdist each contain the bundle and fingerprint sidecar.
5. **The closeout quality gate is no longer hard-coded to one repository name.** Applicability is
   decided by whether the target checkout carries `mcp/test_support/agents_remember_test_support/code_quality/check.py`;
   a checkout without it is reported as `wrapper-unavailable` rather than silently skipped.

What follows for anyone reading older material: `--no-verify` was routine here precisely because
the pre-commit hook could not pass, and any statement that pre-commit runs the full wrapper, that
CI is scoped to `main`, or that the shipped bundle is committed describes the world before this
leaf.

## Historical 260731-EFA-L4 Repository Impact — Closeout Stages Before It Gates

This leaf's subject was wire contracts and typed vocabularies, and most of it is route-local. Three
things changed about the **repository's** shape and rules, and a future agent will get them wrong
otherwise.

**1. Closeout resets the index and stages the whole task worktree before the quality gate runs, and
does not put it back.** Every rail of the gate reads the index — `derive_scope` lists what ruff and
pyright are handed with `git ls-files`, and `diff_coverage` diffs the base against the tracked tree
— while closeout commits with `git add -A`. Everything in that gap, meaning every path a task
*created* rather than edited, went into the commit with no rail of the gate having read a line of
it, and the gate reported green. **Leaf 3's `abc7cbcc` — the commit this leaf is cut from — shipped
four files that way.** `worktrees/modules/closeout.py::_gate_staged_code` now runs
`git reset --mixed HEAD` then `git add -A` and hands the gate exactly what the commit will contain.
The mixed reset is not tidiness: `git add -A` applies ignore rules only to paths git does not
already track or hold staged, so a file staged by a refused attempt stays staged after the leaf adds
it to `.gitignore` and the retry commits it anyway. Resetting first makes every run recompute the
index from the working tree under the ignore rules in force at that moment, which is what makes a
retry equivalent to a first run rather than merely asserted to be.

The end state after a refusal is **staged, not rolled back**, and that is deliberate. The checkout
is the task's own disposable worktree — created by `worktree_start`, destroyed by
`lifecycle_finalize_task` — so nobody is holding a partial staging in it, and `commit_if_dirty` was
going to `add -A` over it moments later regardless. An earlier attempt saved the index file aside
and copied it back; that machinery is **gone rather than fixed**, because it could not survive
`core.splitIndex` or a `SIGTERM` (which is how an MCP server actually dies), and every guarantee it
offered was about a person who is never in that checkout. So "closeout fails **without mutation**"
is no longer the accurate phrasing anywhere it appears — the accurate phrasing is "without any
**commit**".

Two refusals guard the staging step, and because they guard it they run exactly where the gate runs
— when code would commit **and** this checkout carries
`mcp/test_support/agents_remember_test_support/code_quality/check.py`. They are **not** closeout-wide preconditions: a
consuming repository with no wrapper runs no gate, is not staged early, and reaches the ordinary
commit step's own `git add -A` exactly as before; the preview reports that as `wrapper-unavailable`.
Where the gate does run, closeout refuses **before staging anything** when

- the code checkout is **not a task worktree**. The test is git's own — `--git-dir` equal to
  `--git-common-dir` is what a repository's own checkout looks like — rather than the contract's
  `kind`, because that is the property the safety argument rests on: `kind` is a label beside the
  path, the git-dir comparison constrains the path about to be written. This is reachable, not
  hypothetical: `default_series_contract` records `code_worktree = code.repo_path`, so a
  series/master contract reaching `worktree_closeout_apply` would otherwise stage in a checkout a
  person works in — overwriting a partial `git add -p` selection and writing a durable blob for a
  deliberately untracked file. Close out the leaf contract instead.
- the code worktree has **unresolved merge conflicts**. `git add -A` over an unmerged index does not
  refuse; it resolves every conflict to whatever the working tree holds and closeout commits the
  `<<<<<<<` markers. Both refusals run before the reset as well as before the add, because
  `git reset` drops the unmerged entries and `MERGE_HEAD` and would silently disarm the second one.

All **nine** `c-12-closeout/SKILL.md` copies carry this — the canonical `skills/c-12-closeout/`
plus the eight per-harness mirrors — and they are byte-identical after the edit (verified with
`md5sum` and `cmp` across all nine, plus the tenth copy under
`mcp/src/agents_remember/package_data/runtime/skills/`, all `e7279e57604ea6c1871ff918cf713449`, all
mode 644). They are generated, not hand-copied: `scripts/sync-skills.py` fans root `skills/` into
those nine targets (the eight harness roots plus the MCP package-data tree), and drift is caught by
`scripts/sync-skills.py --check` inside `_gate.sh`'s `generated_copy_checks`, which **both** local
hook tiers call. **The hooks are no longer the only net.**
`mcp/tests/test_sync_scripts.py::RealTreeDriftTests` reads the real trees in this checkout:
`test_every_skill_copy_matches_the_canonical_tree` iterates all nine `sync-skills.TARGETS` and
`test_every_runtime_package_asset_matches_its_source` iterates all four `sync-runtime.TARGETS`, both
through the shared module-level `drifted_files()` reader over each script's `diff_target`, which
rebases every entry onto the target so a failure names the copy that has to be fixed rather than the
path it shares with eight others; the assertion message names the `python3 scripts/sync-skills.py`
that repairs it.
Because it is a plain `unittest` class under `mcp/tests/` — the sole `testpaths` entry pytest is
given — it runs in the quality wrapper's pytest step, so a hand-edited mirror now fails at pre-push,
at closeout, and in CI, whether or not the contributor ever installed the hooks.
**Know exactly where that stops.** CI still does not invoke `--check` at all (no workflow runs
`_gate.sh` or any `scripts/sync-*.py`, and the wrapper does not either); the guarantee arrives
through the pytest step, not through a workflow wiring. And the tests are only as strong as
`TARGETS`: nothing asserts that set is complete, so a tenth skill mirror added without registering it
would still drift unseen. `test_sync_runtime.py::test_default_targets_only_write_to_mcp_package_data`
pins the runtime target set exactly that way — `sync-skills.TARGETS` has no equivalent.
The six temp-directory cases in `ReplaceTreeTests` were not replaced and still earn their place: they
test `replace_tree`'s crash-safe copy-then-swap semantics, a different property from real-tree drift.
This now matches the harness trees, where
`test_sync_harness.py::test_every_generated_harness_file_matches_its_source` reads the real
generated files and therefore fails in CI too — the test `RealTreeDriftTests` is explicitly
modelled on.

**2. `.gitignore` gained `.dmypy.json` and `.mypy_cache/`, and the reason is item 1.** Because
closeout now stages the whole worktree, any tool dropping left in the tree becomes staged content
and then committed — it is no longer merely "ignored by ruff". `dmypy` writes a `.dmypy.json`
holding a pid and a socket path next to whatever it was pointed at, and it landed in `mcp/src/`
twice during this task's tooling evaluation; one such file reached this leaf's own first commit by
exactly the path-dependence the mixed reset now removes. The rule and its reason are recorded inline
in `.gitignore` itself.

**3. The production E2E spec now type-checks its happy-path payloads against the wire mirrors, and
its fault-injection payloads deliberately stay untyped.** `dashboard/e2e-production/cockpit.production.spec.ts`
fulfils every endpoint itself, so it faced the same question as a unit fixture: is what it serves a
payload the server could produce? Its happy-path terminal payloads now carry
`satisfies TerminalCatalogRow` / `satisfies TerminalOpenSuccessBody`, which found real drift — the
open response omitted `controlEndpoint` and `controlProtocol` (both declared required by
`TerminalOpenSuccessBody`) and spread `harness`/`controlState` conditionally where the server always
sends the key with `null` when unset, so a client bug behind those keys could not have been caught
there. The `missing`/`malformed`/`contradictory` and 4xx/5xx bodies are left untyped **on purpose
and must stay that way**: their entire job is to be shapes the server should never send, and a
`satisfies` there would delete the test. The third answer is the one to quote back at anyone who
reads the spec as producer-verified: the projection is read whole from `src/fixtures/snapshot.json`,
and the spec's own comment says that is **reuse, not provenance** — the biggest payload in the file
is exactly as unverified as a hand-written one, merely unverified in one place instead of many.

**Be precise about what each artifact pins.** `dashboard/src/fixtures/snapshot.json` remains a
hand-maintained sampled payload. `dashboard/src/types/projection.ts`, however, is generated from
`WorkspaceProjection.model_json_schema()` plus the served projection tail, and
the code-quality `stale_generated_files` comparison detects schema and TypeScript bytes that differ from the generator cit:([`stale_generated_files`], mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:614-620). Fixture builders are type-checked against that
generated mirror, `wireFixtureGuard` refuses fixture-side opt-outs, and `contract.test.ts` measures
how completely the manual sample exercises the mirror. The human-maintained boundary is sample
coverage, not the producer-to-TypeScript contract.

## Historical milestone context: 260727-CHATS-IM-L2 Repository Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The structured Chats path now keeps parent control and siblings usable when one selected child's
history is unavailable or exceeds a bounded source contract. The active projector was decomposed
by mutable authority, and workspace projection ticks gained exact domain invalidation plus
per-file task parsing. The repository's public capability, task, and dashboard surfaces are
unchanged; ownership and failure containment are now explicit in their route overviews.

## Historical milestone context: 260731-EFA-L7 — File-Size Rail And In-Place Facade Splits

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

This master leaf armed the file-size detector (`code_quality/file_size.py`, hard limit 1,200 / architectural failure 2,000+ / emergency cleanup 4,000+, `wc -l` counting, enforced in the project wrapper via `file_size_armed`) and closed the standard's scope loophole (Python source + tests + `dashboard/src` TS/TSX; narrowed "explicitly boring" exception). Over-limit modules were split in place into facades plus private responsibility modules under `kernel/`, `observer/snapshots_impl/`, `observer/reducer_impl/`, and `serving/`, each facade surface pinned mechanically. The test tree was split into in-place families (79 new modules) and the historical CRAP/coverage scope included test roots. Current CCR profile authority separates product measurement from verification inputs: lint/type checks cover both, while product CRAP/coverage does not measure test code.

## Historical Quality Altitude Milestone

The earlier altitude split reduced repeated master-wide work, but its per-leaf acceptance procedure and coverage floor are superseded. Current work uses focused development checks and master-end full aggregation/review without weakening certification owners.

## Historical milestone context: 260731-EFA-L9 Change — First Structural Leaf

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

260731-EFA-L9 is the first leaf that moves code: both serving model monoliths split into the new
`models/conversations/` route (plus `models/terminal_catalog.py` and `models/task_document.py`),
the kernel gained the `kernel/primitives/` vocabulary route, `serving/projections/` took over
the observer projection readers, and `code_quality/layering.py` was built and ARMED as the
package-layering gate (rank violations, cycles, undeclared dirs/imports all fail closed with no
baseline). The move ledger and pre-change serialization baseline prove zero wire drift.

## Historical milestone context: L23 Source-Lineage Enforcement Slice

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

Structural task admission now derives code and external-memory ancestry from
canonical sprint/master/leaf documents and enclosure contracts. The control
plane proves super-to-master and, for leaf roles, master-to-leaf before exposing
a checkout or mutating lifecycle state. Operations projects the same strict
evidence and contract-addressed recovery; no agent must remember a commit,
branch, runtime, or occupant id.

## Historical milestone context: L23 Detached Operation Authority Boundary

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

Checkout isolation now distinguishes four explicit process classes without
turning live coordination into a general CLI capability: long-lived MCP and
dashboard daemons, the plane-owned detached lifecycle-operation worker, tests,
and undeclared checkout execution. The detached worker alone declares
`lifecycle-operation` before loading its services/config because it must claim
and finalize the task's accepted durable closeout or integration operation. It
does not acquire either daemon writer role; an ordinary unpublished checkout
command remains confined to its leaf-local development coordinator and report
root.

## Historical milestone context: L23 Task-Derived Lineage Enforcement

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

Canonical sprint/master/leaf documents and their enclosure contracts remain the sole identity for
source-lineage enforcement. The same transitive code and external-memory ancestry proof now guards
start/resume, the manager's final pre-curator boundary, closeout, and integration. Rechecks after
long quality work and immediately before claim/merge prevent stale work from being documented,
approved, or merged; no agent-supplied runtime or commit identifier becomes control-plane
authority.

## Historical milestone context: R39 Acceptance Topology

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The repository now has one test-capable environment and two lifecycle acceptance altitudes.
Nonce-attested Dagger runs targeted once at leaf closeout and full once at master integration.
Leaf integration, series/master closeout, hooks, push, pull-request, tag, and publish do not rerun
acceptance. Pull requests keep deterministic non-test validation, and the tag workflow proves main
reachability before publishing. Generic runtime doctrine resolves each repository's concrete
acceptance policy from its own memory rather than embedding this repository's Dagger command.

## IAS Contract-Scoped Activation And Disposable Queue Boundary

The task topology has a mechanistic closeout-door surface, but the queue is only a disposable
projection of current task truth and current waiting door generations. It owns ordering and
schedulability, not selection, claim, commit, certification, integration, recovery, or terminal
evidence. An otherwise-valid task mutation never waits on queue or activation state: publication
completes first, invalidates the affected projection to explicit invalid-empty, and rebuilds waiting
candidates from authoritative task/door inputs.

Atomic implementation admission belongs to one replace-in-place activation record per canonical
series contract, addressed by a fingerprint of that contract path. A contract enters `reconciling`
until its exact source pair is current, then becomes `active`; the record is never shared, so one
master's state cannot pause another master that merely shares the sprint's code and memory source
branches. The only activation waiting reason is `atomic-series-reconciling`: a vacant, `active`, or
foreign-master record is never this contract's reason to wait, and a record that does not name the
addressed contract is unreadable rather than adopted. Missing or malformed activation authority
fails closed only for affected runtime admission/projection. Real wave dependencies still gate
through the sprint execution graph's own `predecessor-incomplete:` reasons. Normal readers never
reconstruct activation from task prose, queue rows, legacy files, or ambient Git.

### Atomic-Sequential Default — Developer Ruling (Nothing Serializes A Graph-Less Sprint)

A sprint without an `executionGraph` declares no dependencies, so there is nothing to honour:
**nothing serializes a graph-less sprint.** Independent atomic masters proceed concurrently, no
master is held because another master is selected, and `atomic-sequential` describes the sprint's
SHAPE — every commanded master executes atomically — not a serialization mechanism.
`resolve_scheduling_mode` (`mcp/src/agents_remember/worktrees/scheduling_mode.py`) returns that mode
with both commanded masters in `mode.masters` and a single `facts` string that now states the ruling
("executionGraph absent: atomic-sequential default — every commanded master executes atomically and
no dependency is declared, so nothing serializes the masters"); `commanded_sprint_masters` likewise
records that neither contract presence nor the absence of a graph adds a dependency. Activation stays
per contract — each canonical series contract owns its own record, so two masters that share one
protected source pair keep independent records and one master's `reconciling` state is never a
sibling's waiting reason — and an explicit `executionGraph` wake is unchanged: a graph-backed sprint
still gates its masters on real predecessors (`predecessor-incomplete:`). No new serialization
authority was introduced and no unrelated scheduling semantics changed.

### Known Defect — The Ungoverned `onboarding/skills/**` Tree

`onboarding/skills/**` is a legacy mirror of the code repository's root `skills/**`. The source path
`skills/**` is absent from this memory root's `system/settings.json` `pathRules.include` (the include
set lists `AGENTS.md`, `README.md`, `dashboard/src/**`, `examples/mcp/**`, `installer/**`, `mcp/**`,
`runtime/**` and `scripts/**`), so the tree sits outside normal census coverage — yet the
contract-scoped memory-quality checker still validates it and enforces findings inside it. The tree
is therefore ungated by path rules while still being graded, which is a follow-up decision rather than
a settled design: either bring it into `pathRules` and govern it like any other route, or retire it.
The contradiction is the concrete reason the decision cannot wait: the tree's sibling sidecars (beyond
the four gate-required files) still describe the retired source-pair exclusivity rule — the superseded
"one selected master / paused by the selected master" activation story — while the corrected shipped
skills under `mcp/src/agents_remember/package_data/runtime/skills/**` now state per-contract
activation and the ruling above. Two onboarding trees describing opposite activation semantics is a
known defect of this memory root, not an accepted current-state description.

## IAS Sync And Protected-Source Authority Boundary

Integration and sync remain journaled Git transactions over task-derived protected source refs, but
task-document publication is not serialized behind their long-lived state. This contract's own
activation record starts or resumes a contract-addressed sync whose durable record lives at the
worktree enclosure root and whose exact base, source, and pre-sync commits are pinned in Git refs.
Automatic sync is only phase one: a genuine code or memory merge conflict is retained for agent
resolution and staged `continue`; explicit `cancel` restores provably operation-owned pre-sync heads.
Cleanup vacates only the exact selected terminal contract before its canonical pointer is removed.

## Historical milestone context: 260815-DAG-L14 Sprint Structure Route Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The sprint document now carries first-class seats and typed master links: `SubTaskRef.masterRef`
rows point at the commanded master document and render as real relative links (sprint → master →
leaf click path in markdown and dashboard), `TaskDocument.seats`/`SprintSeat` make sprint seats
structure rather than seat task documents, and `attach_master`/`detach_master` write the typed row,
membership slug, and graph node as one atomic validated batch (L14-R4). Consistency validation
(`validate_sprint_linkage`) hard-fails new-shape drift while legacy shapes surface as facts through
`linkage_report`/`linkageFacts` (L14-R5/R7). The MCP `task_doc` surface registers the new
operations and the dashboard projection carries `seats` + `masterRef`.


## Historical milestone context: 260815-DAG-L12 Route Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The execution-graph render is now human-readable end to end: `tasks/render.py` emits a deterministic mermaid `flowchart TD` diagram (subgraph per master, lump nodes for atomic masters, labeled edges) joined with real titles via the new `tasks/execution_graph_titles.py`, and `observer/projection_graph.py` builds the render-ready per-node `executionGraphView` the dashboard's new sprint-graph wave-grid panel renders directly (pure CSS grid, no layout library — the documented L12-R3 fallback). New sprint-graph sidecars and test sidecars carry the detail.


## Historical milestone context: 260815-DAG-L15 Route Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

L15 (hygiene sweep and review-doctrine repair) landed across the mcp application/tasks/controlplane routes: the served-build preflight gate (`tasks/serving_preflight.py`), the async memory-quality surface (`application/memory_quality_runs.py` + `wait`/`run_id` registration), the typed authoring dialect (judgment-required, move-retargets-edge, node-kind order, named cycle members), `create=False` dry-run locks, and the L7 `worktrees/orchestration_portfolio.py` deletion (recorded decision: doctrine + queue mechanism). The review-doctrine repair (no self-review, evidence-type matching, PR-8, RV-1 extension, D-6 bounded requirement ids) was folded into the memory-repo canonical `system/coding-guidelines.md` Source Comment Scope rule at master level.

## Historical milestone context: 260815-DAG Master Full-Gate Repair Route Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

Thirty-two modules moved into four new packages (`application/task_docs/`, `models/queue/`, `worktrees/queue/`, `worktrees/integration/`); the `task_doc` special ops gained declared `TaskDocResponse` wire fields with the `_sprint_doc_identity` merge (the strict-envelope rejection bug class); `worktrees/modules/closeout.py` and `worktrees/reopen.py` refactored (`_closeout_quality_facts`, `_reopened_contract`); the orchestration-task template heading restored; the dashboard snapshot gained execution-graph/super-to-leaf fixture coverage.

## 260821-CLIVE-L2 Historical Intermediate Architecture

At repository level, L2 established one total configured-contract admission API and one root-local
journal that owns generations, mutation/termination/legacy/direct-landing evidence.
Retry/recover/cancel/revise are task-addressed and evidence-derived. Bounded schema-1 migration and
pre-locator enclosure adoption are explicit, removable tools, never fallback readers. The
selected/in-flight/certified queue rows described by the L2 handoff were removed by L3; current
scheduling is the disposable waiting-door projection described in the Hot Path Summary.

The committed package layout mirrors those owners: public adapters are under `application/lifecycle/`; durable operation authority is under `worktrees/integration/lifecycle/`; direct landing and bounded legacy repair have isolated sibling packages; tool response models live under `models/tools/`; and start collaborators live under `worktrees/modules/startup/`. No former flattened path is retained as a compatibility surface.

### Reconciled Source Evidence

- Closed admission and one public projector. [53]
- Root manifest/journal location authority. [54]
- Task-addressed lifecycle controls. [55]
- Retained-generation projection derives public legal controls and recovery surfaces without owning evidence. [56]

## Historical milestone context: 260824-PDLS — Python Evidence Altitudes

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The repository has one pinned Dagger environment for Python investigation and lifecycle acceptance.
Candidate A's host command, sealed cohort, static closure analyzer, and self-proof were removed
after representative exact-candidate measurement failed to earn their maintenance cost. Its seven
unique product assertions remain ordinary explicit-lane pytest regressions and form the pure cohort
inside the non-accepting representative measurement route. The same master establishes a durable
evidence lifecycle/cadence catalog, product-only Coverage/CRAP, one dependency-ownership graph for
selection and retry, and owner-level causal failure localization. Its package route is documented
at `onboarding/mcp/test_support/agents_remember_test_support/testing/overview.md`; durable workflow
guidance is in `system/tools.md`. Host pytest, direct coverage, and the quality wrapper remain
prohibited, with no compatibility fallback.


## CCR-R12@v5 Current Delivery Boundary

The repository's normal worktree closeout and integration flows complete the approved Git and
external-memory transaction. They preserve explicit developer approval, candidate/source identity,
leases, compare-and-swap/ref safety, and recovery evidence; closeout commits code, mechanically
refreshes and commits substantive memory content when needed, and rebuilds the consumer cache, while integration publishes the
prepared pair without creating a merge commit. Automatic strict code quality, memory quality,
selected certification, curator coherence, and independent review are removed from these normal
routes. Full suites remain an explicit developer request. The dedicated quality/certification and
curation tools remain explicit owners rather than hidden transaction steps.

## Repository Impact Of Terminal Abandonment And Pull-Request Landing

Two repository-wide entities changed. `DocStatus` gained `abandoned` as a second *terminal* value,
and it records a decision rather than a failure: on a master it means nothing of that master
integrated, so its work was deliberately not taken; on a master row it means that leaf's work was not
taken while the master still completed. It carries no reason of its own — the reason belongs to the
declaring operation's audit trail (`skip_step`, `remove_subtask` with a disposition, or the decision
log). `models/task_document.py` publishes the shared `RESOLVED_MASTER_ROW_STATUSES = {"Completed",
"abandoned"}` and `tasks/readiness.py::master_is_terminal` is the one judgement every plane reads, so
the task, worktree, queue and observer routes cannot drift apart on the terminal set.

The second entity is the landing route. `worktree_record_landing` is a new public tool for the
pull-request route: a PR lands on the remote and never moves refs locally, so `worktree_integrate`
cannot express it. Both routes now write the same terminal `integration` cell through one shared
writer (`worktrees/modules/landing_record.py`), and a commit that is not reachable from a landing
target is refused, so the cell cannot be set from a commit that landed nowhere. Retiring a series'
integration branch also changed: it now requires the master's own terminal task state rather than
only an enclosure census, because a child that was never started has no enclosure to walk.

## 260915-CAPS-L9 Scripts-Route Note — A New Generated Mirror And Its Generator Target

The root `scripts/` route gained no new script, but the generator it already owned changed shape:
`scripts/sync-runtime.py` declares a **fifth** target, `eve_runtime/` →
`mcp/src/agents_remember/package_data/runtime/eve-runtime/`, so a whole new **generated** tree now
sits under this route's canonical-folder list. Two facts belong at this altitude because they decide
how the mirror is read anywhere else in the tree: the mirror is **generated content and is never
hand-edited** (the authored source is `eve_runtime/`, and the generator's read-only `--check` is its
only currency proof), and the ignore rule that keeps machine-local trees out of it is **per target**
— only the eve application's own canonical folder carries `node_modules`/`.eve`/`.output`/`.vercel`,
so no other canonical tree can silently lose a same-named directory. The same script now refuses to
report a target whose canonical source is absent as "in sync", because an empty comparison is not
evidence of a synced tree.

## Historical milestone context: 260821-DAGQC-L4 Doctrine And Review Closure

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

Review inventory is NUL-safe and treats every untracked entry as hostile filesystem evidence:
inspect no-follow type, mode, bounded content eligibility, explicit disposition, and race limits
instead of silently following or omitting it. Planning has one effective candidate priority
(candidate override, otherwise master default), while the orchestrator still compares the
portfolio. Graph-less atomic-sequential is a valid ruled topology; strategist skip transfers the
full reasoning duty, and graph adoption from graph-less attaches every master before one complete
nodes-plus-evidence-edges publication batch.

Handover points receivers at the canonical candidate, code ancestry, memory ancestry, and per-leaf
ledger references so they revalidate instead of trusting copied maps. Existing `add_edge` examples
already carried `judgmentId`; no fabricated fix, lifecycle evidence, fake nonce, bypass, shadow
configuration, fallback, or compatibility route was added. Delegated-authority redesign,
disabled-memory behavior, mandatory-graph runtime, and declared-caller trust redesign remain out
of scope.

## Build And Development Reference

Ordinary Python development is supported directly through `mcp/.venv/bin/python -m pytest`; four workers run the isolated unit population. `-m integration` selects the small real-boundary population and `-m ""` selects both. Focused file/node execution, including serial debugging, is valid development work and does not acquire certification authority. The repository declares budgets of **4,000 unit and 1,000 integration** parametrized collected cases (`unit_case_budget` at `pyproject.toml:278` and `integration_case_budget` at `:279`; raised from 3,000 / 600 by the `260918-TSIP-L13` budget-and-landable-closeout leaf on 2026-09-20 under a second direct developer decision, that pair having been raised from 2,300 / 400 by the `260918-TSIP-L7` agreement leaf under a direct developer decision — the first raise on this line that is a **policy** rather than a measurement, because every increment before it was earned from a collected population: 1,500 / 400 by the `260915-KS` master's owning seat, then 2,000 and 2,200 on the merged line, then **2,300** by `260915-KS-L21` over its measured 2,206-case candidate). Extend or consolidate distinct behavior protection before adding cases; do not restore deleted matrices, private-branch tests or unused fixture machinery because an old milestone names them.

Coverage, including changed-line coverage, is diagnostic only. No percentage floor requires additional tests. Production-only CRAP retains 20 as a review trigger, not a delivery blocker; tests and verification support are excluded. Lint, formatting, typing, structural rules and test failures still enforce. Diagnostic-tool execution errors remain visible failures distinct from metric findings. There is no coverage baseline, score-exception registry or ratchet.

Only genuine Dagger admission and the existing lifecycle owners can issue immutable candidate-bound certifying evidence. A host pytest pass, copied report, green helper result or use of Dagger alone is insufficient. Reuse the existing shared engine and preserve process identity, disposable state, credential isolation, exact candidate and publication ownership. Full-suite execution and whole-master independent review belong to the master aggregation boundary under the current execution policy; this overview does not impose either on every leaf. Focused development evidence remains useful without pretending to be final acceptance.

## Key Invariants

- **Nothing serializes a graph-less sprint** (developer ruling): a sprint without an `executionGraph`
  declares no dependencies, so `atomic-sequential` names the sprint SHAPE (every commanded master
  executes atomically) rather than a serialization mechanism; activation is per canonical series
  contract, and a real graph wave still gates through `predecessor-incomplete:`.
- **Known defect: `onboarding/skills/**` is ungated by `pathRules` yet still graded.** The legacy
  mirror of the code repo's `skills/**` is absent from `system/settings.json` `pathRules.include` and
  from normal census coverage, but the contract-scoped memory-quality checker validates it, and its
  sibling sidecars still carry the retired source-pair exclusivity rule. Needs a follow-up decision
  (govern it or retire it); see the boundary section above.

- Controlled prompt delivery has one epoch-bound authority. Request identity/payload is immutable;
  only certified pre-dispatch failure retries; full operation refs complete work; pop-back is an
  atomic server withdrawal of an explicit queued row; PTY paste and adapter/native queues are never
  fallback authority.

- Onboarding should describe current repository state; task files describe planned or in-progress future work.
- `c-08-ar-coordination-context-resolver` skill owns topology and path resolution facts; it must not perform Git worktree operations.
- `c-02-memory-quality-control` skill owns memory quality control: task-start drift detects file-level, overview, inline, and per-entity fingerprint drift; pre-code-commit checks catch new files without onboarding; closeout checks combine integrity and style. It must not update onboarding itself or write temporary reports into durable memory repos.
- `c-05-create-or-update-onboarding-files` skill creates and maintains onboarding artifacts; it must use actual evidence sources rather than citing source registries as proof.
- Task workflows must stop for developer approval before implementation.
- Worktree-backed task workflows must stop again for applicable closeout authority before `c-09-git-worktree-manager` skill closeout creates commits: explicit developer approval for standalone/final/unclear work, or recorded delegated series authority for subordinate accepted-series work.
- The installed runtime `system/AGENTS.md` start-of-task onboarding gate is hard: after drift detection, agents must not silently drop, ignore, or stop using onboarding; they must report update candidates and dirty-source findings, update approved candidates through `c-05-create-or-update-onboarding-files`, rerun drift, and only then continue.
- `c-09-git-worktree-manager` skill wraps task workflows with worktree lifecycle state; it does not replace `w-02-light-task-workflow` skill, starts external-memory worktrees only from a clean committed memory baseline, does not commit, integrate, or clean up without the relevant applicable authority, uses `c-02-memory-quality-control` skill memory quality control after the code commit, refreshes memory, runs `memory_quality_check` before the memory commit, and runs cleanup only after successful integration.
- `c-10-adopt-memory-baseline` skill is an adoption wrapper for existing external-memory onboarding; it does not refresh onboarding; adoption is detected from attributed Git history, and the disposable ledger may be rebuilt.
- `c-03-repo-bootstrap` skill bootstrap memory must keep durable route-local overviews in the mirrored onboarding hierarchy under the resolved onboarding root, use root `bootstrap/` artifacts as temporary promotion/review artifacts, keep low-confidence claims out of durable fact sections, apply candidate excludes before scouting, and hand file-level onboarding semantics to `c-05-create-or-update-onboarding-files` skill.
- `c-05-create-or-update-onboarding-files` skill file-level onboarding remains strict one-to-one with source files and must not collapse file-specific facts into a generic route overview reference; structural route changes route to `c-03-repo-bootstrap` skill rather than becoming disconnected file edits.
- Route indexes are generated availability metadata, not hand-authored truth; overview `## Hot Path Summary` sections and file sidecars are the maintained inputs, and `c-04-retrieval-strategy-router` skill should infer missing sidecars from `sourceScope` plus `coveredFiles`. One validated Git snapshot supplies both repository membership and path-rule eligibility so counts, coverage, and generated bytes cannot observe different filesystem moments; carryover requires explicit official-memory storage authority rather than parser defaults before it may refresh indexes.
- Generated dashboard JavaScript may contain runtime-significant whitespace-only lines. Preserve the
  Vite bytes through raw package sync; only direct shipped `assets/*.js` disable `blank-at-eol`, while
  authored source, generated near misses, and all other whitespace diagnostics remain strict.
- Repo entity catalogs use deterministic `git-blob-set-v1` fingerprints over curated load-bearing evidence files so `c-02-memory-quality-control` skill can flag stale entity memory without semantic guessing.
- The package-owned runtime `AGENTS.md` template set is currently `coordinator`, `skills`, `system`, and `tasks`; memory repos use `system/*` files rather than a root-level `AGENTS.md`.
- Runtime, provider, benchmark, route-index, memory quality, memory, worktree, and skill-install behavior belongs in MCP package modules. Repository `scripts/` still owns build, synchronization and clean-room verification tooling; it is not a competing installed runtime.
- **Ruff owns complexity enforcement as well as hygiene; Radon only scouts.** (Superseded 2026-07-31 by 260731-EFA-L2: this line used to say Radon owned complexity scouting, which was read as a reason to ignore three Ruff complexity rules — deferring enforcement to a tool that exits 0 whatever it finds.) `C901`, `PLR0911`, `PLR0912`, `PLR0915` and `PLR0913` are enforced by `ruff` directly with no baseline behind them; Radon's findings feed refactor planning and must never be recorded as a pass.
- **A configured limit whose rule is unselected is not a limit, and a rule ignored in deference to a tool that cannot enforce is not delegation.** Both patterns were individually invisible and collectively hollowed out this gate. When a suppression cites another tool, check that the other tool can fail.
- **Ratchets, baselines, grandfather lists and burn-down schedules are forbidden in this repository's gates — fix the finding instead.** (Developer ruling, 2026-07-31, overruling this leaf's own plan.) 260731-EFA-L2 built the well-shaped version of that idea — a `quality/complexity-baseline.txt` failing in *both* directions, with an auto-tightening cap, a named owner and a dated burn-down — and then deleted it along with three empty allowlists in `test_gate_scope.py`. The reasoning is that **an exemption list, even an empty one, is a place to put the next offender**; all 67 complexity findings, 274 of 293 long signatures and all 46 CRAP offenders were paid instead. The one surviving carve-out (`PLR0913` on published MCP tool signatures) is a category the coding standard already exempts, is scoped by path rather than by entry, and is held shut by an AST test that fails if it widens.
- Test case budgets are explicit and bounded; growth needs a distinct-protection and runtime tradeoff. Coverage percentages impose no acceptance floor.

- **Derive scope from the tree, never enumerate it.** Every hand-written scope constant in this repository had fallen behind: the wrapper's, the pre-commit hook's, and Pyright's `include`, each silently narrower than the last. `git ls-files` plus a test that asserts the *real* argument vectors reach every tracked path is what makes "the gate covers everything" a fact rather than an intention.
- **A safety guard that lives in one copy of a duplicated function is not a guard.** Six copies of the git runner drifted apart and only one scrubbed the `GIT_DIR`-family repository selectors, which is why every `git` subprocess in the package now goes through `kernel/git_command.py::run_git` and an AST sweep fails the suite if a second spawner appears (260731-EFA-L3). Wrapping the one runner is fine; re-implementing it is not.
- **Nothing on the server's import path may reach the network, and a mitigation must not live only in the test harness.** The tool surface is imported while the MCP handshake is starting, so an import-time download is a startup dependency on egress; the `o200k_base` vocabulary is vendored and a missing one raises instead of downloading. The same rule applies to test scaffolding: `conftest.py` stripped the git selectors at import, which made the production defect *undetectable by any test*, so the redirection tests re-set them inside their own scope on purpose.
- **A gate must be shown the content that will be committed, not the content that happens to be
  tracked.** Every rail of the quality wrapper reads the git index, and closeout commits with
  `git add -A`, so until closeout staged first, a file the task *created* was committed unread while
  the gate reported green (260731-EFA-L4; leaf 3's `abc7cbcc` shipped four such files). The same
  asymmetry runs the other way: an unstaged deletion left a path in `git ls-files` that no longer
  existed on disk.
- **`git add -A` is not idempotent across attempts, so a step that stages must reset first.** Git
  applies ignore rules only to paths it does not already track or hold staged, so a file staged by a
  refused attempt survives being added to `.gitignore` and is committed by the retry. A `--mixed`
  reset before the add is index-only and is what makes a retry mean the same thing as a first run
  rather than merely be asserted to.
- **Staging is safe in a task worktree and unsafe in a checkout a person works in, so the guard must
  test the property, not the label.** A linked worktree is disposable scratch space that
  `worktree_start` creates and `lifecycle_finalize_task` destroys; a repository's own checkout can
  hold a partial `git add -p` selection, deliberately untracked files, and an in-progress merge.
  The refusal compares git's own `--git-dir` against `--git-common-dir` rather than the contract's
  `kind`, because `kind` is a label beside the path while the git-dir comparison constrains the path
  about to be written — and `default_series_contract` records `code_worktree = code.repo_path`, so
  the unsafe shape is producible.
- **A generated contract and a manual sample have different jobs.** The dashboard TypeScript mirror
  is generated and stale-checked from the Pydantic schema; fixture builders plus the fixture guard
  bind tests to it. `dashboard/src/fixtures/snapshot.json` remains hand-maintained, and the contract
  suite measures its coverage. Never describe the sample itself as generated or treat sample
  completeness as the producer-to-TypeScript authority.
- **A downstream integrity check is not a check if the downstream repairs itself.** tiktoken verifies the vendored vocabulary's SHA-256 and then answers a mismatch by deleting the file and re-downloading it, so "tiktoken verifies it" was never the guarantee it read as — inside an installed package that repair is a startup download plus a rewrite of the installed tree. `models/tokens.py` hashes the file itself before handing it over and raises `TokenizerVocabularyError`, which is what makes corruption behave like absence (260731-EFA-L3). When delegating verification, check what the verifier does on failure, not just that it looks.
- Managed provider mode should wrap provider databases and daemon infrastructure in Docker instead of requiring host-level PostgreSQL, FalkorDB, OS service managers, launch agents, package-manager services, or global user daemons.
- Provider runtime artifacts are not durable memory or source data: GrepAI config/state/cache/home files belong under `providers/runners/grepai/`, GrepAI per-root `.grepai/` working directories are git-ignored runtime artifacts, CGC runtime files belong under `providers/runners/codegraphcontext/<repo-id>/.codegraphcontext/`, durable provider database data belongs under `providers/data/`, and MCP/provider operator logs belong under `logs/`.

## Glossary Terms

| Term                     | Meaning                                                                                                       | Notes                                                                                                                                               |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| onboarding unit          | A deterministic documentation unit for one source file or one repo-level entity catalog.                      | File-level units mirror source paths and carry verification metadata.                                                                               |
| entity fingerprint       | A deterministic hash over the load-bearing files that define a repo entity.                                  | `c-05-create-or-update-onboarding-files` skill curates the evidence paths; `c-02-memory-quality-control` skill recomputes `git-blob-set-v1` and flags drift.                                                                 |
| coordination context     | The resolved root/path/settings facts returned by `c-08-ar-coordination-context-resolver` skill for a code repository.                                 | Current implementation exposes `code_repository_name`, `code_repository_root`, `memory_root`, `coordination_root`, repo-specific `task_root`, and `temp_root`. |
| pathRules                | Include/exclude eligibility rules that decide which source paths and file types are managed.                  | Storage and eligibility are separate concepts.                                                                                                      |
| drift report             | A `c-02-memory-quality-control` skill memory quality artifact that classifies onboarding trust.                                              | It is temporary evidence under `temp/drift-reports`, not durable repo behavior; explicit memory-root report paths are redirected to temp.           |
| memory quality check     | The MCP closeout gate that combines drift integrity and memory style checks.                                  | It runs after onboarding refresh and before the memory content commit; task-start work uses the drift-control subset of `c-02-memory-quality-control` skill.                       |
| worktree contract        | Local runtime state file for worktree-backed tasks.                                                           | The parser/writer lives in `mcp/src/agents_remember/worktrees/worktree_contract.py`; `c-09-git-worktree-manager` skill creates and consumes contracts beside the task wrapper's `task.md`. |
| worktree integration     | The approved `c-09-git-worktree-manager` skill phase that lands closed task work back onto source branches.                                | `ff-only` requires unchanged source ancestry; `replay` supports parallel non-overlapping work and blocks conflicts before main moves.               |
| memory baseline adoption | Adopting current external-memory onboarding into attributed memory history with a rebuildable ledger cache. | `c-10-adopt-memory-baseline` skill checks drift first, requires explicit drift acceptance when needed, and delegates attributed content creation to the baseline implementation; cache refresh creates no commit.                                     |
| runtime AGENTS template  | A package-owned `AGENTS.md` source under `mcp/src/agents_remember/package_data/runtime/agents-md-files/`.                                             | Current templates are coordinator, skills, system, and tasks; there is no memory-repo `AGENTS.md` template or expected memory-repo root instruction file. |
| MCP runtime settings     | A trusted settings file outside the coordinator root that controls the MCP server.                              | It provides `coordinationRoot`, `workspaceRoot`, allowed repos/providers, timeout caps, and optional contract paths; coordinator files do not grant authority. |

## What To Explore Next

| Priority | Area / Path                                                                                                               | Why Next                                                                                                            |
| -------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| high     | [mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager) | External workflow metadata and richer task-intake variables are the next likely worktree lifecycle polish area.     |
| high     | MCP-backed scheduled coordination and agent inbox direction                                                                | Future multi-harness coordination could use Agents Remember as a central inbox where Codex, Claude Code, Hermes, and cheaper/background harnesses pick up scheduled or queued work. Do not implement ad hoc timers for current tasks, but when an implementation would strongly benefit from periodic checks, queued work pickup, weekly evals, or scheduled refactors, record that as evidence for a future scheduler/poller system. |
| medium   | [mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow)                                     | The master + light sub-task escalation in the `w-02-light-task-workflow` skill (which absorbed the retired heavy workflow) may need a separate onboarding pass if worktree-backed task folders become common. |
| medium   | [mcp/src/agents_remember/package_data/runtime/system/defaults](agents-remember/mcp/src/agents_remember/package_data/runtime/system/defaults)                                                     | Add richer settings fixtures if cross-repo v2 behavior needs more than the current example files.                   |

## Needs Verification

- An older review recorded unrelated `resolve_auto_editor` checks in coordinator tools guidance. This is historical and was not reasserted against live coordination during isolated L31 recovery.
- The current source registry is useful as a discovery index but has no direct external domain evidence for this repo's own skill/workflow mechanics.
- External-memory closeouts must preserve actual code/memory output identity and attribution. The consumer ledger is computed from that history and must not gate Git operations.
- The memory quality package is now the home for drift integrity and update-history style checks; further quality checks should be added under `memory_quality/style` or `memory_quality/integrity`.

## Historical Review Notes

Updated 2026-08-10T19:57:55+02:00 — No route impact: 260731-EFA-L21 changes the
checkout-only coordination boundary inside the existing MCP package routes; the repo-level
inventory and feature routing remain current. Verification metadata remains pinned until closeout
stamps the L21 code commit.

Updated 2026-08-05T22:30+02:00 — No route impact: 260731-EFA-L16 (the cross-store lock-order repair, its forcing tests, and the coding-guidelines/spawn-doctrine skill chain) is recorded in the `mcp/` and `skills/l-01-agent-lifecycles/` route overviews and their children; this root inventory is unchanged. Verification metadata pinned until closeout stamps the L16 code commit.

Updated 2026-06-28T07:43+02:00 — task 29 S7: refreshed the root Event River, actionable-drift, and dashboard frontend inventory for backend-retained raw events, raw-stream hydration, no frontend count cap, targetless actionable-drift dismissal, and the hidden Lifecycle Flow tab. Route detail lives in the `mcp/`, `observer/`, `serving/`, `controlplane/`, `memory_quality/`, `dashboard/src/`, and `dashboard/src/panels/` route overviews. Verification metadata pinned until closeout stamps the task-29 code commit.

Updated 2026-06-27T22:00+02:00 — task 28 (NOTIFY-AND-CONTINUE turn end): refreshed the Observable session lifecycle inventory row + functional-area section for the new public `lifecycle_turn_end_notification` tool, the non-terminal `awaiting-developer` state, the next-step hint repoint off the now-parked `lifecycle_gate`, and the reducer gate-open/blocked-gate dedup. Route detail lives in the `observer/`, `mcp/tools/`, and `models/` route overviews and their file sidecars. Verification metadata pinned until closeout stamps the code commit.

Updated 2026-06-17T22:45+02:00 after the Engine Room visual-parity pass enriched the dashboard-frontend Feature Inventory row (the 5g G6 atmospheric backdrop + Effects/Calm toggle, the restored HUD decal layer, and the fixed-height `Panel fill` layout); verification metadata stays pinned until closeout commits the source. (Prior: 2026-06-06T12:28+02:00 after adding the public `docs/features.md` tour, replacing README `## Core Model` with `## Core Features`, and documenting the Claude Code root `.mcp.json` detection caveat. Prior: 2026-06-04T10:29+02:00 — documented hidden harness starter packages as source-owned surfaces in the main overview and noted their `l-01` deep-research retrieval-strategy tally requirement. Prior: 2026-05-29T17:30+02:00 — re-spined the public docs and this overview's "What This Repo Is" framing around the three retrieval substrates (by path / by meaning / by relationship) and retired the sidecar-only anti-retrieval positioning. Prior: 2026-05-28T19:52+02:00 — added the Pydantic public response-contract model surface, compact `ContextPacketV2` boundary, and dedicated provider diagnostics feature inventory entries.)

## Historical milestone context: 260821-ARSPAWN-L2 Repository Feature Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

Agent-facing session dispatch keeps `dispatch_agent` as its one public spawn tool, but its durable
identity is now explicitly the canonical `(taskDocumentRef, role)` seat rather than a runtime
session. Same-seat retries converge through pinned-brief evidence, vacancy-safe messages wait on
the address, and staged replacement is resolved only at delivery. Runtime ids remain private
generation/correlation data and are absent from public structural results.

## Historical milestone context: 260821-ARSPAWN-L3 Repository Feature Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The installed vocabulary now makes that runtime contract learnable: free chat compiles the
canonical architect brief and invokes `dispatch_agent` once; role tables say which seats are
plane-hosted callers and which are target-only; product and harness documentation repeat the same
two caller kinds and the no-fallback boundary. Canonical skills and generated package/harness
copies are synchronized projections, not competing authorities.

## Historical milestone context: 260821-ARSPAWN-L5 Repository Feature Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The repository now carries a dedicated `scripts/e2e_harness/` clean-room acceptance route for the
failure that motivated this master. The Dagger graph runs real Codex 0.151.0 against the candidate
MCP server and a deterministic localhost Responses provider, twice from fresh state with no retry.
It proves normally advertised `dispatch_agent` discovery for ambient and hosted callers, byte-exact
architect bootstrap, the ambient-to-worker structural chain, canonical manager addressing through
a real vacancy/replacement, actionable failure evidence, and complete teardown. Production starter
commands remain self-updating; the static pin belongs only to reproducible candidate acceptance.

## 260915-KS-L1 Experimental Knowledge Storage Increment

An experimental master on this repository's branch pair added a knowledge-storage subsystem. It is one primary
requirement (`KS-R01@v1` — stable knowledge identities and immutable invariant revisions) on an experimental
branch, with **no IAS landing implied**, and legacy Markdown remains operational authority throughout.

What exists after this leaf: `mcp/src/agents_remember/memory/knowledge/` (the concrete APSW-backed SQLite
candidate: schema, connection contract, row codecs, typed refusals, one insert-only revision operation),
`mcp/src/agents_remember/models/knowledge/` (the shared frozen vocabulary it writes),
`mcp/src/agents_remember/application/knowledge.py` (the composition seam, and its only consumer), and
`mcp/src/agents_remember/kernel/canonical_json.py` (the single canonical encoder the seal and the schema
fingerprint are computed through). The route overviews are
[`mcp/overview.md`](onboarding/mcp/overview.md),
[`memory/overview.md`](onboarding/mcp/src/agents_remember/memory/overview.md),
[`models/overview.md`](onboarding/mcp/src/agents_remember/models/overview.md) and
[`application/overview.md`](onboarding/mcp/src/agents_remember/application/overview.md).

Two repository-governance facts accompany it, and both are deliberate rather than incidental:

- **`layers.toml` gained charter wording, not a rank.** `[package.memory]` now states that the experimental
  knowledge storage lives there and ranks with the record stores rather than with the application that admits its
  writes, and that consumers ranked below it — `worktrees` and `memory_quality` among them — receive
  `models/knowledge` values or an already-prepared result from `application` and never import this package. No
  rank, order or sequencing entry moved, which is the narrow charter change the leaf document permits.
- **`mcp/pyproject.toml`, `mcp/requirements.txt` and `mcp/uv.lock` gained an exact `apsw==3.53.4.0` pin** — the
  repository's first binary-wheel runtime dependency whose capability is a build-time SQLite option
  (`ENABLE_SESSION`, needed for the session/changeset machinery a later merge leaf requires). The pin is exact
  because that capability belongs to the wheel rather than to the version line.

Scope this increment explicitly does **not** claim: authority adjudication, recommendation, invariant-family
behaviour, the admitted batch contract, snapshot publication, Git merging, portable roundtrip, selective read and
candidate diff, and any product surface. Storing a proposal grants no acceptance — the store manufactures no
acceptance and exposes no promotion operation. The leaf's own review converged to PASS after three rounds with an
empty remaining set; its two material disclosures are the unexecuted macOS spike and the R04 journal-mode
behaviour, both carried for the owning seat.

- The charter paragraph that records the storage home and the one-way import direction, with no rank move. [57]
- The exact SQLite-binding pin and the in-file reason tying it to the session build option. [58]
- The storage package's ownership boundary in its own words. [59]
The requirement this increment implements: requirement packet `KS-R01@v1`, which lives in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address it.
The leaf's independent review, whose final round returned PASS with an empty remaining set: task report `260915-KS-L1-review-fix-verification-2.md`, which lives in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address it.

## 260921-ICR-L19 The Ordinary Retrieval Route Reads The Repository's Published Intent Before Planning

**This route's impact is one capability at repository altitude (ICR-R19@v1): a planner can now read what
this repository already intended, before a task exists.** `application/published_intent.py` resolves the
repository's published knowledge dataset from the ordinary read's own coordination context
(`<memory_root>/knowledge.sqlite`), resolves the source-resolution pair recorded anchors are observed
against, and reads one bounded page per requested path through the shipped selective read
(`application/knowledge_read.py`, reused unchanged) — no task, leaf or enclosure is required. The result
rides the ordinary paired read as a `published_intent` block, so a fresh planner that calls `read_ar_files`
gets the recorded intent beside the source and its onboarding. Every failure is a named state: a repository
that published nothing yet reports `not-recorded` (and source and onboarding research continue unchanged),
while a non-file entry, undecodable bytes or another repository's dataset is `unusable` with the failed
binding named and no rows served.

**The canonical retrieval instructions and their generated copies moved with it.** The retrieval carrier
`skills/c-04-retrieval-strategy-router/SKILL.md` grew 179 → 239 lines: its Intent bullet names the
published-intent half, and a new **Published Intent Before Planning** section states the route, the
publication location the read side declares (with the write-side obligation named as ICR-R20@v1's and the
two-consecutive-task journey as ICR-R25@v1's), the memory-worktree-versus-canonical-root rule with no
fallback between the two, the payload's exact field spellings and its named absences, and the limitation
that a bounded page's cursor continues the scope read rather than the mounted view read. The repository's
own `scripts/sync-skills.py` regenerated all nine in-repo copies from that authored source (this package's
`package_data/runtime/skills/` copy and the eight harness starter folders), and one test derives the
carrier's field spellings from a real payload so the instruction cannot drift into a second vocabulary.
**Six of the seven installed harness skill roots under `~/.agents`, `~/.claude`, `~/.codex`,
`projects/.claude`, `projects/.codex`, `projects/.pi` and `projects/.hermes` still carry the 179-line
carrier** (`c-04-retrieval-strategy-router/SKILL.md` at 179 lines, sha256
`45174b88161cfc57365ac56c27b143cbf1c23f1f032d4f235403d009aedcc66b`, and **no `c-14`** — measured
absent): `~/.claude/skills`, `~/.codex/skills`, `projects/.claude/skills`, `projects/.codex/skills`,
`projects/.pi/skills` and `projects/.hermes/skills`. **The seventh moved while this section kept its
sentence**: `~/.agents/skills` — the root the delivered server reports as `server_info.harnessSkillRoot` —
holds `c-04` at **241 lines**, sha256
`4a8bf5a83d202ca72685aa68c89d575ff4a1870e127d026c8e48273580c09c88`, and `c-14` at **311 lines**, sha256
`87aaacd18fd072563ba71af10ca40a25506d18a00d2c97f5460377cfa036ed8d`, each byte-identical (`cmp`) to the
canonical `skills/**`; the `260921-ICR-L25` curator corrected this on 2026-09-24, when the original
sentence had become false of one of the seven. Installing and verifying the remaining copies is the
orchestrator's acceptance step, not a repository change.

**One memory-tree fact this repository-level section owns, because no nearer overview does.** The `skills/`
tree has file-level sidecars for some skills (`skills/c-09-git-worktree-manager/`, `skills/l-01-agent-lifecycles/`,
`skills/w-02-light-task-workflow/`) but **no `skills/overview.md`** — there is no route-local overview at
that folder, so this root overview (route `.`) is the governing overview for files placed directly under
`skills/`, including the carrier this leaf changed. The generated copy of that carrier under
`mcp/src/agents_remember/package_data/runtime/skills/` is governed by `mcp/overview.md` and has its own
sidecar there.

- **The selection the ordinary route gained, and the shipped read it delegates to rather than duplicating.** [60]
- **The ordinary paired read is the mount point, and the response field the block travels on.** [61]
- **The canonical retrieval carrier, whose new section directs a caller to the route.** [62]
- **The generated copy of that carrier this package ships, regenerated from the authored source.** [63]
- **The case that holds the carrier to the payload's real field spellings, and the constant that reaches the authored skill from the test file.** [64]

## 260921-ICR-L17 The Intent Reviewer's Comparison Identity, Staleness And Refresh

`260921-ICR-L17` (`ICR-R17@v1`) is the leaf that makes a review's *generation* a stated fact on both
sides of the wire:

- **Application.** `application/review_comparison_staleness.py` is a new owner carrying the comparison's
  declared identity and the staleness it earns against a previous binding; `knowledge_review.py`
  (1077 → 1041 lines) delegates to it and deletes its two private helpers rather than aliasing them.
- **Models.** `ReviewSurfaceRequest.previous_binding_digest` is the new optional, sha256-shaped field the
  previous identity travels on — the *previous* identity only, never a substitute for the current one.
- **Serving.** The review route admits `previousBindingDigest` in its own vocabulary, compiles the
  models' published digest pattern instead of re-spelling it, and forwards the value without comparing
  it: whether it is the comparison that is there now is the owners' answer.
- **Dashboard.** `panels/review/ReviewReadCycle.ts` and `panels/review/ReviewRefresh.tsx` take the read
  cycle and the refresh control out of `ReviewSurface.tsx`; `panels/detail-panel/changeSetBar.tsx` makes
  the entry's catalogue read invalidated by the workspace projection the store already republishes; and
  `data/review.ts` gains the ninth client argument and the one spelling of the query parameter.


## 260921-ICR-L22 Managed Git Recovery Rebinding

`260921-ICR-L22` (`ICR-R22@v1`) is the leaf that makes a managed sync **measure itself**: after the
transaction has carried the official line into a leaf, the pair it resolved is compared against the
comparison generation that leaf published, and that measurement is what a reader of the review sees. The
five owners below all route to the more specific `mcp/src/agents_remember/application/overview.md`,
`mcp/src/agents_remember/models/overview.md` and `mcp/tests/overview.md` bodies, which were updated in
this same candidate; this section records the leaf for a reader who arrived at the root.

- **Application.** `application/review_sync_rebinding.py` (733 lines, new) owns the measurement — the
  reviewed identities read from the generation's sealed manifest, the resolved source side re-derived by
  the shipped capture owner, the resolved knowledge side read through the ordinary publication route —
  and it owns the *reason nothing was measured*: a table with one entry per sync state, so a preview, an
  already-current leaf, an unresolved sync, a cancellation and a required choice each say which fact was
  observed instead of one blanket sentence. Its never-raising block runs after the Git transaction and
  its contract write, so nothing here can refuse a sync. `application/review_sync_movement.py` (334
  lines, new) is the read half: it resolves what the leaf's own syncs measured against the selected
  generation and renders it in the review's measured-currentness vocabulary, taking the state from the
  record's own verdict rather than re-deriving it from the channel matches, because re-deriving it
  promoted the record's `unmeasured` verdict to agreement.
- **Application, modified.** `application/worktree_tools.py` (1030 → 1035) returns the `worktree_sync`
  tool result through that block; `application/review_comparison_reopen.py` (730 → 778) gains a fifth
  channel, `sync_rebinding`, read through the record and then checked against the generation itself;
  `application/knowledge_review.py` (1041 → 1054) folds a measured movement into the staleness it
  publishes and carries the movement on the payload.
- **Models.** `models/knowledge/review_sync_rebinding.py` (390 lines, new) is the
  `ar-review-sync-rebinding/v1` record: the reviewed pair, the resolved pair, both channel matches and
  one three-valued verdict, validated against its own fields so an inconsistent success cannot be
  constructed. `models/knowledge/review_staleness.py` (204 lines, new) takes `ReviewStaleness`,
  `ReviewSubmission` and the new `ReviewSyncMovement` out of `models/knowledge/review.py` — which stood
  at 1198 lines against the repository's 1200-line hard rail — and `review.py` (1198 → 1164) re-exports
  all three so its importers and tests keep resolving.
- **Tests.** `mcp/tests/test_review_sync_rebinding.py` (942 lines, new) drives the real production sync
  tool, the real transaction, the real binary-stage knowledge merge and the real publication owner;
  `mcp/tests/test_review_sync_movement_read.py` (356 lines, new) owns the read-side cases, sharing its
  sibling's enclosure fixture rather than duplicating it. Eight consumer rows and two lane rows register
  them, the catalog digest is re-pinned to `d07c2f9d…`, and the split returned
  `mcp/tests/test_worktree_sync.py` to its base bytes — the leaf no longer touches it.

## 260921-ICR-L24 The Family-Centred Review Workspace In The Dashboard

`260921-ICR-L24` (`ICR-R24@v3`) puts the accepted reviewer design on the client, and the delta is
**dashboard-only plus one repository-hygiene repair — it contains zero production Python**. The
walk-completion correction this surface depends on was re-homed to its owner instead of widened into
this leaf: it landed as `5f14fc67` on the master from the reopened L31 enclosure.

Three facts belong at repository altitude rather than on any one route.

**The family vocabulary reaches the browser as a mirror that may not narrow.** `reviewFamily.ts` mirrors
the R31 value tree one-for-one, and its contract is negative: the five context states, the four side
states and the two member content states are distinct facts a rendering must keep apart, and a field the
server omits stays `undefined` rather than being defaulted. The two decisions that carry sentences are
pure and shared — `guaranteeComparison` keeps `unchanged_revision` (one authored revision behind both
sides, the only shape allowed to say "unchanged") apart from `identical_text` (two distinct revisions
whose text happens to match) and from a one-sided record, and `memberComparison` decides from each
member's own carried content, never from revision ids alone, and deliberately carries no sentence at all.
A row whose content fell outside the page is a fact about the page, never a claim that the snapshot
records nothing.

**The paged-collection union and the cursor-less set are two different things.** The union gained
`family_members` because the server accepts it and narrowing the client's union would misdescribe the
wire; the cursor-less set is the smaller `REVIEW_WALKABLE_COLLECTIONS`, which excludes it because
`family_members` is not one walk but the set of per-family roster walks a response composes. A control
offering "first page of family_members" would fetch the server's own refusal, so the family walk is
stated once and continued from the cursor each family's own roster page published — one handler, mounted
by both the tree and the centre, over the same value. The review payload's `family_context` is optional
on the client and its absence is its own fact: it is not a measured zero and is never rendered as
`no_family_recorded`.

**The reader's state outlives the request.** Selection, filter, diff layout, full-file disclosure and the
expanded path are owned once, above the pane switch, because a page request is exactly the interaction
that would otherwise reset them; the surface calls the workspace hook once and passes it down, and no
payload is retained by doing so. The complete source change explorer is one section, mounted once, with
the inventory, its entry-opening controls and its byte-form rows moved out of the surface into their own
module; the surface keeps the three diagnostic panes inside a disclosure, so every control, refusal and
technical identity they carry stays in the DOM and on the keyboard.

**Repository hygiene.** This leaf appends the `temp/` rule to `.gitignore` and untracks the evidence six
earlier closeouts committed because they derive their candidate tree with `git add -A`: fifty-two tracked
evidence files are staged as deletions while the files stay on disk, and `git ls-files temp` is zero.
That repair is repository-level, not dashboard-level, and it is the reason this leaf's diff names any
`temp/` path at all.

**Where the walk's live proof sits.** On this enclosure's bytes the roster walk's live route can no
longer compose the completing page — the enclosure's Python is back at base — so this leaf's walk
evidence is a recorded route body and the *live* proof belongs to enclosure `260921-icr-l31b-ar` at commit
`5f14fc67`, which this leaf replays onto. The assembled `R25@v3` acceptance must re-drive that walk live
on the landed master.

## Authored assessments survive comparison cleanup

The ordinary comparison producer now captures the actual curator-owned assessment inputs for its resolved source and knowledge pair. Reopened history reads the pinned immutable curator generation and retained evidence, while live readiness still validates live inputs. Explicit recovery names both a retained parent comparison and the original curator digest; it preserves the historical operands and authored judgments. An uncaptured channel stays unknown, an empty measured collection stays empty, and missing expected artifacts refuse.

- Ordinary capture preserves the actual owner inputs at the resolved pair. [65]
- Explicit recovery preserves the named historical comparison and curator identity. [66]
