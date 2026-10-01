# skills/l-01-agent-lifecycles/templates/curator-handoff-list.md

## Governing Overview

[lifecycle skill overview](../overview.md)

## Purpose

Defines the producer/curator handoff data boundary. Nine producer fields travel unchanged; the curator resolves the outcome and authors semantic scope, family coverage and external-source provenance.

## Code Commentary

### Logic

Producer entries identify one obligation and all its targets together. Target locators are required; evidence locators may be absent. Statements and producer dispositions are preserved rather than paraphrased. Applicability, conditions and exclusions are authored before invariant ingest.

The family plane distinguishes declared guarantees, exact memberships, deliberate no-family and unexamined entries. A successor declaration may include `retain_memberships`, with each item exactly `member_id` and a nonblank `basis`. Read the exact family view first: a family_member row’s subject.record_id is the stored membership ID, and its statement names the invariant revision.

The references must resolve in the selected dataset within an explicitly declared same-family predecessor. Omitted/empty retention keeps none. No current-head lookup or implicit roster inheritance is permitted. Repeated IDs, duplicate new endpoints and retain/retire conflicts refuse. A changed nonempty retention set or basis under an allocated declaration key is a content conflict.

The public writer adds successor edges while leaving old records unchanged. Check `retainedFromMemberId`, measured unchanged-sibling counts and the published exact roster. This syntax extends a declaration carried by a genuine obligation; it is not a standalone family-only operation. External evidence retains document identity and provenance instead of fabricated Git anchors.

Since leaf `260921-ICR-L45` (developer ruling "require rationale"; Architect rulings on reviews R1–R3)
each `target` element is `{path, locator, governing_route, rationale, role}`: `rationale` is the required
authored explanation of why that place carries the obligation, `role` is optional (omit to inherit the
entry's `realization_role`; only when neither level states one is the claim `unclassified`), and an entry
may state `realization_rationale` / `realization_role` as an explicit default. The writer never generates a
rationale. It refuses, per entry and before minting, a target with no rationale
(`realization_rationale_absent`), non-string values (`realization_value_not_text`), unknown role words
including `"absent"` (`realization_role_unknown`), rationales over 20000 characters
(`realization_rationale_too_long`), and the placeholder route word `absent` in any case
(`realization_governing_route_absent_literal`) — a missing route is spelled by omitting the key. An exact
retry of an already committed entry is not checked again. The authority paragraph states that this element
shape supersedes rule 1's `{path, locator, governing_route}` in the external schema note
*260915-KS-curator-handoff-list-schema.md* revision 1 (not edited; it lives outside this repository), while
the rest of rule 1 stands; the verbatim worked examples predate per-target rationale and say so.

Since leaf `260928-MIK-L21` (MIK-R21) the template ends its producer-facing part with **"Where an entry
lands once knowledge is text (MIK-R21)"**: an informational map from today's hand-off fields to the text
knowledge format — records as `knowledge/<kind-dir>/<ID>-<slug>.json` that never list their own
locations, tests, families or decisions; writer-minted IDs (`INV-7K3F9Q`, 8-character derived IDs for
exported legacy records); each target becoming a `realizes` entry in `onboarding/<path>.json` with an
anchor that omits its own path; test evidence becoming a `proves` entry; `origin`; and the canonical
formatting applied by `agents-remember knowledge-format`. It says explicitly that **nothing changes what
a producer emits before MIK-R37**, and that `incidental` has no spelling in the file format (its mapping
is MIK-R12's to decide).

Since leaf `260928-MIK-L04` (MIK-R04) that section also holds the curator-guidance subsection **"Family
routes (MIK-R04)"**: the family record owns its `routes`; Coverage (every `realizes` entry of every member
lies under a route) and Non-empty (every route holds one), with `proves` entries not counting; routes
placed as deep as makes sense, one broad `mcp/` route passing the rules but being the wrong placement; the
root route spelled `.` only when a family has no narrower home; `unrealized_family` and `route_unassigned`
reported, never refused, and a retired family exempt; an added route must be a code directory while a
carried absent one is reported for MIK-R06; and `agents-remember knowledge-routes`, whose suggestion is
labelled `mechanical` and never writes a route. It changes nothing a producer emits.

Since leaf `260928-MIK-L12` (MIK-R12) the template decides that mapping — `incidental` is written as
`support` — and gains its own section, **"The file writer's sections (MIK-R12)"**, after the MIK-R21
section. It applies only on a **converted** memory tree (the layout marker); on unconverted memory, which
is every tree until the cutover (MIK-R37), the installed ingest is unchanged, and the producer's thirteen
fields do not change either. It documents the list-or-object document with `entries`, `records` and
`history`; the curator keys on entries (`scope`, `admission`, `status`, `invariant_id`, `supersedes`,
`proofs: [{test, facet}]`); that an entry naming no record is refused unless a `records` item names it;
that evidence is stored in `origin.handoff.evidence` of this leaf's own record, and for another leaf's
record in this leaf's `history` row about it (without the row the run is refused); rerun removal of this
leaf's unnamed entries; the `path::name` evidence states (`proof_written`, `needs_facet`,
`unresolvable`); record items of the ten kinds; history rows and their four cover forms; `handoff:<key>`
handles; what the writer fills in (IDs, anchors at C with `blob` and `content`, revisions against the
memory base, origin, row fields, canonical formatting, whole-file row agreement); and what it checks (the
validator over the resulting tree, all-or-nothing, the MIK-R04 route rules reported inside the writer
while every commit route still refuses them, planning without `--commit`, a non-blank
`--authorization-ref` recorded in the report).

Since leaf `260928-MIK-L28` (MIK-R28) the MIK-R12 section's evidence bullet names both forms in which
evidence names a test, a test ID `path::name` or a path plus symbol `path -k name`, and says that
`needs_facet` offers the statement only as a draft while the curator authors the facet: what this test
demonstrates, not the invariant's statement. A test file named without a test in it is `unresolvable`. A
new bullet, **"Proofs are shown and counted (MIK-R28)"**, tells the curator that `knowledge_read`'s
`invariant` and `family` views of a converted tree return the proofs, that the checklist lists the
invariants without any proof as information and not as a gate, and that a curator pass turns a migrated
record's "Evidence: …" text (`origin.handoff`) into proofs through `proofs`, with an authored facet. The
same text reaches the package copy and the eight harness starter copies through `sync-skills.py`.

Since leaf `260928-MIK-L30` (MIK-R30) the MIK-R12 section's history-row bullets gain one for the
**onboarding row**, on converted memory only: subject `onboarding:<source path>` or
`onboarding:<route>/overview` (`onboarding:overview` for the root route), disposition `no_impact`, and
nothing else. It records that a changed source file's card, or its governing route overview, was reviewed
and needs no change; a counted change of the card or overview (its Markdown, or a sidecar field other than
an anchor's `blob`, line numbers and `content`) needs no row. This is the curator's side of the
onboarding gate on history files, where only a counted change or such a row satisfies a trace (architect
ruling 2026-09-29T18:49:50 (1)). The bullet reaches the package copy and the eight harness starter copies
through `sync-skills.py`.

Since leaf `260928-MIK-L11` (MIK-R11) the same list gains a bullet for the **planned row**, on converted
memory only. It answers a `planned_untouched` worklist item: an effect the leaf's task document declared in
`expectedKnowledgeEffects` that no row delivered. Its subject is the item's,
`planned:<declared subject>#<effect>`; its disposition is `realized_elsewhere`, `deferred` or `dropped`; and
it adds `ref` and nothing else: `{row}` or `{invariant}` (which must exist) for `realized_elsewhere`,
`{requirement: {task, packet, id, version}}` or `{leaf}` for `deferred`, and `{decision: "<at>"}` for
`dropped`, the `at` of exactly one decision entry in the leaf's task document, which the writer resolves
through the task owner and refuses when it does not resolve. The bullet also states that a `no_impact` row
about the declared invariant does not answer the item, while a `changed` row with the declared effect (or,
for `retire`, a retiring `deleted` row) delivers it and raises no item. It reaches the package copy and the
eight harness starter copies through `sync-skills.py`.

Since leaf `260928-MIK-L10` (MIK-R10) the same list gains a bullet for the **no_invariant row**, on converted
memory only. It answers an `unexplained_hunk` or `unexplained_file` worklist item in a **covered** file: a
change no entry covers that carries no invariant. Its subject is the item's `facts.row` (`hunk:<item id>`, or the
item's own `file:<path>@<blob>`); its disposition is `no_invariant`; its `reason` says why, and it adds nothing
else. The bullet also names the other answers, which need no such row: attach a `target` to a stored,
non-retired invariant (`invariant_id`) or author a new invariant over the change. A delete-only hunk admits
only `no_invariant` (ruling 2026-09-30T01:56:39 Q1: an attach or author cannot answer it, so the item stays
open), and an item in an **uncovered** file is answered by the file's onboarding trace, not by this row (ruling
03:24:28 N2). It reaches the package copy and the eight harness starter copies through `sync-skills.py`.

Since leaf `260928-MIK-L27` (MIK-R27) the template has a section, **"The admission rule (MIK-R27)"**,
after the file writer's sections. Every **new** invariant, family and decision record states the
admission criterion it meets with a one-sentence justification, `"admission": {"criteria": [...],
"justification": "..."}`; the knowledge validator enforces it on converted memory, inside the writer and
at every commit route, and a code change alone is never an admissible reason. A table gives each kind's
criteria and meaning, marking the two the validator checks (`spans_locations`: realizations in two or
more files; `guarded_by_test`: a `proves` entry). Bullets state what **new** means (absent from the
memory base and not an export: an export's `origin.legacyId` derives its ID, and a hand-written
`legacyId` does not make a record exported, ruling 2026-09-29T23:04:57 F2); what is **refused** (no
criterion, `legacy-unassessed`, a justification made only of task, leaf, requirement, step or section
references, developer ruling IDs, commit hashes, dates and provenance words, rulings 22:11:24 Q2 and
23:04:57 F1, or an unsupported checkable claim); that every other record is only **reported** and the
`legacy-unassessed` records counted; that **local stays local** (prose under "Boundaries"); and that
**demotion** retires the record with a `deleted` row, effect `retire`, and never deletes its file. It
gives two admitted, two refused and one local example, as packet rule 5 requires; the "New" bullet was
rewrapped to 100 columns (F5), while the table rows cannot wrap. The section reaches the package copy
and the eight harness starter copies through `sync-skills.py`. It binds converted memory only, so
today's hand-off lists are unchanged.
Since leaf `260928-MIK-L13` (MIK-R13) the template has a section, **"Decision records (MIK-R13)"**, after the
admission section. A decision record keeps a choice that **keeps governing code** with the alternatives weighed, as
a `records` item of `kind: decision`: `context`; at least two `alternatives` in a fixed order, **exactly one**
`chosen`, and a `reconsider_when` on every `rejected` or `deferred` one (prose nothing evaluates); `consequences`,
`decider`, `supersedes` and `admission`; `status` starting `active`, with `superseded` **never stored** (derived from
a later decision's `supersedes`). Its `links` name what it governs (`explains`, `constrains`,
`motivated_change_to`; a decision with none is reported) and `reconsider_on` targets, each with the index of a
rejected or deferred alternative. A requirement target `{task: {repository, path}, packet, id, version}` is
resolved by the requirement owner and reported in `requirementEndpoints` as `resolved` or `unresolved`, never
refused. The ruling travels in the attached entry's `evidence` (`origin.handoff`; ruling 2026-09-30T01:45:56 Q1).
The section lists the validator's refusals, says how to **lift decisions at closeout** (developer rulings and
requirement-packet choices between real designs that keep governing code, with only the alternatives actually
weighed; task-only decisions stay in the task; the curator records and links, never reverses) and gives D18 as the
example. It binds converted memory only, so today's hand-off lists are unchanged.

Since leaf `260928-MIK-L14` (MIK-R14) the same list gains a bullet for the **reconsideration row**, on converted
memory only, after the no_invariant bullet. It answers a `reconsideration_candidate` worklist item (a target a
decision's `reconsider_on` link names changed in the leaf): its subject is the item's,
`reconsider:<DEC-ID>#<alternative index>`, and it carries the common fields only. `still_rejected` says why the
rejection holds; the writer then refreshes the links whose trigger fired to what the curator judged (a requirement
re-pointed to the item's `latestApproved`, an anchor re-anchored at C with a line range mapped through the leaf's
diff), and the decision's revision goes up once in the leaf; a link that cannot be mapped refuses the row; a stale
link anchor (`anchor_stale`) is raised too. When a newer version is approved, or the anchored code changes again,
after the refresh, rerunning the same row is refused and the curator answers the new item by naming its ID in
`items` (rulings 2026-09-30T10:39:15 and 11:01:18 R5-4, which also set the second-person voice). `raise` sets the
decision `under_reconsideration` and appends a question to the leaf's task-document `openQuestions` through
`task_doc`, keeping every existing question; when the question cannot be written the `raise` is refused and the
item stays open. The bullet adds that a `route:` target is raised by a row that reroutes, retires or deletes it,
that a superseded decision is never raised, never to reverse a decision (`raise` it), and to keep linked
alternatives at their index. The decision-record section's refusal list gains "a linked alternative moved to
another index against the memory base" (`R14.1-linked-alternative-order`). The stale-item refusal is not in the
template; its message names its own fix (review note R6-3). It reaches the package copy and the eight harness
starter copies through `sync-skills.py`, and binds converted memory only, so today's hand-off lists are
unchanged.

### Conventions

Canonical skills own instructions. Generated copies are synchronized artifacts; curate the matching sidecar against its own source path. One output list preserves the producer’s nine fields and fills only curator-owned decisions.

### Invariants And Boundaries

- Ground every record in accepted scope and real source evidence; do not create records to inflate coverage.
- Exact retained revisions are reused without rewriting old meaning or provenance.
- New membership edges are not new invariant revisions or semantic acceptance.
- A refusal or unexamined plane stays explicit; no favorable default substitutes for it.

### Todos

No additional work is asserted by this card. Actual project publication and semantic acceptance remain separately evidenced outcomes.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

The operative contract is defined by the repository sources cited below.

### Repo-Internal References

These references name the current owners and the behavior they establish.

- **The MIK-R04 curator-guidance subsection: family routes, their rules, the root route `.` and the read-only `knowledge-routes` suggestion.** [1]
- **The MIK-R12 section: the file writer's document, the curator keys and record, history and handle forms, what the writer fills in and what it checks; and the `incidental` → `support` decision.** [2]
- **The informational MIK-R21 section: where an entry lands once knowledge is text, and that nothing changes before MIK-R37.** [3]
- Curator-owned semantic scope remains required. [4]
- The public retention input and exact readback requirements. [5]
- **Per-target realization rationale and role, the value/vocabulary/length/route rules, the committed-retry exemption, and the stated supersession of revision 1's target element shape.** [6]
- **The MIK-R28 additions: both evidence forms, the facet authored beside the statement draft, and the views, the informational "without proof" list and the migration pass.** [7]
- The MIK-R30 onboarding-row bullet: its subject forms, its one disposition and when no row is needed. [8]
- The MIK-R11 planned-row bullet: its subject, its three dispositions and the ref each takes, and what does and does not answer the item. [9]
- The MIK-R10 no_invariant-row bullet: its subject, its one disposition, the answers that need no row, delete-only hunks and uncovered files. [10]
- The MIK-R14 reconsideration-row bullet: its subject, `still_rejected` with the refresh and the new-item answer, `raise` with the task-document question, route targets, superseded decisions, never reversing, and linked alternatives kept at their index. [11]
- The decision section's refusal list names the reorder of a linked alternative (MIK-R14). [12]
- The MIK-R27 admission section: the criteria and their meanings, what is new, refused and reported, local stays local, demotion, and two admitted, two refused and one local example. [13]
- The MIK-R13 decision-record section: the fields, the links and alternative indexes, requirement endpoints, the refusals, lifting at closeout and the D18 example. [14]

### Cross-Repo References

No sibling repository defines this file's contract.

No meaningful cross-repository implementation dependency.
