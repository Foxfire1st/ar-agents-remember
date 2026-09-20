# skills/l-01-agent-lifecycles/composition-manifest.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/composition-manifest.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T17:09+02:00 |
| lastVerifiedCommitHash | `562cef4ca64de5b11712d5165d24e78c9a035312` |
| lastVerifiedCommitDate | 2026-09-19T17:51:43+02:00|
| governingOverview | `skills/l-01-agent-lifecycles/overview.md` |

## Governing Overview

[lifecycle skill overview](overview.md)

## Purpose

The routing metadata for the `l-01-agent-lifecycles` corpus: it maps a role and an operation to the
source files that carry the instruction, and carries no instruction prose of its own. Its own
`authority` key states the relationship — "skills/l-01-agent-lifecycles/SKILL.md (thin router) · this
file is routing metadata only" — and the `notes` block repeats the rule the whole corpus is built on:
"Exactly one source per instruction. core/ is authored once; a role file states its own seat's side of
a shared rule and never restates the whole of it." The router's own table names it the "Routing
metadata" layer holding "role → core + role + operation blocks; no prose."

It is authored bytes, not generated output: the parser that consumes it is explicit that "the
declared vocabulary is authoritative over the manifest, not the other way round", so a manifest edit
"can therefore not quietly mint a new role or a ninth operation."

## Code Commentary

### Logic

**The identity keys say what the file is and where its authority sits.** `schema` fixes the document
vocabulary at `ar-role-capsule-composition/v1`; `authority` names `SKILL.md` as the thin router and
this file as metadata only; `entry_router` names the router file a session enters through;
`authoritative_tree` is `skills/`, which is the canonical authored tree the packaged copies are
generated from. `composition_order` is the three-step order a capsule is composed in — `role`,
`operation`, `repository-specialization` — and the `notes` array states the four boundaries of the
metadata plane, including "Task facts are a separate context channel and are not part of this
manifest."

**`role_order` is the role registry, and `routing_conditions` is the router, expressed as data.**
`role_order` lists the ten roles in canonical order: architect, orchestrator, designer, strategist,
manager, worker, curator, reviewer, system-specialist, bootstrap. The `notes` block fixes the
consequence: "The launcher is a routing condition, not a role: the role registry is exactly the
entries in `role_order`." `routing_conditions` holds the three conditions in order — `spawn-role-env`
(selected from `AR_SPAWN_ROLE`, `never_selects: launcher`, failing closed when the value has no
matching `roles/<value>.md` or arrives without its plane-injected hosted identity),
`fresh-session-role-brief` (the first user message is a `templates/*-brief.md`-shaped dispatch or a
first line of the form `ROLE BRIEF - <role>`), and `ambient-launcher` (no spawn-role env and no role
brief), which carries `is_role: false` and points its `instruction_source` at `core/launcher.md`.

**`operations` declares each operation's source and the roles that may run it.** Nine entries —
orientation, planning, implementation, review, curation, coordination, authorized-closeout, recovery
and bootstrap — each with a `source` under `operations/`, a one-line `purpose`, and an
`applies_to_roles` list. Two of them are narrow on purpose: `implementation` applies to `worker`
alone, and `bootstrap` to `bootstrap` alone, while `orientation` applies to all ten roles and
`planning` to the four planning seats. The role side repeats the same applicability from the other
direction; the parser refuses a manifest where the two disagree rather than letting the compiler
resolve the conflict at selection time.

**`core` declares the six shared blocks every role can be composed with.** Each entry pairs a `source`
under `core/` with a `purpose`: `authority` (seat authority, the dispatch transaction, takeover, the
escalation ladder), `invariants` (the shared invariants and the task-doc/branch/worktree spine),
`lifecycle-frame` (the six signals and the trust checkpoint), `loop` (the three-party loop doctrine),
`acceptance` (completion truth vs acceptance and the handoff artifact table), and `launcher` (the
ambient launcher's own obligations, "authored here so the role registry holds only roles").

**`roles` is the per-seat registry and is where the selection actually happens.** Each of the ten
entries carries `file` (the role source under `roles/`), `altitude`, `tools` (the tool ids the seat
may use), `skills` (the skill pointers it may reference), `seat` (the one-line statement of what the
seat is), `core` (which shared blocks compose into it), `operations` (the authoritative applicability
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
orientation and coordination as its operations, and `architect-brief.md` as its one template. The
`references` block lists the five reference-only trees — `reference/rationale.md`,
`reference/rulings.md`, `lenses.md`, `criteria/` and `templates/` — each with a `description` and,
except `lenses`, `injected: false`, so a reader can see what is available without any of it entering
a composed capsule.

### Conventions

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

### Todos

No task-independent follow-up is recorded in the file. One deliberate asymmetry is worth knowing
rather than fixing: `references.lenses` carries no `injected` field while its four siblings do, and
the value that field would carry is the same `false`.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The rows below pair the manifest's own declarations with the consumers that read them: the parser
that turns these bytes into typed values, the packaging provider that yields the corpus root and
manifest together, the source admission that gives the manifest its reserved metadata identity, the
install-time corpus anchor, and the corpus test that pins the registry wiring.

| Finding | Anchor | Source |
| --- | --- | --- |
| The document's identity and authority: the schema name, the authority statement naming the thin router, and the authoritative tree the packaged copies are generated from. | "ar-role-capsule-composition/v1"; "skills/l-01-agent-lifecycles/SKILL.md (thin router)"; "authoritative_tree" | skills/l-01-agent-lifecycles/composition-manifest.json:2-2; skills/l-01-agent-lifecycles/composition-manifest.json:3-3; skills/l-01-agent-lifecycles/composition-manifest.json:5-5 |
| The role registry in canonical order and the three routing conditions, including the launcher condition that is not a role. | "role_order"; "spawn-role-env"; "fresh-session-role-brief"; "ambient-launcher" | skills/l-01-agent-lifecycles/composition-manifest.json:6-17; skills/l-01-agent-lifecycles/composition-manifest.json:18-26; skills/l-01-agent-lifecycles/composition-manifest.json:27-34; skills/l-01-agent-lifecycles/composition-manifest.json:35-44 |
| The nine operation blocks, each with its source, purpose and the roles that may run it. | "operations"; "orientation"; "curation" | skills/l-01-agent-lifecycles/composition-manifest.json:45-134; skills/l-01-agent-lifecycles/composition-manifest.json:46-61; skills/l-01-agent-lifecycles/composition-manifest.json:89-96 |
| The six shared core blocks a role may be composed with, including the launcher block authored here so the registry holds only roles. | "core"; "authority"; "launcher" | skills/l-01-agent-lifecycles/composition-manifest.json:135-160; skills/l-01-agent-lifecycles/composition-manifest.json:136-139; skills/l-01-agent-lifecycles/composition-manifest.json:156-159 |
| The role registry itself and the two role entries that show the per-seat shape. | "roles"; "roles/architect.md"; "roles/orchestrator.md" | skills/l-01-agent-lifecycles/composition-manifest.json:161-161; skills/l-01-agent-lifecycles/composition-manifest.json:162-198; skills/l-01-agent-lifecycles/composition-manifest.json:200-242 |
| The per-role entry fields a consumer selects on: the altitude, the tool ids, and the one-line seat statement. | "altitude"; "tools"; "seat" | skills/l-01-agent-lifecycles/composition-manifest.json:382-382; skills/l-01-agent-lifecycles/composition-manifest.json:383-387; skills/l-01-agent-lifecycles/composition-manifest.json:391-391 |
| The four template lists that register the curator hand-off list, one per seat on either side of that contract (each anchor quotes a sibling entry of the same list, because the shared file name appears in all four). | "master-handover-packet.md"; "turn-report.md"; "curator-brief.md"; "impact-analysis.md" | skills/l-01-agent-lifecycles/composition-manifest.json:231-238; skills/l-01-agent-lifecycles/composition-manifest.json:371-375; skills/l-01-agent-lifecycles/composition-manifest.json:402-405; skills/l-01-agent-lifecycles/composition-manifest.json:433-438 |
| The launcher entry: a routing condition with its own core block, its operations, and the brief it compiles. | "launcher"; "is_role" | skills/l-01-agent-lifecycles/composition-manifest.json:505-520; skills/l-01-agent-lifecycles/composition-manifest.json:506-506 |
| The reference-only trees that never enter a capsule, the composition order, and the notes that state what the file is not. | "injected"; "composition_order"; "Routing metadata only: this file carries no instruction prose and no copies of any source section." | skills/l-01-agent-lifecycles/composition-manifest.json:521-546; skills/l-01-agent-lifecycles/composition-manifest.json:548-552; skills/l-01-agent-lifecycles/composition-manifest.json:553-558 |
| The consumer that parses these bytes: the schema constant it checks against, and the pure parser that builds the typed manifest and refuses a vocabulary disagreement. | `COMPOSITION_MANIFEST_SCHEMA`; `parse_composition_manifest` | mcp/src/agents_remember/models/role_capsules/manifest.py:37-37; mcp/src/agents_remember/models/role_capsules/manifest.py:168-215 |
| The packaging consumer: the manifest is admitted beside its corpus root, and the provider yields root and manifest as one value "because they are one admission". | `COMPOSITION_MANIFEST`; `shipped_composition_corpus` | mcp/src/agents_remember/application/skill_resources/capsule.py:87-88; mcp/src/agents_remember/application/skill_resources/provider.py:50-64 |
| The admission identity rule: the manifest is metadata rather than an instruction block, so it takes the reserved metadata identity and can never collide with a real block identity. | `_identity_for` | mcp/src/agents_remember/application/role_capsules/sources.py:160-166 |
| The install-time corpus anchor and the corpus test that reads the manifest by path. | `CORPUS_ANCHOR`; `MANIFEST_PATH` | mcp/src/agents_remember/install/experiment.py:96-97; mcp/tests/test_role_instruction_corpus.py:33-33 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every declared path is relative to the
admitted corpus root, the one skill entry names this repository's own tree as its origin, and no
sibling repository or external system is addressed by any key.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-19T17:09+02:00 — 260915-KS-L28 curator: created this one-to-one card for the lifecycle
  corpus's routing manifest. It records the identity and authority keys, the ten-role `role_order`
  registry and the three `routing_conditions`, the nine `operations` blocks with their applicability
  lists, the six shared `core` blocks, the per-seat `roles` entries (file, altitude, tools, skills,
  seat, core, operations, templates, criteria) and the four template lists that register the curator
  hand-off list, the single declared skill by origin and URI, the ambient `launcher` composition, the
  reference-only trees marked `injected: false`, and the composition order and notes that state the
  file is metadata only. It also records the consumers: the pure parser that enforces the declared
  vocabulary, the packaging provider that admits the corpus root and manifest together, the source
  admission that gives the manifest its reserved metadata identity, the install-time corpus anchor,
  and the corpus test. Verified against the committed source at
  `d0c1d1cfa9b576fd117ac2a0c05c5defe0089678`.
