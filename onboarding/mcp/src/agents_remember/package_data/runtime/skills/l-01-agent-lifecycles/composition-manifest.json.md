# composition-manifest.json

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/composition-manifest.json` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `3054af87fdf0e21e9ec7132a5d62ba0d514600ba` |
| lastVerifiedCommitDate | 2026-09-16T08:23:52+02:00|
| governingOverview      | `../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../overview.md)

## Purpose

The prose-free **routing metadata** plane of the `l-01-agent-lifecycles` corpus: it maps each of the
nine roles to the core blocks, operation blocks, templates, and criteria catalogs it composes with, and
declares the three routing conditions plus the ambient launcher as a non-role. It carries **no
instruction prose and no copies of any source section** — a consumer reads it to learn *what to
assemble*, never *what the rules are*.

## Code Commentary

### Logic

The manifest's schema is `ar-role-capsule-composition/v1` and its `authority` field states the
load-bearing boundary directly: `skills/l-01-agent-lifecycles/SKILL.md` is the thin router and this file
is routing metadata only, with `skills/` as the authoritative tree.

`role_order` lists exactly the nine roles and must agree with the `roles` object; `routing_conditions`
declares the three conditions in order (`spawn-role-env`, `fresh-session-role-brief`, `ambient-launcher`)
and gives each its `fail_closed_when` case; `launcher` declares `is_role: false` and points its
instruction source at `core/launcher.md`, which is how the corpus keeps the launcher a routing condition
rather than a tenth role.

`operations` declares the **frozen eight-name vocabulary** (`orientation`, `planning`,
`implementation`, `review`, `curation`, `coordination`, `authorized-closeout`, `recovery`) with each
entry's source file, purpose, and `applies_to_roles`. An operation outside that set is an explicit
error, never a silent fallback. `core` names the six shared blocks; `roles` names each role's altitude,
seat, and its four source lists; `references` marks rationale, rulings, lenses, criteria, and templates
as `injected: false`, so reference material stays out of the normative path.

`composition_order` fixes assembly as **core → role → operation → repository-specialization**, and the
`notes` array restates the three anti-duplication rules: no prose here, exactly one source per
instruction, and task facts travelling as a separate context channel.

### Conventions

Edit the canonical `skills/l-01-agent-lifecycles/composition-manifest.json` and let
`scripts/sync-skills.py` propagate it. A new operation name or a role source that does not exist is
rejected by the shipped check rather than tolerated.

### Invariants And Boundaries

- This file is metadata, not doctrine: adding prose here duplicates a rule that already has one home.
- The operation vocabulary is closed at eight names; the role registry is closed at nine roles.
- Every `source`, `file`, template, and criteria path it names must exist — a missing source is an error,
  not a skip.
- Exactly one source per instruction; `core/` is authored once and a role file never restates a shared
  rule.
- The launcher is `is_role: false` and has no entry under `roles`.

### Todos

None recorded.

## Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| The manifest resolves every role and operation source and keeps the registry at nine roles. | `test_manifest_resolves_every_role_and_operation_source`; `ROLE_ORDER`; `OPERATION_KEYS` | mcp/tests/test_role_instruction_corpus.py:199-225; mcp/tests/test_role_instruction_corpus.py:32-42; mcp/tests/test_role_instruction_corpus.py:56-64 |
| A manifest entry pointing at a missing source, an unknown operation, an unknown core block, or a missing criteria catalog is reported instead of silently accepted. | `test_manifest_reports_a_missing_source_instead_of_accepting_it` | mcp/tests/test_role_instruction_corpus.py:291-329 |
| The canonical source of this metadata plane. | `"schema": "ar-role-capsule-composition/v1"` | skills/l-01-agent-lifecycles/composition-manifest.json:1-4 |

## Cross-Repo References

No sibling-repository contract defines this instruction file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: created this card for `skills/l-01-agent-lifecycles/composition-manifest.json` — a file added by the role-instruction corpus consolidation. The canonical source is It is the routing-metadata plane the deterministic capsule compiler (a later leaf) selects from.; the packaged copy is produced by `scripts/sync-skills.py` and is not hand-edited. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
