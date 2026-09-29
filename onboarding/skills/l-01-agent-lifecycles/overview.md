# skills/l-01-agent-lifecycles

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `skills/l-01-agent-lifecycles` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-29T10:05:46+02:00 |
| lastVerifiedCommitHash | `a4eba7b7b5b5ffee7277f6c19086697925a22df2` |
| lastVerifiedCommitDate | 2026-09-29T21:14:42+02:00|

## The onboarding row in the curator hand-off template (260928-MIK-L30)

`templates/curator-handoff-list.md`'s writer section (MIK-R12) now serves MIK-R30. Its list of history-row
forms gains the **onboarding row**, for converted memory only: subject `onboarding:<source path>` or
`onboarding:<route>/overview` (`onboarding:overview` for the root route), disposition `no_impact`, and nothing
else. It records that a changed source file's card or its governing route overview was reviewed and needs no
change; a counted change (the Markdown, or a sidecar field other than an anchor's `blob`, line numbers and
`content`) needs no row. On a converted tree only such a change or such a row satisfies the onboarding gate
(architect ruling 2026-09-29T18:49:50 (1)). Nothing a producer emits changes, and no role, operation or other
template in this route changed.

| Finding | Anchor | Source |
| --- | --- | --- |
| The onboarding-row history form in the writer section. | "An onboarding row (MIK-R30, converted memory only)"; "needs no row." | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:558-563 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| Both evidence forms, and the facet authored beside the statement draft. | "as a path plus symbol"; "offers the statement as a draft" | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:524-529 |
| The views, the informational list and the migration pass. | "Proofs are shown and counted (MIK-R28)." | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:530-534 |

## The file writer's sections in the curator hand-off template (260928-MIK-L12)

`templates/curator-handoff-list.md` gained the section "The file writer's sections (MIK-R12)", after the MIK-R21
section and its "Family routes (MIK-R04)" subsection. It applies only on a converted memory tree; on unconverted
memory, which is every tree until MIK-R37, the installed ingest is unchanged. It documents the curator's side of
the file writer: the list-or-object document with `entries`, `records` and `history`; the curator keys on entries
(`scope`, `admission`, `status`, `invariant_id`, `supersedes`, `proofs`); record items of the ten kinds; history
rows and their cover forms; `handoff:<key>` handles; what the writer fills in; and what it checks. The
`incidental` line now says the writer writes it as `support`. Nothing a producer emits changes. No role,
operation or other template in this route changed.

| Finding | Anchor | Source |
| --- | --- | --- |
| The section and the `incidental` decision. | `## The file writer's sections (MIK-R12)`; "writes it as" | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:485-593; skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:451-451 |

## Family routes in the curator hand-off template (260928-MIK-L04)

`templates/curator-handoff-list.md` gained a **curator-guidance** subsection, "Family routes (MIK-R04)",
inside the informational text-format section: the family record owns its `routes`; Coverage and Non-empty
over `realizes` entries (proofs do not count); routes placed as deep as makes sense (one broad `mcp/` route
passes but is wrong); the root route spelled `.` only when there is no narrower home; `unrealized_family`
and `route_unassigned` reported, not refused; an added route must be a code directory while a carried absent
one is reported for MIK-R06; and `agents-remember knowledge-routes`, whose mechanical suggestion never writes
a route. Nothing a producer emits changes. No role, operation or other template in this route changed.

| Finding | Anchor | Source |
| --- | --- | --- |
| The subsection and the command it names. | `### Family routes (MIK-R04)`; "agents-remember knowledge-routes" | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:460-484; skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:478-478 |

## Where a hand-off entry lands once knowledge is text (260928-MIK-L21)

`templates/curator-handoff-list.md` gained an **informational** section, "Where an entry lands once
knowledge is text (MIK-R21)", mapping today's hand-off fields onto the text knowledge format: records as
`knowledge/<kind-dir>/<ID>-<slug>.json` that never list their own locations, tests, families or
decisions; writer-minted IDs; each target becoming a `realizes` entry in `onboarding/<path>.json`; test
evidence becoming a `proves` entry; `origin`; and the canonical formatting of `agents-remember
knowledge-format`. It states that nothing a producer emits changes before MIK-R37, and that the template
role `incidental` has no file spelling (MIK-R12 decides its mapping). No role, operation or other template
in this route changed.

| Finding | Anchor | Source |
| --- | --- | --- |
| The section heading and its no-change statement. | `## Where an entry lands once knowledge is text (MIK-R21)`; "Nothing here changes what a producer emits today." | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:425-484 |
| `incidental` has no spelling in the file format. | "has no spelling in the file format" | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:450-450 |

## Explicit sibling selection in curation

A curator adding obligations to a family successor reads and names the exact old membership IDs with authored retention bases. Canonical role, operation and handoff carriers require this selection and published roster readback; no unchanged invariant is revised merely to populate the successor. The existing writer and role boundaries remain.

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical handoff explains exact stored-sibling selection and readback. | `### Retain exact siblings when adding new obligations to a family successor` | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:356-424 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical per-target rationale section. | "Realization rationale and role: one authored explanation per target" | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:101-140 |
| The stated supersession of the external schema note's rule-1 element shape. | "this file's element shape supersedes rule 1's" | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:8-18 |
| The curation operation's step 3 duty. | "Every target in it carries its own" | skills/l-01-agent-lifecycles/operations/curation.md:71-75 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The foundation entry as a second, bounded shape of the curator's work, with its own carrier and the seat's admission stated **either way** rather than a refusal assumed. | "This seat is admitted for it either way:"; "never required to start." | skills/l-01-agent-lifecycles/roles/curator.md:40-53 |
| The curator process distinguishes leaf ingest from taskless bootstrap and preserves enclosure-scope refusal. | `## Process` | skills/l-01-agent-lifecycles/roles/curator.md:59-159 |
| The report facts the foundation entry owes instead of a leaf's, inside the seat's own output section. | `## Outputs`; "the same report carries the foundation's own facts instead of a leaf's:" | skills/l-01-agent-lifecycles/roles/curator.md:160-185 |
| Permitted actions name both admitted writer entry points and refuse taskless bootstrap within an enclosure. | `## What you may do` | skills/l-01-agent-lifecycles/roles/curator.md:186-203 |
| The operation's ownership paragraph: the manager's half is a leaf-entry fact, and the foundation is reached as the procedure states. | "named role scope is required" | skills/l-01-agent-lifecycles/operations/curation.md:23-29; skills/l-01-agent-lifecycles/operations/curation.md:26-26 |
| The comparison table that separates the two entries by carrier, scope, required inputs, writer, onboarding and missing inputs. | `## The repository-foundation entry — the curator's work, before a leaf exists`; `enclosure_in_scope` | skills/l-01-agent-lifecycles/operations/curation.md:190-219 |
| The authority gate that names both writers and keeps the knowledge batch and its publication with their existing owners. | `## Authority gates` | skills/l-01-agent-lifecycles/operations/curation.md:220-255 |
| The handoff paragraph: on the foundation entry the same facts come from the bootstrap report, with the areas a partial run did not reach named as not reached. | `## Handoff / exit` | skills/l-01-agent-lifecycles/operations/curation.md:273-286 |
| The bootstrap role's step 5: reach the foundation, report the state it read, hand the authoring on, and never report a repository whose knowledge is not recorded as ready. | "Reach the knowledge foundation and report its outcome" | skills/l-01-agent-lifecycles/roles/bootstrap.md:49-58 |
| The bootstrap role's prohibition: the seat reads and reports the foundation's state and never authors records. | "Never author knowledge records either." | skills/l-01-agent-lifecycles/roles/bootstrap.md:136-139 |
| The bootstrap operation's step 6, with the seat gate quoted and the knowledge step made independent of the operation's other steps. | "Reach the repository's knowledge foundation." | skills/l-01-agent-lifecycles/operations/bootstrap.md:73-84 |
| The four knowledge rows the operation's failure table gains, keeping `unusable` and a refused admission distinct from `not-recorded`. | `not-recorded`; `snapshot_unavailable`; `context-not-admitted` | skills/l-01-agent-lifecycles/operations/bootstrap.md:111-114 |
| The bootstrap operation's own prohibition on authoring the foundation, and the completion line that carries the foundation's state. | "It does not author the knowledge foundation." | skills/l-01-agent-lifecycles/operations/bootstrap.md:148-150 |
| The procedure these carriers delegate to, and its own statement that a taskless curator seat **now exists** and authors the foundation when no task does — the statement L27 landed in the opposite form and `260921-ICR-L32` reversed. | `## Who Runs It`; `task-binding-required` | skills/c-14-knowledge-bootstrap/SKILL.md:38-83 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| **The authoring step the curator role file now carries: the real invocation, what to read from the report, and the identity the handoff owes.** | "Author and publish the durable knowledge through the real writer."; "Read the report, never the exit status" | skills/l-01-agent-lifecycles/roles/curator.md:70-70; skills/l-01-agent-lifecycles/roles/curator.md:81-81 |
| **The same obligation in the curation operation, with the invocation spelled out and the report's consumed fields named.** | "Route the durable knowledge through the real writer, and publish it."; "Consume the report, not the exit status"; `publicationRoute`; `publishedIdentity` | skills/l-01-agent-lifecycles/operations/curation.md:60-71; skills/l-01-agent-lifecycles/operations/curation.md:79-80; skills/l-01-agent-lifecycles/operations/curation.md:175-175; skills/l-01-agent-lifecycles/operations/curation.md:82-82; skills/l-01-agent-lifecycles/operations/curation.md:80-81 |
| The authority gate that keeps the batch and its publication with their existing owners, and the rule that a partial hand-off stays partial. | "The knowledge batch and its publication keep their existing owners."; "A partial or refused knowledge hand-off stays partial." | skills/l-01-agent-lifecycles/operations/curation.md:225-225; skills/l-01-agent-lifecycles/operations/curation.md:263-263 |
| The prohibition that makes the mounted tool's refusal the carrier's own rule, and the permitted-action line naming the subcommand. | "Never write the knowledge dataset yourself."; "ordinary knowledge authoring route" | skills/l-01-agent-lifecycles/roles/curator.md:191-191; skills/l-01-agent-lifecycles/roles/curator.md:208-208 |
| The handoff paragraph both carriers gained, which is what makes the published identity travel with the report. | "knowledge hand-off result"; "published dataset identity" | skills/l-01-agent-lifecycles/operations/curation.md:259-259; skills/l-01-agent-lifecycles/operations/curation.md:260-260; skills/l-01-agent-lifecycles/roles/curator.md:168-168; skills/l-01-agent-lifecycles/roles/curator.md:169-169 |
| The read route whose declaration the write side now publishes to, restated as current truth in the retrieval carrier. | "Where the route reads, and what publishes there."; `--publish` | skills/c-04-retrieval-strategy-router/SKILL.md:181-190 |
| The write plane the carrier invokes, and the publication owner whose result it reads back. | `ingest_curator_list`; `declared_publication_location`; `published_identity_read_back` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1116-1243; mcp/src/agents_remember/application/knowledge_publication_route.py:115-132; mcp/src/agents_remember/application/knowledge_publication_route.py:202-250 |

## Purpose

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
current sprint truth and calling `dispatch_agent` exactly once on the sprint document. An explicit
developer-declared task-seat takeover instead targets the named role on its canonical task document. Missing plane identity
selects ambient target-document and architect-altitude validation. After handoff, the architect and
other spawning seats use the same public verb under plane identity and direct-child scope; a plane
refusal never becomes an ambient retry. Source-lineage conflicts remain resumable through the
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
delegated leaf gates and integrate a master, and orchestrators govern master handovers. Mechanical
fact relay replaces role-local polling and inference.

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

The quality altitude ladder uses the pinned Dagger graph for Agents Remember acceptance. Leaf
closeout selects targeted mode exactly once; leaf integration and series closeout do not rerun it.
Master integration selects full mode exactly once. Both require the task-derived explicit diff
base. Host pytest/wrapper runs are refused; a hard cap remains an explicit constrained-lifecycle
setting rather than role-local judgment.

A curator completes only after the current-additions missing-onboarding check and full leaf-scoped
memory-quality worklist have been repaired and rerun. Dirty-source drift and future commit-derived
verification can be classified as closeout-owned only after no repairable citation, claim, shape,
history, entity, or index finding remains. The curator then publishes the sole structured,
candidate-bound coherence authority through the lifecycle API; generated Markdown is only its
human-readable projection.

Before that curator is created, the manager requires the leaf's task-derived source-lineage
projection to be current and includes it in the complete brief. The structural dispatch transaction
re-proves lineage before host creation, so a parent move between status and dispatch fails closed.

## Conventions

- Canonical role doctrine lives under `roles/`; templates feed complete role inputs.
- Shared rules live in `SKILL.md` and are not restated as competing role-local variants.
- Runtime package and harness copies are synchronized artifacts of the complete canonical tree.
- Current intent stays in default bodies; semantic history records transitions without leaf diaries.
- `dispatch_agent` is the sole public spawn verb; caller kind is derived from process context, never
  selected in the request.
- Role-table `dispatch` and `tools` rows are fixed authority/capability documentation rather than
  settings knobs.

## Invariants And Boundaries

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


## CCR-R12@v5 Lifecycle Boundary

Workers provide targeted checks and curators provide scoped onboarding checks with honest failed or not-run states. The prepared code and memory-content outputs move through the authorized Git transaction, whose commit legs suppress automatic quality and test hooks. The consumer ledger is refreshed without a commit while ordinary explicit Git hook policy outside the transaction remains unchanged; full quality, full tests, full memory quality, certification, and review require an explicit developer request. Requested reviews retain the sealed monotonic three-round rule.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Shared routing, authority, loop, and dispatch doctrine is canonical here. | "## Which Lifecycle Am I? (the router — exactly three conditions, in order)"; "## Delegated series authority"; "comes only from process context"; "Every launcher or role that dispatches a hosted role calls"; `## Which Lifecycle Am I? (the router — exactly three conditions, in order)`; `## Delegated series authority`; `# Core — The Three-Party Loop (one home — this file owns the loop doctrine)` | skills/l-01-agent-lifecycles/SKILL.md:13-13; skills/l-01-agent-lifecycles/SKILL.md:24-66; skills/l-01-agent-lifecycles/core/authority.md:50-68; skills/l-01-agent-lifecycles/core/authority.md:149-166; skills/l-01-agent-lifecycles/core/loop.md:1-115 |
| The graph-less atomic-sequential default describes sprint shape; nothing serializes a graph-less sprint. | "nothing serializes a graph-less"; "nothing serializes its masters"; "serializes the masters" | skills/l-01-agent-lifecycles/criteria/plan-review.md:65-68; skills/l-01-agent-lifecycles/templates/orchestration-task.md:172-174; docs/reference/execution-topology-migration.md:61-63 |
| The architect launcher packet is one canonical compiler contract, not fixture prose or a second brief. | "# Template — Architect Brief"; "This architect seat is now plane-hosted."; "Compiler notes for the launcher" | skills/l-01-agent-lifecycles/templates/architect-brief.md:1-84 |
| Curator owns conservative three-way memory reconciliation, the complete pre-closeout onboarding worklist, and structured authority publication. | "You run one leaf's coherence pass and you write onboarding."; `## Process`; "Reconcile three ways before writing anything"; `curator_coherence` | skills/l-01-agent-lifecycles/roles/curator.md:7-49; skills/l-01-agent-lifecycles/roles/curator.md:31-52; skills/l-01-agent-lifecycles/roles/curator.md:77-140; skills/l-01-agent-lifecycles/roles/curator.md:60-60; skills/l-01-agent-lifecycles/roles/curator.md:58-58; skills/l-01-agent-lifecycles/roles/curator.md:61-61; skills/l-01-agent-lifecycles/roles/curator.md:59-159 |
| Manager owns one real master and its leaf closeout chain. | `# Manager`; "You drive exactly one master's leaf sequence from dispatch to handover." | skills/l-01-agent-lifecycles/roles/manager.md:6-211; skills/l-01-agent-lifecycles/roles/manager.md:10-30 |
| Worker owns one real leaf's implementation and durable report. | `# Worker`; "You build one leaf."; "The turn report" | skills/l-01-agent-lifecycles/roles/worker.md:6-146; skills/l-01-agent-lifecycles/roles/worker.md:7-17; skills/l-01-agent-lifecycles/roles/worker.md:72-78 |
| The shared frame defines the mandatory per-ID worker envelope and independent reviewer disposition. | `## Acceptance is per stable ID and version, never aggregate` | skills/l-01-agent-lifecycles/core/acceptance.md:44-78 |
| Core acceptance doctrine defines the mandatory per-ID worker envelope and the independent reviewer's adjudication. | `## Acceptance is per stable ID and version, never aggregate`; "The independent reviewer inspects the owned primary packet revision" | skills/l-01-agent-lifecycles/core/acceptance.md:44-78 |

Current working-candidate evidence for this route:

| Finding | Anchor | Source |
| --- | --- | --- |
| Lifecycle publication and recovery carry the actual code/memory outputs. | `LifecycleOperationRecoveryCommits` | mcp/src/agents_remember/models/lifecycles/operation.py:66-72 |

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

## Update History
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): **route body updated for MIK-R30.** New section at the top, "The onboarding row in the curator hand-off template (260928-MIK-L30)", with architect ruling 2026-09-29T18:49:50 (1). One row. The six inserted template lines moved later template lines only; the L12, L04 and L21 sections cite lines above the insertion or were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): **Route body update (MIK-R28).** New top section "Test proofs in the curator hand-off template": both evidence forms (the ruled `path -k name`), the facet authored beside the statement draft, and the new "Proofs are shown and counted (MIK-R28)" bullet. Two rows. The installed `memory-citations --fix` widened the MIK-R12 and MIK-R04 rows' heading citations to their sections, with no wording change.
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): **route body updated — new section "The file writer's sections in the curator hand-off template (260928-MIK-L12)".** The L04 section's row moved by the one-line `incidental` insertion and was re-pointed. No verification stamp was advanced.
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): **route body updated — new section "Family routes in the curator hand-off template (260928-MIK-L04)"** for the template's new MIK-R04 subsection. No stamp advanced.
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): **route body updated — new section for the curator hand-off template's informational MIK-R21 section.** No stamp advanced.
- 2026-09-28T17:19:01+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): body update — added the per-target realization rationale section (template shape, supersession of the external schema note revision 1's rule-1 element shape, role/operation/c-14 duties). Other ranges re-pointed through the exact base-to-candidate line map. No stamp advanced.

- 2026-09-27T05:43:38+00:00 — Curator-authored re-citation of 1 investigated L41 source-linked claim(s). Each named registration or declaration was selected individually after the composite guarded projection declined. Prior explanation, refusal evidence, generated history and real verification stamps are preserved.
- 2026-09-27T05:29:53+00:00: Generated citation repair: `## The repository-foundation entry — the curator's work, before a leaf exists`; `enclosure_in_scope` repointed to skills/l-01-agent-lifecycles/operations/curation.md:187-216; skills/l-01-agent-lifecycles/operations/curation.md:206-206. No content impact: mechanical anchor-range projection bound to citation source snapshot a9e4bf20669ecb356be8a208a2ac77489c28fc161e108a6d1b20c61579617d84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T05:29:53+00:00: Generated citation repair: `## Handoff / exit` repointed to skills/l-01-agent-lifecycles/operations/curation.md:270-283. No content impact: mechanical anchor-range projection bound to citation source snapshot a9e4bf20669ecb356be8a208a2ac77489c28fc161e108a6d1b20c61579617d84; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-27T00:34:45Z — L39: No content impact: resolved the affected registry/instruction/overview reference rows against their exact current named anchors after the scoped source changes. Existing factual meaning, verification stamps and earlier history are preserved.


- 2026-09-26T23:48:33Z — L39: Reconciled the explicit retained-sibling input across existing curator carriers; no role, admission or transaction authority changed.

- 2026-09-26T21:20:53+00:00: Generated citation repair: `## Outputs`; "the same report carries the foundation's own facts instead of a leaf's:" repointed to skills/l-01-agent-lifecycles/roles/curator.md:153-178; skills/l-01-agent-lifecycles/roles/curator.md:169-169. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:20:53+00:00: Generated citation repair: `## The repository-foundation entry — the curator's work, before a leaf exists`; `enclosure_in_scope` repointed to skills/l-01-agent-lifecycles/operations/curation.md:165-194; skills/l-01-agent-lifecycles/operations/curation.md:184-184. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:20:53+00:00: Generated citation repair: `## Authority gates` repointed to skills/l-01-agent-lifecycles/operations/curation.md:195-230. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:20:53+00:00: Generated citation repair: `## Handoff / exit` repointed to skills/l-01-agent-lifecycles/operations/curation.md:248-261. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T19:49:05Z — Reconciled the current reviewer and curator responsibilities without changing role or transaction authority.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "Author and publish the durable knowledge through the real writer."; "Read the report, never the exit status" repointed to skills/l-01-agent-lifecycles/roles/curator.md:70-70; skills/l-01-agent-lifecycles/roles/curator.md:76-76. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **route body updated — the seat policy moves and these carriers follow it.** The new section records that the four carriers this route owns were corrected first and propagated into all ten copies, names the route-level statements that changed (the comparison table's carrier row, the bootstrap pair's read-and-report wording, the curator role's entry paragraph), and states that the L20 section's "the subcommand" became "the subcommands" because the mounted tool now names both write-plane entry points. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T12:25:00+02:00 — 260921-ICR-L27 curator (uncommitted change set on `ar/260921-icr-l27-ar`, code base `06ed70cfcde7e3860ee5b53435727e7512e4335c`): **route body updated for the repository-foundation entry and the seat gate it depends on.** `roles/curator.md` gained the entry paragraph and process block, `operations/curation.md` gained the comparison-table section and the authority-gate sentence, and `roles/bootstrap.md` / `operations/bootstrap.md` gained the first-hour read-and-hand-on step with the four knowledge rows in the failure table. The section states the rule a reader is most likely to invert — a session opened for the curator with no task document is refused `400 task-binding-required`, so **a taskless curator seat does not exist** and the pre-task step is carried by the taskless bootstrap seat plus the taskless writer with no enclosure in scope — because a round-one adversarial verdict was `blocking` on exactly that sentence in the procedure and its three sibling carriers. **Citation accounting:** the rows this section adds were derived from the carriers' own post-edit lines, not by adding a delta to an old number; the rows this document already carried into `roles/curator.md`, `operations/curation.md` and `skills/c-14-knowledge-bootstrap/SKILL.md` were re-read in the same pass and their drifted ranges re-anchored to the lines that now carry each construct. No claim and no row was dropped, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base
  `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **route body updated for the curator method's family and
  external-source steps.** `roles/curator.md` gained the numbered author-and-read-back step,
  `operations/curation.md` gained the same for the reconciliation pass, and
  `templates/curator-handoff-list.md` gained the section stating the shape of `family` and
  `external_sources` beside the thirteen producer/curator fields. The section records the three rules a
  seat is most likely to get wrong: an unexamined obligation is never reported as family-free, nothing
  is grouped by directory/route/label/shared anchor, and an external document never becomes a repository
  path with a Git blob. **Citation accounting:** the rows this route carries into the three carriers were
  re-derived against this candidate's bytes rather than shifted by a remembered delta, and the
  `citation_claim_reopened` rows the product reported for these files were re-read and disposed of by
  hand. No claim and no row was dropped, and no verification stamp was advanced: the candidate is
  uncommitted and the governed closeout owns the real stamp.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **route body updated for the curator's new authoring step, which is an obligation this route's carriers now state rather than an instruction detail.** `roles/curator.md` (144 lines) and `operations/curation.md` (161 lines) gained the real invocation (`knowledge-ingest … --baseline … --publish --commit --json`), what to consume from its report (`committed`/`rulings`/`refused`, `publicationRoute`, `publishedIdentity`), the authority gate that keeps the batch and publication with their existing owners, the rule that a partial hand-off stays partial, the prohibition on writing the dataset from the seat, and the handoff obligation to carry the published identity. The section states the route-level rule those carriers now depend on — `--commit` is the knowledge-batch write word and `--publish` is an explicit selection, never implied — and that `skills/` is canonical with the harness and package-data copies generated from it. **Citation accounting:** the section's ranges were read from the carriers' own post-edit lines, and the rows this document already carried into `roles/curator.md` were re-derived in the same pass (`:56-56` → `:74-74`) because that file grew 5 → 31 net lines at the top of the workflow. No claim and no row was dropped, and no verification stamp was advanced — the governed closeout owns it.
- 2026-09-20T01:00+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared the 1 enforced citation row this card carried (citation_anchor_absent_from_range) — the dead single-line range skills/l-01-agent-lifecycles/roles/curator.md:31-31 in the curator row was repointed to skills/l-01-agent-lifecycles/roles/curator.md:74-137, which carries `curator_coherence`, while `## Process` and `Reconcile three ways before writing anything` remain held by the same row's other ranges; every claim wording, anchor and every other range is unchanged, and no verification stamp was advanced.
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `overview.md:180` (curator_coherence) — re-read the claim against the current source: the construct moved, and the range was re-derived from its real extent in the file the claim already cites.
- 2026-09-18T13:27+02:00 — 260915-KS-L13 curator (range-closure pass): **the last five dead-anchor rows in this document were re-cited to the lines that now carry their facts, not re-pointed at adjacent sites.** `## Delegated Series Authority` was the *casing* of the live `## Delegated series authority` (now at `core/authority.md:149`, and the row already carried the live backticked form), so the quoted duplicate was corrected to the source's own heading text; `Caller kind comes only from process context` was the *casing and location* of `comes only from process context` at `core/authority.md:68`, so the quoted anchor was corrected and the `core/authority.md:50-52` extent widened to `50-68` (the whole `## Dispatch is one structural transaction` section, which still holds `Every launcher or role that dispatches a hosted role calls` at `:52`). `nothing serializes its masters` was carried by the row's sibling anchor in `criteria/plan-review.md` in the *wording the catalog actually uses* (`nothing serializes the masters`, `:65-66`), while the sentence the row quotes verbatim lives in `docs/reference/execution-topology-migration.md:63` — that per-site source was added rather than the anchor re-worded, because the migration note is a real live carrier and the claim's words are true there. The three `## What This Seat Is` anchors were the *rewritten* role files' old section heading: the live equivalent is each file's own `# Curator` / `# Manager` / `# Worker` title plus its opening duty sentence (`You run one leaf's coherence pass and you write onboarding.`, `You drive exactly one master's leaf sequence from dispatch to handover.`, `You build one leaf.`), so the dead heading was replaced by those quotes. No claim was deleted or softened and no anchor set was dropped. No verification stamp advanced: the source is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T13:20+02:00 — 260915-KS-L13 curator (post-merge pass): **stale citations repaired in this document after the master's sync onto its moved super line.** The card rows whose anchors no longer exist anywhere in the indexed corpus were re-worded to the text the split files now carry — the `# Core — The Minimal Lifecycle Frame`, `# Core — Shared Invariants (every role can count on these)`, `## Acceptance is per stable ID and version, never aggregate` and `## Requirement revisions and delivery attempts are separate axes` headings, and `two disjoint caller kinds` — and their cited ranges were widened or given the carrying per-site source. Rows whose anchors name text that exists nowhere in the tree are named in `notes/reports/260915-KS-L13-named-residue.md` rather than re-pointed at an adjacent site.

2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T14:15+02:00 — 260915-CAPS-L19 curator: **Field-name warrant corrected — `ready-for-closeout` read as *never* a value of the combined `checklistStatus`.** That absolute sentence was written by 260915-CAPS-L10's curator as the warrant for this card's `D35` correction, and `CAPS-R19` (`260915-CAPS-L19`) measures it **literally false** (`application/memory_quality/controller.py:685-687` leaves the combined field at its incoming `ready-for-closeout` value on the success path, with `closeoutReady=true`). The card now states the three-path model instead: the raw `qualityChecklistStatus` is the repair loop's gate; the combined `checklistStatus` is rewritten to `coherence-required` **only when the coherence record is then missing or stale**; and `closeoutReady` becomes true only once that validation passes. Corrected under `CAPS-R19`'s revision note (2026-09-17T13:55), which is the authority for this change. The field-name correction itself stands and attribution is complementary — `260915-CAPS-L10` corrected the onboarding cards, `CAPS-R19` corrected the shipped sources (the five loop-gate carriers, their nine generated copies, the guard registry's docstring) and brought `docs/reference/mcp-tools.md` into the loop-gate census and the guard's `LOOP_GATE_DOCUMENTS`. The earlier entries below are left exactly as written: they record what L10 did, and this entry is the correction of their warrant. No verification stamp advanced — the candidate is uncommitted and the governed closeout owns the real commits.
- 2026-09-17T13:45+02:00 — 260915-CAPS-L10 curator: **the corpus restructure is labelled as structure, not as a measured saving.** Added the measured qualification to Purpose: the `620 → 179` router change moved doctrine into the new sibling layers rather than removing it, the one measurement that exists points the other way at the worker elevation (delivered capsule **11,828** vs a **5,928** legacy chain, **+5,900**; like-for-like 11,645, +5,717), manager and architect are **UNMEASURED** (`binding-unresolved`), preservation is intact at **36/36** across ten declared roles plus launcher routing, and **adoption acceptance FAILED** with disposition **REVISE**. Also **corrected a landed defect (`D35`)** in the CAPS-L18 section: `ready-for-closeout` is never a value of the combined `checklistStatus`; the repair loop's gate is the **raw** `qualityChecklistStatus`, the combined field then reports `coherence-required`, and `closeoutReady` follows validation (`application/memory_quality/controller.py:664,671,678,687`). No verification stamp or fingerprint advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: the complete-curation doctrine reaches this route. The canonical sources on this route now state that the full `memory_quality_check` operation is part of every leaf's curation, that a subset never stands in for it, and that closeout and integration carry the completed result as a prerequisite while invoking nothing. Body updated as above; no verification stamp advanced because the sources are uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "nothing serializes a graph-less"; "nothing serializes its masters" repointed to skills/l-01-agent-lifecycles/templates/orchestration-task.md:172-172; skills/l-01-agent-lifecycles/roles/orchestrator.md:266-266. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "Requirement acceptance is per stable ID and version, never aggregate." repointed to skills/l-01-agent-lifecycles/SKILL.md:321-321. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `## Delegated Series Authority` in the row 152 of this card from skills/l-01-agent-lifecycles/SKILL.md:13-13 to skills/l-01-agent-lifecycles/SKILL.md:448, the extent of the construct the claim is about (the checker named line(s) [448] as its live location); re-pointed `Caller kind comes only from process context` in the row 152 of this card from skills/l-01-agent-lifecycles/SKILL.md:448 to skills/l-01-agent-lifecycles/SKILL.md:492, the extent of the construct the claim is about (the checker named line(s) [492] as its live location); re-pointed `Every launcher or role that dispatches a hosted role calls` in the row 152 of this card from skills/l-01-agent-lifecycles/SKILL.md:492 to skills/l-01-agent-lifecycles/SKILL.md:499, the extent of the construct the claim is about (the checker named line(s) [499] as its live location)

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: **route body updated** for the corpus consolidation. Purpose now names the route's actual 260915-CAPS-L1 shape (thin router + `core/` + nine role files + eight `operations/` blocks + `reference/` + `composition-manifest.json`), and the Ungoverned Mirror Status section records this pass's explicit decision: the overview is updated because route meaning changed, while the legacy `onboarding/skills/l-01-agent-lifecycles/**` sidecars are deliberately left untouched because they are outside `pathRules.include`, already declared knowingly stale, and a partial hand-refresh would duplicate the governed cards on the tracked generated `mcp/**` copy without resolving the govern-or-remove question this section already raises. No verification stamp or fingerprint was advanced.
- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Aligned role/template handoff doctrine with two outputs and non-authoritative cache status. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.

- 2026-09-13T15:01:46+02:00 — Gate-required ungoverned-mirror curation: rewrote the planning/runtime
  boundary to the shipped per-contract activation (each canonical series contract owns its own
  activation record; `reconciling` suspends nothing and excludes no other master; multiple
  nonterminal contracts remain valid) and added the explicit developer ruling that nothing serializes
  a graph-less sprint — `atomic-sequential` describes sprint SHAPE, not a serialization mechanism.
  Repaired the rotated citation row after `grep -n` verification: `"## Delegated Series Authority"`
  → SKILL.md:422-422, `"Caller kind comes only from process context"` → SKILL.md:466-466, `"Every
  launcher or role that dispatches a hosted role calls"` → SKILL.md:473-473 (all three had been bound
  to each other's line), and added the graph-less ruling row citing
  templates/orchestration-task.md:172-172 and roles/orchestrator.md:265-265. Added the Ungoverned
  Mirror Status defect statement. Verification metadata remains closeout-owned.
- 2026-09-10T09:58+02:00 — CCR-R12@v5 transaction-only curation against code commit `4bbe2c37b0fa70b07af4ddbc247aeee1f58343b0`: re-read the curator reference row against the rewritten `skills/l-01-agent-lifecycles/roles/curator.md` — section 4 is now `### 4 — Repair Affected Onboarding, Then Publish`, so the row carries the current heading and its 153-195 extent. Verification metadata remains closeout-owned.

- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "Requirement acceptance is per stable ID and version, never aggregate." repointed to skills/l-01-agent-lifecycles/SKILL.md:295-295. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: recorded task-altitude
  reviewer binding, generation-bound parent stamping, and the fail-closed unstamped sprint seam.
  Verification remains closeout-owned.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 adopted one public `dispatch_agent` verb, separated
  ordinary architect bootstrap from explicit takeover, clarified fixed role authority versus
  launch settings, and preserved resumable lineage-conflict recovery. Verification remains
  closeout-owned.

- 2026-08-29T09:14+02:00 — MCAR-L02 replaced the hand-authored coherence report with one
  lifecycle-published structured authority and a generated Markdown projection. Verification
  remains closeout-owned.

- 2026-08-28T14:18+02:00 — Reconciled lifecycle overview citations against the committed PDLS
  candidate; the architect/seat routing and acceptance boundaries are unchanged.

- 2026-08-27T22:15+02:00 — Clarified the route-wide attempt boundary: never-handed-off malformed
  rows are non-attempt corrections, while handed-off malformed records require reviewer rejection.
- 2026-08-27T21:53+02:00 — M40@v2/M44@v2 route correction: formal attempts now begin at review
  handoff, internal protocol events stay separate, and lightweight journal records link frozen
  expanded evidence without inflating the master summary.
- 2026-08-27T20:45+02:00 — Clarified that each leaf has one physical append-only attempt journal;
  worker and reviewer records share that authority while reports and verdicts link exact anchors.
- 2026-08-27T19:59+02:00 — M40-M45 route impact: recorded leaf-authoritative attempt journals,
  non-gating summaries, and the M42 distinction between stale in-flight candidates and unrelated
  post-acceptance movement.
- 2026-08-27T12:43+02:00 — M38: documented the exact stable-ID acceptance set, worker evidence
  envelope, independent reviewer adjudication, non-code citation form, and overall no-rejection
  rule. The durable-evidence promotion hold point remains separately mandatory. Verification
  metadata stays pinned until governed closeout stamps the PDLS commit.

- 2026-08-26T08:20+02:00 — Reconciled the planning/runtime source-pair boundary and synchronized
  doctrine set to the frozen candidate; verification remains closeout-owned.

- 2026-08-24T14:19+02:00 — No route impact: aligned the curator brief's quality examples with the canonical sync/start/poll request. Verification metadata remains pinned until architect-owned closeout.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair route impact: orchestration-task template heading restored to `## Canonical executionGraph Adoption Payload`; copies re-synced. Verified at code commit e5cb139f.


- 2026-08-20T21:30+02:00 — 260815-DAG-L15 route impact: review-doctrine repair — no-self-review + evidence-type matching (reviewer/orchestrator), PR-8, RV-1 extension, D-6 bounded requirement ids, verdict/manager-brief templates, SKILL.md three-party loop. Verified at code commit de3a0fd9.


- 2026-08-20T05:06+02:00 — 260815-DAG-L14 route impact: doctrine files updated to the
  `attach_master` flow and seats structure. Verified at code commit 8071a644.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13 route impact: the architect/orchestrator roles and the
  orchestration-task template now teach the atomic-sequential default — a graph-less sprint runs
  one master at a time, `task_doc.author_execution_graph` owns graph bootstrap and edits, and the
  `migrate_execution_topology` cutover reference is gone; lifecycle routing doctrine is unchanged.
  Verification remains closeout-owned.

- 2026-08-18T09:25+02:00 — No route impact: renamed the atomic 'barrier' concept to 'blocker' throughout; route purpose unchanged.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: documented architect-owned initial planning,
  evidence-cited judgment, ready-frontier recomputation, organizational versus atomic master
  topology, exact pre-landing organizational completion, and the no-workbench boundary.
  Verification remains closeout-owned.
- 2026-08-14T11:29+02:00 — R39 curator: removed Agents Remember-specific quality commands from
  generic lifecycle guidance while preserving exact cadence. Verification remains closeout-owned.
- 2026-08-14T06:25+02:00 — L23 final candidate review: lifecycle doctrine keeps Dagger as the sole
  acceptance graph and makes manager lineage plus exact candidate-bound route review mandatory
  before curator dispatch. Verification provenance remains closeout-owned.
- 2026-08-13T14:32+02:00 — L23 final route review: synchronized Dagger-only acceptance,
  targeted/full altitude, explicit diff-base ownership, and diagnostic-only host execution across
  canonical lifecycle doctrine. Verification remains closeout-owned.
- 2026-08-13T08:47+02:00 — L23 integration-gate repair: added the manager-owned pre-curator lineage gate, brief-carried projection, and pre-host dispatch recheck to canonical lifecycle doctrine. Verification metadata remains closeout-owned.

- 2026-08-12T20:20+02:00 — L23 curator: documented canonical pre-dispatch lineage policy; verification remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 route impact: manager,
  orchestrator, worker, and their dispatch briefs now state that master full
  gates use host-managed RAM/swap by default. Verification metadata remains
  pinned until closeout stamps L24.

- 2026-08-11T14:40+02:00 — Made the required missing-onboarding and full leaf-quality
  repair-and-rerun loop part of current curator completion doctrine; real-commit fields remain
  closeout-owned only after the curator-actionable worklist is empty.
- 2026-08-11T14:10+02:00 — Replaced accumulated route-impact sections with the compact current
  lifecycle topology, authority, dispatch, and synchronization contract.
- 2026-08-10T07:30+02:00 — Completion cleanup kept durable reports/transcripts while reclaiming
  completed subordinate seats.
- 2026-08-09T12:08+02:00 — Fact-relay supervision superseded ladder and watcher doctrine.
- 2026-08-08T02:00+02:00 — Quality work was assigned to leaf closeout and master integration
  altitudes.
- 2026-07-12T14:20+02:00 — Established governing route coverage.
