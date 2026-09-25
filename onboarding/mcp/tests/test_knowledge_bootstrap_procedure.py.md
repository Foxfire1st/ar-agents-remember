# mcp/tests/test_knowledge_bootstrap_procedure.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_bootstrap_procedure.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T12:20:00+02:00 |
| lastVerifiedCommitHash | `09329a7ee598920c519b06305b73ba8e48d72c88` |
| lastVerifiedCommitDate | 2026-09-26T00:58:43+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

**The curator-led knowledge bootstrap is protected as four separately failable readings, not as one
document-exists assertion.** The module's subject is the delivery `260921-ICR-L27` makes of
`ICR-R27@v1`: a repository whose first knowledge is being written has no leaf and no enclosure
contract, and before this leaf the only shipped instruction that authored knowledge was the leaf route
(`agents-remember knowledge-ingest`), which requires one. So first-time creation had no operational
process at all.

The reading is deliberately split, because the ways the delivery can be false are independent:

- the **procedure** exists and is **served** — a fresh session discovers it through the shipped skill
  catalog, and the bytes it reads are the canonical tree's bytes, so a stale or hand-edited copy is
  indistinguishable from shipping the wrong instruction;
- the **commands the procedure prints** exist on the shipped command line, and every option printed
  belongs to the subcommand it is printed with — the requirement's own named failure, "a document that
  describes commands which do not exist", caught mechanically;
- the **seats** the procedure names are admitted by the shipped **opener**, measured at the route
  rather than read off the policy constant, because the launch *compiler* accepts any declared role
  while the *opener* admits a session with no task document only for the taskless seat roles;
- the instructions that **are** delivered name the procedure — to the seat the opener admits taskless,
  to the curator shape the compiler produces, and through the two served skills an ordinary setup
  follows.

**The subject is instruction identity, not behaviour.** Nothing here drives a live curator session or
writes knowledge; the module grades what is published, what parses, and which session shapes the
product actually admits. `test_the_compiled_curator_shape_names_the_procedure_it_would_receive` is
named for the **compiler** for exactly that reason: it measures the compiled instructions of the
curator shape, not an admission, and the route-level cases next to it are what measure admission.

## Code Commentary

### 260921-ICR-L27 The Module That Pins The Delivered Entries — And The Base Defect It Reproduces

**The case set, and what defends what.** Seven cases, four readings:

| Reading | Case |
| --- | --- |
| the seat gate, by observed status | `test_the_opener_admits_exactly_the_taskless_seat_roles_and_instructs_each` |
| the admitted taskless seat reaches the foundation | `test_the_admitted_taskless_seat_receives_the_foundation_step` |
| the curator's own seat opens on a task document | `test_the_curator_seat_opens_on_a_task_document_and_taskless` |
| the served catalog publishes the procedure, bytes compared with `skills/` | `test_the_served_catalog_publishes_the_bootstrap_procedure` |
| every printed invocation resolves in the shipped parser | `test_every_invocation_the_procedure_prints_resolves_in_the_shipped_parser` |
| the compiled curator shape names the procedure | `test_the_compiled_curator_shape_names_the_procedure_it_would_receive` |
| the two served setup/onboarding skills name it | `test_the_served_setup_and_onboarding_surfaces_reach_the_procedure` |

**Why the seat reading is a route case and not a string case.** An earlier revision of this module
asserted only that the compiled capsule for a taskless curator names the procedure, while the shipped
opener refuses that session with `400 task-binding-required` — a session that never opens has no first
prompt, so nothing is handed over. The three route cases replaced that: they drive the dashboard's own
open route over the shipped `_scratch_world` and assert the **observed status per role**, with the
admitted arms as the control. `test_the_curator_seat_opens_on_a_task_document_and_taskless` is the other half
— the curator opens **with** a named role scope and receives the procedure.

**The parser case grades both halves at once and executes nothing.** Each invocation the procedure
prints is filled from `PLACEHOLDER_VALUE` and run through the real `build_parser()`: the subcommand must
be declared, and every printed option must belong to that subcommand. An option that moved to another
subcommand is the shape a reorganisation produces and is caught here. The placeholder only has to
satisfy the parser's arity, never a real path.

**The base defect is reproduced rather than asserted.** On the leaf's base
`06ed70cfcde7e3860ee5b53435727e7512e4335c` the module fails **5 cases and passes 2**; on the candidate
it is **7 passed**. The two base-passing cases are the seat gate itself — the measurement that
constrained the correction — and the report discloses that rather than presenting them as delivered
work. That is the right way round: a case that passes on base cannot be evidence that the leaf
delivered anything.

**The world is the shipped one, not a fixture invented here.** The module imports `LEAF_REF`,
`_scratch_world` and `_write_codex_settings` from the shipped launch-wiring module, so the coordination
root, task document, enclosure contract, code worktree and external memory root it opens seats over are
the real ones. `pytestmark = pytest.mark.evidence_unit` places the module in the evidence-unit lane, and
its census rows are the three consumer-row additions this leaf makes to
`mcp/tests/evidence-lifecycle.toml` and `mcp/tests/test-evidence-lanes.toml`.

### Invariants And Boundaries

- The module grades instruction identity, parsing and admission — never a knowledge write and never a
  live curator session.
- Every case must fail on the leaf's base or be explicitly disclosed as a base-passing control.
- Served content is compared with the canonical tree rather than trusted; a copy that drifted is a
  failure, not a variation.
- The launch world comes from the shipped wiring module; no parallel fixture is invented.

### Todos

No open file-local todos.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is needed to prove this test module's contract. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's subject is the *authored* knowledge foundation and the missing first-time process, and its four readings are deliberately kept apart. | "A repository's knowledge foundation is *authored*"; "the **procedure** exists and is served"; "the **commands the procedure prints** exist"; "the **seats** the procedure names are admitted by the shipped opener" | mcp/tests/test_knowledge_bootstrap_procedure.py:1-40 |
| The constants bind the case to the canonical tree: the skill name and the file whose bytes a served read is compared against. | `PROCEDURE_SKILL`; `PROCEDURE_FILE`; `CANONICAL_SKILLS` | mcp/tests/test_knowledge_bootstrap_procedure.py:108-110 |
| The printed-invocation grammar is a line that *opens* with the program name, so an inline mention inside a sentence is prose rather than a command line. | `PROGRAM`; `_INVOCATION`; `_PLACEHOLDER` | mcp/tests/test_knowledge_bootstrap_procedure.py:113-113; mcp/tests/test_knowledge_bootstrap_procedure.py:117-117; mcp/tests/test_knowledge_bootstrap_procedure.py:120-120 |
| The placeholder is filled only to satisfy the parser's arity, because the case grades the command line's shape and runs no command. | `PLACEHOLDER_VALUE` | mcp/tests/test_knowledge_bootstrap_procedure.py:124-124 |
| The served route reads a published skill body through the catalog's own read entry point rather than from `skills/` directly. | `served_body` | mcp/tests/test_knowledge_bootstrap_procedure.py:171-192 |
| The compiled free-agent instructions for a role are obtained through the launch compiler's own shape. | `free_agent_instructions` | mcp/tests/test_knowledge_bootstrap_procedure.py:194-225 |
| The cases open seats over the shipped scratch world and compare the observed status per role. | `open_seat`; `test_the_opener_admits_exactly_the_taskless_seat_roles_and_instructs_each` | mcp/tests/test_knowledge_bootstrap_procedure.py:269-353 |
| The one seat the product admits without a task document **and** instructs about the foundation is the bootstrap seat. | `test_the_admitted_taskless_seat_receives_the_foundation_step` | mcp/tests/test_knowledge_bootstrap_procedure.py:298-328; mcp/tests/test_knowledge_bootstrap_procedure.py:354-354 |
| The curator's own seat opens with a named role scope and receives the procedure, which is the other half of the seat gate. | `test_the_curator_seat_opens_on_a_task_document_and_taskless` | mcp/tests/test_knowledge_bootstrap_procedure.py:388-417 |
| The served catalog publishes the procedure, and the served bytes are compared with the canonical tree's. | `test_the_served_catalog_publishes_the_bootstrap_procedure` | mcp/tests/test_knowledge_bootstrap_procedure.py:418-440 |
| Every invocation the procedure prints is filled and run through the real parser, grading declaration and option-ownership together without executing anything. | `test_every_invocation_the_procedure_prints_resolves_in_the_shipped_parser`; "The requirement's own failure: a document that describes commands which do not exist." | mcp/tests/test_knowledge_bootstrap_procedure.py:443-469 |
| The curator-shape case measures the **compiler**, which is why it is named for the compiler rather than for an admission. | `test_the_compiled_curator_shape_names_the_procedure_it_would_receive` | mcp/tests/test_knowledge_bootstrap_procedure.py:409-429; mcp/tests/test_knowledge_bootstrap_procedure.py:472-472 |
| The two served skills an ordinary setup follows name the procedure and report the knowledge state. | `test_the_served_setup_and_onboarding_surfaces_reach_the_procedure` | mcp/tests/test_knowledge_bootstrap_procedure.py:494-517 |
| The launch world the route cases drive is the shipped wiring module's own, not a fixture invented here. | `_scratch_world`; `LEAF_REF` | mcp/tests/test_capsule_launch_wiring.py:120-120; mcp/tests/test_capsule_launch_wiring.py:331-353 |
| The module is placed in the evidence-unit lane. | "pytestmark = pytest.mark.evidence_unit" | mcp/tests/test_knowledge_bootstrap_procedure.py:105-105 |

## Cross-Repo References

No sibling repository evidence is needed for this test module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-09-25T22:19:46+00:00: Generated citation repair: `PROCEDURE_SKILL`; `PROCEDURE_FILE`; `CANONICAL_SKILLS` repointed to mcp/tests/test_knowledge_bootstrap_procedure.py:109-109; mcp/tests/test_knowledge_bootstrap_procedure.py:110-110; mcp/tests/test_knowledge_bootstrap_procedure.py:108-108. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `PROGRAM`; `_INVOCATION`; `_PLACEHOLDER` repointed to mcp/tests/test_knowledge_bootstrap_procedure.py:113-113; mcp/tests/test_knowledge_bootstrap_procedure.py:117-117; mcp/tests/test_knowledge_bootstrap_procedure.py:120-120. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `PLACEHOLDER_VALUE` repointed to mcp/tests/test_knowledge_bootstrap_procedure.py:124-124. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `test_the_served_catalog_publishes_the_bootstrap_procedure` repointed to mcp/tests/test_knowledge_bootstrap_procedure.py:418-440. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `test_every_invocation_the_procedure_prints_resolves_in_the_shipped_parser`; "The requirement's own failure: a document that describes commands which do not exist." repointed to mcp/tests/test_knowledge_bootstrap_procedure.py:443-469; mcp/tests/test_knowledge_bootstrap_procedure.py:444-444. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `test_the_served_setup_and_onboarding_surfaces_reach_the_procedure` repointed to mcp/tests/test_knowledge_bootstrap_procedure.py:494-517. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `_scratch_world`; `LEAF_REF` repointed to mcp/tests/test_capsule_launch_wiring.py:331-353; mcp/tests/test_capsule_launch_wiring.py:120-120. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "pytestmark = pytest.mark.evidence_unit" repointed to mcp/tests/test_knowledge_bootstrap_procedure.py:105-105. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **body update — the false taskless-curator sentences are corrected (D56, and F1 of the leaf's round-one verdict, which was `blocking`).** Four copies of the claim are gone: the module docstring's bullet, a docstring citing a case name that no longer existed after the rename, the bootstrap-seat case's "the one seat" sentence, and the curator-shape case's docstring; every case-name reference in the module now resolves. **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T12:20:00+02:00 — 260921-ICR-L27 curator (uncommitted change set on `ar/260921-icr-l27-ar`, code base `06ed70cfcde7e3860ee5b53435727e7512e4335c`): **created** for the leaf's new test module (453 L, seven cases). The card records the four readings the module keeps apart, and states plainly which half each case measures — in particular that `test_the_compiled_curator_shape_names_the_procedure_it_would_receive` measures the **compiler** and not an admission, the correction the independent re-verification required after the round-one `blocking` verdict found the module's own name and docstring claiming a session-level delivery while the shipped opener refused that session. It also records the base reproduction (5 failed / 2 passed on base, 7 passed on the candidate) with the two base-passing cases named as the seat gate that constrained the correction rather than as delivered work. No verification stamp is advanced as a commit: the candidate is uncommitted, so the header's pair is the leaf's base commit plus this working-tree delta, and the governed closeout owns the real stamp.
