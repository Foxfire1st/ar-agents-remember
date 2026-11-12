# skills/l-01-agent-lifecycles/composition-manifest.json

## Governing Overview

[overview](overview.md)

## Purpose

This authored manifest is the prose-free routing metadata for canonical role and operation sources. `SKILL.md` remains the thin selector and `skills/` the authoritative source tree. The native route composes the selected role followed by one applicable operation; task and workspace facts remain separate handover data. Retained core/launcher/registry metadata does not inject shared core prose or expand the eight canonical roles this native launcher exposes.

It is authored bytes, not generated output: the parser that consumes it is explicit that "the
declared vocabulary is authoritative over the manifest, not the other way round", so a manifest edit
"can therefore not quietly mint a new role or a ninth operation."

## Current Source Qualification

The `bootstrap` role's tool list holds `runtime_install`, `memory_init`, `memory_baseline_status`, `memory_baseline_adopt`, `role_message` and `user_settings_init`, and its one template is `bootstrap-report.md`. Its two Bootstrap-only step details are `bootstrap/foundation-state` (`reference/bootstrap/foundation-state.md`, "the foundation state this seat reports and the Architect handover that follows it") and `bootstrap/failure-states` (`reference/bootstrap/failure-states.md`, "the states a new user's setup actually hits, and the move for each", read when a step returns a state the seat cannot name). Both stay non-injected step details for the `bootstrap` role, which also reads the shared step details `refused-write`, `knowledge/use`, `knowledge/commands`, `tasks/document-authoring` and `sandbox-actors`.

## Code Commentary

### Logic

**Identity and composition.** The schema is `ar-role-capsule-composition/v1`, the router is `SKILL.md` and the authoritative tree is `skills/`. Native `composition_order` is `role` then `operation`. Canonical task/workspace facts travel as separate handover data.

**Explicit routing and retained vocabulary.** `routing_conditions` has supplied-native-role-binding and manual-taskless-projects-role. The role/operation are explicitly supplied; missing, unsupported, inapplicable or conflicting bindings fail closed rather than selecting a default. Manual taskless Projects selection admits Architect/Investigator without a synthetic task. `role_order` and the frozen role vocabulary hold the eight launchable roles, including Bootstrap; the system-specialist spelling is an alias of Investigator that the launcher code reads, not a manifest role.

**`operations` declares each operation's source and the roles that may run it.** Nine entries —
orientation, planning, implementation, review, curation, coordination, authorized-closeout, recovery
and bootstrap — each with a `source` under `operations/`, a one-line `purpose`, and an
`applies_to_roles` list. Two of them are narrow on purpose: `implementation` applies to `worker`
alone, and `bootstrap` to `bootstrap` alone, while `orientation` applies to all eight roles and
`planning` to the Architect and the Orchestrator. The role side repeats the same applicability from the other
direction; the parser refuses a manifest where the two disagree rather than letting the compiler
resolve the conflict at selection time.

**Core metadata.** The seven `core` entries name authority, invariants, lifecycle-frame, loop, acceptance, launcher and the separately delivered every-role digest. The map records source ownership: a role capsule receives no shared core block, and the digest accompanies the capsule in its first message. The lifecycle-frame purpose names task worktree records and the landing chain contract lifecycle, not ambient adoption.

**`roles` is the per-seat registry and is where the selection actually happens.** Each of the eight
entries carries `file` (the role source under `roles/`), `altitude`, `tools` (the tool ids the seat
may use), `skills` (the skill pointers it may reference), `seat` (the one-line statement of what the
seat is), `core` (retained core-selection metadata, not shared instruction injection), `operations` (the authoritative applicability
list), `templates` (the field schemas and handoff artifacts that seat compiles or emits) and
`criteria` (the reviewer criteria catalogs bound to it). The lists differ per seat rather than being
uniform: `implementation` appears only in the worker's operations, the curator's operations are
orientation, curation and recovery, and `curator-handoff-list.md` appears in exactly four template
lists — the orchestrator's, the worker's, the curator's and the reviewer's — which is the registry
wiring behind the producer/consumer hand-off contract. `altitude` is a plain string rather than an
enum; the reviewer's is `leaf`.

**`skills`, retained `launcher` metadata and `references` complete the declared surface.** `skills` declares the one
skill by origin, URI and root source (`agents-remember/skills`, `skill://agents-remember/skills/l-01-agent-lifecycles`,
`SKILL.md`); the parser's own model notes a skill reference "is a *pointer to separately delivered
content*, so its identity is server/repository origin plus skill URI — a bare name would collide
across servers." `launcher` is the ambient launcher's composition: `is_role: false`, the routing
condition it belongs to, `core/launcher.md` as its instruction source, the `launcher` core block,
orientation and coordination as its operations, and no template. The `references` block holds 50 entries: the digest map, the `criteria/` and `templates/` trees, the detail files under the `reference/` subject folders and the template entries. 38 declare `step_detail: true`, including `writing/visual-explainers`, and 10 declare `step_detail: false`. Entries carry `injected: false`; step details declare their reader roles and read step, rather than entering the inline instruction body.

**The identity keys say what the file is and where its authority sits.** `schema` fixes the document
vocabulary at `ar-role-capsule-composition/v1`; `authority` names `SKILL.md` as the thin router and
this file as metadata only; `entry_router` names the router file a session enters through;
`authoritative_tree` is `skills/`, which is the canonical authored tree the packaged copies are
generated from.

**`operations` declares each operation's source and the roles that may run it.** Nine entries —
orientation, planning, implementation, review, curation, coordination, authorized-closeout, recovery
and bootstrap — each with a `source` under `operations/`, a one-line `purpose`, and an
`applies_to_roles` list. Two of them are narrow on purpose: `implementation` applies to `worker`
alone, and `bootstrap` to `bootstrap` alone, while `orientation` applies to all eight roles and
`planning` to the Architect and the Orchestrator. The role side repeats the same applicability from the other
direction; the parser refuses a manifest where the two disagree rather than letting the compiler
resolve the conflict at selection time.

**`core` names the block sources the corpus holds, but a dispatched role seat composes none of them into its capsule.** The manifest's `composition_order` is exactly `role` then `operation` (canonical manifest `1082-1085`); the frozen core map remains metadata for compiler compatibility and shared core blocks are not injected. `models/role_capsules/selection.py:158-163` returns `core_blocks=()` for a dispatched role seat: the manifest declaration tells a reader where the doctrine lives, it is not what the seat is sent; the seat's binding text is its role and operation, the every-role digest and each detail read at its named step.

**`roles` is the per-seat registry and is where the selection actually happens.** Each of the eight
entries carries `file` (the role source under `roles/`), `altitude`, `tools` (the tool ids the seat
may use), `skills` (the skill pointers it may reference), `seat` (the one-line statement of what the
seat is), `core` (retained shared-block metadata, not injected role instructions), `operations` (the authoritative applicability
list), `templates` (the field schemas and handoff artifacts that seat compiles or emits) and
`criteria` (the reviewer criteria catalogs bound to it). The lists differ per seat rather than being
uniform: `implementation` appears only in the worker's operations, the curator's operations are
orientation, curation and recovery, and `curator-handoff-list.md` appears in exactly four template
lists — the orchestrator's, the worker's, the curator's and the reviewer's — which is the registry
wiring behind the producer/consumer hand-off contract. `altitude` is a plain string rather than an
enum; the reviewer's is `leaf`.

**`skills`, `launcher` and `references` complete the declared surface.** `skills` declares the one
skill by origin, URI and root source (`agents-remember/skills`, `skill://agents-remember/skills/l-01-agent-lifecycles`,
`SKILL.md`); the parser's own model notes a skill reference "is a *pointer to separately delivered
content*, so its identity is server/repository origin plus skill URI — a bare name would collide
across servers." `launcher` is the ambient launcher's composition: `is_role: false`, the routing
condition it belongs to, `core/launcher.md` as its instruction source, the `launcher` core block,
orientation and coordination as its operations, and no template.

### Conventions

The file is a flat JSON object with `snake_case` keys, ordered so the document reads from identity to
registry to composition to notes. Values that select a file are root-relative POSIX strings
(`roles/architect.md`, `operations/curation.md`, `core/loop.md`), never absolute paths and never
package paths, because the corpus root is supplied by the consumer. Every list that a consumer
iterates is an array of strings or of objects with a `source`/`purpose` pair; nothing is keyed by a
display name where an identity would do, and the one skill entry carries origin plus URI rather than
a bare name. Duplicated knowledge is deliberate and testable: the operations' `applies_to_roles` and
the roles' `operations` are two views of one applicability, and the parser refuses disagreement. The `notes` array states role/operation-only composition, core metadata as source ownership with the digest accompanying the capsule, separate handover facts, eight launchable roles and nine operations with agreeing applicability, and Paseo as host with `role_start` and `role_message`.

The file is a flat JSON object with `snake_case` keys, ordered so the document reads from identity to
registry to composition to notes. Values that select a file are root-relative POSIX strings
(`roles/architect.md`, `operations/curation.md`, `core/loop.md`), never absolute paths and never
package paths, because the corpus root is supplied by the consumer. Every list that a consumer
iterates is an array of strings or of objects with a `source`/`purpose` pair; nothing is keyed by a
display name where an identity would do, and the one skill entry carries origin plus URI rather than
a bare name. Duplicated knowledge is deliberate and testable: the operations' `applies_to_roles` and
the roles' `operations` are two views of one applicability, and the parser refuses disagreement. The
`notes` array is where the file states what it is: routing metadata, with task facts carried separately.

### Invariants And Boundaries

- **The manifest carries no instruction prose.** It selects sources; the prose lives in `core/`,
  `roles/`, `operations/`, `criteria/` and `templates/`, and the file
  holds no instruction text of its own.
- **The role registry is exactly `role_order`.** Eight roles; the launcher is a routing condition with
  `is_role: false` and is not a ninth entry.
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
  `injected: false`; a declared step detail is read at its step, not composed into the capsule.
- **The corpus root is the consumer's, not the file's.** Every declared path is relative to the
  admitted corpus root, which is why the same manifest can be read from the authored tree or from the
  packaged copy without editing a path.

### Todos

No task-independent follow-up is recorded. The current reference entries all explicitly carry injected=false.

## Current composition and authoring contract

Operations declare `audience`: `sections` for the eight marked operation sources and `all` for the protected authorized-closeout source. The stage markers select common text and named-role text rather than requiring the complete multi-role operation in every capsule. Selected role text remains whole; task facts remain separate handover data.

The references registry declares 38 entries with `step_detail: true`, step text and eligible roles, with `injected: false`, including the writing profile and the visual-explainer file; they are separate named-step material, not a second instruction authority. Registration is not proof of a real start or a read at the named step.

Retained core metadata remains non-injected for native role capsules; the eight-role, nine-operation vocabulary matches the native launcher roster. Requested tools are metadata, not grants; public start admission owns may-start permission.

The current template lists are: Architect, Investigator and the launcher none; Orchestrator `manager-brief.md`, `master-handover-packet.md`, `impact-analysis.md`, `onboarding-coherency.md` and `curator-handoff-list.md`; Manager `manager-brief.md`, `curator-brief.md`, `master-handover-packet.md`, `verdict.md` and `turn-report.md`; Worker `turn-report.md` and `curator-handoff-list.md`; Curator `curator-brief.md`, `curator-handoff-list.md` and `curator-handoff-ingestion.md`; Reviewer `verdict.md`, `impact-analysis.md`, `onboarding-coherency.md` and `curator-handoff-list.md`; Bootstrap `bootstrap-report.md`. No seat lists `architect-brief.md`, `worker-brief.md` or `conversation-handover-packet.md`. The Reviewer seat is an independent Reviewer hosted on a leaf whose intake selects the reviewed candidate, requirement and seam.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The rows below pair the manifest's own declarations with the consumers that read them: the parser
that turns these bytes into typed values, the packaging provider that yields the corpus root and
manifest together, the source admission that gives the manifest its reserved metadata identity, the
install-time corpus anchor, and the corpus test that pins the registry wiring.

- The four template lists that register the curator hand-off list, one per seat on either side of that contract (each anchor quotes a sibling entry of the same list, because the shared file name appears in all four). [7]

- The consumer that parses these bytes: the schema constant it checks against, and the pure parser that builds the typed manifest and refuses a vocabulary disagreement. [10]

- The packaging consumer: the manifest is admitted beside its corpus root, and the provider yields root and manifest as one value "because they are one admission". [11]
- The admission identity rule: the manifest is metadata rather than an instruction block, so it takes the reserved metadata identity and can never collide with a real block identity. [12]
- The install-time corpus anchor and the corpus test that reads the manifest by path. [13]

- The document's identity and authority: the schema name, the authority statement naming the thin router, and the authoritative tree the packaged copies are generated from. [15]

- The nine operation blocks, each with its source, purpose and the roles that may run it. [16]

- The seven block names the corpus holds (including the launcher block authored here so the registry holds only roles, and the every-role digest); the manifest composes role then operation only, and a dispatched seat receives no shared core block (`models/role_capsules/selection.py:158-163` returns `core_blocks=()`).

- The four template lists that register the curator hand-off list, one per seat on either side of that contract (each anchor quotes a sibling entry of the same list, because the shared file name appears in all four). [20]

- The launcher entry: a routing condition with its own core block and its operations; it compiles no template. [21]

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

The manifest exposes canonical Investigator among the eight native roles, requests the seven Investigator reading tools and preserves explicit Projects/sprint/master launch scope. The single earlier spelling is read normalization outside this routing metadata, not another manifest role. Registry/compiler vocabulary is not a permission grant.

## Refreshed current evidence

- The document's identity and authority: the schema name, the authority statement naming the thin router, and the authoritative tree the packaged copies are generated from. [1]

- The role registry in canonical order and the two routing conditions, with the non-role launcher declared separately. [32]

- The nine operation blocks, each with its source, purpose and the roles that may run it. [3]

- The launcher entry: a routing condition with its own core block and its operations; it compiles no template. [8]

## Canonical Source Ownership

The byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. Whole-file source evidence does not certify inherited statements, execution, grading or the whole card.

## Current account — the curator's requested tool list

The curator role's `tools` list requests `knowledge_write` beside `knowledge_read`. The list requests tools: it is checked against the published tool roster and enters the seal digest, so it records what the role may reach and grants nothing by itself. The mounted `knowledge_write` runs the same leaf writer with the same arguments as `knowledge-ingest`, which is why the curator's role text may name it as an authoring route.

- The curator role requests `knowledge_write` beside the other knowledge operations, so the mounted writer is among the tools its capsule may name. [31]

- The core-source map's lifecycle-frame entry names task worktree records and the landing chain's lifecycle, not session adoption; the lifecycle-frame source points to the public worktree_start, worktree_attach and terminal-lifecycle references. [4]

- The role registry itself and the two role entries that show the per-seat shape. [5]

- The per-role entry fields a consumer selects on: the altitude, the tool ids, and the one-line seat statement. [6]

- The manifest records reference material and declared named-step details with injected:false, composes role then operation, and keeps shared core blocks out of that stream. The shared digest travels beside the capsule in its first message. [9]
- The manifest records reference material and declared named-step details with injected:false, composes role then operation, and keeps shared core blocks out of that stream. The shared digest travels beside the capsule in its first message. [22]
- The authored source owns this contract; the distribution copy is not a separate authority. [27]
- All nine operation entries declare audience selection. The references registry contains 50 entries, 38 marked step_detail; the shared digest is declared separately in core metadata. These are parsed registry declarations, not a compiled capsule or execution result. Anchor: `references` [29]
- The manifest declares audience selection for all nine operations and records 50 reference entries, 38 marked step_detail. The role/operation order and the separately delivered shared digest are explicit routing declarations. Anchor: `composition_order` [30]
- The registry contains 38 non-injected step-detail entries, including `refused-write` and `writing/visual-explainers`. Named readers and steps are declarations, not proof that a particular role read a file. [33]

- The manifest retains canonical Investigator with seven declared tool IDs and separately names Bootstrap; the current public LauncherRole roster has eight canonical roles plus the system-specialist alias, not a second Investigator role. [14]

- The role registry itself and the two role entries that show the per-seat shape. [18]

- The per-role entry fields a consumer selects on: the altitude, the tool ids, and the one-line seat statement. [19]
