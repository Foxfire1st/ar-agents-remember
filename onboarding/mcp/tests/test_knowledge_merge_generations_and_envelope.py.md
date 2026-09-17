# mcp/tests/test_knowledge_merge_generations_and_envelope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_merge_generations_and_envelope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T22:00+02:00 |
| lastVerifiedCommitHash | `4904e08f0668ed6d11a2c44d0118716bb82f735c` |
| lastVerifiedCommitDate | 2026-09-17T22:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](../overview.md)

## Purpose

The case module for what generation 2 makes possible and what it must refuse: the mixed-generation merge preflight,
the typed record envelope's payload seam, and the route scope's confinement and acyclicity. Three requirement groups
share one file because they share one subject — generation 2 — and its docstring names them: **6.1/6.2** (the preflight
reads each input's generation first, refuses a mixed-generation merge before any session exists, and validates a
same-generation merge against the generation the inputs agree on), **3.1** (one registry maps a `(kind, record_schema)`
pair to one frozen model and one entry point decides admissibility), and **4.2/4.3** (a route path is normalised and
confined, and the hierarchy is acyclic with the check running inside the caller's transaction). This is one of the
leaf's own new test modules.

## Code Commentary

### Logic

The module declares `MERGE_OPERATION = "merge_knowledge_datasets"` and `pytestmark = pytest.mark.evidence_unit`, and
imports the merge preflight (`declared_generation`, `selected_generation`, `require_supported_structure`), the payload
seam, the two route rules, and `create_generation_1_store` from the shared support module.

- `_v1_dataset` creates one genuine version-1 dataset bound to a caller-supplied repository namespace. Its docstring
  gives the reason the caller supplies it: the three positions of one merge share a namespace, so three datasets bound
  to three different namespaces are not a merge of one dataset's branches, and their repository rows would show up as a
  difference that has nothing to do with the generation.
- `test_a_version_1_merge_on_the_generation_2_build_selects_generation_1` is the required **passing** case and the one
  a partially threaded preflight breaks. All three inputs declare version 1, `declared_generation(base)` and
  `selected_generation` both resolve to generation 1, each input validates against generation 1's manifest through
  `require_supported_structure(..., generation=GENERATION_1)`, and `build_delta(left, base, side="left",
  generation=GENERATION_1)` reports operation counts over exactly generation 1's ten tables with an empty delta. With
  the live globals left in place, the same merge would ask for `route`, `knowledge_record` and `record_revision` and be
  refused.
- `test_a_mixed_generation_merge_is_refused_before_any_session_exists` builds two version-1 inputs and one
  generation-2 input and asserts the refusal's code `schema_mismatch`, its operation, its `(expected, observed)` pair
  `("1", "2")`, and that the detail names the disagreeing position and the base. It then proves the preflight is
  read-only: both inputs are byte-identical afterwards and a second attempt refuses again.
- `test_a_generation_2_merge_on_the_generation_2_build_selects_generation_2` shows the same mechanism serving the
  newest generation: agreement selects `CURRENT_GENERATION`, each input validates against it, and a read-only reader
  sees an empty `route` table in the logical body.
- `test_the_payload_seam_registers_one_shape_and_refuses_every_inadmissible_payload` asserts the registry entry exists,
  that a valid payload round-trips to `{"note": "conformance"}`, and that the validated value is **frozen** (assignment
  raises). Five inadmissible combinations are then measured — an unknown kind, a schema not admissible for a known
  kind, an empty note, an extra field, and a missing field — each returning a `KnowledgeRefusal` with code
  `invalid_payload`, table `record_revision` and the supplied `record_id`.
- `test_a_confined_route_path_normalises_to_itself` and `test_a_route_path_outside_the_admitted_form_is_refused` are the
  two directions of requirement 4.2: four admitted spellings normalise to themselves, and eleven refused spellings
  (empty, absolute, traversal, dot segment, doubled separator, backslash, drive form, two UNC spellings, trailing
  separator, embedded NUL) each return a refusal whose table is `route` and whose `observed` is the exact input.
- `test_the_route_hierarchy_is_acyclic_and_a_cycle_rolls_the_batch_back` measures both directions of 4.3 on a real
  generation-2 schema: a chain and a two-root forest pass, a three-node cycle introduced inside an explicit `BEGIN`
  returns a `lineage_cycle` refusal naming a route in the cycle, the subsequent `ROLLBACK` restores the hierarchy the
  walk passed on, and the **one-node** cycle is the table's own `CHECK`, raising `apsw.ConstraintError` instead of
  reaching the walk.
- `test_the_gen_2_record_tables_carry_no_competing_identity_and_the_association_is_a_constraint` asserts the
  generation-2 facts behind 3.3 and 4.4: the envelope's columns contain none of `content_digest`, `logical_digest` or
  `fingerprint`, `payload` is a declared column and a typed-JSON column of `record_revision`, the three governing-route
  joins key on the governed entity's own id, no generation-1 table carries `governing_route_id`, and no create statement
  starts with `ALTER TABLE`.

### Conventions

- Each case measures **both directions** where a rule has a passing and a failing form; the module docstring states why
  (a check observed only in the passing direction is not evidence).
- Version-1 datasets always come from the shared support module, and generation-2 datasets from the real creation path
  with foreign keys enabled.
- Refusal assertions address the structured facts a caller branches on (code, operation, table, expected/observed,
  detail content) rather than message text.
- Parametrized refusal tables carry the exact offending spelling so a failure names the form that regressed.

### Invariants And Boundaries

- **A mixed-generation merge is refused before any session exists and picks no winner**, and the refusal leaves both
  inputs byte-identical — the case proves input preservation by comparing file bytes, not by re-reading the refusal.
- **The passing case is the load-bearing one.** A v1/v1/v1 merge on the generation-2 build must proceed *under
  generation 1* and attach generation 1's ten tables; the docstring records that this is exactly what a partially
  threaded preflight breaks, which is requirement 5.1 broken by the mechanism meant to serve it.
- **Route scope is recorded, never inferred.** The confinement cases admit only the normalised spelling and refuse a
  path that would need normalising rather than rewriting it; the acyclicity case refuses however the cycle arrives, not
  only through the authoring path.
- **The envelope must not become a second identity authority**, which is why the case asserts the *absence* of any
  identity-valued column on it; the payload lives on the revision with `json_valid`, and the governing association is a
  generation-2 table keyed by the governed row rather than a new column on a generation-1 table.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The three requirement groups the module covers and why they share one file. | "what generation 2 makes possible and what it must refuse" | mcp/tests/test_knowledge_merge_generations_and_envelope.py:1-15 |
| The one-namespace helper for the three merge positions, and why the caller supplies the namespace. | `_v1_dataset` | mcp/tests/test_knowledge_merge_generations_and_envelope.py:58-69 |
| The required passing case: a version-1 merge on the generation-2 build selects generation 1 and attaches generation 1's ten tables. | `test_a_version_1_merge_on_the_generation_2_build_selects_generation_1` | mcp/tests/test_knowledge_merge_generations_and_envelope.py:72-102 |
| A mixed-generation merge refuses before any session exists, names the disagreeing input, and leaves both files byte-identical. | `test_a_mixed_generation_merge_is_refused_before_any_session_exists` | mcp/tests/test_knowledge_merge_generations_and_envelope.py:105-135 |
| The same mechanism selects the newest generation when the inputs agree. | `test_a_generation_2_merge_on_the_generation_2_build_selects_generation_2` | mcp/tests/test_knowledge_merge_generations_and_envelope.py:138-166 |
| One registry, one entry point, a frozen validated value, and five inadmissible payloads refused with the shipped code. | `test_the_payload_seam_registers_one_shape_and_refuses_every_inadmissible_payload` | mcp/tests/test_knowledge_merge_generations_and_envelope.py:169-197 |
| Confinement measured in both directions, with the refused spelling carried in the refusal's `observed`. | `test_a_confined_route_path_normalises_to_itself`; `test_a_route_path_outside_the_admitted_form_is_refused` | mcp/tests/test_knowledge_merge_generations_and_envelope.py:200-205; mcp/tests/test_knowledge_merge_generations_and_envelope.py:208-230 |
| Acyclicity measured in both directions, including the rollback and the one-node cycle the table's own CHECK catches. | `test_the_route_hierarchy_is_acyclic_and_a_cycle_rolls_the_batch_back` | mcp/tests/test_knowledge_merge_generations_and_envelope.py:233-284 |
| The generation-2 DDL facts: no identity column on the envelope, payload on the revision, the joins keyed by the governed row, no altered generation-1 table. | `test_the_gen_2_record_tables_carry_no_competing_identity_and_the_association_is_a_constraint` | mcp/tests/test_knowledge_merge_generations_and_envelope.py:287-311 |
| The merge preflight the generation cases drive: per-input generation, agreement selection, and structural validation against the selected generation. | `declared_generation`; `selected_generation`; `require_supported_structure` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:94; mcp/src/agents_remember/memory/knowledge/merge_schema.py:110; mcp/src/agents_remember/memory/knowledge/merge_schema.py:230 |
| The delta builder the passing case calls with an explicit generation, and the empty-delta fact it asserts. | `build_delta` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:190 |
| The payload seam: registry, entry point and the refusal it returns. | `PAYLOAD_MODELS`; `validate_record_payload`; `INTERNAL_CONFORMANCE_KIND` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:57-59; mcp/src/agents_remember/memory/knowledge/record_envelope.py:69-113; mcp/src/agents_remember/memory/knowledge/record_envelope.py:38 |
| The two route rules the module exercises. | `normalize_route_path`; `require_acyclic_routes` | mcp/src/agents_remember/memory/knowledge/routes.py:75-89; mcp/src/agents_remember/memory/knowledge/routes.py:92-144 |
| The generation-2 declarations the DDL case reads as facts. | `APPENDED_TABLE_DDL`; `APPENDED_PRIMARY_KEYS`; `APPENDED_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:103-201; mcp/src/agents_remember/memory/knowledge/schema_v2.py:81-88; mcp/src/agents_remember/memory/knowledge/schema_v2.py:51-76 |
| The genuine version-1 datasets the merge cases use. | `create_generation_1_store` | mcp/tests/generation_test_support.py:34-54 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-17T22:00+02:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`; the module is untracked in the leaf's code worktree): created this one-to-one card for the leaf's new merge/envelope/route case module. It records the required passing case a partially threaded preflight breaks, the byte-identical input preservation a refusal must leave behind, the both-directions rule for the pin-like checks, the five inadmissible payloads, and the generation-2 DDL facts the module asserts as absences as well as presences.
