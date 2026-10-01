# composition-manifest.json

## Governing Overview

[MCP package overview](../../../../../../overview.md)

## Purpose

The prose-free **routing metadata** plane of the `l-01-agent-lifecycles` corpus: it maps each of the
ten roles to the core blocks, operation blocks, templates, and criteria catalogs it composes with, and
declares the three routing conditions plus the ambient launcher as a non-role. It carries **no
instruction prose and no copies of any source section** — a consumer reads it to learn *what to
assemble*, never *what the rules are*.

## Code Commentary

### Logic

The manifest's schema is `ar-role-capsule-composition/v1` and its `authority` field states the
load-bearing boundary directly: `skills/l-01-agent-lifecycles/SKILL.md` is the thin router and this file
is routing metadata only, with `skills/` as the authoritative tree.

`role_order` lists exactly the ten roles and must agree with the `roles` object; `routing_conditions`
declares the three conditions in order (`spawn-role-env`, `fresh-session-role-brief`, `ambient-launcher`)
and gives each its `fail_closed_when` case; `launcher` declares `is_role: false` and points its
instruction source at `core/launcher.md`, which is how the corpus keeps the launcher a routing condition
rather than an invented role.

`operations` declares the **frozen nine-name vocabulary** (`orientation`, `planning`,
`implementation`, `review`, `curation`, `coordination`, `authorized-closeout`, `recovery`,
`bootstrap`) with each entry's source file, purpose, and `applies_to_roles`. An operation outside that
set is an explicit error, never a silent fallback. `core` names the six shared blocks; `roles` names
each role's altitude, seat, and its four source lists; `references` marks rationale, rulings, lenses,
criteria, and templates as `injected: false`, so reference material stays out of the normative path.

**The tenth role's entry (added by 260915-CAPS-L13).** `roles.bootstrap` declares
`"altitude": "free-agent"` — the only role whose altitude is not a task altitude — with `seat`
describing the first-hour setup seat, three operations (`orientation`, `bootstrap`, `recovery`), the
three shared core blocks, five requested tools, and empty `templates` and `criteria` lists. The
`operations.bootstrap` entry names `operations/bootstrap.md` and `applies_to_roles: ["bootstrap"]`, so
exactly one role carries it. Both additions are **appends**: `bootstrap` is last in `role_order` and
last in `operations`, so no pre-existing index, settings key, or projection addressed to an earlier
role shifts because it was added.

`composition_order` fixes assembly as **core → role → operation → repository-specialization**, and the
`notes` array restates the three anti-duplication rules: no prose here, exactly one source per
instruction, and task facts travelling as a separate context channel.

**Declared capability metadata (added by 260915-CAPS-L2).** The routing plane now also declares
*what each seat asks for*, which is a different thing from *what it is permitted*. The manifest
gained **41 keys and lost none** against the file L1 shipped: a new top-level `skills` object, a
per-role `tools` array and `skills` array, and a `launcher.operations` list.

- **`skills`** (top level, **new**) — the declared skill registry, keyed by skill name. The one
  entry is `l-01-agent-lifecycles` = `{"origin": "agents-remember/skills", "uri":
  "skill://agents-remember/skills/l-01-agent-lifecycles", "source": "SKILL.md"}`. Identity is
  **origin plus skill name**, because a bare name collides across servers; `source` names the
  skill's root instruction file, whose content digest is what a reference's `revision` means. A
  bare `skills: ["l-01-agent-lifecycles"]` on a role is therefore a *pointer into this registry*,
  not a name that stands alone.
- `roles.<role>.tools` — the tool identities the role's compiled capsule requests. **32 ids across
  the ten roles, 18 distinct** (the tenth role contributes five: `runtime_install`, `memory_init`,
  `memory_baseline_status`, `memory_baseline_adopt`, `provider_status`). Every one is held against the
  published tool roster by the shipped check, so a typo is an error rather than an inert request. They
  are **requests, not grants**: the
  compiler narrows them against the admitted `CapsuleToolPolicy` snapshot and refuses an id outside
  it. A role-to-tool table authored in Python instead would be a second source of truth about a
  role — exactly what this corpus's one-source-per-instruction rule forbids — and in
  `application/` it would read as a grant rather than a request.
- `roles.<role>.skills` — **one skill reference per role**, each pointing into the registry above.
  **This channel is carried, not narrowed**: the compiler builds a content-addressed reference
  (`origin`, `identity`, `uri`, `revision`) and consults **no** permission policy, because a skill
  reference points at separately delivered content rather than asking for a capability. Do not
  describe it as narrowed or granted.
- `launcher.operations` — `[]` became `["orientation", "coordination"]`. This is the one addition
  the compiler relies on: without it the launcher seat has no permitted operation, and **every
  launcher compilation is refused `operation-not-applicable` by design.**

These key families are what a role capsule returns as its separately typed requested-tool
identities and optional skill references, so the compiler can obey that requirement without
inventing a second authority. A declared skill's root file must be admitted, or its revision would
be a fiction; both the metadata plane and the compiled plane fail closed.

### Conventions

Edit the canonical `skills/l-01-agent-lifecycles/composition-manifest.json` and let
`scripts/sync-skills.py` propagate it. A new operation name or a role source that does not exist is
rejected by the shipped check rather than tolerated. `tools` and `skills` are treated as
**optional** by the parser, so their presence is additive and removing them leaves a manifest that
still parses and compiles for every role (returning no requests and no skill references).

### Invariants And Boundaries

- This file is metadata, not doctrine: adding prose here duplicates a rule that already has one home.
- The operation vocabulary is closed at nine names; the role registry is closed at ten roles.
- **The tenth role is a free agent.** `roles.bootstrap` carries `"altitude": "free-agent"`, which is
  not a task altitude, and its `operations` list is the only one containing `bootstrap`. Adding a task
  altitude to it, or letting a second role claim that operation, is a corpus design change rather than
  a metadata tidy.
- Every `source`, `file`, template, and criteria path it names must exist — a missing source is an error,
  not a skip.
- Exactly one source per instruction; `core/` is authored once and a role file never restates a shared
  rule.
- The launcher is `is_role: false` and has no entry under `roles`.
- **A declared tool identity is a request, never a permission.** This file says what a role asks
  for; the admitted `CapsuleToolPolicy` snapshot says what is permitted. Do not merge the two
  authorities, and do not treat this file as a policy source.
- Every declared tool id must exist in the published tool roster, and every declared source path
  must exist on disk. The shipped check is what holds both.
- `tools`, `skills` and `launcher.operations` are additive and independently removable; the
  compiler must not require them for any role that declares none. `launcher.operations` is the
  documented exception with a behavioral consequence: reverting it to `[]` makes every launcher
  compilation refuse `operation-not-applicable`.
- A generated copy is never hand-edited. This card documents the packaged copy; its content is
  byte-identical to the canonical source (all ten copies share one sha256).
- **The skill channel is carried, not narrowed.** `skills.<name>` declares `origin`/`uri`/`source`,
  and a role's `skills` entry is a pointer into that registry. The compiler consults no permission
  policy for a skill reference, so describing one as narrowed, permitted, or granted is wrong. What
  *is* enforced is that each declared skill's root `source` file must be admitted, or its revision
  would be a fiction.
- A skill name in `roles.<role>.skills` must resolve in the top-level `skills` object. An
  unresolvable declaration is refused (`_require_role_skills_are_declared`), never dropped.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

No relevant documentation found after checking live sources.

### Repo-Internal References

The manifest is consumed by the deterministic capsule compiler through the package
`agents_remember.models.role_capsules`; the rows below are the consuming seams and the shipped
guards that hold this file's declarations true.

- The manifest resolves every role and operation source and keeps the registry at ten roles. [1]
- A manifest entry pointing at a missing source, an unknown operation, an unknown core block, or a missing criteria catalog is reported instead of silently accepted. [2]
- The canonical source of this metadata plane. [3]
- Declared tool identities are **requests** narrowed against the admitted policy snapshot, never grants; an id outside it is refused. [4]
- **The declared skill registry and the skill entry shape** — the parser that turns `skills.<name>` into `CapsuleSkillEntry`. [5]
- **Skill references are carried, not narrowed.** [6]
- A declared skill must resolve in the registry, and its root file must be admitted. [7]
- The parser treats `tools` and `skills` as optional and refuses a manifest that disagrees with the frozen vocabulary. [8]
- Every tool id this plan declares exists in the published roster — the guard that makes a typo an error rather than an inert request. [9]
- The plan still parses and compiles for every role with `tools`/`skills` absent, and emptying `launcher.operations` refuses instead of compiling — the launcher's own case, the one that replaced the older launcher-refusal case this row used to name. [10]
- The plan still parses and compiles for every role with `tools`/`skills` absent, and the launcher refusal is `operation-not-applicable` when `launcher.operations` is empty. [11]
- The carried skill channel against the shipped corpus: one reference per declaration, revision follows the admitted bytes. [12]
- The L13 additions as the compiler reads them: the tenth role's source, altitude and single-carrier operation. [13]

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.
