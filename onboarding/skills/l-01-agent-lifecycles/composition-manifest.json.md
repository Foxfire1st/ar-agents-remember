# skills/l-01-agent-lifecycles/composition-manifest.json

## Governing Overview

[lifecycle skill overview](overview.md)

## Purpose

This authored manifest is the prose-free routing metadata for canonical role and operation sources. `SKILL.md` remains the thin selector and `skills/` the authoritative source tree. The native route composes the selected role followed by one applicable operation; task and workspace facts remain separate handover data. Retained core/launcher/registry metadata does not inject shared core prose or expand the seven roles this native launcher exposes.

It is authored bytes, not generated output: the parser that consumes it is explicit that "the
declared vocabulary is authoritative over the manifest, not the other way round", so a manifest edit
"can therefore not quietly mint a new role or a ninth operation."

## Code Commentary

### Logic

**Identity and composition.** The schema is `ar-role-capsule-composition/v1`, the router is `SKILL.md` and the authoritative tree is `skills/`. Native `composition_order` is `role` then `operation`. Canonical task/workspace facts travel as separate handover data.

**Explicit routing and retained vocabulary.** `routing_conditions` has supplied-native-role-binding and manual-taskless-projects-role. The role/operation are explicitly supplied; missing, unsupported, inapplicable or conflicting bindings fail closed rather than selecting a default. Manual taskless Projects selection admits Architect/Investigator without a synthetic task. `role_order` still retains ten registry roles; native launch support remains the seven current UI roles.

**`operations` declares each operation's source and the roles that may run it.** Nine entries —
orientation, planning, implementation, review, curation, coordination, authorized-closeout, recovery
and bootstrap — each with a `source` under `operations/`, a one-line `purpose`, and an
`applies_to_roles` list. Two of them are narrow on purpose: `implementation` applies to `worker`
alone, and `bootstrap` to `bootstrap` alone, while `orientation` applies to all ten roles and
`planning` to the four planning seats. The role side repeats the same applicability from the other
direction; the parser refuses a manifest where the two disagree rather than letting the compiler
resolve the conflict at selection time.

**Retained core metadata.** The six `core` entries still name authority, invariants, lifecycle-frame, loop, acceptance and launcher sources. This frozen map is inert metadata for compiler compatibility: the current native route injects no shared core block.

**`roles` is the per-seat registry and is where the selection actually happens.** Each of the ten
entries carries `file` (the role source under `roles/`), `altitude`, `tools` (the tool ids the seat
may use), `skills` (the skill pointers it may reference), `seat` (the one-line statement of what the
seat is), `core` (retained core-selection metadata, not shared instruction injection), `operations` (the authoritative applicability
list), `templates` (the field schemas and handoff artifacts that seat compiles or emits) and
`criteria` (the reviewer criteria catalogs bound to it). The lists differ per seat rather than being
uniform: `implementation` appears only in the worker's operations, the curator's operations are
orientation, curation and recovery, and `curator-handoff-list.md` appears in exactly four template
lists — the orchestrator's, the worker's, the curator's and the reviewer's — which is the registry
wiring behind the producer/consumer hand-off contract. `altitude` is a plain string rather than an
enum, and for the reviewer it is the composite `leaf | master | sprint, by seam`.

**`skills`, retained `launcher` metadata and `references` complete the declared surface.** `skills` declares the one
skill by origin, URI and root source (`agents-remember/skills`, `skill://agents-remember/skills/l-01-agent-lifecycles`,
`SKILL.md`); the parser's own model notes a skill reference "is a *pointer to separately delivered
content*, so its identity is server/repository origin plus skill URI — a bare name would collide
across servers." `launcher` is the ambient launcher's composition: `is_role: false`, the routing
condition it belongs to, `core/launcher.md` as its instruction source, the `launcher` core block,
orientation and coordination as its operations, and `architect-brief.md` as its one template. The
`references` block lists the five reference-only trees — `reference/rationale.md`,
`reference/rulings.md`, `lenses.md`, `criteria/` and `templates/` — each with a `description` and,
all carry `injected: false`, so a reader can see what is available without any of it entering
a composed capsule.

**The identity keys say what the file is and where its authority sits.** `schema` fixes the document
vocabulary at `ar-role-capsule-composition/v1`; `authority` names `SKILL.md` as the thin router and
this file as metadata only; `entry_router` names the router file a session enters through;
`authoritative_tree` is `skills/`, which is the canonical authored tree the packaged copies are
generated from.

**`operations` declares each operation's source and the roles that may run it.** Nine entries —
orientation, planning, implementation, review, curation, coordination, authorized-closeout, recovery
and bootstrap — each with a `source` under `operations/`, a one-line `purpose`, and an
`applies_to_roles` list. Two of them are narrow on purpose: `implementation` applies to `worker`
alone, and `bootstrap` to `bootstrap` alone, while `orientation` applies to all ten roles and
`planning` to the four planning seats. The role side repeats the same applicability from the other
direction; the parser refuses a manifest where the two disagree rather than letting the compiler
resolve the conflict at selection time.

**`core` names the block sources the corpus holds, but a dispatched role seat composes none of them into its capsule.** The manifest's `composition_order` is exactly `role` then `operation` (canonical manifest `600-606`); the frozen core map remains metadata for compiler compatibility and shared core blocks are not injected. `models/role_capsules/selection.py:158-163` returns `core_blocks=()` for a dispatched role seat (developer ruling 2026-09-17): the manifest declaration tells a reader where the doctrine lives, it is not what the seat is sent, and the role file states every obligation that binds the seat.

**`roles` is the per-seat registry and is where the selection actually happens.** Each of the ten
entries carries `file` (the role source under `roles/`), `altitude`, `tools` (the tool ids the seat
may use), `skills` (the skill pointers it may reference), `seat` (the one-line statement of what the
seat is), `core` (the shared-block names the seat lists for capsule composition), `operations` (the authoritative applicability
list), `templates` (the field schemas and handoff artifacts that seat compiles or emits) and
`criteria` (the reviewer criteria catalogs bound to it). The lists differ per seat rather than being
uniform: `implementation` appears only in the worker's operations, the curator's operations are
orientation, curation and recovery, and `curator-handoff-list.md` appears in exactly four template
lists — the orchestrator's, the worker's, the curator's and the reviewer's — which is the registry
wiring behind the producer/consumer hand-off contract. `altitude` is a plain string rather than an
enum, and for the reviewer it is the composite `leaf | master | sprint, by seam`.

**`skills`, `launcher` and `references` complete the declared surface.** `skills` declares the one
skill by origin, URI and root source (`agents-remember/skills`, `skill://agents-remember/skills/l-01-agent-lifecycles`,
`SKILL.md`); the parser's own model notes a skill reference "is a *pointer to separately delivered
content*, so its identity is server/repository origin plus skill URI — a bare name would collide
across servers." `launcher` is the ambient launcher's composition: `is_role: false`, the routing
condition it belongs to, `core/launcher.md` as its instruction source, the `launcher` core block,
orientation and coordination as its operations, and `architect-brief.md` as its one template.

### Conventions

The file is a flat JSON object with `snake_case` keys, ordered so the document reads from identity to
registry to composition to notes. Values that select a file are root-relative POSIX strings
(`roles/architect.md`, `operations/curation.md`, `core/loop.md`), never absolute paths and never
package paths, because the corpus root is supplied by the consumer. Every list that a consumer
iterates is an array of strings or of objects with a `source`/`purpose` pair; nothing is keyed by a
display name where an identity would do, and the one skill entry carries origin plus URI rather than
a bare name. Duplicated knowledge is deliberate and testable: the operations' `applies_to_roles` and
the roles' `operations` are two views of one applicability, and the parser refuses disagreement. The `notes` array states role/operation-only native composition, the inert core map, separate handover facts, the retained ten/nine vocabulary versus seven launchable roles, and bound native role tools.

The file is a flat JSON object with `snake_case` keys, ordered so the document reads from identity to
registry to composition to notes. Values that select a file are root-relative POSIX strings
(`roles/architect.md`, `operations/curation.md`, `core/loop.md`), never absolute paths and never
package paths, because the corpus root is supplied by the consumer. Every list that a consumer
iterates is an array of strings or of objects with a `source`/`purpose` pair; nothing is keyed by a
display name where an identity would do, and the one skill entry carries origin plus URI rather than
a bare name. Duplicated knowledge is deliberate and testable: the operations' `applies_to_roles` and
the roles' `operations` are two views of one applicability, and the parser refuses disagreement. The
`notes` array is where the file states what it is not — routing metadata, no prose, no task facts, and
the launcher is not a role.

### Invariants And Boundaries

- **The manifest carries no instruction prose.** It selects sources; the prose lives in `core/`,
  `roles/`, `operations/`, `criteria/` and `templates/`, and the notes state that this file "carries
  no instruction prose and no copies of any source section."
- **The role registry is exactly `role_order`.** Ten roles; the launcher is a routing condition with
  `is_role: false` and is not an eleventh entry.
- **The declared vocabulary is authoritative over the file.** The consumer parses these bytes against
  frozen role and operation sets and refuses a manifest that disagrees, so an edit cannot mint a role
  or a tenth operation by writing one.
- **Operation applicability must agree on both sides.** A role's `operations` list and the
  operation's `applies_to_roles` list are checked against each other at parse time; a disagreement is
  a `manifest-inconsistent-applicability` refusal rather than a selection-time surprise.
- **One source per instruction.** A block is authored once and referenced by path; a role file states
  its own seat's side of a shared rule and never restates the whole of it.
- **Task facts are not part of the manifest.** They travel as a separate context channel.
- **Reference-only trees do not enter a capsule.** The `references` entries are marked
  `injected: false`, and `lenses.md` is described as material for the scoping seats rather than
  something "a dispatched role" picks.
- **The corpus root is the consumer's, not the file's.** Every declared path is relative to the
  admitted corpus root, which is why the same manifest can be read from the authored tree or from the
  packaged copy without editing a path.

- **The manifest carries no instruction prose.** It selects sources; the prose lives in `core/`,
  `roles/`, `operations/`, `criteria/` and `templates/`, and the notes state that this file "carries
  no instruction prose and no copies of any source section."
- **The role registry is exactly `role_order`.** Ten roles; the launcher is a routing condition with
  `is_role: false` and is not an eleventh entry.
- **The declared vocabulary is authoritative over the file.** The consumer parses these bytes against
  frozen role and operation sets and refuses a manifest that disagrees, so an edit cannot mint a role
  or a tenth operation by writing one.
- **Operation applicability must agree on both sides.** A role's `operations` list and the
  operation's `applies_to_roles` list are checked against each other at parse time; a disagreement is
  a `manifest-inconsistent-applicability` refusal rather than a selection-time surprise.
- **One source per instruction.** A block is authored once and referenced by path; a role file states
  its own seat's side of a shared rule and never restates the whole of it.
- **Task facts are not part of the manifest.** They travel as a separate context channel.
- **Reference-only trees do not enter a capsule.** The `references` entries are marked
  `injected: false`, and `lenses.md` is described as material for the scoping seats rather than
  something "a dispatched role" picks.
- **The corpus root is the consumer's, not the file's.** Every declared path is relative to the
  admitted corpus root, which is why the same manifest can be read from the authored tree or from the
  packaged copy without editing a path.

### Todos

No task-independent follow-up is recorded. The current reference-only entries, including lenses, all explicitly carry injected=false.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The rows below pair the manifest's own declarations with the consumers that read them: the parser
that turns these bytes into typed values, the packaging provider that yields the corpus root and
manifest together, the source admission that gives the manifest its reserved metadata identity, the
install-time corpus anchor, and the corpus test that pins the registry wiring.




- The retained six-block core map is metadata and is not injected into native role capsules. [4]


- The four template lists that register the curator hand-off list, one per seat on either side of that contract (each anchor quotes a sibling entry of the same list, because the shared file name appears in all four). [7]


- The consumer that parses these bytes: the schema constant it checks against, and the pure parser that builds the typed manifest and refuses a vocabulary disagreement. [10]
- The packaging consumer: the manifest is admitted beside its corpus root, and the provider yields root and manifest as one value "because they are one admission". [11]
- The admission identity rule: the manifest is metadata rather than an instruction block, so it takes the reserved metadata identity and can never collide with a real block identity. [12]
- The install-time corpus anchor and the corpus test that reads the manifest by path. [13]

- The document's identity and authority: the schema name, the authority statement naming the thin router, and the authoritative tree the packaged copies are generated from. [15]
- The nine operation blocks, each with its source, purpose and the roles that may run it. [16]
- The six block names the corpus holds (including the launcher block authored here so the registry holds only roles); the manifest composes role then operation only, and a dispatched seat receives no shared core block (`models/role_capsules/selection.py:158-163` returns `core_blocks=()`).
- The role registry itself and the two role entries that show the per-seat shape. [18]
- The per-role entry fields a consumer selects on: the altitude, the tool ids, and the one-line seat statement. [19]
- The four template lists that register the curator hand-off list, one per seat on either side of that contract (each anchor quotes a sibling entry of the same list, because the shared file name appears in all four). [20]
- The launcher entry: a routing condition with its own core block, its operations, and the brief it compiles. [21]
- The reference-only trees that never enter a capsule, the composition order, and the notes that state what the file is not. [22]
- The consumer that parses these bytes: the schema constant it checks against, and the pure parser that builds the typed manifest and refuses a vocabulary disagreement. [23]
- The packaging consumer: the manifest is admitted beside its corpus root, and the provider yields root and manifest as one value "because they are one admission". [24]
- The admission identity rule: the manifest is metadata rather than an instruction block, so it takes the reserved metadata identity and can never collide with a real block identity. [25]
- The install-time corpus anchor and the corpus test that reads the manifest by path. [26]

### Cross-Repo References

No cross-repository behavior is implemented in this file. Every declared path is relative to the
admitted corpus root, the one skill entry names this repository's own tree as its origin, and no
sibling repository or external system is addressed by any key.

No meaningful cross-repo references found.


## Current Investigator contract impact

The manifest exposes canonical Investigator among the seven native roles, requests the approved fourteen Investigator reading tools and preserves explicit Projects/sprint/master launch scope. The single earlier spelling is read normalization outside this routing metadata, not another manifest role. Registry/compiler vocabulary is not a permission grant.

- This source owns the stated current Investigator scope or canonical vocabulary. [14]


## Refreshed current evidence

- The document's identity and authority: the schema name, the authority statement naming the thin router, and the authoritative tree the packaged copies are generated from. [1]
- The role registry in canonical order and the three routing conditions, including the launcher condition that is not a role. [2]
- The nine operation blocks, each with its source, purpose and the roles that may run it. [3]
- The role registry itself and the two role entries that show the per-seat shape. [5]
- The per-role entry fields a consumer selects on: the altitude, the tool ids, and the one-line seat statement. [6]
- The launcher entry: a routing condition with its own core block, its operations, and the brief it compiles. [8]
- The reference-only trees that never enter a capsule, the composition order, and the notes that state what the file is not. [9]

## Inherited Source-Epoch Commentary

The following distribution-copy account preserves useful explanations and source-epoch history, not a second current contract. Its currentness, tool, seat, provider, execution and permission claims are inherited scope unless separately qualified above against the current canonical source. Earlier incompatible claims on the explicitly updated seams are historical, not restored authority. Historical labels in this quotation do not allocate this card's reference numbers.

> # composition-manifest.json
>
> ## Current operative account — MIK-R112
>
> The current source facts below replace the former operative inventory. The separately labelled superseded claims describe only the pre-repair card. Original paragraphs, dated closures, evidence and citation identities remain intact in the explicitly historical section; they grant no current call, restored route or fresh execution acceptance.
>
> - Current roles.bootstrap.tools contains four names and no provider_status.
> - Other role request arrays also remove retired tools and add bounded staying tools.
>
> ### Superseded inventory
>
> - Pre-repair card claim: Card describes bootstrap’s five requested tools, including provider_status. This is superseded archival wording, not a current prescription.
>
> ### Source and authority bounds
>
> - Source comparison: `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/composition-manifest.json:508 (roles.bootstrap.tools)`.
>
> Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.
>
> ## Historical original card — preserved, not the current operative account
>
> <details>
> <summary>Retained original source accounts and producer history</summary>
>
> ## Governing Overview
>
> [MCP package overview](../../../../../../overview.md)
>
> ## Purpose
>
> Routing metadata for the canonical lifecycle corpus; it declares source selection rather than duplicating instruction prose.
>
> ## Current Contract
>
> `routing_conditions` names explicit supplied native role binding and manual taskless Projects selection. Missing, unsupported, inapplicable or conflicting selection fails closed; no role, task, repository, parent or operation default is inferred.
>
> `composition_order` is `role`, then `operation`. The retained core map is inert metadata for the compiler and supplies no shared instructions to a role capsule. Task facts and workspace bindings are a separate handover channel.
>
> The registry/compiler vocabulary retains ten roles and nine operations, while the native launcher exposes seven roles. Native role-start authority is granted only to Architect, Orchestrator and Manager within their documented scope; the seven launched roles receive role messaging.
>
> ## Conventions
>
> Canonical skills/l-01-agent-lifecycles/composition-manifest.json owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy and the eight harness copies; no generated file defines a separate obligation.
>
> ## Invariants And Boundaries
>
> A retained registry entry does not establish native launch support. Select an operation only when the manifest admits it for the role. Generated copies never define separate routing policy.
>
> ## Code Commentary
>
> ### Logic
>
> The manifest's schema is `ar-role-capsule-composition/v1` and its `authority` field states the
> load-bearing boundary directly: `skills/l-01-agent-lifecycles/SKILL.md` is the thin router and this file
> is routing metadata only, with `skills/` as the authoritative tree.
>
> `role_order` lists exactly the ten roles and must agree with the `roles` object; `launcher` declares `is_role: false` and points its
> instruction source at `core/launcher.md`, which is how the corpus keeps the launcher a routing condition
> rather than an invented role.
>
> `operations` declares the **frozen nine-name vocabulary** (`orientation`, `planning`,
> `implementation`, `review`, `curation`, `coordination`, `authorized-closeout`, `recovery`,
> `bootstrap`) with each entry's source file, purpose, and `applies_to_roles`. An operation outside that
> set is an explicit error, never a silent fallback. `core` names the six shared blocks; `roles` names
> each role's altitude, seat, and its four source lists; `references` marks rationale, rulings, lenses,
> criteria, and templates as `injected: false`, so reference material stays out of the normative path.
>
> **The tenth role's entry (added by 260915-CAPS-L13).** `roles.bootstrap` declares
> `"altitude": "free-agent"` — the only role whose altitude is not a task altitude — with `seat`
> describing the first-hour setup seat, three operations (`orientation`, `bootstrap`, `recovery`), the
> three shared core blocks, five requested tools, and empty `templates` and `criteria` lists. The
> `operations.bootstrap` entry names `operations/bootstrap.md` and `applies_to_roles: ["bootstrap"]`, so
> exactly one role carries it. Both additions are **appends**: `bootstrap` is last in `role_order` and
> last in `operations`, so no pre-existing index, settings key, or projection addressed to an earlier
> role shifts because it was added.
>
> **Declared capability metadata (added by 260915-CAPS-L2).** The routing plane now also declares
> *what each seat asks for*, which is a different thing from *what it is permitted*. The manifest
> gained **41 keys and lost none** against the file L1 shipped: a new top-level `skills` object, a
> per-role `tools` array and `skills` array, and a `launcher.operations` list.
>
> - **`skills`** (top level, **new**) — the declared skill registry, keyed by skill name. The one
>   entry is `l-01-agent-lifecycles` = `{"origin": "agents-remember/skills", "uri":
>   "skill://agents-remember/skills/l-01-agent-lifecycles", "source": "SKILL.md"}`. Identity is
>   **origin plus skill name**, because a bare name collides across servers; `source` names the
>   skill's root instruction file, whose content digest is what a reference's `revision` means. A
>   bare `skills: ["l-01-agent-lifecycles"]` on a role is therefore a *pointer into this registry*,
>   not a name that stands alone.
>
> - `roles.<role>.tools` — the tool identities the role's compiled capsule requests. (the tenth role contributes five: `runtime_install`, `memory_init`,
>   `memory_baseline_status`, `memory_baseline_adopt`, `provider_status`). They
>   are **requests, not grants**: the
>   compiler narrows them against the admitted `CapsuleToolPolicy` snapshot and refuses an id outside
>   it. A role-to-tool table authored in Python instead would be a second source of truth about a
>   role — exactly what this corpus's one-source-per-instruction rule forbids — and in
>   `application/` it would read as a grant rather than a request.
>
> - `roles.<role>.skills` — **one skill reference per role**, each pointing into the registry above.
>   **This channel is carried, not narrowed**: the compiler builds a content-addressed reference
>   (`origin`, `identity`, `uri`, `revision`) and consults **no** permission policy, because a skill
>   reference points at separately delivered content rather than asking for a capability. Do not
>   describe it as narrowed or granted.
>
> - `launcher.operations` — `[]` became `["orientation", "coordination"]`.
>
> These key families are what a role capsule returns as its separately typed requested-tool
> identities and optional skill references, so the compiler can obey that requirement without
> inventing a second authority. A declared skill's root file must be admitted, or its revision would
> be a fiction; both the metadata plane and the compiled plane fail closed.
>
> ### Conventions
>
> Edit the canonical `skills/l-01-agent-lifecycles/composition-manifest.json` and let
> `scripts/sync-skills.py` propagate it. A new operation name or a role source that does not exist is
> rejected by the shipped check rather than tolerated. `tools` and `skills` are treated as
> **optional** by the parser, so their presence is additive and removing them leaves a manifest that
> still parses and compiles for every role (returning no requests and no skill references).
>
> ### Invariants And Boundaries
>
> - This file is metadata, not doctrine: adding prose here duplicates a rule that already has one home.
> - The operation vocabulary is closed at nine names; the role registry is closed at ten roles.
> - **The tenth role is a free agent.** `roles.bootstrap` carries `"altitude": "free-agent"`, which is
>   not a task altitude, and its `operations` list is the only one containing `bootstrap`. Adding a task
>   altitude to it, or letting a second role claim that operation, is a corpus design change rather than
>   a metadata tidy.
> - Every `source`, `file`, template, and criteria path it names must exist — a missing source is an error,
>   not a skip.
> - Exactly one source per instruction; `core/` is authored once and a role file never restates a shared
>   rule.
> - The launcher is `is_role: false` and has no entry under `roles`.
> - **A declared tool identity is a request, never a permission.** This file says what a role asks
>   for; the admitted `CapsuleToolPolicy` snapshot says what is permitted. Do not merge the two
>   authorities, and do not treat this file as a policy source.
> - A generated copy is never hand-edited. This card documents the packaged copy; its content is
>   byte-identical to the canonical source (all ten copies share one sha256).
> - **The skill channel is carried, not narrowed.** `skills.<name>` declares `origin`/`uri`/`source`,
>   and a role's `skills` entry is a pointer into that registry. The compiler consults no permission
>   policy for a skill reference, so describing one as narrowed, permitted, or granted is wrong. What
>   *is* enforced is that each declared skill's root `source` file must be admitted, or its revision
>   would be a fiction.
> - A skill name in `roles.<role>.skills` must resolve in the top-level `skills` object. An
>   unresolvable declaration is refused (`_require_role_skills_are_declared`), never dropped.
>
> ### Todos
>
> None recorded.
>
> ## Evidence
>
> ### Repo-Internal References
>
> | Finding | Anchor | References |
> | --- | --- | --- |
> | The two explicit routing conditions and their scope/refusal fields. | lines 18-36 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/composition-manifest.json:18-36 |
> | Role/operation order, inert core metadata, separate facts and seven-launcher distinction. | lines 593-602 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/composition-manifest.json:593-602 |
>
> ### Docs References
>
> No external or domain documentation governs this repository-local instruction file; it is canonical
> repository prose consumed by the skill router.
>
> No relevant documentation found after checking live sources.
>
> ### Repo-Internal References
>
> The manifest is consumed by the deterministic capsule compiler through the package
> `agents_remember.models.role_capsules`; the rows below are the consuming seams and the shipped
> guards that hold this file's declarations true.
>
> - The manifest resolves every role and operation source and keeps the registry at ten roles. (historical reference 1)
> - A manifest entry pointing at a missing source, an unknown operation, an unknown core block, or a missing criteria catalog is reported instead of silently accepted. (historical reference 2)
> - The canonical source of this metadata plane. (historical reference 3)
> - Declared tool identities are **requests** narrowed against the admitted policy snapshot, never grants; an id outside it is refused. (historical reference 4)
> - **The declared skill registry and the skill entry shape** — the parser that turns `skills.<name>` into `CapsuleSkillEntry`. (historical reference 5)
> - **Skill references are carried, not narrowed.** (historical reference 6)
> - A declared skill must resolve in the registry, and its root file must be admitted. (historical reference 7)
> - The parser treats `tools` and `skills` as optional and refuses a manifest that disagrees with the frozen vocabulary. (historical reference 8)
> - The carried skill channel against the shipped corpus: one reference per declaration, revision follows the admitted bytes. (historical reference 9)
> - The L13 additions as the compiler reads them: the tenth role's source, altitude and single-carrier operation. (historical reference 10)
>
> ### Cross-Repo References
>
> No sibling-repository contract defines this instruction file.
>
> No meaningful cross-repo references found.
>
> </details>

Inherited reference 1 commentary (not a revalidated target):

> The manifest resolves every role and operation source and keeps the registry at ten roles.

Inherited reference 10 commentary (not a revalidated target):

> The L13 additions as the compiler reads them: the tenth role's source, altitude and single-carrier operation.
>
> Anchor: `bootstrap`

Inherited reference 2 commentary (not a revalidated target):

> A manifest entry pointing at a missing source, an unknown operation, an unknown core block, or a missing criteria catalog is reported instead of silently accepted.

Inherited reference 3 commentary (not a revalidated target):

> The canonical source of this metadata plane.
>
> Anchor: `schema`

Inherited reference 4 commentary (not a revalidated target):

> Declared tool identities are **requests** narrowed against the admitted policy snapshot, never grants; an id outside it is refused.

Inherited reference 5 commentary (not a revalidated target):

> **The declared skill registry and the skill entry shape** — the parser that turns `skills.<name>` into `CapsuleSkillEntry`.

Inherited reference 6 commentary (not a revalidated target):

> **Skill references are carried, not narrowed.**

Inherited reference 7 commentary (not a revalidated target):

> A declared skill must resolve in the registry, and its root file must be admitted.

Inherited reference 8 commentary (not a revalidated target):

> The parser treats `tools` and `skills` as optional and refuses a manifest that disagrees with the frozen vocabulary.

Inherited reference 9 commentary (not a revalidated target):

> The carried skill channel against the shipped corpus: one reference per declaration, revision follows the admitted bytes.

## Canonical Source Ownership

The byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. Whole-file source evidence does not certify inherited statements, execution, grading or the whole card.

- The authored source owns this contract; the distribution copy is not a separate authority. [27]
