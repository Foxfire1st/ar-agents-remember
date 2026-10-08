# skills/l-01-agent-lifecycles


## The governing row and the rationale cover in the curator hand-off template (260928-MIK-L37)

One file of this skill changed: `templates/curator-handoff-list.md`'s History section. It now says that the writer
fills a row's `items` from the leaf's persisted worklist; that a cover may carry a `rationale`, which replaces a
realization entry's rationale in place; that a row named again replaces the earlier row with its covers; that an
invariant whose record the leaf changed is governed by its `changed` row, which may be named again at an unchanged
revision to correct its effect, because or reason and to carry entry work; and that a family has one governing row,
`changed` whenever the leaf changes the guarantee. The changes reach the package copy and the eight harness starter
copies through `sync-skills.py`. They bind converted memory only.

- The History section: items, the rationale cover, the governing row of a changed invariant, and a family's one governing row. [51]

## The reconsideration row in the curator hand-off template (260928-MIK-L14)

One file of this skill now serves MIK-R14 (reconsideration surfacing):

- `templates/curator-handoff-list.md`'s writer section gains a bullet after the no_invariant row, for converted
  memory only: a **reconsideration row** answers a `reconsideration_candidate` worklist item (a target a decision's
  `reconsider_on` link names changed in the leaf). Its subject is the item's, `reconsider:<DEC-ID>#<alternative
  index>`, with the common fields only. `still_rejected` says why the rejection holds, and the writer refreshes the
  links whose trigger fired to what was judged; when a newer version is approved, or the anchored code changes again,
  after the refresh, a plain rerun is refused and the curator answers the new item by naming its ID in `items`
  (rulings 2026-09-30T10:39:15 and 11:01:18 R5-4, in the second person). `raise` sets the decision
  `under_reconsideration` and appends a question to the leaf's task document through `task_doc`; when the question
  cannot be written the `raise` is refused and the item stays open. The bullet also covers route targets, superseded
  decisions, never reversing a decision, and keeping linked alternatives at their index.
- The same template's decision-record section adds the refusal of a linked alternative moved to another index
  against the memory base (`R14.1-linked-alternative-order`).

The stale-item refusal is not in the template; its message names its own fix (review note R6-3). The changes reach
the package copy and the eight harness starter copies through `sync-skills.py` (`--check` ok). They bind converted
memory only, so no hand-off list of today's memory changes; no role, operation or other template changed.

- The reconsideration-row bullet in the writer section. [1]
- The decision section's reorder refusal. [2]

## The no_invariant row in the curator hand-off template (260928-MIK-L10)

One file of this skill now serves MIK-R10 (unexplained change disposition):

- `templates/curator-handoff-list.md`'s writer section gains a bullet after the planned row, for converted memory
  only: a **no_invariant row** answers an `unexplained_hunk` or `unexplained_file` worklist item in a covered file,
  a change no entry covers that carries no invariant. Its subject is the item's `facts.row` (`hunk:<item id>`, or
  the item's own `file:<path>@<blob>`), its disposition `no_invariant`, and its `reason` says why; it adds nothing
  else. The other answers need no row: attach a `target` to a stored, non-retired invariant, or author a new
  invariant over the change. A delete-only hunk admits only `no_invariant` (ruling 2026-09-30T01:56:39 Q1), and an
  item in an uncovered file is answered by the file's onboarding trace, not by this row (ruling 03:24:28 N2).

It reaches the package copy and the eight harness starter copies through `sync-skills.py`. It binds converted
memory only, so no hand-off list of today's memory changes; no role, operation or other template changed.

- The no_invariant-row bullet in the writer section. [3]

## Decision records in the curator hand-off template and the curator role (260928-MIK-L13)

Two files of this skill now serve MIK-R13 (decision records with rejected alternatives):

- `templates/curator-handoff-list.md` gains the section **"Decision records (MIK-R13)"**: a decision record keeps a
  choice that keeps governing code, as a `records` item of `kind: decision`, with its `context`, at least two
  `alternatives` in a fixed order (exactly one `chosen`, a `reconsider_when` on every rejected or deferred one),
  `consequences`, `decider`, `supersedes` and `admission`; `superseded` is never stored; `links` name what it
  governs and, by alternative index, what should reopen it; requirement targets are resolved by the requirement
  owner and reported, never refused; the ruling travels in the attached entry's evidence (ruling
  2026-09-30T01:45:56 Q1). It lists the validator's refusals, says how to lift decisions at closeout (only real
  alternatives; task-only decisions stay in the task; the curator records and links, never reverses) and gives D18
  as the example.
- `roles/curator.md` Process step 3 gains a four-line pointer: on converted memory, lift the decisions that keep
  governing code.

Both reach the package copy and the eight harness starter copies through `sync-skills.py`. They bind converted
memory only, so no hand-off list of today's memory changes.

- The decision-record section of the hand-off template. [4]
- The curator role's pointer in step 3. [5]

## The admission rule in the curator hand-off template, and the reviewer's OM-4 (260928-MIK-L27)

Two files of this skill now serve MIK-R27 (the admission rule), and one file of a sibling skill:

- `templates/curator-handoff-list.md` gains the section **"The admission rule (MIK-R27)"**: every new
  invariant, family and decision record states the criterion it meets with a one-sentence justification; a
  table of each kind's criteria and meanings, marking the two the validator checks; what **new** means (not in
  the memory base and not an export, where an export's `legacyId` derives its ID, ruling 2026-09-29T23:04:57
  F2); what is **refused** (no criterion, `legacy-unassessed`, a justification made only of references,
  developer-ruling IDs, commit hashes, dates and provenance words, rulings 22:11:24 Q2 and 23:04:57 F1, or an
  unsupported checkable claim); that every other record is only reported; that local stays local; demotion;
  and two admitted, two refused and one local example.
- `criteria/onboarding-memory.md` gains the standing criterion **OM-4, "Admission justifications are
  plausible"**, the reviewer's judgment the packet's rule 5 asks for. It entered **by requirement, not by the
  promotion ratchet** (ruling 22:11:24 Q3), is marked so in its heading, binds converted memory only, and is
  demoted only by a developer ruling.
- `c-14-knowledge-bootstrap/SKILL.md` (a sibling skill) gains the same rule in step 3, with its own two
  admitted and two refused examples.

The paragraphs were rewrapped to 100 columns (ruling F5). All three reach the package copy and the eight
harness starter copies through `sync-skills.py`. The rule binds converted memory only, so no hand-off list,
review or foundation run of today's memory changes.

- The admission section of the hand-off template. [6]
- OM-4, the requirement-bound reviewer criterion. [7]

## The planned row in the curator hand-off template, and the reviewer's declaration check (260928-MIK-L11)

Two files of this skill now serve MIK-R11 (planned invariant effects reconciliation):

- `templates/curator-handoff-list.md`'s writer section (MIK-R12) gains the **planned row**, for converted
  memory only. It answers a `planned_untouched` worklist item — an effect the leaf's task document declared in
  `expectedKnowledgeEffects` that no row delivered — with the item's subject
  `planned:<declared subject>#<effect>`, a disposition (`realized_elsewhere`, `deferred` or `dropped`) and a
  `ref` of the kind that disposition takes; a `dropped` row cites a decision of the leaf's task document by
  its `at`, which the writer resolves through the task owner. A `no_impact` row about the declared invariant
  does not answer the item.
- `roles/reviewer.md`, step 7, gains one line: when the leaf's task document declares
  `expectedKnowledgeEffects`, the adversarial reviewer checks the declaration against the leaf's requirement
  packet, and a mismatch is a finding (architect ruling Q3, 2026-09-29T21:56:18+02:00). It is in the role file,
  not a criteria catalog, because the catalogs admit a standing criterion only with catching evidence.

Both reach the package copy and the eight harness starter copies through `sync-skills.py`. Nothing a producer
emits changes, and no other role, operation or template in this route changed. No real task document carries
the declaration before the L37 install (ruling Q2).

- The planned-row history form in the writer section. [8]
- The reviewer's declaration check in step 7. [9]

## The onboarding row in the curator hand-off template (260928-MIK-L30)

`templates/curator-handoff-list.md`'s writer section (MIK-R12) now serves MIK-R30. Its list of history-row
forms gains the **onboarding row**, for converted memory only: subject `onboarding:<source path>` or
`onboarding:<route>/overview` (`onboarding:overview` for the root route), disposition `no_impact`, and nothing
else. It records that a changed source file's card or its governing route overview was reviewed and needs no
change; a counted change (the Markdown, or a sidecar field other than an anchor's `blob`, line numbers and
`content`) needs no row. On a converted tree only such a change or such a row satisfies the onboarding gate
(architect ruling 2026-09-29T18:49:50 (1)). Nothing a producer emits changes, and no role, operation or other
template in this route changed.

- The onboarding-row history form in the writer section. [10]

## Test proofs in the curator hand-off template (260928-MIK-L28)

`templates/curator-handoff-list.md`'s writer section (MIK-R12) now serves MIK-R28. Its evidence bullet names
both forms in which evidence names a test: a test ID `path::name`, or a path plus symbol `path -k name`
(one identifier, `.py` files; architect ruling). It says that `needs_facet` offers the statement only as a
draft while the curator authors the facet, which states what this test demonstrates and not the invariant's
statement, and that a test file named without a test is `unresolvable`. A new bullet, "Proofs are shown and
counted (MIK-R28)", tells the curator that the `invariant` and `family` views of a converted tree return the
proofs, that the checklist lists the invariants without any proof as information and not as a gate, and that
a curator pass turns a migrated record's "Evidence: …" text into proofs through `proofs`, with an authored
facet. It applies only on a converted memory tree; nothing a producer emits changes, and no role, operation or
other template in this route changed.

- Both evidence forms, and the facet authored beside the statement draft. [11]
- The views, the informational list and the migration pass. [12]

## The file writer's sections in the curator hand-off template (260928-MIK-L12)

`templates/curator-handoff-list.md` gained the section "The file writer's sections (MIK-R12)", after the MIK-R21
section and its "Family routes (MIK-R04)" subsection. It applies only on a converted memory tree; on unconverted
memory, which is every tree until MIK-R37, the installed ingest is unchanged. It documents the curator's side of
the file writer: the list-or-object document with `entries`, `records` and `history`; the curator keys on entries
(`scope`, `admission`, `status`, `invariant_id`, `supersedes`, `proofs`); record items of the ten kinds; history
rows and their cover forms; `handoff:<key>` handles; what the writer fills in; and what it checks. The
`incidental` line now says the writer writes it as `support`. Nothing a producer emits changes. No role,
operation or other template in this route changed.

- The section and the `incidental` decision. [13]

## Family routes in the curator hand-off template (260928-MIK-L04)

`templates/curator-handoff-list.md` gained a **curator-guidance** subsection, "Family routes (MIK-R04)",
inside the informational text-format section: the family record owns its `routes`; Coverage and Non-empty
over `realizes` entries (proofs do not count); routes placed as deep as makes sense (one broad `mcp/` route
passes but is wrong); the root route spelled `.` only when there is no narrower home; `unrealized_family`
and `route_unassigned` reported, not refused; an added route must be a code directory while a carried absent
one is reported for MIK-R06; and `agents-remember knowledge-routes`, whose mechanical suggestion never writes
a route. Nothing a producer emits changes. No role, operation or other template in this route changed.

- The subsection and the command it names. [14]

## Where a hand-off entry lands once knowledge is text (260928-MIK-L21)

`templates/curator-handoff-list.md` gained an **informational** section, "Where an entry lands once
knowledge is text (MIK-R21)", mapping today's hand-off fields onto the text knowledge format: records as
`knowledge/<kind-dir>/<ID>-<slug>.json` that never list their own locations, tests, families or
decisions; writer-minted IDs; each target becoming a `realizes` entry in `onboarding/<path>.json`; test
evidence becoming a `proves` entry; `origin`; and the canonical formatting of `agents-remember
knowledge-format`. It states that nothing a producer emits changes before MIK-R37, and that the template
role `incidental` has no file spelling (MIK-R12 decides its mapping). No role, operation or other template
in this route changed.

- The section heading and its no-change statement. [15]
- `incidental` has no spelling in the file format. [16]

## Explicit sibling selection in curation

A curator adding obligations to a family successor reads and names the exact old membership IDs with authored retention bases. Canonical role, operation and handoff carriers require this selection and published roster readback; no unchanged invariant is revised merely to populate the successor. The existing writer and role boundaries remain.

- The canonical handoff explains exact stored-sibling selection and readback. [17]

## Per-target realization rationale in curation (260921-ICR-L45)

The curator hand-off target shape is now `{path, locator, governing_route, rationale, role}`: each target
carries its own authored rationale (why that place carries the obligation) and an optional role, with the
entry-level `realization_rationale` / `realization_role` as an explicit default. The writer generates no
rationale and refuses an unexplained, non-text, unknown-role, over-long or placeholder-route (`absent`)
target by name before minting; an exact retry of an already committed entry is not checked again. The
canonical template states that its element shape supersedes rule 1's in the external schema note
revision 1 (the rest of rule 1 stands); the curator role (Process step 3) and the curation operation (step
3) carry the same duty, and `c-14-knowledge-bootstrap` step 3 carries it for the foundation route. The
generated copies follow through `scripts/sync-skills.py`.

- The canonical per-target rationale section. [18]
- The stated supersession of the external schema note's rule-1 element shape. [19]
- The curation operation's step 3 duty. [20]

## Curator semantic scope and comparison handoff

The curator authors semantic applicability, conditions and exclusions alongside preserved producer fields before ingest. Ordinary curation records the task comparison through the existing review-record-comparison producer after reconciliation; explicitly unchanged code-only knowledge uses its validated mode. The handoff carries the actual generation identity or refusal. This does not create a semantic closeout gate or authorize a fabricated invariant.

## 260921-ICR-L32 The Seat Policy Moves, And These Carriers Follow It

`260921-ICR-L32` admits `curator` to the taskless seat roles on the developer's 2026-09-24 ruling, which is a
change to **this route's** carriers before it is a change to any card: `roles/curator.md`,
`operations/curation.md`, `roles/bootstrap.md` and `operations/bootstrap.md` (plus `c-14` and `c-13`, which
are separate routes) were corrected first and propagated by `scripts/sync-skills.py` into all ten copies.
The route-level statements this section makes are the ones that changed: the carrier row of
`operations/curation.md`'s comparison table, the read-and-report wording in the bootstrap pair, and the
curator role's own entry paragraph, which no longer says this seat "is opened on a task document" as though
that were the only way it opens.
**The dated form matters here.** L27's seat-policy note recorded the policy of the bytes *that* curation read,
truthfully; this leaf therefore adds a second note rather than editing the first, so a later reader can tell
which revision each sentence was true at. The L20 section above also gains one correction that is not about
the seat: the mounted `knowledge_change` tool now names **both** write-plane entry points, so "the subcommand"
became "the subcommands" — again completed, not deleted.

## 260921-ICR-L27 The Repository-Foundation Entry, And The Seat That Is Not Admitted

`260921-ICR-L27` (`ICR-R27@v1`) puts a repository's **first or resumed knowledge foundation** into this
route's own carriers as a second, bounded shape of the curator's work, and it states the seat gate that
shape depends on. `roles/curator.md` gains the entry paragraph, a process block and the report facts;
`operations/curation.md` gains *The repository-foundation entry* section with its comparison table and
the authority-gate sentence; `roles/bootstrap.md` and `operations/bootstrap.md` gain the first-hour half
— the seat that reads the foundation's state and hands the authoring on **without authoring anything**.

**The rule a reader must not get wrong — a round-one verdict was `blocking` on exactly it, and
`260921-ICR-L32` changed what the rule says.** At L27's bytes a session opened for the curator with
**no task document was refused** — `400 task-binding-required`, "named role scope is required" — because
the opener admitted only the taskless seats (`bootstrap`, `chat`, a plain `terminal` pane) without one,
so **a taskless *curator* seat did not exist** and the pre-task step was carried by the taskless
**bootstrap** seat (which reads the state and reports it) together with the taskless writer an instructed
session holds. **Since the developer's 2026-09-24 ruling such a seat exists**: `curator` joined
`TASKLESS_SEAT_ROLES` in `260921-ICR-L32`, so a document-less curator session is admitted, receives the
curator capsule, and authors the foundation under this seat's own rules; the bootstrap seat carries the
read-and-report half, and the taskless writer is still run by an instructed session whose writing session
must have **no enclosure in scope**, because the writer refuses one (`enclosure_in_scope`) so a bootstrap
can never publish onto a task's line. Every other role is still refused. The carriers state the admission
in the product's own vocabulary: the **ruling** changed the policy, and neither a card nor the procedure
did.

**What stays identical, and what changes.** The reconciliation and the authored knowledge — supported
invariants and facets, justified family guarantees with exact memberships, source realizations, external
sources — belong to the curator on **both** entries, and there is still exactly one admitted writer and
one declared published location. What changes is the **carrier**, the admission and the scope: the leaf
entry needs this leaf's enclosure contract, while the repository-foundation entry has no brief, no change
set and no contract to intake. The `c-14-knowledge-bootstrap` skill owns the procedure; this route's
carriers own who runs it and what its report owes.

**Completion is a named state, not an omission.** The bootstrap role's report gains a
`Knowledge foundation:` line, and the operation refuses to read an absent foundation as a ready
repository: the onboarding and the baseline can both be complete while the knowledge is still
`not-recorded`, and those are separate facts rather than one verdict. The operation's failure table gains
four knowledge rows — `not-recorded`, `recorded` at an exact identity, `unusable` with its shipped
refusal code (`selected_input_unavailable`, `snapshot_unavailable`), and `context-not-admitted` as an
admission failure that is not a knowledge state at all. Neither the onboarding nor the baseline
substitutes for the foundation, and the foundation substitutes for neither.

**Propagation is generated, not hand-maintained**, and no harness skill root was installed by this leaf:
`scripts/sync-skills.py` writes the package-owned copy under
`mcp/src/agents_remember/package_data/runtime/skills/` and the eight self-hosted harness starter copies.

- The foundation entry as a second, bounded shape of the curator's work, with its own carrier and the seat's admission stated **either way** rather than a refusal assumed. [21]



- The operation's ownership paragraph: the manager's half is a leaf-entry fact, and the foundation is reached as the procedure states. [25]
- The comparison table that separates the two entries by carrier, scope, required inputs, writer, onboarding and missing inputs. [26]


- The bootstrap role's step 5: reach the foundation, report the state it read, hand the authoring on, and never report a repository whose knowledge is not recorded as ready. [29]
- The bootstrap role's prohibition: the seat reads and reports the foundation's state and never authors records. [30]
- The bootstrap operation's step 6, with the seat gate quoted and the knowledge step made independent of the operation's other steps. [31]
- The four knowledge rows the operation's failure table gains, keeping `unusable` and a refused admission distinct from `not-recorded`. [32]
- The bootstrap operation's own prohibition on authoring the foundation, and the completion line that carries the foundation's state. [33]
- The procedure these carriers delegate to, and its own statement that a taskless curator seat **now exists** and authors the foundation when no task does — the statement L27 landed in the opposite form and `260921-ICR-L32` reversed. [34]

> **Seat-policy note at L27's bytes (dated 2026-09-24).** This records the policy of the candidate that curation read: code base `06ed70cfcde7e3860ee5b53435727e7512e4335c` plus that leaf's working-tree delta, where `TASKLESS_SEAT_ROLES` was `{"chat", "terminal", "bootstrap"}` and a document-less `curator` session was refused `task-binding-required`. That was true of those bytes and is **superseded**: whether `curator` joined the set was then a product decision under revision, and it was taken in `260921-ICR-L32`. The carrier instructions and their ten generated copies changed first and this memory followed them.
>
> **Seat-policy note at these bytes (L32 curation, dated 2026-09-24T17:20+02:00).** At the bytes this curation read — code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus this leaf's working-tree delta — `TASKLESS_SEAT_ROLES` is `{"chat", "terminal", "bootstrap", "curator"}`: a document-less `curator` session is **admitted** and receives the curator capsule, while every other role is still refused `task-binding-required`. Read the sentences above as the policy **at these bytes**, not as a permanent property of the product.

## 260921-ICR-L28 The Curator Method Grows The Family Plane And The External-Source Manifest

`260921-ICR-L28` (`ICR-R28@v2`) puts the curator's two authored planes into this route's own method
carriers, so a curator seat authors them as part of the same grounded foundation rather than as a
separate pass. `roles/curator.md` gains a numbered step (**Examine family coverage and author it, then
read the two planes back**), `operations/curation.md` gains the same for the reconciliation pass, and
`templates/curator-handoff-list.md` gains the section that **states the shape** of the two keys the
producer never writes — `family` and `external_sources` — beside the existing thirteen fields.

**What the method now says, in the carriers' own words.** For every scoped obligation, decide whether
the evidence and the project's intent justify a **joint obligation**: where they do, author the family
identity, its **own** guarantee text and the exact memberships that place exact invariant revisions in
it; where they do not, record the deliberate `no_family` outcome **with its basis**. An obligation may
belong to several families and several obligations to one. **Nothing is grouped by directory, route,
label or shared anchor**, and an obligation the pass did not examine is left without either key so the
report names it **unexamined** — never as family-free. A member or membership change **prompts a fresh
look at the affected recorded guarantee**; a successor revision is authored only where that is
justified, the earlier revision and its memberships are kept exactly as recorded, and an implementation
change never rewrites member intent or family meaning by itself.

**The external source rule is stated where it is most easily got wrong**: declare what you inspected
with its document identity, its version or retrieval time, the digest of what was read when one was
taken, and the location — the run retains it in a bounded manifest and binds the authored records'
origin references to it, so a document is **never** misrepresented as a repository path with a Git
blob.

**Reading back is part of the step.** `family` and `sources` each carry their own state
(`recorded` / `projected` / `not-recorded`); a plane whose state is not `recorded` measured nothing, and
its null counts are not zeroes. The same coverage travels into the role's record: guarantees authored
and examined with their exact family and invariant revision identities, memberships added/reused/retired,
the no-family bases with their reasons, the measured unchanged sibling members, and every entry neither
plane placed.

**Propagation is generated, not hand-maintained.** `scripts/sync-skills.py` writes the package-owned
copy under `mcp/src/agents_remember/package_data/runtime/skills/` and the eight self-hosted harness
starter copies, which is why this route's change set shows the same three carriers in each of them.

## 260921-ICR-L20 The Curator's Authoring Step: The Real Writer, And The Publication It Reads Back

This route gained **one obligation in two carrier files**, and it is a route-level fact rather than a
paragraph of instruction: the curator seat's own lifecycle and its curation operation now state the
**real** knowledge-authoring invocation instead of leaving the reconciliation's requirement-shaped items
to be written as prose.

- **What the two carriers now say, and why it belongs at this altitude.** `roles/curator.md` gained a
  numbered authoring step (invoke `agents-remember knowledge-ingest … --baseline … --publish --commit
  --json`), a permitted-action line naming that route, a prohibition on writing the dataset itself, and
  a handoff obligation to carry the read-back identity. `operations/curation.md` gained the same step in
  its procedure, the authority-gate paragraph that keeps the batch and publication owners where they
  are, a rule that a partial or refused hand-off stays partial, and the handoff paragraph that carries
  the per-entry outcomes and the published identity. Both state one discipline: **consume the report,
  not the exit status.**
- **The route-level rule a reader should carry away.** `--commit` remains the *knowledge-batch* write
  word — not a Git action and not an acceptance — and `--publish` is an explicit selection of the
  repository's one declared published dataset location, never a default implied by committing. The
  mounted `knowledge_change` tool is not a write route at all (it refuses every kind and exists to name
  the real one), so the carriers must keep pointing at the subcommand — and since `260921-ICR-L32` that
  naming is **two** entry points, not one: `agents-remember knowledge-ingest` on a leaf enclosure's
  ordinary route and `agents-remember knowledge-bootstrap` on the taskless repository-foundation route.
  At L20's bytes only the first existed, which is why this section said "the subcommand" for as long as
  it did.
- **These are canonical source edits, and the generated copies follow.** `skills/` is the canonical
  tree; the harness starter packages and `mcp/src/agents_remember/package_data/runtime/skills/` are
  generated from it by `scripts/sync-skills.py`. This leaf ran the generator and its `--check`; **no
  harness skill root was installed**, which is the orchestrator's own acceptance step.

- **The authoring step the curator role file now carries: the real invocation, what to read from the report, and the identity the handoff owes.** [35]

- The authority gate that keeps the batch and its publication with their existing owners, and the rule that a partial hand-off stays partial. [37]

- The permitted-action line naming the subcommand. [38]
- The prohibition that makes the mounted tool's refusal the carrier's own rule. [56]

- The handoff paragraph both carriers gained, which is what makes the published identity travel with the report. [39]
- The read route whose declaration the write side now publishes to, restated as current truth in the retrieval carrier. [40]

## Purpose

This route owns the canonical instruction sources and routing metadata for native role capsules. `SKILL.md` is the thin selector; `roles/` owns role duties, `operations/` owns the selected procedure, and the handover carries canonical task/workspace facts separately. The native launcher exposes Architect, Investigator, Orchestrator, Manager, Worker, Reviewer and Curator. The ten-role registry remains a compiler vocabulary; it is not evidence that every registry role is launched through this path.

A native capsule selects one explicit supported role source followed by one applicable operation and injects no shared `core/` block. Projects is an execution workspace, not a registered repository. Manual taskless Architect/Investigator launches ask only for missing outcome/repository or concern/report scope and do not synthesize tasks.

Paseo runs agents and delivers their messages. AR’s bound `agents-remember-task` tools retain canonical task, knowledge and paired-Git ownership. A delegating Architect hands coordination first to one Manager for one master, or to one Orchestrator on the sprint for two or more concurrently worked masters (one Manager per master); direct coordination and a single-master Orchestrator are the developer’s choices. Existing dated corpus measurements remain facts of their frozen candidates and do not measure the current capsule or establish context savings.

## Hot Path Summary

Manager, orchestrator and curator handoffs name actual code/memory output refs and scoped onboarding evidence. They never require a ledger commit, cache freshness proof or cache-repair transaction; downstream consumers can rebuild the ledger from committed attribution.

## Detailed Route Context

### IAS Planning-To-Runtime Boundary

Planning truth is upstream of runtime scheduling. Architect, strategist, and orchestrator seats may
author otherwise-valid task changes without asking a closeout queue or atomic-series selector for
permission. A material task change invalidates the affected disposable projection and causes the
waiting frontier to be recomputed from current truth; it does not freeze task authoring.

Multiple live atomic masters on one protected source pair are normal. Implementation admission is
contract-scoped: each canonical series contract owns its own activation record, so selection
publishes `reconciling` for that exact contract — which suspends nothing and excludes no other
master — and the contract becomes `active` only when both of its own protected source tips are
current. One master's selection never pauses another, and multiple nonterminal contracts remain
valid. Role doctrine must treat retained sync conflicts as agent-resolvable, resumable, or
cancellable worktree state, never as a reason to rewrite planning around a stuck queue. Exact changed
doctrine files and synchronized copies are reconciled to the frozen candidate; commit verification
remains closeout-owned.

Nothing serializes a graph-less sprint. A sprint without an `executionGraph` declares no
dependencies, so the shipped `atomic-sequential` default describes the sprint's SHAPE — every
commanded master executes atomically — and is not a serialization mechanism: independent atomic
masters proceed concurrently and no master is held because another is selected. Only an explicit
`executionGraph` gates masters on real predecessors (`predecessor-incomplete:`).

Free chat launches ordinary role-shaped work by compiling `templates/architect-brief.md` from
current sprint truth and calling ambient `dispatch_agent` exactly once on the sprint document; no
plane-injected hosted identity selects ambient-launcher mode and the request carries no caller
identity. An explicit developer-declared task-seat takeover instead targets the named role on its
canonical task document in the same ambient mode. After the first Architect exists, hosted role
seats start and reach eligible roles with native `role_start` and `role_message` on
`agents-remember-task`, keeping the returned agent IDs and their direct-child scope; a refusal
names its rule or reason and never becomes an ambient retry. Source-lineage conflicts remain resumable through the
contract-addressed sync continuation until a genuine semantic ambiguity requires escalation. The
internal session primitive and readiness/brief correlations remain control-plane details. The architect owns sprint composition and the initial ruled topology.
When the graph is missing or materially stale, an approved strategist authors the evidence-cited
plan before the orchestrator exists. The orchestrator adopts that plan, recomputes its ready
frontier after material events, and records every queue or reprioritization judgment with rationale,
evidence, author, confidence, and supersession. Structural task document plus role remains the
durable address at every altitude.

An organizational master is a logical grouping whose ordinary leaves branch directly from the
current super line and may land independently. An atomic master keeps its own integration branch
and exposes no partial result; each contract's own activation record controls that master's
implementation exposure, while a separate landing authority serializes conflicting protected-ref
movement. That ref-landing exclusion is not sprint scheduling: nothing serializes a graph-less
sprint's masters. Mechanisms publish facts and candidate sets; architect, strategist, orchestrator,
and manager seats retain their explicit judgment boundaries. Integration lines are not repair
workbenches.

Role continuity is task-document and artifact based. Workers build and report, reviewers provide
independent verdict evidence, curators reconcile system intent and memory, managers decide
delegated leaf gates and integrate a master, and orchestrators govern master handovers. Direct
`role_message` hand-overs between the leaf seats replace role-local polling and inference.

Reviewer is polymorphic without becoming ambiguous: it binds the exact leaf, master, or sprint
being reviewed, while the plane stamps the generation's parent document+role. Managers therefore
own leaf and master-exit review, the architect owns plan review, and the orchestrator owns super
review. An unstamped sprint reviewer cannot route because choosing between those two sprint planes
would be invented authority.

Requirement completion is an exact-set protocol. Before dispatch, the manager compiles the stable
IDs inherited from the master and owned by the leaf. The worker must write one acceptance envelope
per ID with delivery and verification rationales, independently inspectable citations, and exact
commands/results or durable evidence. The reviewer receives the same set, inspects the artifacts
itself, and accepts or rejects every ID separately; an invalid citation, wrong evidence class, or
missing developer ruling is a requirement rejection and prevents an overall pass. Non-code work
uses deliverable paths plus stable section anchors rather than invented code fields.

Requirement revisions, delivery attempts, and internal protocol events are separate. Semantic
revisions require explicit developer approval. Workers advance immutable exact-candidate attempts
only at review handoff or after reviewer rejection; internal implementation/test/evidence reruns
remain separate protocol events. Lightweight requirement-specific records link content-addressed
expanded evidence, reviewers append independent adjudications, and rejected work advances through
linked successors with one closed failure class. Accepted attempts remain closed across unrelated
later candidates; only direct-regression proof plus bounded owner invalidation or an approved
requirement revision can reopen them. Leaf journals remain authority while the master summary
excludes protocol events, is rebuildable, and never gates tasks, lifecycle, closeout, integration,
or queues.

Implementation and leaf work run focused host diagnostics freely — direct host pytest (units by
default, `-m integration` for the small integration population) and targeted Vitest, with Ruff,
formatting, Pyright and Radon as the repository's static checks. The repository's old
`scripts/test-python` wrapper remains deleted and is not recreated. The pinned Dagger graph is the
explicit certification ladder
for Agents Remember when it is requested: leaf closeout selects targeted mode exactly once, leaf
integration and series closeout do not rerun it, and master integration selects full mode exactly
once, each against the task-derived explicit diff base. A hard cap remains an explicit
constrained-lifecycle setting rather than role-local judgment. Transactions launch no optional
quality; the Curator's complete leaf-scoped memory-quality check and coherence remain standing
curation obligations.

A curator completes only after the current-additions missing-onboarding check and full leaf-scoped
memory-quality worklist have been repaired and rerun. Dirty-source drift and future commit-derived
verification can be classified as closeout-owned only after no repairable citation, claim, shape,
history, entity, or index finding remains. The curator then publishes the sole structured,
candidate-bound coherence authority through the lifecycle API; generated Markdown is only its
human-readable projection.

Before that curator is created, the manager requires the leaf's task-derived source-lineage
projection to be current and includes it in the complete brief. The native start re-proves lineage
before host creation, so a parent move between status and start fails closed.

## Conventions

- Edit doctrine in canonical `skills/`; `scripts/sync-skills.py` generates the package and eight harness trees.
- Select role/operation from explicit handover bindings; do not infer tasks, repositories or owners from chat/workspace names.
- Use exact task-read arguments, returned canonical document paths and the bound tool schemas; preserve durable prior approvals.
- Use native `role_start`/`role_message` with actual returned IDs and same-request reconciliation; a developer question goes to the parent when one exists, and only a parentless or unreachable-parent agent asks in its own chat.
- Keep current role/operation contracts separate from retained reference/registry history. A retained core map does not inject shared instructions.

## Invariants And Boundaries

- Each task-bound role preserves its exact canonical requirement, paired workspace, report and admitted write surface.
- Worker implements code and leaves it uncommitted; Reviewer independently supplies verdict evidence; Curator owns admitted memory/knowledge. Task and paired-Git owners retain semantic acceptance and publication.
- Normal curation preserves MIK’s converted entries/records/history writer, authored target rationale, exact family/sibling coverage, full contract-scoped MQC and required coherence. Explicit report-only admission claims none of that normal pass complete.
- Unknown execution or refused capability does not authorize another owner, transport, runtime writer or workspace.
- A finished turn, review, curation, semantic acceptance and paired-Git publication remain separate evidence-bound facts.
- Commit-derived memory attribution follows the real source commit through the governed closeout owner.
- Per-requirement worker/reviewer evidence is preserved; aggregate completion prose cannot replace it.


## CCR-R12@v5 Lifecycle Boundary

Workers provide targeted checks and curators provide scoped onboarding checks with honest failed or not-run states. The prepared code and memory-content outputs move through the authorized Git transaction, whose commit legs suppress automatic quality and test hooks. The consumer ledger is refreshed without a commit while ordinary explicit Git hook policy outside the transaction remains unchanged; full quality, full tests, certification and independent review require an explicit developer request, while the Curator's complete leaf-scoped memory-quality check and coherence remain standing curation duties. Requested reviews retain the sealed monotonic three-round rule.

## 260928-MIK-L99 — a leaf's agents hand over to each other

The lifecycle route now states the leaf-seat direct loop and the all-role harness freedom: the Worker, Reviewer and Curator hand exact objects between their seats, the Manager keeps only its named occasions and the gate, and every role organises its assigned work with its own harness inside the seat's boundaries.

## 260928-MIK-L93 — a question for the developer goes up the chain

Every delivered role and operation now routes a developer question to the parent named in the handover, with the busy/pending report recovery, the unreachable-parent own-chat exception and the quoted developer answer; the parentless and dashboard behavior is unchanged. The handover constructor's `developerQuestions`/`ownerRelation` values follow parent presence for every role, with the leaf seats' direct peer routes preserved, and the four transportable `role_message` refusal remedies name the parent first. The retired own-chat sentences and the old Manager/Orchestrator forwarding prohibition are registered in the sixteen-statement R93 census and guarded by an independent negative test.

## Evidence

### Repo-Internal References


- The graph-less atomic-sequential default describes sprint shape; nothing serializes a graph-less sprint. [43]
- The architect launcher packet is one canonical compiler contract, not fixture prose or a second brief. [44]



- The shared frame defines the mandatory per-ID worker envelope and independent reviewer disposition. [48]
- Core acceptance doctrine defines the mandatory per-ID worker envelope and the independent reviewer's adjudication. [49]

Current working-candidate evidence for this route:

- Lifecycle publication and recovery carry the actual code/memory outputs. [50]

## L23 Pre-Dispatch Lineage

Canonical lifecycle guidance now places task-derived ancestry before process
creation: managers require current master lineage and leaf roles require the
full chain. Refusal creates no child and recovery is contract-addressed, keeping
commit/session identity inside the control plane.

## R39 Repository-Resolved Quality Doctrine

The lifecycle skill is repository-generic: roles and briefs resolve executor, environment,
arguments, retry, resources, and evidence from the active repository memory. The cross-repository
cadence remains fixed at leaf closeout once and master integration once, with no leaf-integration
rerun and no inferred fallback.

## 260815-DAG-L14 Doctrine Route

The `l-01-agent-lifecycles` doctrine was synced to the atomic `attach_master` flow and the
first-class sprint seats structure: `roles/orchestrator.md`, `roles/strategist.md`,
`roles/architect.md`, `criteria/plan-review.md`, and `templates/orchestration-task.md` all
updated, with canonical and generated copies kept identical by `scripts/sync-skills.py`.

## 260815-DAG-L15 Review-Doctrine Repair

The review doctrine route was repaired: `roles/reviewer.md` gained the Review Independence and Evidence-Type Matching section (reviewer seat ≠ author seat; rendering → mounted-UI proof, scheduling → operation-level proof, data model → artifact-level proof, doctrine → code anchor); `roles/orchestrator.md` gained the independence paragraph; `criteria/plan-review.md` gained standing PR-8; `criteria/report-verification.md` extended RV-1 to `git diff --summary` mode rows; `criteria/doctrine.md` gained D-6 (bounded `L<leaf>-R<n>`/`S<n>` requirement ids allowed — reconciled with the memory canonical Source Comment Scope rule, folded at master level); `templates/verdict.md` gained rule 7 + the author-seat row; `templates/manager-brief.md` gained the independence/evidence line; `SKILL.md` extended the three-party-loop paragraph. All 9 generated copy trees stay byte-identical via `scripts/sync-skills.py`.

## 260815-DAG Master Full-Gate Repair Route Impact

The `templates/orchestration-task.md` heading was restored to `## Canonical executionGraph Adoption Payload` (the `executionGraph` qualifier phrase restored); all 9 generated copy trees re-synced byte-identically via `scripts/sync-skills.py`.

## 260821-DAGQC-L2 Curator Call Synchronization

No lifecycle topology or authority changed. The curator brief now demonstrates the canonical
discriminated memory-quality request so fresh seats do not reconstruct the retired flat grammar.

## 260915-CAPS-L18 Complete Curation Reaches This Route

CAPS-R18@v1 inverted the optional/narrow-curation doctrine in the shipped instruction sources. The
sentences that presented the full `memory_quality_check` operation and the `curator_coherence`
certification as developer-request-only diagnostics, "never routine closeout/integration prerequisites",
are gone. The rule is now normative: **curation is complete on every leaf** — the full operation runs at
the leaf's contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every
curator-actionable finding is repaired or escalated as blocked with its exact returned code, and the
operation is re-run after every repair until `curatorActionableCount=0` and the **raw**
`qualityChecklistStatus=ready-for-closeout`. The **combined** `checklistStatus` is rewritten to
`coherence-required` **only when the coherence record is then missing or stale** — that is the coherence
gate, cleared by publishing the `curator_coherence` authority with `prepare` → `publish` → `validate`.

**Field-name correction (`D35`, made by 260915-CAPS-L10).** The sentences above and in the shipped
sources previously named `checklistStatus=ready-for-closeout` as the loop's termination condition. The
loop's gate is the **raw** `qualityChecklistStatus`; the **combined** `checklistStatus` is rewritten to
`coherence-required` **only when the coherence record is then missing or stale**, which is the coherence
gate that `prepare` → `publish` → `validate` must clear. On the success path, where the record is already
current, the combined field is **not rewritten** and keeps its incoming `ready-for-closeout` value, with
`closeoutReady=true`; so `ready-for-closeout` *is* a value the combined field can hold, but only once the
whole pipeline is already complete. Read the raw field to decide whether the repair loop can end, and the
combined field to decide whether the coherence gate applies; `closeoutReady` is `true` only after the
coherence authority validates (`application/memory_quality/controller.py:664`, `:671`, `:678`,
`:685-687`). A curator following the old wording watches the combined field sit at `action-required` while
repairs are outstanding and then flip to `coherence-required` at the exact moment they finish — the gate
it waits on is unsatisfiable precisely while the wait matters, and the next required action is not a
repair at all.

**Warrant corrected by `CAPS-R19` (leaf `260915-CAPS-L19`).** The `D35` correction above originally rested
on the sentence *"`ready-for-closeout` is never a value of the combined field."* That absolute claim is
**literally false**, and `CAPS-R19`'s revision note records it as superseded by the three-path model now
stated here. The field-name correction it supported still holds; only its stated warrant was wrong.
**Attribution is complementary and both halves hold:** `260915-CAPS-L10`'s curator corrected the
**onboarding cards** that carried the wrong form, while `CAPS-R19` corrected the **shipped sources** — the
five loop-gate carriers, their nine generated copies, and the guard registry's own docstring — and brought
`docs/reference/mcp-tools.md` into both the loop-gate census and the guard's `LOOP_GATE_DOCUMENTS`.

Two corrections the inversion must not collapse, both preserved: closeout still owns only the Git
transaction and **invokes** nothing — it **carries** the completed curation as a prerequisite; and the
rule is about the completeness of curation, not about unscoped runs, so "complete" always means the whole
operation at the leaf's contract scope. The ruling is forward-looking: the already-landed and finalized
leaves are not re-curated, and whole-layer completeness is discharged by L11's full-scope run at the
frozen tip.

## Ungoverned Mirror Status (known defect)

This route overview lives in the `onboarding/skills/**` tree, which mirrors the code repository's
`skills/**` route. `skills/**` is absent from `settings.json`'s `pathRules.include`, so this whole
onboarding tree sits outside normal onboarding census coverage: it is legacy and ungoverned. It is
retained here only because the contract-scoped memory-quality checker still validates these documents
whenever `skills/**` is part of a leaf's changed set, which is exactly why this overview was updated
by hand rather than by a governed maintenance pass. The remaining sibling sidecars under
`onboarding/skills/**` — the other role, criteria, and template cards — are knowingly stale and are
deliberately left untouched pending a follow-up decision on whether this mirror should be governed or
removed. That mismatch between the declared path rules and the enforced checking scope is itself the
recorded defect.

**260915-CAPS-L1 decision, recorded rather than implied.** This leaf rewrote the canonical route (the
router became a thin router; `core/` · `operations/` · `reference/` · `composition-manifest.json` were
added; all nine role files were rewritten), so a contract-scoped quality pass reports this route's
unmodified bodies. The curator updated **this overview**, because route meaning genuinely changed and the
overview is the right home for it. It deliberately did **not** refresh the legacy role/criteria/template
sidecars under `onboarding/skills/l-01-agent-lifecycles/**`: they sit outside `pathRules.include`, they are
already declared knowingly stale by this section, and a partial hand-refresh would leave them
inconsistent with each other while duplicating the governed cards that do exist — the 18 new and 17
updated cards on the tracked generated copy under
`onboarding/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/**`. The follow-up
decision this section already asks for (govern or remove the mirror) also determines whether those cards
should be refreshed or deleted, so resolving it now by hand would prejudge it. No fingerprint or
verification stamp was advanced.

## Current native instruction evidence





## Retained pre-import corpus account and measurements

The following text is retained verbatim from the pre-import source account. Its dated measurements, source counts and old composition vocabulary describe those recorded candidates; the current native contract is stated above.

### Former Purpose

This route owns canonical lifecycle doctrine: the session router, the shared `core/` blocks, the role
registry, the nine self-contained role lifecycles, the eight `operations/` procedure blocks, the
reference-only rationale and rulings, the composition manifest, dispatch briefs, durable reports, review
criteria, and authority templates. Generated package/harness trees mirror this route and never define
independent behavior.

260915-CAPS-L1 restructured this route: `SKILL.md` is now a **thin router with no doctrine** (620 → 179
lines), `core/` · `operations/` · `reference/` · `composition-manifest.json` are new, and all nine role
files were rewritten into one readable order (purpose/authority → required inputs → normal workflow →
permitted writes → stop/escalation → completion/handoff, then the knob block) with an `**Inherits:**`
line naming their shared sources. A role file now names a sibling role file only to wear that hat or
dispatch that seat.

**That restructure is a structural change, NOT a measured context reduction** (labelled by
260915-CAPS-L10, which measured the capsule this corpus feeds). The `620 → 179` line count describes the
**router**, and the doctrine it used to carry moved into the new sibling layers rather than disappearing:
the corpus a session reads is now selected per role and per operation by the deterministic compiler, and
nothing in that arrangement was measured to be smaller. The one measurement that exists points the other
way — at the worker elevation the delivered capsule is **11,828** tokens against a **5,928** token legacy
startup chain (**+5,900**; like-for-like `implementation` capsule 11,645, **+5,717**), the manager and
architect elevations are **UNMEASURED** (`binding-unresolved`), and **adoption acceptance FAILED** with
disposition **REVISE**. Obligation preservation is intact (**36/36** across ten declared roles plus
launcher routing), so the failure is on the reduction half alone. Full account, frozen artifacts and the
residuals with their owners: `notes/reports/260915-CAPS-L10-worker-report.md`,
`notes/reports/caps-l10-disposition.md` and the measurement method
`notes/reports/caps-l10-measurement-method.md` (digest `sha256:902676a6…`). **No card may describe this
corpus, the compiler or the cutover as saving context**; the design intent was a single-source,
role-addressed corpus, and that intent is what this route may claim.


### Former Conventions

- Canonical role doctrine lives under `roles/`; templates feed complete role inputs.
- Shared rules live in `SKILL.md` and are not restated as competing role-local variants.
- Runtime package and harness copies are synchronized artifacts of the complete canonical tree.
- Current intent stays in default bodies; semantic history records transitions without leaf diaries.
- `dispatch_agent` is the sole public spawn verb; caller kind is derived from process context, never
  selected in the request.
- Role-table `dispatch` and `tools` rows are fixed authority/capability documentation rather than
  settings knobs.


### Former Invariants And Boundaries

- Runtime ids never become model-held work addresses.
- Spawn ancestry is provenance, not responsibility topology.
- Each role acts only at its assigned task altitude and authority boundary.
- Initial briefs are exact-pinned; ordinary messages re-resolve current structural occupants.
- Ambient bootstrap and plane-hosted child dispatch share one exact-brief transaction, while their
  authority checks remain disjoint and never fall back into one another.
- Curator completion requires zero curator-actionable findings from both required onboarding checks;
  the structured coherence authority is published only after their repair-and-rerun loop.
- Commit-derived memory verification follows the real code commit during governed closeout.
- Aggregate completion prose cannot replace the worker envelope or reviewer adjudication for any
  stable requirement ID.

## Scoped investigation and exact execution identity

Investigator replaces the earlier narrow provider/system role with one scoped concern of any kind. Architect, Orchestrator and Manager may start it within their admitted non-leaf selections. Its broader reading requests preserve report-first remediation and the strict code/memory/task owner boundary; earlier identity spellings remain read aliases rather than separate roles. Generated mirrors derive from this canonical instruction tree.


- This source owns the route’s Investigator selection or execution boundary. [57]


## Refreshed current evidence

- The curator process distinguishes leaf ingest from taskless bootstrap and preserves enclosure-scope refusal. [22]
- The report facts the foundation entry owes instead of a leaf's, inside the seat's own output section. [23]
- Permitted actions name both admitted writer entry points and refuse taskless bootstrap within an enclosure. [24]
- The authority gate that names both writers and keeps the knowledge batch and its publication with their existing owners. [27]
- The handoff paragraph: on the foundation entry the same facts come from the bootstrap report, with the areas a partial run did not reach named as not reached. [28]
- **The same obligation in the curation operation, with the invocation spelled out and the report's consumed fields named.** [36]
- Shared routing, authority, loop, and dispatch doctrine is canonical here. [42]
- Curator owns conservative three-way memory reconciliation, the complete pre-closeout onboarding worklist, and structured authority publication. [45]
- Manager owns one real master and its leaf closeout chain. [46]
- Worker owns one real leaf's implementation and durable report. [47]
- Current supplied role/operation, Projects scope, bound tools and execution/semantic separation. [52]
- Role then operation, inert core and retained vocabulary distinction. [53]
- Bound intake and preserved converted writer/family duties. [54]
- Normal full curation and coherent handoff. [55]
