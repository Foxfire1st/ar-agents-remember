# composition-manifest.json

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/composition-manifest.json` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T09:38+02:00 |
| lastVerifiedCommitHash | `0dd1df9a950d59ac9622e5fb54250e528df08fa5` |
| lastVerifiedCommitDate | 2026-09-16T20:47:18+02:00|
| governingOverview      | `../../../../../../overview.md` |

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

## Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

The manifest is consumed by the deterministic capsule compiler through the package
`agents_remember.models.role_capsules`; the rows below are the consuming seams and the shipped
guards that hold this file's declarations true.

| Finding | Anchor | Source |
| --- | --- | --- |
| The manifest resolves every role and operation source and keeps the registry at ten roles. | `test_manifest_resolves_every_role_and_operation_source`; `ROLE_ORDER`; `OPERATION_KEYS` | mcp/tests/test_role_instruction_corpus.py:248-300; mcp/tests/test_role_instruction_corpus.py:32-43; mcp/tests/test_role_instruction_corpus.py:59-69 |
| A manifest entry pointing at a missing source, an unknown operation, an unknown core block, or a missing criteria catalog is reported instead of silently accepted. | `test_manifest_reports_a_missing_source_instead_of_accepting_it` | mcp/tests/test_role_instruction_corpus.py:468-507 |
| The canonical source of this metadata plane. | `"schema": "ar-role-capsule-composition/v1"` | skills/l-01-agent-lifecycles/composition-manifest.json:1-4 |
| Declared tool identities are **requests** narrowed against the admitted policy snapshot, never grants; an id outside it is refused. | `narrow_tool_requests` | mcp/src/agents_remember/models/role_capsules/tools.py:24-58 |
| **The declared skill registry and the skill entry shape** — the parser that turns `skills.<name>` into `CapsuleSkillEntry`. | `CapsuleSkillEntry`; `_parse_skills` | mcp/src/agents_remember/models/role_capsules/manifest.py:94-110; mcp/src/agents_remember/models/role_capsules/manifest.py:455-478 |
| **Skill references are carried, not narrowed.** | `skill_references`; `skills_declared_identity` | mcp/src/agents_remember/models/role_capsules/compiler.py:154-193; mcp/src/agents_remember/models/role_capsules/sources.py:126-138 |
| A declared skill must resolve in the registry, and its root file must be admitted. | `_require_role_skills_are_declared`; `_require_declared_skills_present` | mcp/src/agents_remember/models/role_capsules/manifest.py:479-508; mcp/src/agents_remember/models/role_capsules/source_set.py:195-228 |
| The parser treats `tools` and `skills` as optional and refuses a manifest that disagrees with the frozen vocabulary. | `parse_composition_manifest`; `CapsuleRoleEntry` | mcp/src/agents_remember/models/role_capsules/manifest.py:168-216; mcp/src/agents_remember/models/role_capsules/manifest.py:63-82 |
| Every tool id this plan declares exists in the published roster — the guard that makes a typo an error rather than an inert request. | `test_every_tool_the_shipped_manifest_requests_exists_in_the_public_roster` | mcp/tests/test_role_capsule_admission.py:221-230 |
| The plan still parses and compiles for every role with `tools`/`skills` absent, and the launcher refusal is `operation-not-applicable` when `launcher.operations` is empty. | `test_every_shipped_role_compiles_deterministically_under_every_declared_operation`; `test_launcher_is_refused_an_operation_no_role_inherits_to_it`; `test_emptying_the_launcher_operations_refuses_instead_of_compiling` | mcp/tests/test_role_capsule_admission.py:520-602; mcp/tests/test_role_capsule_compiler.py:548-560; mcp/tests/test_role_capsule_admission.py:765-818 |
| The carried skill channel against the shipped corpus: one reference per declaration, revision follows the admitted bytes. | `test_every_shipped_role_that_declares_a_skill_carries_one_reference_per_declaration`; `test_the_skill_revision_follows_the_admitted_skill_bytes` | mcp/tests/test_role_capsule_admission.py:605-655; mcp/tests/test_role_capsule_admission.py:659-694 |
| The L13 additions as the compiler reads them: the tenth role's source, altitude and single-carrier operation. | `"altitude": "free-agent"`; `"applies_to_roles"` | skills/l-01-agent-lifecycles/composition-manifest.json:451-477; skills/l-01-agent-lifecycles/composition-manifest.json:127-135 |

## Cross-Repo References

No sibling-repository contract defines this instruction file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-16T17:59+02:00 — 260915-CAPS-L13 curator: **body rebased on the corpus's tenth role**
  (`CAPS-R13@v1`). `role_order` is now ten roles and `operations` nine names, so the Purpose, the
  Logic's two enumerations, the tool census (27 ids across nine roles / 14 distinct → **32 across ten
  / 18 distinct**, the tenth contributing five) and the closed-registry invariant were all corrected.
  Added the tenth role's entry as its own Logic paragraph — `altitude: "free-agent"` (the only
  non-task altitude), three operations with `bootstrap` unique to it, and empty `templates`/`criteria`
  — plus the append-not-insert property that keeps earlier roles' positions stable, and the free-agent
  invariant. **This card's Repo-Internal section had lost its `| Finding | Anchor | Source |` header
  row**, so its rows were rendering as prose; the header and delimiter are restored and every range
  re-derived, and three stale case names were replaced with the cases that actually exist
  (`test_every_shipped_role_compiles_deterministically_under_every_declared_operation`,
  `test_launcher_is_refused_an_operation_no_role_inherits_to_it`). Verification metadata is left at
  the leaf base commit because the source is uncommitted — the governed closeout stamps the real code
  commit.

- 2026-09-16T09:38+02:00 — 260915-CAPS-L2 curator: corrected against the A3 candidate, which grew this change. The diff against L1's shipped file is now **41 keys added, 0 removed, 0 values changed** (was 38) because the manifest gained a **new top-level `skills` object** declaring the skill registry — `l-01-agent-lifecycles` = `{origin: "agents-remember/skills", uri: "skill://agents-remember/skills/l-01-agent-lifecycles", source: "SKILL.md"}`. Documented that registry and the `CapsuleSkillEntry` shape it parses into, and corrected this card's central distinction: the previous entry called all three key families "declared requests, never grants" and leaned on the tool-narrowing rule. That is right for `tools` and **wrong for `skills`** — a skill reference is **carried**, `skill_references` consults no policy, and identity is `origin + skill` because a bare name collides across servers. Added two invariants (carried-not-narrowed; a skill name must resolve in the registry) and four reference rows, and refreshed every range. The file remains a **cross-leaf change carried by the L2 candidate**, ruled ACCEPTED by the owning seat on 2026-09-16. All ten copies still share one sha256. Verification metadata stays at the leaf base commit — the closeout stamps the real code commit.

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: body updated for the three key families this leaf added to the routing plane. Documented the per-role `tools` array (27 declared ids across the nine roles, 14 distinct, each held against the published roster) and `skills` array (one corpus skill reference per role) as **declared requests, never grants**, and `launcher.operations` changing from `[]` to `["orientation", "coordination"]` — the one addition with a behavioral consequence, since reverting it makes every launcher compilation refuse `operation-not-applicable` by design. Added five invariants (request-versus-permission, roster/source existence, independent removability of the three families, the launcher exception, and the never-hand-edit-the-generated-copy rule) and five Repo-Internal rows. The change is a **cross-leaf change carried by the L2 candidate** — `skills/l-01-agent-lifecycles/composition-manifest.json` is L1's artifact — ruled ACCEPTED by the owning seat on 2026-09-16 after independently reproducing the structural diff (38 keys added, 0 removed, 0 values changed), L1's corpus test (6 passed, unedited) and `scripts/sync-skills.py --check` (exit 0). All ten copies of this file share one sha256. **Governing-link repair:** this card's `governingOverview` and its `## Governing Overview` link were corrected from five steps to **six** (`../../../../../../overview.md`), which is the level that actually resolves to `onboarding/mcp/overview.md` — the `skills/` segment above this directory does not exist, so the card sits five real levels below `onboarding/`, and the five-step form resolved to a nonexistent `onboarding/mcp/src/overview.md`. The same defect and the same repair apply to the sibling `SKILL.md.md` card, which records the correction in its own history; both were found while creating this leaf's cards for this directory. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit.

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: created this card for `skills/l-01-agent-lifecycles/composition-manifest.json` — a file added by the role-instruction corpus consolidation. The canonical source is It is the routing-metadata plane the deterministic capsule compiler (a later leaf) selects from.; the packaged copy is produced by `scripts/sync-skills.py` and is not hand-edited. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
