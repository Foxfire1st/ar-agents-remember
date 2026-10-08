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

### Conventions

The file is a flat JSON object with `snake_case` keys, ordered so the document reads from identity to
registry to composition to notes. Values that select a file are root-relative POSIX strings
(`roles/architect.md`, `operations/curation.md`, `core/loop.md`), never absolute paths and never
package paths, because the corpus root is supplied by the consumer. Every list that a consumer
iterates is an array of strings or of objects with a `source`/`purpose` pair; nothing is keyed by a
display name where an identity would do, and the one skill entry carries origin plus URI rather than
a bare name. Duplicated knowledge is deliberate and testable: the operations' `applies_to_roles` and
the roles' `operations` are two views of one applicability, and the parser refuses disagreement. The `notes` array states role/operation-only native composition, the inert core map, separate handover facts, the retained ten/nine vocabulary versus seven launchable roles, and bound native role tools.

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
