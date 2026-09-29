# mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T23:27:43+02:00 |
| lastVerifiedCommitHash | `46ca74302e76cf40fb6370ea9ece16d8fa719f00` |
| lastVerifiedCommitDate | 2026-09-30T00:07:49+02:00|
| governingOverview | `mcp/overview.md` |

## Governing Overview

[mcp route overview](../../../../../../../overview.md)

## Purpose

Packaged runtime copy of the canonical skills/l-01-agent-lifecycles/templates/curator-handoff-list.md. It is synchronized by the existing skill propagation owner and introduces no independent doctrine.

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
This package copy is generated from the canonical root template by `scripts/sync-skills.py`.

Since leaf `260928-MIK-L21` (MIK-R21) the template ends its producer-facing part with **"Where an entry
lands once knowledge is text (MIK-R21)"**: an informational map from today's hand-off fields to the text
knowledge format — records as `knowledge/<kind-dir>/<ID>-<slug>.json` that never list their own
locations, tests, families or decisions; writer-minted IDs (`INV-7K3F9Q`, 8-character derived IDs for
exported legacy records); each target becoming a `realizes` entry in `onboarding/<path>.json` with an
anchor that omits its own path; test evidence becoming a `proves` entry; `origin`; and the canonical
formatting applied by `agents-remember knowledge-format`. It says explicitly that **nothing changes what
a producer emits before MIK-R37**, and that `incidental` has no spelling in the file format (its mapping
is MIK-R12's to decide).
The section reached this generated copy through `scripts/sync-skills.py`, as did the eight harness starter copies.

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
The subsection reached this generated copy through `scripts/sync-skills.py`, as did the eight harness starter copies.

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

### Conventions

Canonical skills own instructions. Generated copies are synchronized artifacts; curate the matching sidecar against its own source path. One output list preserves the producer’s nine fields and fills only curator-owned decisions.

### Invariants And Boundaries

- Ground every record in accepted scope and real source evidence; do not create records to inflate coverage.
- Exact retained revisions are reused without rewriting old meaning or provenance.
- New membership edges are not new invariant revisions or semantic acceptance.
- A refusal or unexamined plane stays explicit; no favorable default substitutes for it.

### Todos

No additional work is asserted by this card. Actual project publication and semantic acceptance remain separately evidenced outcomes.

## Docs References

No configured Domain Documentation source applies to this repository-owned contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The operative contract is defined by the repository sources cited below. | — | — |

## Repo-Internal References

These references name the current owners and the behavior they establish.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The MIK-R04 curator-guidance subsection: family routes, their rules, the root route `.` and the read-only `knowledge-routes` suggestion.** | `### Family routes (MIK-R04)`; "never writes a route." | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:460-484; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:482-482 |
| **The MIK-R12 section: the file writer's document, the curator keys and record, history and handle forms, what the writer fills in and what it checks; and the `incidental` → `support` decision.** | `## The file writer's sections (MIK-R12)`; "every other commit route still refuse them."; "writes it as" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:485-604; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:601-601; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:451-451 |
| **The informational MIK-R21 section: where an entry lands once knowledge is text, and that nothing changes before MIK-R37.** | `## Where an entry lands once knowledge is text (MIK-R21)`; "Nothing here changes what a producer emits today." | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:425-484 |
| Curator-owned semantic scope remains required. | `### Curator-authored semantic scope` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:144-194 |
| The public retention input and exact readback requirements. | `### Retain exact siblings when adding new obligations to a family successor` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:356-424 |
| **Per-target realization rationale and role, and the stated supersession of revision 1's target element shape (generated copy).** | "Realization rationale and role: one authored explanation per target"; "this file's element shape supersedes rule 1's" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:101-140; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:8-18 |
| **The MIK-R28 additions: both evidence forms, the facet authored beside the statement draft, and the views, the informational "without proof" list and the migration pass.** | "as a path plus symbol"; "Proofs are shown and counted (MIK-R28)." | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:524-529; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:530-534 |
| The MIK-R30 onboarding-row bullet: its subject forms, its one disposition and when no row is needed. | "An onboarding row (MIK-R30, converted memory only)" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:558-563 |
| The MIK-R11 planned-row bullet: its subject, its three dispositions and the ref each takes, and what does and does not answer the item. | "A planned row (MIK-R11, converted memory only)" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:564-574 |

## Cross-Repo References

No sibling repository defines this file's contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository implementation dependency. | — | — |

## Update History
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): **body update — the MIK-R11 planned-row bullet.** Added a Logic paragraph for the new bullet in the writer section's history-row list (subject `planned:<declared subject>#<effect>`, the three dispositions and their refs, the task owner resolving a `dropped` decision), and one row citing it. The eleven inserted lines moved the MIK-R12 row's section extent and its `every other commit route` anchor; that row was re-pointed by the exact +11 line shift. No verification stamp was advanced.
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): **body update — the MIK-R30 onboarding-row bullet.** Added a Logic paragraph for the new bullet in the writer section's history-row list (subject forms, `no_impact` only, no row needed after a counted change) with architect ruling 2026-09-29T18:49:50 (1), and one row citing it. The six inserted lines moved the MIK-R12 row's `every other commit route` anchor; that row was re-pointed by the exact base-to-working line map. No verification stamp was advanced.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): **body update — the MIK-R28 additions to the writer section.** Added a Logic paragraph: the evidence bullet names both test forms (`path::name` and the ruled `path -k name`), `needs_facet` offers the statement only as a draft while the curator authors the facet, a bare test file is `unresolvable`, and the new bullet "Proofs are shown and counted (MIK-R28)" covers the views, the informational "without proof" list and the migration pass. One new row (`:524-529`, `:530-534`). The change added six lines, so the MIK-R12 row's `:578` range was re-pointed to `:584` by the exact line map, and the installed `memory-citations --fix` widened the MIK-R04 row's heading citation to its section (`:460-484`); no claim wording changed there. No verification stamp was advanced.
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): **body update — the template gains the section "The file writer's sections (MIK-R12)"** after the MIK-R21 section, and the `incidental` line now says the writer writes it as `support`. The Logic paragraph records both, including that the section applies only to converted memory and changes nothing a producer emits; one row was added (`:485`, `:578`, `:451`). The claim that the `incidental` mapping "is MIK-R12's to decide" is kept as the MIK-R21 history it is, and the new paragraph states the decision. The same section reaches the package copy and the 8 harness starter copies through `scripts/sync-skills.py` (the L04 merge kept "Family routes (MIK-R04)" first). The MIK-R04 row moved by the one-line `incidental` insertion and was re-pointed. No verification stamp was advanced.
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): **body update — the template gains the curator-guidance subsection "Family routes (MIK-R04)"** inside the MIK-R21 section. The Logic paragraph above records what it says and that it changes nothing a producer emits; one reference row cites it (`:459`, `:481`). No verification stamp was advanced.
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): **body update — the template gains the informational section "Where an entry lands once knowledge is text (MIK-R21)".** The Logic paragraph above records what it maps and that it changes nothing a producer emits before MIK-R37; one reference row cites it (`:425-457`). This copy was regenerated by `scripts/sync-skills.py`; `--check` reports ok. No verification stamp was advanced.
- 2026-09-28T17:18:24+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): body update — this generated copy now carries the per-target rationale/role element shape, the named refusals and the supersession statement (regenerated by `sync-skills.py`, byte-identical to the canonical template). No stamp advanced.

- 2026-09-26T23:48:33Z — L39: reconciled exact sibling-retention input, immutable endpoint behavior and reporting against the frozen source. Preserved prior history and existing verification metadata; actual source commit stamping remains closeout-owned.

- 2026-09-26T21:17:04+00:00: Generated citation repair: "It is not the curator's side." repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:319-319. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T19:49:05Z — The generated handoff template makes applicability, conditions and exclusions curator-owned semantic scope. Missing scope remains unfilled curation. Changed scope under an allocated entry key is a content conflict that needs a successor; historical records are never silently migrated.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **body update: the packaged copy carries the canonical template's new section** stating the shape of the two keys the producer never writes, `family` and `external_sources`, beside the unchanged thirteen fields — one declaration per local key, `basis` required wherever the curator decides, reuse by identity, a changed guarantee as a successor under a new key, at most 32 sources per entry, and `external_sources: []` meaning examined-and-none while an omitted key means not examined. Written in `skills/l-01-agent-lifecycles/templates/curator-handoff-list.md` and propagated by `scripts/sync-skills.py`. **Citation accounting:** the ranges this card carries into the files this leaf's change set moved were re-derived against the candidate's own bytes rather than shifted by a remembered delta. No claim and no row was dropped, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
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
